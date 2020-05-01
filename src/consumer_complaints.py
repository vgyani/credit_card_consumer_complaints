#!/usr/bin/env python3
# coding: utf-8

import sys
import csv
from collections import defaultdict
from datetime import datetime

# input_filename = 'complaints.py'
# output_filename = 'report.csv'
input_filename = sys.argv[1]
output_filename = sys.argv[2]

INPUT_FILE_PATH = './input/' + input_filename
OUTPUT_FILE_PATH = './output/' + output_filename


def get_year(date_str):
    """
    Helper function for data_filter().
    Checks if the date field is valid and returns the year if it is valid
    
    Paramters: date (string)
    Return: year (string) or None
    """
    try:
        year = datetime.strptime(date_str, '%Y-%m-%d').year
        return year
    except:
        return None


def clean_text(txt):
    """
    Helper function for data_filter().
    Strips trailing and leading whitespaces, and converts th input text to lowercase
    
    Parameters: txt (string)
    Return: string
    """
    return txt.strip().lower()


def data_filter(row, num_columns):
    """
    Helper function for read_csv().
    Filters any row with data quality issues (number of columns less than expected, invalid data format),
    and extracts [year, product, company] from the row
    
    Parameters: row (list): list with all values in one row of the csv file
                num_columns (int): number of expected values in the row
    Return: [year, product, company] (list) or None
    """
    if len(row) != num_columns:
        print('skipping row: invalid no. of columns')
        return None
    year = get_year(row[0])
    if year is None:
        print('skipping row: invalid date format')
        return None
    else:
        return [year, clean_text(row[1]), clean_text(row[7])]


def read_csv(file_path):
    """
    Reads the input csv file, parses it, filters bad data and returns a dictionary with all product, year,
    company and complaint count.
    
    Parameters: file_path (string)
    Return: {(product, year):{company:count}} (dict(dict(int)))
    """
    print('Input path: ', file_path)
    print('Reading input file...')
    data_dictionary = defaultdict(lambda: defaultdict(int))
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        header_row = next(csv_reader)
        num_columns = len(header_row)
        for row in csv_reader:
            filtered_row = data_filter(row, num_columns)
            if filtered_row is None:
                continue
            else:
                year, product, company = filtered_row
            data_dictionary[(product,year)][company] += 1
    print('Read complete!')
    return data_dictionary


def analyse_data(product_year_dict):
    """
    Analyses the input data to get complaint statistics for each year, product combination in unsorted order
    
    Parameters: data dictionary --> {(product, year):{company:count}}
    Return: [product, year, total_num_of_complaints, \
                total_num_of_companies, highest_complaint_percent] (list)
    """
    print('Analysing data...')
    report_output = []
    for product_year_companies_complaintCount in product_year_dict.items():
        product_year, companies_complaintCount = product_year_companies_complaintCount
        total_num_of_companies = len(companies_complaintCount)
        total_num_of_complaints = 0
        max_complaints_against_one_company = 0
        for company_count in companies_complaintCount.items():
            company, num_complaints = company_count
            total_num_of_complaints += num_complaints
            if num_complaints > max_complaints_against_one_company:
                max_complaints_against_one_company = num_complaints
        highest_complaint_percent = round(max_complaints_against_one_company/total_num_of_complaints*100)
        report_output.append([product_year[0], product_year[1], total_num_of_complaints, \
                total_num_of_companies, highest_complaint_percent])
    print('Analysis complete!')
    return report_output


def sort_write_csv(report_list, output_path):
    """
    Sorts the input list and writes it to a csv file
    """
    print('Output path: ', output_path)
    print('Writing output...')
    sorted_by_product_year = sorted(report_list, key=lambda x: (x[0], x[1]))
    with open(output_path, "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(sorted_by_product_year)
    print('Write complete!')


def main():
    data_dict = read_csv(INPUT_FILE_PATH)
    report_output_unsorted = analyse_data(data_dict)
    sort_write_csv(report_output_unsorted, OUTPUT_FILE_PATH)

if __name__ == "__main__":
    main()