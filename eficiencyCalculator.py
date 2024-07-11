import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def financialImpact():
    previous_years_years =np.arange(2016,2021,1).reshape(-1,1)
    previous_years_expenses = np.asarray([24*1e4,26*1e4,29*1e4,32*1e4,37*1e4]).reshape(-1,1)
    linearRegression = LinearRegression()
    linearRegression.fit(previous_years_years,previous_years_expenses)
    coefs = linearRegression.coef_
    x=np.arange(2016,2023,1).reshape(-1,1)
    y = linearRegression.predict(x)
    plt.figure(figsize=(10,8))
    plt.title("Maintanence expenses in air system and its estimative for year 2022",fontsize=18)
    plt.plot(previous_years_years,previous_years_expenses,'ok',markersize=10)
    plt.bar(np.append(previous_years_years,x[-1]),np.append(previous_years_expenses,y[-1]),width=0.6,color="green",alpha=0.5)
    plt.plot(x,y,'--r',linewidth=1.8)
    plt.plot(x[-1],y[-1],'ob',markersize=10)
    plt.ylabel("Cost in dollars ($)",fontsize=18)
    plt.xlabel("Years",fontsize=18)
    plt.legend(["Known cost in previous years","Expenses tendency","Expected cost in 2022"],fontsize=12)
    plt.savefig("financial_impact.png")
    plt.show()
    plt.figure(figsize=(10,8))
    plt.title("Maintanence expenses in air system and its estimative for year 2022",fontsize=18)
    plt.plot(previous_years_years,previous_years_expenses,'ok',markersize=10)
    plt.bar(np.append(previous_years_years,x[-1]),np.append(previous_years_expenses,y[-1]),width=0.6,color="green",alpha=0.5)
    plt.plot(x,y,'--r',linewidth=1.8)
    plt.plot(x[-1],y[-1],'or',markersize=10)
    plt.plot([2022],[16434],'ob',markersize=10)
    plt.bar([2022],[16434],width=0.4,color="blue",alpha=0.6)
    plt.ylabel("Cost in dollars ($)",fontsize=18)
    plt.xlabel("Years",fontsize=18)
    plt.legend(["Known cost in previous years","Expenses tendency","Expected cost in 2022"],fontsize=12)
    plt.savefig("financial_impact_ML.png")
    plt.show()

