# Bloomsday: Reproducible Tutorial

This tutorial guides you through setting up and running **Bloomsday** locally.

## Prerequisites
- Linux environment (tested on Ubuntu 22.04).
- Python 3.10+.
- `pip` and `virtualenv`.

## Step 1: Clone the Repository
```bash
 git clone https://github.com/fairyfemirins/bloomsday.git
 cd bloomsday
```

## Step 2: Set Up a Virtual Environment
```bash
 python3 -m venv venv
 source venv/bin/activate
```

## Step 3: Install Dependencies
```bash
 pip install -r requirements.txt
```

**Note:** If `requirements.txt` is missing, create it with:
```bash
 pip freeze > requirements.txt
```

## Step 4: Run the Flask Server
```bash
 python app.py
```

The server will start at `http://localhost:5002`.

## Step 5: Test the App
1. Open `http://localhost:5002` in your browser.
2. View the positive news stories.
3. Click on headlines to read the full story.

## Step 6: Verify the API
- The `/api/news` endpoint returns mock news data.
- To test it, run:
  ```bash
  curl http://localhost:5002/api/news
  ```

## Troubleshooting
### 1. **Port 5002 in Use**
   - **Solution:** Kill the conflicting process:
     ```bash
     pkill -f "python app.py"
     ```
   - **Alternative:** Change the port in `app.py`:
     ```python
     if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5003, debug=True)
     ```

### 2. **Reddit API Credentials**
   - **Solution:** Replace mock data with real API calls:
     1. Create a Reddit app at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
     2. Add your `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` to `.env`.
     3. Update `app.py` to use the real API.

### 3. **No News Displayed**
   - **Solution:** Ensure the `/api/news` endpoint returns data:
     ```bash
     curl http://localhost:5002/api/news
     ```

## License
MIT