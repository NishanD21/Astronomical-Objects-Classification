import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def predictor(alpha, delta, u, g, i, r, z, redshift): # To predict the class of the astronomical objet for given features.
    # Load the trained model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Make the prediction
    x = np.array([[alpha, delta, u, g, i, r, z, redshift]])
    prediction = model.predict(x)[0]
    
    # Map the predicted value to the desired class
    if prediction == 0:
        return "Galaxy"
    elif prediction == 1:
        return "Quasar"
    elif prediction == 2:
        return "Star"
    else:
        return "Unknown"
    
def plot_feature_distribution(data): # To plot the distribution of each feature in the dataset.

    # Extract the features
    features = data.columns[:-1]

    # Plot the distribution of each feature
    for feature in features:
        sns.displot(data=data, x=feature, hue='class', kde=True)
        plt.title(f"Distribution of {feature}")
        plt.show()


def plot_correlation_matrix(data): #To Plot the correlation matrix of the dataset.

    # Calculate the correlation matrix
    corr_matrix = data.corr()

    # Plot the correlation matrix
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()


def get_feature_names():# To get the names of the features used to train the model.

    return ['alpha', 'delta', 'u', 'g', 'i', 'r', 'z', 'redshift']

# Feature descriptions
FEATURES = {
    'u': 'U-band (ultraviolet) magnitude',
    'g': 'G-band (green) magnitude',
    'r': 'R-band (red) magnitude',
    'i': 'I-band (infrared) magnitude',
    'z': 'Z-band (near-infrared) magnitude',
    'redshift': 'Redshift (measure of the expansion of the universe)',
    'ra': 'Right ascension (angular distance eastward along the celestial equator from the vernal equinox)',
    'dec': 'Declination (angular distance north or south of the celestial equator)'
}

def get_feature_descriptions(): #To get the feature descriptions
    return FEATURES

