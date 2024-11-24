import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, InvalidArgumentException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def scrape_glassdoor(keyword, num_jobs):
    url = "https://www.glassdoor.com/Job/all-jobs"
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(15)
    
    search_bar = driver.find_element(By.XPATH, '//*[@id="searchBar-jobTitle"]')
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.ENTER)
    
    try:
        driver.find_elements(By.CLASS_NAME, "button_Button__meEg5 button-base_Button__9SPjH")
    except InvalidArgumentException:
        pass
        #print('Stage 4')
    
    time.sleep(10)
    
    # loads all job search 
    while True:
        try:
            time.sleep(3)
            jobs = driver.find_elements(By.CLASS_NAME, "JobsList_jobListItem__JBBUV")

            # click on see more
            try:
                driver.find_element(By.XPATH, '//*[@id="left-column"]/div[2]/div/button').click()
            except ElementClickInterceptedException:
                driver.find_element(By.CLASS_NAME, 'CloseButton').click() # close popup
            
            if len(jobs) > num_jobs:
                break
        except:
            print('No more jobs')
            break
    
    print(len(jobs))
    
    job_list = []
    
    for job in jobs:
        
        try:
            job.click()
        except ElementNotInteractableException:
            break
            
            
        time.sleep(5)
        job_role = driver.find_element(By.CLASS_NAME, 'JobDetails_jobTitle__Rw_gn').text
        company_name = job.find_element(By.CSS_SELECTOR, '[class^="EmployerProfile_employerInfo"]').text
        
        """print('\n')
        print(company_name)
        print('\n')
        """
        try:
            description = driver.find_element(By.CSS_SELECTOR, '[class^="JobDetails_jobDescription"]').text
        except:
            description = None
        try:
            salary = driver.find_element(By.CLASS_NAME, 'SalaryEstimate_averageEstimate__xF_7h').text
        except:
            salary = None
        location = driver.find_element(By.CLASS_NAME, 'JobDetails_location__MbnUM').text

        job_list.append({
            "Job Title": job_role,
            "Salary Estimate": salary,
            "Company Name": company_name,
            "Description": description,
            "Location": location
        })
    
    driver.quit()

    df = pd.DataFrame(job_list).reset_index()
    return df
