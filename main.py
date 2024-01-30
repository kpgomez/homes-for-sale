import datetime
import requests
import time

from playwright.sync_api import sync_playwright
from rich.console import Console
from rich.prompt import Prompt

""" 
Manual steps to navigate xome.com and download list of homes for sale
# 1 open https://www.xome.com/Listing/ListingSearch.aspx
# 2 type name of city into search box
# 3 change view to list
# 3 find download button and copy link address
# 4 assign link address to download_url
# 5 download content
"""


def menu():
    choices = ["Irving, TX  0", "Carrollton, TX  1", "Arlington, TX  2", "Coppell, TX  3"]
    for choice in choices:
        console.print(f"{choice[:len(choice)-3]} [blue]{choice[len(choice)-1:]}[/blue]", end=" | ")
    selection = Prompt.ask("\nPlease select city [[blue]0[/blue] for Irving, TX] ")
    choice = choices[int(selection)]
    formatted_city = choice[:len(choice)-3]
    console.print("You have selected [bold underline blue]" + formatted_city + "[/bold underline blue]")
    search_city(formatted_city)


def search_city(city):
    with sync_playwright() as playwright:
        # open chrome and navigate to target pate
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        url = "https://www.xome.com/Listing/ListingSearch.aspx"
        page.goto(url)

        # find search input field and input name of city
        page.locator("#criteria-location-input").fill(str(city))
        time.sleep(5)

        # simulate keyboard actions
        page.keyboard.press("Enter")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")

        # change from map to list view
        page.get_by_title("List view").click()
        time.sleep(5)

        # find download all button called Download All Data
        link = page.get_by_text("Download All Data").get_attribute("href")
        time.sleep(5)

        # pass link to download_file function
        download_file(link, city)


def download_file(link, city):
    home = "https://www.xome.com"
    download_url = f"{home}{link}"
    print(download_url)

    # make API call, added user-agent to prevent 403 error
    req = requests.get(download_url, headers={"User-Agent": "Mozilla/5.0"})

    # context manager to write file to csv
    with open(f"{city}-{datetime.date.today()}.csv", "wb") as file:
        chunks = req.iter_content(chunk_size=8192)
        for chunk in chunks:
            if chunk:
                file.write(chunk)



# TODO
def parse_file():
    ...

# TODO:
# 6 rename file to city + date of download
# 7 parse renamed file
# 8 find mean, mode, min, max
# 9 use streamlit-vizzu module to present data <-- this might take awhile to learn


if __name__ == "__main__":
    console = Console()
    menu()

