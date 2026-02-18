# Show two volumes overlaid

**Topic ID**: 2626
**Date**: 2018-04-18
**URL**: https://discourse.slicer.org/t/show-two-volumes-overlaid/2626

---

## Post #1 by @anitakh1 (2018-04-18 07:02 UTC)

<p>hello, is it possible to see two volumes one over other. like i want to put segmented output result on original images. how to do it using slicer?</p>

---

## Post #2 by @lassoan (2018-04-18 14:19 UTC)

<p>Yes, and there are many visualization options. You can overlay any number of segmentations over a grayscale volume, both in slice and 3D views. You can also overlay two grayscale volumes and a labelmap volume in each slice viewer, and display these slices in 3D. You can display grayscale volume using volume rendering in 3D.</p>
<p>Have you completed <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#General_Introduction">Slicer introduction tutorials</a>? If you still have questions then let us know.</p>

---

## Post #5 by @mikbuch (2023-02-18 23:33 UTC)

<p>Hi, just a quick shortcut if anybody else would be trying to get this simple functionality:</p>
<ol>
<li>
<p>Load and display one of the volumes.</p>
</li>
<li>
<p>Click the “double arrow” option from the top bar in one of the views (screenshot below):</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad9f01693e9b714380ed4398273c1d0cae69446c.jpeg" data-download-href="/uploads/short-url/oLVgKmFtNPiovf9N5q4HqSvzQv2.jpeg?dl=1" title="Screenshot 2023-02-19 at 00.29.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9f01693e9b714380ed4398273c1d0cae69446c_2_690x419.jpeg" alt="Screenshot 2023-02-19 at 00.29.06" data-base62-sha1="oLVgKmFtNPiovf9N5q4HqSvzQv2" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9f01693e9b714380ed4398273c1d0cae69446c_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9f01693e9b714380ed4398273c1d0cae69446c_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9f01693e9b714380ed4398273c1d0cae69446c_2_1380x838.jpeg 2x" data-dominant-color="4D464A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-02-19 at 00.29.06</span><span class="informations">1920×1166 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="3">
<li>
<p>Set up your view.</p>
</li>
<li>
<p>Optionally: set up colours for volumes using the “Volumes” module (see the above screenshot).</p>
</li>
</ol>
<p>Bonus: you can also display segments (and labels) on top of the overlaid images.</p>
<p>I found out how to do it thanks to this post: <a href="https://discourse.slicer.org/t/visualization-of-the-background-and-foreground-image-together/4981/2" class="inline-onebox">Visualization of the background and foreground image together - #2 by cpinter</a></p>

---

## Post #6 by @Sheryl (2024-05-16 08:11 UTC)

<p>I am wondering what does ‘50%’ mean after the foreground?</p>

---

## Post #7 by @hannaho (2024-05-16 11:26 UTC)

<p>Hi Sheryl,</p>
<p>That’s an opacity setting. You can change how ‘see through’ the foreground layer is with the scrolling bar on the left.</p>

---
