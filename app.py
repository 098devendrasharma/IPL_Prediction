from flask import Flask, render_template, request
import pickle
import mysql.connector
import pandas as pd

app = Flask(__name__)

# 1. Load your Model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# 2. Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789', # Change this
    'database': 'cricket_db'    # Change this
}

teams = ['Mumbai Indians', 'Chennai Super Kings', 'Kolkata Knight Riders',
         'Royal Challengers Bengaluru', 'Rajasthan Royals', 'Delhi Capitals',
         'Sunrisers Hyderabad', 'Kings XI Punjab', 'Lucknow Super Giants', 'Gujarat Titans']

cities = ['Mohali', 'Durban', 'Mumbai', 'Delhi', 'Hyderabad', 'Bangalore',
          'Kolkata', 'Abu Dhabi', 'New Chandigarh', 'Ahmedabad',
          'Visakhapatnam', 'Dharamsala', 'Pune', 'Chennai', 'Bengaluru',
          'East London', 'Jaipur', 'Cape Town', 'Navi Mumbai', 'Guwahati',
          'Centurion', 'Johannesburg', 'Chandigarh', 'Indore', 'Dubai',
          'Lucknow', 'Raipur', 'Cuttack', 'Sharjah', 'Bloemfontein',
          'Port Elizabeth', 'Ranchi', 'Kimberley', 'Nagpur']

@app.route('/')
def index():
    return render_template('index.html', teams=sorted(teams), cities=sorted(cities))

@app.route('/predict', methods=['POST'])
def predict():
    # Capture Form Data
    batting_team = request.form.get('batting_team')
    bowling_team = request.form.get('bowling_team')
    city = request.form.get('city')
    target = int(request.form.get('target'))
    score = int(request.form.get('score'))
    wickets = int(request.form.get('wickets'))
    overs = float(request.form.get('overs'))

    # Calculations for Model Input
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    # Create Input DataFrame for pipe.pkl
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_left],
        'runs_total_x': [target],
        'curr_run_rate': [crr],
        'req_run_rate': [rrr]
    })

    # Get Prediction (Probability)
    result = pipe.predict_proba(input_df)
    win_prob = round(result[0][1] * 100) # Probability of batting team winning
    loss_prob = round(result[0][0] * 100)
    # print(result)
    prediction_text = f"{batting_team}: {win_prob}% | {bowling_team}: {loss_prob}%"

    # 3. Save to MySQL
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = """INSERT INTO predictions 
                   (batting_team, bowling_team, city, target, score, wickets, overs, win_probability) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (batting_team, bowling_team, city, target, score, wickets, overs, win_prob)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database Error: {e}")

    return render_template('index.html', teams=sorted(teams), cities=sorted(cities), result=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)