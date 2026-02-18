# Is there a way to do conversion between vtkCollection and vtkMRMLNode?

**Topic ID**: 8243
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-do-conversion-between-vtkcollection-and-vtkmrmlnode/8243

---

## Post #1 by @aiden.zhu (2019-08-30 22:03 UTC)

<p>Excuse my silly question if it is silly or it has been addressed somewhere else (please forward a link to me then, Thanks.). Anyway I have been confused a lot by this–&gt;</p>
<p>In the class vtkMRMLScen, the following methods:<br>
GetNodes()<br>
GetNodesByClass(…)<br>
GetNodesByClassByName(…, …)<br>
GetNodesByName(…)<br>
return “<strong>vtkCollection</strong>”, while the following methods:<br>
GetNodeByID(…)<br>
GetNthNode(…)<br>
GetNthNodeByClass(…, …)<br>
retrun “<strong>vtkMRMLNode</strong>”.</p>
<p>So would you please get me any explanation ? is there a way to get converted to each other?  Thanks a lot in advance.<br>
Best,<br>
Aiden</p>

---

## Post #2 by @Sam_Horvath (2019-08-30 22:15 UTC)

<p>A vtkCollection is just a list of vtk objects. See: <a href="https://vtk.org/doc/nightly/html/classvtkCollection.html" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkCollection.html</a></p>
<p>A vtkMRMLNode is a subclass of vtkObject, and so can be stored in a vtkCollection. You can access the members of a collection through a variety of functions (by index, iterating, etc).  Example in C++ of accessing an object at index <code>i</code> as a vtkMRMLNode:</p>
<p><code>vtkMRMLNode * node = vtkMRMLNode::SafeDownCast(collection-&gt;GetItemAsObject(i))</code></p>
<p>The tests for this class should give a good example of how to iterate through a collection.<br>
C++: <a href="https://vtk.org/gitweb?p=VTK.git;a=blob;f=Common/Core/Testing/Cxx/TestCollection.cxx" rel="nofollow noopener">https://vtk.org/gitweb?p=VTK.git;a=blob;f=Common/Core/Testing/Cxx/TestCollection.cxx</a><br>
Python: <a href="https://vtk.org/gitweb?p=VTK.git;a=blob;f=Common/Core/Testing/Python/TestIterateCollection.py" rel="nofollow noopener">https://vtk.org/gitweb?p=VTK.git;a=blob;f=Common/Core/Testing/Python/TestIterateCollection.py</a></p>

---

## Post #3 by @lassoan (2019-08-30 22:53 UTC)

<p>What would you like to do?</p>
<p>There are helper functions, such as <code>slicer.util getNodesByClass</code> that returns nodes in a Python list instead of a VTK collection.</p>
<p>You can also convert a <code>vtkCollection</code> to a Python list by using <code>list()</code>:</p>
<pre><code>allNodesAsPythonList = list(slicer.mrmlScene.GetNodes())</code></pre>

---

## Post #4 by @aiden.zhu (2019-09-02 15:24 UTC)

<p>Thanks a lot. That works me out of this puzzle.</p>

---

## Post #5 by @aiden.zhu (2019-09-02 15:26 UTC)

<p>Thanks a lot.<br>
I was confused/puzzled by these similar methods/functions which have almost same-type names but return different types. I was always lost while I tried to use one or another such method function.</p>

---
