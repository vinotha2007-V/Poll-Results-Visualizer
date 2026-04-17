def poll_counts(df):
    return df['Option'].value_counts()

def satisfaction_avg(df):
    return df.groupby('Option')['Satisfaction'].mean()
