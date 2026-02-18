# Change image without changing zoom and positions of sliders

**Topic ID**: 13784
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/change-image-without-changing-zoom-and-positions-of-sliders/13784

---

## Post #1 by @rohan_n (2020-09-30 23:54 UTC)

<p>I have a scripted module that looks like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6a11bee25598efda8057234d3ad6f189e1ea3b8.jpeg" data-download-href="/uploads/short-url/uCHlUdXFSwR6c7GdsU1kWc55x4k.jpeg?dl=1" title="exampleimg9_30_2020" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a11bee25598efda8057234d3ad6f189e1ea3b8_2_690x388.jpeg" alt="exampleimg9_30_2020" data-base62-sha1="uCHlUdXFSwR6c7GdsU1kWc55x4k" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a11bee25598efda8057234d3ad6f189e1ea3b8_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a11bee25598efda8057234d3ad6f189e1ea3b8_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6a11bee25598efda8057234d3ad6f189e1ea3b8_2_1380x776.jpeg 2x" data-dominant-color="BDBDBD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">exampleimg9_30_2020</span><span class="informations">2560×1440 460 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
In the example shown, the user has zoomed in on both the red and the yellow slices, and the red &amp; yellow slice slider positions are off center.<br>
The user is about to display a different image by choosing that image from the dropdown menu. Image selection from the dropdown menu prompts my scripted module to call<br>
<code>slicer.util.setSliceViewerLayers(background=self.inputSelector.currentNodeID)</code><br>
so that the image chosen by the user will be displayed. However, it appears that this line of code automatically resets the zoom and slice slider positions to their default values.<br>
Is there any way I can call<br>
<code>slicer.util.setSliceViewerLayers(background=self.inputSelector.currentNodeID)</code><br>
without resetting zoom and slider positions, so that the user doesn’t lose track of the region they have zoomed into whenever they switch images?</p>
<p>Thanks,<br>
Rohan</p>

---

## Post #2 by @cpinter (2020-10-01 07:37 UTC)

<p>I’m not completely sure that this doesn’t change any other setting, but as far as I remember it doesn’t.</p>
<pre><code class="lang-auto">sliceCompositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
for sliceCompositeNode in sliceCompositeNodes:
  sliceCompositeNode.SetBackgroundVolumeID(newVolumeNode.GetID())
</code></pre>

---

## Post #3 by @rohan_n (2020-10-01 16:38 UTC)

<p>Thank you, this way of switching image displayed does what I need.</p>

---
