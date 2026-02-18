# Surface to surface distance

**Topic ID**: 20672
**Date**: 2021-11-18
**URL**: https://discourse.slicer.org/t/surface-to-surface-distance/20672

---

## Post #1 by @archamb4 (2021-11-18 01:05 UTC)

<p>Hello,</p>
<p>I am searching for guidance on using ParaView or a similar software as done in a research paper. I attached the figures from the paper. I want to use point cloud analysis to calculate linear deviation from a scanned cut surface to a plane. Does anyone have ideas of how to do this? I think that it is Distance to polydata in Paraview but I do not know how to do that. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/220d9ab5459b2a344c29d6ba77d1bde98e39d017.jpeg" data-download-href="/uploads/short-url/4RfnD53nyqMoVNaueERwR09TafR.jpeg?dl=1" title="Screen Shot 2021-11-16 at 12.16.05 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/220d9ab5459b2a344c29d6ba77d1bde98e39d017_2_264x500.jpeg" alt="Screen Shot 2021-11-16 at 12.16.05 PM" data-base62-sha1="4RfnD53nyqMoVNaueERwR09TafR" width="264" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/220d9ab5459b2a344c29d6ba77d1bde98e39d017_2_264x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/220d9ab5459b2a344c29d6ba77d1bde98e39d017_2_396x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/220d9ab5459b2a344c29d6ba77d1bde98e39d017_2_528x1000.jpeg 2x" data-dominant-color="5B5C58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-11-16 at 12.16.05 PM</span><span class="informations">824×1556 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you!</p>

---

## Post #2 by @jcfr (2021-11-18 01:08 UTC)

<p>For convenience (data from the <a href="https://discourse.paraview.org/t/point-cloud-analysis-help/8422">original post</a>) are also available below:</p>
<p><a class="attachment" href="https://discourse.paraview.org/uploads/short-url/zWJuQngxQBerLFMJcQGBTPziCal.stl">Cut 1-right.stl</a></p>
<p><a class="attachment" href="https://discourse.paraview.org/uploads/short-url/zotkjg57qs0thLfDrQcNgXuLfvQ.stl">Post Op.stl</a></p>

---

## Post #3 by @lassoan (2021-11-18 01:51 UTC)

<p>You can use ModelToModelDistance extension to compute the distances of bone surface points from the cutting plane:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56622bb0da853859478066b565de984230898027.png" data-download-href="/uploads/short-url/ckbojoJx4gJMEuverGFHJgP8W6r.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56622bb0da853859478066b565de984230898027_2_528x500.png" alt="image" data-base62-sha1="ckbojoJx4gJMEuverGFHJgP8W6r" width="528" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56622bb0da853859478066b565de984230898027_2_528x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56622bb0da853859478066b565de984230898027_2_792x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56622bb0da853859478066b565de984230898027.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">924×874 41.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After this you can copy-paste this code snippet into the Python console to get the distance distribution as a histogram:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = getNode("VTK Output File")
modelPointValues = modelNode.GetPolyData().GetPointData().GetArray("Signed")
import numpy as np
histogram = np.histogram(modelPointValues, bins=50, range=[-2.0, 2.0])
chartNode = slicer.util.plot(histogram, xColumnIndex = 1)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2919c3a942f014865eef947e9eae705b741addcc.png" data-download-href="/uploads/short-url/5RAM78nKWeMAGwV05EieVSIikIA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2919c3a942f014865eef947e9eae705b741addcc_2_690x420.png" alt="image" data-base62-sha1="5RAM78nKWeMAGwV05EieVSIikIA" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2919c3a942f014865eef947e9eae705b741addcc_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2919c3a942f014865eef947e9eae705b741addcc_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2919c3a942f014865eef947e9eae705b741addcc_2_1380x840.png 2x" data-dominant-color="E1E3EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1373 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jcfr (2021-11-18 01:58 UTC)

<blockquote>
<p>ModelToModelDistance</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I completely missed the <code>ModelToModelDistance</code> extension as it did not appear on linux in the extension manager and I ended up using a similar module  in OsteotomyPlanner extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e58085024a4e7e425f31b19f31201a437eb7af5c.png" data-download-href="/uploads/short-url/wKgGWtXjS5O3yowaNzHXBtQZmva.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58085024a4e7e425f31b19f31201a437eb7af5c_2_517x232.png" alt="image" data-base62-sha1="wKgGWtXjS5O3yowaNzHXBtQZmva" width="517" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58085024a4e7e425f31b19f31201a437eb7af5c_2_517x232.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58085024a4e7e425f31b19f31201a437eb7af5c_2_775x348.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e58085024a4e7e425f31b19f31201a437eb7af5c_2_1034x464.png 2x" data-dominant-color="B8BAC6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1756×789 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @archamb4 (2021-11-18 17:28 UTC)

<p>Thank you so much!! Our team is trying it out today but it seems very promising and I will report back on how successful we are.</p>

---

## Post #6 by @archamb4 (2021-11-19 03:56 UTC)

<p>Is it possible to select a certain area as the surface to analyze? So that just some of the total object is being compared to the plane at a time?</p>

---

## Post #7 by @lassoan (2021-11-19 13:25 UTC)

<p>Yes, sure, there are many ways to cut out part of a surface, for example Dynamic Modeler module in recent Slicer Preview Releases or the Combine Models module in the Sandbox extension.</p>

---
