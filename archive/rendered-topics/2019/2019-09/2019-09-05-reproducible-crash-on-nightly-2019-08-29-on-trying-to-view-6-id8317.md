---
topic_id: 8317
title: "Reproducible Crash On Nightly 2019 08 29 On Trying To View 6"
date: 2019-09-05
url: https://discourse.slicer.org/t/8317
---

# Reproducible crash on Nightly (2019-08-29) on trying to view 64 bit image

**Topic ID**: 8317
**Date**: 2019-09-05
**URL**: https://discourse.slicer.org/t/reproducible-crash-on-nightly-2019-08-29-on-trying-to-view-64-bit-image/8317

---

## Post #1 by @mikebind (2019-09-05 21:55 UTC)

<p>The following code reproducibly crashes Slicer:</p>
<pre><code>import numpy as np
crashVolNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode','crashVol')
crashVolNode.CreateDefaultDisplayNodes()
slicer.util.updateVolumeFromArray(crashVolNode,np.array(np.ones((100,100,100)),dtype=np.int64))
slicer.util.setSliceViewerLayers(background=crashVolNode)
</code></pre>
<p>There is no crash if the dtype is np.int32.  The crash does not occur until the image is viewed in the slice viewers. As long as it is not viewed, the Volumes module reports everything correctly about it. The Scalar Type is listed as long long</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56eae8dd0d582682604ab10a675b3790735213e7.png" data-download-href="/uploads/short-url/coUlWNeBiPe9BQPmhHlGgndgkh9.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56eae8dd0d582682604ab10a675b3790735213e7_2_336x500.png" alt="Capture" data-base62-sha1="coUlWNeBiPe9BQPmhHlGgndgkh9" width="336" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56eae8dd0d582682604ab10a675b3790735213e7_2_336x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56eae8dd0d582682604ab10a675b3790735213e7_2_504x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56eae8dd0d582682604ab10a675b3790735213e7.png 2x" data-dominant-color="F0EFED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">525×780 86.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t actually need 64bit images, so casting down is just fine. However, this was difficult to track down as there was no error and nothing in the Slicer log, so I figured I would post this here for general awareness. I was naively using the output of skimage.measure.label to create the image, and the output was 64bit integers, so it crashed Slicer. I assumed at first I was incorrectly creating the volume, but it turns out it was just the data type.</p>

---

## Post #2 by @pieper (2019-09-05 22:11 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>I am able to reproduce that on a local debug build.  It crashes in vtkImageReslice.  Interesting.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97bbc713c2509f0275329a165cff48ed9df440a7.jpeg" data-download-href="/uploads/short-url/lEippdMZWX7zmQZmy0uQ2wv10Kr.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97bbc713c2509f0275329a165cff48ed9df440a7_2_690x181.jpeg" alt="image" data-base62-sha1="lEippdMZWX7zmQZmy0uQ2wv10Kr" width="690" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97bbc713c2509f0275329a165cff48ed9df440a7_2_690x181.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97bbc713c2509f0275329a165cff48ed9df440a7_2_1035x271.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97bbc713c2509f0275329a165cff48ed9df440a7_2_1380x362.jpeg 2x" data-dominant-color="E6E2DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1584×416 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
