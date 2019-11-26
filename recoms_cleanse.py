
"""
Cleaning the Spanish Santander dataset
Author: Mei Yong
https://github.com/mei-yong/neo4j_recoms/

"""


# https://www.kaggle.com/c/santander-product-recommendation/data


# Import the raw data
import pandas as pd
df = pd.read_csv("data/santander_cust_products.csv")


## testing
#original_df = df.copy() 
#df = df.sample(1000)


### CLEANSING ###

# Rename the columns from Spanish to English
column_name_mapping = {
					'fecha_dato': 'date_fetched',
					'ncodpers': 'cust_id',
					'ind_empleado': 'employee_type',
					'pais_residencia': 'cust_country',
					'sexo': 'cust_gender',
					'age': 'cust_age',
					'fecha_alta': 'first_contract_date',
					'ind_nuevo': 'new_cust_last_6_months',
					'antiguedad': 'cust_seniority_months',
					'indrel': 'cust_primary',
					'ult_fec_cli_1t': 'last_date_as_primary_cust',
					'indrel_1mes': 'cust_type_at_start_of_month',
					'tiprel_1mes': 'cust_relation_type_at_start_of_month',
					'indresi': 'residence_vs_bank_country_same',
					'indext': 'birth_vs_bank_country_diff',
					'conyuemp': 'spouse_of_bank_employee',
					'canal_entrada': 'entrance_channel',
					'indfall': 'deceased',
					'tipodom': 'primary_address',
					'cod_prov': 'address_province_code',
					'nomprov': 'address_province_name',
					'ind_actividad_cliente': 'active_customer',
					'renta': 'household_gross_income',
					'segmento': 'segmentation',
					'ind_ahor_fin_ult1': 'savings_account',
					'ind_aval_fin_ult1': 'guarantees',
					'ind_cco_fin_ult1': 'current_account',
					'ind_cder_fin_ult1': 'derivada_account',
					'ind_cno_fin_ult1': 'payroll_account',
					'ind_ctju_fin_ult1': 'junior_account',
					'ind_ctma_fin_ult1': 'premium_individual_account',
					'ind_ctop_fin_ult1': 'individual_account',
					'ind_ctpp_fin_ult1': 'individual_plus_account',
					'ind_deco_fin_ult1': 'shortterm_deposit',
					'ind_deme_fin_ult1': 'medterm_deposit',
					'ind_dela_fin_ult1': 'longterm_deposit',
					'ind_ecue_fin_ult1': 'eaccount',
					'ind_fond_fin_ult1': 'funds',
					'ind_hip_fin_ult1': 'mortgage',
					'ind_plan_fin_ult1': 'pension',
					'ind_pres_fin_ult1': 'loan',
					'ind_reca_fin_ult1': 'taxes',
					'ind_tjcr_fin_ult1': 'credit_card',
					'ind_valo_fin_ult1': 'securities',
					'ind_viv_fin_ult1': 'home_account',
					'ind_nomina_ult1': 'payroll',
					'ind_nom_pens_ult1': 'pensions',
					'ind_recibo_ult1': 'direct_debit'
					}

df = df.rename(columns=column_name_mapping)

# Replace any infinites with nulls
import numpy as np
df = df.replace([np.inf, -np.inf], np.nan)

# Dealing with nulls
df = df.drop(['last_date_as_primary_cust'], axis=1) # drop the column
df['spouse_of_bank_employee'] = df['spouse_of_bank_employee'].fillna(0) # replace nulls with zero
df = df.dropna(subset=['household_gross_income']) # drop rows where gross income is null


# Clean up cells where the formatting isn't right
df['cust_age'] = df['cust_age'].astype(str).str.strip().astype(int) # string to int
df['cust_seniority_months'] = df['cust_seniority_months'].astype(str).str.strip().astype(int) # string to int
df['cust_type_at_start_of_month'] = df['cust_type_at_start_of_month'].astype(str).str.strip() # mixed to string for later renaming/categorisation
df['new_cust_last_6_months'] = df['new_cust_last_6_months'].astype(int)
df['cust_primary'] = df['cust_primary'].astype(int)
df['primary_address'] = df['primary_address'].astype(int)
df['active_customer'] = df['active_customer'].astype(int)



# Convert the data in columns based on mappings

employee_type = {'A': 'active',
				'B': 'ex_employee',
				'F': 'filial',
				'N': 'not_employee',
				'P': 'passive'}
df['employee_type'] = df['employee_type'].map(employee_type)


cust_primary = {1: 'primary',
				99: 'primary_at_beginning_but_not_end_of_month'}
df['cust_primary'] = df['cust_primary'].map(cust_primary)

			
cust_type_at_start_of_month = {'1': 'primary',
                               '1.0': 'primary',
                               '2': 'co-owner',
                               '2.0': 'co-owner',
                               'P': 'potential',
                               '3': 'former_primary',
                               '3.0': 'former_primary',
                               '4': 'former_co-owner',
                               '4.0': 'former_co-owner'}
df['cust_type_at_start_of_month'] = df['cust_type_at_start_of_month'].map(cust_type_at_start_of_month)

									
cust_relation_type_at_start_of_month = {'A': 'active',
										'I': 'inactive',
										'P': 'former_customer',
										'R': 'potential'}
df['cust_relation_type_at_start_of_month'] = df['cust_relation_type_at_start_of_month'].map(cust_relation_type_at_start_of_month)

										
residence_vs_bank_country_same = {'S': 1,
								'N': 0}
df['residence_vs_bank_country_same'] = df['residence_vs_bank_country_same'].map(residence_vs_bank_country_same)

								
birth_vs_bank_country_diff = {'S': 1,
							'N': 0}
df['birth_vs_bank_country_diff'] = df['birth_vs_bank_country_diff'].map(birth_vs_bank_country_diff)


deceased = {'S': 1,
			'N': 0}
df['deceased'] = df['deceased'].map(deceased)

			
segmentation = {'01 - TOP': 'VIP',
				'02 - PARTICULARES': 'individual',
				'03 - UNIVERSITARIO': 'college_graduate'}
df['segmentation'] = df['segmentation'].map(segmentation)



# Export to a CSV
df.to_csv('data/santander_cust_products_clean.csv')












