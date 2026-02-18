# Meaning of "precision" in unit specification

**Topic ID**: 18087
**Date**: 2021-06-12
**URL**: https://discourse.slicer.org/t/meaning-of-precision-in-unit-specification/18087

---

## Post #1 by @chendong9416 (2021-06-12 02:25 UTC)

<p>Hi, when i change the precision in units setting, it doesn’t work well in the image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8dfd478a4c3bc3513c0f9d61cdcbd76e36039eb.jpeg" data-download-href="/uploads/short-url/o5VLEdbg2ADpXQnkYbMhUzoXEDh.jpeg?dl=1" title="0.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8dfd478a4c3bc3513c0f9d61cdcbd76e36039eb_2_690x161.jpeg" alt="0.PNG" data-base62-sha1="o5VLEdbg2ADpXQnkYbMhUzoXEDh" width="690" height="161" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8dfd478a4c3bc3513c0f9d61cdcbd76e36039eb_2_690x161.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8dfd478a4c3bc3513c0f9d61cdcbd76e36039eb_2_1035x241.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8dfd478a4c3bc3513c0f9d61cdcbd76e36039eb_2_1380x322.jpeg 2x" data-dominant-color="C4C4C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0.PNG</span><span class="informations">3839×896 436 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-12 03:34 UTC)

<p>This works as it should. Precision = 4 means that 4 digits are used for displaying length, and this is what you see (5580 and 4233).</p>

---

## Post #3 by @chendong9416 (2021-06-12 03:45 UTC)

<p>how can i make it accurate to one decimal places?</p>

---

## Post #4 by @lassoan (2021-06-12 03:49 UTC)

<p>There is no fixed decimal display mode. Can you tell a bit about what you are trying to achieve so that we can understand why the current display mode is not appropriate?</p>

---

## Post #5 by @chendong9416 (2021-06-12 04:02 UTC)

<p>i want to make the image show fixed decimal measurement, such as 5.6mm and 42.3mm in this picture</p>

---

## Post #6 by @lassoan (2021-06-12 04:08 UTC)

<p>We need to understand what you are trying to achieve and why the current behavior is problematic for you.</p>

---

## Post #7 by @chendong9416 (2021-06-12 04:35 UTC)

<p>In this picture, the decimal places is not unified;</p>
<p>when we say precision of decimal, we mean that the measurement is accurate to the same decimal places, such as 5.58mm and 42.33mm in this image;</p>
<p>i want the image show the unified decimal places for measurement and the current setting obvious behave in another way.</p>

---

## Post #8 by @lassoan (2021-06-12 13:09 UTC)

<p>It is clear <em>what</em> you want, but we need to understand <em>why</em> because they’re are many ways how this could be achieved and we need to choose solutions that address the underlying need and not just match a particular appearance. For example, these completely different solutions could all result in line length measurements appearing with the same number of decimals:</p>
<ul>
<li>A. add a fixed decimal display mode</li>
<li>B. allow override of display format or precision value for each measurement</li>
<li>C. set line length measurement display precision based on the current zoom factor, or based on what object was visible where you made the measurement (e.g., measure where a high-resolution volume or a continuous surface is visible could result in higher number of decimals displayed).</li>
</ul>
<p>There are good reasons for using the current precision definition. Primarily, it corresponds to a specific error percentage. For example, precision=4 means that you display the value with +/- 0.1% error. Note that these display settings are used everywhere throughout the application, not just when you measure length in an image but when you measure length on a continuous surface (where there is no limitation on precision) or when displaying measurement results or taking length value as input. When you interactively measure length in a view the you typically use a higher zoom factor and you want to see smaller length differences.</p>
<p>We need to understand why the current, generally reasonable behavior is not suitable for your use case. For example, if the distance that you measure is comparable to the voxel size then you may not want to claim that your shorter distance measurements are more accurate. Is this the reason for wanting a fixed number of decimals? Why is it a problem that more digits are displayed for shorter distances? Would you want to use this fixed decimals display for every length value inputs and outputs the application or just for line length measurements? Would you always use the same number of decimals for all length measurements in your scene, or you would use a different value depending on the resolution of the underlying image that you used for that specific measurement?</p>

---

## Post #9 by @chendong9416 (2021-06-13 01:59 UTC)

<p>it is just personal habit, nothing special underlining the thought to unify the decimal places, thank you very much for you detailed reply.</p>

---
