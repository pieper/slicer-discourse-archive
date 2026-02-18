# Closing python matplotlib window not possible

**Topic ID**: 10638
**Date**: 2020-03-11
**URL**: https://discourse.slicer.org/t/closing-python-matplotlib-window-not-possible/10638

---

## Post #1 by @rprueckl (2020-03-11 12:01 UTC)

<p>Hi, I create (for quick testing and prototyping) some matplotlib windows from my segmenteditor effect (in the callback of the apply button) like described here:</p><aside class="quote quote-modified" data-post="5" data-topic="7162">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/use-full-power-of-python-in-slicer/7162/5">Use full power of Python in Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve just tried interactive plotting using matplotlib and it works fine for me on Windows. I just had to switch to WXAgg backend. 
Setup: 
pip_install("matplotlib wxPython")

Example interactive plot using matplotlib: 
# Get a volume from SampleData and compute its histogram
import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

# Set matplotlib to use WXAgg backend
import matplotlib
matplotl…
  </blockquote>
</aside>

<p>Unfortunately, it is not possible to close the window after use. Any ideas why this happens? Thanks.</p>

---

## Post #2 by @lassoan (2020-03-11 12:37 UTC)

<p>You can find various ways of plotting using matplotlib here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Using_matplotlib">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Using_matplotlib</a> (including rendering in a static qt window, which can be surely closed without problems).</p>

---
