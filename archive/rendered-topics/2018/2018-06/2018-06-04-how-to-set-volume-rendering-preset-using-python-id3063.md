# How to set volume rendering preset using Python

**Topic ID**: 3063
**Date**: 2018-06-04
**URL**: https://discourse.slicer.org/t/how-to-set-volume-rendering-preset-using-python/3063

---

## Post #1 by @ollih10 (2018-06-04 07:13 UTC)

<p>Hi developers,</p>
<p>Using a Python script I am trying to load a volume, set the slice views and also a volume rendering preset. While loading and setting the slice views works out well, the volume rendering always shows up with the default settings and not the targeted preset. Could someone please give me a hint of what’s missing? Is there a way to adjust the preset parameter “shift” in advance?<br>
Since I am new to Slicer development I would also be happy about any hint of how to  improve the code (is there something that can be skipped or is there a utitlity function to get similar results easier?). Here is the code I am using:</p>
<pre><code class="lang-auto">fileName = "Image01.IMA"
volume_logic = slicer.modules.volumes.logic()
volume_node = volume_logic.AddArchetypeScalarVolume(fileName, "Volume3D", 2, None)

mrmlLogic = slicer.app.applicationLogic()
selNode = mrmlLogic.GetSelectionNode()
selNode.SetReferenceActiveVolumeID(volume_node.GetID())
mrmlLogic.PropagateVolumeSelection()

logic = slicer.modules.volumerendering.logic()
preset = logic.GetPresetByName('CT-AAA')
preset_node = slicer.mrmlScene.AddNode(preset)
display_node = logic.CreateVolumeRenderingDisplayNode()
slicer.mrmlScene.AddNode(display_node)
logic.UpdateDisplayNodeFromVolumeNode(display_node, volume_node, preset_node)
display_node.SetVisibility(1)
</code></pre>
<p>Thanks in advance and best wishes,<br>
Oliver</p>
<p>Operating system: Win7<br>
Slicer version: 4.8.1</p>

---

## Post #2 by @cpinter (2018-06-04 14:32 UTC)

<p>Hi Oliver,</p>
<p>There have been some improvements since 4.8.1 that makes it easier for us to do this. So if you use the latest nightly, then this is what you can do:</p>
<p>Easier setup of volume rendering (no need to create the display node and update it from the logic):</p>
<pre><code>volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
</code></pre>
<p>This is not very clean, because it uses widgets from the volume rendering module, but you can apply a shift like this:</p>
<pre><code>volRenWidget = slicer.modules.volumerendering.widgetRepresentation()
if volRenWidget is None:
  logging.error('Failed to access volume rendering module')
  return
# Make sure the proper volume property node is set
volumePropertyNode = displayNode.GetVolumePropertyNode()
if volumePropertyNode is None:
  logging.error('Failed to access volume properties')
  return
volumePropertyNodeWidget = slicer.util.findChild(volRenWidget, 'VolumePropertyNodeWidget')
volumePropertyNodeWidget.setMRMLVolumePropertyNode(volumePropertyNode)
# Adjust the transfer function
volumePropertyNodeWidget.moveAllPoints(x, 0, false)
</code></pre>
<p>where ‘x’ is your shift.<br>
It would be probably possible to do this on the MRML/VTK level, but as there are CTK widget calls involved in moveAllPoints, it is not as easy as it should be, and it was not too high on the priority list thus far.</p>
<p>Hope this helps, let us know if you have further questions.</p>

---

## Post #3 by @ollih10 (2018-06-04 15:25 UTC)

<p>Hi Csaba,</p>
<p>thanks for your quick answer. That helps a lot. Do you also have a suggestion of how to set the preset (in the example above ‘CT-AAA’) at first? The code I posted to achieve to set a preset doesn’t work. The volume rendering looks the same as not providing a preset in the call</p>
<p>logic.UpdateDisplayNodeFromVolumeNode(display_node, volume_node, preset_node)</p>
<p>Additionally I have one more question that came up today. When activating the “eye” in the slice views the slice appears in the 3D view. I try to achieve the same behaviour using the following Python lines for the red slice in my code:</p>
<p>display_node = slicer.mrmlScene.GetNodeByID(‘vtkMRMLModelDisplayNode1’)<br>
display_node.VisibilityOn()</p>
<p>Which works for the current red slice position until I change that position by scrolling in the red slice window. The slice in the 3D view immediately disappears. I observed that the “eye” in the red slice window also stays closed after the call above. Any idea what could be the cause?</p>

---

## Post #4 by @lassoan (2018-06-04 15:37 UTC)

<aside class="quote no-group" data-username="ollih10" data-post="3" data-topic="3063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/f1d935/48.png" class="avatar"> ollih10:</div>
<blockquote>
<p>Additionally I have one more question that came up today. When activating the “eye” in the slice views the slice appears in the 3D view.</p>
</blockquote>
</aside>
<p>This is not related to the original question. Could you please post this as a separate topic?</p>

---

## Post #5 by @cpinter (2018-06-04 15:43 UTC)

<p>I think if you copy the properties of the preset node from the private presets scene to the volume property node of your volume then it should do the trick. Something like this:</p>
<pre><code>volumePropertyNode.Copy(preset)</code></pre>

---

## Post #6 by @ollih10 (2018-06-05 06:51 UTC)

<p>Sorry, I’ll setup a new post.</p>

---

## Post #7 by @ollih10 (2018-06-05 07:15 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="3063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)</p>
</blockquote>
</aside>
<p>Works perfect now!<br>
Thanks for your help Csaba</p>

---

## Post #8 by @Yash_Kumar_Gumashta (2019-07-31 09:13 UTC)

<p>Hi Team,</p>
<p>I am using 3D Slicer and Python for the first time and need some help.</p>
<p>What I am trying to do &gt; Open a example dataset in 3D slicer, Change the view to 3D only and then enable volume rendering so that I can see in MR-Default via Python interactor.</p>
<p>Why I am doing this &gt; I want to automate this, So that I can do it on thousands of machines simultaneously and understand the application requirements in terms of CPU, Storage and GPU.</p>
<p>What I have figured out till now &gt;</p>
<p>Opening of Application <span class="hashtag">#Run</span> - Slicer.exe</p>
<p>Ctrl + 3 <span class="hashtag">#Opening</span> Python Interactor</p>
<pre><code>slicer.util.loadVolume("C:\Medical Data\MR-head.nrrd")   #Open the sample data set 
</code></pre>
<p>and after that I am not able to do proceed.</p>
<p>If possible, Please help me with the code or the resources which I can utilize to develop the python script.</p>
<p>-Yash</p>

---

## Post #9 by @lassoan (2019-08-01 04:06 UTC)

<aside class="quote no-group quote-modified" data-username="Yash_Kumar_Gumashta" data-post="8" data-topic="3063">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yash_kumar_gumashta/48/4294_2.png" class="avatar"> Yash_Kumar_Gumashta:</div>
<blockquote>
<p>slicer.util.loadVolume(“C:\Medical Data\MR-head.nrrd”) <span class="hashtag-raw">#Open</span> the sample data set</p>
</blockquote>
</aside>
<p>Since <code>\</code> is an escape character in Python, the file path is incorrect, and so no volume will be loaded. See more details and description of correct syntax <a href="https://discourse.slicer.org/t/load-valume-issue/2400/2">here</a>.</p>

---

## Post #10 by @cpinter (2020-06-17 12:24 UTC)

<p>A post was split to a new topic: <a href="/t/adjust-volume-rendering-transfer-function-in-python/12069">Adjust volume rendering transfer function in Python</a></p>

---
