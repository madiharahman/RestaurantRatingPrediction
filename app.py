from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline
import pandas as pd

app = Flask(__name__)

# Home Page
@app.route("/")
def home_page():
    return render_template("home.html")

# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Prediction Page - Form + Result
@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            name=request.form.get('name'),
            online_order=request.form.get('online_order'),
            book_table=request.form.get('book_table'),
            rate=request.form.get('rate'),
            votes=request.form.get('votes'),
            location=request.form.get('location'),
            rest_type=request.form.get('rest_type'),
            cost2plates=float(request.form.get('cost2plates')),
            category=request.form.get('category'),
            grouped_cuisines=request.form.get('grouped_cuisines')
        )
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        results = round(pred[0], 2)
        return render_template('form.html', final_result=results)

# Auto-Suggest Route
@app.route('/suggest')
def suggest():
    query = request.args.get('q', '').lower().strip()  # Clean the query
    df = pd.read_csv("notebooks/data/cleaned_data.csv")
    restaurant_names = df['name'].dropna().unique()

    # Use startswith or contains for dynamic filtering
    matches = [name for name in restaurant_names if query in name.lower()]
    return jsonify(matches[:10])  # Return top 10 matches

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=8000)
