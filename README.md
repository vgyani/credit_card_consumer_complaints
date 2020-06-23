# Consumer Complaints

## Table of Contents
1. [Problem](README.md#problem)
1. [Instructions](README.md#instructions)
1. [Input Dataset](README.md#input-dataset)
1. [Output](README.md#expected-output)
1. [Repo directory structure](README.md#repo-directory-structure)
1. [Testing your code](README.md#testing-your-code)

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This project is about identifying the number of complaints filed and how they're spread across different companies. 

** We want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

## Instructions
To complete the project, I have only used the default data structures that come with Python. For example, I haven't used Pandas or any other external libraries (i.e., not used Python modules that must be installed using 'pip').

The objective here is to showcase that I can implement the solution using basic data structure building blocks and software engineering best practices (by writing clean, modular, and well-tested code).

## Input dataset
An input file, `complaints.csv`, sits in the top-most `input` directory of the repository. The code reads that input file, processes it and writes the results to an output file, `report.csv` in the top-most `output` directory of the repository.

Below are the contents of an example `complaints.csv` file: 
```
Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
2019-10-24,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
```
Each line of the input file, except for the first-line header, represents one complaint. Consult the [Consumer Finance Protection Bureau's technical documentation](https://cfpb.github.io/api/ccdb/fields.html) for a description of each field.  

* Notice that complaints are not listed in chronological order
* In 2019, there was a complaint against `TRANSWORLD SYSTEMS INC` for `Debt collection` 
* Also in 2019, `Experian Information Solutions Inc.` received one complaint for `Credit reporting, credit repair services, or other personal consumer reports` while `TRANSUNION INTERMEDIATE HOLDINGS, INC.` received two
* In 2020, `Experian Information Solutions Inc.` received a complaint for `Credit reporting, credit repair services, or other personal consumer reports`

In summary that means 
* In 2019, there was one complaint for `Debt collection`, and 100% of it went to one company 
* Also in 2019, three complaints against two companies were received for `Credit reporting, credit repair services, or other personal consumer reports` and 2/3rd of them (or 67% if we rounded the percentage to the nearest whole number) were against one company (TRANSUNION INTERMEDIATE HOLDINGS, INC.)
* In 2020, only one complaint was received for `Credit reporting, credit repair services, or other personal consumer reports`, and so the highest percentage received by one company would be 100%

For this challenge, we want for each product and year that complaints were received, the total number of complaints, number of companies receiving a complaint and the highest percentage of complaints directed at a single company.

For the purposes of this challenge, all names, including company and product, should be treated as case insensitive. For example, "Acme", "ACME", and "acme" would represent the same company.

## Output

After reading and processing the input file, the code creates an output file, `report.csv`, with as many lines as unique pairs of product and year (of `Date received`) in the input file. 

Each line in the output file lists the following fields in the following order:
* product (name should be written in all lowercase)
* year
* total number of complaints received for that product and year
* total number of companies receiving at least one complaint for that product and year
* highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, is rounded to 1% and anything less than 0.5% should round to 0%)

The lines in the output file are sorted by product (alphabetically) and year (ascending)

Below are the contents of an example `report.csv` file: 
```
"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100
```
Notice that because `debt collection` was only listed for 2019 and not 2020 in the example input file, the output file only has a single entry for debt collection. Also, notice that when a product has a comma (`,`) in the name, the name is enclosed by double quotation marks (`"`). Finally, notice that percentages are listed as numbers and do not have `%` in them.

## Repo directory structure
The top-level directory structure for your repo should look like the following: (So that we can grade your submission, replicate this directory structure at the top-most level of your project repository. Do not place the structure in a subdirectory)

    ├── README.md
    ├── run.sh
    ├── src
    │   └── consumer_complaints.py
    ├── input
    │   └── complaints.csv
    ├── output
    |   └── report.csv
    └── tests
        └── test_1
        |   ├── input
        |   │   └── complaints.csv
        |   |__ output
        |   │   └── report.csv
        ├── test_2
            ├── input
            │   └── complaints.csv
            |── output
                └── report.csv

## Assumptions/ Working:
1) Any row with a problem in data quality will be skipped
2) Dates are expected to be in yyyy-mm-dd format
