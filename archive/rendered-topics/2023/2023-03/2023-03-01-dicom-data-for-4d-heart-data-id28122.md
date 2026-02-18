# DICOM data for 4D heart data

**Topic ID**: 28122
**Date**: 2023-03-01
**URL**: https://discourse.slicer.org/t/dicom-data-for-4d-heart-data/28122

---

## Post #1 by @alireza (2023-03-01 18:02 UTC)

<p>I’m looking for a 4D dicom data of heart. Slicer seems to have a nice one in the sample data (CT Cardio Sequence) that is inside the welcome message</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9927f6e8fa7554af0237dd3bef1d45a236dc90f5.jpeg" data-download-href="/uploads/short-url/lQSFWv1bCqZME6r6dc6tolWyQ2V.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9927f6e8fa7554af0237dd3bef1d45a236dc90f5.jpeg" alt="image" data-base62-sha1="lQSFWv1bCqZME6r6dc6tolWyQ2V" width="690" height="464" data-dominant-color="B9B8B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">718×483 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f01275eb1616e51d5b2edf585cdb15f8b1d62cf5.jpeg" data-download-href="/uploads/short-url/yfM8XQhOHmbhKVMFQgq5vvHQchT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01275eb1616e51d5b2edf585cdb15f8b1d62cf5_2_678x500.jpeg" alt="image" data-base62-sha1="yfM8XQhOHmbhKVMFQgq5vvHQchT" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01275eb1616e51d5b2edf585cdb15f8b1d62cf5_2_678x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01275eb1616e51d5b2edf585cdb15f8b1d62cf5_2_1017x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f01275eb1616e51d5b2edf585cdb15f8b1d62cf5_2_1356x1000.jpeg 2x" data-dominant-color="818084"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1382×1018 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>At Cornerstone3D, we have recently added support for 4D data reading (demo <a href="https://www.cornerstonejs.org/live-examples/dynamicPetCt.html" rel="noopener nofollow ugc">here</a>), but I’m looking to add a smaller demo that is not as huge as the one we use right now and beating heart is always a nice demo for 4D.</p>
<p>Can anyone from SlicerHeart team help me with some DICOM data?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2023-03-01 18:31 UTC)

<p>We have recently published 4D cardiac US and a 3D cardiac CT in NRRD format in <a href="https://github.com/SlicerHeart/SlicerHeart/releases/tag/TestingData">SlicerHeart Sample Data</a>, but right now we don’t have any publicly shareable 4D cardiac CT in DICOM format. I haven’t come across any public repository for them either, but I haven’t searched.</p>
<p>Note that the CTs in the Slicer core Sample Data sets are very small, downscaled versions. Size of a typical 4D CT heart series is between 800MB and 6GB (512x512 pixels, 400-800 slices, 10-20 time points).</p>

---

## Post #3 by @alireza (2023-03-01 18:47 UTC)

<p>Thanks, I will look into those datasets.</p>
<p>Yeah, the browser can handle the 6GB memory and even more (assuming the machine has capacity). Based on our experiments:</p>
<ul>
<li>Browser can store at max 2GB memory per array buffer (the only way we can push it is through webAssembly memory, but one series in 4D is hardly more than 2GB as I have seen)</li>
<li>You can have as many array buffers as your Chrome &amp; RAM permits. We created a demo here (<a href="https://arraybuffer.netlify.app/" rel="noopener nofollow ugc">https://arraybuffer.netlify.app/</a>) to see how many array buffers you can allocate on your machine and the total amount of memory.</li>
</ul>
<p>For my 16GB Mac it is</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81f96c6a406b6e1c9a31a552b96b895a480021eb.png" alt="image" data-base62-sha1="ixNYPd35B886lQDgGunsqpclRHR" width="448" height="282"></p>
<p>which means</p>
<p>mine is like</p>
<ul>
<li>browser can store 8000 1MB array buffer</li>
<li>71 of 200 MB buffers</li>
<li>….</li>
</ul>
<p>and totally in most cases (except the 1MB for some weird reason), it can reach the 16GB of my RAM.</p>
<p>So as long as each time point is not great than 2GB we are fine in web, and I expect some advanced caching to disk can happen if there are MANY timepoints,.</p>

---
