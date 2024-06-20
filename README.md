#### Overview
This repository contains a Python script designed to scrape URLs containing the path "YOUR TEXT" from Google search results using Selenium WebDriver. The script automates the process of searching Google, navigating through multiple result pages, and extracting relevant URLs which are then saved into a CSV file.

#### Requirements
- Python 3.x
- Selenium WebDriver (ChromeDriver)
- Pandas library
- Chrome browser

#### Setup Instructions
1. **Install Python**: Ensure Python 3.x is installed on your system.
   
2. **Install Selenium**: Install Selenium using pip:
   ```
   pip install selenium
   ```

3. **PATH ChromeDriver**: Change this code according to your system, specify the path explicitly in the script.
    ```
    os.environ["PATH"] += r"C:/SeleniumDrivers"
    ```

4. **Install Pandas**: Install Pandas library using pip:
   ```
   pip install pandas
   ```

5. **Clone Repository**: Clone or download this repository to your local machine.

#### Running the Script
1. Navigate to the directory containing the script (`app.py`).

2. Open a terminal or command prompt and run the script:
   ```
   python app.py
   ```
   This will execute the script which performs the Google search, scrapes URLs, and saves them into `links.csv` in the same directory.

#### Script Explanation
- **Initialization**: The script initializes a `GoogleSearchScraper` class with a query ("arcgis/rest/services"), change this to required text, and sets up the Selenium WebDriver for Chrome.
  
- **Search and Scraping**: 
  - It opens Google, performs the search query, and navigates through multiple result pages by clicking on "More results" until no more are available.
  - URLs containing "arcgis/rest/services" are extracted from the search results.

- **Saving Results**: Extracted URLs are stored in a Pandas DataFrame and saved to a CSV file (`links.csv`).

- **Error Handling**: The script handles exceptions such as clicking "More results" and scrolling down to load more content.

#### Output
The script outputs a CSV file (`links.csv`) containing two columns: `id` and `link`. Each row represents a URL extracted from Google search results that match the specified query.

#### Conclusion
This script provides a straightforward solution for automating the extraction of specific URLs from Google search results using Python and Selenium. It demonstrates basic web scraping techniques and error handling for handling dynamic content loading.

#### Notes
- Adjust sleep times and exception handling as needed based on network speed and page load times.

For any issues or improvements, feel free to raise them in the repository issues section.