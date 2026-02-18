# Only flat slices show in 3D view

**Topic ID**: 27194
**Date**: 2023-01-11
**URL**: https://discourse.slicer.org/t/only-flat-slices-show-in-3d-view/27194

---

## Post #1 by @borjaider (2023-01-11 18:03 UTC)

<p>Hello, I have uploaded a dicom folder following all the steps, but on the 3D view I can only see the flat slices. Any idea of why this happens? Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc6c57aef6a86279cbb8f4fe397eb6f032eed80b.png" data-download-href="/uploads/short-url/A12rBNGN75yMypyaI7gsBawSKZZ.png?dl=1" title="renderbone" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc6c57aef6a86279cbb8f4fe397eb6f032eed80b_2_690x316.png" alt="renderbone" data-base62-sha1="A12rBNGN75yMypyaI7gsBawSKZZ" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc6c57aef6a86279cbb8f4fe397eb6f032eed80b_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc6c57aef6a86279cbb8f4fe397eb6f032eed80b_2_1035x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc6c57aef6a86279cbb8f4fe397eb6f032eed80b_2_1380x632.png 2x" data-dominant-color="59596E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">renderbone</span><span class="informations">1912×877 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-01-11 18:06 UTC)

<p>Does <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">enabling/disabling depth peeling</a> in the 3D view makes a difference?</p>
<p>Which Slicer version do you use, on what operating system?</p>

---

## Post #3 by @muratmaga (2023-01-11 19:20 UTC)

<aside class="quote no-group" data-username="borjaider" data-post="1" data-topic="27194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/3ec8ea/48.png" class="avatar"> borjaider:</div>
<blockquote>
<p>Hello, I have uploaded a dicom folder following all the steps, but on the 3D view I can only see the flat slices. Any idea of why this happens? Thank you!</p>
</blockquote>
</aside>
<p>Please turn on the visibility.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/517156cce2c2d01d1f0fc4290fb32022844813f7.png" alt="image" data-base62-sha1="bCtvbgsCLJn2zgLK830eAM9SCHl" width="551" height="161"></p>

---

## Post #4 by @borjaider (2023-01-12 10:06 UTC)

<p>Thank you both! I turned visibility on (sigh) and I see a cylinder, which I am not sure if it is because how the scan was made, or if I can “clean” it so see the bones only. I see the same in all presets, can I fix this? Thanks again!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/551284b21e3e7af3da4f72dc58e44f6a31930293.png" data-download-href="/uploads/short-url/c8Ag8NPJjmioM4maEpzqDeA5ol5.png?dl=1" title="renderbone2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551284b21e3e7af3da4f72dc58e44f6a31930293_2_690x311.png" alt="renderbone2" data-base62-sha1="c8Ag8NPJjmioM4maEpzqDeA5ol5" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551284b21e3e7af3da4f72dc58e44f6a31930293_2_690x311.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551284b21e3e7af3da4f72dc58e44f6a31930293_2_1035x466.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551284b21e3e7af3da4f72dc58e44f6a31930293_2_1380x622.png 2x" data-dominant-color="57576C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">renderbone2</span><span class="informations">1846×833 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @cpinter (2023-01-12 12:40 UTC)

<p>Please read the appropriate sections of the documentation, it will be more efficient for you I think. I’d start here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="inline-onebox">Volume rendering — 3D Slicer documentation</a></p>

---

## Post #6 by @lassoan (2023-01-12 17:31 UTC)

<p>You can try different volume rendering presets to get a nicer appearance.</p>
<p>You can move the “Shift” slider to the right to make the dark region (low voxel values) disappear.</p>

---

## Post #7 by @borjaider (2023-01-13 10:39 UTC)

<p>Thank you all! I think I have it now, I´ll read the documentation in detail, I could not find the issue there.</p>

---
