---
topic_id: 33233
title: "Python Script To Create An Empty Time Sequence List"
date: 2023-12-05
url: https://discourse.slicer.org/t/33233
---

# Python script to create an empty time sequence list

**Topic ID**: 33233
**Date**: 2023-12-05
**URL**: https://discourse.slicer.org/t/python-script-to-create-an-empty-time-sequence-list/33233

---

## Post #1 by @admarques (2023-12-05 14:47 UTC)

<p>I’m working with a CT image dataset containing different time phases.<br>
I would like to write a Python script to create an empty time sequence list as a placeholder to have these pre-created lists with specific names and fill them by selecting points in the interface.</p>
<p>My current code is:</p>
<blockquote>
<p>emptyFiducialNode = slicer.vtkMRMLMarkupsFiducialNode()<br>
emptyFiducialNode.SetName(“TSPlF”)<br>
slicer.mrmlScene.AddNode(emptyFiducialNode)</p>
<p>sequenceNode = slicer.vtkMRMLSequenceNode()<br>
sequenceNode.SetName(“FS”)<br>
sequenceNode.CreateNodeInstance()<br>
slicer.mrmlScene.AddNode(sequenceNode)</p>
<p>sequenceBrowserNode = slicer.vtkMRMLSequenceBrowserNode()<br>
sequenceBrowserNode.SetName(“FSBrowser”)<br>
slicer.mrmlScene.AddNode(sequenceBrowserNode)<br>
sequenceBrowserNode.AddProxyNode(emptyFiducialNode, sequenceNode, True)</p>
<p>sequenceBrowserNode.SetAndObserveMasterSequenceNodeID(sequenceNode.GetID())<br>
sequenceBrowserNode.SetOverwriteProxyName(sequenceNode, True)<br>
sequenceBrowserNode.SetPlayback(sequenceNode, True)<br>
sequenceBrowserNode.SetRecording(sequenceNode, True)<br>
sequenceBrowserNode.SetSaveChanges(sequenceNode, True)</p>
</blockquote>
<p>With this code, I’m seeing in the 3Dslicer interface 3 Points Lists:<br>
FS [time=0s]<br>
TSPIF<br>
FS [time0s]</p>
<p>However, none of them make a distinction between times. For example,  one point inserted at time 0 will appear selected at all other times. Moreover, I only want one list appearing in the interface instead of this repeated one.</p>
<p>Is it possible to achieve this behavior through a Python script?</p>

---
