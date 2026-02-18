# O-key shortcut in "Segment Editor" module

**Topic ID**: 32965
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/o-key-shortcut-in-segment-editor-module/32965

---

## Post #1 by @Reza (2023-11-22 18:11 UTC)

<p>Operating system: Windows10 64bit<br>
Slicer version:4.10.2<br>
Expected behavior: O-key shortcut<br>
Actual behavior:</p>
<p>Hi,</p>
<p>In 3D Slicer version 4.10.2, when I use “Editor” module, I can use O-key shortcut to paint over the ROI in a way that it only shows the border of the area I have painted. But, when I use “Segment Editor” module, the O-key shortcut does not work. I would be thankful if you could help me with this issue. (I also tried this shortcut the latest version of 3D slicer, but it did not work)</p>
<p>Thank you,</p>

---

## Post #2 by @lassoan (2023-11-22 18:30 UTC)

<p>I’ve asked <code>bing chat</code> this question:</p>
<blockquote>
<p>create a python script that toggles segmentation filling in 3D Slicer when I press the “O” key</p>
</blockquote>
<p>It generated an almost-perfect code that you can simply copy-paste into the Python console (or if you always want this shortcut then put it into your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file"><code>.slicerrc.py</code> file</a>). It makes <code>O</code> key toggle the filling of the first segmentation node in the scene:</p>
<pre data-code-wrap="python"><code class="lang-python"># Define a function that toggles the segmentation filling
def toggleSegmentationFilling():
  segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
  displayNode = segmentationNode.GetDisplayNode()
  fillVisibility = displayNode.GetVisibility2DFill()
  displayNode.SetVisibility2DFill(not fillVisibility)

# Create a shortcut for the "O" key
shortcut = qt.QShortcut(slicer.util.mainWindow())
shortcut.setKey(qt.QKeySequence("O"))
shortcut.connect("activated()", toggleSegmentationFilling)
</code></pre>
<p>You can ask <code>bing chat</code> to make further changes to the code. For example, if you want to toggle fill visibility in all the segmentations in the scene, not just the first one then you can ask:</p>
<blockquote>
<p>Modify this code to change slice fill of all segmentation nodes in the scene:</p>
</blockquote>
<p>and copy the full script from above. I’ve tried it and it worked perfectly.</p>

---

## Post #3 by @Reza (2023-11-22 19:04 UTC)

<p>Thank you. Is there any way to use the O-key shortcut while I am segmenting in the 3D Slicer?</p>

---

## Post #4 by @lassoan (2023-11-22 19:09 UTC)

<p>Yes, the shortcut works while you are segmenting.</p>

---
