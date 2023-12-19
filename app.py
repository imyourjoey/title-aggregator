from flask import Flask, render_template
from scraper import scrape_headlines
import os

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/headlines')
def headlines():
    headlines_data = scrape_headlines()
    return render_template('headlines.html', headlines=headlines_data)

if __name__ == '__main__':
    # Use the PORT environment variable if available, or default to 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=port)
