import streamlit as st
import numpy as np
import random
import datetime
from datetime import date
import pandas as pd
import io

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
        "name": "Full Name",
        "email": "Email Address",
        "checkin": "📅 Check-in Date",
        "time": "⏰ Check-in Time",
        "coupon": "Apply Coupon Code (Optional)",
        "confirm_btn": "✅ Confirm Booking"
    },
    "Hindi": {
        "title": "🏠 स्मार्ट एयरबीएनबी बुकिंग डैशबोर्ड",
        "name": "पूरा नाम",
        "email": "ईमेल पता",
        "checkin": "📅 चेक-इन तिथि",
        "time": "⏰ चेक-इन समय",
        "coupon": "कूपन कोड लागू करें",
        "confirm_btn": "✅ बुकिंग की पुष्टि करें"
    },
    "Marathi": {
        "title": "🏠 स्मार्ट एअरबीएनबी बुकिंग डॅशबोर्ड",
        "name": "पूर्ण नाव",
        "email": "ईमेल पत्ता",
        "checkin": "📅 चेक-इन तारीख",
        "time": "⏰ चेक-इन वेळ",
        "coupon": "कूपन कोड लागू करा",
        "confirm_btn": "✅ बुकिंग करा"
    }
}

t = translations[language]

# ============================================================
# ======================= BOOKING PAGE =======================
# ============================================================
if page == "🏠 Booking":

    st.title("🏨 Smart Airbnb Booking Dashboard")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")

    with col2:
        travel_date = st.date_input("Check-in Date", min_value=date.today())
        travel_time = st.time_input("Check-in Time", datetime.time(14, 0))

    # ---------------- HOTEL LIST ----------------
    hotel = st.selectbox("Select Hotel", [
        "Taj Luxury ⭐⭐⭐⭐⭐",
        "ITC Royal ⭐⭐⭐⭐⭐",
        "The Oberoi Grand ⭐⭐⭐⭐⭐",
        "JW Marriott ⭐⭐⭐⭐⭐",
        "Grand Palace ⭐⭐⭐⭐",
        "Hyatt Regency ⭐⭐⭐⭐",
        "Radisson Blu ⭐⭐⭐⭐",
        "Lemon Tree Premier ⭐⭐⭐⭐",
        "Budget Comfort ⭐⭐⭐",
        "Treebo Residency ⭐⭐⭐",
        "FabHotel Prime ⭐⭐⭐",
        "OYO Townhouse ⭐⭐⭐"
    ])

    city = st.selectbox("City", [
        "Mumbai",
        "Pune",
        "Delhi",
        "Bangalore",
        "Hyderabad",
        "Gurugram (Haryana)",
        "Faridabad (Haryana)",
        "Chandigarh",
        "Jaipur",
        "Goa",
        "Kolkata",
        "Chennai",
        "Ahmedabad",
        "Lucknow",
        "Indore"
    ])

    room_type = st.selectbox("Room Type",
        ["Entire Home", "Private Room", "Shared Room", "Luxury Suite 🏆"])

    guests = st.slider("Guests", 1, 10, 2)
    nights = st.slider("Nights", 1, 30, 3)

    payment = st.selectbox("Payment Mode",
        ["UPI", "Credit Card", "Debit Card", "Net Banking"])

    coupon = st.text_input("Apply Coupon Code (Optional)").strip()

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

    original_price = base_price + guests*300 + nights*200

    if travel_date.weekday() >= 5:
        original_price *= 1.20

    if travel_time.hour >= 20:
        original_price *= 1.10

    original_price = int(original_price)

    # ---------------- COUPON ENGINE ----------------
    coupons = {
        "SAVE10": lambda price: price * 0.10,
        "FLAT1000": lambda price: 1000,
        "FESTIVE1000": lambda price: 1000
    }

    discount = int(coupons.get(coupon.upper(), lambda price: 0)(original_price))

    discounted_price = original_price - discount
    gst = int(discounted_price * 0.18)
    final_price = discounted_price + gst

    availability = np.random.choice(["Available", "Fully Booked"], p=[0.85, 0.15])

    # ---------------- DISPLAY ----------------
    st.markdown("---")
    st.subheader("💰 Pricing Summary")
    st.write(f"Original Price: ₹ {original_price}")
    st.write(f"Discount: ₹ {discount}")
    st.write(f"GST (18%): ₹ {gst}")
    st.success(f"Final Payable Amount: ₹ {final_price}")
    st.write("Status:", availability)

    # ---------------- CONFIRM ----------------
    if st.button("Confirm Booking"):

        if availability == "Fully Booked":
            st.error("Property Fully Booked")
        elif name == "" or email == "":
            st.warning("Fill all details")
        else:

            booking_id = "AIR" + str(random.randint(10000, 99999))

            booking_data = {
                "Booking ID": booking_id,
                "Name": name,
                "Email": email,
                "Hotel": hotel,
                "City": city,
                "Room": room_type,
                "Guests": guests,
                "Nights": nights,
                "Total": final_price
            }

            st.session_state.bookings.append(booking_data)

            st.success("Booking Confirmed 🎉")
            st.balloons()

            # ---------------- PDF RECEIPT ----------------
            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer)
            elements = []
            styles = getSampleStyleSheet()

            elements.append(Paragraph("SMART AIRBNB PRO", styles["Title"]))
            elements.append(Paragraph("PAYMENT RECEIPT", styles["Heading2"]))
            elements.append(Spacer(1, 0.3 * inch))

            receipt_text = f"""
Booking ID: {booking_id}<br/><br/>
Name: {name}<br/>
Email: {email}<br/>
Hotel: {hotel}<br/>
City: {city}<br/>
Room Type: {room_type}<br/>
Guests: {guests}<br/>
Nights: {nights}<br/>
Check-in Date: {travel_date}<br/>
Check-in Time: {travel_time}<br/>
Payment Mode: {payment}<br/><br/>
Original Price: ₹ {original_price}<br/>
Discount: ₹ {discount}<br/>
GST: ₹ {gst}<br/>
<b>Final Amount: ₹ {final_price}</b>
"""

            elements.append(Paragraph(receipt_text, styles["Normal"]))
            doc.build(elements)
            buffer.seek(0)

            st.download_button(
                "📥 Download Payment Receipt",
                buffer,
                file_name=f"{booking_id}.pdf",
                mime="application/pdf"
            )
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

    st.title("Admin Dashboard")

    if len(st.session_state.bookings) == 0:
        st.info("No Active Bookings")
    else:
        df = pd.DataFrame(st.session_state.bookings)
        st.dataframe(df)
        st.metric("Total Revenue", f"₹ {df['Total'].sum()}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Smart Airbnb Booking System By Harshal | Version 2.8 ")
