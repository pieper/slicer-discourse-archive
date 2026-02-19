---
topic_id: 6218
title: "Python Console Warnings For Deprecated Methods"
date: 2019-03-20
url: https://discourse.slicer.org/t/6218
---

# Python console warnings for deprecated methods

**Topic ID**: 6218
**Date**: 2019-03-20
**URL**: https://discourse.slicer.org/t/python-console-warnings-for-deprecated-methods/6218

---

## Post #1 by @fedorov (2019-03-20 17:56 UTC)

<p>I was debugging a code that iterated over segmentation nodes as below</p>
<pre><code class="lang-python">sn = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
while sn:
  ...
  sn = slicer.mrmlScene.GetNextNodeByClass('vtkMRMLSegmentationNode')
</code></pre>
<p>and it was getting only the first node from the scene.</p>
<p>I then searched for the method in the source code, and found that the method I was using was deprecated: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScene.h#L246-L253" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScene.h#L246-L253</a></p>
<p>There is even a <code>vtkWarningMacro()</code> in the implementation of that method: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScene.cxx#L1655" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScene.cxx#L1655</a>, but nothing gets printed out on the console to warn the user when that method is used (at least not for me).</p>
<p>Is that warning supposed to be printed? Is it a bug, or some setting that prevented me from seeing it?</p>

---

## Post #2 by @lassoan (2019-03-20 19:06 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.getNodesByClass" rel="nofollow noopener">getNodesByClass</a> method to get all nodes of a certain class in a Python list.</p>
<p><code>slicer.mrmlScene.GetNextNodeByClass()</code> failed for you because traversing the MRML node list is initialized by <code>slicer.mrmlScene.InitTraversal()</code> method call (and not <code>GetFirstNodeByClass</code>). We kept the method for only backward compatibility. Documentation of how to use it was removed because it could have encouraged people to use it.</p>
<p>VTK errors are not printed on the Python console. It is not a bug, but I agree that it could be a useful feature to have. We would probably not want to flood the console with log VTK messages all the time, so I’m not sure what the expected behavior would be.</p>

---

## Post #3 by @fedorov (2019-03-20 19:13 UTC)

<p>Thanks Andras. I was able to quickly fix the code once I realized that method was deprecated.</p>

---
