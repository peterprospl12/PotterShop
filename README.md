# PotterShop

Project PotterShop aims to copy internet shop [Pottermania.pl](https://pottermania.pl) using [Prestashop 1.7.8](https://github.com/PrestaShop/PrestaShop/tree/1.7.8.x) platform. The project also aims to clone product information from the mother website using a scraper and create automated tests using Selenium to ensure quality and functionality.

---

## Content
- [About Project](#about-project)
- [Repository Structure](#repository-structure)
- [Used Tools](#used-tools)
- [Installation Instructions](#installation-instructions)
- [Team](#team)

---

## About Project
PotterShop is an e-commerce platform designed to replicate the look and products from [Pottermania.pl](https://pottermania.pl). The main features include product browsing, searching, and a shopping cart system. The project will utilize web scraping to import product data from the original site and Selenium for automated testing to ensure the website operates smoothly.

## Repository Structure
The contents of the repository are divided into the following folders:
1. **/prestashop** -> source code for the store;
2. **/tests** -> source code for automated tests;
3. **/scraper** -> source code for the scraping tool;
4. **/scraper-results** -> results of the scraping;
5. **/scripts** -> scripts used while developing and deploying the app;
6. **/api** -> source code for the API, mainly used to add scraped products to the shop;
7. **/ssl** -> directory containing SSL certificates and related files;
8. **/tests** -> directory containing automated test scripts written in Selenium;
9. **docker-compose.yml** -> Docker Compose file;
10. **permissions.sh** -> script to set the necessary permissions for the project files;



## Used Tools
- [Prestashop 1.7.8 Docker Image](https://github.com/PrestaShop/PrestaShop/tree/1.7.8.x)
- [MariaDB Docker Image](https://hub.docker.com/_/mariadb)
- [Phpmyadmin Docker Image](https://hub.docker.com/_/phpmyadmin)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Selenium](https://www.selenium.dev/documentation/)

## Installation Instructions
1. Clone the repository.
2. Run the Docker containers using Docker Compose.
3. Docker Compose will automatically pull the necessary images.
4. If everything is set up correctly, the server should run on localhost:8080.
5. If there are any problems, try to run `permissions.sh`.

## Team
- Tomasz Sankowski
- Piotr Sulewski
- Michał Konieczny
- Konrad Czarnecki
