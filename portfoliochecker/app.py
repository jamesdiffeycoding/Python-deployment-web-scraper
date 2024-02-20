from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():

    # COUNT VARIABLES
    count_of_working_sites = 0
    count_of_potentially_broken_sites = 0 

    # MESSAGES TO DISPLAY
    url_success_message = 'Url reached.'
    url_failure_message = 'Url failed. Check for typos.'
    tp_success_message = 'Touch points reached.'
    tp_failure_message = 'Touch points failed. Check for changes.'

    # STATUS FOR WHETHER A SITE WAS REACHED (i.e. a valid URL was provided)
    banana_url = False
    shelter_url = False
    tailwind_url = False
    devlessons_url = False
    ghibli_url = False
    rubydex_url = False
    awesunsolar_url = False
    djangofirstproject_url = False

    # STATUS VARIABLES FOR WHETHER SPECIFIED TOUCHPOINTS WERE REACHED (e.g. a h1 tag with a specific class name)
    banana_tp = False
    shelter_tp = False
    tailwind_tp = False
    devlessons_tp = False
    ghibli_tp = False
    rubydex_tp = False
    awesunsolar_tp = False
    djangofirstproject_tp = False

    # SITE 1 - "shelter" APP CHECK
    try: 
        page_to_scrape = requests.get("https://secure-nextjs-homeless-shelter-database.vercel.app/")
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("h1", attrs={"class": "white-font"})
        second_touch_points = soup.findAll("strong")
        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            shelter_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            shelter_tp = False
            count_of_potentially_broken_sites += 1
        shelter_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        shelter_url = False

    # SITE - "banana" APP CHECK
    try: 
        page_to_scrape = requests.get("https://jamesdiffeycoding.github.io/JS-Banana-and-Ivy-Game/")
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("h1", attrs={"class": "white-font"})
        second_touch_points = soup.findAll("strong")
        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            banana_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            banana_tp = False
            count_of_potentially_broken_sites += 1
        banana_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        banana_url = False


    # RETURN STATEMENT 
    return render_template('deployments.html', 
    count_of_working_sites=count_of_working_sites, count_of_potentially_broken_sites=count_of_potentially_broken_sites,
    # EXAMPLE VARIABLES
    url_success_message = url_success_message,
    url_failure_message = url_failure_message, 
    tp_success_message = tp_success_message, 
    tp_failure_message = tp_failure_message,
    # PROJECT STATUS BOOLEAN VARIABLES
    banana_url = banana_url,
    shelter_url = shelter_url,
    tailwind_url = tailwind_url,
    devlessons_url = devlessons_url,
    ghibli_url = ghibli_url,
    rubydex_url = rubydex_url,
    awesunsolar_url = awesunsolar_url,
    djangofirstproject_url = djangofirstproject_url,
    banana_tp=banana_tp,
    shelter_tp=shelter_tp,
    tailwind_tp=tailwind_tp,
    devlessons_tp=devlessons_tp,
    ghibli_tp=ghibli_tp,
    rubydex_tp=rubydex_tp,
    awesunsolar_tp=awesunsolar_tp,
    djangofirstproject_tp=djangofirstproject_tp)




# @app.route('/quotesworking')
# def quotesworking():
#     try:
#         page_to_scrape = requests.get("http://quotes.toscrape.com")
#         page_to_scrape.raise_for_tp()  # Raise an HTTPError if the request was unsuccessful
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

