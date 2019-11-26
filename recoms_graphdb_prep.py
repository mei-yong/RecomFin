
"""
Prepare the data to be suitable for Neo4j importing
Author: Mei Yong
https://github.com/mei-yong/bank_product_recommendations

"""

import pandas as pd
import numpy as np


# Create list of product types to be made into nodes

df = pd.read_csv(r"C:\Users\shaom\Desktop\neo4j\santander_recom\santander_cust_products_clean_sample.csv")

prod_cols = (list(df.columns))[23:]

prod_types = pd.DataFrame({'prod_id': list(range(1,24)),
                           'product_type': prod_cols})

prod_types.to_csv("santander_products.csv", index=False)


# Create the CSVs mapping customer IDs with lists of products they bought to be made into edges

df = pd.read_csv(r"C:\Users\shaom\Desktop\neo4j\santander_recom\santander_cust_products_clean_50k.csv")

prod_cols = (list(df.columns))[23:]

prod_df = df[['cust_id']+prod_cols]

for col in prod_df[prod_cols]:
    prod_df[col] = prod_df[col].map({1:col,0:np.nan})
    
prod_df['product_type'] = str(prod_df[prod_cols].values.tolist())

for x in prod_df['product_type']:
    x = x[1:-1]


prod_df_final = prod_df[['cust_id','product_type']]

prod_df_final.to_csv(r"C:\Users\shaom\Desktop\neo4j\santander_recom\santander_cust_products_rels_50k.csv",index=False)

test = prod_df.head()