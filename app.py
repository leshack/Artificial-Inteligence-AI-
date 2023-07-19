from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

def predict_exercise_intensity(user_input):
    # Load the trained model
    with open('kitale_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    # Define expected features and mappings
    expected_features = ['Calories to Burn (Kcal)', 'Dream Weight', 'Actual Weight', 'Age', 'Duration',
                         'maximum Heart Rate', 'Height', 'Weather Conditions', 'Gender']
    weather_mapping = {'Sunny': 0, 'Cloudy': 1, 'Rainy': 2}
    gender_mapping = {'Male': 0, 'Female': 1}

    # Define exercise intensity descriptions
    exercise_intensity_descriptions = {
        1: 'Very low intensity: Suitable for individuals with minimal physical activity, such as walking at a leisurely pace, stretching or yoga, and gentle swimming. However, please note that your preference is prioritized.',
        2: 'Low intensity: Suitable for beginners or individuals with limited physical activity, such as light jogging or running, cycling at a relaxed pace, and beginner\'s aerobics. However, please remember that your preference takes priority.',
        3: 'Moderate intensity: Suitable for individuals who engage in regular physical activity, including brisk walking, dancing, and water aerobics. However, please keep in mind that your preference is given priority.',
        4: 'Medium intensity: Suitable for individuals with moderate fitness and physical activity, such as power walking, cycling at a moderate pace, and Zumba. However, please remember that your preference is given priority.',
        5: 'Moderate to high intensity: Suitable for individuals with moderate to high fitness levels, including jogging or running at a moderate pace, high-intensity interval training (HIIT), and kickboxing. However, please note that your preference is given priority.',
        6: 'High intensity: Suitable for individuals with a high level of fitness and physical activity, such as running at a fast pace, circuit training, and CrossFit. However, please keep in mind that your preference is given priority.',
        7: 'High intensity: Suitable for individuals with a high level of fitness and physical activity, such as advanced HIIT workouts, competitive sports (e.g., soccer, basketball), and spinning or indoor cycling classes. However, please remember that your preference is given priority.',
        8: 'Very high intensity: Suitable for individuals with very high fitness and physical activity, including sprinting or interval sprints, plyometric exercises, and heavy weightlifting. However, please keep in mind that your preference is given priority.',
        9: 'Very higher intensity: Suitable for individuals with very high fitness and physical activity, such as advanced CrossFit workouts, box jumps, and Olympic weightlifting. However, please note that your preference is given priority.',
        10: 'Extremely high intensity: Suitable for athletes or individuals with exceptional fitness levels, including professional sports training, marathon running, and elite-level strength and conditioning programs. However, please remember that your preference is given priority.'
    }

    # Encode categorical variables and prepare user input
    user_input_encoded = user_input.copy()
    user_input_encoded['Weather Conditions'] = user_input_encoded['Weather Conditions'].map(weather_mapping)
    user_input_encoded['Gender'] = user_input_encoded['Gender'].map(gender_mapping)
    user_input_encoded = user_input_encoded.reindex(columns=expected_features)

    # Make prediction
    predicted_intensity = loaded_model.predict(user_input_encoded)
    rounded_intensity = int(round(predicted_intensity[0]))
    intensity_description = exercise_intensity_descriptions.get(rounded_intensity, 'No description available')

    max_heart_rate = 220 - int(user_input_encoded['Age'].values[0])

    return rounded_intensity, intensity_description, max_heart_rate

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract user input from the form
        calorie_range = request.form['calorie_range']
        dream_weight = int(request.form['dream_weight'])
        actual_weight = int(request.form['actual_weight'])
        age = int(request.form['age'])
        duration = int(request.form['duration'])
        height = float(request.form['height'])
        weather_conditions = request.form['weather_conditions']
        gender = request.form['gender']

        user_input = pd.DataFrame({
            'Calories to Burn (Kcal)': [0.0],
            'Dream Weight': [dream_weight],
            'Actual Weight': [actual_weight],
            'Age': [age],
            'Duration': [duration],
            'maximum Heart Rate': [0],
            'Height': [height],
            'Weather Conditions': [weather_conditions],
            'Gender': [gender]
        })

        # Map calorie range to numeric values
        calorie_mapping = {
            '100 and Below': -1,
            '101 to 200': -0.5,
            '201 to 300': 0.1,
            '301 to 400': 0.3,
            '401 to 500': 0.8,
            '501 to 600': 1.3,
            '601 to 700': 1.6,
            '701 to 800': 1.9,
            '801 and Above': 3.7
        }

        user_input['Calories to Burn (Kcal)'] = calorie_mapping[calorie_range]

        # Get prediction results
        rounded_intensity, intensity_description, max_heart_rate = predict_exercise_intensity(user_input)

        # Prepare the response as a JSON object
        response = {
            'intensity': rounded_intensity,
            'description': intensity_description,
            'heart_rate': max_heart_rate
        }

        return jsonify(response)

    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 500

if __name__ == '__main__':
    app.run(port=4000)
