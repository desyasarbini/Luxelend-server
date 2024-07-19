# Luxelend-Server Project

Luxelend is a rental platform for luxury outfits and items, this project uses Poetry, Flask, Supabase and CORS to manage and fetch the database.

## Table of Contents

- [Overview](#overview)
- [ERD](#erd)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [API Documentation](#api-documentation)
- [Deployment]()

## Overview

This project serves as the backend for Luxelend, handling all the data management and API functionalities. It integrates with Supabase for database services and uses CORS for cross-origin requests.

## ERD

![Entity-Relationship-Diagram](./app/assets/erd.png)

## Prerequisites

- Python 3.10
- Poetry
- Flask
- Supabase account and project setup

## Installation

1.  clone repository
    `git clone https://github.com/desyasarbini/Luxelend-server.git`
    `cd Luxelend-server`

2.  install package manager
    `pip3 install poetry` or you can follow the [Poetry installation guide](https://python-poetry.org/docs/)

3.  install depencies
    `poetry install`

4.  Activate the virtual environment
    `poetry shell`

## Environment Variables

Create a .env file in the root directory project and add the following variables:

```
FLASK_DEBUG = TRUE
FLASK_ENV = Development

DATABASE_TYPE = your_supabase_database_type
DATABASE_HOST = your_supabase_database_host
DATABASE_NAME = your_supabase_database_name
DATABASE_PORT = your_supabase_database_port
DATABASE_USER = your_supabase_database_user
DATABASE_PASSWORD = your_supabase_database_password

JWT_SECRET_KEY=your_secret_key
```

## Database Setup

1.  Initialize the database
    Since you're using Supabase, ensure your Supabase project is set up and the database schema is created.

2.  Run migrations
    If you have migrations set up in your project, run them to update the database schema.

## Running the Application

`poetry run flask run`

## API Endpoints

- GET /product: list all product
- GET /product/<product_id>: get a spesific detail product by ID
- GET /category: list all category
- GET /category/<catgeory_id>: get a detail category by ID
- GET /gender: list gender
- GET /property: list all property

## API Documentation

[Luxelend API Documentation](https://documenter.getpostman.com/view/32144902/2sA3e1AV8d)

## Deployment

### Build Docker Image

- install gunicorn `poetry add gunicorn`
- install docker `poetry add docker`
- create docker file dan .dockerignore
- check docker installed or not `sudo docker run hello-world`
- build docker image in existing directory `docker build -t namaimage . `
- if error occured like this **permission denied** try:
  1. `sudo systemctl restart docker`
  2. `sudo chmod 666 /var/run/docker.sock`
- run docker image `docker run -p 5000:5000 --env-file .env namaimagedocker`

### Railway Deploy

- login ke railway, saya menggunakan github untuk login sehingga jika ada deployment akan terintegrasi dengan railway
- pilih repository yang ingin di upload
- pilih variable, dan setting menggunakan data yang ada pada .env kalian
- setting FLASK_DEBUG `true` ubah ke `false`
- setting FLASK_ENV `Development` ke `Production`
- setting PORT mengikuti dengan localhost yang disetting ke app
