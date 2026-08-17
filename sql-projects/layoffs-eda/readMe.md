Layoffs Data Cleaning & Exploratory Analysis
Problem / Objective

A raw global layoffs dataset contained duplicates, inconsistent formatting, and messy null values. The goal was to clean the dataset into an analysis-ready state, then explore it to identify trends in layoffs by company, industry, country, and time period.

Approach
Tools: MySQL
Removed duplicate records using window functions (ROW_NUMBER() partitioned over key columns)
Standardised inconsistent text fields (company names, industry labels, country names) and trimmed whitespace
Handled null/blank values, either populating them from related rows or removing unusable records
Used CTEs and window functions to explore layoffs by company, industry, and country
Calculated a rolling monthly total of layoffs to track the trend over time
