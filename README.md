# LinkedIn Scraper

LinkedIn is an extremely popular platform for job seekers make it one of the best websites to gather data on the job market.

## Scraping Job Listings

To use this scraper to collect data, clone this repository, download the proper [ChromeDriver](https://chromedriver.chromium.org/downloads) for your version of the Chrome Browser and put the executable in the same directory as both linkedin.py and scrape.py. The python libraries needed for this program are numpy, pandas, selenium, and tqdm. A requirements.txt file is provided.

## Structure of Scraped Data

id - index number
title - title of the listing
full_url - the LinkedIn URL of the job posting
company - the company name
company_url - the company's LinkedIn URL
location - the job's location
description - raw HTML of the job's description
seniority_level - the job's seniority level
employment_type - the job's employment type (Full Time, Part Time etc.)
job_function - the job's expected functions
industries - the industries the company is in
