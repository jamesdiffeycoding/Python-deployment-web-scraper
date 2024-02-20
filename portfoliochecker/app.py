from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():

    # COUNT VARIABLES
    count_of_working_sites = 0
    count_of_potentially_broken_sites = 0 

    # BOOLEAN STATUS VARIABLES
    banana_bl = 'False'
    shelter_bl = 'False'
    tailwind_bl = 'False'
    devlessons_bl = 'False'
    ghibli_bl = 'False'
    rubydex_bl = 'False'
    awesunsolar_bl = 'False'
    djangofirstproject_bl = 'False'

    # SITE 1 - "shelter" APP CHECK
    try: 
        shelter_page_to_scrape = requests.get("https://secure-nextjs-homeless-shelter-database.vercel.app/")
        soup = BeautifulSoup(shelter_page_to_scrape.content, 'html.parser')
        shelter_first_touch_points = soup.findAll("h1", attrs={"class": "white-font"})
        shelter_second_touch_points = soup.findAll("strong")

        # Check if both lists are non-empty before proceeding
        if shelter_first_touch_points and shelter_second_touch_points:
            shelter_bl = 'True'
        else:
            print("No shelter_first_touch_points or shelter_second_touch_points found.")
            shelter_bl = 'False'


        if shelter_bl == 'True':
            print('shelter is up and running and specified touch points were found')
            count_of_working_sites += 1
        else: 
            print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            count_of_potentially_broken_sites += 1


    except requests.exceptions.RequestException as e:
        print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1


    # RETURN STATEMENT 
    return render_template('deployments.html', 
    count_of_working_sites=count_of_working_sites, count_of_potentially_broken_sites=count_of_potentially_broken_sites,
    banana_bl=banana_bl,
    shelter_bl=shelter_bl,
    tailwind_bl=tailwind_bl,
    devlessons_bl=ghibli_bl,
    ghibli_bl=ghibli_bl,
    rubydex_bl=rubydex_bl,
    awesunsolar_bl=awesunsolar_bl,
    djangofirstproject_bl=djangofirstproject_bl)




# @app.route('/quotesworking')
# def quotesworking():
#     try:
#         page_to_scrape = requests.get("http://quotes.toscrape.com")
#         page_to_scrape.raise_for_bl()  # Raise an HTTPError if the request was unsuccessful
#         soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

#         # Find all quotes
#         quotes = soup.findAll("span", attrs={"class": "text"})

#         # Find all authors
#         authors = soup.findAll("small", attrs={"class": "author"})

#         # Combine quotes and authors into a list of tuples
#         quote_data = [(quote.text, author.text) for quote, author in zip(quotes, authors)]

#         return render_template('quotes.html', quotes=quote_data)

#     except requests.exceptions.RequestException as e:
#         return "Error making request: {}".format(e)

