# Synthetic CT from MRI - editing MRI segments to Hounsfield Units

**Topic ID**: 20351
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/synthetic-ct-from-mri-editing-mri-segments-to-hounsfield-units/20351

---

## Post #1 by @Harsforn (2021-10-26 02:09 UTC)

<p>Hi all,</p>
<p>I’m trying to generate a synthetic CT from an MRI for use in an MRI-only radiotherapy treatment planning approach (with SlicerRT).</p>
<p>I’ve segmented out bone, air, tissue, and a mock tumour from the MRI - is there a way to convert their voxel values to Hounsfield Units? This is an exploratory approach so I only need those 4 basic features in the sCT; ideally I would like to set the HU for each segment (similar to assigning label values in the ‘Model to LabelMap’ module).</p>
<p>Thanks for your time.</p>

---

## Post #2 by @lassoan (2021-10-26 03:26 UTC)

<p>You can use the segmentation to change voxels of a volume of the same geometry using numpy array operations, something like this:</p>
<pre><code class="lang-python">volumeNode = getNode('MRHead')
segmentationNode = getNode('Segmentation')

segmentNames = ['bone', 'air', 'tissue', 'tumor']
voxelIntensities = [2000, -1000, 60, 150]

volumeArray = slicer.util.arrayFromVolume(volumeNode)

for segmentName, voxelIntensity in zip(segmentNames, voxelIntensities):
    # Get segment as numpy array
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
    # Update voxel of the volume
    volumeArray[ segmentArray &gt; 0 ] = voxelIntensity

slicer.util.arrayFromVolumeModified(volumeNode)
</code></pre>

---

## Post #3 by @Harsforn (2021-10-26 04:06 UTC)

<p>Thanks for the reply, Andras. I’m getting the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
File "&lt;console&gt;", line 3, in &lt;module&gt;
TypeError: arrayFromSegmentBinaryLabelmap() takes 2 positional arguments but 3 were given
</code></pre>
<p>I’ve tried limiting it to two (of those three) arguments but it errs every time. Any ideas?</p>

---

## Post #4 by @PaoloZaffino (2021-10-26 08:01 UTC)

<p>There are several AI-based algorithms for converting MRI into sCT.</p>
<p>However, to check quality conversion, you can use this module:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ImageCompare" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ImageCompare</a></p>
<p>Best,<br>
Paolo</p>

---

## Post #5 by @lassoan (2021-10-26 11:45 UTC)

<aside class="quote no-group" data-username="Harsforn" data-post="3" data-topic="20351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/85e7bf/48.png" class="avatar"> Harsforn:</div>
<blockquote>
<p>I’ve tried limiting it to two (of those three) arguments but it errs every time. Any ideas?</p>
</blockquote>
</aside>
<p>The code snippet works in recent Slicer Preview Releases. The latest Slicer Stable Release users slightly different syntax.</p>

---

## Post #6 by @Harsforn (2021-10-26 12:35 UTC)

<p>Thanks for the help. I’ve downloaded the most recent preview release but I’m now getting a different error - I’ve attached a screenshot in case the problem is my structuring of the nodes/segments.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7a689184a70a312df22e2aa3e6c92f579cca97b.jpeg" data-download-href="/uploads/short-url/nV6xnaAbKxbTZXKUsE5x7qvd1ZF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a689184a70a312df22e2aa3e6c92f579cca97b_2_690x434.jpeg" alt="image" data-base62-sha1="nV6xnaAbKxbTZXKUsE5x7qvd1ZF" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a689184a70a312df22e2aa3e6c92f579cca97b_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a689184a70a312df22e2aa3e6c92f579cca97b_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a689184a70a312df22e2aa3e6c92f579cca97b_2_1380x868.jpeg 2x" data-dominant-color="B8C1BE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1208 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The code I’m using is:</p>
<pre><code class="lang-auto">volumeNode = getNode('101')
segmentationNode = getNode('Segmentation')

segmentNames = ['bone', 'gas', 'tissue', 'mass']
voxelIntensities = [2000, -1000, 60, 150]

for segmentName, voxelIntensity in zip(segmentNames, voxelIntensities):
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
    segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
    volumeArray[ segmentArray &gt; 0 ] = voxelIntensity

slicer.util.arrayFromVolumeModified(volumeNode)
</code></pre>

---

## Post #7 by @lassoan (2021-10-26 20:50 UTC)

<p>It seems that I’ve missed a line. Call <code>volumeArray = slicer.util.arrayFromVolume(volumeNode)</code> after setting <code>volumeNode</code>.</p>

---
