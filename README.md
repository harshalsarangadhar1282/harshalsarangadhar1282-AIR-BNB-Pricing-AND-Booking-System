Smart Airbnb Booking System

A modern, interactive Airbnb-style booking dashboard built using Streamlit.
This project simulates a real-world booking system with pricing logic, availability prediction, ticket generation, and multilingual support.

🚀 Features

🌍 Multi-language Selection ( Languages: English, Hindi, Marathi )

🏠 Home Page

👤 User Details Input (Name, Email)

📅 Calendar Date Picker (MTWTFSS view)

⏰ Time Selection

🏡 Room Type Selection

👥 Guest & Nights Selection

💳 Payment Method Selection

🎁 Coupon Code System

💰 Dynamic Price Calculation

📊 Booking Summary Dashboard

📅 Real-Time Availability Simulation

🎟️ Auto Booking ID Generation

📥 Downloadable E-Reciept

🎨 Professional UI with Custom CSS

🛠️ Tech Stack

Python

Streamlit

NumPy

HTML/CSS (via Streamlit styling)

📂 Project Structure
📦 Smart-Airbnb-Booking
 ┣ 📜 app.py
 ┣ 📜 README.md
 ┗ 📜 requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/harshalsarangdhar1282/AIR-BNB-Pricing-AND-Booking-System.git
cd AIR-BNB-Pricing-AND-Booking-System

2️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt is not available:

pip install streamlit numpy

3️⃣ Run the Application
streamlit run app.py

💰 Pricing Logic

Total Price is calculated based on:

Base Price

Room Type

Number of Guests

Number of Nights

Coupon Discount (SAVE10 → 10% off)

📊 Availability Logic

Availability is simulated using probabilistic logic:

80% chance → Available

20% chance → Fully Booked

🎟️ Booking System Flow

User enters personal details

Selects location and room type

Chooses date & time

Selects seat/view preference

Applies coupon (optional)

Confirms booking

System generates:

Booking ID

E-Ticket

Download option

🎯 Use Cases

Internship Project

Portfolio Project

Mini Full-Stack Demo

UI + ML Simulation Project

Resume Showcase Project

📌 Future Improvements

Database integration (MySQL / Firebase)

Login & Authentication System

Admin Dashboard

Payment Gateway Integration

Real-time ML Price Prediction

Booking History Tracking

Deployment on Streamlit Cloud / AWS

🧠 Learning Outcomes

Streamlit UI development

Dynamic price logic implementation

Interactive dashboard design

Ticket generation system

Real-world booking workflow simulation

👨‍💻 Author

Your Name : Harshal Sarangdhar
B.E – Information Technology
Internship / Academic Project

📄 License

This project is for educational and demonstration purposes.
