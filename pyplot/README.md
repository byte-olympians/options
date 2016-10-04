
# MatPlotLib

MatPlotLib is a graphing library that is used to produce graphs in Python. `matplotlib.pyplot` is the module within matplotlib that you will use as the interface to send in commands to have the library draw all of your graphs. 
In order to use the library you would first need to install it (using the pip package manager) using the command
```
pip install matplotlib  
or
pip3 install matplotlib
```


Once its installed you need to import pyplot into your code like so

```
import matplotlib.pyplot as plt
```

## Example usage
What's listed below is a quick and dirty set of examples to help you get started with this graphing module.


### Simple line plot
The most basic usage is to draw a simple line graph, which you would do like so

```
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```
which will produce a simple line graph that looks like ![alt text](http://matplotlib.org/pyplots/pyplot_simple.hires.png)

### Plot function
Plot is the main function that will take in the array(s) of points that pyplot will use to plot as a graph within its internal data structures. This is a very versatile command that can be called in multiple different ways depending on the desired objective.
When plot is called with a single array, pyplot treats it as points on the y-axis and generates the x-axis automatically starting at 0 (this is how the graph above was created)

#### Specify both axes
`plt.plot([1,2,3,4][2,4,6,8])`
When called with two arrays, plot will assume the first array as the x-axis points and the second array as y-axis points.

#### Line formatting
`plt.plot([1,2,3,4], [2,4,6,8], ‘ro’]`
For every pair of x,y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type that should be plotted. The above line will plot the points as red circles. The default is ‘b-‘ which starts for blue solid line.
There are a whole set of formatting rules that you can look up under the documentation of the [plot](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot) command

#### Axes range
`plt.axis([0,6,0,20])`
The axis command is issued in the format x-min, x-max, y-min, y-max all as elements of an array. You would use this to size the output graph that pyplot plots.

#### Display the Graph
plt.show()
Ultimately to have it render the graph, you need to issue the final show() command (or in other words, call the show function)

#### Multiple Line Series
`plt.plot([1,2], [1,2], [2,3], [1,2], [4,5], [1,2])`
Plot can also accept multiple line series to be plotted on the same graph. Two or three parameters per line, either two arrays (representing x and y axis data) or three arrays (including line type: b-, ro) per line series.

You can make multiple calls to plot() to add multiple data series individually. This will give you greater control for adding details to each series.
```
plt.plot([1,2,3], [1,2,3], label=“line 1”)
plt.plot([1,2,3], [2,4,6], label=“line 2”)
plt.legend()
plt.show()
```
This will render a graph with both lines series along with a legend for each of them. 

#### Legends
`plt.legend()`
This function will cause the legends of your graph to be displayed once you call the plt.show() function. This call takes several parameters, the most useful of them being “loc” which takes in positional values for the placement of the legend.

---

`plt.legend(loc=0)`
Will find the best (empty space) on the graph to display the legend

---
`plt.legend(loc=1)  or plt.legend(loc=2)`
Will cause the legend to appear on the upper right (1) or upper left (2). There are a whole bunch of positional codes for the location of the legend that you can lookup here http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend

#### Setp
`plt.setp()`
Can be used to set properties of the lines that are rendered on the graph. These could be the line width, color etc. To get a list of settable line properties call
lines = plt.plot([1,2,3])
plt.setp(lines)

#### Text
`plt.text(1, 1, “Some arbitrary text”)`
Can be used to place arbitrary text at the coordinates (1,2) on the graph. This is useful if you want to annotate your graph with bits of text to make it more readable. You can take this further with the annotate function that will allow you to draw arrows (as pointers) to locations on the lines in your graph allowing you to make more specific/explicit annotations

#### Annotate
You can use the annotate command to place arrows and further annotate your graph by drawing the observers attention to specific points
`plt.annotate('Point of Interest', xy=(36, 45),xytext=(33, 35), arrowprops=dict(facecolor='black', shrink=0.05))`
This will place the text “Point of Interest” at the coordinates (33, 35) on the graph, and will draw an arrow from this text to the point (36, 45) on the line. You can style the arrow by providing attribute values to the arrowprops dictionary parameter

#### Line Labels
```
plt.xlabel('Samples')
plt.ylabel('Values')
plt.title('My Title')
```
xlabel, ylabel and title are some standard text shortcuts that you can use to place text as labels for the axes in your graph.

#### Putting it all together
Take a look at the sample code that includes the function calls listed above

```
x_axis = range(0, 10)
plt.plot(x_axis, [0,1,2,3,4,5,6,7,8,9], label='Line 1')
plt.plot(x_axis, [9,8,7,6,5,4,3,2,1,0], label='Line 2')
plt.plot(x_axis, [0,2,4,6,8,10,12,14,16,18], label='Line 3')
plt.legend(loc=0)
plt.xlabel('Samples')
plt.ylabel('Values')
plt.title('Sampling Results')
plt.annotate('Point of Interest', xy=(9,9), xytext=(6,9), arrowprops=dict(facecolor='black', shrink=0.5))
plt.show()
```
Will produce the following graph
![alt text](https://github.com/ByteAcademyCo/parttimefinance/blob/nikhil/pyplot/all_together.png)

### SubPlots
If you need to render multiple graphs you would do so using subplot. Subplot arranges multiple graphs in a grid, and you would provide specifics of each graph by identifying it using the subplot command

```
plt.subplot(2,1,1)
```
> The function takes in the following arguments
row_num: The number of rows in the grid of graphs. Here the value is 2
column_num: The number of columns in the grid of graphs. Value of 1 tells subplot to expect a 2x1 grid of graphs.
graph_num: Value 1, identifies the first graph in the grid.

This call instructs pyplot to render the graphs in a 2x1 grid and also identifies graph number 1 as the current one. So any further calls to plt.plot() would be reflected in graph number 1

Consider the following example

```
x_values = [0,1,2,3,4,5]
# Create a 2x1 grid of graphs and make the top graph active
plt.subplot(2,1,1)
# Draw a blue line graph in the first subplot
plt.plot(x_values, [0,1,2,3,4,5], ‘b-‘)

# Activate the bottom graph
plt.subplot(2,1,2)
# Draw a green line graph in the second subplot
plt.plot(x_values, [0,2,4,6,8,10], ‘g-)

# render the grid of graphs (both subplots)
plt.show()
```
There’s opportunity for much finer grained control in multiple graphs thats available using calls to subplots() and axes() that are out of scope for the introduction


## Other Graphs
Besides lines, you can have pyplot render several other graphical forms of data

### Histogram: `hist()`
`plt.hist([1,2,3,3,3,3,4,4,5,6,6,6,6], bins=6)`
This will render a histogram with 6 bins that shows the bucketed count of the values in each bin

### Pie Charts: `pie()`
`plt.pie([60, 30, 6, 4], labels=[“Sixty %”, “30 %”, “6 %”, “4 %”])`
This will generate a pie chart with 4 “Wedges” with each wedge labelled by the corresponding string in the second array. The pie command takes in the array of data points in the first array and generates each wedge using the formula (x/sum(x))

### Bar Graphs: `bar()`
`plt.bar([0,2,4,6,8], [25,32,48,37,35])`
This will generate a bar graph with 5 bars. Each bar will be placed on the x-axis at points 0, 2, 4, 6, 8. The bars will have heights 25, 32, 48, 37, 35
