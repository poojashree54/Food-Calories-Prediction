# Indian Food Calorie Prediction – ML + FastAPI

## Project Overview

**Indian Food Calorie Predictor** is a Machine Learning–powered API that predicts the **Caloric Value of Indian dishes** using macro & micro-nutrient features such as fat, carbohydrates, saturated fats, vitamins, and minerals.

This project demonstrates:

* Feature engineering on nutrition datasets
* Training a regression model (XGBoost)
* Building a REST API with **FastAPI + Uvicorn**
* Deploying as a **Docker container**
* Swagger auto-docs for API interaction

The main goal is to enable **nutrition insights, diet planning, and calorie estimation** for Indian cuisines.

---

## Features

| Component           | Description            |
| ------------------- | ---------------------- |
| ML Regression Model | Predicts caloric value |
| Model Type          | XGBoost Regressor      |
| API Framework       | FastAPI + Uvicorn      |
| Deployment          | Docker                 |
| Docs UI             | `/docs` Swagger        |
| Input Format        | JSON                   |
| Output              | Predicted calories     |

---

## Machine Learning Approach

### **Dataset**

Contains macro & micronutrient values for Indian foods:

* Fat, Carbs, Protein
* Sugar, Fiber, Cholesterol, Sodium
* Vitamins A, B1, B2, B6, B12, C, D, E, K
* Minerals: Ca, Mg, Iron, Zinc, Copper etc.

### **Target**

`Nutrition Density`

### **Model Pipeline**

1. Load & clean data
2. Exploratory data analysis
3. Feature selection
4. Train Multiple Models
5. Best performance model exported with `pickle`

### **Final Output**

Predict Nutrition Density based on numeric nutrient input.

---

## FastAPI Endpoints

| Method | Endpoint   | Description           |
| ------ | ---------- | --------------------- |
| GET    | `/`        | Health check          |
| POST   | `/predict` | Predict Nutrition Density value |

### Example JSON Input (POST `/predict`)

```json
{
  "fat": 10.5,
  "saturated_fats": 3.2,
  "monounsaturated_fats": 4.1,
  "polyunsaturated_fats": 1.8,
  "carbohydrates": 25,
  "sugars": 5,
  "protein": 6,
  "dietary_fiber": 3,
  "cholesterol": 0,
  "sodium": 300,
  "water": 50,
  "vitamin_a": 200,
  "vitamin_b1": 0.2,
  "vitamin_b11": 20,
  "vitamin_b12": 0.1,
  "vitamin_b2": 0.3,
  "vitamin_b3": 1.5,
  "vitamin_b5": 0.5,
  "vitamin_b6": 0.2,
  "vitamin_c": 10,
  "vitamin_d": 0,
  "vitamin_e": 0.5,
  "vitamin_k": 5,
  "calcium": 60,
  "copper": 0.1,
  "iron": 1.2,
  "magnesium": 30,
  "manganese": 0.3,
  "phosphorus": 80,
  "potassium": 150,
  "selenium": 5,
  "zinc": 0.5
}
```

### Response

```json
{
  "prediction": 245.73
}
```

---

## Run Locally (Without Docker)

Make sure dependencies are installed through Pipenv:

```bash
pipenv install
pipenv shell
uvicorn predict:app --reload --port 8000
```

Visit → [http://localhost:8000](http://localhost:8000)
Docs → [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Run With Docker (Recommended)

### Build the Docker Image

```bash
docker build -t food-calorie-api .
```

### Run the Container

```bash
docker run -p 8000:8000 food-calorie-api
```

### Test

| URL                                                      | Description |
| -------------------------------------------------------- | ----------- |
| [http://localhost:8000](http://localhost:8000)           | API Running |
| [http://localhost:8000/docs](http://localhost:8000/docs) | Swagger UI  |

---

## Technologies Used

| Category         | Tech                                         |
| ---------------- | -------------------------------------------- |
| ML               | Python, Pandas, NumPy, Scikit-Learn, XGBoost |
| API              | FastAPI, Uvicorn                             |
| Packaging        | Docker                                       |
| Version Control  | Git & GitHub                                 |
| Deployment Ready | Dockerized Service                           |

---

## Run Locally (Without Docker)
<img width="1887" height="1034" alt="image" src="https://github.com/user-attachments/assets/8c59677f-e19e-4921-a8ad-f48c75e6ca1a" />

<img width="1446" height="943" alt="image" src="https://github.com/user-attachments/assets/9443233d-c1a5-4071-94ad-043bafa9a970" />

## Run Locally (With Docker)
<img width="1435" height="937" alt="image" src="https://github.com/user-attachments/assets/8393522c-199d-4a3c-8dc0-2704b9792290" />

<img width="1164" height="532" alt="image" src="https://github.com/user-attachments/assets/e0132645-3f67-4f0f-867d-9ab54d740d28" />

