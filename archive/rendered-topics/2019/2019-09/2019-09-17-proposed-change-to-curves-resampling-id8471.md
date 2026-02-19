---
topic_id: 8471
title: "Proposed Change To Curves Resampling"
date: 2019-09-17
url: https://discourse.slicer.org/t/8471
---

# Proposed change to curves resampling

**Topic ID**: 8471
**Date**: 2019-09-17
**URL**: https://discourse.slicer.org/t/proposed-change-to-curves-resampling/8471

---

## Post #1 by @smrolfe (2019-09-17 19:30 UTC)

<p>I noticed some unexpected behavior while using <a href="https://github.com/Slicer/Slicer/blob/1ba1f270ccb6e5227d27944b7968e00c688e78fd/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsCurveNode.cxx#L193" rel="noopener nofollow ugc">vtkMRMLMarkupsCurveNode::ResamplePoints</a></p>
<p>Due to small rounding differences when comparing the remaining segment to the sampling distance, the last point is sometimes not placed, as shown in the figure below. The resampled curve (blue) is plotted over the original curve (red). <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fbb5749e7e9c86093b716f221b8eb8fa8ea19b1.png" data-download-href="/uploads/short-url/dESJCH7ah5jgFR31UEEeIsvjfnb.png?dl=1" title="OriginalCurve" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fbb5749e7e9c86093b716f221b8eb8fa8ea19b1_2_670x499.png" alt="OriginalCurve" data-base62-sha1="dESJCH7ah5jgFR31UEEeIsvjfnb" width="670" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fbb5749e7e9c86093b716f221b8eb8fa8ea19b1_2_670x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fbb5749e7e9c86093b716f221b8eb8fa8ea19b1_2_1005x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fbb5749e7e9c86093b716f221b8eb8fa8ea19b1.png 2x" data-dominant-color="989AD2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OriginalCurve</span><span class="informations">1217×908 36.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This issue can be replicated by creating an arbitrary 5 point curve and running:</p>
<pre><code class="lang-python">resampleNumber=10
curve=getNode("C")
currentPoints = curve.GetCurvePointsWorld()
newPoints = vtk.vtkPoints()
sampleDist = curve.GetCurveLengthWorld()/(resampleNumber-1)

closedCurveOption = 0
curve.ResamplePoints(currentPoints,newPoints,sampleDist,closedCurveOption)

vector=vtk.vtkVector3d()
pt=[0,0,0]
resampledCurve = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", "resampledCurveOrig")

for controlPoint in range(0,newPoints.GetNumberOfPoints()):
  newPoints.GetPoint(controlPoint,pt)
  vector[0]=pt[0]
  vector[1]=pt[1]
  vector[2]=pt[2]
  resampledCurve.AddControlPoint(vector)
</code></pre>
<p>I fixed this for myself by rounding the remaining segment length and sampling distance to 4 decimal places when they are compared. I was wondering if there’s interest in changing this in vtkMRMLMarkupsCurveNode::ResamplePoints too? I can submit a pull request if so. Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe7e9804ff51ed62cc2f5581b0d202d503dfa816.png" data-download-href="/uploads/short-url/AjmvdvWvAKx2wbo5AtVGTXKja9o.png?dl=1" title="UpdatedCurve" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe7e9804ff51ed62cc2f5581b0d202d503dfa816_2_662x500.png" alt="UpdatedCurve" data-base62-sha1="AjmvdvWvAKx2wbo5AtVGTXKja9o" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe7e9804ff51ed62cc2f5581b0d202d503dfa816_2_662x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe7e9804ff51ed62cc2f5581b0d202d503dfa816_2_993x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe7e9804ff51ed62cc2f5581b0d202d503dfa816.png 2x" data-dominant-color="989BD2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">UpdatedCurve</span><span class="informations">1222×922 40.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-09-17 20:29 UTC)

<p>Yes, please send a pull request.</p>

---

## Post #3 by @smrolfe (2019-09-17 23:04 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>.  I have one more question on this. In my module, I rounded to 4 decimal places to get rid of the differences on the order of ~1e-14 when comparing two doubles. I would like to use a more precise approach such as:</p>
<blockquote>
<p>double a, b;<br>
if(fabs(a - b) &lt;= epsilon * fabs(a))</p>
</blockquote>
<p>Is there a convention or recommended approach for setting this epsilon in Slicer?</p>

---

## Post #4 by @lassoan (2019-09-17 23:52 UTC)

<p>I’ve just found that the resample function already handled this case properly but only for closed curves. I’ve update the code to do the same for open curves, too.</p>

---

## Post #5 by @smrolfe (2019-09-18 00:44 UTC)

<p>Great! Thanks <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---

## Post #6 by @lassoan (2019-09-18 16:21 UTC)

<p>Fix committed to master (Revision: 28508).</p>

---

## Post #7 by @smrolfe (2019-09-19 18:29 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, this is working well for me in the preview version.</p>

---
