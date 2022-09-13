import pandas as pd


loc = "../Datasets/"

raw_data_1 = pd.read_csv(loc + '2000-01.csv')
raw_data_2 = pd.read_csv(loc + '2001-02.csv')
raw_data_3 = pd.read_csv(loc + '2002-03.csv')
raw_data_4 = pd.read_csv(loc + '2003-04.csv')
raw_data_5 = pd.read_csv(loc + '2004-05.csv')
raw_data_6 = pd.read_csv(loc + '2005-06.csv')
raw_data_7 = pd.read_csv(loc + '2006-07.csv')
raw_data_8 = pd.read_csv(loc + '2007-08.csv')
raw_data_9 = pd.read_csv(loc + '2008-09.csv')
raw_data_10 = pd.read_csv(loc + '2009-10.csv')
raw_data_11 = pd.read_csv(loc + '2010-11.csv')
raw_data_12 = pd.read_csv(loc + '2011-12.csv')
raw_data_13 = pd.read_csv(loc + '2012-13.csv')
raw_data_14 = pd.read_csv(loc + '2013-14.csv')
raw_data_15 = pd.read_csv(loc + '2014-15.csv')
raw_data_16 = pd.read_csv(loc + '2015-16.csv')
raw_data_17 = pd.read_csv(loc + '2016-17.csv')
raw_data_18 = pd.read_csv(loc + '2017-18.csv')
raw_data_19 = pd.read_csv(loc + '2018-19.csv')
raw_data_20 = pd.read_csv(loc + '2019-20.csv')
raw_data_21 = pd.read_csv(loc + '2020-21.csv')
raw_data_22 = pd.read_csv(loc + '2021-22.csv')

feature_list = ['HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR']

raw_data_1 = raw_data_1[feature_list]
raw_data_2 = raw_data_2[feature_list]
raw_data_3 = raw_data_3[feature_list]
raw_data_4 = raw_data_4[feature_list]
raw_data_5 = raw_data_5[feature_list]
raw_data_6 = raw_data_6[feature_list]
raw_data_7 = raw_data_7[feature_list]
raw_data_8 = raw_data_8[feature_list]
raw_data_9 = raw_data_9[feature_list]
raw_data_10 = raw_data_10[feature_list]
raw_data_11 = raw_data_11[feature_list]
raw_data_12 = raw_data_12[feature_list]
raw_data_13 = raw_data_13[feature_list]
raw_data_14 = raw_data_14[feature_list]
raw_data_15 = raw_data_15[feature_list]
raw_data_16 = raw_data_16[feature_list]
raw_data_17 = raw_data_17[feature_list]
raw_data_18 = raw_data_18[feature_list]
raw_data_19 = raw_data_19[feature_list]
raw_data_20 = raw_data_20[feature_list]
raw_data_21 = raw_data_21[feature_list]
raw_data_22 = raw_data_22[feature_list]

feature_list = ['HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR']
raw_data_22 = raw_data_22[feature_list]

columns_req = ['HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR']
playing_statistics_22 = raw_data_22[columns_req]

# 홈/원정 팀 골득실 전처리
# 슈팅 개수, 유효슈팅 개수 전처리

def get_goals_scored(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
#     print(teams)
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        HTGS = playing_stat.iloc[i]['FTHG']
        ATGS = playing_stat.iloc[i]['FTAG']
        teams[playing_stat.iloc[i].HomeTeam].append(HTGS)
        teams[playing_stat.iloc[i].AwayTeam].append(ATGS)
#     print(teams)
    
    match_round_len = ((len(playing_stat)+1) // 10) + 1
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    # 행이 팀이고 열이 라운드인 dataframe 생성하여 각 라운드별로 먹힌 골 수 넣기
    GoalsScored = pd.DataFrame(data=teams, index = [i for i in range(1,match_round_len)]).T
    GoalsScored[0] = 0    # 마지막(39라운드)에 0을 넣은 열 추가(???)
#     print(GoalsScored)
    
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsScored[i] = GoalsScored[i] + GoalsScored[i-1]

#     print(GoalsScored)
    return GoalsScored
    
    
def get_goals_conceded(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        ATGC = playing_stat.iloc[i]['FTHG']
        HTGC = playing_stat.iloc[i]['FTAG']
        teams[playing_stat.iloc[i].HomeTeam].append(HTGC)
        teams[playing_stat.iloc[i].AwayTeam].append(ATGC)
    
    match_round_len = ((len(playing_stat)+1) // 10) + 1
#     print(match_round_len)
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    # 행이 팀이고 열이 라운드인 dataframe 생성하여 각 라운드별로 먹힌 골 수 넣기
    GoalsConceded = pd.DataFrame(data=teams, index = [i for i in range(1,match_round_len)]).T
    GoalsConceded[0] = 0
    # Aggregate to get uptil that point
    for i in range(2,39):
        GoalsConceded[i] = GoalsConceded[i] + GoalsConceded[i-1]
        
#     print(GoalsConceded)
    return GoalsConceded


# def get_etc_stats(playing_stat):
    
# 슈팅 개수 전처리
def get_shoots(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
#     print(teams)
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        HS = playing_stat.iloc[i]['HS']
        AS = playing_stat.iloc[i]['AS']
        teams[playing_stat.iloc[i].HomeTeam].append(HS)
        teams[playing_stat.iloc[i].AwayTeam].append(AS)
#     print(teams)
    
    match_round_len = ((len(playing_stat)+1) // 10) + 1
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    # 행이 팀이고 열이 라운드인 dataframe 생성하여 각 라운드별로 먹힌 골 수 넣기
    Shoots = pd.DataFrame(data=teams, index = [i for i in range(1,match_round_len)]).T
    Shoots[0] = 0    # 마지막(39라운드)에 0을 넣은 열 추가(???)
    
    # Aggregate to get uptil that point
    for i in range(2,39):
        Shoots[i] = Shoots[i] + Shoots[i-1]

#     print(GoalsScored)
    return Shoots


# 유효 슈팅 개수 전처리
def get_shoots_on_target(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
#     print(teams)
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        HST = playing_stat.iloc[i]['HST']
        AST = playing_stat.iloc[i]['AST']
        teams[playing_stat.iloc[i].HomeTeam].append(HST)
        teams[playing_stat.iloc[i].AwayTeam].append(AST)
#     print(teams)
    
    match_round_len = ((len(playing_stat)+1) // 10) + 1
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    # 행이 팀이고 열이 라운드인 dataframe 생성하여 각 라운드별로 먹힌 골 수 넣기
    ShootsOnTarget = pd.DataFrame(data=teams, index = [i for i in range(1,match_round_len)]).T
    ShootsOnTarget[0] = 0    # 마지막(39라운드)에 0을 넣은 열 추가(???)
    
    # Aggregate to get uptil that point
    for i in range(2,39):
        ShootsOnTarget[i] = ShootsOnTarget[i] + ShootsOnTarget[i-1]

#     print(GoalsScored)
    return ShootsOnTarget


def get_gss(playing_stat):
    GC = get_goals_conceded(playing_stat)
    GS = get_goals_scored(playing_stat)
    S = get_shoots(playing_stat)
    SoT = get_shoots_on_target(playing_stat)

    
#     print(GC)

    j = 0
    HTGS = []    # 홈 팀 넣은 골
    ATGS = []    # 원정 팀 넣은 골
    HTGC = []    # 홈 팀 먹힌 골
    ATGC = []    # 원정 팀 먹힌 골
    HS = []      # 홈 팀 슈팅 개수
    AS = []      # 원정 팀 슈팅 개수
    HTSoT = []      # 홈 팀 슈팅 개수
    ATSoT = []      # 원정 팀 슈팅 개수

    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
        at = playing_stat.iloc[i].AwayTeam
        HTGS.append(GS.loc[ht][j])
        ATGS.append(GS.loc[at][j])
        HTGC.append(GC.loc[ht][j])
        ATGC.append(GC.loc[at][j])
        HS.append(S.loc[ht][j])
        AS.append(S.loc[at][j])
        HTSoT.append(SoT.loc[ht][j])
        ATSoT.append(SoT.loc[at][j])
        
        if ((i + 1)% 10) == 0:
            j = j + 1
    
    df_temp = pd.DataFrame()
    
    df_temp['HomeTeam'] = playing_stat['HomeTeam']
    df_temp['AwayTeam'] = playing_stat['AwayTeam']
    
    df_temp['HTGS'] = HTGS
    df_temp['ATGS'] = ATGS
    df_temp['HTGC'] = HTGC
    df_temp['ATGC'] = ATGC
    
    df_temp['HS'] = HS
    df_temp['AS'] = AS
    df_temp['HST'] = HTSoT
    df_temp['AST'] = ATSoT
    
#     print(playing_stat)
    
#     playing_stat.drop(['FTHG', 'FTAG'], axis=1, inplace=True)
    
    return df_temp
    
playing_statistics_22 = get_gss(raw_data_22)

## 각 경기마다 팀별 누적승점 전처리

def get_points(result):
    if result == 'W':
        return 3
    elif result == 'D':
        return 1
    else:
        return 0
    

def get_cuml_points(matchres):
    matchres_points = matchres.applymap(get_points)
    for i in range(2,39):
        matchres_points[i] = matchres_points[i] + matchres_points[i-1]
        
    matchres_points.insert(column =0, loc = 0, value = [0*i for i in range(20)])
    return matchres_points


def get_matchres(playing_stat):
    # Create a dictionary with team names as keys
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []

    # the value corresponding to keys is a list containing the match result
    for i in range(len(playing_stat)):
        if playing_stat.iloc[i].FTR == 'H':
            teams[playing_stat.iloc[i].HomeTeam].append('W')
            teams[playing_stat.iloc[i].AwayTeam].append('L')
        elif playing_stat.iloc[i].FTR == 'A':
            teams[playing_stat.iloc[i].AwayTeam].append('W')
            teams[playing_stat.iloc[i].HomeTeam].append('L')
        else:
            teams[playing_stat.iloc[i].AwayTeam].append('D')
            teams[playing_stat.iloc[i].HomeTeam].append('D')
    
#     print(teams)
    
    return pd.DataFrame(data=teams, index = [i for i in range(1,39)]).T

def get_agg_points(playing_stat):
#     print(playing_stat)
    matchres = get_matchres(playing_stat)       # 팀별 경기결과 전처리
#     print(matchres)
    cum_pts = get_cuml_points(matchres)         # 팀별 누적승점 전처리
#     print(cum_pts)

    # 각 경기마다 팀별 누적승점 전처리
    HTP = []
    ATP = []
    j = 0
    for i in range(380):
        ht = playing_stat.iloc[i].HomeTeam
#         print(ht)
        at = playing_stat.iloc[i].AwayTeam
        HTP.append(cum_pts.loc[ht][j])
        ATP.append(cum_pts.loc[at][j])

        if ((i + 1)% 10) == 0:
            j = j + 1
#     print(playing_stat)
    
    df_temp = pd.DataFrame()
    
    df_temp['HTP'] = HTP
    df_temp['ATP'] = ATP
    
    return df_temp

# Apply to each dataset
playing_statistics_22 = pd.concat([playing_statistics_22, get_agg_points(raw_data_22)], axis=1)

# 시즌별 데이터 concat
raw_data_list = [raw_data_1, raw_data_2, raw_data_3, raw_data_4, raw_data_5, raw_data_6, raw_data_7, raw_data_8, raw_data_9, \
                 raw_data_10, raw_data_11, raw_data_12, raw_data_13, raw_data_14, raw_data_15, raw_data_16, raw_data_17, raw_data_18, raw_data_19, raw_data_20, raw_data_21, raw_data_22]

raw_data_total = pd.concat(raw_data_list, ignore_index=True)

# HomeTeam 인코딩
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)

df_temp = raw_data_total['HomeTeam']
df_temp = df_temp.to_numpy()
df_temp = df_temp.reshape(-1, 1)
ohe.fit(df_temp)
onehot_temp = ohe.transform(df_temp)

onehot_temp_table_home = pd.DataFrame(onehot_temp)

# 인코딩 레이블명 변경
temp = raw_data_total['HomeTeam'].unique()
temp.sort()
temp = ['Home_'+i for i in temp]
onehot_temp_table_home.columns = temp

# AwayTeam 인코딩
ohe = OneHotEncoder(sparse=False)

df_temp = raw_data_total['AwayTeam']
df_temp = df_temp.to_numpy()
df_temp = df_temp.reshape(-1, 1)
ohe.fit(df_temp)
onehot_temp = ohe.transform(df_temp)

onehot_temp_table_away = pd.DataFrame(onehot_temp)

# 인코딩 레이블명 변경
temp = raw_data_total['AwayTeam'].unique()
temp.sort()
temp = ['Away_'+i for i in temp]
onehot_temp_table_away.columns = temp

# 팀명(문자열) 레이블 제거
playing_statistics_22 = playing_statistics_22.drop(['HomeTeam', 'AwayTeam'], axis=1)

# 인덱스 초기화
onehot_temp_table_home = onehot_temp_table_home.loc[len(onehot_temp_table_home)-10:].reset_index(drop=True)
onehot_temp_table_away = onehot_temp_table_away.loc[len(onehot_temp_table_away)-10:].reset_index(drop=True)
playing_statistics_22 = playing_statistics_22.loc[len(playing_statistics_22)-10:].reset_index(drop=True)

# 인코딩 데이터 합치기
raw_data_total_final = pd.concat([onehot_temp_table_home.loc[len(onehot_temp_table_home)-10:], onehot_temp_table_away.loc[len(onehot_temp_table_away)-10:], playing_statistics_22.loc[len(playing_statistics_22)-10:]], axis=1, ignore_index=True)

# X, Y 나누기
X_test = raw_data_total_final

# lstm 입력층에 맞게 reshape

import numpy as np
X_test = np.array(X_test).reshape(X_test.shape[0], X_test.shape[1], 1)

# 모델 불러오기
from keras.models import load_model
model = load_model('(0523)only02_550.h5')

yhat = model.predict(X_test)
predicted_json = np.round(yhat, 2)

raw_data_22.loc[370, 'HomeTeam']
test_team_list_home = []
test_team_list_away = []

for i in range(10):
    test_team_list_home.append(raw_data_22.loc[len(raw_data_22)-10+i, 'HomeTeam'])
    test_team_list_away.append(raw_data_22.loc[len(raw_data_22)-10+i, 'AwayTeam'])

import json

data = {
    "game_1" : {
        "HomeTeam" : str(test_team_list_home[0]),
        "AwayTeam" : str(test_team_list_away[0]),
        "Result" : {
            "Result_Home" : str(predicted_json[0][0]),
            "Result_Draw" : str(predicted_json[0][1]),
            "Result_Away" : str(predicted_json[0][2])
        }
    },
    "game_2" : {
        "HomeTeam" : str(test_team_list_home[1]),
        "AwayTeam" : str(test_team_list_away[1]),
        "Result" : {
            "Result_Home" : str(predicted_json[1][0]),
            "Result_Draw" : str(predicted_json[1][1]),
            "Result_Away" : str(predicted_json[1][2])
        }
    },
    "game_3" : {
        "HomeTeam" : str(test_team_list_home[2]),
        "AwayTeam" : str(test_team_list_away[2]),
        "Result" : {
            "Result_Home" : str(predicted_json[2][0]),
            "Result_Draw" : str(predicted_json[2][1]),
            "Result_Away" : str(predicted_json[2][2])
        }
    },
    "game_4" : {
        "HomeTeam" : str(test_team_list_home[3]),
        "AwayTeam" : str(test_team_list_away[3]),
        "Result" : {
            "Result_Home" : str(predicted_json[3][0]),
            "Result_Draw" : str(predicted_json[3][1]),
            "Result_Away" : str(predicted_json[3][2])
        }
    },
    "game_5" : {
        "HomeTeam" : str(test_team_list_home[4]),
        "AwayTeam" : str(test_team_list_away[5]),
        "Result" : {
            "Result_Home" : str(predicted_json[4][0]),
            "Result_Draw" : str(predicted_json[4][1]),
            "Result_Away" : str(predicted_json[4][2])
        }
    },
    "game_6" : {
        "HomeTeam" : str(test_team_list_home[5]),
        "AwayTeam" : str(test_team_list_away[5]),
        "Result" : {
            "Result_Home" : str(predicted_json[5][0]),
            "Result_Draw" : str(predicted_json[5][1]),
            "Result_Away" : str(predicted_json[5][2])
        }
    },
    "game_7" : {
        "HomeTeam" : str(test_team_list_home[6]),
        "AwayTeam" : str(test_team_list_away[6]),
        "Result" : {
            "Result_Home" : str(predicted_json[6][0]),
            "Result_Draw" : str(predicted_json[6][1]),
            "Result_Away" : str(predicted_json[6][2])
        }
    },
    "game_8" : {
        "HomeTeam" : str(test_team_list_home[7]),
        "AwayTeam" : str(test_team_list_away[7]),
        "Result" : {
            "Result_Home" : str(predicted_json[7][0]),
            "Result_Draw" : str(predicted_json[7][1]),
            "Result_Away" : str(predicted_json[7][2])
        }
    },
    "game_9" : {
        "HomeTeam" : str(test_team_list_home[8]),
        "AwayTeam" : str(test_team_list_away[8]),
        "Result" : {
            "Result_Home" : str(predicted_json[8][0]),
            "Result_Draw" : str(predicted_json[8][1]),
            "Result_Away" : str(predicted_json[8][2])
        }
    },
    "game_10" : {
        "HomeTeam" : str(test_team_list_home[9]),
        "AwayTeam" : str(test_team_list_away[9]),
        "Result" : {
            "Result_Home" : str(predicted_json[9][0]),
            "Result_Draw" : str(predicted_json[9][1]),
            "Result_Away" : str(predicted_json[9][2])
        }
    }
}

file_path = "test.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file)

print(data)