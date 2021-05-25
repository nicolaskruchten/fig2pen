from IPython.core.display import HTML, display
import json


def single(fig, template=False):
    fig_json = json.loads(fig.to_json())
    if template == False:
        del fig_json["layout"]["template"]
    payload = dict(
        html='<div id="gd" style="width: 95vw; height: 95vh" />',
        js_external="https://cdn.plot.ly/plotly-latest.min.js",
        js="""Plotly.newPlot(
          document.getElementById("gd"),
          %s
        )"""
        % json.dumps(fig_json, indent=2),
    )
    display(
        HTML(
            """
    <form action="https://codepen.io/pen/define" method="POST" target="_blank">
      <input type="hidden" name="data" value='%s'>
      <input type="submit" value="Create New Pen with Prefilled Data">
    </form>
    <p>Reminder: clicking this button sends your entire figure, including data, over the internet to CodePen</p>
    """
            % json.dumps(payload)
        )
    )


def react_multi(figs, template=False):
    fig_json = [json.loads(fig.to_json()) for fig in figs]
    if template == False:
        for f in fig_json:
            del f["layout"]["template"]
    payload = dict(
        html="""
<div id="steps"></div>
<div id="gd"></div>
<pre id="code"></pre>
        """,
        js_external=[
            "https://cdn.plot.ly/plotly-latest.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js",
        ],
        js="""
var steps = [%s];

$("#steps").append(
  $.map(steps, function(s, i){
    var fig = JSON.stringify(s(), null, 2);
    return [
      $("<button>")
      .text("newPlot @ step "+ i)
      .on("click", function(){
        $("#code").text(fig);
        Plotly.newPlot("gd", s());
        }),
      $("<button>")
      .text("react @ step "+ i)
      .on("click", function(){
        $("#code").text(fig);
        Plotly.react("gd", s());
        }),
      $("<br>")
    ]
  })
)
    """
        % ",\n".join(
            "function(){ return %s; }" % json.dumps(f, indent=2) for f in fig_json
        ),
    )
    display(
        HTML(
            """
    <form action="https://codepen.io/pen/define" method="POST" target="_blank">
      <input type="hidden" name="data" value='%s'>
      <input type="submit" value="Create New Pen with Prefilled Data">
    </form>
    <p>Reminder: clicking this button sends your entire figure, including data, over the internet to CodePen</p>
    """
            % json.dumps(payload)
        )
    )
