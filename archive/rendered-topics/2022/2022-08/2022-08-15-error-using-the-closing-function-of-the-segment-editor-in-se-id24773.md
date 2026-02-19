---
topic_id: 24773
title: "Error Using The Closing Function Of The Segment Editor In Se"
date: 2022-08-15
url: https://discourse.slicer.org/t/24773
---

# Error using the closing function of the segment editor in semi-automated segmentation using python

**Topic ID**: 24773
**Date**: 2022-08-15
**URL**: https://discourse.slicer.org/t/error-using-the-closing-function-of-the-segment-editor-in-semi-automated-segmentation-using-python/24773

---

## Post #1 by @FOosterbaan (2022-08-15 19:18 UTC)

<p>Hi all!</p>
<p>I’m fairly new to using slicer so I might have made a mistake somewhere but I keep getting an error while running my script and I can not figure out why. I have written a script to automate part of the segmentation process based on CT scans. As I have a lot of scans to go through I have put several segment editor functions in a double loop that goes over the different scans and segments in python. I have run the program before without any problems but the last few days I keep getting an error without having changed anything. What I don’t understand is that I get an error for a function that doesn’t give a problem the first time(s) it is executed by the script but then it suddenly doesn’t seem to work anymore (sometimes it does go over the loops once or twice before giving the error). I call all segment editor functions in a similar fashion but the part calling the closing function seems to be the only one giving problems.</p>
<p>This is part of the script I wrote, the last line of the ‘Closing gaps’ part is the line that gives the error. After this part it runs a few more segment editor functions and it assigns names to the different segments, but I left that out for now.</p>
<pre><code class="lang-auto">Islands
min_size_islands = 20000
# Closing
cl_kernel_size_mm = 8

# Set range of required images for segmentation 
Numbers = list(range(21,42))

# List of segments for segmentation
Segments = ["Bone", "Bone_2", "Bone_3", "Bone_4", "Bone_5", "Bone_6"]

# PROCESSING
for i in Numbers:
    # Open mrb file
    slicer.util.loadScene(filepath + "SlicerSegmentation_" + str(i) + ".mrb")

    masterVolumeNode = getNode("vtkMRMLScalarVolumeNode" + str(i-20))

    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(getNode("vtkMRMLSegmentationNode" + str(i-20)))
    segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

    # Split islands
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation", "SPLIT_ISLANDS_TO_SEGMENTS")
    effect.setParameter("MinimumSize", min_size_islands)
    effect.self().onApply()

    # Set Masking
    segmentEditorNode.SetMaskMode(0)
    segmentEditorNode.SetOverwriteMode(2)

    for x in Segments:
        # Closing gaps
        segmentEditorWidget.setCurrentSegmentID(x)
        segmentEditorWidget.setActiveEffectByName("Smoothing")
        effect = segmentEditorWidget.activeEffect()
        effect.setParameter("SmoothingMethod", "CLOSING")
        effect.setParameter("KernelSizeMm", cl_kernel_size_mm)
        effect.self().onApply()

    # Cleaning up
    segmentEditorWidget = None
    slicer.mrmlScene.RemoveNode(segmentEditorNode)
    slicer.mrmlScene.RemoveNode(getNode("vtkMRMLSubjectHierarchyNode" + str(i-20)))
    slicer.mrmlScene.RemoveNode(getNode("vtkMRMLScalarVolumeNode" + str(i-20)))
    slicer.mrmlScene.RemoveNode(getNode("vtkMRMLSegmentationNode" + str(i-20)))
</code></pre>
<p>And the error I keep getting is the following:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
File "&lt;console&gt;", line 1, in &lt;module&gt;
File "&lt;string&gt;", line 71, in &lt;module&gt;
File "/Applications/Slicer.app/Contents/lib/Slicer-5.0/qt-scripted-modules/SegmentEditorEffects/SegmentEditorSmoothingEffect.py", line 235, in onApply
self.smoothSelectedSegment(maskImage, maskExtent)
File "/Applications/Slicer.app/Contents/lib/Slicer-5.0/qt-scripted-modules/SegmentEditorEffects/SegmentEditorSmoothingEffect.py", line 348, in smoothSelectedSegment
thresh.SetOutputScalarType(clippedSelectedSegmentLabelmap.GetScalarType())
AttributeError: 'NoneType' object has no attribute 'GetScalarType'
</code></pre>
<p>I can’t figure out what the problem is as it was running smoothly before and still does sometimes. I have tried to change “CLOSING” to “MORPHOLOGICAL_CLOSING” (as it is called <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#effect-parameters" rel="noopener nofollow ugc">here</a>) but that did not seem to solve the problem.</p>
<p>Another thing I noticed is that slicer sometimes skips a number when naming the nodes automatically. As you can see my script relies on the numbering of the different nodes, which causes an error when a number is skipped. I can fix this by just running the script again but it seems there should be a better solution to this?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2022-08-15 23:41 UTC)

<p>If you don’t get any solutions you could try reproducing this as a test that anyone can replicate (e.g. a script that uses the SampleData and can be pasted into the python console).</p>

---

## Post #3 by @FOosterbaan (2022-08-17 12:33 UTC)

<p>Hi, thanks for your suggestion, unfortunately I couldn’t reproduce the error with sample data as the above code works without problems on that data. Using my own data the problem only occurs for some images and works for most, which is why I couldn’t find the problem in my code. So maybe I’ll have to segment the images were the problem occurs by hand.</p>

---

## Post #4 by @FOosterbaan (2022-08-22 08:49 UTC)

<p>Hi all, I have found why I got the error. In some images two bones were so close to each other that the script I wrote segmented them as one bone. This meant the segment ‘Bone_6’ didn’t exist so the closing function couldn’t be used for that particular segment which resulted in the error. The program still skips numbers in the naming of the nodes sometimes (most of the times it skips <code>vtkMRMLSubjectHierarchyNode2</code>) for which I haven’t found a solution yet apart from rerunning my script.</p>

---
