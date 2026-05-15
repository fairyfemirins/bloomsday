# Bloomsday: Design Decisions & Rationale

## Overview
This document explains the design decisions behind **Bloomsday**, a minimal open-source tool for aggregating and displaying positive news from Reddit.

## Tech Stack Choices
### 1. **Backend: Flask (Python)**
   - **Why?** Lightweight, easy to deploy, and integrates well with the Reddit API.
   - **Alternatives Considered:** Django (overkill for MVP), FastAPI (less mature for simple projects).

### 2. **Frontend: HTML/CSS/JS + Bootstrap**
   - **Why?** Simple, no build step, and works out of the box with Flask.
   - **Alternatives Considered:** React/Vue (unnecessary complexity for MVP).

### 3. **Data Source: Reddit API (Mock Data for MVP)**
   - **Why?** Reddit has a wealth of positive news subreddits (e.g., r/UpliftingNews, r/HappyNews).
   - **Mock Data:** Used for the MVP due to Reddit API credential requirements.
   - **Future Work:** Replace with real API calls using OAuth.

## Key Design Decisions
### 1. **Mock Data for MVP**
   - **How?** Hardcoded mock data to simulate Reddit API responses.
   - **Why?** Simplifies the MVP and avoids credential management.
   - **Limitations:** No real-time updates or dynamic content.
   - **Future Work:** Integrate Reddit API with OAuth.

### 2. **No Database (File-Based Storage)**
   - **Why?** Simplifies the MVP by avoiding database setup.
   - **Future Work:** Add SQLite or PostgreSQL for persistent storage.

### 3. **Simple Frontend**
   - **Why?** Focuses on readability and ease of use.
   - **Future Work:** Add user authentication, favorites, and social sharing.

## Challenges & Workarounds
### 1. **Reddit API Credentials**
   - **Issue:** Reddit API requires OAuth credentials.
   - **Workaround:** Used mock data for the MVP.

### 2. **Rate Limiting**
   - **Issue:** Reddit API may rate-limit requests.
   - **Workaround:** Mock data avoids this issue.

### 3. **Port Conflicts**
   - **Issue:** Flask server failed to start due to port 5000/5001 being in use.
   - **Workaround:** Switched to port 5002.

## License
MIT