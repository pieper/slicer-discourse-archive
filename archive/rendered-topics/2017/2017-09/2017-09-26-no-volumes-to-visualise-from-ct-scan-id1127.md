---
topic_id: 1127
title: "No Volumes To Visualise From Ct Scan"
date: 2017-09-26
url: https://discourse.slicer.org/t/1127
---

# No volumes to visualise from CT scan

**Topic ID**: 1127
**Date**: 2017-09-26
**URL**: https://discourse.slicer.org/t/no-volumes-to-visualise-from-ct-scan/1127

---

## Post #1 by @John_D (2017-09-26 22:29 UTC)

<p>I am looking at this tutorial: <a href="https://www.slicer.org/wiki/Documentation/4.3/Modules/VolumeRendering" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.3/Modules/VolumeRendering</a></p>
<p>I have loaded DICOM data for a CT scan - added the files and then clicked Load in DICOM panel -  and it is displaying fine in the standard views but when I open the volume rendering module no volumes are listed.</p>
<p>I’m brand new to 3D Slicer so I guess I miss something obvious here… am I supposed to manually load a volume from the dataset as an extra step? I was kind of expecting since CT is a volumetric dataset a volume would be shown automatically? The Inputs section is greyed out as is the ‘eye’ button.</p>
<p>When I look in Volumes module I can see there is a volume, and the standard RGY views are displaying this volume.</p>
<p>This tutorial page seems to basically be empty: <a href="https://www.slicer.org/wiki/Slicer3:Volume_Rendering_Tutorials" rel="nofollow noopener">https://www.slicer.org/wiki/Slicer3:Volume_Rendering_Tutorials</a></p>
<p>So I’m at a loss - what am I missing please?</p>

---

## Post #2 by @lassoan (2017-09-26 22:37 UTC)

<p>Please try it with the latest nightly version of Slicer. If it still does not work then send a screenshot showing the Volume rendering module.</p>

---

## Post #3 by @John_D (2017-09-26 23:04 UTC)

<p>I think I just figured it out… it’s a multiframe dataset. I don’t fully<br>
understand but in multivolume explorer module I did something to select<br>
which frame was used as the volume and then it sprang to life.</p>
<p>I don’t need it, and understand technically why it is a BIG task, but is<br>
any sort of multi-frame volume-rendering supported?</p>
<p>Thankyou.</p>

---

## Post #4 by @lassoan (2017-09-26 23:59 UTC)

<p>Multi-volume rendering works well. You just have to enable “copy volume” option (or something similar) in multi-volume explorer module.</p>
<p>You can also use Sequences extension for replaying time sequence of any nodes. Replaying o volume sequences can be also captured using ScreenCapture module and written to video files. This allows high-quality display at high frame rates.</p>
<p>SequenceRegistration extension can compute dense deformation field between time points.</p>
<p>Let us know if you need to do any further operations with 4D volumes.</p>

---

## Post #5 by @lassoan (2018-03-12 05:43 UTC)

<p>A post was split to a new topic: <a href="/t/brain-visibility-in-ct-images/2293">Brain visibility in CT images</a></p>

---
