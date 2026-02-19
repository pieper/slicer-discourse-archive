---
topic_id: 18468
title: "Get Individual Control Point From A Combobox In A Scripted M"
date: 2021-07-01
url: https://discourse.slicer.org/t/18468
---

# Get individual control point from a combobox in a scripted module

**Topic ID**: 18468
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/get-individual-control-point-from-a-combobox-in-a-scripted-module/18468

---

## Post #1 by @Yihao_Liu (2021-07-01 20:25 UTC)

<p>How to select an individual control point from a combobox?</p>
<p>I attempted to do this by a qMRMLNodeComboBox, with its node type as “vtkMRMLMarkupsFiducialNode”. This can only allow selecting a node which contains multiple control points (or fiducials, I am not sure what to call it in Slicer’s term). Looking at the documentation, I don’t think there is a node type “vtkControlPoint” or something like this. <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayableNode.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkMRMLDisplayableNode Class Reference</a></p>

---

## Post #2 by @lassoan (2021-07-02 03:44 UTC)

<p>You can use the <a href="http://apidocs.slicer.org/master/classqSlicerSimpleMarkupsWidget.html">qSlicerSimpleMarkupsWidget</a> to show a list of markup control points that the user can choose from. If you don’t need a node selector or adjust options then you can hide those parts.</p>
<pre data-code-wrap="python"><code class="lang-python">w = slicer.qSlicerSimpleMarkupsWidget()
w.setMRMLScene(slicer.mrmlScene)
w.setCurrentNode(getNode('F'))
w.setNodeSelectorVisible(False)
w.setOptionsVisible(False)
w.show()
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64d2567fbe6de4381a8cbbcdbcdc26d4caad887a.png" alt="image" data-base62-sha1="enUoq6JLKnsQ8UsQIjn9blMyEu6" width="578" height="175"></p>

---

## Post #3 by @Yihao_Liu (2021-07-02 17:49 UTC)

<p>Thanks for the answer. I am using qSlicerSimpleMarkupsWidget as a display of the individual control points, but in addition to this, I also wanted to have an option where the user can select a point and get the coordinate in the backend (in the scripted module code), for some other processing.</p>
<p>I wonder what do you mean by “… the user can choose from”? Does it mean when the user click on the list, once one control point is highlighted as shown in your picture, it can be received in the backend?</p>
<p>One possible solution I am trying is to just have a generic combobox, and list a bunch of numbers to the total number of the elements in the markup array, but obviously this is not very “elegant”, as people may say…</p>

---

## Post #4 by @lassoan (2021-07-02 18:16 UTC)

<p>You can connect the <a href="http://apidocs.slicer.org/master/classqSlicerSimpleMarkupsWidget.html#ac00084bd475a818296ca3a92b2922841">currentMarkupsControlPointSelectionChanged</a> signal to a function in your module widget class to get notified when the user selects a control point.</p>

---

## Post #5 by @Yihao_Liu (2021-07-02 18:19 UTC)

<p>I see! Thanks a lot!</p>

---
