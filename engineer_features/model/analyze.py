from synthetic_data import generate_counts
from neural_network import train
from plot import plot_rates
from plot import plot_counts


def analyze(f, xs_max):
    data_df = generate_counts(f, xs_max=xs_max)
    # data_df = data_df[data_df.length > 10]
    data_df_headings = {'l_heading_list': ['length'],
                        'X_heading_list': ['x'],
                        'y_heading_list': ['counts']}
    log_df = train(data_df, **data_df_headings)
    plot_rates(f, data_df)
    plot_counts(data_df, **data_df_headings)
    return data_df, log_df
