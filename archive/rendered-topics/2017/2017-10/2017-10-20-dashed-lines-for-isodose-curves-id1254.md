---
topic_id: 1254
title: "Dashed Lines For Isodose Curves"
date: 2017-10-20
url: https://discourse.slicer.org/t/1254
---

# Dashed lines for isodose curves

**Topic ID**: 1254
**Date**: 2017-10-20
**URL**: https://discourse.slicer.org/t/dashed-lines-for-isodose-curves/1254

---

## Post #1 by @larsf (2017-10-20 13:42 UTC)

<p>Dear Slicer experts,</p>
<p>Is there any way to create isodose curves using dashed lines (or dots, just not solid lines) in the Radiotherapy Isodose extension? I took a look in the Models module where the thickness of the isodose curves can be altered. But I did unfortunately not figure out a way to change the line type.</p>
<p>Thanks,</p>
<p>Lars</p>

---

## Post #2 by @cpinter (2017-10-20 16:47 UTC)

<p>Hi Lars,</p>
<p>As far as I know model intersections indeed don’t support line styles. It may be possible to implement by running a filter on the line given by vtkCutter around <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLModelSliceDisplayableManager.cxx#L475-L493">here</a>, but I’m not aware of a VTK filter that does that. If there is one, then this is fairly easy to implement.</p>

---

## Post #3 by @cpinter (2017-10-20 16:59 UTC)

<p>Or perhaps use these properties for the actor<br>
<a href="https://www.vtk.org/Wiki/VTK/Examples/Python/DottedLine" class="onebox" target="_blank">https://www.vtk.org/Wiki/VTK/Examples/Python/DottedLine</a></p>

---

## Post #4 by @cpinter (2017-10-20 17:16 UTC)

<p>I quickly tried the latter (added actorProperties-&gt;SetLineStipplePattern(0xf0); under <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLModelSliceDisplayableManager.cxx#L573">this line</a>). It seems to work well, but it looks strange when zoomed out:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2749f73d8755d75d3ba326411b8532e301d46233.jpeg" data-download-href="/uploads/short-url/5Bz5IP4GxZK1kMRB6Yfj4lpdf3R.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2749f73d8755d75d3ba326411b8532e301d46233_2_438x500.jpg" alt="image" data-base62-sha1="5Bz5IP4GxZK1kMRB6Yfj4lpdf3R" width="438" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2749f73d8755d75d3ba326411b8532e301d46233_2_438x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/2749f73d8755d75d3ba326411b8532e301d46233_2_657x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2749f73d8755d75d3ba326411b8532e301d46233.jpeg 2x" data-dominant-color="6C6256"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">694×791 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> Any idea why? I can add a combobox for line style in Models / Slice Display if this is figured out.</p>

---

## Post #5 by @Lorensen (2017-10-20 17:20 UTC)

<p>Here is an example that uses texture:<br>
<a href="https://lorensen.github.io/VTKExamples/site/Cxx/Rendering/StippledLine/" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Cxx/Rendering/StippledLine/</a></p>

---

## Post #6 by @cpinter (2017-10-20 17:22 UTC)

<p>Thank you, <a class="mention" href="/u/lorensen">@Lorensen</a>! Especially that the way I found is no longer supported in OpenGL2, which will be the default version soon (hopefully). I’ll try this out.</p>

---

## Post #7 by @cpinter (2017-10-20 20:46 UTC)

<p>Unfortunately vtkActor2D does not support textures. I’m not sure if a vtkActor could be used for model slice intersections.</p>
<p>Work-in-progress topic branch here: <a href="https://github.com/cpinter/Slicer/tree/slice-intersection-line-styles">https://github.com/cpinter/Slicer/tree/slice-intersection-line-styles</a></p>

---
