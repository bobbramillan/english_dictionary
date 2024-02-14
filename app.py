import requests
from bs4 import BeautifulSoup
import streamlit as st

def get_word_definition(keyword):
    scrape_url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + keyword
    headers = {"User-Agent": ""}
    web_response = requests.get(scrape_url, headers=headers)

    if web_response.status_code == 200:
        soup = BeautifulSoup(web_response.text, 'html.parser')
        return soup
    else:
        return None

def show_definitions(keyword):
    soup = get_word_definition(keyword)
    if soup:
        senses = soup.find_all('li', class_='sense')
        for i, s in enumerate(senses):
            definition = s.find('span', class_='def').text
            st.markdown(f'{i+1}.  {definition}')

            examples = s.find_all('li', class_='example')
            for ex in examples:
                st.markdown(f'---- {ex.text}')
    else:
        st.error('Failed to get word definition. Please try again later.')

def main():
    st.title("Oxford Dictionary Web Scraper")

    keyword = st.text_input("Enter a word:")
    if st.button("Find"):
        show_definitions(keyword)

if __name__ == "__main__":
    main()
