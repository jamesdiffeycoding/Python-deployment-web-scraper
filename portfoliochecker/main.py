from flask import Flask, render_template
app = Flask(__name__)
import requests

# Define the home page

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/portfolio')
def portfolio():
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

        return render_template('index.html', quotes=quote_data)

    except requests.exceptions.RequestException as e:
        return "Error making request: {}".format(e)
