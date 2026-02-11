## Flight Price Prediction

A machine learning-powered web application that predicts flight ticket prices using advanced predictive models and an intuitive Streamlit interface.

## 📋 Description

This project is a **Flight Price Prediction Web Application** built using machine learning techniques and deployed with Streamlit. It enables users to input flight details and receive accurate price predictions based on historical flight data patterns.

## ✨ Features

- **Machine Learning Model**: Pre-trained model for accurate flight price predictions
- **Web Interface**: Interactive Streamlit application for easy user interaction
- **Data Preprocessing**: Integrated encoders for categorical variable transformation
- **Real-time Predictions**: Get instant price predictions for your flight queries
- **User-Friendly Design**: Simple and intuitive interface for all users

## 📁 Project Structure

```
Flight_Price_Prediction/
├── app.py                 # Main Streamlit application
├── model.pkl             # Pre-trained ML model
├── encoders.pkl          # Categorical encoders for data preprocessing
├── requirements.txt      # Project dependencies
├── .devcontainer/        # Dev container configuration
└── README.md             # This file
```

## 🛠️ Tech Stack

- **Python 3.x**: Core programming language
- **Streamlit**: Web application framework
- **scikit-learn**: Machine learning model
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

## 📦 Dependencies

The project uses the following main dependencies (see `requirements.txt` for complete list):

- streamlit
- scikit-learn
- pandas
- numpy

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sejalambekar04/Flight_Price_Prediction.git
   cd Flight_Price_Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Launch the Streamlit app with:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 💡 How It Works

1. **Input Flight Details**: Enter flight information (departure/arrival cities, date, time, airline, etc.)
2. **Data Preprocessing**: The application encodes categorical variables using pre-trained encoders
3. **Prediction**: The machine learning model processes the input and generates a price prediction
4. **Display Results**: The predicted flight price is displayed to the user

## 📊 Model Information

- **Type**: Supervised Learning Regression Model
- **Pre-trained**: Yes - model is provided as `model.pkl`
- **Encoders**: Categorical variable encoders stored in `encoders.pkl`
- **Training Data**: Historical flight pricing data

## 🔧 Development

### Project Setup with Dev Container

This project includes a `.devcontainer` configuration for consistent development environments. If using VS Code with Dev Containers:

1. Install the "Dev Containers" extension
2. Open the project folder
3. Click "Reopen in Container"

## 📝 Usage Example

Once the Streamlit app is running:

1. Fill in the flight details in the sidebar or main form
2. Select relevant parameters (departure city, arrival city, date, etc.)
3. Click the prediction button
4. View the predicted flight price

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙋‍♂️ Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/sejalambekar04/Flight_Price_Prediction/issues).

## 👨‍💻 Author

**Sejal Ambekar**
- GitHub: [@sejalambekar04](https://github.com/sejalambekar04)

## 🔗 Project Links

- **Repository**: https://github.com/sejalambekar04/Flight_Price_Prediction
- **Issues**: https://github.com/sejalambekar04/Flight_Price_Prediction/issues

---

**Last Updated**: February 2026
