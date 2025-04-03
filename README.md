# nifty_assignment

Automated script to fetch **Nifty 50** stock data from **NSE India**, analyze market trends, and generate insights including:  
✔ **Top 5 gainers & losers**  
✔ **Stocks 30% below their 52-week high**  
✔ **Stocks 20% up from their 52-week low**  
✔ **Best-performing stocks in the last 30 days**  
✔ **Bar chart visualization**  

---

## **📁 Project Directory Structure**
```
nifty_assignment/
│── assets/
│   ├── data/                  # Stores CSV files with stock data
│   ├── plots/                 # Stores generated bar charts
│── src/
│   ├── nifty_analyser.py       # Main script for fetching & analyzing Nifty 50 data
│── tests/
│   ├── test_nifty_analyser.py  # Unit tests for verification
│── requirements.txt            # Dependencies for the project
│── README.md                   # Project documentation
```

---

## **🔧 Installation & Setup**
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/nifty_assignment.git
cd nifty_assignment
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Analysis**
```bash
python3 src/nifty_analyser.py
```

---

## **📊 Features & Analysis**
| Feature                           | Description |
|------------------------------------|-------------|
| **Top 5 Gainers & Losers**        | Identifies stocks with the highest and lowest percentage gains. |
| **30% Below 52-Week High**        | Finds stocks trading 30% below their highest value in the last year. |
| **20% Up from 52-Week Low**       | Detects stocks recovering 20% or more from their lowest value. |
| **Best 30-Day Performers**        | Highlights stocks with the highest returns in the past month. |
| **Bar Chart Visualization**       | Generates a graphical representation of gainers & losers. |

---

## **🛠 Running Tests**
To validate the script and its outputs, run:
```bash
python3 -m unittest discover -s tests
```

---

## **📂 Output Files**
| File | Location | Description |
|------|---------|-------------|
| `nifty50_data.csv` | `assets/data/` | Stores raw stock data fetched from NSE. |
| `analysis_output.txt` | `assets/data/` | Summary of gainers, losers, and trends. |
| `nifty_gainers_losers.png` | `assets/plots/` | Bar chart visualization. |

---

## **📜 Example Output (Terminal)**
```
Top 5 Gainers:
1. TCS - +3.5%
2. INFY - +2.8%
...

Top 5 Losers:
1. HDFC - -4.2%
2. ICICI - -3.6%
...

Stocks 30% Below 52-Week High:
1. RELIANCE - Currently 32% below 52-week high.
...

Stocks 20% Up from 52-Week Low:
1. SBI - Up 22% from its lowest value.
...

Best 30-Day Performers:
1. BAJAJ AUTO - +12.5% in last 30 days.
...
```

---
To contribute:  
1. **Fork the repository**  
2. **Create a feature branch** (`git checkout -b feature-new-analysis`)  
3. **Commit changes** (`git commit -m "Added new stock filter"`)  
4. **Push to GitHub & create a PR**  

---

## **📧 Contact**
For any issues or suggestions, reach out:  
📩 Email: vivek.patidar@shorthills.ai
🔗 GitHub: [your-username](https://github.com/VivekPatidarShorthillsAI)  

---