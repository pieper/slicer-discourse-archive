---
topic_id: 11905
title: "Fov Spacing Match Volumes"
date: 2020-06-06
url: https://discourse.slicer.org/t/11905
---

# FOV, spacing match Volumes

**Topic ID**: 11905
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/fov-spacing-match-volumes/11905

---

## Post #1 by @ada (2020-06-06 14:50 UTC)

<p>Hi developers,</p>
<p>What is the python function to set the slice views as “FOV, spacing match Volumes” instead of “FOV, spacing match 2D” ?<br>
Thank you,<br>
Best</p>

---

## Post #2 by @lassoan (2020-06-06 21:15 UTC)

<p>It controls how Slicer generates pixels of the slice that is shown in the 3D view. See more details <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">here</a>. Let us know if you need more details.</p>

---

## Post #3 by @ada (2020-06-06 21:28 UTC)

<p>Hello,<br>
Thank you for your answer. I know what is done, I just would like to know how can I automatically set this option with my own script in python ?<br>
Thank you</p>

---

## Post #4 by @lassoan (2020-06-06 23:07 UTC)

<p>How to find a Python function for any Slicer features:</p>
<ul>
<li>Go to <a href="https://github.com/Slicer/Slicer/">Slicer project repository on github</a>
</li>
<li>Enter text that you see on the GUI near the function that you want to use. In this case, enter <code>"FOV, spacing match Volumes"</code> (adding quotes around the text makes sure it finds that exact text)</li>
<li>Usually the text is found in a .ui file, in this case it is in <a href="https://github.com/Slicer/Slicer/blob/dfef9574096a10c4f02337b59c5edfd6810b55db/Libs/MRML/Widgets/Resources/UI/qMRMLSliceControllerWidget.ui">qMRMLSliceControllerWidget.ui</a>, open the file</li>
<li>Find the text in the page, and look up what is the name of the widget or action that it is associated with - in this case it is an action named <code>actionSliceModelModeVolumes</code>
</li>
<li>Search for that widget or action name in the repository, you should find a source file(s) that use it. In this case it will is <a href="https://github.com/Slicer/Slicer/blob/46345e8a3dba3d591a7f06767aff83a2beefad6a/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx">qMRMLSliceControllerWidget.cxx</a>
</li>
<li>Search for the action/widget name, and you’ll find what it does - in this case it calls <code>setSliceModelModeVolumes</code> method, which calls <code>this-&gt;setSliceModelMode(vtkMRMLSliceNode::SliceResolutionMatchVolumes)</code>, which then calls <code>d-&gt;MRMLSliceNode-&gt;SetSliceResolutionMode(mode)</code>
</li>
</ul>
<p>This means that this action calls <code>someSliceNode-&gt;SetSliceResolutionMode(vtkMRMLSliceNode::SliceResolutionMatchVolumes)</code> in Python syntax it is <code>someSliceNode.SetSliceResolutionMode(slicer.vtkMRMLSliceNode.SliceResolutionMatchVolumes)</code>. For example, for the red slice node this will be:</p>
<pre><code class="lang-python">sliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
sliceNode.SetSliceResolutionMode(slicer.vtkMRMLSliceNode.SliceResolutionMatchVolumes)
</code></pre>

---

## Post #5 by @ada (2020-06-08 07:21 UTC)

<p>Thank you so much for your help !</p>

---
