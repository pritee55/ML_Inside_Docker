import joblib
model = joblib.load(“salary_model.pkl”)
#predict
years=int(input(“\n Please Enter the  years of Experience: “))
predict=model.predict([[years]])
print(“Your salary is Approximatly :”,round(predict[0],2),” INR \n ”)
