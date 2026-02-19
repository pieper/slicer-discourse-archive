---
topic_id: 18772
title: "Resampled Segmentation Limited By A Bounding Box Not The Who"
date: 2021-07-17
url: https://discourse.slicer.org/t/18772
---

# Resampled segmentation limited by a bounding box (not the whole volume)

**Topic ID**: 18772
**Date**: 2021-07-17
**URL**: https://discourse.slicer.org/t/resampled-segmentation-limited-by-a-bounding-box-not-the-whole-volume/18772

---

## Post #1 by @laurentletg (2021-07-17 00:22 UTC)

<p>Operating system: Mac OS Catalina 10.15.7<br>
Slicer version: 4.13.0-2021-04-04 (also 4.11)<br>
Expected behavior: Able to perform segmentation using a resampled version on the whole volume<br>
Actual behavior: Segmentation using a resampled version is limited to a bounding box</p>
<p>Hello Slicer community, this is my first post on this forum,</p>
<p>I could not find the answer in this forum, please redirect me if this has been already answered.</p>
<p>I resampled pairs of volumes and segmentations so that I can perform random re sizing of segmentation labels. Among my dataset I have variable slice thicknesses which limits my ability to use the grow/shrink segmentation module (I want to increment by 1 mm steps). Segmentations were performed using the original  head CT images without resampling prior to segmentation. The typical resolution of original images is 0.5 x 0.5 x 4.0 mm and I resampled this to 1.0 mm3 isotropic voxels. I was able to do this using the following script as well as using the torchio package (tio.resample) .</p>
<h3><a name="p-63337-load-any-volume-and-perform-a-sample-segmentation-1" class="anchor" href="#p-63337-load-any-volume-and-perform-a-sample-segmentation-1" aria-label="Heading link"></a>Load any volume and perform a sample segmentation</h3>
<h3><a name="p-63337-get-nodes-2" class="anchor" href="#p-63337-get-nodes-2" aria-label="Heading link"></a>Get nodes</h3>
<pre><code class="lang-auto">volumeNode = slicer.util.getNode("vtkMRMLScalarVolumeNode1")
segmentationNode = slicer.util.getNode("vtkMRMLSegmentationNode1")
</code></pre>
<h3><a name="p-63337-resample-the-volume-3" class="anchor" href="#p-63337-resample-the-volume-3" aria-label="Heading link"></a>Resample the volume</h3>
<pre><code class="lang-auto">transformedVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode")
parameters = {
    "outputPixelSpacing":"1,1,1",
    "InputVolume":volumeNode.GetID(),
    "interpolationMode":'linear',
    "referenceVolume": volumeNode.GetID(),
    "OutputVolume":transformedVolumeNode.GetID()}
slicer.cli.run(slicer.modules.resamplescalarvolume, None, parameters)
</code></pre>
<h3><a name="p-63337-resample-the-segmentation-4" class="anchor" href="#p-63337-resample-the-segmentation-4" aria-label="Heading link"></a>Resample the segmentation</h3>
<pre><code class="lang-auto">transformedSegmNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
parameters = {
    "outputPixelSpacing":"1,1,1",
    "InputVolume":segmentationNode.GetID(),
    "interpolationMode":'linear',
    "referenceVolume": segmentationNode.GetID(), # I also tried volumeNode.GetID()
    "OutputVolume":transformedSegmNode.GetID()}
slicer.cli.run(slicer.modules.resamplescalarvolume, None, parameters)
</code></pre>
<p>However, when I try to perform additional annotations on the resampled segmentation <a href="https://www.dropbox.com/s/86rmw8zk3gdnzn1/slicer%20issue%20resampling.png?dl=0" rel="noopener nofollow ugc">I am limited to a smaller ROI than the volume</a> (I can segment a bounding box that seems to be limited by the outer edges of the original segmentation). This occurs using resampled segmentations from both Slicer and torchio. Interestingly using itk-snap I can edit segmentation over the whole resampled volume, as expected (but not in Slicer).</p>
<p>I am able to recreate this issue using a downloaded sample image from Slicer after performing a segmentation, then running the script above and trying to annotate the resampled pair of volume/labels.</p>
<p>If there is a way to correct this using python scripting I’d be very interested in getting the code since I want to leverage the ability to batch process multiple cases using the Jupiter integration.</p>
<p>Maybe I am doing something wrong, please let me know,</p>
<p>Thanks</p>
<p>Best,</p>
<p>Laurent</p>

---

## Post #2 by @lassoan (2021-07-17 05:06 UTC)

<p>Segmentation geometry (origin, spacing, axis directions, extents) is determined from the first selected master volume, as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>. You can change the geometry later, if necessary, but you can avoid this by resampling the volume before segmentation.</p>
<aside class="quote no-group" data-username="laurentletg" data-post="1" data-topic="18772">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/laurentletg/48/10051_2.png" class="avatar"> laurentletg:</div>
<blockquote>
<p>Among my dataset I have variable slice thicknesses which limits my ability to use the grow/shrink segmentation module (I want to increment by 1 mm steps).</p>
</blockquote>
</aside>
<p>When you import a data set with varying spacing, Slicer computes a non-linear transform, which moves all the slices to the correct physical location and interpolates across the varying distances. I think segmentation module can work on volumes that are under a non-linear transform, but I haven’t checked this now, so if you run into any problems then you can harden the transform on the volume before you start the segmentation. You can do that in Data module: right-click on the transform column of the volume node, and harden the transform (resample the volume). You can of course do this from Python, too (by calling <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformableNode.html#add3fb3ed7b65c0f2de92f535f013869b">ApplyTransform</a>. If there is any specific geometry (extent, spacing, etc.) that you want then you can use a resampling module or Crop volume module to resample the volume.</p>

---

## Post #3 by @laurentletg (2021-10-11 01:30 UTC)

<p>Thank you for the answer.</p>
<p>The missing part in the last code block was, as suggested, to set the reference geometry. Here is the code to resample a segment and set its reference geometry.</p>
<h2><a name="p-67846-resample-the-segmentation-corrected-1" class="anchor" href="#p-67846-resample-the-segmentation-corrected-1" aria-label="Heading link"></a>Resample the segmentation (corrected)</h2>
<pre><code class="lang-auto"># Create a resampled node
transformedSegmNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
parameters = {
    "outputPixelSpacing":"1,1,1",
    "InputVolume":segmentationNode.GetID(),
    "interpolationType":'linear',
    "referenceVolume": transformedVolumeNode.GetID(),
    "OutputVolume":transformedSegmNode.GetID()}
slicer.cli.run(slicer.modules.resamplescalarvolume, None, parameters)

#Set reference geometry (resampled volume)
transformedSegmNode.SetReferenceImageGeometryParameterFromVolumeNode(transformedVolumeNode)
</code></pre>

---
