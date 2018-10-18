Problem 2
=========

Approach 1
----------

Python script which in following steps pulls data:
- downloads zip archive
- extracts contained CSVs

### Usage

```bash
cd problem2
pip install requests
python download.py -u https://www150.statcan.gc.ca/n1/en/tbl/csv/17100009-eng.zip
```

Approach 2
----------------------------

Selenium engine based page scrapping. Steps:

- navigate to required page
- open table customizations
- select required time period
- parse HTML
- output to CSV


