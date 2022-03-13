from time import sleep
import requests
from bs4 import BeautifulSoup
from model.school import School
from service.school_service import get_school_for_city
from service.csv_service import CsvService
import time

def init_file(file_path):
    csv_file = CsvService(file_path = file_path)
    header = School.get_data_header_array()
    csv_file.append(header)
    return csv_file

def do_task(city_name, city_code):
    file_path = './result/' + city_name + '.csv'
    csv_file = init_file(file_path)

    for school in get_school_for_city(city_code):
        # show data
        school.display()
        data = school.to_array()
        csv_file.append(data)
        time.sleep(0.2)

if __name__ == '__main__':
    #do_task('台北市', '#city20')
    #do_task('新北市', '#city21')
    #do_task('基隆市', '#city24')
    #do_task('桃園市', '#city33')
    #do_task('新竹縣', '#city36')
    #do_task('新竹市', '#city35')
    #do_task('苗栗縣', '#city37')
    do_task('台中市', '#city42')
    do_task('彰化縣', '#city47')
    do_task('雲林縣', '#city55')
    do_task('嘉義市', '#city52')
    do_task('嘉義縣', '#city53')
    do_task('台南市', '#city62')
    do_task('高雄市', '#city70')
    do_task('屏東縣', '#city87')
    do_task('南投縣', '#city49')
    do_task('宜蘭縣', '#city39')
    do_task('花蓮縣', '#city38')
    do_task('台東縣', '#city89')
    do_task('澎湖縣', '#city69')
    do_task('金門縣', '#city82')
    do_task('連江縣', '#city83')
    do_task('台北市', '#city20')