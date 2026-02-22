# 🛒 Py-Shop

**Py-Shop** is a beginner-friendly e-commerce web application built with **Django**. Created as a short, practical lesson in Django development, this project demonstrates the core concepts of building a web store, managing products, and handling static/media files.

## 📂 Project Structure

This project follows a standard Django architecture, broken down into the following key directories:

- **`pyshop/`**: The main Django configuration folder containing settings, primary routing (URLs), and WSGI setup.
- **`products/`**: The core app responsible for managing the shop's inventory, displaying items, and handling product-related backend logic.
- **`templates/`**: Contains the HTML files used to render the frontend interfaces.
- **`static/`**: Houses the CSS, JavaScript, and other static assets to style the application.
- **`media/`**: Stores user-uploaded content, specifically structured to hold product images (`media/images/products/`).

## ✨ Features

- **Product Catalog:** A structured way to add, view, and manage products.
- **Media Management:** Properly configured to handle dynamic image uploads for products.
- **Styled Frontend:** Uses HTML, CSS, and JavaScript to create an interactive and visually appealing storefront.
- **Built-in Database:** Uses SQLite (`db.sqlite3`) making it incredibly easy to set up and run locally without extra database configurations.

## 🚀 Prerequisites

To run this project on your local machine, you will need:
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)

## 🛠️ Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/ArabianDeveloper/py-shop.git](https://github.com/ArabianDeveloper/py-shop.git)
cd py-shop
