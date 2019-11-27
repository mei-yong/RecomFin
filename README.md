# Santander bank product recommendation model in a graph database using Python & Neo4j

### Method
1) Spanish data downloaded from Kaggle
	* https://www.kaggle.com/c/santander-product-recommendation/data
2) Data cleansing done in Python - see the cleanse.py
	* Translated column names from Spanish to English
	* Dealt with nulls
	* Cleaned up data where columns contained data of the incorrect format
	* Converted categorical column contents to full descriptions
	* Converted Y/N (or rather si or no) columns to 1s and 0s
3) Data prep for graph db import done in Python - see graphdb_prep.py
	* Extracted out the product types into its own CSV for easier node creation later
	* Extracted out customer IDs and a string of their products for easier edge creation later
4) Created nodes and edges/relationships in Neo4j using Python py2neo library in iPython notebook to be able to embed images for user viewing but could be converted to a Python file to be executable


