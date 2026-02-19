---
topic_id: 576
title: "Use A List Of Models In A Cli"
date: 2017-06-26
url: https://discourse.slicer.org/t/576
---

# Use a list of models in a CLI

**Topic ID**: 576
**Date**: 2017-06-26
**URL**: https://discourse.slicer.org/t/use-a-list-of-models-in-a-cli/576

---

## Post #1 by @mirclem (2017-06-26 22:43 UTC)

<p>Hello,</p>
<p>I am trying to create a CLI with a variable number of models as input and only one as output.<br>
First, I tried to use a string-vector but when running some C++ code it doesn’t pass OpenVTKFile() if I use a vtkPolyDataReader or doesn’t pass IsFilePolyData() if I use vtkGenericDataObjectReader().</p>
<p>The second option was to use the geometry tag with the “multiple” attribute set as True, but when I assign a list of nodes to the cli input (via python for example), the list is not propagated to the computation part and I so the C++ code return an error because the list is size 0.</p>
<p>Do you have any idea?</p>

---

## Post #2 by @lassoan (2017-06-27 00:13 UTC)

<p>One approach is to assign a unique scalar value to the points of each polydata (for example, add a “ComponentID” value, it would be 0 for all the points in the first data set, 1 for all points in the second data set, etc) and append all polydata into one, using vtkAppendPolyData filter. In your CLI you can separate components by thresholding.</p>
<p>Another approach is to choose a model hierarchy node. Model hierarchies can be transferred as a “mini-scene”. You’ll get the filename of a scene and the hierarchy node ID (separated by #). You can load the scene from that file, find the hierarchy node by its ID, and get each child node and their polydata. Example CLI module description XML:</p>
<pre><code>&lt;geometry aggregate="true" fileExtensions=".mrml" multiple="true"&gt;
  &lt;name&gt;ModelSceneFileIn&lt;/name&gt;
  &lt;channel&gt;input&lt;/channel&gt;
  &lt;label&gt;Models&lt;/label&gt;
  &lt;longflag&gt;--modelSceneFileIn&lt;/longflag&gt;
  &lt;description&gt;&lt;![CDATA[Some description.]]&gt;&lt;/description&gt;
  &lt;default&gt;models.mrml&lt;/default&gt;
&lt;/geometry&gt;
</code></pre>
<p>There is one trick to this: you have to make sure there is a storage node created for your model nodes (for example, you iterate through all model nodes in the scene and call CreateDefaultStorageNode() method; it is not a problem if you call it multiple times - if the model node already has a storage node then the call will simply have no effect).</p>

---
