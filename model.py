# load dataset
import pandas 
db=pandas.read_csv(“SalaryData.csv”)
print(“\n Thanks For Giving , Your Dataset Loaded Sucessfully......:)\n ”)
# Creating features and target.
#x = feature/independant variable
#y = target / dependant variable
x=db[“YearsExperience”]
y=db[“Salary”]
# loading LinearRegression
from sklearn.linear_model import LinearRegression
model=LinearRegression()
x = db[“YearsExperience”].values.reshape(30,1)
model.fit(x,y)
print(“\n Great your ML Model created Sucessfully.....:)\n ”)
# Saving trained model
import joblib
joblib.dump(model,’salary_model.pkl’)
print(“\n Your Created Model Saved Successfully.....:)\n ”)
