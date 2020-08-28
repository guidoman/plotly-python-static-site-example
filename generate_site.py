import os
import shutil

import plotly.express as px


def generate_site():
    try:
        os.makedirs('dist')
    except FileExistsError:
        pass
    shutil.copyfile('templates/index.html', 'dist/index.html')

    df = px.data.iris()

    create_plot_iframe(df, 'sepal_width', 'sepal_length', 'dist/sepal_plot.html',
                       'Iris dataset - sepal size scatter plot')
    create_plot_iframe(df, 'petal_width', 'petal_length', 'dist/petal_plot.html',
                       'Iris dataset - petal size scatter plot')


def create_plot_iframe(df, x_name, y_name, outpath, title):
    plot = px.scatter(data_frame=df, x=x_name, y=y_name, color='species', title=title)
    plot.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
    )
    plot.write_html(outpath,
                    full_html=False,
                    include_plotlyjs='cdn')


if __name__ == '__main__':
    generate_site()
