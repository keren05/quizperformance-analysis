# Quiz Performance Analysis

This project analyzes quiz performance using AI-driven insights and rank prediction. It processes quiz submissions, compares them with historical data, and provides recommendations based on performance.

## Features
- Fetches quiz data from API endpoints
- Processes and cleans the data
- Provides insights on quiz performance
- Predicts NEET rank based on quiz results
- Deploys a Streamlit-based interactive dashboard

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit
- Requests

## Installation
### Prerequisites
Ensure you have Python installed. You can install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
### Running the Streamlit App
To start the application, run:
```bash
streamlit run app.py
```

### Folder Structure
```
quizperformance/
│-- app.py               # Streamlit frontend
│-- data_processing.py   # Fetches and processes data
│-- analysis.py          # Provides performance insights
│-- rank_prediction.py   # Predicts NEET rank
│-- requirements.txt     # Dependencies
│-- README.md            # Documentation
```

## API Endpoints
The project fetches data from the following endpoints:
- **Quiz Endpoint:** https://api.jsonserve.com/rJvd7g
- **Quiz Submission:** https://api.jsonserve.com/XgAgFJ
- **Historical Data:** https://www.jsonkeeper.com/b/LLQT


## Contributing
Feel free to submit pull requests for improvements!

## License
This project is licensed under the MIT License.

