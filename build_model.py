from sklearn.externals import joblib
import numpy as np

if __name__ == "__main__":
        
        estimator = joblib.load('predicted.pkl')
        instance=[40.75038236, -73.90333918,1,1,2,1,1,1,9.83333333]
        instance=[instance]
        prediction = estimator.predict(instance)
        print(np.exp(prediction))
   