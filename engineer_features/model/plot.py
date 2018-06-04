import matplotlib.pyplot as plt
import numpy as np
import plotly


def format_fig(fig):
    fig.set_size_inches(10, 6)


def format_axis(a):
    label_fontsize = 20
    legend_fontsize = 18
    tick_fontsize = 16

    a.set_xlabel(a.get_xlabel(), fontsize=label_fontsize)
    a.set_ylabel(a.get_ylabel(), fontsize=label_fontsize)
    a.legend(fontsize=legend_fontsize)
    a.tick_params(labelsize=tick_fontsize)


def plot_rates(f, df):
    fig = plt.figure()
    format_fig(fig)
    ax = fig.add_subplot(111)
    x = np.linspace(df.x.min(), df.x.max())
    ax.plot(x, f(x), '-', label='true rate, f(x)')
    ax.plot(df[['x']].values, df[['h']].values, 'x', label='learned rate, h(x_i)')
    ax.set_xlabel('feature, x')
    ax.set_ylabel('rate')
    format_axis(ax)


def df_to_listOfStrings(df, cols, delimiter="<br>"):
    # cols is a list of strings describing the column headings
    # output: list of strings, each of the form, e.g., "col1: 2.3 \t col2: 3"
    return [delimiter.join("{}: {}".format(*t) for t in zip(cols, row)) for _, row in df[cols].iterrows()]


def plot_counts(df, y_heading_list, hover_text_list):

    plotly.offline.init_notebook_mode(connected=True)

    y_heading, = y_heading_list

    trace1 = plotly.graph_objs.Scattergl(
        x=df[y_heading],
        y=df['expected_counts'],
        mode='markers',
        marker=dict(
            size=10,
            line=dict(width=1.5)),
            text=df_to_listOfStrings(df, hover_text_list),
            hoverinfo='text')

    a = np.arange(df[y_heading].max())
    trace2 = plotly.graph_objs.Scattergl(x=a, y=a)

    # b = df[l_heading].max() * np.ones_like(a)
    # trace3 = plotly.graph_objs.Scattergl(x=a, y=b)

    data = [trace1, trace2]

    layout = dict(font=dict(size=16),
                  hovermode='closest',
                  xaxis=dict(title='observed counts, n', type='log'),
                  yaxis=dict(title='expected counts, l*h(x)', type='log'),
                  showlegend=False)

    fig = dict(data=data, layout=layout)
    plotly.offline.iplot(fig)
