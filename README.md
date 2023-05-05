# Astronomical-Objects-Classification
This project investigates the impact of Redshift on Classification of astronomical Objects of Stars, Galaxies and Quasars with Machine Learning.

## ML model training and evaluation architecture

![Architecture](https://user-images.githubusercontent.com/108488940/235837891-16cf41b1-009c-4b11-abcd-a62eda8eb562.png)

Descriptions of files and folders
--------------------------------

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

10_sgq_predictor - Python Source file to predict the class of astronomical objects for given parameters.
