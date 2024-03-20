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
    url_failure_message = 'Url request failed.'
    tp_success_message = 'Touch points reached.'
    tp_failure_message = 'Touch points failed.'

    # STATUS FOR WHETHER A SITE WAS REACHED (i.e. a valid URL was provided)
    emissions_url = False
    banana_url = False
    shelter_url = False
    tailwind_url = False
    devlessons_url = False
    ghibli_url = False
    rubydex_url = False
    awesunsolar_url = False
    djangofirstproject_url = False
    madeupurl_url = False # deliberate fail example site
    google_url = False # deliberate fail example site
    # STATUS VARIABLES FOR WHETHER SPECIFIED TOUCHPOINTS WERE REACHED (e.g. a h1 tag with a specific class name)
    emissions_tp = False
    banana_tp = False
    shelter_tp = False
    tailwind_tp = False
    devlessons_tp = False
    ghibli_tp = False
    rubydex_tp = False
    awesunsolar_tp = False
    djangofirstproject_tp = False
    madeupurl_tp = False # deliberate fail example site
    google_tp = False # deliberate fail example site


    # SITE - "emissions" APP CHECK
    try: 
        page_to_scrape = requests.get("https://corporate-carbon-disclosures.vercel.app/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("div")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors
        second_touch_points = soup.findAll("p")
        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            emissions_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            emissions_tp = False
            count_of_potentially_broken_sites += 1
        emissions_url = True
    except requests.exceptions.RequestException as e: # this checks for request errors
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        shelter_url = False
    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        shelter_url = False


    # SITE - "shelter" APP CHECK
    try: 
        page_to_scrape = requests.get("https://secure-nextjs-homeless-shelter-database.vercel.app/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("h1", attrs={"class": "white-font"})
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors
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
    except requests.exceptions.RequestException as e: # this checks for request errors
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        shelter_url = False
    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        shelter_url = False

    # SITE - "banana" APP CHECK
    try: 
        page_to_scrape = requests.get("https://jamesdiffeycoding.github.io/JS-Banana-and-Ivy-Game/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("div", attrs={"class": "header"})
        second_touch_points = soup.findAll("p")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

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

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        banana_url = False

    # SITE - "tailwind" APP CHECK
    try: 
        page_to_scrape = requests.get("https://jamesdiffeycoding.github.io/Tailwind-Responsive-Grid-Experiments/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("h1", attrs={"class": "text-4xl"})
        second_touch_points = soup.findAll("p")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            tailwind_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            tailwind_tp = False
            count_of_potentially_broken_sites += 1
        tailwind_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        tailwind_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        tailwind_url = False


    # SITE - "devlessons" APP CHECK
    try: 
        page_to_scrape = requests.get("https://developer-lessons-react.vercel.app/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("div") # note: I'm not sure why on this one I can't get a green flag for anything with a class attribute
        second_touch_points = soup.findAll("div")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            devlessons_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            devlessons_tp = False
            count_of_potentially_broken_sites += 1
        devlessons_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        devlessons_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        devlessons_url = False


    # SITE - "ghibli" APP CHECK
    try: 
        page_to_scrape = requests.get("https://jamesdiffeycoding.github.io/Animated-Wallpaper-StudioGhibli/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("video", attrs={"class": "bg-video"})
        second_touch_points = soup.findAll("p")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            ghibli_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            ghibli_tp = False
            count_of_potentially_broken_sites += 1
        ghibli_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        ghibli_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        ghibli_url = False


    # SITE - "rubydex" APP CHECK
    try: 
        page_to_scrape = requests.get("https://rubyonrails-pokedex.onrender.com/pokemonsters", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("div", attrs={"class": "footer"})
        second_touch_points = soup.findAll("p")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            rubydex_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            rubydex_tp = False
            count_of_potentially_broken_sites += 1
        rubydex_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        rubydex_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        rubydex_url = False


    # SITE - "awesunsolar" APP CHECK
    try: 
        page_to_scrape = requests.get("https://awesun-solar-visualiser.vercel.app/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("div", attrs={"class": "backgroundImage"})
        second_touch_points = soup.findAll("p")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            awesunsolar_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            awesunsolar_tp = False
            count_of_potentially_broken_sites += 1
        awesunsolar_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        awesunsolar_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        awesunsolar_url = False


    # SITE - "djangofirstproject" APP CHECK
    try: 
        page_to_scrape = requests.get("https://django-learning-project.vercel.app/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("nav", attrs={"class": "navbar"})
        second_touch_points = soup.findAll("p")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            djangofirstproject_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            djangofirstproject_tp = False
            count_of_potentially_broken_sites += 1
        djangofirstproject_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        djangofirstproject_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        djangofirstproject_url = False


# DELIBERATE FAIL SITES
    # SITE - "madeupurl" - madeupurl APP CHECK
    try: 
        page_to_scrape = requests.get("https://madeupurlthatdoesntexist.com/", timeout=1)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("h1", attrs={"class": ""})
        second_touch_points = soup.findAll("div")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            madeupurl_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            madeupurl_tp = False
            count_of_potentially_broken_sites += 1
        madeupurl_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        madeupurl_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        madeupurl_url = False
    
    # SITE - "google" - deliberate touch point fail APP CHECK
    try: 
        page_to_scrape = requests.get("https://google.com/", timeout=0.01)
        soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
        first_touch_points = soup.findAll("h10", attrs={"class": ""})
        second_touch_points = soup.findAll("div")
        page_to_scrape.raise_for_status()  # Raise an exception for HTTP errors

        # Check if both lists are non-empty before proceeding
        if first_touch_points and second_touch_points:
            google_tp = True
            count_of_working_sites += 1
        else:
            # print('The request went through suggesting the URL was valid, but the touch points you set may have changed')
            google_tp = False
            count_of_potentially_broken_sites += 1
        google_url = True
    except requests.exceptions.RequestException as e:
        # print("Error making request to shelter. Maybe there was a typo?") 
        # print(e)
        count_of_potentially_broken_sites += 1
        google_url = False

    except Exception as e: # this checks for other erros fetching the site
        count_of_potentially_broken_sites += 1
        google_url = False
# END OF DELIBERATE FAIL SITES

    # RETURN STATEMENT 
    return render_template('deployments.html', 
    count_of_working_sites=count_of_working_sites, count_of_potentially_broken_sites=count_of_potentially_broken_sites,
    # EXAMPLE VARIABLES
    url_success_message = url_success_message,
    url_failure_message = url_failure_message, 
    tp_success_message = tp_success_message, 
    tp_failure_message = tp_failure_message,
    madeupurl_tp=madeupurl_tp,
    madeupurl_url=madeupurl_url,
    google_tp=google_tp,
    google_url=google_url,
    # PROJECT STATUS BOOLEAN VARIABLES
    emissions_url = emissions_url,
    banana_url = banana_url,
    shelter_url = shelter_url,
    tailwind_url = tailwind_url,
    devlessons_url = devlessons_url,
    ghibli_url = ghibli_url,
    rubydex_url = rubydex_url,
    awesunsolar_url = awesunsolar_url,
    djangofirstproject_url = djangofirstproject_url,
    emissions_tp= emissions_tp,
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

