---
topic_id: 5051
title: "Custom Window Level Presets"
date: 2018-12-11
url: https://discourse.slicer.org/t/5051
---

# Custom window/level presets

**Topic ID**: 5051
**Date**: 2018-12-11
**URL**: https://discourse.slicer.org/t/custom-window-level-presets/5051

---

## Post #1 by @emckenzi123 (2018-12-11 23:49 UTC)

<p>Hello,</p>
<p>I often import many images of the same type, and they all should be the same window/level which I would like to set (when Slicer loads them they are washed out with the auto W/L).  It is very tedious to go through each one on the Volumes module and type in the appropriate window and level value for each image.  Is there a way  I could customize a preset window/level setting?  Or maybe just change a bunch of them at the same time?  I welcome GUI or programmatic advice.</p>
<p>~E</p>

---

## Post #2 by @lassoan (2018-12-12 00:00 UTC)

<p>You can set default window/level settings like this (the example sets minimum/maximum to 30/60):</p>
<pre><code class="lang-auto">defaultVolumeDisplayNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLScalarVolumeDisplayNode")
defaultVolumeDisplayNode.AutoWindowLevelOff()
defaultVolumeDisplayNode.SetWindowLevelMinMax(30,60)
slicer.mrmlScene.AddDefaultNode(defaultVolumeDisplayNode)
</code></pre>
<p>You can add this code snippet to your <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F" rel="nofollow noopener">.slicerrc.py</a> file to set these defaults persistently.</p>

---
