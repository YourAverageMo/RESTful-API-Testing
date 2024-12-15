# RESTful-API-Testing
QA Focused project to test public api's. I've been tasked with testing any public api's capabilities and limitations. For this project i chose to go with [Finnhub's](https://finnhub.io/) free api service that provides up-to-date stock information. I was offered creativity in selection of which i use so i figured it would be fun to fiddle with stock api's.

- [RESTful-API-Testing](#restful-api-testing)
- [The Plan](#the-plan)
- [Todo List](#todo-list)
- [Part 1: API Testing](#part-1-api-testing)
- [Part 2: Automation Framework](#part-2-automation-framework)
- [Part 3: Reporting](#part-3-reporting)


# The Plan
![Untitled-2024-12-10-1352](https://github.com/user-attachments/assets/784e73a1-fac5-4feb-a979-180c711d643f)

# Todo List

- [x] choose api
- [x] implement automated tests for CRUD operations (invalid in this with Finnhub api)
- [x] response structure
- [x] status code and error message validation for invalid inputs
- [x] simulate high traffic 
- [x] automation frameworks using selenium (invalid in this project since no ui interaction, but i implemented a workaround)
- [x] document test plan
- [x] visulizations

# Part 1: API Testing

1. **API Choice:** i choose to go with FinnHub for this project, however i learned midway through that finnhub doesnt offer full CRUD capabilities like some other learning api's might have. This is fine as i still test it and validate it with external data using Selenium.

2. **Automated Test Validations:** since this api doesn't offer CRUD operations and project-wise there would be no UI to interact with i choose to combine Part 1.2 and Part 2.1. Instead i will be using selenium to fetch the same stock price from yahoo finance and compare it with the value FinnHub provides as a means of validating API response. This is done in test_api_selenium.py:

   ![image](https://github.com/user-attachments/assets/7b841464-0a08-46e4-9800-3257d1e70d3f)

3. **Response Structure:** The response from Finnhub is just like you would expect from any api returning a json object with key value pairs as follows:
   - c: Current price
   - d: Change
   - dp: Percent change
   - h: High price of the day
   - l: Low price of the day
   - o: Open price of the day
   - pc: Previous close price

   there are a few important distinctions i ran into when testing the api's responses with various different inputs.
       
    - I noticed that FinnHub handles invalid requests gracefully not throwing any errors. the symbol provided in the api request must be a valid symbol and in uppercase
    - The only way i was able to get anything other than a code 200 response was by providing an invalid api key or invalid endpoint. This means that that the input `aapl` still returns a valid response, though not uppercase. Resulting in 0's for all its values in the json response.

4. **Simulated High Traffic:** 
   
   For simulating high traffic originally the plan was to use locust to hit the api with multiple users all accessing different stock prices. However, attacking a public api like this would not be something i would feel comfortable doing myself, and ultimately decided against it as the results from locust would, more or less, be the same as the `test_api_response_time()` test. Regardless the locust.py file is still in the tests folder and should work as is.
   
   In the response time function I built a simpler version of what locust would aim to do, that hits the same endpoint a set amount of times per second to gather response time numbers. The API never failed unless you hit it faster than the 60 calls/minute limit so its safe to assume the same would apply to locust.

   On a similar note, I ran into api limiting due to high traffic when running all the tests together. To circumvent this, a few time.sleep() functions were added to key areas of the tests.

# Part 2: Automation Framework

selenium was combined in [Part 1.2 Automated testing](#part-1-api-testing) others will be merged into [Part 3 Reporting](#part-3-reporting)

# Part 3: Reporting

**Test plan** and scope is shown in [The Plan](#the-plan).

**Test objectives** are to test functionality of FinnHub api, validate response with external data, ensure proper positive/negative responses from API (i.e. invalid responses), and to measure API response time.

In terms of **failure/success rates**, API functionality and all tests implemented functioned properly with no abnormalities except in the improper 200 status code with invalid inputs.

With that being said, i **highly recommend** providing better feedback when invalid inputs are provided. In the `aapl` vs `AAPL` example both inputs would result in a status code 200 and a json payload with valid data. Only the uppercase `AAPL`, however, would be a "valid" input and return the correct price of Apple stock. This behavior could lead to confusion for users not being aware of invalid inputs when submitted.

**Finnhub API Response Time**

![Histogram](https://github.com/user-attachments/assets/260ec88a-7f31-460f-a73e-49a4ce9a7c54)

The graph above came from the data available in  `./api_calls.json` which was logged during unit testing 1 api call every second for 200 seconds. **Average response time was .2025 seconds**.