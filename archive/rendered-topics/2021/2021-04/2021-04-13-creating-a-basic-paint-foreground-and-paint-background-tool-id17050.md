# Creating a basic Paint Foreground and Paint Background Tool

**Topic ID**: 17050
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/creating-a-basic-paint-foreground-and-paint-background-tool/17050

---

## Post #1 by @masadcv (2021-04-13 00:06 UTC)

<p>Hi,<br>
I am new to 3D Slicer.<br>
I am trying to implement an interactive segmentation tool for correcting issues in existing segmentation labels. The expected behaviour of this tool is to have “background” and “foreground” paint brushes, so any issues in existing segmentation labels can be corrected by painting over the viewed data.</p>
<p>What I intend to implement is a basic extension that provides two buttons (one for background and another for foreground). When foreground is selected, the paint tool should paint in a specific color (e.g. green). For background the paint tool should paint a different color (e.g. red). In the python script I will access the masks for each and save for corrected label processing through a logic.</p>
<p>I have looked around and into the Segment Editor Widget. However I am unsure about what is the best way to implement a simple gui that can allow user to switch between foreground/background paints (and corresponding segmentation layers), while still providing the ability to click and interact with the data.</p>
<p>I would be very grateful if you can provide with any material that can help me in implementing the above flow. Many thanks!</p>

---

## Post #2 by @pieper (2021-04-13 17:36 UTC)

<p>Hi -</p>
<p>If I understand your goal right it may already be available via the ‘w’ key, that cycles through the segments.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html?highlight=shortcuts#keyboard-shortcuts" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html?highlight=shortcuts#keyboard-shortcuts</a></p>

---

## Post #3 by @lassoan (2021-04-14 04:25 UTC)

<p>For correcting segmentations, you may also find useful the “Color smudge” option in Paint effect. When enabled, clicking on any segment and dragging it into an empty region or into another segment will overwrite that region with the selected segment.</p>

---

## Post #4 by @masadcv (2021-04-14 12:22 UTC)

<p>Hi Andras,<br>
Many thanks! Do you have any guidance/example on how I can include just the two tools (Paint and Smudge) in my own extension? As I will always be painting  foreground and background, it be would be great to hide this in extension and always initialize to have foreground/background layers to paint in. I need to implement this as a separate extension from the Segmentation Effect extension as the goal of my project is to eventually send the painted regions to a research framework (which will be used to correct the original labels). However as a starting point I need to have this in an extension and have the foreground and background paint accessible so we can then send them to the research algorithm.</p>

---

## Post #5 by @masadcv (2021-04-14 12:25 UTC)

<p>Hi Pieper,<br>
Many thanks for providing this. Is there a way I can include the “Paint” (or selected effects) only in my own extension? I need to implement a separate extension from Segment Editor Effects as this user interaction then needs to be send to a research framework for correcting the labels. I would appreciate if you can point me to a simple example that uses Segment Editor widget in similar application.</p>

---

## Post #6 by @lassoan (2021-04-14 14:53 UTC)

<p>You can put a segment editor widget into your own module GUI and this widget is highly customizable. You can choose which effects to show, etc. If you really want just a smudge brush then probably the best is to hide the segment editor widget and just put a few buttons on your module GUI that control the hidden widget.</p>

---

## Post #7 by @masadcv (2021-04-15 23:23 UTC)

<p>Many thanks Andras. This is very helpful for me.</p>
<p>I understand now how to do this. Using the example from here: <a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5" class="inline-onebox" rel="noopener nofollow ugc">This example demonstrates how to do segment brain tumor using Nvidia's AI-assisted annotation tool in batch mode (without GUI, using qMRMLSegmentEditorWidget) using 3D Slicer · GitHub</a>, I have changed it to allow painting and adding two segmentation layers.</p>
<pre><code class="lang-auto"># Create segmentation node to store the segmentation result
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
# add foreground
segmentationNode.GetSegmentation().AddEmptySegment()
# add background
segmentationNode.GetSegmentation().AddEmptySegment()

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

segmentEditorWidget.setActiveEffectByName("Paint")
effect = segmentEditorWidget.activeEffect()
</code></pre>
<p>I have three questions regarding this. How can I switch between the two layers? Is there a function call to do the same as pressing ‘w’ in the Segmentation Editor?<br>
Secondly, how I can change the size of Paint brush?<br>
Third, once I am done - how can I extract the foreground and background masks?</p>

---

## Post #8 by @lassoan (2021-04-16 03:54 UTC)

<aside class="quote no-group" data-username="masadcv" data-post="7" data-topic="17050">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/masadcv/48/10632_2.png" class="avatar"> masadcv:</div>
<blockquote>
<p>How can I switch between the two layers?</p>
</blockquote>
</aside>
<p>You can use <a href="http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a1537f275ab7571d8b330dfb5afdfe5ed">setCurrentSegmentID</a> method.</p>
<aside class="quote no-group" data-username="masadcv" data-post="7" data-topic="17050">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/masadcv/48/10632_2.png" class="avatar"> masadcv:</div>
<blockquote>
<p>how I can change the size of Paint brush?</p>
</blockquote>
</aside>
<p>See parameters of paint effect <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#paint-effect-and-erase-effect">here</a>.</p>
<aside class="quote no-group" data-username="masadcv" data-post="7" data-topic="17050">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/masadcv/48/10632_2.png" class="avatar"> masadcv:</div>
<blockquote>
<p>how can I extract the foreground and background masks?</p>
</blockquote>
</aside>
<p>You can convert segmentation to various other nodes as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">examples in the script repository</a>.</p>

---
