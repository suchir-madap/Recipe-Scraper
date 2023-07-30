import urllib3
from bs4 import BeautifulSoup


url = "https://www.delish.com/cooking/recipe-ideas/g40850309/high-protein-vegetarian-meals/"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
# print(soup.find('title').text)


# The statement below prints out the Webpage title
print(soup.title.string)


# for paragraph in soup.find_all('p'):
#     print(paragraph.string)
#     print(str(paragraph.text))



# class = "css-ycx8oo e1tmud0h7"

elements = soup.find_all('h2', class_= "css-ycx8oo e1tmud0h7")

# Loop through the elements and extract the desired information
for element in elements:
    print(element.text)