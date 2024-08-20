# Canadian Tech Industry Salary Dashboard and Prediction App

This project involves the analysis and prediction of salaries in the Canadian tech industry using data from the Stack Overflow Developer Survey available on Kaggle. It includes two main components:

1. **Power BI Dashboard**: A comprehensive dashboard that provides insights into salary distributions, trends, and other key metrics within the Canadian tech industry.

2. **Machine Learning Prediction App**: A web application developed using Streamlit that predicts salaries for various tech roles based on user inputs such as company size, industry, experience, title, and location.

## Project Components

### 1. Power BI Dashboard
- **Features**:
  - Salary distribution across different tech roles in Canada.
  - Insights into industry-wise salary trends.
  - Analysis of the impact of experience and company size on salaries.
[PowerBI Dashboard](URL)

### 2. Machine Learning Prediction App
- **Model**: The machine learning model used in the app was trained on the same Stack Overflow survey data. The model predicts estimated salaries based on selected features.
- **Web App**: The app allows users to input details like company size, industry, experience, job title, and location to receive a salary estimate.
- **Deployment**: The app is deployed using Streamlit.
  [ML App](URL)

## Installation

To run the prediction app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/canadian-tech-salary-prediction.git
   cd canadian-tech-salary-prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```


## Notes

- The estimated salary provided by the app is an approximation and is intended for informational purposes only. The underlying data may not be adequate for real-world applicability.
- The app is designed with a focus on Canadian tech roles and may not accurately predict salaries outside of this context.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

