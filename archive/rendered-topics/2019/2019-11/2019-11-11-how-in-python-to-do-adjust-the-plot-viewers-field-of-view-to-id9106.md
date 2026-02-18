# How, in python, to do "Adjust the Plot Viewer's field of view to match the extent of the Plot axes"?

**Topic ID**: 9106
**Date**: 2019-11-11
**URL**: https://discourse.slicer.org/t/how-in-python-to-do-adjust-the-plot-viewers-field-of-view-to-match-the-extent-of-the-plot-axes/9106

---

## Post #1 by @aiden.zhu (2019-11-11 20:50 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.0<br>
Expected behavior: reset the focal of the quantitative view through Python<br>
Actual behavior:  click button</p>
<p>Hi all,<br>
I know the slice views, I may use: sliceWidget(“Red”).fitSliceToBackgrond() to do the reset focal view;<br>
I know the 3d-view, I may use: threeDView.resetFocalPoint(),</p>
<p>what’s the similar control function inside the quantitative view (as shown in the following image) ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee31accb0fb14c0994f66f4e394dee894457baa9.png" data-download-href="/uploads/short-url/xZa4674GIchSmSzEUE97n4FcGJH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee31accb0fb14c0994f66f4e394dee894457baa9_2_613x500.png" alt="image" data-base62-sha1="xZa4674GIchSmSzEUE97n4FcGJH" width="613" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee31accb0fb14c0994f66f4e394dee894457baa9_2_613x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee31accb0fb14c0994f66f4e394dee894457baa9_2_919x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee31accb0fb14c0994f66f4e394dee894457baa9_2_1226x1000.png 2x" data-dominant-color="F8F8F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1561×1273 64.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot, Aiden</p>

---

## Post #2 by @lassoan (2019-11-12 00:19 UTC)

<p>Plot view axes can be reset to include the entire plot using <code>plotWidget.plotView().fitToContent()</code> (see <a href="https://apidocs.slicer.org/master/classqMRMLPlotView.html#a4238275e4e9114eeeb2f7ae14bacb11b">documentation</a>).</p>

---

## Post #3 by @aiden.zhu (2019-11-12 13:34 UTC)

<p>Thanks a lot, Andras!<br>
Aiden</p>

---
