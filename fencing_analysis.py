import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

def two_proportion_test(pool1_df, pool2_df):
    # Merge pool data based on First and Last names
    merged_df = pool1_df.merge(pool2_df, on=['First', 'Last'], suffixes=('_pool1', '_pool2'))

    # Calculate proportions for each fencer in each pool
    merged_df['proportion_pool1'] = merged_df['Victories_pool1'] / 6
    merged_df['proportion_pool2'] = merged_df['Victories_pool2'] / 6

    # Initialize z_score and p_value columns
    merged_df['z_score'] = 0
    merged_df['p_value'] = 0

    # Perform a 2-proportion test for each fencer
    for index, row in merged_df.iterrows():
        z_score, p_value = proportions_ztest(
            [row['Victories_pool1'], row['Victories_pool2']],
            [6, 6],
            alternative='two-sided'
        )
        merged_df.at[index, 'z_score'] = z_score
        merged_df.at[index, 'p_value'] = p_value

    return merged_df
