from IPython.core.display import HTML, display
import json


def get_js_url(branch, cdn_version):
    if branch is None:
        if cdn_version is None:
            from plotly.offline import get_plotlyjs_version

            cdn_version = get_plotlyjs_version()
        return "https://cdn.plot.ly/plotly-%s.min.js" % cdn_version
    import requests

    builds = requests.get(
        "https://circleci.com/api/v1.1/project/github/plotly/"
        + "plotly.js/tree/%s?limit=50&filter=completed" % branch
    ).json()
    build_num = [
        b for b in builds if b["build_parameters"]["CIRCLE_JOB"] == "publish-dist"
    ][0]["build_num"]
    return (
        "https://%d-45646037-gh.circle-artifacts.com/0/dist/plotly.min.js" % build_num
    )


def single(fig, template=False, branch=None, cdn_version=None):
    fig_json = json.loads(fig.to_json())
    if not template:
        del fig_json["layout"]["template"]
    payload = dict(
        html='<div id="gd" style="width: 95vw; height: 95vh" />',
        js_external=get_js_url(branch, cdn_version),
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


def react_multi(figs, template=False, branch=None, cdn_version=None):
    fig_json = [json.loads(fig.to_json()) for fig in figs]
    if not template:
        for f in fig_json:
            del f["layout"]["template"]
    payload = dict(
        html="""
<div id="steps"></div>
<div id="gd"></div>
<pre id="code"></pre>
        """,
        js_external=[
            get_js_url(branch, cdn_version),
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
