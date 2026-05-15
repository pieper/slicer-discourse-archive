---
topic_id: 47036
title: "Segment Editor Paint Tool Stops Working After The First Stro"
date: 2026-05-14
url: https://discourse.slicer.org/t/47036
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
