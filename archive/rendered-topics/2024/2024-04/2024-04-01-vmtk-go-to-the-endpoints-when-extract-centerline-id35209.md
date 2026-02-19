---
topic_id: 35209
title: "Vmtk Go To The Endpoints When Extract Centerline"
date: 2024-04-01
url: https://discourse.slicer.org/t/35209
---

# VMTK go to the endpoints when extract centerline

**Topic ID**: 35209
**Date**: 2024-04-01
**URL**: https://discourse.slicer.org/t/vmtk-go-to-the-endpoints-when-extract-centerline/35209

---

## Post #1 by @Ethan_Penn (2024-04-01 21:05 UTC)

<p>when I extract the centerline in slicer, it does not go all the way to the endpoints, just close, is there a way to make it so the centerline will go all the way to the endpoints?</p>

---

## Post #2 by @lassoan (2024-04-01 21:27 UTC)

<p>Centerline means that it is in the center of the vessel model in 3D. If the end of the line touched the surface then it would not be in the center anymore. You could slightly extend the centerlines with a short line segment to reach the vessel wall. However, if you do CFD analysis then you typically need to extend the vessel with a long straight segment anyway, so there is no need to add any extensions at the time of centerline extraction.</p>

---

## Post #3 by @Ethan_Penn (2024-04-02 19:52 UTC)

<p>In vmtk there looks to be a setting that allows/tells the software to end the centerline at the endpoint opposed to at the end of the voronoi diagram. I was wondering if this setting is available in slicer too/how could I add it (this would make my measurements easier/more accurate. Thanks so much</p>

---

## Post #4 by @lassoan (2024-04-02 23:19 UTC)

<p>VMTK Slicer modules are just Python scripts (see for example <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py">this</a>), you can edit them in a text editor. If you enable developer mode in application settings then edit and reload buttons show up in the GUI.</p>
<p>Why do you need the centerline extend beyond the center: for aesthetic purposes or there is a specific clinical need?</p>

---

## Post #5 by @Deep_Learning (2024-06-20 16:07 UTC)

<p>The reason is to compute the length, from endpoint to endpoint along the centerline.  One can add the endpoints to curve and then resample.  Works well.  resampling is needed.</p>
<p>I have two endpoints.  Easy to copy paste the last “endpoint” into the curve at the end.</p>
<p>Cannot figure how to add the “first point” without python.  Is it possible to paste into the first point? Or paste at the end and reorder that point without scripting.</p>

---
