'''


[dict scraping]
https://arguswaikhom.medium.com/web-scraping-word-meaning-with-beautifulsoup-99308ead148a

[st]
https://github.com/sanketchavan5595/stwebapp/blob/main/app.py


12/3/23

- Built the engine and UI with starbucks coffee


'''

import requests
from bs4 import BeautifulSoup as bs
import lxml.etree as xml
import lxml

import requests
from bs4 import BeautifulSoup as bs

import sys
import requests
from datetime import datetime
from bs4 import BeautifulSoup

import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title


def show_origin(soup):
    try:
        origin = soup.find('span', {'unbox': 'wordorigin'})
        print('\nOrigin -> ', origin.text)
    except AttributeError:
        pass


def show_definitions(soup):
    print()
    senseList = []
    senses = soup.find_all('li', class_='sense')
    for i, s in enumerate(senses):
        definition = s.find('span', class_='def').text
        st.markdown(f'{i+1}.  {definition}')

        # Examples
        examples = s.find_all('ul', class_='examples')
        for e in examples:
            for ex in e.find_all('li'):
                #st.write('\t-', ex.text)
                st.markdown(f'---- {ex.text}')

        st.markdown("---")
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("app.py", "Dictionary"),
        #Page("pages/update_params.py", "Update Param Vals"),
        # Unless you explicitly say in_section=False
        Page("pages/todo.py", "To Do"),
        Page("pages/links.py", "Links", in_section=False),
        #Page("pages/images.py", "Image Gallery", in_section=False),

    ]
)

if 'keyword' not in st.session_state:
    st.session_state.keyword = ""


form = st.form("my_form")
keyword = form.text_input("")

find_button = form.form_submit_button("Find")


if find_button:

    scrape_url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + keyword
    headers = {"User-Agent": ""}
    web_response = requests.get(scrape_url, headers=headers)

    if web_response.status_code == 200:
        #st.markdown(scrape_url, unsafe_allow_html=True)
        st.markdown(f'''
        Click to hear: <a href = {scrape_url}> Oxford Dict </a>
        ''', True)

        soup = BeautifulSoup(web_response.text, 'html.parser')

        try:
            # show_origin(soup)
            show_definitions(soup)
        except AttributeError:
            print('Word not found!!')
    else:
        print('Failed to get response...')

