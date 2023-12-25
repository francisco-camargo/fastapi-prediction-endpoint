Creating an Efficient Prediction API Endpoint with FastAPI
==========================================================

Based on the chapter, Creating an Efficient Prediction API Endpoint with FastAPI, from the book [Building Data Science Applications with FastAPI - Second Edition](https://www.amazon.com/Building-Data-Science-Applications-FastAPI-ebook/dp/B0C9D1QYVX?qid=1692021319&refinements=p_27:Fran%C3%A7ois+Voron&s=digital-text&sr=1-1&text=Fran%C3%A7ois+Voron&linkCode=sl1&tag=mobilea00b2a6-20&linkId=751999f2c2a85565dbd749e640befa60&language=en_US&ref_=as_li_ss_tl) by François Voron which covers
* Persisting a trained model with Joblib
* Implementing an efficient prediction endpoint
* Caching results with Joblib

In this repo we take as given a trained model which categorizes news articles using multinomial Naive Bayes. To learn about training this model, see the chapter Introduction to Data Science in Python.

Run app with `uvicorn prediction_endpoint:app --reload`

View documentation at `http://localhost:8000/docs`
