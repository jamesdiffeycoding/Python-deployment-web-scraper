# Python Live Deployments Dashboard

![DeploymentsDashboardShot1](https://github.com/jamesdiffeycoding/python-live-deployments-dashboard/assets/139918141/c6d6d78f-0136-4ce7-8315-9fbcdefbef54)

## Inspiration
As a developer with many projects online, I wanted a quick way to check that all of my public deployments were working.

I used Python to create this web scraping tool, that tests my own site URLs, checking that they are working and returning content as desired.

An extra bit of value provided by this site is that visiting it helps to ensure none of my deployments spin down with inactivity.

## What it does

This site checks my deployments at their url, parses the html response, and checks that they return certain html 'touch points' I am checking for (e.g. h1 tags, p tags, etc).

The site displays the status of the url requests to these sites and the html responses and displays whether the request was successful or unsuccessful. If, for instance, the site is down, the url has moved, or it cannot find the specified tags, a clear visual indicator will let me know that the site may require my attention.

## How I built it
I built this project using Python, Flask, BeautifulSoup (for web scraping) and straightforward HTML and CSS.

## What I learned
This was my first deployed project in Python that didn't use django. Setup was the hardest part for me, particularly to understand how to link together python scripts and HTML files using Flask. Once everything was linked up, however, it was quite straightforward. It was useful practice of linking up python files and debugging.

## Built with
Python, Flask, Beautiful Soup, HTML, CSS 

## Issues to fix
Sometimes the site has a loading issue I am currently trying to fix. My understanding is it is to do with making requests to so many different sites, that if any of the sites it is requesting from are returning their response very slowly, it can prevent my Python template from rendering.

## Try it out
[My Live Deployments Dashboard](https://jamesdiffeycoding-pythonlivedashboard.vercel.app/)
