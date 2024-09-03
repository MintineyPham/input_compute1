"""
File: project1/input_compute_output.py
Initial developers: Professors Gitlitz and Sabin
Student developers: Mintiney Pham 
Date: Sep 3 2024 
"""

print("Initial Question: get minutes from years")
print("========================================")
years_str = input("Enter the number of years: ")
years = int(years_str)
days = years * 365
hours = days * 24
minutes = hours * 60
print(f"There are {minutes} minutes in {years} year(s)")

print("Question 1: get seconds from years")
print("========================================")
years_str = input("Enter the number of years: ")
years = int(years_str)
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"There are {seconds} seconds in {years} year(s)")


### Q2 Answer ###
print("Question 2: get years from seconds")
print("========================================")
seconds_str = input("Enter the number of secpnds: ")
years = int(seconds_str)
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"There are {years} years in {seconds} seconds(s)")

### Q3 Answer ### 
print("Initial Question: get minutes from years")
print("========================================")
years_str = input("Enter the number of years: ")
years = int(years_str)
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60 
print(f"There are {seconds} seconds, {minutes} minutes, {hours} hours in {years} year(s)")