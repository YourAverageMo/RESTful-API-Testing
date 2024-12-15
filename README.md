# RESTful-API-Testing
QA Focused project to test public api's. I've been tasked with testing any public api's capabilities and limitations. For this project i chose to go with [Finnhub's](https://finnhub.io/) free api service that provides up-to-date stock information. I was offered creativity in selection of which i use so i figured it would be fun to fiddle with stock api's.

# The Plan
![Untitled-2024-12-10-1352](https://github.com/user-attachments/assets/784e73a1-fac5-4feb-a979-180c711d643f)

# Todo List

- [x] choose api
- [x] implement automated tests for CRUD operations (invalid in this with Finnhub api)
- [ ] response structure
- [x] status code and error message validation for invalid inputs
- [ ] simulate high traffic 
- [x] automation frameworks using selenium (invalid in this project since no ui interaction, but i implemented a workaround)
- [ ] document test plan
- [ ] visulizations

# Part 1: API Testing

1. **API Choice:** i choose to go with FinnHub for this project, however i learned midway through that finnhub doesnt offer full CRUD capabilities like some other learning api's might have. This is fine as i still test it and validate it with external data using Selenium.

2. **Automated Test Validations**