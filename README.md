# Nutrition Data Unit Conversion Tool

## Overview
This Python script processes survey food intake data by mapping each food item to a reference nutrient database (FPED). It scales nutrient values based on reported serving sizes, outputs a comprehensive CSV with calculated nutrient intakes, and logs unmatched food codes for review. This tool is ideal for dietary research and nutritional analysis.

## Features
- Maps survey food codes to reference nutrient database.
- Scales nutrient values according to serving size.
- Generates an output CSV with calculated nutrient intakes.
- Logs unmatched food codes for further investigation.
- Handles numeric data safely and efficiently.

## Requirements
- Python 3.x
- pandas library

Install pandas if you don’t have it:
```bash
pip install pandas
