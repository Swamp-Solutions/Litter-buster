# Litter-buster

## Project Description

Litterbuster is an application to identify and catalog instances of littering as well as reporting it.
We are using Jira to track our project progress. Link to projectboard: [Jira](https://mcvk.atlassian.net/jira/software/projects/LB/boards/2)

- [Litter-buster](#litter-buster)
  - [Project Description](#project-description)
  - [Project plan](#project-plan)
    - [Objectives](#objectives)
    - [Methods](#methods)
    - [Predictions](#predictions)
    - [Predicted issues](#predicted-issues)
  - [Known issues](#known-issues)
    - [Alternative solutions](#alternative-solutions)

## Project plan

### Objectives

1. Train machine learning models to identify faces.
2. Train machine learning model to recognize faces in images.
3. We will also build a machine learning model to recognize littering.
4. Create a backend-application to run the machine-learning functions.
5. Lastly there will be an application to view instances of littering from a database.
6. Create a database structure to catalog the classified images.
7. Build an application to send images of littering to an email-adress.
8. Create a dashboard showing data and predictions.

### Methods

- OpenCV
- Flask
- Dash
- Pandas, numpy
- SKlearn
- PostgreSQL
- joblib / pickle

### Predictions

- Predict person will litter
- Predict littering peak-littering-times
- Predict clean-up need

### Predicted issues

- Object recognition distance
- The distance to the object may affect recognition.
- Lighting conditions may affect the recognition.

## Known issues

- GDPR has to be taken into consideration if using facial recognition functions.

### Alternative solutions

- Face recognition and classification
-
