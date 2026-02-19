---
topic_id: 10156
title: "Segment Editor Repetitive Function"
date: 2020-02-07
url: https://discourse.slicer.org/t/10156
---

# Segment Editor - Repetitive function

**Topic ID**: 10156
**Date**: 2020-02-07
**URL**: https://discourse.slicer.org/t/segment-editor-repetitive-function/10156

---

## Post #1 by @manjula (2020-02-07 14:16 UTC)

<p>It would be great if we can determine the number of times the same effect is applied.</p>
<p>For example,</p>
<p>If i want to grow the margin by 5 mm and if my computer processing power is not enough to grow it by 5 mm at the same time but it can grow it by 1 mm at a time, rather than i having to manually do the function 5 times it would be good if we can control how many times it is applied on the segment one after the other.</p>
<p>This will make it possible for lower end computers to do the processing when it comes to large data sets.</p>

---

## Post #2 by @lassoan (2020-02-07 14:29 UTC)

<p>Repeating an effect should not be necessary in general. Repeating an effect many times sometimes also results in less accurate results than running the effect once, with modified parameters (e.g., margin effect 5x with 1mm kernel is not as accurate as margin effect 1x 5mm kernel).</p>
<p>If repeating an effect many times is needed for a very particular workflow then it can be scripted as part of that workflow.</p>
<p>If repeating an effect could be useful in many workflows then we would add that as an option to that specific effect’s GUI.</p>
<p>For Margin and Hollow effect performance issue we already have a fast and accurate solution that will be released soon.</p>

---

## Post #4 by @Juicy (2020-02-09 09:24 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a> as loassan said running the effect lots of times may cause inaccuracies but if you have to do it because of computer power then you could try this script, it worked ok for me. Once the margin effect has run a few times (amount chosen by you) it will print out the total amount that the segment has grown by.</p>
<p>You will need to make some changes to the code for it to work for you including:</p>
<ol>
<li>Set how much you want the segment to grow per iteration (change growSize variable)</li>
<li>Set how many interations or how many times you want the effect to run (change nOfIterations variable)</li>
<li>Change the volume getNode line to include the title or MRML ID of the volume you are using for the segmentation.</li>
<li>Change the segmentation node getNode line to include the title or MRML ID of the segment node you wish to grow.</li>
<li>Change the getSegment line to the title of the actual segment you wish to grow within that segmentation node.</li>
</ol>
<p>I have added # comments by the lines which you need to change.</p>
<p>Hopefully this works for you,</p>
<pre><code>growSize = 0.5 # set how much you want to grow the segment per iteration here
nOfIterations = 4 # set how many times you want to run the effect here

volume = getNode('vtkMRMLScalarVolumeNode1') # put the name of the main volume here

# get the segmentation node
segmentationNode = getNode('vtkMRMLSegmentationNode1') # put the name of the segment node here
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume)
segmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1') # put the name of the segment here


# setup temporary segment editor widget
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(volume)
segmentEditorNode.SetSelectedSegmentID(segmentID)

# set active effect to 'Margin' and set margin size
segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MarginSizeMm", str(growSize))

totalGrowth = 0

# run the effect several times using a loop
for i in range(nOfIterations):
  effect.self().onApply()
  totalGrowth += growSize

print('The Segment Has Successfully Grown by ' + str(totalGrowth) + 'mm')

# delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)
#</code></pre>

---

## Post #5 by @manjula (2020-02-09 10:35 UTC)

<p>Dear <a class="mention" href="/u/juicy">@Juicy</a> many many thanks for the script and this is extremley useful and  it works as intended for the first segment.</p>
<p>However when i add the next segment and run the script  the second segment gets overridden.</p>
<div class="lazyYT" data-youtube-id="e6_wEDTA5RM" data-youtube-title="out 7" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If i move the segment two above the segment one then the segment two grows but segment one is altered. I guess this has to do with default masking settings of the margin effect.</p>
<p>So i guess we need to modify the masking settings. Can you please teach me how to modify the masking settings ?<br>
thank you for the help.</p>

---

## Post #6 by @Juicy (2020-02-09 23:18 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a> I think I have figured out why it overwrites the other segment. If you change the ‘Modify other segments’ setting to ‘Allow overlap’ in the masking settings area down the bottom of segment editor then the other segment is not overwritten.</p>
<p>It took me a while to figure out how to change this setting in python but I can across <a href="https://discourse.slicer.org/t/how-can-i-set-masking-settings-on-a-segment-editor-effect-in-python/4406">this post</a> which describes how to change the masking settings. So I have added the line segmentEditorNode.SetOverwriteMode(2) which I think changes the ‘Modify other segments’ setting to ‘Allow overlap’.</p>
<p>It worked on my computer. Hopefully it is ok for you. Updated code below.</p>
<pre><code>growSize = 0.5 # set how much you want to grow the segment per iteration here
nOfIterations = 4 # set how many times you want to run the effect here

volume = getNode('vtkMRMLScalarVolumeNode1') # put the name of the main volume here

# get the segmentation node
segmentationNode = getNode('vtkMRMLSegmentationNode1') # put the name of the segment node here
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume)
segmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1') # put the name of the segment here


# setup temporary segment editor widget
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(volume)
segmentEditorNode.SetSelectedSegmentID(segmentID)
segmentEditorNode.SetOverwriteMode(2)

# set active effect to 'Margin' and set margin size
segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MarginSizeMm", str(growSize))

totalGrowth = 0

# run the effect several times using a loop
for i in range(nOfIterations):
  effect.self().onApply()
  totalGrowth += growSize

# delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

print('The Segment Has Successfully Grown by ' + str(totalGrowth) + 'mm')
#</code></pre>

---

## Post #7 by @manjula (2020-02-09 23:24 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="6" data-topic="10156">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>segmentEditorWidget.setMRMLScene(slicer.mrmlScene)</p>
</blockquote>
</aside>
<p>Thank you once again for taking time on this… yes now it works great and this will solve the problem while we look for a better PC or wait for the pull request as Prof Lasso get materialized. !!!</p>

---

## Post #8 by @lassoan (2020-02-10 01:02 UTC)

<p>Integer values are not self-explaining (and they may change in the future), so use these enumerated values instead:</p>
<ul>
<li><code>segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteAllSegments)</code></li>
<li><code>segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteVisibleSegments)</code></li>
<li><code>segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)</code></li>
</ul>

---
