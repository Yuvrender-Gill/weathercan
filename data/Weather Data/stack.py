def stack_weather_data(station_name, start_year, start_month, end_year, end_month):
    df_lst = []
    for i in range(start_year, end_year):
        for j in range(start_year, 13):
#             if (i == end_year) & (j == (end_month+1)):
#                 break
            print(str(station_name) + str(i) + str(j) + ".csv")
            df = pd.read_csv(str(station_name) + str(i) + str(j) + ".csv", index_col=[0], parse_dates=[0])
            df = df.drop(columns=['Date/Time'])
            print(df)
            df_lst.append(df)
#     df1 = pd.concat(df_lst)
    return None

if __name__ == "__main__":
    print(stack_weather_data('Toronto', 2003, 1, 2019, 12).head())