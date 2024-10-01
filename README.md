# LinkedIn Easy Apply Automation with Selenium

This project automates the process of applying for jobs on LinkedIn using the "Easy Apply" feature. The script logs into LinkedIn, searches for job opportunities based on user-provided keywords and location, filters by "Easy Apply," and automatically submits applications.

## Features

- Automatically logs in to LinkedIn.
- Searches for job listings using specified keywords and location.
- Filters jobs by the "Easy Apply" option.
- Automatically applies for jobs and skips those that have already been applied for.
- Handles multi-page job searches.
- Discards complex applications that cannot be completed through automation.
- Cleanly logs out and closes the browser after completion.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**
- **Selenium** library
- **webdriver_manager** for managing the ChromeDriver installation
- **BeautifulSoup4** for parsing HTML (optional but included for potential future use)
- Google Chrome browser

You can install the required libraries by running the following command:

```bash
pip install selenium webdriver_manager beautifulsoup4


## Config.json
{
    "email": "your-email@example.com",
    "password": "your-password",
    "keywords": "Software Engineer",
    "location": "San Francisco, California"
}
