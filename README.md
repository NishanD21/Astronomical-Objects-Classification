# Astronomical-Objects-Classification
This project investigates the impact of Redshift on Classification of astronomical Objects of Stars, Galaxies and Quasars with Machine Learning.

## ML model training and evaluation architecture

![Architecture](https://user-images.githubusercontent.com/108488940/235837891-16cf41b1-009c-4b11-abcd-a62eda8eb562.png)

# Project Summary

This research study investigates the impact of redshift on the classification of galaxies, quasars, and stars using machine learning techniques. The study uses the catalog data from the seventeenth release of the SDSS survey, which includes information on spectral features and astronomical coordinates of galaxies, quasars and stars. The dataset was normalized using two methods of min-max and z-score, to cross-check the accuracy of the machine learning models and to select the ideal feature scaling method from the two methods. Two datasets were created from each normalization method by keeping redshift field and removing redshift field, resulting four datasets in total. Five different machine learning models, namely Random Forest, SVM, ERT, Decision Tree, and KNN, were trained on these datasets, and their performance was evaluated using confusion matrix, accuracy, precision, recall, and F1 score evaluation metrics.
The results of the evaluation have shown that the Random Forest algorithm consistently outperformed other machine learning models in all scenarios. Extremely randomized trees model (ERT) has shown a closer accuracy to random forest. Support Vector Machines (SVM) has given the lowest accuracies out of all the models. Moreover, the z-score normalization method performed better than the min-max normalization method, possibly because it is less sensitive to outliers and more robust to the range of values in the dataset. The inclusion of redshift as a feature in the dataset had a significant positive impact on the classification performance of all three classes.
Stars have the highest impact from the inclusion of redshift feature in the dataset. The accuracy of classification improved from 89.31% without redshift to 99.68% with redshift for stars (An improvement of 10.37%). The particular improvement is higher than both galaxies’ and quasars’.
Based on these results, a Python package was built and uploaded to PyPI, using the Random Forest algorithm and the dataset with the redshift field to classify astronomical objects of galaxies, quasars, and stars. This study demonstrates the effectiveness of machine learning techniques in classifying astronomical objects and the importance of including redshift as a feature in the dataset for accurate classification. The findings of this study can be useful in improving the accuracy of classification algorithms in future astronomical surveys.


# Descriptions of files and folders

Datasets - Folder consisting all the datasets used for the research study.

1_feature_engineering  -  Jupyter Source file of feature engineering done for sgq_classification dataset.

2_exploratory_analysis - Jupyter Source file of exploratory analysis conducted for the dataset.

3_ml_min_max_w_redshift - Jupyter Source file of Machine Learning models training for the data set normalized by min-max method and without redshift field.

4_ml_min_max_redshift - Jupyter Source file of Machine Learning models training for the data set normalized by min-max method and with redshift field.

5_ml_z_sc_w_redshift - Jupyter Source file of Machine Learning models training for the data set normalized by z-score method and without redshift field.

6_ml_z_sc_redshift - Jupyter Source file of Machine Learning models training for the data set normalized by z-score method and with redshift field.

7_impact_of_rs_for_classes - Jupyter Source file of evaluating the classification accuracy of each class of astronomical objects.

8_pickle_for_package - Jupyter Source file of creating pickle file for python package development.

model.pkl - Pickle file created for python package development.

skyndo - folder consisting files created for "skyndo" python package.

9_package_test - Jupyter Source file of package testing.

