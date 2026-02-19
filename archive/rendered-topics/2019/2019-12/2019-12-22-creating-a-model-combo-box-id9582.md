---
topic_id: 9582
title: "Creating A Model Combo Box"
date: 2019-12-22
url: https://discourse.slicer.org/t/9582
---

# Creating a model combo box

**Topic ID**: 9582
**Date**: 2019-12-22
**URL**: https://discourse.slicer.org/t/creating-a-model-combo-box/9582

---

## Post #1 by @talmazov (2019-12-22 01:25 UTC)

<p>Hey all,<br>
I tried to create a combo box that will list mesh models, which i know fall under the general classification of ModelNode class, like this</p>
<blockquote>
<p>modelNodeSelector = slicer.qMRMLNodeComboBox()<br>
modelNodeSelector.objectName = ‘modelNodeSelector’<br>
modelNodeSelector.toolTip = “Select a model.”<br>
modelNodeSelector.nodeTypes = [‘vtkMRMLModelNode’]<br>
modelNodeSelector.noneEnabled = True<br>
modelNodeSelector.addEnabled = True<br>
modelNodeSelector.removeEnabled = True<br>
self.pathFormLayout.addRow(“Input Model:”, modelNodeSelector)<br>
self.parent.connect(‘mrmlSceneChanged(vtkMRMLScene*)’, modelNodeSelector, ‘setMRMLScene(vtkMRMLScene*)’)</p>
</blockquote>
<p>however the UI is grayed out and i cannot select anything. i suspect it has something to do with specifying the nodeTypes but im not sure. I have imported an STL model into the scene and it is visible in the Models viewer.</p>

---

## Post #2 by @lassoan (2019-12-22 02:18 UTC)

<p>You need to set the MRML scene. I’m not sure that the parent connection that you are trying to use to set the scene is working. In scripted modules we usually set the scene using set method instead.</p>
<p>Note that manual widget creation is not recommended since you can now use a visual editor (Qt Designer) that is bundled with Slicer. It results in much less code, nicer look, with less development effort. See detailed tutorial here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---
