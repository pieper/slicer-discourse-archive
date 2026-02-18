# VMTK centerline extraction

**Topic ID**: 21577
**Date**: 2022-01-22
**URL**: https://discourse.slicer.org/t/vmtk-centerline-extraction/21577

---

## Post #1 by @Pavel_Zhabyeyev (2022-01-22 15:55 UTC)

<p>I have used VMTK centerline extraction to extract centerline from the example aorta with manually placed 2 points.</p>
<p>However, the procedure does not work for multiple point (&gt;2) on the same aorta example from the library. One point was seeded, used auto-detect to find more, and deleted some non-relevant end points. Once I try to run the module, It gets stuck in “Generate curves and quantification tables” for tens of minutes. Allocated memory grows and grows: it grew to 80 Gb out of 128 Gb in 20-25 min after that I have shutdown the slicer.</p>
<p>I am using the recent version for Windows.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3974eca60a9475ab4ceab4bc463439012f0bab91.png" data-download-href="/uploads/short-url/8chIXGOxcoAQRRHtfUcfsmPvcL7.png?dl=1" title="HungUp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_690x388.png" alt="HungUp" data-base62-sha1="8chIXGOxcoAQRRHtfUcfsmPvcL7" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3974eca60a9475ab4ceab4bc463439012f0bab91_2_1380x776.png 2x" data-dominant-color="B9BADB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">HungUp</span><span class="informations">1920×1080 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2022-01-22 20:09 UTC)

<p>As <a class="mention" href="/u/mikebind">@mikebind</a> <a href="https://discourse.slicer.org/t/vmtk-centerline-extraction-trouble/16983/11">said</a>, VMTK has been functioning nicely for years. You have really a lot of endpoints, do you really need so many centerlines ?</p>
<p>Try simply with two endpoints that you manually place in the aorta itself, and increase progressively focusing on your project’s end goals.</p>
<p>If you don’t get any centerline at all, you can use ‘Smoothing’ effect in ‘Segment editor’, with ‘Fill holes’ options. The default kernel size is 3mm, it should be suitable. But sometimes, it has to be increased to 6 or 9, rarely more. Then restart creating simple centerlines.</p>
<p>In the ‘Advanced’ section of ‘Extract centerline’, ‘Subdivide’ often helps, as well as reducing ‘Decimation aggressiveness’. Disabling ‘Preprocess input surface’ may be useful too.</p>
<p>Explore further, an aorta should be processed successfully.</p>

---

## Post #3 by @Pavel_Zhabyeyev (2022-01-24 22:18 UTC)

<p>Thank you chir.set for the tips.</p>
<p>After several tries, I have found what was the problem. Centerline Curve and Centerline Properties must not be selected until centerline build, or the slicer will hung up at the last step. The centerline must be extracted first. Only than, these parameters must be set (see below).</p>
<p>I think the procedure needs to be more robust to user input.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f92f87a6adee299fe6caa49e55f7b146e590877.png" data-download-href="/uploads/short-url/fV1SHCJXE0knjHT2O8LVK3slNsP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f92f87a6adee299fe6caa49e55f7b146e590877_2_690x466.png" alt="image" data-base62-sha1="fV1SHCJXE0knjHT2O8LVK3slNsP" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f92f87a6adee299fe6caa49e55f7b146e590877_2_690x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f92f87a6adee299fe6caa49e55f7b146e590877_2_1035x699.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f92f87a6adee299fe6caa49e55f7b146e590877.png 2x" data-dominant-color="C8C6DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1370×926 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
