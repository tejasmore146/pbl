# CET Scraper

This project aims to collect data from publically available pdfs found at the Official sites of the state CET cell.

## Goals :

Collect all the valid data that exists in the pdfs.

Automate the scraping to work for the past year and the following year.

Reference links:

2022 Data: [https://fe2022.mahacet.org/StaticPages/frmInstituteWiseAllotmentList?did=2021](https://fe2022.mahacet.org/StaticPages/frmInstituteWiseAllotmentList?did=2021)

2021 Data: [https://fe2021.mahacet.org/StaticPages/frmInstituteWiseAllotmentList?did=2020](https://fe2021.mahacet.org/StaticPages/frmInstituteWiseAllotmentList?did=2020)

## Checklist :

- [x]  Decide on a scraping method to use
- [x]  Start collecting raw data to text files
- [x]  Start making sense of the text files
- [x]  Write individual functions to make the text legible
- [x]  List out the logic used in the documentation
- [x]  Rewrite all of it in a single file while using function definitions
- [ ]  Keep implementing more logic

## Logic :

- [x]  Remove header and footer
- [x]  Remove the Candidate Seat type line
- [x]  Remove lines with Minority Seats
- [x]  Merge Lines that are split because of Long names
- [x]  Merge the line with State Level Seats
- [ ]  Merge score type into one line
- [ ]  Do something about the Page Number