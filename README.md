# RESTful-API-Testing

A QA-focused project to test public APIs. This project involves analyzing the capabilities and limitations of a public API. For this task, I selected [Finnhub's](https://finnhub.io/) free API service, which provides up-to-date stock market information. The choice of API was left to my discretion, and I thought it would be interesting to experiment with a stock API.

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
   Initially, I planned to use Locust to simulate high traffic by having multiple users access different stock prices. However, I decided against this approach to avoid overloading a public API. The Locust script (`locust.py`) is still included in the `tests` folder and should work as intended. 

   Instead, I built a simpler response time test (`test_api_response_time()`), which repeatedly hits the same endpoint at a set frequency to gather response time data. The API performed reliably unless the 60 calls/minute rate limit was exceeded. 

   Additionally, when running all tests together, I encountered rate-limiting issues. To mitigate this, I added `time.sleep()` functions at critical points in the test scripts.

# Part 2: Automation Framework

The Selenium tests are integrated into [Part 1.2: Automated Test Validations](#part-1-api-testing). Additional features are incorporated in [Part 3: Reporting](#part-3-reporting).

# Part 3: Reporting

**Test plan** and scope are outlined in [The Plan](#the-plan).

**Test Objectives:**  
- Validate the functionality of the Finnhub API.  
- Cross-verify API responses with external data.  
- Ensure proper handling of valid and invalid requests.  
- Measure API response time.

**Observations:**  
- API functionality and all implemented tests performed as expected, with no abnormalities except for the improper 200 status code for invalid inputs.  
- I recommend improving the API feedback for invalid inputs. For example, both `aapl` and `AAPL` return a 200 status code, but only the uppercase `AAPL` yields the correct price for Apple stock. This behavior can confuse users unaware of input requirements.

**Finnhub API Response Time**

![Histogram](https://github.com/user-attachments/assets/260ec88a-7f31-460f-a73e-49a4ce9a7c54)

The graph above came from the data available in  `./api_calls.json` which was logged during unit testing 1 api call every second for 200 seconds. **Average response time was .2025 seconds**.