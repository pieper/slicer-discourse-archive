---
topic_id: 10733
title: "Creating A Sequence Of Volumes With Python"
date: 2020-03-18
url: https://discourse.slicer.org/t/10733
---

# Creating a sequence of volumes with Python

**Topic ID**: 10733
**Date**: 2020-03-18
**URL**: https://discourse.slicer.org/t/creating-a-sequence-of-volumes-with-python/10733

---

## Post #1 by @Dootsiie (2020-03-18 13:19 UTC)

<p>Hi there,</p>
<p>I am fairly new to 3D slicer and am working on an interesting project, however I am stuck at a certain point. I want to create a 3-Dimensional Time Lapse of individual CT scans using a Python script and 3D Slicer. But for some reason, I can’t visualize the sequence in the 3D view.</p>
<p>I have tried the following:</p>
<ul>
<li>loading the volumes in, and using volume rendering to visualize the individual volumes, and placing these visualized volume rendering nodes in a Sequence. When placing the sequence in the sequence browser, I get ‘0’ as output.</li>
</ul>
<blockquote>
<p># Create model node sequence<br>
Sequence = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSequenceNode”)<br>
erycina = slicer.util.loadVolume(slicer.app.slicerHome + “/Scans/result2/vol_000000.tiff”)<br>
node = getNode(‘vol_000000’)<br>
volRenLogic = slicer.modules.volumerendering.logic()<br>
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(node)<br>
Sequence.SetDataNodeAtValue(displayNode, “0”)<br>
slicer.mrmlScene.RemoveNode(node.GetDisplayNode())<br>
slicer.mrmlScene.RemoveNode(node)</p>
<p>erycina = slicer.util.loadVolume(slicer.app.slicerHome + “/Scans/result2_2/vol_000000.tiff”)<br>
node = getNode(‘vol_000000_1’)<br>
volRenLogic = slicer.modules.volumerendering.logic()<br>
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(node)<br>
Sequence.SetDataNodeAtValue(displayNode, “1”)<br>
slicer.mrmlScene.RemoveNode(node.GetDisplayNode())<br>
slicer.mrmlScene.RemoveNode(node)</p>
<p># Create sequence browser node</p>
<p>sequencebrowser = slicer.mrmlScene.AddNode(slicer.vtkMRMLSequenceBrowserNode())<br>
sequencebrowser.AddSynchronizedSequenceNodeID(Sequence.GetID())</p>
<p>ProxyNode = sequencebrowser.GetProxyNode(Sequence)<br>
ProxyNode.SetAndObserveDisplayNodeID(ProxyNode.GetID())</p>
</blockquote>
<ul>
<li>loading the volumes in, and placing them in the Sequence, after which I tried to visualize the Sequence using volume rendering (which is how you visualize the Sequence if you just make it by hand without programming). Similarly, when I try to place the Sequence in a sequence browser, it gives me ‘0’ as output</li>
</ul>
<blockquote>
<p># loading the data</p>
<p>erycina = slicer.util.loadVolume(slicer.app.slicerHome + “/Scans/result2/vol_000000.tiff”)<br>
n1 = getNode(‘vol_000000’)</p>
<p>erycina2= slicer.util.loadVolume(slicer.app.slicerHome + “/Scans/result2_2/vol_000000.tiff”)<br>
n2 = getNode(‘vol_000000_1’)</p>
<p>erycina3= slicer.util.loadVolume(slicer.app.slicerHome + “/Scans/res_na_6/vol_000000.tiff”)<br>
n3 = getNode(‘vol_000000_2’)</p>
<p># creating sequence</p>
<p>SequenceNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSequenceNode’, ‘Sequence’)<br>
SequenceNode.SetDataNodeAtValue(n1, str(0))<br>
SequenceNode.SetDataNodeAtValue(n2, str(1))<br>
SequenceNode.SetDataNodeAtValue(n3, str(2))</p>
<p># Create a sequence browser node for the new merged sequence</p>
<p>SequenceBrowserNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSequenceBrowserNode’, ‘TimeLapseSequence’)<br>
SequenceBrowserNode.AddSynchronizedSequenceNode(SequenceNode)<br>
slicer.modules.sequencebrowser.setToolBarActiveBrowserNode(SequenceBrowserNode)</p>
<p># Show proxy node in slice viewers</p>
<p>ProxyNode = SequenceBrowserNode.GetProxyNode(SequenceNode)<br>
slicer.util.setSliceViewerLayers(background=ProxyNode)</p>
<p># volume rendering</p>
<p>volRenLogic = slicer.modules.volumerendering.logic()<br>
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(SequenceNode)</p>
</blockquote>
<p>Another question I have is, are there any possibilities in saving the created time lapse? Other than screenrecording the made time lapse directly? As it would be super convenient if there is some sort of way to save it as .mpg, instead of having to record it, as I strive for the full automation of this process.<br>
I hope you can help me out with this!</p>

---

## Post #2 by @lassoan (2020-03-18 13:23 UTC)

<p>You don’t need to worry about display nodes (unless you want to modify display properties as you are replaying the animation).</p>
<p>You can save the rendered sequence as a video using Screen Capture module by choosing “Animation mode” -&gt; sequence.</p>

---

## Post #3 by @Dootsiie (2020-03-19 13:43 UTC)

<p>The suggestion how to save the video did work perfectly, thank you.</p>
<p>However, I still have the issue of getting the 3-D view of the sequence using python.<br>
I want to be able to see the volumes of the sequence and want to write this in python, but everything i tried failed.</p>
<p>I did successfully create the sequence and place the volumes in the sequence, but can’t seem to find out how to visualize this in the 3-D view.</p>

---

## Post #4 by @lassoan (2020-03-19 20:35 UTC)

<p>You can find examples of building sequences of volumes and transforms in these modules:</p>
<ul>
<li><a href="https://github.com/SlicerRt/Sequences/blob/master/CropVolumeSequence/CropVolumeSequence.py">https://github.com/SlicerRt/Sequences/blob/master/CropVolumeSequence/CropVolumeSequence.py</a></li>
<li><a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py">https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py</a></li>
</ul>

---
