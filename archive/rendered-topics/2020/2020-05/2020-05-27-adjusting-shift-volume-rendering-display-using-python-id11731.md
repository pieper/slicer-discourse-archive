# Adjusting "Shift" Volume Rendering Display using Python

**Topic ID**: 11731
**Date**: 2020-05-27
**URL**: https://discourse.slicer.org/t/adjusting-shift-volume-rendering-display-using-python/11731

---

## Post #1 by @Dootsiie (2020-05-27 13:32 UTC)

<p>Hi,</p>
<p>I am trying to visualize a volume using Python and volume rendering.<br>
When I render the volume, it is rather dark. I know I can solve this by moving the “Shift” bar under Display in Volume Rendering. Now I tried doing this by using Python, and I used the following code:</p>
<blockquote>
<p>volRenLogic = slicer.modules.volumerendering.logic()<br>
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(node)<br>
layoutManager = slicer.app.layoutManager()<br>
threeDWidget = layoutManager.threeDWidget(0)<br>
threeDView = threeDWidget.threeDView()<br>
threeDView.resetFocalPoint()</p>
<p>volRenWidget = slicer.modules.volumerendering.widgetRepresentation()<br>
volumePropertyNode = displayNode.GetVolumePropertyNode()</p>
<p>volumePropertyNodeWidget = slicer.util.findChild(volRenWidget, ‘VolumePropertyNodeWidget’)<br>
volumePropertyNodeWidget.setMRMLVolumePropertyNode(volumePropertyNode)<br>
volumePropertyNodeWidget.moveAllPoints(x, 0, false)</p>
</blockquote>
<p>It does visualize the volume (which is a CT scan), but when I try to apply the shift change, no visible changes are applied to the visualized volume. It does not matter what i fill in at x, but nothing seems to work, I do not get any Error messages either, it just straight up does not show the changes I made. I have tried searching these forums for a suitable answer, but i did not find anything that would completely solve this issue, and I hope anyone can help me out on this.</p>

---

## Post #2 by @hemmer (2024-05-09 12:38 UTC)

<p>I would also be interested to learn how to do this programmatically, and similarly, centre the volume rendering (as you would with the crosshair icon in the UI).</p>

---

## Post #3 by @mikebind (2024-05-09 15:21 UTC)

<p>Here is how you center the 3D view programmatically: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#center-the-3d-view-on-the-scene" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#center-the-3d-view-on-the-scene</a></p>

---

## Post #4 by @hemmer (2024-05-09 15:27 UTC)

<p>Thanks Mike, that solves the centring problem!</p>

---

## Post #5 by @hemmer (2025-05-09 11:31 UTC)

<p>And the “shift” problem can be solved following here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="3063">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-volume-rendering-preset-using-python/3063/2">How to set volume rendering preset using Python</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi Oliver, 
There have been some improvements since 4.8.1 that makes it easier for us to do this. So if you use the latest nightly, then this is what you can do: 
Easier setup of volume rendering (no need to create the display node and update it from the logic): 
volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)

This is not very clean, because it uses widgets from the volume rendering module, but you can apply a shift li…
  </blockquote>
</aside>


---
