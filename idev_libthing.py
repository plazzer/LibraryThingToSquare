#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


import configparser
config = configparser.ConfigParser()
config.read('config.ini')

business_name = config['business']['business_name']


# In[ ]:


catalog = pd.read_csv('data/librarything_plazzer.tsv', sep='\t')


# In[ ]:


column_names = [
 #       'Reference Handle',
        'Token',
        'Item Name',
        'Variation Name',
        'SKU',
        'Description',
        'Categories',
        'Reporting Category',
        'GTIN', 
        'Item Type',
        'Weight (kg)',
        'Social Media Link Title',
        'Social Media Link Description',
        'Price',
        'Online Sale Price',
        'Archived',
        'Sellable',
        'Contains Alcohol',
        'Stockable',
        'Skip Detail Screen in POS',
        'Option Name 1',
        'Option Value 1',
        'Default Unit Cost',
        'Default Vendor Name',
        'Default Vendor Code',
        f"Current Quantity {business_name}",
        f"New Quantity {business_name}",
        f"Stock Alert Enabled {business_name}",
        f"Stock Alert Count {business_name}"
        ]


# In[ ]:


reference_handle = None
token = None
item_name = catalog['Title'].tolist()
variation_name = None
sku = None
description = catalog['Summary'].tolist()
categories = catalog['Subjects'].tolist()
reporting_category = "Books"
gtin = None
item_type = "Physical"
weight = (catalog['Weight'].str.extract(r'([\d.]+)').astype(float) * 0.453592)[0].tolist() # Convert pounds to kg
social_media_link_title = None
social_media_link_description = None
price = None
online_sale_price = None
archived = None
sellable = None
contains_alcohol = "No"
stockable = None
skip_detail_screen_in_pos = None
option_name_1 = "Author"
option_value_1 = catalog['Primary Author'].tolist()
default_unit_cost = None
default_vendor_name = None
default_vendor_code = None
current_quantity = None
new_quantity = None
stock_alert_enabled = None
stock_alert_count = None


# In[ ]:


output = pd.DataFrame({
    #'Reference Handle': reference_handle,
    'Token': token, 
    'Item Name': item_name,
    'Variation Name': variation_name,
    'SKU': sku,
    'Description': description,
    'Categories': categories,
    'Reporting Category': reporting_category,
    'GTIN': gtin,
    'Item Type': item_type,
    'Weight (kg)': weight,
    'Social Media Link Title': social_media_link_title,
    'Social Media Link Description': social_media_link_description,
    'Price': price,
    'Online Sale Price': online_sale_price,
    'Archived': archived,
    'Sellable': sellable,
    'Contains Alcohol': contains_alcohol,
    'Stockable': stockable,
    'Skip Detail Screen in POS': skip_detail_screen_in_pos,
    'Option Name 1': option_name_1,
    'Option Value 1': option_value_1,
    'Default Unit Cost': default_unit_cost,
    'Default Vendor Name': default_vendor_name,
    'Default Vendor Code': default_vendor_code,
    f'Current Quantity {business_name}': current_quantity,
    f'New Quantity {business_name}': new_quantity,
    f'Stock Alert Enabled {business_name}': stock_alert_enabled,
    f'Stock Alert Count {business_name}': stock_alert_count
    })


# In[ ]:


output['Option Value 1'] = output['Option Value 1'].fillna('No author information')

output['Item Name'] = output['Item Name'].fillna('No Item Name information').apply(lambda x: x[:96] if isinstance(x, str) else x) 
output['Description'] = output['Description'].fillna('No Description information').apply(lambda x: x[:96] if isinstance(x, str) else x) 
output['Categories'] = output['Categories'].fillna('No Categories information').apply(lambda x: x[:96] if isinstance(x, str) else x) 


# In[ ]:


#output.to_csv('data/square_bulk_upload.csv', index=False)
output.to_excel("data/square_bulk_upload.xlsx", index=False, engine='openpyxl')

