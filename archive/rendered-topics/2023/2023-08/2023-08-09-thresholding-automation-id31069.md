---
topic_id: 31069
title: "Thresholding Automation"
date: 2023-08-09
url: https://discourse.slicer.org/t/31069
---

# Thresholding automation

**Topic ID**: 31069
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/thresholding-automation/31069

---

## Post #1 by @William (2023-08-09 15:23 UTC)

<p><strong>What I am trying to do:</strong></p>
<p>In 3d slicer I have several volumes loaded (they show in the data tab) for each of these I would like to automatically perform a threshold segmentation. Each should receive two separate threshold segmentations, the first at 8.00-8.00 and the second 20.00-20.00 (these correspond to the grayscale values of specific labels within the volume, nothing special about these values furthermore). I then want each to be saved, with a unique name that corresponds to the volume they were segmented from, as a compressed nifti i.e. " .nii.gz".</p>
<p><strong>What I have so far:</strong></p>
<pre><code class="lang-auto">1 # Threshold automation
2 # v1.0
3
4 # Get the list of loaded volumes from the Data module
5 loadedVolumes = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')
6
7 # Define threshold ranges
8 threshold_ranges = [(8.00, 8.00), (20.00, 20.00)]
9
10 # Iterate through loaded volumes
11 for volume in loadedVolumes:
12     volume_name = volume.GetName()
13
14    # Create a directory to save the segmented results
15    output_dir = os.path.join("path/goes/here", "SegmentedVolumes")
16    os.makedirs(output_dir, exist_ok=True)
17
18    # Iterate through threshold ranges
19    for idx, (lower, upper) in enumerate(threshold_ranges):
20    
21        # Create segmentation node
22        segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
23        segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume)
24        segmentationNode.CreateDefaultDisplayNodes()
25        segmentationNode.GetSegmentation().AddEmptySegment(volume_name+"_"+str( idx))
26
27        # Create segment editor widget for effects
28        segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
29        segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
30        segmentEditorWidget.setSegmentationNode(segmentationNode)
31        
32        # Create a threshold effect for the segmentation
33        segmentEditorWidget.setActiveEffectByName("Threshold")
34        effect = segmentEditorWidget.activeEffect()
35        effect.setParameter("MinimumThreshold", lower)
36        effect.setParameter("MaximumThreshold", upper)
37        effect.self().onApply()
38
39        # Save the segmented volume as a .nii.gz file
40        output_file = os.path.join(output_dir, f'{volume_name}_Threshold_{idx}.nii.gz')
41        slicer.util.saveNode(segmentationNode, output_file)
42        
43        # Reset
44        slicer.mrmlScene.RemoveNode(segmentEditorNode)
</code></pre>
<p><strong>The error that I get:</strong></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 35, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'setParameter'
</code></pre>
<p>I am not sure how to resolve this, I am clearly doing <em>something</em> wrong, I am just puzzled as to what as, as far as I am aware, setParameter should work like this, implying that it isn’t the direct cause of this error.</p>
<p>Any help with this is appreciated, I’d rather not have to do this manually for hundreds of volumes <img src="https://emoji.discourse-cdn.com/twitter/melting_face.png?v=12" title=":melting_face:" class="emoji" alt=":melting_face:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @William (2023-08-09 19:15 UTC)

<p>I am on my commute home with a strong cup of coffee and I think I have identified the (several) problems. Once I am home I will try out what I think the probable solution is and report it back here.</p>
<p>So for anyone reading this thread, don’t use your time on my problem quite yet!</p>

---

## Post #3 by @lassoan (2023-08-09 19:26 UTC)

<p>If you have a label image (where each discrete value corresponds to a structure) then you can load the image directly as a segmentation.</p>
<p>You only need thresholding if you want to map a range of values (e.g., any values between 20 and 50) to a single segment.</p>

---
