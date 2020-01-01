# RecomFin
#### Model Santander bank customer and financial products data in a graph database - Python, Neo4j
#### Note: This is a work in progress - see github.com/mei-yong/RecomMovies for a more end-to-end project


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


### Example of 2 customers with multiple financial products in common
![alt text](https://github.com/mei-yong/RecomFin/blob/master/images/example1.JPG)
