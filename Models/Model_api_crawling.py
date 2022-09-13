import pandas as pd
import numpy as np

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

# xG 크롤링 데이터 불러오기
loc_xG = "../crawling/xG_final/"

raw_data_15 = pd.read_csv(loc_xG + '2014-2015_final.csv')
raw_data_16 = pd.read_csv(loc_xG + '2015-2016_final.csv')
raw_data_17 = pd.read_csv(loc_xG + '2016-2017_final.csv')
raw_data_18 = pd.read_csv(loc_xG + '2017-2018_final.csv')
raw_data_19 = pd.read_csv(loc_xG + '2018-2019_final.csv')
raw_data_20 = pd.read_csv(loc_xG + '2019-2020_final.csv')
raw_data_21 = pd.read_csv(loc_xG + '2020-2021_final.csv')
raw_data_22 = pd.read_csv(loc_xG + '2021-2022_final.csv')


# xG column 추가
xG_columns = ['Home_xG', 'Home_xA', 'Home_xPTS', 'Away_xG', 'Away_xA', 'Away_xPTS']

def add_columns(df, columns):
    for i in columns:
        df[i] = np.NaN
    return df

xG_data_1 = add_columns(raw_data_1, xG_columns)
xG_data_2 = add_columns(raw_data_2, xG_columns)
xG_data_3 = add_columns(raw_data_3, xG_columns)
xG_data_4 = add_columns(raw_data_4, xG_columns)
xG_data_5 = add_columns(raw_data_5, xG_columns)
xG_data_6 = add_columns(raw_data_6, xG_columns)
xG_data_7 = add_columns(raw_data_7, xG_columns)
xG_data_8 = add_columns(raw_data_8, xG_columns)
xG_data_9 = add_columns(raw_data_9, xG_columns)
xG_data_10 = add_columns(raw_data_10, xG_columns)
xG_data_11 = add_columns(raw_data_11, xG_columns)
xG_data_12 = add_columns(raw_data_12, xG_columns)
xG_data_13 = add_columns(raw_data_13, xG_columns)
xG_data_14 = add_columns(raw_data_14, xG_columns)


feature_list = ['HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR']
feature_list_xG = ['HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR', 'Home_xG', 'Home_xA', 'Home_xPTS', 'Away_xG', 'Away_xA', 'Away_xPTS']

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
raw_data_15 = raw_data_15[feature_list_xG]
raw_data_16 = raw_data_16[feature_list_xG]
raw_data_17 = raw_data_17[feature_list_xG]
raw_data_18 = raw_data_18[feature_list_xG]
raw_data_19 = raw_data_19[feature_list_xG]
raw_data_20 = raw_data_20[feature_list_xG]
raw_data_21 = raw_data_21[feature_list_xG]
raw_data_22 = raw_data_22[feature_list_xG]


# 필요한 column 추출
columns_req = ['HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR', 'Home_xG', 'Home_xA', 'Home_xPTS', 'Away_xG', 'Away_xA', 'Away_xPTS']

playing_statistics_1 = xG_data_1[columns_req]                      
playing_statistics_2 = xG_data_2[columns_req]
playing_statistics_3 = xG_data_3[columns_req]
playing_statistics_4 = xG_data_4[columns_req]
playing_statistics_5 = xG_data_5[columns_req]
playing_statistics_6 = xG_data_6[columns_req]
playing_statistics_7 = xG_data_7[columns_req]
playing_statistics_8 = xG_data_8[columns_req]
playing_statistics_9 = xG_data_9[columns_req]
playing_statistics_10 = xG_data_10[columns_req]
playing_statistics_11 = xG_data_11[columns_req]   
playing_statistics_12 = xG_data_12[columns_req]
playing_statistics_13 = xG_data_13[columns_req]
playing_statistics_14 = xG_data_14[columns_req]
playing_statistics_15 = raw_data_15[columns_req]
playing_statistics_16 = raw_data_16[columns_req]
playing_statistics_17 = raw_data_17[columns_req]
playing_statistics_18 = raw_data_18[columns_req]
playing_statistics_19 = raw_data_19[columns_req]
playing_statistics_20 = raw_data_20[columns_req]
playing_statistics_21 = raw_data_21[columns_req]
playing_statistics_22 = raw_data_22[columns_req]


# 경기 결과(승무패) 전처리
def transformResult(row):
    if(row.FTR == 'H'):
        return -1
    elif(row.FTR == 'A'):
        return 1
    else:
        return 0

def add_match_result(playing_stat, raw_data):
    playing_stat["Result"] = raw_data.apply(lambda row: transformResult(row),axis=1)
    return playing_stat

playing_statistics_22 = add_match_result(playing_statistics_22, raw_data_22)


# 결과 원-핫 인코딩
from sklearn.preprocessing import OneHotEncoder

def result_onehotencoder(playing_stat):
    ohe = OneHotEncoder(sparse=False)
    
    df_temp = playing_stat['Result']
    df_temp = df_temp.to_numpy()
    df_temp = df_temp.reshape(-1, 1)

    ohe.fit(df_temp)
    onehot_temp = ohe.transform(df_temp)
    
#     print(df_temp)
#     print(onehot_temp)
    onehot_temp_table = pd.DataFrame(onehot_temp)
    onehot_temp_table.columns=['Home', 'draw', 'Away']
    
    playing_stat = pd.concat([playing_stat, onehot_temp_table], axis=1)
#     print(playing_stat)
    playing_stat = playing_stat.drop(['Result'], axis=1)
    playing_stat = playing_stat.drop(['FTR'], axis=1)
    
    return playing_stat

playing_statistics_22 = result_onehotencoder(playing_statistics_22)


# 데이터 합치기
df_total_list = [playing_statistics_1, playing_statistics_2, playing_statistics_3, playing_statistics_4,  playing_statistics_5, playing_statistics_6, playing_statistics_7, playing_statistics_8, playing_statistics_9, playing_statistics_10, playing_statistics_11, playing_statistics_12, playing_statistics_13, playing_statistics_14, playing_statistics_15, playing_statistics_16,playing_statistics_17, playing_statistics_18, playing_statistics_19, playing_statistics_20, playing_statistics_21, playing_statistics_22]

playing_statistics_total = pd.concat(df_total_list)


## 원-핫 인코딩
# HomeTeam 인코딩

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse=False)

df_temp = playing_statistics_total['HomeTeam']
df_temp = df_temp.to_numpy()
df_temp = df_temp.reshape(-1, 1)
ohe.fit(df_temp)
onehot_temp = ohe.transform(df_temp)

onehot_temp_table_home = pd.DataFrame(onehot_temp)

# 인코딩 레이블명 변경
temp = playing_statistics_total['HomeTeam'].unique()
temp.sort()
temp = ['Home_'+i for i in temp]
onehot_temp_table_home.columns = temp

# AwayTeam 인코딩
ohe = OneHotEncoder(sparse=False)

df_temp = playing_statistics_total['AwayTeam']
df_temp = df_temp.to_numpy()
df_temp = df_temp.reshape(-1, 1)
ohe.fit(df_temp)
onehot_temp = ohe.transform(df_temp)

onehot_temp_table_away = pd.DataFrame(onehot_temp)

# 인코딩 레이블명 변경
temp = playing_statistics_total['AwayTeam'].unique()
temp.sort()
temp = ['Away_'+i for i in temp]
onehot_temp_table_away.columns = temp


# 인덱스 초기화
playing_statistics_total = playing_statistics_total.reset_index()


# 인코딩 데이터 합치기
playing_statistics_total_final = pd.concat([onehot_temp_table_home, onehot_temp_table_away, playing_statistics_total], axis=1)

# 팀명(문자열) 레이블 제거
playing_statistics_total_final = playing_statistics_total_final.drop(['HomeTeam', 'AwayTeam'], axis=1)

playing_statistics_total_final


# 마지막 시즌만 떼어내기
season_index = 380
playing_statistics_22 = playing_statistics_total_final[season_index*21:]


# 인덱스 초기화
playing_statistics_22 = playing_statistics_22.reset_index()


## 팀명(HomeTeam, AwayTeam) 붙이기
playing_statistics_22 = pd.concat([playing_statistics_22, raw_data_22[['HomeTeam', 'AwayTeam']]], axis=1)


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

def get_xG(playing_stat):
    
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
#     print(teams)
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        temp_Home = playing_stat.iloc[i]['Home_xG']
        temp_Away = playing_stat.iloc[i]['Away_xG']
        teams[playing_stat.iloc[i].HomeTeam].append(temp_Home)
        teams[playing_stat.iloc[i].AwayTeam].append(temp_Away)
#     print(teams)
    
    match_round_len = ((len(playing_stat)+1) // 10) + 1
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    # 행이 팀이고 열이 라운드인 dataframe 생성하여 각 라운드별로 먹힌 골 수 넣기
    xG = pd.DataFrame(data=teams, index = [i for i in range(1,match_round_len)]).T
    xG[0] = 0    # 마지막(39라운드)에 0을 넣은 열 추가(???)
    
    # Aggregate to get uptil that point
    for i in range(2,39):
        xG[i] = xG[i] + xG[i-1]
        
    return xG


def get_xA(playing_stat):
    
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
#     print(teams)
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        temp_Home = playing_stat.iloc[i]['Home_xA']
        temp_Away = playing_stat.iloc[i]['Away_xA']
        teams[playing_stat.iloc[i].HomeTeam].append(temp_Home)
        teams[playing_stat.iloc[i].AwayTeam].append(temp_Away)
#     print(teams)
    
    match_round_len = ((len(playing_stat)+1) // 10) + 1
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    # 행이 팀이고 열이 라운드인 dataframe 생성하여 각 라운드별로 먹힌 골 수 넣기
    xA = pd.DataFrame(data=teams, index = [i for i in range(1,match_round_len)]).T
    xA[0] = 0    # 마지막(39라운드)에 0을 넣은 열 추가(???)
    
    # Aggregate to get uptil that point
    for i in range(2,39):
        xA[i] = xA[i] + xA[i-1]
        
    return xA


def get_xPTS(playing_stat):
    
    teams = {}
    for i in playing_stat.groupby('HomeTeam').mean().T.columns:
        teams[i] = []
#     print(teams)
    
    # the value corresponding to keys is a list containing the match location.
    for i in range(len(playing_stat)):
        temp_Home = playing_stat.iloc[i]['Home_xPTS']
        temp_Away = playing_stat.iloc[i]['Away_xPTS']
        teams[playing_stat.iloc[i].HomeTeam].append(temp_Home)
        teams[playing_stat.iloc[i].AwayTeam].append(temp_Away)
#     print(teams)
    
    match_round_len = ((len(playing_stat)+1) // 10) + 1
    # Create a dataframe for goals scored where rows are teams and cols are matchweek.
    # 행이 팀이고 열이 라운드인 dataframe 생성하여 각 라운드별로 먹힌 골 수 넣기
    xPTS = pd.DataFrame(data=teams, index = [i for i in range(1,match_round_len)]).T
    xPTS[0] = 0    # 마지막(39라운드)에 0을 넣은 열 추가(???)
    
    # Aggregate to get uptil that point
    for i in range(2,39):
        xPTS[i] = xPTS[i] + xPTS[i-1]
        
    return xPTS




# 'Home_xG', 'Home_xA', 'Home_xPTS', 'Away_xPTS',
def get_gss(playing_stat):
    GC = get_goals_conceded(playing_stat)
    GS = get_goals_scored(playing_stat)
    S = get_shoots(playing_stat)
    SoT = get_shoots_on_target(playing_stat)
    xG = get_xG(playing_stat)
    xA = get_xA(playing_stat)
    xPTS = get_xPTS(playing_stat)
    
    
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
    Home_xG = []
    Away_xG = []
    Home_xA = []
    Away_xA = []
    Home_xPTS = []
    Away_xPTS = []

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
        Home_xG.append(xG.loc[ht][j])
        Away_xG.append(xG.loc[at][j])
        Home_xA.append(xA.loc[ht][j])
        Away_xA.append(xA.loc[at][j])
        Home_xPTS.append(xPTS.loc[ht][j])
        Away_xPTS.append(xPTS.loc[at][j])
        
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
    
    df_temp['Home_xG'] = Home_xG
    df_temp['Away_xG'] = Away_xG
    df_temp['Home_xA'] = Home_xG
    df_temp['Away_xA'] = Away_xG
    df_temp['Home_xPTS'] = Home_xG
    df_temp['Away_xPTS'] = Away_xG
    
    columns = ['Home_Arsenal', 'Home_Aston Villa', 'Home_Birmingham', 'Home_Blackburn', 'Home_Blackpool', 'Home_Bolton', 'Home_Bournemouth', 'Home_Bradford', 'Home_Brentford', 'Home_Brighton', 'Home_Burnley', 'Home_Cardiff', 'Home_Charlton', 'Home_Chelsea', 'Home_Coventry', 'Home_Crystal Palace', 'Home_Derby', 'Home_Everton', 'Home_Fulham', 'Home_Huddersfield', 'Home_Hull', 'Home_Ipswich', 'Home_Leeds', 'Home_Leicester', 'Home_Liverpool', 'Home_Man City', 'Home_Man United', 'Home_Middlesboro', 'Home_Middlesbrough', 'Home_Newcastle', 'Home_Norwich', 'Home_Portsmouth', 'Home_QPR', 'Home_Reading', 'Home_Sheffield United', 'Home_Southampton', 'Home_Stoke', 'Home_Sunderland', 'Home_Swansea', 'Home_Tottenham', 'Home_Watford', 'Home_West Brom', 'Home_West Ham', 'Home_Wigan', 'Home_Wolves', 'Away_Arsenal', 'Away_Aston Villa', 'Away_Birmingham', 'Away_Blackburn', 'Away_Blackpool', 'Away_Bolton', 'Away_Bournemouth', 'Away_Bradford', 'Away_Brentford', 'Away_Brighton', 'Away_Burnley', 'Away_Cardiff', 'Away_Charlton', 'Away_Chelsea', 'Away_Coventry', 'Away_Crystal Palace', 'Away_Derby', 'Away_Everton', 'Away_Fulham', 'Away_Huddersfield', 'Away_Hull', 'Away_Ipswich', 'Away_Leeds', 'Away_Leicester', 'Away_Liverpool', 'Away_Man City', 'Away_Man United', 'Away_Middlesboro', 'Away_Middlesbrough', 'Away_Newcastle', 'Away_Norwich', 'Away_Portsmouth', 'Away_QPR', 'Away_Reading', 'Away_Sheffield United', 'Away_Southampton', 'Away_Stoke', 'Away_Sunderland', 'Away_Swansea', 'Away_Tottenham', 'Away_Watford', 'Away_West Brom', 'Away_West Ham', 'Away_Wigan', 'Away_Wolves', 'Home', 'draw', 'Away']
    df_temp = pd.concat([df_temp, playing_stat[columns]], axis=1)
    
#     print(playing_stat)
    
#     playing_stat.drop(['FTHG', 'FTAG'], axis=1, inplace=True)
    
    return df_temp
    
playing_statistics_22 = get_gss(playing_statistics_22)


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
    
#     playing_stat['HTP'] = HTP
#     playing_stat['ATP'] = ATP
    
#     print(playing_stat)
    
    return df_temp

# Apply to each dataset
playing_statistics_22 = pd.concat([playing_statistics_22, get_agg_points(raw_data_22)], axis=1)


# HomeTeam, AwayTeam 제거
playing_statistics_22 = playing_statistics_22.drop(['HomeTeam', 'AwayTeam', 'Away_xA', 'Away_xG'], axis=1)


# X, y 나누기
X_test = pd.concat([playing_statistics_22.loc[:, "HTGS":"Away_Wolves"], playing_statistics_22.loc[:, "HTP":"ATP"]], axis=1)
y_test = playing_statistics_22.loc[:, "Home":"Away"]

X_test = X_test[370:].reset_index(drop = True)
y_test = y_test[370:].reset_index(drop = True)


# lstm 입력층에 맞게 reshape
import numpy as np
X_test = np.array(X_test).reshape(X_test.shape[0], X_test.shape[1], 1)

# 모델 불러오기
from keras.models import load_model
model = load_model('(0609)526_gru.h5')
yhat = model.predict(X_test)
predicted = yhat.argmax(axis=-1)
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

######### 그래프 파라미터
file_path = "test.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file)
    
## 각 팀별 라운드별 예측 경기결과 정리
# 해당 시즌 팀 생성
column = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

j = 0
for i in raw_data_22.groupby('HomeTeam').mean().T.columns:
    column[j] = i
    j = j + 1

## DataFrame 생성
df_teams = pd.DataFrame(index=column, columns=[i for i in range(1, 39)])


## 생성한 DataFrame 채우기 (경기별 얻은 승점)
import math

for i in range(len(raw_data_22)):
    for j in range(1, 39):
        if math.isnan(df_teams.loc[raw_data_22.loc[i, 'HomeTeam'], j]):
            if predicted[i] == 0:
                df_teams.loc[raw_data_22.loc[i, 'HomeTeam'], j] = 3
                df_teams.loc[raw_data_22.loc[i, 'AwayTeam'], j] = 0

            elif predicted[i] == 2:
                df_teams.loc[raw_data_22.loc[i, 'HomeTeam'], j] = 0
                df_teams.loc[raw_data_22.loc[i, 'AwayTeam'], j] = 3

            else:
                df_teams.loc[raw_data_22.loc[i, 'HomeTeam'], j] = 1
                df_teams.loc[raw_data_22.loc[i, 'AwayTeam'], j] = 1
        else:
            continue

            
## 팀별 승점 누적
for i in range(len(df_teams)):
    for j in range(df_teams.shape[1]-1):
        df_teams.iloc[i, j+1] = df_teams.iloc[i, j] + df_teams.iloc[i, j+1]
        

## 딕셔너리 생성
dict_teams = {}

for i in range(df_teams.shape[0]):
    dict_teams[df_teams.index[i]] = list(df_teams.iloc[i])

    
## json 파일 생성 (그래프 생성에 필요한 값)
file_path = "graph.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(dict_teams, file)