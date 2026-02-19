---
topic_id: 17511
title: "Get Displacement Vector Fields Within A Segment From Vector"
date: 2021-05-07
url: https://discourse.slicer.org/t/17511
---

# Get displacement vector fields within a segment from vector volume

**Topic ID**: 17511
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/get-displacement-vector-fields-within-a-segment-from-vector-volume/17511

---

## Post #1 by @marianaslicer (2021-05-07 15:55 UTC)

<p>Hi everyone,</p>
<p>I used the Transforms module to convert a transform in a vector volume node because I’m interested in getting the motion of a ROI in the three directions.</p>
<p>I think I was able to get the magnitude of the motion in the three directions using the commands:</p>
<pre><code>volumeNode = getNode('Displacement Field')
volumeArray = slicer.util.arrayFromVolume(volumeNode)
</code></pre>
<p>Result:<br>
print(volumeArray)<br>
[[[[ 1.8819143e-01  2.5158906e-01  2.4303983e-01]<br>
[ 1.9190283e-01  2.5705618e-01  2.4819151e-01]<br>
[ 1.9539744e-01  2.6224315e-01  2.5308487e-01]<br>
…<br>
[-2.4863344e-01  2.2675639e-01  2.8394413e-01]<br>
[-2.4424334e-01  2.2257148e-01  2.7850366e-01]<br>
[-2.3958866e-01  2.1815073e-01  2.7276406e-01]]</p>
<pre><code>  [[ 1.9246668e-01  2.5698945e-01  2.4814722e-01]
   [ 1.9626349e-01  2.6257366e-01  2.5340959e-01]
   [ 1.9983855e-01  2.6787159e-01  2.5840810e-01]
   ...
   [-2.5424054e-01  2.3186195e-01  2.9020959e-01]
   [-2.4974997e-01  2.2758357e-01  2.8464693e-01]
   [-2.4498877e-01  2.2306396e-01  2.7877831e-01]]

  [[ 1.9650456e-01  2.6209354e-01  2.5296500e-01]
   [ 2.0038210e-01  2.6778823e-01  2.5833178e-01]
   [ 2.0403317e-01  2.7319089e-01  2.6342940e-01]
   ...
</code></pre>
<p>Now, I would like to get the vector fields within a specific segment (e.g. tumor).<br>
I tried to use the example code <a href="https://discourse.slicer.org/t/get-image-intensity-histogram-of-a-segment/11277">here</a> but when I try to run</p>
<p><code>segmentVoxels = volumeArray[labelArray == labelValue]</code></p>
<p>I’m having the following error:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
IndexError: boolean index did not match indexed array along dimension 0; dimension is 137 but corresponding boolean dimension is 5
</code></pre>
<p>More Info:<br>
labelValue = 1</p>
<pre><code>print(labelArray)

[[[0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 1 1 0 0 0 0 0 0]
  [0 0 1 1 1 1 0 0 0 0 0]
  [0 0 1 1 1 1 0 0 0 0 0]
  [0 1 1 1 1 1 1 0 0 0 0]
  [0 0 1 1 1 1 1 0 0 0 0]
  [0 0 0 1 1 1 1 0 0 0 0]
  [0 0 0 0 1 1 1 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]]

 [[0 0 1 1 1 1 0 0 0 0 0]
  [0 1 1 1 1 1 1 0 0 0 0]
  [1 1 1 1 1 1 1 0 0 0 0]
  [1 1 1 1 1 1 1 1 0 0 0]
  [1 1 1 1 1 1 1 1 0 0 0]
  [1 1 1 1 1 1 1 1 1 0 0]
  [0 1 1 1 1 1 1 1 1 0 0]
  [0 0 1 1 1 1 1 1 1 0 0]
  [0 0 1 1 1 1 1 1 0 0 0]
  [0 0 0 0 0 1 1 0 0 0 0]]

 [[0 0 0 0 1 1 1 1 0 0 0]
  [0 0 1 1 1 1 1 1 1 0 0]
  [0 1 1 1 1 1 1 1 1 0 0]
  [1 1 1 1 1 1 1 1 1 1 0]
  [1 1 1 1 1 1 1 1 1 1 0]
  [1 1 1 1 1 1 1 1 1 1 1]
  [0 1 1 1 1 1 1 1 1 1 1]
  [0 1 1 1 1 1 1 1 1 1 0]
  [0 0 1 1 1 1 1 1 1 1 0]
  [0 0 0 1 1 1 1 1 1 0 0]]

 [[0 0 0 0 0 1 1 1 0 0 0]
  [0 0 0 0 1 1 1 1 1 0 0]
  [0 0 0 0 1 1 1 1 1 0 0]
  [0 0 1 1 1 1 1 1 1 1 0]
  [0 1 1 1 1 1 1 1 1 1 0]
  [0 1 1 1 1 1 1 1 1 1 0]
  [0 1 1 1 1 1 1 1 1 1 0]
  [0 1 1 1 1 1 1 1 1 1 0]
  [0 0 1 1 1 1 1 1 1 0 0]
  [0 0 1 1 1 1 1 1 0 0 0]]

 [[0 0 0 0 0 0 0 0 0 0 0]
  [0 0 0 0 0 1 1 1 0 0 0]
  [0 0 0 0 0 1 1 1 0 0 0]
  [0 0 0 0 1 1 1 1 1 0 0]
  [0 0 1 1 1 1 1 1 1 0 0]
  [0 1 1 1 1 1 1 1 1 0 0]
  [0 0 1 1 1 1 1 1 1 0 0]
  [0 0 0 1 1 1 1 1 0 0 0]
  [0 0 0 0 1 1 0 0 0 0 0]
  [0 0 0 0 0 0 0 0 0 0 0]]]
</code></pre>
<p>I would appreciate some help. Thank you.</p>

---

## Post #2 by @lassoan (2021-05-13 04:52 UTC)

<p>You almost got it right, just missed a dimension when specified the displacement array indices. Here is a complete working example:</p>
<pre><code class="lang-python">displacementVolumeNode = getNode('Displacement Field')
segmentationNode = getNode('Segmentation')
labelValue = 1  # label value of first segment

# Get displacement field as numpy array
displacementVolumeArray = slicer.util.arrayFromVolume(volumeNode)

# Get segment as numpy array
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)
labelmapVolumeArray = slicer.util.arrayFromVolume(labelmapVolumeNode)

# Get displacement vectors in the segment as numpy array
displacementsInSegment = displacementVolumeArray[labelmapVolumeArray == labelValue, :]
</code></pre>

---
