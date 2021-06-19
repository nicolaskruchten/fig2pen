# fig2pen

## Installation

```bash
pip install -U fig2pen
```

## Usage

```python
import fig2pen

fig2pen.single(fig)
fig2pen.react_multi([fig_state1, fig_state2])

# default behaviour is to erase fig.layout.template
fig2pen.single(fig, template=True) # don't strip out layout.template

# default Plotly.js version is the same one as is built into active Plotly.py
fig2pen.single(fig, cdn_version="1.58.4") # use specific JS version
fig2pen.single(fig, branch="plotly.js_branch_name") # use specifc CircleCI artifact
```
