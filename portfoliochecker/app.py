from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():

    # COUNT VARIABLES
    count_of_working_sites = 0
    count_of_potentially_broken_sites = 0 

    # BOOLEAN STATUS FOR WHETHER A SITE WAS REACHED (i.e. a valid URL was provided)
    banana_url_bl = 'False'
    shelter_url_bl = 'False'
    tailwind_url_bl = 'False'
    devlessons_url_bl = 'False'
    ghibli_url_bl = 'False'
    rubydex_url_bl = 'False'
    awesunsolar_url_bl = 'False'
    djangofirstproject_url_bl = 'False'

    # BOOLEAN STATUS VARIABLES FOR WHETHER SPECIFIED TOUCHPOINTS WERE REACHED (e.g. a h1 tag with a specific class name)
    banana_tp_bl = 'False'
    shelter_tp_bl = 'False'
    tailwind_tp_bl = 'False'
    devlessons_tp_bl = 'False'
    ghibli_tp_bl = 'False'
    rubydex_tp_bl = 'False'
    awesunsolar_tp_bl = 'False'
    djangofirstproject_tp_bl = 'False'



    # SITE 1 - "shelter" APP CHECK
    try: 
        shelter_page_to_scrape = requests.get("https://secure-nextjs-homeless-shelter-database.vercel.app/")
        soup = BeautifulSoup(shelter_page_to_scrape.content, 'html.parser')
        shelter_first_touch_points = soup.findAll("h1", attrs={"class": "white-font"})
        shelter_second_touch_points = soup.findAll("strong")
        # Check if both lists are non-empty before proceeding
        if shelter_first_touch_points and shelter_second_touch_points:
            shelter_tp_bl = 'True'
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            shelter_tp_bl = 'False'
            count_of_potentially_broken_sites += 1
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1


    # RETURN STATEMENT 
    return render_template('deployments.html', 
    count_of_working_sites=count_of_working_sites, count_of_potentially_broken_sites=count_of_potentially_broken_sites,
    banana_url_bl = banana_url_bl,
    shelter_url_bl = shelter_url_bl,
    tailwind_url_bl = tailwind_url_bl,
    devlessons_url_bl = devlessons_url_bl,
    ghibli_url_bl = ghibli_url_bl,
    rubydex_url_bl = rubydex_url_bl,
    awesunsolar_url_bl = awesunsolar_url_bl,
    djangofirstproject_url_bl = djangofirstproject_url_bl,
    banana_tp_bl=banana_tp_bl,
    shelter_tp_bl=shelter_tp_bl,
    tailwind_tp_bl=tailwind_tp_bl,
    devlessons_tp_bl=devlessons_tp_bl,
    ghibli_tp_bl=ghibli_tp_bl,
    rubydex_tp_bl=rubydex_tp_bl,
    awesunsolar_tp_bl=awesunsolar_tp_bl,
    djangofirstproject_tp_bl=djangofirstproject_tp_bl)




# @app.route('/quotesworking')
# def quotesworking():
#     try:
#         page_to_scrape = requests.get("http://quotes.toscrape.com")
#         page_to_scrape.raise_for_tp_bl()  # Raise an HTTPError if the request was unsuccessful
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

