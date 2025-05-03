# Optimizing Decision-Making in E-Commerce using Machine Learning and Data Analytics through a Web-Enabled Predictive System

## 🧠 Problem Statement

This project aims to perform a detailed Exploratory Data Analysis (EDA) on a Zomato restaurant dataset and build a Machine Learning model capable of predicting restaurant ratings based on various features, helping restaurants enhance their services and customer satisfaction.

## 🎯 Objectives

- Assist users in choosing top-rated restaurants based on predictive analysis  
- Help restaurant owners understand factors affecting their ratings  
- Leverage machine learning for the accurate prediction of restaurant performance  
- Visualize trends and insights using dynamic dashboards  

## 🏢 Industry Context and Background

The Indian restaurant industry has rapidly evolved, with an increasing trend towards online food ordering platforms like Zomato. This project analyzes patterns to assist businesses in better targeting their audience and optimizing offerings.

## 📄 Source of Data

- Dataset sourced from Kaggle — a curated version of restaurant information originally scraped from Zomato.

## 🎓 Purpose of Study

To analyze key factors affecting restaurant ratings, such as:

- Location and demography  
- Price range  
- Cuisines served  
- Theme-based restaurant concepts  
- Customer preferences in specific neighborhoods  

## 🛠️ Technologies Used

| Component            | Tools & Frameworks                        |
|----------------------|--------------------------------------------|
| **Backend**          | Python (Flask)                             |
| **Frontend**         | HTML, CSS, JavaScript                      |
| **Data Science**     | Jupyter Notebook, Scikit-learn             |
| **Dashboard**        | Power BI                                   |
| **Development IDE**  | Visual Studio Code                         |

## 📂 Project Structure

```
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── raw.csv
│   ├── train.csv
│   ├── test.csv
├── notebooks/
│   ├── data/
│   │   ├── cleaned_data.csv
│   │   ├── data.csv
│   ├── bangalore.html
│   ├── notebook.ipynb
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipelines/
│   │   ├── training_pipeline.py
│   │   ├── prediction_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
├── static/
│   ├── files/
│   ├── icons/
│   ├── images/
│   ├── js/
│   ├── videos/
├── templates/
│   ├── about.html
│   ├── dashboard.html
│   ├── form.html
│   ├── home.html
├── app.py
├── requirements.txt
├── setup.py
├── README.md
```
## 🤖 Machine Learning Models Used

- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- K-Neighbors Regressor

The best-performing model is selected automatically based on the R² score.

## ✅ Results

Successfully built a **restaurant rating prediction system** integrated into a Flask-based web application, complemented with an interactive **Power BI dashboard** providing rich data visualizations and insights.

## 👩‍💻 Author

**Madiha Rahman**  