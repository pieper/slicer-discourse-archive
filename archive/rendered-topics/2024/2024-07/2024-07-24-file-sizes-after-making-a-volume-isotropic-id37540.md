# File sizes after making a volume isotropic

**Topic ID**: 37540
**Date**: 2024-07-24
**URL**: https://discourse.slicer.org/t/file-sizes-after-making-a-volume-isotropic/37540

---

## Post #1 by @coco (2024-07-24 09:48 UTC)

<p>Dear all,<br>
I was astonished to see a dramatic drop in file size after using the crop volume module and I don’t understand why.<br>
Here is my original volume volume information:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df7a009c8adb8bc913f87ba68441d3a3db7f19f8.png" alt="image" data-base62-sha1="vSXRCnmWdXNJM0OYwyKsQsSg4mQ" width="594" height="244"><br>
Now this is my new volume information after crop volume (using a roi to the full frame, B spline and isotropic spacing):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e9e616d6867b3ac46befadbcaac601185315cb.png" alt="image" data-base62-sha1="8gklbjziq96ZTY8x7B9Bg87qk1t" width="649" height="208"><br>
Note that I changed the units in the _iso file manually to the right scale (um instead of mm) before running the crop volume</p>
<p>Now if I save the isotropic file, the space used on disk is 2.3 G compared to 6.3 G for the original file.</p>
<p>How come ?</p>
<p>Many thanks to the community and developpers for help and of course, a great software !</p>

---

## Post #2 by @muratmaga (2024-07-24 16:18 UTC)

<p>Your second volume (the one generated after cropping) is actually larger than the original one (there are more voxels in Z dimension).</p>
<p>If you choose to compress the file during the save, the file size will be smaller than the memory footprint required to load the file. I presume your original file was not compressed. So that’s probably where the difference is coming from.</p>
<p>For large files like this, I suggest not compressing them. Most of the wait during the save/open operations are actually spend on compressing/uncompressing them as the compression library used is single-threaded.</p>

---

## Post #3 by @coco (2024-07-25 07:44 UTC)

<p>Thanks Murat,<br>
indeed I expected files larger, not smaller as there are more voxels in the Z dimensions.<br>
In the save tab, I clicked on show options and noticed “compress” was checked. I had forgotten about that option but I probably did this voluntary at some point: I think in my case, storage space is more of a concern than time openning/saving (it s still very fast on my cluster, for files up to 15 GB, I hardly wait).<br>
Perhaps that option should not be “hidden” as I simply forgot about that and went along my pipeline.<br>
S</p>

---

## Post #4 by @muratmaga (2024-07-25 12:41 UTC)

<p>If you are using SlicerMorph, go to Application Settings-&gt;SlicerMorph then check use SlicerMorph customizations and restart Slicer. This will disable compression option for all your volume data.</p>

---
