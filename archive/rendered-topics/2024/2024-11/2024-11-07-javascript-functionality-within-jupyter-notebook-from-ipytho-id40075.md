# Javascript functionality within Jupyter notebook from IPython.display

**Topic ID**: 40075
**Date**: 2024-11-07
**URL**: https://discourse.slicer.org/t/javascript-functionality-within-jupyter-notebook-from-ipython-display/40075

---

## Post #1 by @Sharada (2024-11-07 22:10 UTC)

<p>Hello,</p>
<p>I have a process wherein consecutive cells need to be executed in a jupyter notebook that interacts with Slicer (using SlicerJupyter extension).</p>
<p>I basically have something like</p>
<p>from IPython.display import Javascript<br>
display(Javascript(“IPython.notebook.execute_cells_below()”))</p>
<p>This used to work perfectly in Slicer 4.11, but I am unable to replicate it in the newer 5.6.1 and 5.6.2 versions.</p>
<p>The error is “Javascript Error: display is not defined”</p>
<p>Does anyone have any insights on this? This is for a time sensitive project, so I would appreciate any help! Thank you in advance.</p>
<p>Best,<br>
Sharada</p>

---
