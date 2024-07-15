import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
np.random.seed(42)

fh = pd.read_csv("heart.csv")
X= fh.drop("output", axis=1)
y = fh['output']

features= X.columns.to_list() #used to take the name of the columns
print(features)
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.7,random_state=42)
X_cv, X_test, y_cv, y_test = train_test_split(X_test,y_test,train_size=0.5,random_state=42)

X_train = scaler.fit_transform(X_train)
X_cv = scaler.fit_transform(X_cv)
X_test_s = scaler.fit_transform(X_test)

param_dist = {'C': np.logspace(-3, 3, 100)}

model = LogisticRegression()

#hyperparameter tunning
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=50, cv=5, random_state=42)
random_search.fit(X_train, y_train)
best_params = random_search.best_params_
print(f"Best Parameters: {best_params}")

model = LogisticRegression(C=best_params['C'])
model.fit(X_train, y_train)

#to check which features are important
coefficients = model.coef_[0]
feature_importance = pd.DataFrame({'Feature': features,'Coefficient': coefficients})
feature_importance['Absolute Coefficient'] =np.abs(feature_importance['Coefficient'])
feature_importance = feature_importance.sort_values(by='Absolute Coefficient', ascending=False)
print(feature_importance)

joblib.dump(model, 'model.pkl')
print('Model saved!')
joblib.dump(scaler, 'scaler.pkl')
print("Scaler saved!")

y_predict = model.predict(X_cv)
print(f"Accuracy of the cv set: {accuracy_score(y_cv,y_predict)}")
print(classification_report(y_cv,y_predict))

y_test_predict =model.predict(X_test_s)
print(f"Accuracy of the test set: {accuracy_score(y_test,y_test_predict)}")
print(classification_report(y_test,y_test_predict))
print(f'''Test set vlaues 
{X_test}
      Test set outputs 
{y_test}''')