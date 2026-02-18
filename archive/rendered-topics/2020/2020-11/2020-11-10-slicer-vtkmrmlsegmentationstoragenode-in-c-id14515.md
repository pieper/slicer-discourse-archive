# Slicer vtkMRMLSegmentationStorageNode in C++

**Topic ID**: 14515
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/slicer-vtkmrmlsegmentationstoragenode-in-c/14515

---

## Post #1 by @nm19 (2020-11-10 01:02 UTC)

<p>Hi,</p>
<p>I was wondering what slicer.vtkMRMLSegmentationNode() did and how it could be implemented directly in C++. Moreover, I was not able to find its Python implementation in the Github repo. Any pointers would be greatly appreciated.</p>

---

## Post #2 by @jamesobutler (2020-11-10 02:38 UTC)

<p><a href="https://github.com/Slicer/Slicer/blob/f67f5feb6379ca5a5f57d722a5648f7e33ac66ec/Libs/MRML/Core/vtkMRMLSegmentationNode.cxx" rel="noopener nofollow ugc">vtkMRMLSegmentationNode</a> is originally implemented in C++ in Slicer. What you specified <code>slicer.vtkMRMLSegmentationNode()</code> is available because most of the C++ code is python wrapped which is why you were able to use it in Python.</p>
<p>What was the reason for your question? Do you have a usage question as it relates to the vtkMRMLSegmentationNode object?</p>

---

## Post #3 by @nm19 (2020-11-11 00:40 UTC)

<p>Thanks for the response. I was in the process of converting some Slicer Python code to C++ and the initial Python code called slicer.vtkMRMLSegmentationNode(). I tried to implement it directly in C++ based off of the documentation <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html" rel="noopener nofollow ugc">here</a>, however some of the functionality isn’t quite right. So I wanted to get a better idea of what exactly slicer.vtkMRMLSegmentationNode() is doing.</p>

---

## Post #4 by @lassoan (2020-11-11 15:53 UTC)

<p>Majority of Slicer is implemented in C++, so you can find C++ examples for everything by doing full-text search in the entire Slicer source code.</p>

---
