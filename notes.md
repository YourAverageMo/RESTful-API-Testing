# Finnhub invalid datatypes

i noticed that finnhub handles invalid requests gracefully not throwing any errors. the symbol provided in the api request must be a valid symbol and in upper case

the only way i was able to get anything other than a code 200 response was by providing an invalid api key and invalid endpoint,

# CRUD Operations

finnhub is mostly a data retrieval service so i and only do GET requests (read)

# Selenium

Midway through setting up selenium i figured that since im not submitting any user input i could just use beautiful soup so im opting to use beautiful soup.