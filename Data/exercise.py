import pandas as pd
import numpy as np
from tabulate import tabulate

dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6], 'c2': [7, 8, 9], 'c3': [10, 11, 12], 'c4': [13, 14, 15]}

df = pd.DataFrame(dict_data)

# print(type(df))
# print()
# print(df)

df2 = pd.DataFrame([[18, '남', '김천고'], [19, '여', '울산고']], index=['진현', '민지'], columns=['나이', '성별', '학교'])

# print(df2)
# print(df2.index)
# print(df2.columns)

# df2.rename(columns={'나이': '연령', '성별': '남녀', '학교': '소속'}, inplace=True)
# df2.rename(index={'진현': '학생1', '민지': '학생2'}, inplace=True)

# print(df2)

df2.drop('진현', axis=0, inplace=True)
# print(df2)

df2.drop(['나이', '학교'], axis=1, inplace=True)
# print(df2)

exam_data = {'수학': [100, 40, 70, 30], '영어': [50, 70, 90, 80], '생물': [50, 90, 70, 18], '도덕': [88, 68, 58, 77]}

df3 = pd.DataFrame(exam_data, index=['진현', '민지', '성철', '지산'])

# print(df3)
# print(df3.loc['진현'])
# print(df3.iloc[1])
# print(df3.loc['민지':])
# print(df3.loc[['진현', '지산']])
# print(df3.iloc[3:])
# print(df3.iloc[[2, 1]])
# print(df3.수학)
# print(df3['수학'])
# print(df3[['수학']])
# print(df3[['수학', '영어']])

exam_data = {'이름': ['진현', '민지', '성철', '지산'], '수학': [100, 40, 70, 30], '영어': [50, 70, 90, 80], '생물': [50, 90, 70, 18], '도덕': [88, 68, 58, 77]}

df4 = pd.DataFrame(exam_data)
df4['국어'] = 80

print(tabulate(df4, headers='keys', tablefmt='psql', showindex=True))
