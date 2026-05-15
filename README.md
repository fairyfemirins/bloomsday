# Bloomsday - Positive News Aggregator

A minimal open-source tool for aggregating and displaying positive news from Reddit.

## Features
- Fetch positive news from subreddits like r/UpliftingNews, r/HappyNews, and r/GoodNews.
- Display news in a simple, clean interface.
- Mock data for testing (replace with Reddit API in production).

## Tech Stack
- **Backend:** Python + Flask
- **Frontend:** HTML/CSS/JS + Bootstrap
- **Data Source:** Reddit API (mock data for MVP)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/fairyfemirins/bloomsday.git
   cd bloomsday
   ```

2. Install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python app.py
   ```

4. Open `http://localhost:5002` in your browser.

## Usage
- View positive news stories curated from Reddit.
- Click on headlines to read the full story.

## License
MIT