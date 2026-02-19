---
topic_id: 37108
title: "How To Get First And Last Contact Point Between A Vtkmrmlmar"
date: 2024-06-30
url: https://discourse.slicer.org/t/37108
---

# How to get first and last contact point between a vtkMRMLMarkupsCurveNode and a model?

**Topic ID**: 37108
**Date**: 2024-06-30
**URL**: https://discourse.slicer.org/t/how-to-get-first-and-last-contact-point-between-a-vtkmrmlmarkupscurvenode-and-a-model/37108

---

## Post #1 by @apparrilla (2024-06-30 14:29 UTC)

<p>I have a bone model crossed by a curveNove. Any of the control points in curveNode are in model surface but I want to get them.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/632d0e607037e4af2c8dab8892661f2da81666b4.jpeg" data-download-href="/uploads/short-url/e9lNIH8n1ywlO7myaKfAgrU56ja.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632d0e607037e4af2c8dab8892661f2da81666b4_2_690x390.jpeg" alt="image" data-base62-sha1="e9lNIH8n1ywlO7myaKfAgrU56ja" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632d0e607037e4af2c8dab8892661f2da81666b4_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632d0e607037e4af2c8dab8892661f2da81666b4_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/632d0e607037e4af2c8dab8892661f2da81666b4_2_1380x780.jpeg 2x" data-dominant-color="8A8AA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1629×922 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I´ve used vtk.vtkOBBTree() with IntersectWithLine for lines but I can´t find something similar for curves.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @chir.set (2024-06-30 19:49 UTC)

<p>You may investigate vtkSelectEnclosedPoints and/or vtkExtractEnclosedPoints to get all points from the curve that are inside your bone segment.</p>
<p>You must convert the segment to polydata, and get the curve as polydata also (GetCurveWorld()) as inputs to the mentioned classes. With vtkExtractEnclosedPoints, the first and last points of the output are what you are expecting. You might want to add more points to the curve’s polydata using vtkPolyDataPointSampler.</p>
<p>This approach is valid in the simple case you are exposing: a simple curve, a simple segment, one entry and one exit. If the curve zigzags through the segment, this doesn’t hold.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ee1d026d368e1efcef84f904b0d63bd222a794e.png" alt="entry_exit_locations" data-base62-sha1="fOUk5IDud6CMVKM1xh3Rg8xGWpo" width="559" height="447"></p>

---
