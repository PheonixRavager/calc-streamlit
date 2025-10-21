# Simple Calculator 🧮

Basic arithmetic app with Streamlit UI. Modular design: logic in `logic.py`, web frontend in `calcstream.py`.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38.0-brightgreen)](https://streamlit.io/)
## Features

| Operation | Description | Error Handling |
|:---------|:------------|:---------------|
| + (Add)   | Sum of two numbers | N/A |
| - (Subtract) | Difference of two numbers | N/A |
| * (Multiply) | Product of two numbers | N/A |
| / (Divide) | Quotient of two numbers | Divides by zero → ValueError |
| sqrt (Optional) | Square root of first number | Negative input → ValueError |
| Invalid Ops | Any unsupported operation | ValueError: "Invalid operation" |
- Clean sidebar inputs for better UX.
- Formatted results with 2 decimal places.
- Responsive web interface (localhost:8501).

## Prerequisites
- Python 3.11+ (tested in PyCharm).
- Virtual environment (e.g., `python -m venv venv`).

## Setup & Run
1. Install dependencies:
   pip install -r requirements.txt
   ```
2. Run the app:  
   ```
   streamlit run calcstream.py
   ```
   - Opens in browser at [http://localhost:8501](http://localhost:8501).  
   - Test: Enter 5 & 3, select "+", click **Compute** → Result: 8.00.

## Testing
Run unit tests for the logic:  
```
pytest -v test_logic.py
```
- Covers add/subtract/multiply/divide/sqrt + edge cases (e.g., div-by-zero).  
- All tests should pass green!

## Project Structure
```
calculator/
├── .venv/            # Virtual Environment
├── calcstream.py     # Streamlit UI
├── logic.py          # Core calculate function
├── requirements.txt  # Dependencies
├── README.md         # Project documentation
└── test_logic.py            # Unit tests
```

## Enhancements & TODOs
- Add calculation history (using `st.session_state`).
- Deploy to Streamlit Cloud: Push to GitHub → Connect at [share.streamlit.io](https://share.streamlit.io).
- More ops: Exponents (^), modulo (%).

## Contributing
Fork, PR, or suggest features! Built with ❤️ in PyCharm.

## License
MIT (or add your own).

Built: October 21, 2025