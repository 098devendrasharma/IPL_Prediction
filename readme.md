# IPL Score Prediction 🏏

A machine learning web application that predicts Indian Premier League (IPL) cricket match scores in real-time based on match situation parameters.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![ML](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)

## 📋 Overview

This project uses machine learning to predict IPL match scores based on current match conditions. Users can input various match parameters through a web interface, and the trained model provides real-time score predictions.

## ✨ Features

- **Real-time Predictions**: Get instant score predictions based on current match situation
- **User-Friendly Interface**: Clean and intuitive web UI for easy interaction
- **Machine Learning Model**: Pre-trained model (`pipe.pkl`) for accurate predictions
- **Flask Web Application**: Lightweight and responsive web framework

## 🗂️ Project Structure

```
IPL_Prediction/
├── Prediction/          # Core prediction module with ML model training code
├── templates/           # HTML templates for the web interface
├── app.py              # Flask application entry point
├── pipe.pkl            # Serialized trained ML model
├── requirements.txt    # Python dependencies
├── .gitignor          # Git ignore file
└── README.md          # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/098devendrasharma/IPL_Prediction.git
   cd IPL_Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the web interface**
   - Open your browser and navigate to `http://localhost:5000`

## 📊 How It Works

1. **Input Match Parameters**: Users enter current match conditions such as:
   - Batting team
   - Bowling team
   - Current score
   - Overs completed
   - Wickets fallen
   - Other relevant match statistics

2. **Model Prediction**: The trained machine learning model processes the inputs and predicts the final score

3. **Display Results**: The predicted score is displayed on the web interface

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Flask**: Web framework for the application
- **Scikit-learn**: Machine learning library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Pickle**: Model serialization

## 📁 Key Components

### `app.py`
The main Flask application file that handles:
- Web routing
- User input processing
- Model loading and prediction
- Response rendering

### `pipe.pkl`
The serialized machine learning pipeline containing:
- Pre-trained model
- Feature preprocessing steps
- Model parameters

### `Prediction/`
Contains the model training scripts and data processing code

### `templates/`
HTML templates for the web interface

## 🎯 Model Details

The machine learning model is trained on historical IPL match data and uses various features to predict match outcomes. The model pipeline includes:
- Data preprocessing
- Feature engineering
- Model training and validation
- Hyperparameter tuning

## 📝 Usage Example

1. Start the Flask application
2. Navigate to the web interface
3. Select the batting and bowling teams
4. Enter current match statistics (runs, wickets, overs)
5. Click "Predict" to get the estimated final score

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

Devendra Sharma - [@098devendrasharma](https://github.com/098devendrasharma)

Project Link: [https://github.com/098devendrasharma/IPL_Prediction](https://github.com/098devendrasharma/IPL_Prediction)

## 📜 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- IPL for providing the historical match data
- The cricket analytics community
- Open source contributors

---

**Note**: This is an educational project for learning machine learning and web development. Predictions are based on historical data and may not reflect actual match outcomes.
