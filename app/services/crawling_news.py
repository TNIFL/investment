from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from app.services.gpt_services import classify_news, news_summary_by_gpt
from app.services.news_service import *

def crawling_naver_news():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    section_codes = range(100, 106)

    for section in section_codes:
        driver.get(f'https://news.naver.com/section/{section}')
        #time.sleep(1)

        links = driver.find_elements(By.CSS_SELECTOR, 'div.sa_text a.sa_text_title')
        """
        urls = []
        for elem in links:
            url = elem.get_attribute('href')
            urls.append(url)
        """
        urls = [elem.get_attribute('href') for elem in links]

        print(urls)
        print(f'총 추출한 링크 수 : {len(urls)}')

        for url in urls:
            driver.get(url)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            title_tag = soup.select_one('h2.media_end_head_headline')
            content_tag = soup.select_one('#dic_area')
            time_tag = soup.select_one('span.media_end_head_info_datestamp_time')

            news_url = url
            news_title = title_tag.text.strip() if title_tag else '제목없음'
            news_content = content_tag.text.strip() if content_tag else '내용없음'
            news_upload_time = time_tag.text.strip() if time_tag else '시간없음'

            summary = news_summary_by_gpt(news_content)
            category = classify_news(news_title, news_content)

            news_upload_time_to_datetime = parse_korean_datetime(news_upload_time)

            print('-' * 100)
            print('url : ', news_url)
            print('업로드 시간 : ', news_upload_time_to_datetime)
            print('제목 : ', news_title)
            print('내용 : ', news_content[:200])
            print('분야 : ', category)
            print('요약 : ', summary)
            print('-' * 100)
            if category and summary:
                save_news_with_category(news_title, news_content, summary, category, news_url, news_upload_time_to_datetime)
            else:
                print('오류 발생으로 인한 프로그램 종료')







    driver.quit()

    #여기서 바로 뉴스 카테고리 분류 후 db에 저장까지


