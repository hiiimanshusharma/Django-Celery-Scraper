## Amazon Product Scraper
- Scheduled Amazon product scraper with django for backend using celery for doing background jobs

### Setup:
##### setting up redis, flower, prometheus as containers
```
$ sudo docker-compose up -d
```

##### check containers
```
$ sudo docker ps
```

#### starting server
```
$ python manage.py runserver
```

#### celery 
```
$ celery -A config worker --beat -l info
```

### Monitoring celery tasks using flower
localhost:5555
![Alt text](images/celery-flower.png)

---
[![Django Badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)](#) [![Celery Badge](https://img.shields.io/static/v1?style=for-the-badge&message=Celery&color=37814A&logo=Celery&logoColor=FFFFFF&label)](#) [![Prometheus Badge](https://img.shields.io/badge/Prometheus-000000?style=for-the-badge&logo=prometheus&labelColor=000000)](#) [![Redis Badge](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](#) [![selenium Badge](https://img.shields.io/badge/-selenium-43B02A?style=for-the-badge&labelColor=black&logo=selenium&logoColor=43B02A)](#) [![docker Badge](https://img.shields.io/badge/-docker-2496ED?style=for-the-badge&labelColor=black&logo=docker&logoColor=2496ED)](#)