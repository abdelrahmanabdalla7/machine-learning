import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

class DataCleaningClass:

        ### Checking outliers
    def columns_boxplot(self,data):
        plt.figure(figsize=(20,20))
        num_cols=data.select_dtypes(include=["number"])
        for index,col in  enumerate(num_cols,start=1):
            plt.subplot(len(num_cols.columns),1,index)
            plt.title(f"{col}")
            sns.boxplot(x=data[col],color="red")
        plt.tight_layout()
        plt.show()

        ### Handling outliers
    def handle_outliers(data,columns,method="IQR",threshold=1.5,strategy="replace"):
        total_outliers=0
        for col in columns:
            if method=="IQR":
                Q1=data[col].quantile(0.25)
                Q3=data[col].quantile(0.75)
                IQR=Q3-Q1
                lower_bound=Q1-threshold*IQR
                upper_bound=Q3+threshold*IQR
            elif method=="zscore":
                pass
            else:
                raise ValueError("Invalid method. Choose 'IQR' or 'Zscore'")

            outliers=data[(data[col]<lower_bound) | (data[col]>upper_bound)]
            outliers_count = len(outliers)
            total_outliers += outliers_count
            print(f"Column {col} has {outliers_count} outliers")

            if  strategy=="replace":
                data[col]=np.clip(data[col],lower_bound,upper_bound)
            elif strategy=="remove":
                data=data[(data[col]>=lower_bound) & (data[col]<= upper_bound)]
            else:
                raise ValueError("Invalid strategy. Choose 'replace' or 'remove'")

        print(f"Total outliers across all columns: {total_outliers}")
        return data
    


    ### Numerical values
    def histogram_boxplot(self,data):
        num_cols=data.select_dtypes(include=["number"])
        plt.figure(figsize=(20,30))
        for index,col in  enumerate(num_cols,start=1):
            plt.subplot(len(num_cols.columns),2,index)
            plt.title(f"{col} distribustion graph")
            sns.histplot(x=data[col],color="red",kde=True)
        plt.tight_layout()
        plt.show()


    def KDEplot (self,data):
        num_cols=data.select_dtypes(include=["number"])
        plt.figure(figsize=(20,30))
        for index,col in  enumerate(num_cols,start=1):
            plt.subplot(len(num_cols.columns),2,index)
            plt.title(f"{col} distribustion graph")
            sns.kdeplot(x=data[col])
        plt.tight_layout()
        plt.show()




    ### Categorical Values
    def countplot (self,data):
        num_cols=data.select_dtypes(include=["category"])
        plt.figure(figsize=(20,30))
        for index,col in  enumerate(num_cols,start=1):
            plt.subplot(len(num_cols.columns),2,index,)
            sns.countplot(x=data[col],data=data,palette="mako")
            plt.title(f"{col} distribustion graph")
        plt.tight_layout()
        plt.show()


    def pieplot(self,data):
        plt.figure(figsize=(20,30))
        num_cols=data.select_dtypes(include=["category"])
        for index,col in  enumerate(num_cols,start=1):
            plt.subplot(len(num_cols.columns),3,index)
            unique= data[col].value_counts()
            count=unique.values
            categories=unique.index
            plt.pie(count,labels=categories,startangle=180,autopct='%1.1d%%')
            plt.title(f"{col} distribustion graph")
        plt.tight_layout()
        plt.show()



### Relationships

### Numerical vs Numerical
    def scatterplot(self,data,target):
        num_cols=data.select_dtypes(include=["number"])
        num_cols = num_cols.drop(columns=[target])
        plt.figure(figsize=(20,30))
        for index,col in  enumerate(num_cols.columns,start=1):
            plt.subplot(len(num_cols.columns),2,index)
            plt.title(f"{col} vs {target}")
            sns.scatterplot(x=data[col],y=data[target],data=data)
        plt.tight_layout()
        plt.show()
    
    def lineplot(self,data,target):
        num_cols=data.select_dtypes(include=["number"])
        num_cols = num_cols.drop(columns=[target])
        plt.figure(figsize=(20,30))
        for index,col in  enumerate(num_cols.columns,start=1):
            plt.subplot(len(num_cols.columns),2,index)
            plt.title(f"{col} vs {target}")
            sns.lineplot(x=data[col],y=data[target],data=data)
        plt.tight_layout()
        plt.show()

    #def pairplot (self,data):


### Numerical vs Categorical
    def barplot(self,data,target):
        num_cols=data.select_dtypes(include=["number"])
        if target not in num_cols.columns:
            pass
        else:
            num_cols = num_cols.drop(columns=[target])
        plt.figure(figsize=(20,30))
        for index,col in  enumerate(num_cols.columns,start=1):
            plt.subplot(len(num_cols.columns),2,index)
            plt.title(f"{col} vs {target}")
            sns.barplot(x=data[col],y=data[target],data=data)
        plt.tight_layout()
        plt.show()




