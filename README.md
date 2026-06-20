# Ajantha Watch Store

**Project Type:** Web-based E-commerce Prototype  
**Technologies Used:** Python, Flask, Flask-SQLAlchemy, Flask-WTF, SQLite, HTML, Bootstrap CSS  
**Author:Rizwan Mohammed  
**Date: 12/21/2025


## **Project Description**

Ajantha Watch Store is a simple e-commerce prototype that allows users to browse and purchase a variety of wristwatches. Products are grouped into categories such as Digital, Analog, and Smart Watches. Each product listing includes essential information like brand, model, features, and price.  

Users can:

- Browse watches by category  
- View detailed product specifications  
- Add products to a shopping basket  
- Modify the basket (remove items, empty basket)  
- Complete a checkout process by entering their details  



---

## **Folder Structure**

## Folder Structure

Ajantha_Watch_Store/
│
├── app.py                 # Main Flask application
├── models.py              # SQLAlchemy database models
├── forms.py               # Flask-WTF forms
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── product_detail.html
│   ├── basket.html
│   └── checkout.html
│
├── static/                # Static assets
│   ├── css/
│   │   └── style.css      # Custom CSS
│   └── images/
│       ├── watch1.jpg
│       ├── watch2.jpg
│       └── ...            # Addition


###SET UP and RUN###
1. OPen terminal in project root folder
EX:(AJANTHA_WATCH_STORE)
2.ACtivate virtual Environment
EX:venv\Scripts\activate

3. Install dependencies
EX:pip install -r requirements.txt
4.Run the FLASK Application
Ex:python app.py
5.Open the Browser at 
EX:http://127.0.0.1:5000/

####Functionality of the project##########
Browse Products,add to basket
Item Detail page :View detaail watch info
Shoping basket :View,Delete,Empty items
Checkout Page: Enter details and checkout order


##Database###########
Products:
Orders:
Order_details