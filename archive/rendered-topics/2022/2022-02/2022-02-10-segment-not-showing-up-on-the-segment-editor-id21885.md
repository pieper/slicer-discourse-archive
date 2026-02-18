# Segment not showing up on the segment editor

**Topic ID**: 21885
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/segment-not-showing-up-on-the-segment-editor/21885

---

## Post #1 by @hourglassnam (2022-02-10 04:34 UTC)

<p>Hello~<br>
I have problems with the segmentation editor.<br>
Some of the segments disappear on the Segment Editor during the segmentation process.<br>
However, when I checked the Data list, all the segments were still there!<br>
And the segments eventually reappear when I reopen the file.<br>
It seems like the segments I created through python interactor are the ones with this problem.<br>
Can anybody explain why this might happen?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eafaf580d63f0c9215e00c6325b6657daf1d7b2f.jpeg" data-download-href="/uploads/short-url/xwJp7O1tFn867IBbrvwh3iRu0bB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafaf580d63f0c9215e00c6325b6657daf1d7b2f_2_690x369.jpeg" alt="image" data-base62-sha1="xwJp7O1tFn867IBbrvwh3iRu0bB" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafaf580d63f0c9215e00c6325b6657daf1d7b2f_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafaf580d63f0c9215e00c6325b6657daf1d7b2f_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eafaf580d63f0c9215e00c6325b6657daf1d7b2f_2_1380x738.jpeg 2x" data-dominant-color="C6C6C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1028 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Below is the script I used, which is based on <a href="https://discourse.slicer.org/t/loading-dicom-directory-into-scene-and-obtaining-master-volume-node/10837/2">this forum</a>.</p>
<pre><code class="lang-python">s=getNode('vtkMRMLSegmentationNode1')
se=s.GetSegmentation()

#change name of existing segmentation
seg=se.GetSegment('Segment_1')
seg.SetColor([1.0,0.2,0.8])
seg.SetName("WG")

#create new segmentation with custom color
SegAL = slicer.vtkSegment()
SegAL.SetName("AL")
SegAL.SetColor([1.0,0.0,0.0])
se.AddSegment(SegAL,"AL")
</code></pre>

---

## Post #2 by @lassoan (2022-02-10 20:31 UTC)

<p>It works well for me in the latest Slicer Preview Release:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adaefda65b51b82bfcfc25726088ed91ff644792.png" data-download-href="/uploads/short-url/oMtw94BXFyikn7NHucSACtxevPY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/adaefda65b51b82bfcfc25726088ed91ff644792_2_592x500.png" alt="image" data-base62-sha1="oMtw94BXFyikn7NHucSACtxevPY" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/adaefda65b51b82bfcfc25726088ed91ff644792_2_592x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/adaefda65b51b82bfcfc25726088ed91ff644792_2_888x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/adaefda65b51b82bfcfc25726088ed91ff644792_2_1184x1000.png 2x" data-dominant-color="BDBEBE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1587×1339 399 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Let us know if you run into any issues when using the latest Slicer Preview Release.</p>

---

## Post #3 by @hourglassnam (2022-02-14 09:09 UTC)

<p>Thank you so much for your reply!<br>
I have not yet tried the latest Slicer Release, but the same issue has not happened with other files!<br>
So I am assuming that there was something wrong with my tiff file.<br>
I will try the new Slicer release as soon as possible and see if the same issue happens again.<br>
Thank you again for checking the code!</p>

---
