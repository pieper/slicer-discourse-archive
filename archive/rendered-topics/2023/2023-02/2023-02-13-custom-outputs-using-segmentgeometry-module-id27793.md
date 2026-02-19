---
topic_id: 27793
title: "Custom Outputs Using Segmentgeometry Module"
date: 2023-02-13
url: https://discourse.slicer.org/t/27793
---

# Custom outputs using SegmentGeometry module

**Topic ID**: 27793
**Date**: 2023-02-13
**URL**: https://discourse.slicer.org/t/custom-outputs-using-segmentgeometry-module/27793

---

## Post #1 by @laurabc (2023-02-13 12:39 UTC)

<p>Hello community,</p>
<p>I have a 3D segment and I want to extract as much information as possible from the cross-sectional cuts along the segment principal axis. SegmentGeometry module is being very useful, thank you <a class="mention" href="/u/jmhuie">@jmhuie</a> for the great work, but I would be interested in extracting more metrics from each slice, i.e. fitting an ellipse and get its parameters, eccentricity, etc. Is it possible to program custom metrics using the module and python?</p>
<p>Kind regards,<br>
Laura</p>

---

## Post #2 by @jmhuie (2023-02-16 14:06 UTC)

<p>Thank you <a class="mention" href="/u/laurabc">@laurabc</a> for using SegmentGeometry. It’s certainly possible to keep adding metrics that can be computed with the module. Currently, it wouldn’t be very easy for you to do so from the python window in Slicer. Changes would need to be made to the source script directly.</p>
<p>If you know how to programmatically fit an ellipse, I’d be happy to help incorporate that into the module.</p>

---
