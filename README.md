# Interactive Demonstration of First Order RC Filters

This repo, contains two examples of RC filter networks, that you can play within your browser to see their [bode](https://en.wikipedia.org/wiki/Bode_plot) plot.

Detailed explanation of how the filters are working, and mathematical expressions, you can visit [here](https://www.electronics-tutorials.ws/filter/filter_2.html)


## Installing dependencies

Examples run using python3, you can download and install to your computer from [here](https://www.python.org). To install additional packages, make sure you have official python dependency manager pip. It usually comes with the install too. In addition to these you will need to install [bokeh](https://bokeh.org) and [numpy](https://numpy.org) to run the scripts

```bash
# In your terminal after installing python + pip

pip install numpy 
pip install bokeh
```

## Running the examples

Hopefully if you were able to install everything without problems, you can then run the examples as follows

```bash
# In your terminal after installing python + pip + bokeh + numpy

# pick one of ...
bokeh serve hpf.py # If you want to see high pass filter diagram 
bokeh serve lpf.py # If you want to see low pass filter diagram
```

After you run these you will see the following messages appear 

``` bash
bokeh serve lpf.py
2022-07-08 23:24:55,844 Starting Bokeh server version 2.4.3 (running on Tornado 6.1)
2022-07-08 23:24:55,846 User authentication hooks NOT provided (default user enabled)
2022-07-08 23:24:55,847 Bokeh app running at: http://localhost:5006/lpf
2022-07-08 23:24:55,847 Starting Bokeh server with process id: 49654
2022-07-08 23:24:57,544 WebSocket connection opened
2022-07-08 23:24:57,545 ServerConnection created
```

The line you're looking for is the line starts with "Bokeh app running at: ". Copy that adress and paste it into your browser, once you visit the page you'll see the diagrams in real time.

If you want to quit and try the other one, in the same terminal window, press Ctrl+C and enter the new command, don't close the terminal until you're done playing around, if you close the terminal, webpage will stop to work.