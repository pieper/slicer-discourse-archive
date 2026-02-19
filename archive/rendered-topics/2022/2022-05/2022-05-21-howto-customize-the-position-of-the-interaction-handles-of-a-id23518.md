---
topic_id: 23518
title: "Howto Customize The Position Of The Interaction Handles Of A"
date: 2022-05-21
url: https://discourse.slicer.org/t/23518
---

# Howto customize the position of the Interaction handles of a lineNode?

**Topic ID**: 23518
**Date**: 2022-05-21
**URL**: https://discourse.slicer.org/t/howto-customize-the-position-of-the-interaction-handles-of-a-linenode/23518

---

## Post #1 by @jumbojing (2022-05-21 13:21 UTC)

<p>By default the position of the Interaction handles on the lineNode is at the midpoint, but howto place the Interaction handles in a custom location?<br>
Like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccf1a8f71f41500d22cbfffe884cd0214d67e7ed.jpeg" data-download-href="/uploads/short-url/tf19O2jp4u8RMNU2Ljw0lH58Lhz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccf1a8f71f41500d22cbfffe884cd0214d67e7ed_2_661x500.jpeg" alt="image" data-base62-sha1="tf19O2jp4u8RMNU2Ljw0lH58Lhz" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccf1a8f71f41500d22cbfffe884cd0214d67e7ed_2_661x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccf1a8f71f41500d22cbfffe884cd0214d67e7ed_2_991x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ccf1a8f71f41500d22cbfffe884cd0214d67e7ed_2_1322x1000.jpeg 2x" data-dominant-color="76756C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1464×1106 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-05-23 04:16 UTC)

<p>Currently the handle position is always the center of gravity of all control points, implemented in <code>vtkMRMLMarkupsNode::UpdateInteractionHandleToWorldMatrix()</code> method. You can create a custom markups line node class, override this method in it, then register it as a custom markup.</p>
<p>If you don’t want to implement a custom markup then you can use two markups, one of them just displays the interaction handles (the control points are hidden by setting the glyph size to 0), and the other displays the control points. You would add observers to both nodes and keep the control point positions in the two nodes in sync.</p>

---
