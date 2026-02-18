# Draw principal axes

**Topic ID**: 27144
**Date**: 2023-01-09
**URL**: https://discourse.slicer.org/t/draw-principal-axes/27144

---

## Post #1 by @soukup.la (2023-01-09 22:49 UTC)

<p>Hello,<br>
I would like to draw Principal axes (segment statistic) using Python console. Is it possible please?</p>
<p>thank you!</p>

---

## Post #2 by @cpinter (2023-01-11 13:07 UTC)

<p>You can create line or curve markups for the axes and have a control point at (0,0,0) and the other in the coordinate of the axis you got from Segment Statistics.</p>

---

## Post #3 by @lassoan (2023-01-11 17:52 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi">There is an example in the script repository</a> that draws the principal axes using ROI markup. It should not be hard to modify it to use lines instead.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59074851448c694c723545756da8d709daa2dc74.jpeg" data-download-href="/uploads/short-url/cHA62UPpg07oNTOFILaluSaLBac.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59074851448c694c723545756da8d709daa2dc74_2_690x442.jpeg" alt="image" data-base62-sha1="cHA62UPpg07oNTOFILaluSaLBac" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59074851448c694c723545756da8d709daa2dc74_2_690x442.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59074851448c694c723545756da8d709daa2dc74_2_1035x663.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59074851448c694c723545756da8d709daa2dc74.jpeg 2x" data-dominant-color="4F4951"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1184×759 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @MdeBo (2024-07-09 07:36 UTC)

<p>Hi,<br>
Thanks for the suggestion given above. I found the Python code and I believe I should change some string names. However, I am not sure with what name I can call the principal axes.<br>
For example: what should I put instead of <code>obb_direction_ras_x</code> within <code>"LabelmapSegmentStatisticsPlugin.obb_direction_ras_x"</code> to obtain the principal x axes?</p>
<p>In the end I would like to obtain a figure as in <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">this post</a>, in the <strong>Principal axes and moments</strong> figure.</p>
<p>Thanks in advance!</p>

---

## Post #5 by @lassoan (2024-07-11 04:44 UTC)

<p>The referenced <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi">script</a> to generate the bounding boxes still works well. There is no need to change anything. The principal x axis is saved into the <code>obb_direction_ras_x</code> variable.</p>

---
