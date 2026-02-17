import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        pass

    #this saves the csv to the local directory
    def get_dataset(self):
        data_url = 'https://catalog.data.gov/dataset/'
        #request
        data_website = requests.get(data_url).text
        data_soup = BeautifulSoup(data_website, 'html.parser')
        
        #find the href the main dataset 
        cons_url = 'https://catalog.data.gov'
        data_name = data_soup.find('h3', {'class' : 'dataset-heading'})
        a_tag = data_name.find('a')
        if a_tag:
            title = cons_url + a_tag['href']

        #download the dataset
        dataset_website = requests.get(title).text
        dataset_soup = BeautifulSoup(dataset_website, 'html.parser')
        
        #get the json file
        json_file = dataset_soup.find_all('a', {'class' : 'btn btn-primary'})
        link_list = []
        for href in json_file:
            links = href['href']
            link_list.append(links)
        
        #saving the official json link to download
        official_jsonlink = link_list[0]
        
        #path for saving
        csv_path = r'D:\desktop\Projects\PROJECT_7_ETL_WITH_API\TASK1_PYTHON_SCRAPER\FILES\samp_csv.csv'

        response = requests.get(official_jsonlink)

        #save the json file
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

    if __name__ == '__main__':
        get_dataset()
    