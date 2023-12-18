import csv
import requests

from rich.console import Console
from rich.prompt import Prompt

# import webbrowser
#
# from bs4 import BeautifulSoup


def menu():
    choices = ["Irving, TX - 0", "Carrollton, TX - 1", "Arlington, TX - 2", "Coppell, TX - 3"]
    for choice in choices:
        console.print(f"{choice[:len(choice)-3]} [blue]{choice[len(choice)-3:]}[/blue]", end=" | ")
    selection = Prompt.ask("\nPlease select city [[blue]0[/blue] for Irving, TX] ")
    choice = choices[int(selection)]
    formatted_choice = choice[:len(choice)-3]
    console.print("You have selected [bold underline blue]" + formatted_choice + "[/bold underline blue]")

# Manual steps to navigate xome.com and download list of homes for sale
# 1 open https://www.xome.com/Listing/ListingSearch.aspx
# 2 type name of city into search box
# 3 change view to list
# 3 find download button and copy link address
# 4 assign link address to download_url
# 5


def main():
    download_url = ("https://www.xome.com/Listing/ExportListingInCSV.ashx"
                    "?searchoverride=0fb00fea-c8db-496a-a781-cb870f083298")

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

    # with open("cb870f083298", "r" ) as file:


    # download csv files for each city
    # driver = webdriver.Chrome()
    #
    # driver.get("https://www.xome.com/")

    # url = "https://www.xome.com/Listing/ListingSearch.aspx"
    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html.parser")
    # # input_city = soup.find_all("div", class_="search-input-wrapper")
    # print(soup)

    # list_of_urls = []
    # read csv file and grab all the urls
    # with open("src/Xome_2023-11-21-15-22 Irving.csv") as file:
    #     reader = csv.reader(file)
    #     data = list(reader)
    #     # print(data[0])
    #
    #     url_index = data[0].index('URL')
    #     # print(url_index)
    #
    #     for row in data:
    #         list_of_urls.append((row[url_index]))
    #
    #     print(list_of_urls)
    #     print(len(list_of_urls))
    #
    # webbrowser.open(list_of_urls[1])

    # listingdetail - financialconsiderations
    # go to each url and scrape the Property ID number

    # go to property records and grab appraisal value and name of owners


if __name__ == "__main__":
    # choices = ["Irving, TX - 0", "Carrollton, TX - 1", "Arlington, TX - 2", "Coppell, TX - 3", ]
    # print(str(choices))
    # selection = input("Please type in number of the city you are interested in")
    # choice = choices[int(selection)]
    console = Console()
    menu()

