# Volume render not working

**Topic ID**: 6283
**Date**: 2019-03-25
**URL**: https://discourse.slicer.org/t/volume-render-not-working/6283

---

## Post #1 by @Amine (2019-03-25 19:52 UTC)

<p>Hello, im running against this issue for the second time now, where volume render would stop working for a certain volume, while still working for the others, Reloading the volume.nrrd file from the save folder  into slicer works just fine, so it seems to be a problem with the scene file. i tried hiding unhiding the volume, deleting all other hiearchy , changing volume rendering window, and transfer functions, the only way to make it work is to reload the volume from the save folder.<br>
I uploaded the problematic scene if anyone could figure whats wrong, Thanks!</p>
<p><a href="https://drive.google.com/open?id=1MdtcZKGNlWJU-cvdBBZ29Ltqw7RVO1qF" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1MdtcZKGNlWJU-cvdBBZ29Ltqw7RVO1qF</a></p>

---

## Post #2 by @lassoan (2019-03-25 20:05 UTC)

<p>Could you please also upload the volume property (.vp) file and annotation ROI node (.acsv)?<br>
Probably the best is if you upload the scene as a single .mrb file (click the package icon in the save dialog).</p>

---

## Post #3 by @Amine (2019-03-25 20:13 UTC)

<p>I removed them to lighten up the folder since none worked, i updated the upload with the mrb file</p>
<p><a href="https://drive.google.com/open?id=1MdtcZKGNlWJU-cvdBBZ29Ltqw7RVO1qF" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1MdtcZKGNlWJU-cvdBBZ29Ltqw7RVO1qF</a></p>

---

## Post #4 by @lassoan (2019-03-25 20:42 UTC)

<p>There are two volume rendering display nodes for the same volume. You can create and manage any number of volume rendering display nodes programmatically, but the user interface always shows the first one.</p>
<p>The problem is that the first display node is invalid (volume node is not set in it), therefore the volume renderer cannot display it.</p>
<p>Have you loaded/imported a scene that was created in a version older than Slicer-4.10.1?</p>

---

## Post #5 by @Amine (2019-03-25 20:58 UTC)

<p>Thanks for your answer, No i did only use slicer 4.10.1 for the whole work. i deleted the two volume render nodes and still no result, any way it could be fixed from the UI ?</p>

---

## Post #6 by @lassoan (2019-03-26 00:02 UTC)

<p>What do you mean you deleted volume rendering nodes? Did you delete nodes before this double volume rendering nodes issue happened? It would be great if you could come up with a list of steps that reproduce the problem.</p>

---

## Post #7 by @lassoan (2019-03-27 14:23 UTC)

<aside class="quote no-group" data-username="Amine" data-post="5" data-topic="6283">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine/48/4844_2.png" class="avatar"> Amine:</div>
<blockquote>
<p>any way it could be fixed from the UI ?</p>
</blockquote>
</aside>
<p>You can copy-paste this code snippet into the Python console to restore link between volume rendering display nodes and volumes:</p>
<pre><code class="lang-auto">for vrDisplayNode in getNodesByClass("vtkMRMLVolumeRenderingDisplayNode"):
  volumeNode=vrDisplayNode.GetDisplayableNode()
  if volumeNode:
    vrDisplayNode.SetAndObserveVolumeNodeID(volumeNode.GetID())
    slicer.modules.volumerendering.logic().UpdateDisplayNodeFromVolumeNode(vrDisplayNode, volumeNode)
</code></pre>

---

## Post #8 by @Amine (2019-03-30 01:31 UTC)

<p>Thanks and sorry for the late reply;<br>
I deleted the volume rendering nodes only after you suggested they could be causing interference, (to try and restore the normal connection) : i went to nodes list and removed volume rendering 1 and volume rendering 3 (not sure if this was the right thing to do)</p>
<p>No i did not mess with nodes before the problem happend, only touched hiearchy, volume render module, and other usual modules (segment editor, crop etc)</p>
<p>This issue happened after hours on a project so i do not have any specific order to reproduce the problem</p>
<p>However the first time it happened it was directly after activating two volume renders on two different viewports, some volumes would not show up just like in this one but also the ones that still work would appear on all viewports even if the visibility tick boxes are changed, again this was non reproducible ( and i discarded the files)<br>
Ps: i did not use multiple 3d view for this second time it happened</p>

---

## Post #9 by @Amine (2019-03-30 01:44 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="6283">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>for vrDisplayNode in getNodesByClass(“vtkMRMLVolumeRenderingDisplayNode”): volumeNode=vrDisplayNode.GetDisplayableNode() if volumeNode: vrDisplayNode.SetAndObserveVolumeNodeID(volumeNode.GetID()) slicer.modules.volumerendering.logic().UpdateDisplayNodeFromVolumeNode(vrDisplayNode, volumeNode)</p>
</blockquote>
</aside>
<p>This worked perfectly. thanks! i hope i could help finding out where did it come from.</p>

---

## Post #10 by @lassoan (2019-03-30 02:19 UTC)

<p>Thanks for the additional information. Probably this part of the code will be revisited when we switch to multi-volume rendering as default rendering method (need to get shading fixed in VTK first).</p>

---
