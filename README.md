# fig2pen

```bash
pip uninstall fig2pen && pip install git+git://github.com/nicolaskruchten/fig2pen.git#egg=fig2pen
```

```python
from fig2pen import single, react_multi

single(fig) # strips out template
single(fig, template=True) # leave template alone

react_multi([fig_state1, fig_state2]) # strips out template
react_multi([fig_state1, fig_state2], template=True) # strips out template
```
