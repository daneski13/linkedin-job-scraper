import linkedin as li
import pandas as pd

# Note: LinkedIn only allows up to 1000 listings per search result, 
# recommended to use the same search query with different filter
# combinations for full coverage.

# WARNING: linkedin.py uses multiprocessing to process multiple URLs, 
# scraping many URLs at once is resource intensive.

# Change to your URLs.
urls = [
	'https://www.linkedin.com/jobs/search?keywords=Finance&location=United%20States',
]


if __name__ == '__main__':
	# get listings and drop null full_urls
	df: pd.DataFrame = li.get_listings_from(urls).dropna(axis=0, subset='full_url')

	# drop duplicates
	df.drop_duplicates(subset='full_url', inplace=True)

	# save to csv file, appending to it if it exists
	df.to_csv_('linkedin-job-data.csv', mode='a', index_label='id')
