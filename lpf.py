import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

# Set up data
N = 400
x = np.linspace(20, 48000, N)
y = np.zeros_like(x)

r = 4700
c = 47 * 10 ** -9

for index, freq in np.ndenumerate(x):
    xc = 1.0 / (2.0 * np.pi * freq * c)
    gain = xc / np.sqrt(r * r + xc * xc)
    y[index] = np.log(gain) * 20

source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(height=800, width=800, title="Passive R-C LPF Filter",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_axis_type="log")

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


# Set up widgets
resistance = Slider(title="resistance (ohms)", value=4700, start=50, end=120000, step=10)
capacitor = Slider(title="capacitance (nf)", value=4.7, start=1, end=470, step=0.1)


# Set up callbacks
def update_data(attrname, old, new):

    # Get the current slider values
    r = resistance.value
    c = float(capacitor.value) * 10 ** -9

    # Generate the new curve
    for index, freq in np.ndenumerate(x):
        xc = 1.0 / (2.0 * np.pi * freq * c)
        gain = xc / np.sqrt(r * r + xc * xc)
        y[index] = np.log(gain) * 20

    source.data = dict(x=x, y=y)

for w in [resistance, capacitor]:
    w.on_change('value', update_data)

# Set up layouts and add to document
inputs = column(resistance, capacitor)

curdoc().add_root(row(inputs, plot, width=1280))
curdoc().title = "Passive R-C Filter"