import pandas as pd

def main():
    df =  pd.read_csv("./stations_dir/raw_directory.csv", skiprows=3)
    df.to_csv("./stations_dir/directory.csv", sep=',')

    df1 = df[(df['HLY First Year'].notnull()) & (df['Province'] == 'ONTARIO') & (df['HLY First Year'] >= 2000)]
    df1.to_csv("./stations_dir/2000.csv", sep=',')


if __name__ == "__main__":
    main()

