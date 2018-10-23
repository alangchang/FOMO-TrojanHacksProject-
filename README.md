# FOMO-TrojanHacksProject

USC's amazing Trojan Family gives its students access to a myriad of career opportunities. However, this has led to students being constantly being dumped with hundreds of emails and notifications career and networking events. FOMO centralizes this data into an easily accessible map UI and calendar. It parses information from USC school emails regarding career, sorts it, and pins it onto a google map and calendar for students to see that is updated daily.

## How this project is built

1. GetEmailStrings.py implements a function that scrapes the body of career emails from specific sender. This script uses Gmail API.
2. parseEmail.py takes the email body and parses the weekday and month of the career event in that email. This script uses Google's Natural Language API.
3. Samsort.py gets the date, time, and location of the career event from email body. This script uses regEx in Python.
4. data_col.py runs all previous scripts, stores parsed information as a dictionary, and output the dict to a json file.
5. The collection information is then used to generate markers on a map through Geocode and Google Map API, using javascript. This script can be found in index.html inside the website folder.

## How to run it locally

1. Make sure you have signed up for Google Map API. Put your API key in config.js file.
2. Navigate to website folder and open index.html and you should see markers on a google map.
3. Hover over any marker to see detailed information about a career event!
