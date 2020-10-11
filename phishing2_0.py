import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
# %matplotlib inline

# Filter the uneccesary warnings
import warnings
warnings.filterwarnings("ignore")

df1 = pd.read_csv('Phishing.csv')
df = pd.DataFrame()
df['SSLfinal_State']=df1['SSLfinal_State']
df['URL_of_Anchor']=df1['URL_of_Anchor']
df['Prefix_Suffix']=df1['Prefix_Suffix']
df['web_traffic']=df1['web_traffic']
df['Domain_registeration_length']=df1['Domain_registeration_length']
df['Result']=df1['Result']

df['Result'] = df['Result'].map({-1:0, 1:1})
df['Result'].unique()
#to check null values in the dataframe
df.isnull()

from sklearn.model_selection import train_test_split
X=df.drop("Result",axis=1).values
y=df["Result"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

from sklearn.ensemble import RandomForestClassifier
error= []
# Will take some time
for i in range(550,600):
    rfc = RandomForestClassifier(n_estimators=i)
    rfc.fit(X_train,y_train)
    pred_i = rfc.predict(X_test)
    error.append(np.mean(pred_i != y_test))

rfc = RandomForestClassifier(n_estimators=571)
rfc.fit(X_train,y_train)


pickle.dump(rfc,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))