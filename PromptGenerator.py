#pip install requests
#pip install bs4
#python PromptGenerator.py
import requests
from bs4 import BeautifulSoup

# Base URL for The Verge
BASE_URL = "http://www.theverge.com"
BASE_URL = "http://www.yahoo.com"

# --- Helper function to scrape articles from a given URL and parse specific elements ---
def scrape_articles(url, section_type, is_popular_list=False):
    """
    Scrapes article titles, links, and assigns an engagement score.

    Args:
        url (str): The URL to scrape.
        section_type (str): Descriptor for the source section (e.g., "Tech", "Science").
        is_popular_list (bool): True if scraping a 'Most Popular' or 'Trending' list,
                                 which allows assigning engagement based on rank.

    Returns:
        list: A list of dictionaries, each containing 'title', 'link', 'engagement', 'source'.
    """
    print(f"Fetching articles from: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    articles_data = []

    if is_popular_list:
        # This targets the "Trending Now" section commonly found on the homepage
        trending_section = soup.find('div', class_='c-trending-now-list')
        if trending_section:
            list_items = trending_section.find_all('li')
            for i, li in enumerate(list_items):
                link_tag = li.find('a')
                if link_tag and link_tag.get_text(strip=True):
                    title = link_tag.get_text(strip=True)

scrape_articles(BASE_URL, "", is_popular_list=False)