---
topic_id: 20113
title: "Determination Of The Tumors Move By Time"
date: 2021-10-12
url: https://discourse.slicer.org/t/20113
---

# Determination of the tumor's move by time

**Topic ID**: 20113
**Date**: 2021-10-12
**URL**: https://discourse.slicer.org/t/determination-of-the-tumors-move-by-time/20113

---

## Post #1 by @ylcnkzy (2021-10-12 09:38 UTC)

<p>Dear All,</p>
<p>I am working with CT data that have been acquired from the same patients at different time points. My aim is to evaluate the tumor shrinkage (I have established it well in the 3D slicer, and works well) and tumor’s movement (this part is the question).</p>
<p>Since I am working on the lung (which has breathing phases, and I use average CT), the determination of the tumor’s movement is challanging. I plan to use a coordinate system in which I will assign the XYZ axis by taking advantage of the human anatomy to determine coordinates for each time point.</p>
<p>Is there any tool (plugins) so that I can do it?</p>
<p>Please let me know your ideas.</p>
<p>Thanks for your help.</p>

---

## Post #2 by @pieper (2021-10-12 18:30 UTC)

<p>When you have both patient motion (breathing, body posture etc) and pathological changes (tumor growth, atrophy etc) it can be very difficult to untangle what’s really going on.  Probably your best quantifications will be relative, such as distance from one side of the tumor to the other or distance from tumor to well defined anatomical landmarks.  You can do these measurements in 3D with Slicer Markups or calculate size and other features with the Segment Editor and Segment Statistics or SlicerRadiomics.</p>

---

## Post #3 by @ylcnkzy (2021-10-13 12:17 UTC)

<p>Thanks Steve!</p>
<p>I was also thinking of the possibilities of using some anatomic landmarks. I will try the recommenden plugins.</p>
<p>Best</p>

---

## Post #4 by @lassoan (2021-10-13 12:27 UTC)

<p>If you have anatomical landmarks then you can align the volumes based on them as described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---

## Post #5 by @ylcnkzy (2021-10-13 12:31 UTC)

<p>Thanks Andras!</p>
<p>I will check it out.</p>
<p>Best.</p>

---
