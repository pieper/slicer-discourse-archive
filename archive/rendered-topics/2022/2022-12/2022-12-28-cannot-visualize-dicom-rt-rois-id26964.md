---
topic_id: 26964
title: "Cannot Visualize Dicom Rt Rois"
date: 2022-12-28
url: https://discourse.slicer.org/t/26964
---

# Cannot visualize dicom-rt ROIs

**Topic ID**: 26964
**Date**: 2022-12-28
**URL**: https://discourse.slicer.org/t/cannot-visualize-dicom-rt-rois/26964

---

## Post #1 by @kaizhao (2022-12-28 22:39 UTC)

<p>I’m trying to convert some of our own annotations (closed polygons) into dicom-rt format.</p>
<p>I created some dicom files with ROIs of random coordinates from scratch using pydicom. I can visualize the ROIs of created dicom files in Matlab.</p>
<p>Matlab code:</p>
<pre><code class="lang-auto">info = dicominfo("example/slice-01.dcm");
% info = dicominfo("rtstruct.dcm");
contour = dicomContours(info);
figure
plotContour(contour)
</code></pre>
<p>Results:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed3ab7ebd378e20e173834101f07adf8ce043731.jpeg" data-download-href="/uploads/short-url/xQCXMiKAdG2vXpy8gQerliY7XlD.jpeg?dl=1" title="Matlab plot ROIs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed3ab7ebd378e20e173834101f07adf8ce043731_2_690x471.jpeg" alt="Matlab plot ROIs" data-base62-sha1="xQCXMiKAdG2vXpy8gQerliY7XlD" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed3ab7ebd378e20e173834101f07adf8ce043731_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed3ab7ebd378e20e173834101f07adf8ce043731.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed3ab7ebd378e20e173834101f07adf8ce043731.jpeg 2x" data-dominant-color="D0D6E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Matlab plot ROIs</span><span class="informations">955×652 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, I cannot visualize the ROIs with Slicer. I have installed the <code>SlicerRT</code> extension and there is no error log when I load the dicom files.</p>
<p>System information:</p>
<pre><code class="lang-auto">Ubuntu: 22.04 + MacOS Ventura 13.0.1
Slicer: 5.2.1 r31317 / 77da381
</code></pre>
<p>Examplar generated dicom files can be downloaded from <a href="https://kaizhao.net/dicoms.zip" rel="noopener nofollow ugc">https://kaizhao.net/dicoms.zip</a>.<br>
Any help will be appreciated!</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2023-01-04 11:14 UTC)

<p>SlicerRT can process input that is similar to clinical RT data. Arbitrary polygon ROIs are not like this. An RT Structure Set (RTSTRUCT) references a CT image, and it defines closed polygons on slices of the CT image. If your RTSTRUCT is like that, then SlicerRT can probably load it.</p>
<aside class="quote no-group" data-username="kaizhao" data-post="1" data-topic="26964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kaizhao/48/15623_2.png" class="avatar"> kaizhao:</div>
<blockquote>
<p>I have installed the <code>SlicerRT</code> extension and there is no error log when I load the dicom files.</p>
</blockquote>
</aside>
<p>It is strange that there were no errors. It could be helpful if you showed us the DICOM file you wanted to load and explain exactly how you tried to load it.</p>

---
