#Invoice tax calculation
# def calculate_tax(amount, tax_rate):
#     tax= amount*tax_rate/100
#     total=amount+tax
#     return tax, total
# tax, total=calculate_tax(1000,18)
# print("Tax:", tax)
# print("Total amount:",total)

#fixed rule
# leave_balance=5
# leave_days=2

# if leave_days <=leave_balance and leave_days>0:
#     print("Eligible for leave")
# else:
#     print("Not eligible for leave")

#prediction from history ->ml
from sklearn.linear_model import LinearRegression
#historical sales data
X=[[1],[2],[3],[4],[5]]
y=[100,200,300,400,500]
model=LinearRegression()
model.fit(X,y)
prediction =model.predict([[6]])
print('Predicated sales:',prediction[0])