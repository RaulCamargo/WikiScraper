# WikiScraper

Scrapy spider to scrape all the wikipedia article pages in https://new.wikipedia.org/wiki and output the results into a csv file.

The spider will start from the first page of the "all pages" directory.

The spider will pull the data from the first description in the page. Any page without a description will be ignored. Any page where the article does not meet the length requirement will also be ignored.
