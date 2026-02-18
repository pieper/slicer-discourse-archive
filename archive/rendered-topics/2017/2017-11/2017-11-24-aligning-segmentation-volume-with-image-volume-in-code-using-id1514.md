# Aligning segmentation volume with image volume in code using nrrd headers

**Topic ID**: 1514
**Date**: 2017-11-24
**URL**: https://discourse.slicer.org/t/aligning-segmentation-volume-with-image-volume-in-code-using-nrrd-headers/1514

---

## Post #1 by @dcantor (2017-11-24 04:18 UTC)

<p>Hello, I am working on prostate segmentation in Slicer. After finishing the segmentation and  saving the Scene, I took a look at the image volume (V) and the segmentation volume (S) nrrd files in python, the two volumes have the same orientation as I performed segmentation on axial slices (on the RA plane) and moved in the Superior-Inferior axis, segmenting one slice at a time.</p>
<p>Both V and S have ijk-to-ras matrices that enable me to recreate their relative location in space as shown in the figure below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/313f7bce1885f5f3a7237bda07e9f5be8629fc8a.png" data-download-href="/uploads/short-url/71Fpms2QVq7hXeRadxncjPnyAhs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/313f7bce1885f5f3a7237bda07e9f5be8629fc8a_2_690x316.png" alt="image" data-base62-sha1="71Fpms2QVq7hXeRadxncjPnyAhs" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/313f7bce1885f5f3a7237bda07e9f5be8629fc8a_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/313f7bce1885f5f3a7237bda07e9f5be8629fc8a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/313f7bce1885f5f3a7237bda07e9f5be8629fc8a.png 2x" data-dominant-color="EAEFEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">961×441 26.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For a given a slice in <strong>V</strong>, I would like to find <em>the corresponding slice</em> in <strong>S</strong> in my code (or none if no intersection). Since I know that the two the volumes have the same orientation in space, I was thinking of simply taking one slice in V and check <em>which slice in S is coplanar</em>. I can do this by taking one point for each slice in S, so if S has 10 slices I have 10 points to compare with the current slice in V. Does this make sense? Or is there a simple way to achieve this?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2017-11-24 04:25 UTC)

<p>You can get the slice coordinates very easily by converting voxel coordinates to LPS and LPS to voxel coordinates of the other volume:</p>
<pre><code>point_IJK_S = inv(IJKToRAS_S) * IJKToRAS_V * point_IJK_V</code></pre>

---

## Post #3 by @dcantor (2017-11-24 13:37 UTC)

<p>You mean RAS right? to RAS…</p>

---

## Post #4 by @lassoan (2017-11-24 14:10 UTC)

<p>If you have a slice number (typically K coordinate) in one image and you need slice number in another image then you need to convert IJK-&gt;RAS-&gt;IJK (or IJK-&gt;LPS-&gt;IJK).</p>

---

## Post #5 by @dcantor (2017-11-24 15:03 UTC)

<p>Got it. Makes sense, simpler than what I had in mind, thank you so much Andras!</p>

---

## Post #6 by @lassoan (2019-07-07 12:07 UTC)

<p>A post was merged into an existing topic: <a href="/t/aligning-segmentations-and-images-using-python/7446/3">Aligning Segmentations and images using python</a></p>

---
