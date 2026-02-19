---
topic_id: 20919
title: "Changing Threshold In Python Does Not Update In Any Views"
date: 2021-12-05
url: https://discourse.slicer.org/t/20919
---

# Changing threshold in python does not update in any views

**Topic ID**: 20919
**Date**: 2021-12-05
**URL**: https://discourse.slicer.org/t/changing-threshold-in-python-does-not-update-in-any-views/20919

---

## Post #1 by @koeglfryderyk (2021-12-05 22:04 UTC)

<p>I want to use a shortcut to change the lower threshold of a foreground US volume to 1 (so that the black surrounding pixels disappear).</p>
<p>I used the code from <a href="https://discourse.slicer.org/t/how-to-use-python-to-achieve-the-thresholding-effect-of-the-volumes-module-synchronized-with-the-volume-rendering/20891/9">here</a>, and this code changes the threshold in the GUI, however, it doesn’t ‘propagate’ to any of the views - nothing changes there. I still need to manually nudge the slider/value a bit for the view to be updated.</p>
<p>Is there any command that needs to be executed for the view to be updated?</p>

---

## Post #2 by @jamesobutler (2021-12-06 00:06 UTC)

<p>Make sure you have turned on thresholding for the display node. You can set threshold values with thresholding not enabled.</p>
<pre data-code-wrap="python"><code class="lang-python">volume_node.GetDisplayNode().ApplyThresholdOn()
</code></pre>
<p>This will essentially change the Threshold mode combobox selection from “Off” to “Manual”. It also changes to “Manual” after manually dragging the threshold slider.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48e1d5f6957def4d20304ca19ca50061ce4329b2.png" alt="image" data-base62-sha1="aoKebCnFkBfvu0J3vmyoeM8iKmS" width="464" height="66"></p>

---
