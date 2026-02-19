---
topic_id: 28884
title: "How To Show Orthopeadic Hip And Shoulder Deformities On 3D P"
date: 2023-04-13
url: https://discourse.slicer.org/t/28884
---

# How to show Orthopeadic hip and shoulder Deformities on 3D prints

**Topic ID**: 28884
**Date**: 2023-04-13
**URL**: https://discourse.slicer.org/t/how-to-show-orthopeadic-hip-and-shoulder-deformities-on-3d-prints/28884

---

## Post #1 by @MorganB (2023-04-13 12:49 UTC)

<p>Currently I work for Orthopaedic Surgery and we use 3D models for pre-operative planning. We have noticed that slicer smooths over bone deformities. The recons (ROI) show lots of boney landmarks and deformities. However, these details get lost when made into a model. Is it possible this can be fix to show more deformities?</p>
<p>Side note: I do not use the smoothing option when making the models, I just click the auto generate from the CT to 3D model and it is making too smooth of a model.</p>

---

## Post #2 by @lassoan (2023-04-13 12:51 UTC)

<p>If default surface smoothing removes relevant details then you probably want to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">make the segmentation’s resolution higher</a>. You can also try <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#generated-surface-contains-step-artifacts">adjusting Surface smoothing factor</a>.</p>

---

## Post #3 by @MorganB (2023-04-14 18:20 UTC)

<p>Thanks for these however, I cannot find specify geometry in slicer. I don’t know what the button looks like. The SOP does not show were volume source is as well.</p>

---

## Post #4 by @lassoan (2023-04-15 03:12 UTC)

<p>Specify geometry button is next to the volume selector near the top.</p>

---

## Post #5 by @MorganB (2023-04-18 12:04 UTC)

<p>Where is the volume selector? That still does not help me. Can I have an image that would show me where it is.</p>

---

## Post #6 by @lassoan (2023-04-21 14:20 UTC)

<p>I’ve added a screenshot to the documentation <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options">here</a>.</p>

---
