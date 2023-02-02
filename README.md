# Litter-buster

## Project Description

Litterbuster is an application to identify and catalog instances of littering as well as reporting it.

- [Litter-buster](#litter-buster)
  - [Project Description](#project-description)
  - [Project plan](#project-plan)
    - [**Objectives**](#objectives)
    - [**Methods**](#methods)
    - [**Reference Material**](#reference-material)
    - [**Predictions**](#predictions)
    - [**Predicted issues**](#predicted-issues)
    - [**Project breakdown**](#project-breakdown)
  - [Notes](#notes)
  - [Known issues](#known-issues)
  - [Reflections](#reflections)
    - [Andreas Comments](#andreas-comments)
      - [Andreas Länkar](#andreas-länkar)

## Project plan

### **Objectives**

1. Train machine learning models to identify person.
2. Train machine learning model to recognize person in images.
3. We will also build a machine learning model to recognize littering.
4. Create a backend-application to run the machine-learning functions.
5. Lastly there will be an application to view instances of littering from a database.
6. Create a database structure to catalog the classified images.
7. Build an application to send images of littering to an email-adress.
8. Create a dashboard showing data and predictions.
9. Create a DAG for regular re-learning of the model based on images stored in database. [Maybe better alternative](https://medium.com/value-stream-design/online-machine-learning-515556ff72c5)

### **Methods**

- **Python libraries**

  - OpenCV
  - Flask
  - Dash
  - Numpy
  - Pandas
  - SKlearn
  - PostgreSQL
  - Pickle

- **Apache Airflow**
- **Agile**
  - Jira
    - [Link to Jira](https://mcvk.atlassian.net/jira/software/projects/LB/boards/2)
    - Continuous progress documentation
  - Stand-ups: _@09.00_
  - Check-out: _@16.45_
- **Github**
  - [Link to GitHub Repo](https://github.com/Swamp-Solutions/Litter-buster)
  - Development in personal development branch
    - Changelogs in personal development branches
    - Document code before merging into Main Development
    - Merge into Main Development
      - Update Main Development changelog
      - When Main Development works, merge into Main
      - Tag Main version
    - Discuss merge requests at Check-out

### **Reference Material**

1. Image classification with Scikit-Learn
   - [Kapernikov Tutorial](https://kapernikov.com/tutorial-image-classification-with-scikit-learn/)
   - [Scikit documentation Tutorial](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

-

1. OpenCV

   - [OpenCV Tutorials](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
   - [Face recognition with OpenCV](https://datagen.tech/guides/face-recognition/face-recognition-with-python/)
   - [OpenCV Tips](https://learnopencv.com/getting-started-with-opencv/)

2. Joblib
   - [Joblib Documentation](https://joblib.readthedocs.io/en/latest/)

### **Predictions**

- Predict person will litter
- Predict littering peak-littering-times
- Predict clean-up need

### **Predicted issues**

- Object recognition distance
- The distance to the object may affect recognition.
- Lighting conditions may affect the recognition.

### **Project breakdown**

- [ ] Face recognition and classification

  - [ ] Mark identified face
  - [ ] Create face classes based on picture and description
    - [ ] Only Name to start with

- [ ] Litter identification
  - [ ] Mark identified litter
  - [ ] Application to save instances of litter
    - [ ] Save timestamp
    - [ ] Save location
  - [ ] Predict litter patterns in an area
  - [ ] Check instances of litter in Movie/Video
  - [ ] Visualize

## Notes

## Known issues

- GDPR has to be taken into consideration if using facial recognition functions.

## Reflections

### Andreas Comments

Link in 9. in Objectives
Decide on Dataset for litter
Find method for loading model in scikit learn

#### Andreas Länkar

[What is Online Machine Learning?](https://medium.com/value-stream-design/online-machine-learning-515556ff72c5)

[Litter Detection with Deep Learning: A Comparative Study](https://www.mdpi.com/1424-8220/22/2/548)

[PlastOPol: A Dataset for Litter Detection](https://zenodo.org/record/5829156#.Y9vM6XbMJmM)

[Add new data to a pretrained model](https://towardsdatascience.com/how-to-add-new-data-to-a-pretrained-model-in-scikit-learn-ce16911afe33)
