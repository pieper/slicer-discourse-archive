---
topic_id: 2741
title: "Automating Segmentation On Volumes"
date: 2018-04-30
url: https://discourse.slicer.org/t/2741
---

# Automating segmentation on volumes

**Topic ID**: 2741
**Date**: 2018-04-30
**URL**: https://discourse.slicer.org/t/automating-segmentation-on-volumes/2741

---

## Post #1 by @slojanko (2018-04-30 20:44 UTC)

<p>Hello,</p>
<p>I’ve started using Slicer a few weeks ago for a University project. It’s about segmenting the volume of a cell with a predefined (known parameters) threshold, smoothing, removing small islands and margin increase procedure.<br>
My input is a set of 80 folders, each containing 256 images (named imgXYZ.png).<br>
I’ve searched a couple of websites and youtube videos on achieving this but failed to get further than importing the set of images that build a 256x256x256 cube with:<br>
[success, loadedVolumeNode] = slicer.util.loadVolume("[success, loadedVolumeNode] = slicer.util.loadVolume(“path/fib1000/img001.png”, returnNode=True)", returnNode=True)<br>
and then creating the segmentation “node” with:<br>
seg = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’, ‘Segment’)</p>
<p>Despite not getting further than this I was also trying to access the Name variable of the loadedVolumeNode with print(loadedVolumeNode.GetAttribute(“Name”)) with a simple None as the result.</p>
<p>I am in no way fluent in Python as I’ve first used it when trying to create a script for Slicer (which was last week), so if someone could please point me in the right direction I’d be very grateful.</p>
<p>Janko</p>
<p>PS: If this is in the wrong forum, could it be moved into the correct one.</p>

---

## Post #2 by @muratmaga (2018-04-30 21:04 UTC)

<p>Can you do what you want to do manually using the segment editor (without resorting the scripts) as a test first?</p>
<p>Slicer reads PNG stacks as a vector volume. I am not sure if segment editor works with vector volumes, you may have to convert to a scalar first.</p>
<p>Mail](<a href="https://go.microsoft.com/fwlink/?LinkId=550986" rel="nofollow noopener">https://go.microsoft.com/fwlink/?LinkId=550986</a>) for Windows 10</p>

---

## Post #3 by @slojanko (2018-04-30 21:34 UTC)

<p>I can do it manually, but I would have to do it for 80 subvolumes which were extracted from the master volume. I would also like to specify the segmentations parameters, for example: try all combinations of Threshold Range starting at [0, 20] and ending at [25, 40], which removes doing it by hand as an option.</p>
<p>The segment editor works fine when importing the volume through File -&gt; Add Data -&gt; Select first image (001) -&gt; untick Single File.</p>
<p>The whole process would look like: Load a folder of images, create a segmentation node and apply the volume to it, apply threshold with specified range, apply smoothing, remove small islands, apply margin increase and finally save the segmentation to a file. This would preferably be repeated X times while not crashing for out of memory.</p>
<p>I’m guessing there are functions for this but I either cannot find them or can’t figure out how to call them properly, I’m constantly getting errors or None, when printing something.</p>

---

## Post #4 by @lassoan (2018-05-01 04:17 UTC)

<p>There are complete examples of automating segmentation by Python scripting, which should be quite close to what you need: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #5 by @slojanko (2018-05-03 21:12 UTC)

<p>Hello,</p>
<p>I’m following this example:<br>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9</a></h4>
<h5>ExtractSkin.py</h5>
<pre><code class="Python">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")
</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>and got stuck after the following commands were entered:</p>
<p>// Load Volume consisting of png images<br>
[success, loadedVolumeNode] = slicer.util.loadVolume(“C:/Users/Janko/Desktop/RVP_LGM/MatLabIMG/fib1000/img001.png”, returnNode=True)</p>
<p>// Create segmentation node<br>
segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”, “SegmentationOfVolume”)</p>
<p>// Only needed for display? What does this mean<br>
segmentationNode.CreateDefaultDisplayNodes()</p>
<p>// Set volume of segmentation to loaded volume<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(loadedVolumeNode)</p>
<p>// Create new segment - this is where the effects will be applied to<br>
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(“mitochondrium”)</p>
<p>// Create segment editor to get access to effects<br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(loadedVolumeNode)</p>
<p>It is a copy paste up to right before an effect is created, with only some names changed to suit my case.<br>
After running the last function, the segment editor doesn’t get its Master Volume assigned to the loadedVolumeNode so I’m wondering if I’m doing something wrong.<br>
I’m running the 4.9.0, 4. 17 edition of Slicer.</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2018-05-03 22:25 UTC)

<p>To see the segment editor settings that you’ve set, make your internal segment editor widget visible by calling <code>segmentEditorWidget.show()</code>.</p>

---

## Post #7 by @slojanko (2018-05-04 10:22 UTC)

<p>Thank you.</p>
<p>I’ve got a small problem regarding changing the Margin size for the Margin effect.<br>
I’ve checked the following pages for how the parameter could be called:<br>
<a href="http://apidocs.slicer.org/master/SegmentEditorMarginEffect_8py_source.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/SegmentEditorMarginEffect_8py_source.html</a><br>
<a href="http://apidocs.slicer.org/master/classSegmentEditorMarginEffect_1_1SegmentEditorMarginEffect.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/classSegmentEditorMarginEffect_1_1SegmentEditorMarginEffect.html</a><br>
yet none of the names I’ve tried changed the value of it.</p>
<p>I was also looking for a function that would print all names of parameters but was unsuccessful there as well.<br>
It would be useful because I could also need the parameters for the Islands effect.</p>

---

## Post #8 by @lassoan (2018-05-04 15:58 UTC)

<p>The parameter name is “MarginSizeMm”. What names did you try and what values did you set? Did you see the value updating on the user interface?</p>

---

## Post #9 by @slojanko (2018-05-07 11:40 UTC)

<p>I checked the 2 links I posted above.<br>
Could you please show me where you store the parameter lists for functions? I can’t find the parameter name of the Operation for Margin if I want to change to Grow or Shrink, nor can I find actual value to which I should set the parameter (is it a string “Grow”, is it GROW as a constant).</p>
<p>Thank you,<br>
Janko</p>

---

## Post #10 by @lassoan (2018-05-07 13:18 UTC)

<p>List of all parameters are always listed in <code>setMRMLDefaults</code> method. For the margin effect there is only a single parameter:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/c46fa77daabd5c6d2e641fce72eacb7517788153/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L70-L71" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/c46fa77daabd5c6d2e641fce72eacb7517788153/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L70-L71" target="_blank">Slicer/Slicer/blob/c46fa77daabd5c6d2e641fce72eacb7517788153/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L70-L71</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="70" style="counter-reset: li-counter 69 ;">
<li>def setMRMLDefaults(self):</li>
<li>  self.scriptedEffect.setParameterDefault("MarginSizeMm", 3)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Sign of margin size defines grow/shrink. Positive value means growing, negative value means shrinking.</p>

---

## Post #11 by @slojanko (2018-05-07 18:24 UTC)

<p>Thank you,<br>
I was able to find the parameters for the Islands Segment effect.</p>

---

## Post #12 by @slojanko (2018-05-08 18:00 UTC)

<p>Hello,</p>
<p>is there any way to find exactly what I’m not deleting when closing Slicer? I have a memory leak with the following message:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e930828068867754c313a01834115f4288b7c62.png" alt="image" data-base62-sha1="24VHkygJzFGR7b9ISqv3aPceSUa" width="370" height="110"></p>
<pre><code># Load Volume consisting of png images
[success, loadedVolumeNode] = slicer.util.loadVolume("C:/Users/Janko/Desktop/RVP_LGM/MatLabIMG/fib1000/img001.png", returnNode=True)

# Create segmentation node
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", "SegmentationOfVolume")

# Only needed for display? What does this mean
segmentationNode.CreateDefaultDisplayNodes()

# Set volume of segmentation to loaded volume 
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(loadedVolumeNode)

# Create new segment - this is where the effects will be applied to
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("mitochondrium")

# Create segment editor to get access to effects, literally creates a new Segment Editor window
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(loadedVolumeNode)

# Shows the new Segment Editor window
segmentEditorWidget.show()

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","1")
effect.setParameter("MaximumThreshold","110")
effect.self().onApply()

# Smoothing
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MEDIAN")
effect.setParameter("KernelSizeMm", 7)
effect.self().onApply()

# Islands
segmentEditorWidget.setActiveEffectByName("Islands")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Operation", "REMOVE_SMALL_ISLANDS")
effect.setParameter("MinimumSize", 500)
effect.self().onApply()

# Margin
segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MarginSizeMm", 7)
effect.self().onApply()

segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Write to .seg.nrrd file (.seg required for Slicer to detect it's a segmentation file)
myNode = slicer.util.getNode("SegmentationOfVolume")
myStorageNode = myNode.CreateDefaultStorageNode()
myStorageNode.SetFileName("C:/Users/Janko/Desktop//RVP_LGM/SlicerOutput/"+"fib1000"+".seg.nrrd")
myStorageNode.WriteData(myNode)

slicer.mrmlScene.Clear(0)
</code></pre>
<p>This is my entire code before running a loop that’ll iterate through all 80 volumes and I was hoping the Clear() function would clear all memory allocations, but I am not freeing something. I was hoping to get to a clean start and repeat the process again without running out of memory. I know I could keep some declarations and just change the input to it (like volume for segmentation) but my first goal would be to remove all leaks.<br>
I tried running the code 4x and got the following memory usage from Task manager:<br>
167.3MB<br>
213.2MB<br>
217.9MB<br>
218.4MB<br>
which shows a slight increase in usage each time.</p>
<p>Edit:<br>
I’ve added the following three RemoveNode calls:<br>
slicer.mrmlScene.RemoveNode(myNode)<br>
slicer.mrmlScene.RemoveNode(segmentationNode)<br>
slicer.mrmlScene.RemoveNode(loadedVolumeNode)<br>
which reduces the leaks to: 1, 1, 2, 2 of the same Error.</p>
<p>Janko</p>

---

## Post #13 by @lassoan (2018-05-09 04:05 UTC)

<p>If you clear the scene and delete all Python variables you create then memory usage should return to the initial value. If you have a Python variable that refers to a VTK object then that object will not be deleted until you delete that variable (calling <code>del</code> or letting the variable go out of scope), even if it is a node that you’ve deleted from the scene.</p>
<p>It seems that you leak a storage node. <code>CreateDefaultStorageNode</code> creates a new storage node and sets its reference count of 1 (so that it can be returned as a simple pointer). After you save it in a Python variable, you need to decrement the reference count by calling <code>myStorageNode.UnRegister(None)</code> to indicate that it is now owned by the Python variable. See more details and examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules</a></p>

---

## Post #14 by @slojanko (2018-05-13 12:43 UTC)

<p>Thank you,</p>
<p>I’ve got a bit of a problem loading the segmentation back now, after saving with a StorageNode. The volume information is lost through the process which is something I would like to keep.<br>
Is there a different way to save a segmentation node or am I incorrectly calling something?</p>

---

## Post #15 by @lassoan (2018-05-13 13:13 UTC)

<aside class="quote no-group" data-username="slojanko" data-post="14" data-topic="2741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slojanko/48/1518_2.png" class="avatar"> slojanko:</div>
<blockquote>
<p>The volume information is lost through the process</p>
</blockquote>
</aside>
<p>What do you mean? What did you expect to happen and what happened instead?</p>

---

## Post #16 by @slojanko (2018-05-13 16:31 UTC)

<p>When I load a saved segmentation node and try loading it back, it does not remember the Master volume for it.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f7288d2570fce9dd5bc6ba977aad84ab2753267.png" alt="image" data-base62-sha1="6LJPsKhL9mr8eRUGr3DsS34OLfV" width="519" height="49"><br>
Should I be saving the entire mrml scene, or is there a way to store aditional info about the volume location on my disk?</p>

---

## Post #17 by @lassoan (2018-05-14 02:38 UTC)

<p>Correct. Saved segmentation and master volume files are saved independently and do not refer to each other. In the scene file we store Segment editor settings, which includes reference to the segmentation node and master volume node.</p>

---

## Post #18 by @apparrilla (2019-12-30 15:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="2741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Sign of margin size defines grow/shrink. Positive value means growing, negative value means shrinking.</p>
</blockquote>
</aside>
<p>I´m in trouble with “Margin” effect, <a class="mention" href="/u/lassoan">@lassoan</a> . This is my code:</p>
<blockquote>
<p>segmentEditorWidget.setActiveEffectByName(“Margin”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“KernelSizeMm”, -5)<br>
effect.self().onApply()<br>
# Margin (Shrink)<br>
# Sign of margin size defines grow/shrink. Positive value means growing, negative value means shrinking.</p>
</blockquote>
<p>I´ve probed both signs in kernel size (positive or negative) and always is done growing effect. What I´m doing wrong?</p>
<p>Thanks</p>

---

## Post #19 by @lassoan (2019-12-30 15:20 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="18" data-topic="2741">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>effect.setParameter(“KernelSizeMm”, -5)</p>
</blockquote>
</aside>
<p>The correct parameter name is <code>MarginSizeMm</code> - see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorMarginEffect.py#L71">source code</a>.</p>

---

## Post #20 by @apparrilla (2019-12-30 16:36 UTC)

<p>Right…Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
