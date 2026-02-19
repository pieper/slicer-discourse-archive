---
topic_id: 2784
title: "Displaying Vtk Actor In A Slice View"
date: 2018-05-09
url: https://discourse.slicer.org/t/2784
---

# Displaying VTK actor in a slice view

**Topic ID**: 2784
**Date**: 2018-05-09
**URL**: https://discourse.slicer.org/t/displaying-vtk-actor-in-a-slice-view/2784

---

## Post #1 by @Anniywell (2018-05-09 13:09 UTC)

<p>I created an actor using polydata，but when I use right mouse to zoom image, the actor cannot follow image zoom. How can I do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfa98a37d2b8b9448973d02750369f0908c01021.jpeg" data-download-href="/uploads/short-url/tD44Am63YBi2PfpxXIwRKsMlEQh.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfa98a37d2b8b9448973d02750369f0908c01021_2_464x500.jpg" alt="image" data-base62-sha1="tD44Am63YBi2PfpxXIwRKsMlEQh" width="464" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfa98a37d2b8b9448973d02750369f0908c01021_2_464x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfa98a37d2b8b9448973d02750369f0908c01021_2_696x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfa98a37d2b8b9448973d02750369f0908c01021.jpeg 2x" data-dominant-color="686868"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">703×757 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/377545ce0e63341eaf98ba54edff4c54ad968269.jpeg" alt="image" data-base62-sha1="7UBw183OisB51NH5QZ29bOIBM4p" width="539" height="479"></p>

---

## Post #2 by @lassoan (2018-05-09 13:15 UTC)

<p>You need to add an observer to the slice node and update the actor position based on XYToRAS matrix.</p>
<p>However, I would not recommend this kind of low-level access, because it would require you to do lots of bookkeeping. It is much easier to put your polydata into a vtkMRMLNode and let Slicer do visualization, including all the zooming, panning, visibility, color, etc. in all the views.</p>
<p>You can use even higher level features: Regions are typically segmented using Segment Editor module. You can also draw contours by dropping markup fiducials on the viewer and connect them using MarkupsToModel extension. We’ll add contour widgets to Slicer core within a few months, which might be also usable for this.</p>

---
