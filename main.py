from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver')

for i in range(24):
    driver.get('https://www.99acres.com/property-in-indore-ffid-page-'+str(n))

    content = driver.page_source
    soup = BeautifulSoup(content)
    results =  soup.findAll('div', attrs = {'class' : 'pageComponent srpTuple__srpTupleBox srp'})

    Configuration = []
    Description = []
    Location_Bldng_name = []
    Seller_name = []
    Price = []
    Price_unit = []
    Area = []
    Type_area = []

    for row in results:

        Configuration.append(row.h2.text)

        Location_Bldng_name.append(row.find('td', attrs = {'class' : 'list_header_bold srpTuple__spacer10'}).get_text())

        Seller_name.append(row.find('div', attrs = {'class' : 'list_header_semiBold'}).get_text())

        Description.append(row.find('div', attrs = {'class' : 'srpTuple__descMore body_med'}).get_text())

        Type_area.append(row.find('div', attrs = {'class' : 'caption_subdued_small',
                                                'id' : 'srp_tuple_secondary_area'}).get_text())

        Price.append(row.find('td', attrs = {'class' : 'srpTuple__midGrid title_semiBold srpTuple__spacer16',
                                            'id' : 'srp_tuple_price'}).text[0:5])

        Price_unit.append(row.find('td', attrs = {'class' : 'srpTuple__midGrid title_semiBold srpTuple__spacer16',
                                            'id' : 'srp_tuple_price'}).text[4:8])

        Area.append(row.find('td', attrs = {'class' : 'srpTuple__midGrid title_semiBold srpTuple__spacer16',
                                            'id' : 'srp_tuple_primary_area'}).text[0:11])

    df = pd.DataFrame({
        'Configuration' : Configuration,
        'Location/Bldng_name' : Location_Bldng_name,
        'Seller Name' : Seller_name,
        'Description' : Description,
        'Area' : Area,
        'Area type' : Type_area,
        'Price' : Price,
        'Price Unit' : Price_unit
    })

    df.to_csv(r'C:\\Users\\vivek\\Desktop\\99acres Scrapper\\99acres.csv', header=False, mode = 'a')