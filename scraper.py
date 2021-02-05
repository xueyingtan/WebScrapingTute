import click
import requests
from bs4 import BeautifulSoup
import re
import datetime
import csv
import numpy as np
import pandas as pd

@click.command()
@click.option(
    '-l','--limit', nargs=1, default=float('inf'),
    help='A maximum number of result pages to collect. Defaults to no limit / collect all pages.'
)
@click.option(
    '-f','--filename', nargs=1,
    default="{}.csv".format(datetime.datetime.now().replace(microsecond=0).isoformat().replace(':','.')),
    help='What to name the resulting CSV file. The .csv extension will be added to the provided name.'
)
@click.option('-q','--query', nargs=1, default="",
              help="Search query to collect results for on The Conversation.")
def main(limit, filename, query):
    url = "https://theconversation.com" #baseurl
    urlquery = url+"/au/search?q="+query #contruct the url in ocnjuction with your query

    table = [] # temporary data structure to store the data
    while limit > 0 and urlquery:
        response = requests.get(urlquery) # send HTTP request to the web server and get response
        soup = BeautifulSoup(response.text, 'html.parser') # Get the html content and wrap in soup object
        articles = soup.select("div#content-results article")
        for article in articles:
            row = []
            row.append(article.time['datetime']) #datetime
            row.append(article.a['title']) #title
            row.append(article.select_one("p.byline").a.text) #author
            row.append(article.select_one("p.byline").em.text) #organisation
            row.append(article.header.next_sibling.next_sibling.text) #text (next sibling of header is nextline character)
            row.append(url+"/"+article.a["href"].split("%2F")[-1]) #article's link
            table.append(row)
        limit -= len(articles) # keep track of the number of articles so far if there is a limit
        urlquery = url+soup.find('a',attrs={'rel':'next'})['href'] # get next page if there is one (Each page returns 10 article posts)
        
    # Convert data to dataframe and write to csv file
    df = pd.DataFrame(np.array(table), columns=["Datetime","Title","Author","Author Organisation","Description Text","Article Link"])
    df.to_csv(filename, index=None)



if __name__ == "__main__":
    main()