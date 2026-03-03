# HousePricePrediction

This project provides a modular machine learning pipeline for house price prediction with a Streamlit interface.

## Project Structure

- `data/raw` for raw datasets
- `notebooks` for EDA notebooks
- `src` for source modules (components, pipeline, entity)
- `artifacts` for trained model and preprocessor files
- `app.py` for Streamlit app entrypoint

## Run

1. Train the model artifacts:

```bash
python src/pipeline/training_pipeline.py
```

2. Start Streamlit app:

```bash
streamlit run app.py
```
