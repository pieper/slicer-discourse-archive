# How to reduce lung segmentation time?

**Topic ID**: 31799
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/how-to-reduce-lung-segmentation-time/31799

---

## Post #1 by @mikiN (2023-09-20 10:30 UTC)

<p>When using the AI function of CTlungsegmentation (lungmask R231CovidWeb), segmentation takes more than 3 minutes. The spec of the PC used is RTX3050ti 4GB. What can I improve?</p>

---

## Post #2 by @lassoan (2023-09-20 12:48 UTC)

<p>3 minutes is a really good considering the time and effort you would need to do the work manually and this short computation time is most often acceptable even in intraprocedural workflows. There are <a href="https://gpu.userbenchmark.com/Compare/Nvidia-RTX-4090-vs-Nvidia-RTX-3050-Ti-Laptop/4136vsm1559532"><em>much</em> faster GPUs available</a>, so a trivial option for making segmentation faster is to upgrade your hardware.</p>

---

## Post #3 by @cong_lu (2023-10-27 00:05 UTC)

<p>Hello, I’m wondering how to use the AI function, lungmask R231CovidWeb, in 3D Slicer? I didn’t find the extension.</p>

---

## Post #4 by @rbumm (2023-10-27 04:08 UTC)

<p>Please install the Lung CT Analyzer extension. Lung CT Segmenter is part of it and this includes support for lungmask R231CovidWeb.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf2eae9ca94f20999b3c05191bb548ba3d0ff016.png" alt="image" data-base62-sha1="tyOQQ8GRnpTG387hO1QKgUBGYOa" width="580" height="169"></p>

---

## Post #5 by @cong_lu (2023-10-27 16:54 UTC)

<p>Dear rbumn,<br>
Thank you for your reply. However, I use the version 5.4 but there might be something wrong with my Lung CT Segmenter. Please check the attached screenshot. I didn’t see “very low detail” or “lungmask R231CovidWeb” in your screenshot. Also there is no reaction after clicking the “Start”.<br>
Thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd57da00e6cb573fc9211c505a510a4d14178b4c.jpeg" data-download-href="/uploads/short-url/tiy6miLc4l4ANyc4i9n5D8PP7OY.jpeg?dl=1" title="Screenshot 2023-10-27 at 12.50.18 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd57da00e6cb573fc9211c505a510a4d14178b4c_2_690x448.jpeg" alt="Screenshot 2023-10-27 at 12.50.18 PM" data-base62-sha1="tiy6miLc4l4ANyc4i9n5D8PP7OY" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd57da00e6cb573fc9211c505a510a4d14178b4c_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd57da00e6cb573fc9211c505a510a4d14178b4c_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd57da00e6cb573fc9211c505a510a4d14178b4c_2_1380x896.jpeg 2x" data-dominant-color="BFBCBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-27 at 12.50.18 PM</span><span class="informations">1920×1249 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @rbumm (2023-10-27 17:25 UTC)

<p>Sorry for the problem.<br>
Please install the TotalSegmentator extension, restart 3D Slicer, and try the Segmenter again.<br>
I will push an update soon to avoid this error.</p>

---

## Post #7 by @cong_lu (2023-10-27 17:33 UTC)

<p>Thanks rbumm.<br>
I followed your instruction but still not working.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18b527616f866311caef6297ee91416200269c75.jpeg" data-download-href="/uploads/short-url/3wzzVULHRUBDSZVGe0f4lkfSNMh.jpeg?dl=1" title="Screenshot 2023-10-27 at 1.32.40 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b527616f866311caef6297ee91416200269c75_2_690x448.jpeg" alt="Screenshot 2023-10-27 at 1.32.40 PM" data-base62-sha1="3wzzVULHRUBDSZVGe0f4lkfSNMh" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b527616f866311caef6297ee91416200269c75_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b527616f866311caef6297ee91416200269c75_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b527616f866311caef6297ee91416200269c75_2_1380x896.jpeg 2x" data-dominant-color="ABA9A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-27 at 1.32.40 PM</span><span class="informations">1920×1249 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>here is my installed extension.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faf222c4571c51e5facefc858822ba8ad75dd5a4.jpeg" data-download-href="/uploads/short-url/zNY8KJlyLWR6DS0xT3sVxWmpd1q.jpeg?dl=1" title="Screenshot 2023-10-27 at 1.29.44 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/faf222c4571c51e5facefc858822ba8ad75dd5a4_2_690x448.jpeg" alt="Screenshot 2023-10-27 at 1.29.44 PM" data-base62-sha1="zNY8KJlyLWR6DS0xT3sVxWmpd1q" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/faf222c4571c51e5facefc858822ba8ad75dd5a4_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/faf222c4571c51e5facefc858822ba8ad75dd5a4_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/faf222c4571c51e5facefc858822ba8ad75dd5a4_2_1380x896.jpeg 2x" data-dominant-color="EDECEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-27 at 1.29.44 PM</span><span class="informations">1920×1249 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @rbumm (2023-10-27 17:58 UTC)

<p>That selection of extensions looks good, where is 3D Slicer installed? Could that be an access problem where certain rights are missing when you run Slicer ? I see that Lung CT Segmenter is not initialized correctly.<br>
Could you post the content of the Python interactor during startup ?</p>

---

## Post #9 by @cong_lu (2023-10-27 18:16 UTC)

<p>I’m currently using MacBook air with M2 chip, the macos is 13.2.1. I installed 3D Slicer at Application.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b971ed2e11f6568dcfcd1f18504e308799b9ab.jpeg" data-download-href="/uploads/short-url/wcQKbISKwA6IJk2AoI0GcQJmcEH.jpeg?dl=1" title="Screenshot 2023-10-27 at 2.12.59 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b971ed2e11f6568dcfcd1f18504e308799b9ab_2_690x448.jpeg" alt="Screenshot 2023-10-27 at 2.12.59 PM" data-base62-sha1="wcQKbISKwA6IJk2AoI0GcQJmcEH" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b971ed2e11f6568dcfcd1f18504e308799b9ab_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b971ed2e11f6568dcfcd1f18504e308799b9ab_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1b971ed2e11f6568dcfcd1f18504e308799b9ab_2_1380x896.jpeg 2x" data-dominant-color="CCC6C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-27 at 2.12.59 PM</span><span class="informations">1920×1249 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>PS: I’ve also tried a Windows PC today, with freshly installed 3D and extension, which was facing same problem.</p>

---

## Post #10 by @rbumm (2023-10-27 18:27 UTC)

<p>Please update Lung CT Analyzer tomorrow, select the ct chest sample volume and report back with the same display. Make sure your computer has access to the internet.</p>

---

## Post #11 by @cong_lu (2023-10-30 17:50 UTC)

<p>Dear rbumm,<br>
After update Lung Ct Analyzer to latest version, It works well with the Chest sample data.<br>
Thanks for your support!</p>

---
