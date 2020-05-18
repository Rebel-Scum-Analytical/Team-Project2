import pandas as pd
def prep_data(df):

    # df = pd.read_csv(df, drop_first = True)
    print(df.head())
    X_text = df["Shrt_Desc"].values
    # X = df[['Length3', 'Height', 'Width']].values
    y = df[["Weight"]].values
    #  print("Values of X are: ", X[:5])
    return X, y