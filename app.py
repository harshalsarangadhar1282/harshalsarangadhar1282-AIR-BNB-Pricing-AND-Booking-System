
import streamlit as st
import numpy as np
import random
import datetime
from datetime import date
import uuid
import pandas as pd

# PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Airbnb Pro", layout="wide", page_icon="🏨")

# ---------------- SESSION ----------------
if "bookings" not in st.session_state:
    st.session_state.bookings = []

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.stApp { background-color:#f4f6f9; }
.title { text-align:center; font-size:36px; font-weight:bold; color:#1a237e; }
.card { background:white; padding:20px; border-radius:12px;
box-shadow:0 5px 15px rgba(0,0,0,0.1); text-align:center; }
.price { font-size:28px; font-weight:bold; color:#e53935; }
.good { color:#2e7d32; font-weight:bold; }
.bad { color:#c62828; font-weight:bold; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go To",
                        ["🏠 Booking", "❌ Cancellation", "🛠 Admin"])

language = st.sidebar.selectbox("🌐 Language",
                                ["English","Hindi","Marathi"])

# ---------------- TRANSLATIONS ----------------
translations = {

    "English": {
        "title": "🏠 Smart Airbnb Booking Dashboard",
        "personal": "👤 Personal Details",
        "name": "Full Name",
        "email": "Email Address",
        "checkin": "📅 Check-in Date",
        "time": "⏰ Check-in Time",
        "booking": "🏡 Booking Details",
        "location": "📍 Location",
        "room": "Room Type",
        "guests": "Guests",
        "nights": "Number of Nights",
        "payment": "💳 Payment Details",
        "coupon": "Apply Coupon Code (Optional)",
        "summary": "📊 Booking Summary",
        "price": "💰 Total Price",
        "availability": "📅 Availability",
        "confirm": "🧾 Confirm Booking",
        "confirm_btn": "✅ Confirm Booking",
        "success": "🎉 Booking Confirmed Successfully!",
        "error": "❌ Sorry! This property is fully booked.",
        "warning": "⚠️ Please enter all personal details."
    },

    "Hindi": {
        "title": "🏠 स्मार्ट एयरबीएनबी बुकिंग डैशबोर्ड",
        "personal": "👤 व्यक्तिगत विवरण",
        "name": "पूरा नाम",
        "email": "ईमेल पता",
        "checkin": "📅 चेक-इन तिथि",
        "time": "⏰ चेक-इन समय",
        "booking": "🏡 बुकिंग विवरण",
        "location": "📍 स्थान",
        "room": "कमरे का प्रकार",
        "guests": "मेहमान",
        "nights": "रातों की संख्या",
        "payment": "💳 भुगतान विवरण",
        "coupon": "कूपन कोड लागू करें",
        "summary": "📊 बुकिंग सारांश",
        "price": "💰 कुल मूल्य",
        "availability": "📅 उपलब्धता",
        "confirm": "🧾 बुकिंग पुष्टि",
        "confirm_btn": "✅ बुकिंग की पुष्टि करें",
        "success": "🎉 बुकिंग सफल!",
        "error": "❌ यह प्रॉपर्टी बुक हो चुकी है।",
        "warning": "⚠️ कृपया सभी विवरण भरें।"
    },

    "Marathi": {
        "title": "🏠 स्मार्ट एअरबीएनबी बुकिंग डॅशबोर्ड",
        "personal": "👤 वैयक्तिक माहिती",
        "name": "पूर्ण नाव",
        "email": "ईमेल पत्ता",
        "checkin": "📅 चेक-इन तारीख",
        "time": "⏰ चेक-इन वेळ",
        "booking": "🏡 बुकिंग तपशील",
        "location": "📍 ठिकाण",
        "room": "रूम प्रकार",
        "guests": "अतिथी",
        "nights": "रात्रींची संख्या",
        "payment": "💳 पेमेंट तपशील",
        "coupon": "कूपन कोड लागू करा",
        "summary": "📊 बुकिंग सारांश",
        "price": "💰 एकूण किंमत",
        "availability": "📅 उपलब्धता",
        "confirm": "🧾 बुकिंग पुष्टी",
        "confirm_btn": "✅ बुकिंग करा",
        "success": "🎉 बुकिंग यशस्वी!",
        "error": "❌ ही प्रॉपर्टी पूर्ण बुक आहे.",
        "warning": "⚠️ कृपया सर्व माहिती भरा."
    }
}

t = translations.get(language)


}

t = translations[language]

# ============================================================
# ======================= BOOKING PAGE =======================
# ============================================================
if page == "🏠 Booking":

    st.markdown(f'<div class="title">{t["title"]}</div>',
                unsafe_allow_html=True)
    st.markdown("---")

    col1,col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")

    with col2:
        travel_date = st.date_input("Check-in Date",
                                    min_value=date.today())
        travel_time = st.time_input("Check-in Time",
                                    datetime.time(14,0))

    hotel = st.selectbox("Select Hotel",
        ["Taj Luxury ⭐⭐⭐⭐⭐",
         "Grand Palace ⭐⭐⭐⭐",
         "Budget Comfort ⭐⭐⭐"])

    city = st.selectbox("City",
        ["Mumbai","Pune","Delhi","Bangalore","Hyderabad"])

    room_type = st.selectbox("Room Type",
        ["Entire Home",
         "Private Room",
         "Shared Room",
         "Luxury Suite 🏆"])

    guests = st.slider("Guests",1,10,2)
    nights = st.slider("Nights",1,30,3)

    payment = st.selectbox("Payment Mode",
        ["UPI","Credit Card","Debit Card","Net Banking"])

    coupon = st.text_input("Coupon Code")

    # ---------------- PRICING ----------------
    base_price = 2000

    if room_type == "Entire Home":
        base_price += 1500
    elif room_type == "Private Room":
        base_price += 800
    elif room_type == "Shared Room":
        base_price += 400
    else:
        base_price += 4000

    price = base_price + guests*300 + nights*200

    # Weekend Surge
    if travel_date.weekday() >= 5:
        price *= 1.20

    # Rush Hour
    if travel_time.hour >= 20:
        price *= 1.10

    # Coupon
    discount = 0
    if coupon.upper() == "SAVE10":
        discount = price * 0.10
    elif coupon.upper() == "FLAT1000":
        discount = 1000

    price -= discount

    # GST
    gst = price * 0.18
    final_price = int(price + gst)

    availability = np.random.choice(["Available","Fully Booked"],
                                    p=[0.85,0.15])

    # ---------------- SUMMARY ----------------
    st.markdown("---")
    colA,colB,colC = st.columns(3)

    with colA:
        st.markdown(f'<div class="card"><h4>Hotel</h4><h3>{hotel}</h3></div>',
                    unsafe_allow_html=True)

    with colB:
        st.markdown(f"""
        <div class="card">
        Base: ₹ {int(price)} <br>
        GST (18%): ₹ {int(gst)} <br>
        <div class="price">₹ {final_price}</div>
        </div>
        """, unsafe_allow_html=True)

    with colC:
        cls = "good" if availability=="Available" else "bad"
        st.markdown(f'<div class="card"><h4>Status</h4><h3 class="{cls}">{availability}</h3></div>',
                    unsafe_allow_html=True)

    # ---------------- CONFIRM ----------------
    if st.button("✅ Confirm Booking"):

        if availability=="Fully Booked":
            st.error("Property Fully Booked")
        elif name=="" or email=="":
            st.warning("Fill all details")
        else:

            booking_id = "AIR"+str(random.randint(10000,99999))

            booking_data = {
                "Booking ID":booking_id,
                "Name":name,
                "Email":email,
                "Hotel":hotel,
                "City":city,
                "Room":room_type,
                "Guests":guests,
                "Nights":nights,
                "Total":final_price
            }

            st.session_state.bookings.append(booking_data)

            st.success("Booking Confirmed 🎉")
            st.balloons()

            # ---------------- PDF ----------------
            file_name = f"{booking_id}.pdf"
            doc = SimpleDocTemplate(file_name)
            elements = []
            styles = getSampleStyleSheet()

            elements.append(Paragraph("Airbnb Booking Receipt",
                                      styles["Title"]))
            elements.append(Spacer(1,0.5*inch))

            table_data = [[k,str(v)] for k,v in booking_data.items()]
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('GRID',(0,0),(-1,-1),1,colors.black)
            ]))

            elements.append(table)
            doc.build(elements)

            with open(file_name,"rb") as f:
                st.download_button("📥 Download PDF Receipt",
                                   f,
                                   file_name=file_name)

# ============================================================
# ======================= CANCELLATION =======================
# ============================================================
elif page == "❌ Cancellation":

    st.markdown("<h2 style='color:#c62828;'>Cancellation & Refund</h2>",
                unsafe_allow_html=True)

    cancel_id = st.text_input("Enter Booking ID")

    if st.button("Process Refund"):

        found=False

        for booking in st.session_state.bookings:
            if booking["Booking ID"] == cancel_id:
                found=True
                refund = booking["Total"] * 0.80
                st.success(f"Refund Amount: ₹ {int(refund)}")
                st.session_state.bookings.remove(booking)
                break

        if not found:
            st.error("Invalid Booking ID")

# ============================================================
# ======================= ADMIN ===============================
# ============================================================
elif page == "🛠 Admin":

    st.markdown("<h2 style='color:#1a237e;'>Admin Dashboard</h2>",
                unsafe_allow_html=True)

    if len(st.session_state.bookings)==0:
        st.info("No Active Bookings")
    else:
        df = pd.DataFrame(st.session_state.bookings)
        st.dataframe(df)
      # ---------------- FOOTER ----------------
st.markdown("""
<br>
<center style="color:gray;">
🚀 Smart Airbnb Booking System | Version 2.8
</center>
""", unsafe_allow_html=True)
