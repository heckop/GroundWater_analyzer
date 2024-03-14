# Ground Water Quality Assessment using Machine Learning

This repository contains a machine learning model for assessing the quality of ground water based on various chemical and physical parameters. The model is designed to predict the suitability of ground water for different purposes, such as drinking, livestock, poultry, and crop cultivation.

## Project Overview

The project aims to develop and compare the performance of various machine learning algorithms for a multi-class classification problem, where the goal is to predict the ground water quality based on provided features. The features include districts, mandals, villages, latitude, longitude, and various chemical concentrations.

The primary objectives of this project are:

1. Preprocess and integrate the available ground water quality data.
2. Implement and train various machine learning models, including Softmax Classification, Decision Trees, Random Forests, Naive Bayes, and K-Nearest Neighbors.
3. Evaluate and compare the performance of the trained models using metrics such as accuracy, precision, recall, F1-score, and area under the receiver operating characteristic curve (AU-ROC).
4. Explore additional techniques like feature engineering, ensemble methods (e.g., XGBoost, GBM), and dimensionality reduction to improve model performance.
5. Investigate the calculation of the Entropy-based Water Quality Index (EWQI) as an alternative to the traditional Water Quality Index (WQI).
6. Develop a web application for deploying the trained models, allowing users to input chemical compositions and predict ground water quality.

## Dataset

The project uses the following datasets provided by the Telangana Open Data Portal:

- [Telangana Ground Water Department Pre-Monsoon Water Quality Data](https://data.telangana.gov.in/dataset/telangana-ground-water-department-pre-monsoon-water-quality-data)
- [Telangana Ground Water Department Post-Monsoon Water Quality Data](https://data.telangana.gov.in/dataset/telangana-ground-water-department-post-monsoon-water-quality-data)

## Repository Structure

The repository is structured as follows:

```
ground-water-quality-model/
├── data/
│   ├── pre_monsoon/
│   └── post_monsoon/
├── models/
│   ├── softmax.py
│   ├── decision_tree.py
│   ├── random_forest.py
│   ├── naive_bayes.py
│   └── knn.py
├── utils/
│   ├── data_preprocessing.py
│   ├── evaluation.py
│   └── visualization.py
├── app/
│   ├── static/
│   ├── templates/
│   └── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

- `data/`: Directory for storing the ground water quality datasets.
- `models/`: Directory containing the implementations of various machine learning algorithms.
- `utils/`: Directory with utility functions for data preprocessing, evaluation, and visualization.
- `app/`: Directory for the web application code, including static files and templates.
- `requirements.txt`: File listing the required Python packages and their versions.
- `README.md`: This file, providing an overview of the project and repository.
- `LICENSE`: File containing the license information for the project.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/ground-water-quality-model.git`
2. Install the required Python packages: `pip install -r requirements.txt`
3. Preprocess the data by running the appropriate scripts in the `utils/` directory.
4. Train the machine learning models by executing the corresponding scripts in the `models/` directory.
5. Evaluate the trained models using the evaluation functions in `utils/evaluation.py`.
6. Explore additional techniques, such as feature engineering, ensemble methods, and dimensionality reduction, as desired.
7. To run the web application, navigate to the `app/` directory and execute `python app.py`.

## License

This project is licensed under the [MIT License](LICENSE).
