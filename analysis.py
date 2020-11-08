import pandas as pd
# import vincent as vn
# import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# Data clean
def organize_data():
    # TODO: fix order... uses ASCII rn
    # Sort values by ascending income (makes visualization better)
    # zipcode_df.income = zipcode_df.income.asType(float)
    return zipcode_df.dropna().sort_values('income')


# Helper functions

def get_zips():
    return organize_data().loc[:, 'zip']


def get_income_ratio():
    return organize_data().loc[:, 'income_ratio']


def get_case_ratio():
    return organize_data().loc[:, 'case_rate_ratio']


def visualize_components():
    print("\n\t----- Independent values -----\n")
    print("\nZIP CODES: \n")
    print(get_zips())

    print("\nINCOME RATIO: \n")
    print(get_income_ratio())

    print("\nCASE RATIO: \n")
    print(get_case_ratio())

# Visualize stack plots: zip v. COVID-19 , income v. COVID-19
def visualize_graph(df):
    sns.set_palette('pastel')
    sns.set_style('whitegrid')
    # graph = sns.lmplot('income_ratio', 'case_rate', data=df, fit_reg=False)
    graph = sns.jointplot('income_ratio', 'case_rate', data=df, kind="reg", color='palegoldenrod')
    # graph = sns.jointplot('income_ratio', 'case_rate', data=df, kind="kde", space=0.2, color='aqua')


    plt.gcf().set_size_inches(9,6)
    # plt.title("San Diego County COVID-19 case rates by household income")
    plt.xlabel("Relative household income")
    plt.ylabel("COVID cases per 100,000")


    plt.show()


if __name__ == '__main__':
    # Load and read data
    zipcode_csv = pd.read_csv(r"data",
                              names=['zip', 'city', 'cases', 'case_rate', 'case_rate_ratio', 'income', 'income_ratio'])

    # Create data frame object
    zipcode_df = pd.DataFrame(zipcode_csv).iloc[1:].dropna()
    zipcode_df['income'] = zipcode_df['income'].astype(float)
    zipcode_df['case_rate'] = zipcode_df['case_rate'].astype(float)

    hi_covid_rate = zipcode_df[['income_ratio', 'case_rate']]  # remove rows with null values
    hi_covid_rate['income_ratio'] = pd.to_numeric(hi_covid_rate['income_ratio'], errors='coerce')

    # Helps column view when printing output (doesn't truncate as much!)
    pd.set_option('display.expand_frame_repr', False)

    print("------ Data frame values ------")
    print(hi_covid_rate)

    # # visualize component data from data csv:
    visualize_components()

    print(zipcode_df)
    visualize_graph(hi_covid_rate)

