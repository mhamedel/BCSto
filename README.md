# BCS Smart Irrigation System

A smart irrigation solution built with **Python**, **JavaScript (OWL)**, and **Odoo**, designed to help farmers and agricultural managers monitor and optimize their crop environments using **IoT technology**.

## 🌱 Features

- Real-time monitoring of:
  - 🌡️ Temperature
  - 💧 Humidity
  - 🧪 Soil pH
  - 🧂 Salinity
- IoT integration using APIs and standard communication protocols
- Sensor data is collected per **client**, and structured by:
  - 🏡 **Farm**
  - 📍 **Zone** (specific areas within a farm)
  - 📏 **Depth** (sensor readings at different soil levels)
- Individual dashboards for each client
- Smart alerts for abnormal values
- Historical data analysis and visualization

## 🛠️ Technologies Used

- **Python**
- **Odoo** (ERP backend)
- **OWL (Odoo Web Library)** – for building reactive frontend components
- **JavaScript**
- **IoT protocols** (e.g., 4G, HTTP)
- **RESTful APIs**
- **PostgreSQL** (via Odoo ORM)

## 📊 Charts & Visualization

Interactive charts are used to help clients easily understand the collected data:

- **Line charts** for temperature trends
- **Bar charts** for humidity and salinity levels
- **Color-coded indicators** for pH values
- **Real-time updates** using OWL reactivity
- Libraries used: `Chart.js`, `Plotly.js`, or native OWL rendering

These visualizations appear on the dashboard and are customized for each client's zones and farm areas.

## 🌍 Use Case

This system is ideal for agricultural zones where efficient water usage and soil awareness are essential. It enables farmers to make **data-driven decisions** to improve crop yield, reduce waste, and automate irrigation logic.
