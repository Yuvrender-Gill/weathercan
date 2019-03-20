def stack_weather_data(station_name, start_year, start_month, end_year, end_month):
    df_lst = []
    df_all = pd.DataFrame([])
    for i in range(start_year, end_year + 1):
        for j in range(start_month, 13):
            if (i == end_year) & (j == (end_month+1)):
                 break
            df = pd.read_csv(str(station_name) + str(i) + str(j) + ".csv", index_col=[0], parse_dates=[0])
            df_all = df_all.append(df)
    df_all.to_csv(station_name+'_all' + '.csv')
    return df_all

if __name__ == "__main__":
    stack_weather_data('Toronto', 2003, 1, 2019, 12).head()
    stack_weather_data('Ottawa', 2003, 1, 2019, 12).head()
    stack_weather_data('ThunderBay', 2003, 1, 2019, 12).head()