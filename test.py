
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the URL of the webpage you want to access
url = 'https://www.delish.com/cooking/recipe-ideas/g40850309/high-protein-vegetarian-meals/'
driver.get(url)

time.sleep(5)


# Slowly scroll down the webpage
scroll_pause_time = 3 # Wait for 1 second between each scroll
screen_height = driver.execute_script("return window.screen.height;") # Get the height of the screen
i = 1
while True:
    # Scroll down the page by the screen height
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # Check if we have reached the end of the page
    if driver.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight;"):
        break


time.sleep(5) # Wait for 5 seconds for the page to load

# Parse the HTML content of the webpage using Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')

elements = soup.find_all('h2', class_= "css-ycx8oo e1tmud0h7")

# Loop through the elements and extract the desired information
for element in elements:
    print(element.text)

# Close the browser window
driver.quit()