---
topic_id: 22918
title: "Corresponding Points And Its Correlating Color Map"
date: 2022-04-12
url: https://discourse.slicer.org/t/22918
---

# Corresponding points and its correlating color map

**Topic ID**: 22918
**Date**: 2022-04-12
**URL**: https://discourse.slicer.org/t/corresponding-points-and-its-correlating-color-map/22918

---

## Post #1 by @Lexus_H (2022-04-12 03:06 UTC)

<p>Please help me to determine corresponding points between two models so I can measure the distance between two corresponding points. Also, do I need to use one model as source and registered model (super composed two source and target models)?  I am hoping to generate its corresponding color map along with that?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2022-04-20 15:39 UTC)

<p>You need to determine corresponding point pairs if you want to measure differences between meshes.</p>
<p>Often meshes that you want to compare are very similar, so if they are spatially aligned then the closest on the other mesh is the corresponding point. If this is the case for your data then <code>ModelToModelDistance</code> extension’s <code>Model to model distance</code> module with <code>signed_closest_point</code> to compute distances.</p>
<p>In case when closest points are not the anatomically corresponding points, distance to closest point is not a useful metric. For example, you cannot measure the depth of a narrow and deep depression using closest distance if the bottom of the hole is close to some other unrelated internal or external surface areas.</p>
<p>For these more complicated cases, making manual measurements (e.g., using Markups module) may work better.</p>
<p>If you want to make the process less manual then you may segment the defect (e.g., a cavity) using Segment Editor module and compute metrics (volume, oriented bounding box size, etc.) using Segment Statistics module.</p>

---

## Post #3 by @Lexus_H (2022-05-02 16:30 UTC)

<p>You have advised me that corresponding points is the way to go with my project so if you can share with me some videos or list of steps to follow, that will be great.</p>
<p>I have done modeltomodel, signed closest, so I’d like to focus on corresponding points to generate colormap and measurements.</p>
<p>Thanks,</p>

---

## Post #4 by @lassoan (2022-05-03 22:02 UTC)

<p>If corresponding points are not the closest points then the solution is not trivial. Based on detailed knowledge of your data someone can develop a custom algorithm for that. It can be based on geometry (e.g., surface normal directions, if we know that changes occur along that direction), registration, shape regression, etc. These are complex computational methods applied to your data, so I don’t think you can find steps/videos to follow. I would recommend to get some funding and team up with an academic group or company who has experience in doing such analysis.</p>

---

## Post #5 by @Mohammed_Abdul_Majee (2023-08-21 15:29 UTC)

<p>How can I create a surface model after doing the model to model distance step? I tried watching the demo DCBIA video but the suggested module (shape population viewer) did not give me the same color map creation window (in slicer 5.2.2) as in the video. Instead it just asked me to load the model which took so long. Shall I wait for the model obtained by model to model distance to load and the colour map would be generated automatically ??</p>

---
