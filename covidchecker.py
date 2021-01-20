from bs4 import BeautifulSoup
import requests as re

# getting the page
nyt_covid = re.get("https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html").text

# description
print("This is a basic COVID-19 in the US checker I made.")

# set up BeautifulSoup
soup = BeautifulSoup(nyt_covid, "lxml")

# this part checks for cases from yesterday
cases_yesterday = soup.find("td", class_="num yesterday svelte-fin3s2")
print(cases_yesterday.find("span").text + " cases yesterday.")

# this part checks for deaths from yesterday
deaths_yesterday = soup.find("tr", class_="counts__row deaths svelte-fin3s2")
number = deaths_yesterday.find("td", class_="num yesterday svelte-fin3s2")
print(number.find("span").text + " deaths yesterday.")

print("Stay safe everyone! :D")

done = False
while done == False:
    continue
