
"""
Prepare the data to be suitable for Neo4j importing
Author: Mei Yong
https://github.com/mei-yong/bank_product_recommendations

"""

import pandas as pd
import numpy as np


# Create list of product types to be made into nodes

df = pd.read_csv("data/santander_cust_products_clean_sample.csv")

prod_cols = (list(df.columns))[23:]

prod_types = pd.DataFrame({'prod_id': list(range(1,24)),
                           'product_type': prod_cols})

prod_types.to_csv("santander_products.csv", index=False)



# Create the CSVs mapping customer IDs with lists of products they bought to be made into edges

df = pd.read_csv("data/santander_cust_products_clean_50k.csv")
#df = pd.read_csv("data/santander_cust_products_clean_100k.csv")

prod_cols = (list(df.columns))[23:]

prod_df = df[['cust_id']+prod_cols]

for col in prod_df[prod_cols]:
    prod_df[col] = prod_df[col].map({1:col,0:None})
    
prod_df['product_type'] = prod_df[prod_cols].values.tolist()

prod_df = prod_df[['cust_id','product_type']]


def convert_to_concat(input_list):
    string = ""
    for prod_type in input_list:
        if prod_type is not None:
            if string == "":
                string += str(prod_type)
            else:
                string += ";" + str(prod_type)
    return string


prod_df['product_type'] = prod_df['product_type'].apply(lambda x: convert_to_concat(x))
    
cust_products = prod_df.replace(r'^\s*$', np.nan, regex=True)
    

cust_products.to_csv("data/cust_prod_rels.csv", index=False)


















