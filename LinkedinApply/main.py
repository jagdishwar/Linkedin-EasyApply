import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import json
from selenium.common.exceptions import TimeoutException, NoSuchElementException
chrome_options = Options()
class EasyApplyLinkedin:

    def __init__(self, data):
        """Parameter initialization"""

        self.email = data['email']
        self.password = data['password']
        self.keywords = data['keywords']
        self.location = data['location']
        # Creating Chrome Options
        chrome_options = Options()

        # Create ChromeDriver with ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login_linkedin(self):
        """This function logs into your personal LinkedIn profile"""

        # go to the LinkedIn login url
        self.driver.get("https://www.linkedin.com/login")


        # introduce email and password and hit enter
        login_email = self.driver.find_element(By.NAME,'session_key')
        login_email.clear()
        login_email.send_keys(self.email)
        login_pass = self.driver.find_element(By.NAME,'session_password')
        login_pass.clear()
        login_pass.send_keys(self.password)
        login_pass.send_keys(Keys.RETURN)
        time.sleep(20)

    def job_search(self):
        """This function goes to the 'Jobs' section a looks for all the jobs that matches the keywords and location"""

        # go to Jobs
        jobs_link = self.driver.find_element(By.LINK_TEXT, "Jobs")
        jobs_link.click()
        time.sleep(2)
        show_all = self.driver.find_element(By.LINK_TEXT, "Show all")
        show_all.click()


        time.sleep(2)

        # search based on keywords and location and hit enter
        search_keywords = self.driver.find_element(By.CSS_SELECTOR,
                                                   ".jobs-search-box__text-input[aria-label='Search by title, skill, or company']")
        search_keywords.clear()

        search_keywords.send_keys(self.keywords)
        time.sleep(2)

        search_location = self.driver.find_element(By.CSS_SELECTOR,
                                                   ".jobs-search-box__text-input[aria-label='City, state, or zip code']")
        search_location.clear()
        search_location.send_keys(self.location)
        time.sleep(2)
        search_location.send_keys(Keys.RETURN)
        time.sleep(2)

    def filter(self):
        """This function filters all the job results by 'Easy Apply'"""

        # select all filters, click on Easy Apply and apply the filter
        easy_apply_button = self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Easy Apply filter.']")

        easy_apply_button.click()
        time.sleep(2)

    def find_offers(self):
        """This function finds all the offers through all the pages result of the search and filter"""

        # find the total amount of results (if the results are above 24-more than one page-, we will scroll trhough all available pages)


        # Find the element containing the total results text
        total_results_element = self.driver.find_element(By.XPATH,
                                                         "//div[@class='jobs-search-results-list__subtitle']/span")

        # Get the text and clean it to contain only numbers
        total_results_text = total_results_element.text

        # Use a regular expression to extract only the digits
        numbers_only = re.sub(r'\D', '', total_results_text)

        # Convert to integer
        total_results_int = int(numbers_only)
        print(total_results_int)


        time.sleep(2)
        # get results for the first page
        current_page = self.driver.current_url

        results = self.driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
        print(results)

        # Iterate over each result
        for result in results:
            hover = ActionChains(self.driver).move_to_element(result)
            hover.perform()
            titles = result.find_elements(By.CLASS_NAME, "job-card-list__title")
            print(titles,'ssss')

            # Iterate over each job title
            for title in titles:
                # Extract and print the text of the job title
                print(title.text)

                # Assuming you have a method called submit_apply to submit the job application
                # You can call it here passing the job title WebElement
                self.submit_apply(title)

    def submit_apply(self, job_add):
        """This function submits the application for the job add found"""

        print('You are applying to the position of: ', job_add.text)
        job_add.click()
        print('ysshhhsddfdffd')
        time.sleep(2)

        try:
            print('entered >>>>>>>>>.')
            easy_apply_button = self.driver.find_element(By.CLASS_NAME, "jobs-apply-button")

            # Click on the Easy Apply button
            easy_apply_button.click()

        except NoSuchElementException:
            print('You already applied to this job, go to next...')
            pass
        time.sleep(1)

        try:
            #submit = self.driver.find_element(By.XPATH, "//button[@data-control-name='submit_unify']")
            #submit.click()
            flag=1
            if flag:
                try:
                    next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
                    print(next_button,'kkkkkkkkkk')
                    next_button.click()

                    time.sleep(3)
                except NoSuchElementException:
                    flag=0
                    print('next is what )))))))))))))))))))')
                    pass
            if flag:
                try:
                    next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
                    print(next_button, 'kkkkkkkkkk')
                    next_button.click()
                    time.sleep(3)
                except (TimeoutException, NoSuchElementException) as e:
                    lag = 0
                    print('next is what )))))))))))))))))))')
                    pass
            if flag:
                try:
                    next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
                    print(next_button, 'kkkkkkkkkk')
                    next_button.click()
                    time.sleep(3)
                except (TimeoutException, NoSuchElementException) as e:
                    flag = 0
                    print('next is what )))))))))))))))))))')
                    pass
            if flag:
                try:
                    next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
                    print(next_button, 'kkkkkkkkkk')
                    next_button.click()
                    time.sleep(3)
                except (TimeoutException, NoSuchElementException) as e:
                    flag = 0
                    print('next is what )))))))))))))))))))')
                    pass









                # Check for "Additional Questions" text before clicking Next






            print('next is what )))))))))))))))))))')





            if False:

                    # Get the page source after waiting for dynamic content to load
                    html_content = self.driver.current_url
                    html_content=open(html_content)
                    print(html_content)

                    # Parse the HTML content using BeautifulSoup
                    soup = BeautifulSoup(html_content, 'html.parser')
                    print('mass',soup.body)

                    # Find the section containing "Additional Questions"
                    additional_questions_section = soup.find('h3', class_='t-16 t-bold', text='Additional Questions')

                    # Print the section if found
                    if additional_questions_section:
                        print(additional_questions_section)
                    else:
                        print("Additional Questions section not found")

                    # If the section is found, proceed with extracting questions
                    if additional_questions_section:
                        questions_data = []
                        print('enteredddddd')

                        # Iterate through question elements
                        for question_element in additional_questions_section.find_next_siblings('div',
                                                                                                class_='jobs-easy-apply-form-section__grouping'):
                            question_text = question_element.find('label', class_='artdeco-text-input--label')
                            print(question_element,'sdsasda')
                            print(question_text,'sdsadaslll')

                            # Check if question text is found
                            if question_text:
                                question_text = question_text.text.strip()
                                questions_data.append(question_text)

                        # Print the extracted questions
                        print(questions_data)
                    else:
                        print("No 'Additional Questions' section found")

            review_button = self.driver.find_element(By.XPATH, "//span[text()='Review']")
            review_button.click()
            submit_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
            submit_button.send_keys(Keys.RETURN)
        except NoSuchElementException:
            print('Not direct application, going to next...')

            try:
                discard = close_icon = self.driver.find_element(By.XPATH, "//svg[contains(@class, 'artdeco-button__icon')]")

                discard.send_keys(Keys.RETURN)
                time.sleep(1)
                discard_confirm = discard_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-modal__confirm-dialog-btn') and contains(text(), 'Discard')]")

                discard_confirm.send_keys(Keys.RETURN)
                time.sleep(1)
            except NoSuchElementException:

                pass


            time.sleep(1)

    def close_session(self):
        """This function closes the actual session"""

        print('End of the session, see you later!')
        self.driver.close()

    def apply(self):
        """Apply to job offers"""

        self.driver.maximize_window()
        self.login_linkedin()
        time.sleep(2)
        self.job_search()
        time.sleep(2)
        self.filter()
        time.sleep(2)
        self.find_offers()
        time.sleep(2)
        self.close_session()


if __name__ == '__main__':
    with open('config.json') as config_file:
        data = json.load(config_file)

    bot = EasyApplyLinkedin(data)
    bot.apply()


