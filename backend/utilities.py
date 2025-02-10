from datetime import date
import logging
import json
import requests
import time
from flask import current_app

from data_handler import JsonObject, addEntry



#url=f"https://www.immobiliare.it/api-next/search-list/real-estates/?vrt=41.104579%2C14.31879%3B41.099017%2C14.272099%3B41.070163%2C14.250641%3B41.037542%2C14.272614%3B41.022391%2C14.288063%3B41.023298%2C14.324284%3B41.033399%2C14.34454%3B41.064339%2C14.362907%3B41.090996%2C14.348831%3B41.104579%2C14.31879&idContratto=1&idCategoria=1&__lang=it&pag={count_page}&paramsCount=6&path=%2Fsearch-list%2F"
_DEBUG=False
_DELAY=15
logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)

logger = logging.getLogger()

def fetch_data(page_number):
    url=f"https://www.immobiliare.it/api-next/search-list/real-estates/?vrt=41.104579%2C14.31879%3B41.099017%2C14.272099%3B41.070163%2C14.250641%3B41.037542%2C14.272614%3B41.022391%2C14.288063%3B41.023298%2C14.324284%3B41.033399%2C14.34454%3B41.064339%2C14.362907%3B41.090996%2C14.348831%3B41.104579%2C14.31879&idContratto=1&idCategoria=1&boxAuto[0]=1&boxAuto[1]=3&boxAuto[2]=4&__lang=it&minLat=39.156826&maxLat=42.913068&minLng=14.229242&maxLng=14.379274&pag={page_number}&paramsCount=11&path=%2Fsearch-list%2F"

    logging.debug(url)
    logging.debug(" ")
    logging.debug(" ")

    try:
        response = requests.get(url)
        logging.debug(response)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse response as JSON
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")
        return None
    except ValueError:
        print("Error decoding JSON response.")
        return None


def start_search_scraping():
    count_page = 1
    _DEBUG = False
    _DELAY = 15

    if not _DEBUG:
        logger.info(
            "Debug is disabled. You can define DEBUG environment variable to enable it."
        )
    else:
        logger.setLevel("DEBUG")

    json_data = fetch_data(count_page)
    logger.debug(json_data.get('count', 0))
    max_page = json_data.get('maxPages', 0)
    logger.info(f"Number of pages {max_page}")
    yield f"Number of pages {max_page}"

    while count_page <= max_page:
        time.sleep(_DELAY)
        logger.info(f"Risultati in pagina {count_page}")
        yield f"Risultati in pagina {count_page}"

        json_data = fetch_data(count_page)
        results = json_data.get('results', [])
        count_page += 1

        for res in results:
            try:
                logger.debug(res.get('realEstate', {}))
                logger.debug(" ")

                advertiser = res.get('realEstate', {}).get('advertiser', {})

                if 'supervisor' in advertiser and isinstance(advertiser['supervisor'], dict):
                    if 'type' in advertiser['supervisor'] and advertiser['supervisor']['type'] == 'user':
                        logger.info(res.get('seo', {}))

                        house = JsonObject(
                            id=res['realEstate'].get('id', "unknown"),
                            title=res.get('seo', {}).get('anchor', "No Title"),
                            price=res['realEstate'].get('price', {}).get('value',
                                res['realEstate'].get('price', {}).get('formattedValue', "No Price")),
                            formattedValue=res['realEstate'].get('price', {}).get('formattedValue', "No Price"),
                            link=f"https://www.immobiliare.it/annunci/{res['realEstate'].get('id', 'unknown')}/",
                            img=res['realEstate'].get('properties', [{}])[0].get('photo', {}).get('urls', {}).get('medium', ""),
                            date_added=str(date.today()),
                            clicked=False
                        )

                        yield from addEntry(house)

                        logger.info(f"Titolo: {house.title} - {house.formattedValue}")
                        logger.info(f"Link: {house.link}")

            except Exception as e:
                logger.error(f"Skipping entry due to error: {e}")
                continue  # Skip the current entry and continue the loop


if __name__ == "__main__":
    start_search_scraping()
