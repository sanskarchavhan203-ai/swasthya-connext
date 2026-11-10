# Swasthya Connect — Community Healthcare Access Platform
*(सामुदायिक आरोग्य मंच)*

[![Status](https://img.shields.io/badge/Status-Prototype%20Demo-amber.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Language](https://img.shields.io/badge/Languages-EN%20%7C%20%E0%A4%B9%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A5%80%20%7C%20%E0%A4%AE%E0%A4%B0%E0%A4%BE%E0%A4%A0%E0%A5%80-emerald.svg)]()

> **Notice:** All health camps, facilities, and community numbers in this repository are illustrative fictional data for academic and hackathon demonstration purposes. Listings are marked as demo records and are not official clinical records.

---

## 🌐 Live Public Demo URL (For Hackathon Judges)

👉 **[https://72b610548a82c9.lhr.life](https://72b610548a82c9.lhr.life)** *(Live Tunnel)*
👉 **[http://localhost:3000](http://localhost:3000)** *(Local Offline Demo)*

*Now powered by the official India Post Postal PIN Code API for real-time village, city, and postal code resolution across India.*

---

## 1. Executive Summary

Many people in underserved communities miss preventive screenings, health camps, and public healthcare services because information is fragmented and outreach is insufficient. 

**Swasthya Connect** is a community healthcare access platform with two connected core functions:
1. **Part A: Identify Healthcare Gaps** — Analyzes community-level screening coverage and facility proximity to identify and rank areas in urgent need of outreach.
2. **Part B: Connect People to Healthcare** — Lets residents discover nearby free health camps, public facilities (PHCs/CHCs), check timings, and set screening reminders.

The key connection is that **the dashboard doesn't merely show static statistics; its findings inform outreach interventions, and completed outreach dynamically updates community coverage!**

---

## 2. Core Architecture & Features

### Feature 1: Healthcare Gap Dashboard (Part A)
- **Screening Coverage Formula:**
  $$\text{Coverage Rate (\%)} = \frac{\text{People Screened}}{\text{Total Population}} \times 100$$
- **Explainable Transparent Rule Engine:**
  - **High Priority (Urgent Outreach):** Screening coverage $< 20\%$ **AND** (Distance to nearest facility $> 5\text{ km}$ **OR** $0$ camps held recently).
  - **Medium Priority (Investigate Access):** Screening coverage $< 20\%$ despite nearby facility ($\le 5\text{ km}$) — indicating awareness/timing bottlenecks; **OR** coverage $20\% - 35\%$ with long travel distances.
  - **Lower Priority (Baseline):** Screening coverage $\ge 35\%$ with reasonable facility proximity.
- Interactive **Chart.js Visualizations**:
  - Community screening coverage vs. $20\%$ critical threshold.
  - Priority category distribution breakdown.
- Ranked community table with transparent rationale tags and a one-click **"Schedule Camp Here"** action.

### Feature 2: Find Health Camps (Part B)
- Search by village name, locality, or PIN code (e.g., `Nimgaon Ketki`, `413120`, `412207`).
- Multi-dimensional filters: Date (Upcoming, Completed) and Clinical Service (Hypertension & Diabetes, Maternal Care, Eye Screening, Routine Immunization, General OPD).
- Rich Camp Cards: Eligibility, timings, venue, organizer, verified contact person/phone, directions, and disclaimer badges.
- **Privacy-First Screening Reminders:** Residents can register for an SMS/notification reminder without sharing invasive personal medical records.

### Feature 3: Public Healthcare Directory (Part B)
- Verified directory of Primary Health Centres (PHC), Community Health Centres (CHC), Sub-District Hospitals, and Health & Wellness Sub-Centres.
- Key service tags: 24/7 Emergency, Institutional Delivery, Free Essential Drugs, Ambulance on-site.
- Operating hours, contact numbers, address, and Google Maps / OpenStreetMap direct coordinates.

### Feature 4: Outreach and Follow-up Information
- Educational guides for Hypertension, Diabetes, Antenatal & Routine Immunization, and Cataract Care.
- Healthy normal ranges, screening cadence, and post-camp follow-up instructions.
- Notification management center for active user reminders.

### Feature 5: Area Priority Map
- Interactive Leaflet map with OpenStreetMap tiles.
- Color-coded circular zones:
  - 🔴 **Red:** High priority gap areas ($< 20\%$ coverage, remote facility).
  - 🟡 **Orange:** Medium priority areas.
  - 🟢 **Green:** Baseline served areas.
- 🏥 Hospital/PHC pins and 🏕️ Camp pins with popups for direct actions.

### Feature 6: Outreach Tracking & Closed-Loop Attendance Logger
- Lets administrators log verified post-camp attendance.
- Logging attendance dynamically increments the target community's screened count and updates its coverage percentage and priority score live across all dashboard views!

---

## 3. Demo Scenario: Village B Outreach Journey

You can demonstrate the exact test scenario outlined in Section 12 to judges using the built-in **"⚡ 1-Click Demo Scenario"** button:

1. **Initial State:** Village B (*Nimgaon Ketki*, PIN 413120) has a population of 1,500 with only 150 people screened (**10.0% coverage**) and the nearest hospital 8.5 km away. The dashboard automatically flags it as **High Priority**.
2. **Outreach Action:** The administrator schedules or reviews the Comprehensive Hypertension Camp (`C01`) for Village B.
3. **Resident Discovery:** A resident searches "Nimgaon" or "413120", views camp timings at ZP Primary School, and registers a reminder.
4. **Attendance Logging:** After the event, the administrator records **150 people screened**.
5. **Measurable Impact:** Village B's screened count increases from 150 to **300**, coverage jumps from **10.0% to 20.0%**, and the dashboard live-updates to reflect the improved status!

---

## 4. Standout Features for Hackathons

1. **Multilingual Support:** One-click language switcher supporting **English**, **हिन्दी (Hindi)**, and **मराठी (Marathi)** with culturally relevant terminology.
2. **Low-Bandwidth Mode:** Lightweight, high-contrast mode optimized for basic smartphones and rural 2G/3G connectivity.
3. **Persistent Local State:** Edits, scheduled camps, and recorded attendances persist across browser sessions using `localStorage`, with a 1-click **Reset Demo Data** button.
4. **Safety & Ethics Safeguards:** Prominent demo disclaimers and zero collection of identifiable patient health records.

---

## 5. Quick Start / How to Run

### Option 1: Run with Python (Recommended — 0 Dependencies)
```bash
# Navigate to the project directory
cd "c:\Users\sanskar chavhan\OneDrive\Desktop\karan\problem"

# Start the local server
python server.py
```
Open **[http://localhost:3000](http://localhost:3000)** in your browser.

### Option 2: Open Directly
Double-click `index.html` in any modern web browser.

---

## 6. Project Structure

```
problem/
├── index.html              # Main single-page web app entry point
├── server.py               # Lightweight Python development server
├── package.json            # Project manifest & metadata
├── README.md               # Documentation & judge presentation guide
├── data/
│   ├── communities.json    # 10 sample communities with population & coverage
│   ├── facilities.json     # 10 public healthcare facilities (PHCs, CHCs, SDHs)
│   ├── camps.json          # 8 health camps (upcoming & completed)
│   └── education.json      # Health guidance & screening follow-up tips
└── src/
    ├── app.js              # State management, Gap Algorithm, Leaflet & Chart.js
    └── styles.css          # Map animations, low-bandwidth mode & custom UI
```

---

## 7. Pitch to Judges (Section 14)

> *"Many people in underserved communities miss preventive screenings and public healthcare services because information is fragmented and outreach is insufficient.*
>
> *Swasthya Connect bridges this gap with two interconnected functions. First, it analyzes community-level data to identify areas that need more healthcare outreach through transparent, explainable scoring. Second, it connects residents with verified health camps and public facilities through a clean, multilingual interface.*
>
> *Unlike passive hospital directories, Swasthya Connect forms a closed loop: identifying the gap, scheduling the camp, connecting the resident, and tracking verified attendance to measure real community healthcare progress."*
