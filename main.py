import csv
import time
import requests

from playwright.sync_api import sync_playwright
from rich.console import Console
from rich.prompt import Prompt

# import webbrowser
#
# from bs4 import BeautifulSoup


def menu():
    ...
    # choices = ["Irving, TX - 0", "Carrollton, TX - 1", "Arlington, TX - 2", "Coppell, TX - 3"]
    # for choice in choices:
    #     console.print(f"{choice[:len(choice)-3]} [blue]{choice[len(choice)-3:]}[/blue]", end=" | ")
    # selection = Prompt.ask("\nPlease select city [[blue]0[/blue] for Irving, TX] ")
    # choice = choices[int(selection)]
    # formatted_choice = choice[:len(choice)-3]
    # console.print("You have selected [bold underline blue]" + formatted_choice + "[/bold underline blue]")

    # Manual steps to navigate xome.com and download list of homes for sale
    # 1 open https://www.xome.com/Listing/ListingSearch.aspx
    # 2 type name of city into search box
    # 3 change view to list
    # 3 find download button and copy link address
    # 4 assign link address to download_url
    # 5 download content
    # 6 rename file to city + date of download


def search_city():
    with sync_playwright() as playwright:
        # open chrome and navigate to target pate
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.xome.com/Listing/ListingSearch.aspx")
        # find search input field and input name of city
        page.locator("#criteria-location-input").fill("Irving, TX")
        time.sleep(5)
        # simulate keyboard actions
        page.keyboard.press("Enter")
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")
        # page.keyboard.press("ArrowDown")

        # change from map to list view
        page.get_by_title("List view").click()
        time.sleep(5)

        # find download all button called Download All Data
        link = page.get_by_text("Download All Data").get_attribute("href")
        time.sleep(5)

        # pass link to
        download_file(link)

        # page.get_by_role("button")
        # page.locator(text="").press_sequentially()
        # page.get_by_role("button", {id: "criteria-submit-search"}).click()
        # page.locator("criteria-submit-search").press("Enter")
        # page.get_by_label("Search").fill("Irving, TX")
        # page.keyboard.press("Enter")
        time.sleep(100)


# TODO:
# 7 parse renamed file
# 8 find mean, mode, min, max,
# 9 use streamlit vizzu to present data


def download_file(link):
    home = "https://www.xome.com"
    download_url = home.join(link)

    # make API call, added user-agent to prevent 403 error
    req = requests.get(download_url, headers={"User-Agent": "Mozilla/5.0"})
    print('req.headers', req.headers)
    print(req.url)

    # .rfind finds the first occurrence of "/" character starting from right to left
    # .find starts from left to right
    # find the filename
    filename = req.url[download_url.rfind("-") + 1:]
    print('filename', filename)

    # context manager to write file to csv
    with open(f"{filename}.csv", "wb") as file:
        chunks = req.iter_content(chunk_size=8192)
        for chunk in chunks:
            if chunk:
                file.write(chunk)

    # rename file name to city plus date



if __name__ == "__main__":
    # choices = ["Irving, TX - 0", "Carrollton, TX - 1", "Arlington, TX - 2", "Coppell, TX - 3", ]
    # print(str(choices))
    # selection = input("Please type in number of the city you are interested in")
    # choice = choices[int(selection)]
    console = Console()
    search_city()

