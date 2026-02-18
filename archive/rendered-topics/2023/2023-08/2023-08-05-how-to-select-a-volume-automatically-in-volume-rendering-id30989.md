# How to select a volume automatically in volume rendering?

**Topic ID**: 30989
**Date**: 2023-08-05
**URL**: https://discourse.slicer.org/t/how-to-select-a-volume-automatically-in-volume-rendering/30989

---

## Post #1 by @telomere (2023-08-05 02:47 UTC)

<p>Hi, I’m making some script to make my work faster.</p>
<p>I made a simple shortcut button that just goes to volume rendering.</p>
<p>When it changes to volume rendering module, no volume is selected as a default(even when some volumes are loaded in data)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfde6453a14ae2ed86cb110da6af46f2649b6085.png" alt="image" data-base62-sha1="rnlFuOsahDlX4Qf80HYaJ1TaMqV" width="491" height="32"></p>
<p>I want to make a code that switches to volume rendering and select volumes that I want(like first-loaded volume, second-loaded volume…etc).<br>
Making a button for switching was simple but selecting some volume as a default is not solved…</p>
<p>Any help appreciating. Thanks.</p>

---

## Post #2 by @muratmaga (2023-08-05 15:25 UTC)

<p>You can probably write a little function that will cycle over the loaded volumes in the scene after a keystroke. In each iteration you can turn off the previous volume and turn on the next one,</p>
<p>Otherwise I am not sure how can rendering will know what volume you want to render automatically.</p>

---

## Post #3 by @lassoan (2023-08-06 23:11 UTC)

<p>After you switched to a module, you can use <code>setEditedNode</code> to select what node the module should display.</p>
<p>For example:</p>
<pre><code class="lang-python">myModuleWidget = slicer.modules.mymodule.widgetRepresentation()
myVolume = slicer.util.getNode('myVolume')
myModuleWidget.setEditedNode(myVolume)
</code></pre>

---

## Post #4 by @telomere (2023-08-07 00:11 UTC)

<p>Thanks!<br>
I solved my problem with the code below:</p>
<pre><code class="lang-python">volumeNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLScalarVolumeNode')
secondVolumeNode = volumeNodes.GetItemAsObject(1)
vrWidget = slicer.modules.volumerendering.widgetRepresentation()
vrWidget.setMRMLVolumeNode(secondVolumeNode)
</code></pre>
<p>With this, second loaded volume is selected in Volume Rendering combobox if I want to load second-loaded volume among several loaded volume.</p>
<p>Please help one more!(Maybe not one…but…)<br>
I made a shortcut to go Segment Editor module and automatically load source volume and add segmentation and segment.<br>
In this situation, I also want to control “specify geometry” button which is next to source volume.<br>
I want to choose ROI that I made previously and set spacing as 0.15mm.<br>
But I never could find the function codes for controlling ‘specify geometry’ <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @lassoan (2023-08-07 08:09 UTC)

<p>Thresholding for sharing the solution that worked for you. I would recommend to use <code>myModuleWidget.setEditedNode(myVolume)</code> method, as that is a higher-level API that works all modules.</p>
<p>Please create a new topic for new questions that are unrelated to this topic.</p>

---
