# CRM Application

## Overview

This CRM (Customer Relationship Management) application is designed to help manage customer relationships by registering and tracking orders. The application is developed using Python, with **FastAPI** as the backend framework and **PostgreSQL** as the database engine. Additionally, it is designed to integrate seamlessly with our machine learning application to enhance its capabilities.

## Features

### Version 1.0
- **Order Registration**: Users can register customer orders, allowing for efficient tracking and management of customer interactions.

### Version 2.0
- **Dashboard for Administrators**: A dashboard will be introduced to provide relevant information and analytics, helping administrators make informed decisions based on customer data and order history.

## Integration with Machine Learning
The application will be capable of integrating with a machine learning system to enhance functionalities such as predictive analytics, customer behavior analysis, and personalized recommendations.

## Technologies Used
- **Python**
- **FastAPI** (Backend Framework)
- **PostgreSQL** (Database)
- **Machine Learning Integration**

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <directory-name>
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database in `config.py`.
5. Start the application:
   ```bash
   uvicorn main:app --reload
   ```

---

# Aplicación CRM

## Descripción General

Esta aplicación de CRM (Customer Relationship Management) está diseñada para ayudar a gestionar las relaciones con los clientes mediante el registro y seguimiento de pedidos. La aplicación está desarrollada en Python, con **FastAPI** como framework de backend y **PostgreSQL** como motor de base de datos. Además, está diseñada para integrarse sin problemas con nuestra aplicación de machine learning para mejorar sus capacidades.

## Características

### Versión 1.0
- **Registro de Pedidos**: Los usuarios pueden registrar pedidos de clientes, permitiendo un seguimiento y gestión eficientes de las interacciones con los clientes.

### Versión 2.0
- **Panel para Administradores**: Se introducirá un panel para proporcionar información y análisis relevantes, ayudando a los administradores a tomar decisiones informadas basadas en datos de clientes e historial de pedidos.

## Integración con Machine Learning
La aplicación será capaz de integrarse con un sistema de machine learning para mejorar funcionalidades como análisis predictivo, análisis de comportamiento del cliente y recomendaciones personalizadas.

## Tecnologías Utilizadas
- **Python**
- **FastAPI** (Framework de Backend)
- **PostgreSQL** (Base de Datos)
- **Integración con Machine Learning**

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <repository-url>
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd <nombre-del-directorio>
   ```
3. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```
4. Configura la base de datos en `config.py`.
5. Inicia la aplicación:
   ```bash
   uvicorn main:app --reload
   ```