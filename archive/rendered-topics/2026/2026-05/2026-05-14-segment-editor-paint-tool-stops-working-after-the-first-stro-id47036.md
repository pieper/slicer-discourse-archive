---
topic_id: 47036
title: "Segment Editor Paint tool stops working after the first stroke"
date: 2026-05-14
url: https://discourse.slicer.org/t/47036
last_bumped: 2026-05-18T08:42:44.107Z
---

# Segment Editor Paint tool stops working after the first stroke

**Topic ID**: 47036
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/segment-editor-paint-tool-stops-working-after-the-first-stroke/47036

---

## Post #1 by @Riccardo_Serenella (2026-05-14 20:21 UTC)

<p>Hi everyone,</p>
<p>I am experiencing a strange issue with the <strong>Segment Editor</strong> in 3D Slicer.</p>
<p>When I create a new segmentation and use the <strong>Paint</strong> effect, the first paint stroke works correctly. However, immediately after that first stroke, the Paint tool stops working completely for that segmentation. I can still move the mouse and select the Paint tool, but no additional paint strokes are applied.</p>
<p>The same behavior happens if I create a completely new segmentation: the first paint stroke works, then the Paint effect stops applying any further changes.</p>
<p>So the problem does not seem to be limited to one specific segment or one specific segmentation. It looks like the Paint tool becomes unusable after the first edit.</p>
<p>I have already checked/tried the following:</p>
<ul>
<li>
<p>The correct <strong>Source volume</strong> is selected.</p>
</li>
<li>
<p>The correct segment is selected.</p>
</li>
<li>
<p><strong>Editable area</strong> is set to <code>Everywhere</code>.</p>
</li>
<li>
<p><strong>Editable intensity range</strong> is disabled.</p>
</li>
<li>
<p><strong>Modify other segments</strong> was tested with <code>Allow overlap</code>.</p>
</li>
<li>
<p>I tried creating a new segmentation from scratch.</p>
</li>
<li>
<p>I tried using different segments.</p>
</li>
<li>
<p>The issue still happens: only the first paint stroke works.</p>
</li>
</ul>
<p>From the user interface, there is no obvious warning message. The tool simply stops modifying the segmentation after the first paint operation.</p>
<p>I am attaching a short screen recording showing the behavior.</p>
<p>My setup:</p>
<ul>
<li>
<p>3D Slicer version: <code>5.10.0</code></p>
</li>
<li>
<p>Operating system: <code>[Windows]</code></p>
</li>
<li>
<p>Input data type: <code>[DICOM]</code></p>
</li>
<li>
<p>Module: <code>Segment Editor</code></p>
</li>
<li>
<p>Effect: <code>Paint</code></p>
</li>
</ul>
<p>Could this be related to a corrupted Segment Editor state, segmentation geometry, display scaling, masking settings, or a bug in this Slicer version?</p>
<p>Any suggestion on how to debug or fix this would be very helpful.</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2026-05-14 20:41 UTC)

<aside class="quote no-group" data-username="Riccardo_Serenella" data-post="1" data-topic="47036">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/riccardo_serenella/48/82359_2.png" class="avatar"> Riccardo_Serenella:</div>
<blockquote>
<p>Could this be related to a corrupted Segment Editor state, segmentation geometry, display scaling, masking settings, or a bug in this Slicer version?</p>
</blockquote>
</aside>
<p>What happens you to go Data module, delete the existing segmentation object, right click on your volume and choose “Segment this” and then redo the segmentation?</p>

---

## Post #3 by @Riccardo_Serenella (2026-05-15 07:07 UTC)

<p>Hi, thank you for your answer.</p>
<p>I tried many times and I tried this kind of way too, bu it seems to be stuck. I also tried to uninstall and do the installation again.</p>
<p>First it happened on a WorkStation and then when I tried to do a workaround by installing Slicer on a laptop after playing a bit it happened anyway and in the same way.</p>

---

## Post #4 by @muratmaga (2026-05-15 20:04 UTC)

<p>A lot of people are using the segment editor and this functionality daily on the v5.10.0 with the problem. So the chances are this problem is unique to your data and/or computer settings you are using. We might help more if you can share your data.</p>

---

## Post #5 by @Riccardo_Serenella (2026-05-18 07:21 UTC)

<p>Unfortunately I can’t share my dataset. As far as the computer is concerned, I’m sure that the laptop has standard settings, maybe the bug is in the data, but this feels a little bit weird because I’m working on this data set for a bit and it started doing this at random time.</p>
<p>Any other kind of workaround?</p>
<p>Thank you for you time</p>

---

## Post #6 by @pieper (2026-05-18 07:26 UTC)

<p>Can you reproduce this issue on any public datasets?  Does it happen on other data you have?  Can you describe anything unizue about the data where this happens?</p>

---

## Post #7 by @Riccardo_Serenella (2026-05-18 07:46 UTC)

<p>Hi could you link a public dataset where I can test this?</p>
<p>Meanwhile I think I can share a little video of what happens.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caa03c99eafd22c230f5f188362637a7b737559d.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1a3895705f190adc8e2795473e79039a721e72e.jpeg" data-video-base62-sha1="sUvKMMUGjfKE7ssZCFwKth1I2QJ.mp4">
  </div><p></p>

---

## Post #8 by @cpinter (2026-05-18 08:42 UTC)

<p>There are many datasets in the Sample Data module that you can choose from. The module is available in Slicer core, and there is a button from the Welcome module (“Download Sample Data” on the right side) when you start Slicer, easy to find.</p>

---
