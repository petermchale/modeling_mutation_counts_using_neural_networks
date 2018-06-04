from synthetic_data import generate_counts
from model import train
from plot import plot_rates
from plot import plot_counts


def analyze(f, xs_max):
    data_df = generate_counts(f, xs_max=xs_max)
    data_df_headings = {'l_heading_list': ['length'],
                        'X_heading_list': ['x'],
                        'y_heading_list': ['counts']}
    log_df = train(data_df, **data_df_headings)
    plot_rates(f, data_df)
    plot_counts(data_df,
                y_heading_list=data_df_headings['y_heading_list'],
                hover_text_list=data_df_headings['X_heading_list'])
    return data_df, log_df
