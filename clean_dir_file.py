import pandas as pd

def main():
    df =  pd.read_csv("./stations_dir/raw_directory.csv", skiprows=3)
    df.to_csv("./stations_dir/directory.csv", sep=',')

if __name__ == "__main__":
    main()

