import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import scatterplot
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_score

df = pd.read_excel('Latest IPL Season data for ML.xlsx')

def bat(team):
    
    bat_options = ['Batsman','WK-Batsman']
    in_latest_squad = ['YES','NO']
    
    batsman_and_wk_df = df[df['ROLE'].isin(bat_options)]
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['IN_LATEST_SQUAD'].isin(in_latest_squad)]
    batsman_and_wk_df['IN_LATEST_SQUAD'] = batsman_and_wk_df['IN_LATEST_SQUAD'].map({'YES': 1, 'NO': 0})
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['NO_OF_MATCHES_PLAYED']>=1]
    
    x = batsman_and_wk_df[['INNINGS_PLAYED_BATTING','RUNS','BATTING_AVG','BATTING_STRIKE_RATE']].values
    y = batsman_and_wk_df[['IN_LATEST_SQUAD']].values

    x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))
    
    x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.15, random_state=4)
    
    y_train = y_train.reshape(y_train.shape[0],)
    y_test = y_test.reshape(y_test.shape[0],)

    LR = LogisticRegression().fit(x_train,y_train)
    
    batsman_and_wk_df = batsman_and_wk_df[batsman_and_wk_df['TEAM'] == team]
    batsman_and_wk_df = batsman_and_wk_df[['PLAYERS','NO_OF_MATCHES_PLAYED','INNINGS_PLAYED_BATTING','RUNS','BATTING_AVG','BATTING_STRIKE_RATE']]
    batsman_and_wk_df = batsman_and_wk_df.reset_index(drop=True)
        
    X_bat = batsman_and_wk_df[['INNINGS_PLAYED_BATTING','RUNS','BATTING_AVG','BATTING_STRIKE_RATE']].values
    X_bat = X_bat.astype('float64')
    X_bat = preprocessing.StandardScaler().fit(X_bat).transform(X_bat.astype(float))
    
    final_bat_predict = LR.predict_proba(X_bat)
    final_bat_predict_df = pd.DataFrame(final_bat_predict,columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_bat_predict_df = final_bat_predict_df.reset_index(drop=True)
        
    final_bat_predict_df = pd.concat([batsman_and_wk_df, final_bat_predict_df], axis=1, join='inner')

    final_bat_predict_df = final_bat_predict_df.drop(['PROBABILITY_OF_NOT_PLAYING'], axis=1)
    
    return final_bat_predict_df

def bowl(team):
    
    bowl_options = ['Bowler']    
    in_latest_squad = ['YES','NO']
    
    bowler_df = df[df['ROLE'].isin(bowl_options)]
    bowler_df = bowler_df[bowler_df['IN_LATEST_SQUAD'].isin(in_latest_squad)]
    bowler_df['IN_LATEST_SQUAD'] = bowler_df['IN_LATEST_SQUAD'].map({'YES': 1, 'NO': 0})
    bowler_df = bowler_df[bowler_df['NO_OF_MATCHES_PLAYED']>=1]
    
    x = bowler_df[['INNINGS_BOWLED','WICKETS','BOWLING_AVERAGE','ECONOMY','BOWLING_STRIKE_RATE']].values
    y = bowler_df[['IN_LATEST_SQUAD']].values

    x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))
    
    x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.15, random_state=4)
    
    y_train = y_train.reshape(y_train.shape[0],)
    y_test = y_test.reshape(y_test.shape[0],)

    LR = LogisticRegression().fit(x_train,y_train)

    bowler_df = bowler_df[bowler_df['TEAM'] == team]
    bowler_df = bowler_df[['PLAYERS','NO_OF_MATCHES_PLAYED','INNINGS_BOWLED','WICKETS','BOWLING_AVERAGE','ECONOMY','BOWLING_STRIKE_RATE']]
    bowler_df = bowler_df.reset_index(drop=True)
        
    X_bowl = bowler_df[['INNINGS_BOWLED','WICKETS','BOWLING_AVERAGE','ECONOMY','BOWLING_STRIKE_RATE']].values
    X_bowl = X_bowl.astype('float64')
    X_bowl = preprocessing.StandardScaler().fit(X_bowl).transform(X_bowl.astype(float))
    
    final_bowl_predict = LR.predict_proba(X_bowl)
    final_bowl_predict_df = pd.DataFrame(final_bowl_predict,columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_bowl_predict_df = final_bowl_predict_df.reset_index(drop=True)
        
    final_bowl_predict_df = pd.concat([bowler_df, final_bowl_predict_df], axis=1, join='inner')

    final_bowl_predict_df = final_bowl_predict_df.drop(['PROBABILITY_OF_NOT_PLAYING'], axis=1)
    
    return final_bowl_predict_df

def all_round(team):
    
    all_rounder_options = ['All Rounder']    
    in_latest_squad = ['YES','NO']
    
    all_rounder_df = df[df['ROLE'].isin(all_rounder_options)]
    all_rounder_df = all_rounder_df[all_rounder_df['IN_LATEST_SQUAD'].isin(in_latest_squad)]
    all_rounder_df['IN_LATEST_SQUAD'] = all_rounder_df['IN_LATEST_SQUAD'].map({'YES': 1, 'NO': 0})
    all_rounder_df = all_rounder_df[all_rounder_df['NO_OF_MATCHES_PLAYED']>=1]
    
    x = all_rounder_df[['INNINGS_PLAYED_BATTING','RUNS','BATTING_AVG','BATTING_STRIKE_RATE','INNINGS_BOWLED','WICKETS','BOWLING_AVERAGE','ECONOMY','BOWLING_STRIKE_RATE']].values
    y = all_rounder_df[['IN_LATEST_SQUAD']].values

    x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))
    
    x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.15, random_state=4)
    
    y_train = y_train.reshape(y_train.shape[0],)
    y_test = y_test.reshape(y_test.shape[0],)

    LR = LogisticRegression().fit(x_train,y_train)
    
    all_rounder_df = all_rounder_df[all_rounder_df['TEAM'] == team]
    all_rounder_df = all_rounder_df[['PLAYERS','NO_OF_MATCHES_PLAYED','INNINGS_PLAYED_BATTING','RUNS','BATTING_AVG','BATTING_STRIKE_RATE','INNINGS_BOWLED','WICKETS','BOWLING_AVERAGE','ECONOMY','BOWLING_STRIKE_RATE']]
    all_rounder_df = all_rounder_df.reset_index(drop=True)

    X_all_round = all_rounder_df[['INNINGS_PLAYED_BATTING', 'RUNS', 'BATTING_AVG', 'BATTING_STRIKE_RATE', 'INNINGS_BOWLED', 'WICKETS','BOWLING_AVERAGE', 'ECONOMY', 'BOWLING_STRIKE_RATE']].values
    X_all_round = X_all_round.astype('float64')
    X_all_round = preprocessing.StandardScaler().fit(X_all_round).transform(X_all_round.astype(float))

    final_all_round_predict = LR.predict_proba(X_all_round)
    final_all_round_predict = pd.DataFrame(final_all_round_predict,columns=['PROBABILITY_OF_NOT_PLAYING', 'PROBABILITY_OF_PLAYING'])
    final_all_round_predict = final_all_round_predict.reset_index(drop=True)

    final_all_round_predict = pd.concat([all_rounder_df, final_all_round_predict], axis=1, join='inner')

    final_all_round_predict = final_all_round_predict.drop(['PROBABILITY_OF_NOT_PLAYING'], axis=1)

    return final_all_round_predict


#bat_df = bat('Gujurat Titans')
#bowl_df = bowl('Gujurat Titans')
#all_rounder_df = all_round('Gujurat Titans')