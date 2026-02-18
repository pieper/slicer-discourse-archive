# Segmentation File Working Slowly

**Topic ID**: 6670
**Date**: 2019-05-01
**URL**: https://discourse.slicer.org/t/segmentation-file-working-slowly/6670

---

## Post #1 by @PWB (2019-05-01 22:18 UTC)

<p>Hi All,</p>
<p>I am working with the segment-editor module in Slicer 4.10.1 for Linux on a Dell Precision T7400, Intel Xeon E5440 2.83GH, 32Gb RAM</p>
<p>I am sharing the seg.nrrd. file back and forth over Dropbox with a collaborator who segments on laptop that uses Windows 10 Pro, Intel Core i7-8550U 1.8 GHz, 16Gb RAM.</p>
<p>The process started well, but the segmentation file has grown to 12.2 Mb and processes very slowly. For example, from the moment when I press the enter key after drawing a segment to the moment the segment fills in takes from 30 to 90 seconds. Other processes such as scrolling through the slices are also slowed down. Using the paint tool is less slow but still dramatically slower than before. Saving the segmentation file takes several minutes and occasionally crashes my computer.</p>
<p>Starting a new segmentation file with the same image moves much more quickly.</p>
<p>My collaborator’s laptop has no issues with the same file, and only experiences a ~4 second delay between pressing enter and the segmentation filling in.</p>
<p>I have tried 4.10.1 on several other computers including an iMac and a Surface Pro. I have also tried the most recent nightly build, but all have similar speeds.</p>
<p>Is the issue with my segmentation file, and is there a way I can clean it up to run faster?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-05-02 00:40 UTC)

<p>Is it possible that Grow from seeds or Watershed segmentation is still active (have not clicked Apply or Cancel)? Have you enabled “Show 3D”? Have you disabled surface smoothing? Is the performance OK if you do not load the entire scene just load the segmentation (.seg.nrrd) file and master volume (.nrrd) file? Can you share the file that causes performance problems?</p>

---

## Post #3 by @PWB (2019-05-02 20:52 UTC)

<p>I have not initialized Grow for seeds or Watershed segmentation, neither are active. I have tried with Show 3D on and off. Surface smoothing is off. The performance is the same regardless of whether the files are loaded with the scene or individually. What is the best way for me to share the segmentation file with you?</p>

---

## Post #4 by @lassoan (2019-05-02 21:31 UTC)

<aside class="quote no-group" data-username="PWB" data-post="3" data-topic="6670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> PWB:</div>
<blockquote>
<p>What is the best way for me to share the segmentation file with you?</p>
</blockquote>
</aside>
<p>Upload somewhere (Dropbox, OneDrive, Google drive,…) and send the link. Thanks!</p>

---

## Post #5 by @PWB (2019-05-02 22:02 UTC)

<p>Thank you, here is the link: <a href="https://www.dropbox.com/s/v3kw7zyb3j8oz1n/Nolte%20Segmentation_2.seg.nrrd?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/v3kw7zyb3j8oz1n/Nolte%20Segmentation_2.seg.nrrd?dl=0</a></p>

---

## Post #6 by @cpinter (2019-05-03 00:13 UTC)

<p>I tried it on Windows and editing seemed to work fine. There is around 5 seconds delay with the Draw tool, but not 30-90 as you reported, and slice changes and 3D view are responsive.<br>
For me memory usage didn’t go above 2GB, but when I saved the segmentation to file, it went up to 10+GB and it was indeed slow.</p>
<p>Your image seems quite large resolution (0.211 x 0.05 x 0.05mm) but hard to tell without the master volume. Try subsampling them like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/444cb656d949199440f1955c2c384c12c2ff521d.png" data-download-href="/uploads/short-url/9KcP2AOdjJqYVIL5JKjW2ZhL62h.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/444cb656d949199440f1955c2c384c12c2ff521d_2_690x288.png" alt="image" data-base62-sha1="9KcP2AOdjJqYVIL5JKjW2ZhL62h" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/444cb656d949199440f1955c2c384c12c2ff521d_2_690x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/444cb656d949199440f1955c2c384c12c2ff521d_2_1035x432.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/444cb656d949199440f1955c2c384c12c2ff521d.png 2x" data-dominant-color="E0E1E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1049×438 54.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also the segment ‘Pontine Nuclei - Right’ is very fragmented, maybe it causes slowdown with<br>
operations like surface conversion. Smoothing won’t help this one but you can make it solid.</p>

---

## Post #7 by @lassoan (2019-05-03 03:06 UTC)

<p>The segmentation is editable on my computer (3-year-old Windows PC, 16GB RAM) with about the same speed as <a class="mention" href="/u/cpinter">@cpinter</a> reported above.</p>
<p>The performance is probably not great due to the somewhat large number of segments and large extent.</p>
<p>Your segmentation resolution is highly anisotropic (voxels are stick-shaped - 4x longer than wide), which is wasting a lot of resources. If you follow <a class="mention" href="/u/cpinter">@cpinter</a>’s suggestion above (set spacing to isotropic, oversampling to 0.25-0.5) and then apply smoothing (Smoothing effect, Joint smoothing).</p>
<p>To reduce number of segments that are concurrently updated and reduce extent, you can create additional segmentation node(s) and move segments there that you are not currently editing and/or expensive to update (such as Pontine Nuclei). It may also make sense to move segments out to another segmentation that are far away from the others (such as CNVSP and CNXII).</p>
<p>To prevent any crashes, set virtual memory (swap) size to 10x larger than the data set that you work with 279x848x596 x 46 segments x 10 = about 65 GB.</p>

---

## Post #8 by @Jmarcs (2019-07-14 08:31 UTC)

<p>I like your Idea<br>
thank you</p>

---
