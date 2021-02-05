# Web Scraping Tute

This is an introductory python script I put together for web scraping using BeautifulSoup. 

### From your environment
```
cd anaconda
conda create --name "your_env" python=3.8
activate <your_env>
git clone https://github.com/xueyingtan/WebScrapingTute.git
cd WebScrapingTute
pip install -r requirements.txt
pip install -e .
```

## Usage

After installing webscraper as shown above, in your command terminal in the same directory
as this README file, run the `scrape` command.

### Command Line
```
$ scrape
Usage: scrape [OPTIONS]

Commands:
  scrape [OPTIONS]      

OPTIONS
  -l/--limit        Set the maximum numbe of posts to scrape                           [int][default:positive infinity]
  -f/--filename     File to write/append to with csv extension only ('result.csv')  [string][default:<currentTime>.csv]
  -q/--query        Keyword for the searchbar on the domain                                        [string][default:""]
  --help

Examples:
  1. scrape -q covid -l 200                        Scrape up to 200 posts returned from keyword covid on the website
  2. scrape -l 1000 -f 'output.csv'                Scrape up to 1000 posts and store result in output.csv

Source code available at https://github.com/xueyingtan/WebScrapingTute.git