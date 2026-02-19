---
topic_id: 12020
title: "Curve Visible In 2D Views"
date: 2020-06-14
url: https://discourse.slicer.org/t/12020
---

# Curve visible in 2D views?

**Topic ID**: 12020
**Date**: 2020-06-14
**URL**: https://discourse.slicer.org/t/curve-visible-in-2d-views/12020

---

## Post #1 by @hherhold (2020-06-14 15:58 UTC)

<p>This is probably for Andras (<a class="mention" href="/u/lassoan">@lassoan</a>). When I make an open curve by placing points, I generally do it using a custom layout of stacked 3D views with various layers visible. I noticed this morning when I switched to 4-up view that the curve projection is visible throughout the volume in the 2D viewers. I can disable the projection of the control points and labels, but the curve is always there. Is there a separate visibility setting for the curve itself? I can turn it off in the individual views (Red, Green, Blue) but it I was surprised that the 2D projection visibility “eye” toggle didn’t affect the curve.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2020-06-23 13:53 UTC)

<p>Quick update on this for Andras (<a class="mention" href="/u/lassoan">@lassoan</a>).</p>
<p>Markup curves do appear to fade in 2D views as I scroll through slices, however it looks like the scale of the volume has an effect. If I make curves in a big volume like one of the example CT scans, the curves fade away as I scroll through slices. In a scan with a much smaller scale (insect scan, voxel size of like 10 microns) it looks like the scale is set such that the curves don’t fade quickly enough and stick around through most of the scan.</p>
<p>Is there a scaling or distance factor that feeds into when to fade the curve line in the 2D view? I’m happy to look into this and debug if you can point me in the right direction.</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #3 by @hherhold (2020-06-23 13:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cc6c4d3701f87f4eda696a8ca6481fc06f29204.jpeg" data-download-href="/uploads/short-url/mmUlqPzXbQWDTKZoTfVhyumiRh2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cc6c4d3701f87f4eda696a8ca6481fc06f29204_2_601x500.jpeg" alt="image" data-base62-sha1="mmUlqPzXbQWDTKZoTfVhyumiRh2" width="601" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cc6c4d3701f87f4eda696a8ca6481fc06f29204_2_601x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9cc6c4d3701f87f4eda696a8ca6481fc06f29204_2_901x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cc6c4d3701f87f4eda696a8ca6481fc06f29204.jpeg 2x" data-dominant-color="434346"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1068×888 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Quick example - you can see in the lower middle part of the image that some of the curve is faded, but much of it is still visible. Hopefully this helps!</p>

---

## Post #4 by @lassoan (2020-06-23 15:32 UTC)

<p>The curve starts to fade out at “fading start” distance and completely disappears at “fading end” distance. These values are not exposed on the GUI but you can adjust using the Python console:</p>
<pre><code class="lang-python">markupsNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsNode")
markupsNode.GetDisplayNode.SetLineColorFadingStart(1.0)
markupsNode.GetDisplayNode.SetLineColorFadingEnd(10.0)
</code></pre>
<p>It would be nice to add the option to allow using fade-out distance that is somehow relative to the image size. Maybe we could allow specifying fade-out relative to slice spacing (instead of 10.0mm it could be 10 x slice spacing)?</p>

---

## Post #5 by @hherhold (2020-06-23 16:24 UTC)

<p>Sure, I can look into adding that. Maybe a check box in the “Curve Settings” section? Yes/No for “Fade out relative to slice spacing”?</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2020-06-23 16:37 UTC)

<p>It could be similar to the markups control point sizing (absolute or relative to screen size) and could be implemented similarly: toggle button to switch between sizing modes on the GUI, and a LineFadingMode enum in the markups MRML to switch between fading modes (for now it would only be 2 modes: absolute and relative-to-slice-spacing; but in the future more may be added).</p>

---

## Post #7 by @hherhold (2020-06-23 16:59 UTC)

<p>OK, I’ll take a look. (No promises!!)</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---
