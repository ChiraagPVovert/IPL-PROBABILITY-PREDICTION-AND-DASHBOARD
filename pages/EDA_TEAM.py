import pandas as pd

data = pd.read_csv('assets\\Team_Stats\\IPL_Matches_2008_2022.csv')

df1 = data.Team1.value_counts()
df1_dict = df1.to_dict()

df2 = data.Team2.value_counts()
df2_dict = df2.to_dict()

df_win = data.WinningTeam.value_counts()
df_win_dict = df_win.to_dict()

def win_percentage():

    df1 = pd.DataFrame.from_dict(df1_dict.items())
    df1.columns = ['TEAM', 'TOTAL_MATCHES']

    df2 = pd.DataFrame.from_dict(df2_dict.items())
    df2.columns = ['TEAM', 'TOTAL_MATCHES']

    df = pd.merge(df1, df2, on="TEAM")

    df['TOTAL_MATCHES'] = df['TOTAL_MATCHES_x'] + df['TOTAL_MATCHES_y']
    df = df.drop(['TOTAL_MATCHES_x', 'TOTAL_MATCHES_y'], axis=1)

    df3 = pd.DataFrame.from_dict(df_win_dict.items())
    df3.columns = ['TEAM', 'TOTAL_WINS']

    df = pd.merge(df, df3, on="TEAM")

    df['WIN-PERCENTAGE'] = (df['TOTAL_WINS'] / df['TOTAL_MATCHES']) * 100

    df = df.sort_values(by=['WIN-PERCENTAGE'], ascending=False)

    return df

def total_matches():
    df1 = pd.DataFrame.from_dict(df1_dict.items())
    df1.columns = ['TEAM', 'TOTAL_MATCHES']

    df2 = pd.DataFrame.from_dict(df2_dict.items())
    df2.columns = ['TEAM', 'TOTAL_MATCHES']

    df = pd.merge(df1, df2, on="TEAM")

    df['TOTAL_MATCHES'] = df['TOTAL_MATCHES_x'] + df['TOTAL_MATCHES_y']
    df = df.drop(['TOTAL_MATCHES_x', 'TOTAL_MATCHES_y'], axis=1)

    df3 = pd.DataFrame.from_dict(df_win_dict.items())
    df3.columns = ['TEAM', 'TOTAL_WINS']

    df = pd.merge(df, df3, on="TEAM")

    df['WIN-PERCENTAGE'] = (df['TOTAL_WINS'] / df['TOTAL_MATCHES']) * 100

    df = df.sort_values(by=['TOTAL_MATCHES'], ascending=False)

    return df

def total_finals_played():
    df1 = data.loc[data['MatchNumber'] == 'Final'].Team1.value_counts()
    df1_dict = df1.to_dict()

    df2 = data.loc[data['MatchNumber'] == 'Final'].Team2.value_counts()
    df2_dict = df2.to_dict()

    df1 = pd.DataFrame.from_dict(df1_dict.items())
    df1.columns = ['TEAM', 'TOTAL_FINALS_PLAYED']

    df2 = pd.DataFrame.from_dict(df2_dict.items())
    df2.columns = ['TEAM', 'TOTAL_FINALS_PLAYED']

    df = df1.append(df2)

    agg_functions = {'TOTAL_FINALS_PLAYED': 'sum'}
    df = df.groupby(df['TEAM']).aggregate(agg_functions)
    df.reset_index(inplace=True)
    df = df.sort_values(by=['TOTAL_FINALS_PLAYED'], ascending=False)

    return df

def total_finals_won():

    df1 = data.loc[data['MatchNumber'] == 'Final'].WinningTeam.value_counts()
    df1_dict = df1.to_dict()

    df1 = pd.DataFrame.from_dict(df1_dict.items())
    df1.columns = ['TEAM', 'TOTAL_FINALS_WON']

    return df1

#df = win_percentage()

#print(df)