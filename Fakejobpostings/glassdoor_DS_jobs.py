from utils.selenium_scrapper import scrape_glassdoor

result_df = scrape_glassdoor('data scientist', 2000)

result_df.to_csv('data/uncleaned_glassdoor_DataScience_jobs.csv', index=False)