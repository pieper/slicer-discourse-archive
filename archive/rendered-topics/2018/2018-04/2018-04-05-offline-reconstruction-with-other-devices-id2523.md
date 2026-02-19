---
topic_id: 2523
title: "Offline Reconstruction With Other Devices"
date: 2018-04-05
url: https://discourse.slicer.org/t/2523
---

# Offline reconstruction with other devices

**Topic ID**: 2523
**Date**: 2018-04-05
**URL**: https://discourse.slicer.org/t/offline-reconstruction-with-other-devices/2523

---

## Post #1 by @Nolwenn (2018-04-05 16:54 UTC)

<p>Hi everyone,<br>
I’m a PhD student currently working on ultrasound volume reconstruction and I just found 3DSlicer/SlicerIGT. I tried the tutorials and the results are really impressive.<br>
I need your help for the two following issues:<br>
First I tried the tutorial on the elbow offline reconstruction. It is not clear to me why there is a need for a stylus in this example. I thought the stylus was used for the calibration step, but once this step is done, I do not understand why we need to compute the stylustoreference matrix.<br>
The second point is that I do not have the US and tracking systems that are proposed by the PLUS toolkit. Since I just a do not need a reconstruction in real time but rather an offline reconstruction, do you know if it is possible to change the configuration files so that I can compute a volume reconstruction with other devices ?<br>
Best regards,<br>
Nolwenn</p>

---

## Post #2 by @lassoan (2018-04-07 14:36 UTC)

<aside class="quote no-group" data-username="Nolwenn" data-post="1" data-topic="2523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/82dd89/48.png" class="avatar"> Nolwenn:</div>
<blockquote>
<p>First I tried the tutorial on the elbow offline reconstruction. It is not clear to me why there is a need for a stylus in this example.</p>
</blockquote>
</aside>
<p>It is not needed. It can be useful if you want to register the acquired ultrasound to pre-procedural images based on anatomical landmarks. [quote=“Nolwenn, post:1, topic:2523”]<br>
I do not have the US and tracking systems that are proposed by the PLUS toolkit.<br>
[/quote]</p>
<p>Plus can acquire ultrasound images from any scanner by using framegrabbers. What tracking system do you use?</p>
<aside class="quote no-group" data-username="Nolwenn" data-post="1" data-topic="2523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/82dd89/48.png" class="avatar"> Nolwenn:</div>
<blockquote>
<p>if it is possible to change the configuration files so that I can compute a volume reconstruction with other devices</p>
</blockquote>
</aside>
<p>You just need to create a sequence file that contains images and transforms in this format: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html" class="inline-onebox">Plus applications user manual: Sequence file</a> and run the command-line volume reconstructor tool: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ProcedureVolumeReconstruction.html" class="inline-onebox">Plus applications user manual: Volume reconstruction</a></p>

---

## Post #3 by @Nolwenn (2018-04-09 06:51 UTC)

<p>Thank you so much for your answer !<br>
We have the Vicon system for the tracking and the Aixplorer (Supersonic Imagine) for the US acquisitions.<br>
What I do not understand is the config file which is needed for the reconstruction. Can I create one for my devices ?<br>
Best,</p>

---
