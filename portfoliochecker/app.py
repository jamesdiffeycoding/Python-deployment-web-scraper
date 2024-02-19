from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    count_of_working_sites = 0
    count_of_potentially_broken_sites = 0 
    try: 
        shelterdatabase_page_to_scrape = requests.get("https://secure-nextjs-homeless-shelter-database.vercel.app/")
        soup = BeautifulSoup(shelterdatabase_page_to_scrape.content, 'html.parser')
        shelterdatabase_first_touch_points = soup.findAll("h1", attrs={"class": "white-font"})
        shelterdatabase_second_touch_points = soup.findAll("strong")

        # Check if both lists are non-empty before proceeding
        if shelterdatabase_first_touch_points and shelterdatabase_second_touch_points:
            for shelterdatabase_first_touch_point, shelterdatabase_second_touch_point in zip(shelterdatabase_first_touch_points, shelterdatabase_second_touch_points):
                print(shelterdatabase_first_touch_point.text)
                print(shelterdatabase_second_touch_point.text)
            shelterdatabase_status = 'True'
        else:
            print("No shelterdatabase_first_touch_points or shelterdatabase_second_touch_points found.")
            shelterdatabase_status = 'False'
        if shelterdatabase_status == 'True':
            print('shelterdatabase is up and running and specified touch points were found')
            count_of_working_sites += 1
        else: 
            print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            count_of_potentially_broken_sites += 1
        return render_template('deployments.html', count_of_working_sites=count_of_working_sites, count_of_potentially_broken_sites=count_of_potentially_broken_sites)
    except requests.exceptions.RequestException as e:
        print("Error making request to shelterdatabase. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        return{"5count_of_working_sites": count_of_working_sites, "count_of_potentially_broken_sites": count_of_potentially_broken_sites}
    


@app.route('/quotesworking')
def quotesworking():
    try:
        page_to_scrape = requests.get("http://quotes.toscrape.com")
        page_to_scrape.raise_for_status()  # Raise an HTTPError if the request was unsuccessful
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

        # Find all quotes
        quotes = soup.findAll("span", attrs={"class": "text"})

        # Find all authors
        authors = soup.findAll("small", attrs={"class": "author"})

        # Combine quotes and authors into a list of tuples
        quote_data = [(quote.text, author.text) for quote, author in zip(quotes, authors)]

        return render_template('quotes.html', quotes=quote_data)

    except requests.exceptions.RequestException as e:
        return "Error making request: {}".format(e)

