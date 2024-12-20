import requests
from django.apps import apps
from django.utils import timezone
from celery import shared_task
from helpers import extract_amazon_product_data, fetch_html


@shared_task
def scrape_product_url_task(url):
    ProductScrapeEvent = apps.get_model('products', 'ProductScrapeEvent')
    html = fetch_html(url)
    product_data = extract_amazon_product_data(html)
    event = ProductScrapeEvent.objects.create_scrape_event(product_data, url=url)
    return event.id

@shared_task
def scrape_products_task():
    Product = apps.get_model('products', 'Product')
    qs = Product.objects.filter(active=True)
    for obj in qs:
        url = obj.url
        scrape_product_url_task.delay(url)
