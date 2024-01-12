# LinkedIn Scraper

LinkedIn is an extremely popular platform for job seekers, making it one of the best websites to gather data on the job market.

## Scraping Job Listings

To collect data using this scraper, clone this repository and download the proper [ChromeDriver](https://chromedriver.chromium.org/downloads). Place the executable in the same directory as both linkedin.py and scrape.py. The python libraries needed for this program are numpy, pandas, selenium, and tqdm. A requirements.txt file is provided.

```shell
git clone https://github.com/daneski13/linkedin-job-scraper.git
cd ./linkedin-job-scraper
pip install -r requirements.txt
```

After downloading ChromeDriver and installing the dependencies, open the scrape.py file in your favorite text editor, change the URLs list to list LinkedIn job search URLs you wish to scrape. Running `python scrape.py` will show a progress bar for each URL being scraped and a linkedin-job-data.csv file will eventually be outputted containing the scraped data.

## Structure of Scraped Data

| Column Name     | Definition                                        |
| --------------- | ------------------------------------------------- |
| title           | title of the job listing                          |
| full_url        | LinkedIn URL of the job posting                   |
| company         | company name                                      |
| company_url     | company's LinkedIn URL                            |
| location        | job's location                                    |
| description     | raw HTML of the job's description                 |
| seniority_level | job's seniority level                             |
| employment_type | job's employment type (Full Time, Part Time etc.) |
| job_function    | job's expected functions                          |
| industries      | industries the company is in                      |
