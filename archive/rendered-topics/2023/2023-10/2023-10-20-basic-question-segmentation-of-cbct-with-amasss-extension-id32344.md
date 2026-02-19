---
topic_id: 32344
title: "Basic Question Segmentation Of Cbct With Amasss Extension"
date: 2023-10-20
url: https://discourse.slicer.org/t/32344
---

# Basic question: Segmentation of CBCT with AMASSS extension

**Topic ID**: 32344
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/basic-question-segmentation-of-cbct-with-amasss-extension/32344

---

## Post #1 by @bellfounder (2023-10-20 14:10 UTC)

<p>Operating system: MacOS 14.0<br>
Slicer version: 5.5.0<br>
Expected behavior: Get a segmented model<br>
Actual behavior: Being prompted to select a scan folder<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdfe59fdc5c30b4d0efd14c5785e2138991a3a0c.jpeg" data-download-href="/uploads/short-url/r6LbCWL9oCKzhCam4zJnzLp0Ke0.jpeg?dl=1" title="Bildschirmfoto 2023-10-20 um 12.09.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfe59fdc5c30b4d0efd14c5785e2138991a3a0c_2_493x500.jpeg" alt="Bildschirmfoto 2023-10-20 um 12.09.15" data-base62-sha1="r6LbCWL9oCKzhCam4zJnzLp0Ke0" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfe59fdc5c30b4d0efd14c5785e2138991a3a0c_2_493x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfe59fdc5c30b4d0efd14c5785e2138991a3a0c_2_739x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdfe59fdc5c30b4d0efd14c5785e2138991a3a0c_2_986x1000.jpeg 2x" data-dominant-color="AFAFBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2023-10-20 um 12.09.15</span><span class="informations">1920×1946 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi everyone. Sorry if this is a stupid question. I tried to segment a CBCT file of the maxilla using the AMASSS extension. I set input type as DICOM and entered the correct folder. The model was also downloaded. See screenshot.</p>
<p>After hitting the ‘Run prediction’ button I get a prompt that I should select a scan folder. I thought that this is my DICOM file. What am I doing wrong?</p>
<p>Thanks a lot in advance!<br>
Best,<br>
Jörg</p>

---

## Post #2 by @mau_igna_06 (2023-10-20 16:28 UTC)

<p>I have use it to segment a mandible by:</p>
<ol>
<li>First, uploading the DICOM data to Slicer</li>
<li>Then, open the DICOM browser and load your CBCT</li>
<li>Then open AMASSS module and use it</li>
</ol>
<p>Hope it helps</p>

---

## Post #3 by @bellfounder (2023-10-21 13:46 UTC)

<p>Thank you Mauro! I greatly appreciate your help which really helped me. I could now start the computing. Unfortunately, the processing seems to have gotten stuck (see image attached. Do you have any idea what ist the reason?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/798e931aae43807b8e9d3842a931f6d9ad57ff86.jpeg" data-download-href="/uploads/short-url/hlleNnkdtWuAa0NNrWK0DM6mhQW.jpeg?dl=1" title="Bildschirmfoto 2023-10-21 um 15.42.24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/798e931aae43807b8e9d3842a931f6d9ad57ff86_2_663x500.jpeg" alt="Bildschirmfoto 2023-10-21 um 15.42.24" data-base62-sha1="hlleNnkdtWuAa0NNrWK0DM6mhQW" width="663" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/798e931aae43807b8e9d3842a931f6d9ad57ff86_2_663x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/798e931aae43807b8e9d3842a931f6d9ad57ff86_2_994x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/798e931aae43807b8e9d3842a931f6d9ad57ff86_2_1326x1000.jpeg 2x" data-dominant-color="9596A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2023-10-21 um 15.42.24</span><span class="informations">1920×1447 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Another question is: Tooth segmentation is greyed out. Is there a way to be able to have the teeth and roots be segmented? My special interest are the roots of the teeth.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a501635bdb032691a50e8b9e24abe4aef6315b0.png" data-download-href="/uploads/short-url/faucd5I9KpqrbNkdBtowtYMPTvG.png?dl=1" title="Bildschirmfoto 2023-10-21 um 16.04.19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a501635bdb032691a50e8b9e24abe4aef6315b0_2_429x500.png" alt="Bildschirmfoto 2023-10-21 um 16.04.19" data-base62-sha1="faucd5I9KpqrbNkdBtowtYMPTvG" width="429" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a501635bdb032691a50e8b9e24abe4aef6315b0_2_429x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a501635bdb032691a50e8b9e24abe4aef6315b0_2_643x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a501635bdb032691a50e8b9e24abe4aef6315b0_2_858x1000.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2023-10-21 um 16.04.19</span><span class="informations">1054×1226 92.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks again!<br>
Best, Jörg</p>

---
