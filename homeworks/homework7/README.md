# Housing Prices: Advanced Regression Techniques

## Problem Description

This project addresses the prediction of housing prices using advanced regression techniques. Based on the Kaggle dataset "House Prices: Advanced Regression Techniques," the objective is to predict the sale price of residential properties in Ames, Iowa, using 79 explanatory variables that describe aspects of the homes.

### Project Files
- `data_description.txt`: Detailed description of all variables
- `train.csv`: Training dataset with known prices
- `test.csv`: Test dataset for predictions

## Modeling Approach

### Data Preparation and EDA

**Note**: For simplicity, limited data preprocessing is performed. This likely affects the effectiveness of the price predictions. Transformations, outlier and categorical variable handling, etc., remain to be done. This submission is for educational purposes only.

- **Data Cleaning**: Handling missing values ​​(not outliers)
- **Exploratory Analysis**: Price distribution, correlations between variables

### Models to Implement
**Note**: For this regression problem, the following appropriate models will be used:

1. **Linear Regression**: Baseline model
2. **Decision Tree Regressor**: Nonlinear model
3. **Random Forest Regressor**: Ensemble method
4. **XGBoost Regressor**: Advanced gradient boosting

### Evaluation Metrics
For regression problems, the appropriate metrics are:

- **RMSE (Root Mean Squared Error)**: Main metric

*Improvement Note*: The metrics mentioned (Accuracy, Precision, Recall, F1, ROC, AUC) are for classification, not regression.

## Web Service Implementation (to be added)

### Project Structure
```
├── notebooks/
│ └── house_prices_eda.ipynb
├── src/
│ ├── train.py
│ ├── predict.py
│ └── preprocessing.py
├── models/
│ └── best_model.pkl
├── app/
│ ├── main.py
│ └── schemas.py
├── Dockerfile
├── pyproject.toml
└── requirements.txt
```

### Local Development with FastAPI
```python
# app/main.py
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('models/best_model.pkl')

@app.post("/predict")
async def predict_price(features: dict): 
# Preprocessing and prediction 
return {"predicted_price": prediction}
```

### Containerization with Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY. .
RUN pip install uv && uv pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Cloud Deployment

### Deployment Options (not performed in this release)
1. **Google Cloud Run**: Serverless, auto-scaling
2. **AWS ECS/Fargate**: Managed containers
3. **Azure Container Instances**: Rapid deployment
4. **Railway/Render**: Simplified platforms

### Example with Google Cloud Run
```bash
# Build y push imagen
docker build -t gcr.io/PROJECT_ID/house-prices-api .
docker push gcr.io/PROJECT_ID/house-prices-api

# Deploy
gcloud run deploy house-prices-api \
  --image gcr.io/PROJECT_ID/house-prices-api \
  --platform managed \
  --region us-central1
```
## Possible Improvements

### Data and Preprocessing
- Advanced **feature selection** with statistical methods
- More sophisticated **outlier detection**
- **feature engineering** based on domain knowledge

### Modeling
- **Ensemble methods** combining multiple algorithms
- **Hyperparameter tuning** with Optuna or Hyperopt
- **Cross-validation** stratified by price ranges

### Production
- **Model monitoring** to detect drift
- **A/B testing** for new versions
- Full **logging** and **observability**
- **API rate limiting** and **authentication**
- Automated CI/CD pipeline

### Scalability
- Caching of frequent predictions
- Load balancing for high availability
- Database to store prediction history