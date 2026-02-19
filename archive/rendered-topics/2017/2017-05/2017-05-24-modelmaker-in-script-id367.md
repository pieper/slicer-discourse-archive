---
topic_id: 367
title: "Modelmaker In Script"
date: 2017-05-24
url: https://discourse.slicer.org/t/367
---

# Modelmaker in script

**Topic ID**: 367
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/modelmaker-in-script/367

---

## Post #1 by @brhoom (2017-05-24 10:04 UTC)

<p>Dear all,<br>
I am trying to generate a model from a label then load it to the 3D view. I used the CLI Modelmaker but it does not work:<br>
<code>~/Slicer-4.6.2/Slicer --launch ~/Slicer-4.6.2/lib/Slicer-4.6/cli-modules/ModelMaker ./label.nrrd ./model.stl</code><br>
What about if the label has multiple colors, how can I generate multiple models from such label.</p>
<p>It would be nice if you update the wiki to include such information.</p>
<p>Thanks!<br>
Ibraheem</p>

---

## Post #2 by @lassoan (2017-05-24 11:41 UTC)

<p>In general, I would recommend using a segmentation node module for displaying segments in both 2D and 3D:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D</a></p>

---

## Post #3 by @brhoom (2017-05-24 14:00 UTC)

<p>Thanks Andras, this is really helpful. I just like to comment that it works only with the nightly build.</p>

---

## Post #4 by @lassoan (2017-05-24 14:30 UTC)

<p>Yes. The latest stable version is very old.</p>

---
