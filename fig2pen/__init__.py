from IPython.core.display import HTML, display
import json

def single(fig):
    payload = dict(
        html = '<div id="gd" style="width: 95vw; height: 95vh" />',
        js_external = 'https://cdn.plot.ly/plotly-latest.min.js',
        js = '''Plotly.newPlot(
          document.getElementById("gd"),
          %s
        )''' % json.dumps(json.loads(fig.to_json()), indent=2)
    )
    display(HTML('''
    <form action="https://codepen.io/pen/define" method="POST" target="_blank">
      <input type="hidden" name="data" value='%s'>
      <input type="submit" value="Create New Pen with Prefilled Data">
    </form>
    <p>Reminder: clicking this button sends your entire figure, including data, over the internet to CodePen</p>
    ''' % json.dumps(payload)))
