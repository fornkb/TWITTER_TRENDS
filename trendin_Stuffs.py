from bs4 import BeautifulSoup
import requests
import webbrowser
html_file = requests.get("https://trendlistz.com/india").content
soup = BeautifulSoup(html_file,'lxml')
trends = soup.find('section',class_= "page-content")
trending = trends.find_all('li',class_="trend-item")
trending_names = []
trending_links = []
for data in trending:
    try:
        trending_names.append(data.find('span',class_="term").text.strip())
        trending_links.append(data.find('a')["href"])
    except AttributeError as abc:
        continue
for index,values in enumerate(trending_names):
    print(f"{index+1}. {values}")
choice = (input("Would you like to know more about any of the above trends(y/n): ".title())).lower()
while choice == "y":
    user_input = int(input("Please Enter No. Of The trend you would like to know more about: ".title()))
    for ind,i in enumerate(trending_links):
        if ind+1 == user_input:
            webbrowser.open(i)
    choice = (input("Would you like to know more about any of the above trends(y/n): ".title())).lower()
input("Thank You")
