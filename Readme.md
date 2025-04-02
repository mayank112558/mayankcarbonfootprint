# 🌿 Carbon Footprint Calculator  

This is a **Flask-based web application** that allows users to **calculate, track, and manage carbon emissions** based on various energy consumption parameters. It also provides a feature to **upload CSV files** containing carbon emission data and display reports via a dashboard.  

## 🚀 Features  

- **User Authentication** (Register, Login, Logout)  
- **Secure Password Hashing** using `werkzeug.security`  
- **Carbon Footprint Calculation** based on energy consumption  
- **CSV File Upload** for bulk emission data import  
- **Dynamic Dashboard** displaying stored carbon footprint data  
- **PDF Report Download** for data visualization  
- **Flask-Migrate Support** for database migrations  

---

## 🛠️ Technologies Used  

- **Flask** (Micro web framework)  
- **Flask-SQLAlchemy** (Database ORM)  
- **Flask-Migrate** (Database versioning)  
- **Flask-Login** (User authentication)  
- **Pandas** (Data handling for CSV uploads)  
- **SQLite** (Lightweight database for local storage)  
- **Jinja2** (Template rendering for HTML pages)  

---

## 📂 Project Structure  

```
carbon-footprint-app/
│── static/              # Static files (CSS, JS, images)
│── templates/           # HTML templates
│── migrations/          # Database migration scripts
│── forms.py             # WTForms for input validation
│── models.py            # SQLAlchemy models for database
│── app.py               # Main Flask application
│── requirements.txt     # Python dependencies
│── README.md            # Documentation file
```

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/yourusername/carbon-footprint-app.git
cd carbon-footprint-app
```

### 2️⃣ Create a Virtual Environment  
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database  
```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5️⃣ Run the Application  
```sh
python app.py
```

---

## 🔑 User Authentication  

| Endpoint  | Method | Description |
|-----------|--------|-------------|
| `/register` | `POST` | Register a new user |
| `/login` | `POST` | Login existing users |
| `/logout` | `GET` | Logout current user |

---

## 📊 Carbon Footprint Calculation  

The carbon footprint is estimated using:  
- Electricity Consumption  
- Fuel Consumption  
- Natural Gas Usage  
- Waste Management & Recycling  
- Travel Distance & Fuel Efficiency  

Formula used:  
```
carbon_footprint = 
    (electricity * 0.92) + 
    (fuel * 2.31) + 
    (natural_gas * 2.0) + 
    (waste * 1.5 * ((100 - recycling) / 100)) + 
    (distance / fuel_efficiency * 2.3)
```

---

## 📤 Upload CSV Data  

You can **upload CSV files** containing emission data. The required columns:  
```csv
country,year,co2,cement_co2,coal_co2,oil_co2,gas_co2,co2_per_capita,population,gdp
```

---

## 📎 License  

This project is licensed under the **MIT License**.  

---


