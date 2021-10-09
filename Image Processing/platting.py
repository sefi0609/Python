from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource
#converting the data to date-time format
df['Start_str'] = df['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['End_str'] = df['End'].dt.strftime('%Y-%m-%d %H:%M:%S')
#creating a source for the graph
cds = ColumnDataSource(df)
#creating a figure and adjusting the graph
p = figure(x_axis_type = 'datetime',title = "Motion Graph")
p.sizing_mode = "stretch_both"
p.yaxis[0].ticker.desired_num_ticks = 1
#adding a hover tool
hover = HoverTool(tooltips = [('Start','@Start_str'),('End','@End_str')])
p.add_tools(hover)
#creating the graph
q = p.quad(top =1,bottom=0,left='Start',right='End',source=cds)
#saving the file and showing it
output_file('times.html')
show(p)