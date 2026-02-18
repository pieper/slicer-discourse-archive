# Get the current volume node rendered in the Red Yellow Green view

**Topic ID**: 9190
**Date**: 2019-11-18
**URL**: https://discourse.slicer.org/t/get-the-current-volume-node-rendered-in-the-red-yellow-green-view/9190

---

## Post #1 by @CreepyTrick (2019-11-18 13:08 UTC)

<p>Hello</p>
<p>I’m trying to get the current volume rendered in the RYG views (from a Dicom).<br>
On the screen, i have 2 volume:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e24a8c3fda2e45d6d022feb26ba994341d76fcf0.png" alt="image" data-base62-sha1="whRCPHdRsnk1BufLEpH7xXhleAU" width="597" height="217"></p>
<p>For now, i already got all the vtkMRMLScalarVolumeNode in a VtkCollection, but i cannot find a way to get witch one is visible on the RYG.<br>
Since we cannot set visible multiple volumes, i try a basic solution:</p>
<pre><code class="lang-auto">#currentNode is a vtkMRMLScalarVolumeNode
currentNode.GetScalarVolumeDisplayNode().GetDisplayableNode().GetDisplayVisibility()
</code></pre>
<p>I expected this to return “1” for the volume rendered in the scene, 0 for all others, but it always return 1.</p>
<p>Does anyone have a solution ?</p>

---

## Post #2 by @Amine (2019-11-18 13:25 UTC)

<p>Hi, you can use this to set a volume as background<br>
<code>slicer.util.setSliceViewerLayers(background=currentNode)</code><br>
Edit: i misread you want to get the displayed one</p>

---

## Post #3 by @CreepyTrick (2019-11-18 13:41 UTC)

<p>Hi,</p>
<p>This is not what i want<br>
The result expected is something like (pseudo code)<br>
<code>currentNodeRenderedInTheRYGViews = slicer.util.getFocusedVolume()</code></p>
<p>or</p>
<pre><code class="lang-auto">for all scalarVolumeNode
  if(node.isDisplayed)
    return node
</code></pre>
<p>For now i just got the list of all scalarVolumes (red circle on the screen), but only one of them is displayed in these view, the one i want.</p>
<p>“Edit” Yes, that’s it <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #4 by @lassoan (2019-11-18 14:25 UTC)

<p>See this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images">example in the script repository</a> for how to get/set foreground and background volume node in each slice view (you just need to replace Set…Volume… by Get…Volume…):</p>
<pre><code class="lang-python">layoutManager = slicer.app.layoutManager()
for sliceViewName in layoutManager.sliceViewNames():
    compositeNode = layoutManager.sliceWidget(sliceViewName).sliceLogic().GetSliceCompositeNode()
    volumeNodeID = compositeNode.GetBackgroundVolumeID()
    print(sliceViewName + ": " +volumeNodeID)
</code></pre>

---

## Post #5 by @CreepyTrick (2019-11-18 14:39 UTC)

<p>That’s totally what i wanted to do !<br>
I didn’t know that was called “background”, so i dont paid attention to it</p>
<p>Thanks for your help lassoan</p>

---
