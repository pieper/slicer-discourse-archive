# Color module label size

**Topic ID**: 5335
**Date**: 2019-01-11
**URL**: https://discourse.slicer.org/t/color-module-label-size/5335

---

## Post #1 by @ghnguyen (2019-01-11 19:49 UTC)

<p>Hi I was trying to modify the size of the labels of a scalar bar and found that the “size” slider in the Color module does not have any effect on the actual size shown. The only way I could change the relative size of the labels was by changing the number of labels. Is there any way to do this without changing the number of labels, either through the UI or python scripts?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-01-11 22:44 UTC)

<p>What would you like to achieve?<br>
Do you mean you want to make the text smaller?<br>
What Slicer version do you use?</p>

---

## Post #3 by @ghnguyen (2019-01-11 23:33 UTC)

<p>Yes I would like to make the text smaller than it is right now when there is only a small number of labels. I’m using Slicer 4.10.</p>

---

## Post #4 by @lassoan (2019-01-13 13:53 UTC)

<p>In latest nightly version (that you download tomorrow or later) I’ve made the scalar bar resizable by click-and-drag of the border. If you make the bar wider and taller (and/or reduce the number of displayed labels) then the font will be automatically scaled to be larger.</p>

---
