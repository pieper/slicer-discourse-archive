---
topic_id: 12236
title: "Slicer 4 11 Closes After Closing The Figure Window For Matpl"
date: 2020-06-26
url: https://discourse.slicer.org/t/12236
---

# Slicer 4.11 closes after closing the Figure Window for matplotlib

**Topic ID**: 12236
**Date**: 2020-06-26
**URL**: https://discourse.slicer.org/t/slicer-4-11-closes-after-closing-the-figure-window-for-matplotlib/12236

---

## Post #1 by @siaeleni (2020-06-26 17:10 UTC)

<p>Hi all,</p>
<p>I work on the recent 4.11 (06.24.2020) and Slicer closes right after I close the window from matplotlib.<br>
For your convenience I use that piece of code in Python Interactor:</p>
<pre><code>from matplotlib import pyplot as plt
fig, axs = plt.subplots(1)
plt.show()
</code></pre>
<p>and a window opens. Right after I close it, Slicer closes as well.</p>
<p>Do you think it is a bug?</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @lassoan (2020-06-26 17:30 UTC)

<p>Could you post a complete example (including pip_install and setting of rendering backend)?</p>

---

## Post #3 by @pieper (2020-06-26 18:03 UTC)

<p>If you use matplotlib with a non-gui back end you can save to png and view it with vtk.</p>
<p>There’s an old example here from slicer3, but the same idea should work with the current Slicer.</p>
<p><a href="https://www.slicer.org/wiki/Slicer3:Python#Matplotlib_plotting_functionality" class="onebox" target="_blank">https://www.slicer.org/wiki/Slicer3:Python#Matplotlib_plotting_functionality</a></p>

---

## Post #4 by @siaeleni (2020-06-26 18:10 UTC)

<p>The following steps are:</p>
<pre><code>#pip_install('matplotlib')
#pip_install("matplotlib wxPython")

import matplotlib
matplotlib.use('WXAgg')
from matplotlib import pyplot as plt
fig, axs = plt.subplots(1)
plt.show()
</code></pre>
<p>and still have the same issue, I re-installed the .exe file but still the same issue.</p>
<p>Note: I use the same sample code at 4.11 (3.10.2020) with no issue.</p>

---

## Post #5 by @lassoan (2020-06-26 19:33 UTC)

<p>For static plots, you can use “Agg” backend. It still works well - see example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Non-interactive_plot">here</a>.</p>
<p>Using matplotlib for interactive plots in a GUI application is very unclear, so I would not recommend doing it. Instead I would recommend using <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Slicer_plots_displayed_in_view_layout">VTK plots</a>, as they are faster and they integrate much nicer into 3D Slicer GUI and it allows you to directly interact with data stored in the scene.</p>
<p>If for some reason you want to still try to use matplotlib for interactive rendering then one workaround is to show the plot using <code>plt.show(block=False)</code>, hide the close button on the figure image somehow (to make sure users don’t accidentally push it) and use <code>plt.close()</code> to cleanly close the plot. You could also try other matplotlib rendering backends (such as qt4 or qt5).</p>
<p>What would you like to plot interactively?</p>

---

## Post #6 by @siaeleni (2020-06-27 15:40 UTC)

<p>The only interactive functionality I want for now to have is the zoom in and show the coordinates once the cursor hovers the points. Maybe later to be able to show and hide some graphs at the same figure. Thus, I don’t think that png photos would give me that functionality.</p>
<p>I am wondering why at a latest version was working fine (4.11 03.10.2020), Do you think it is related to Slicer or matplotlib?</p>

---
