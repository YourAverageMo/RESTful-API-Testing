# Finnhub invalid datatypes

i noticed that finnhub handles invalid requests gracefully not throwing any errors. the symbol provided in the api request must be a valid symbol and in upper case

the only way i was able to get anything other than a code 200 response was by providing an invalid api key and invalid endpoint,

# CRUD Operations

finnhub is mostly a data retrieval service so i and only do GET requests (read)

# Selenium

since this project doesnt really have any ui to interact with there really wasnt any need for selenium. So instead i choose to use selenium as api result verification. In this application i will compare the stock price i receive from finnhub to what yahoo finance says the price is. This will act as Automated framework testing.