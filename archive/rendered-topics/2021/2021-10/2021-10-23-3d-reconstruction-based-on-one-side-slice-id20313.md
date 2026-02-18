# 3D reconstruction based on ONE side slice!?

**Topic ID**: 20313
**Date**: 2021-10-23
**URL**: https://discourse.slicer.org/t/3d-reconstruction-based-on-one-side-slice/20313

---

## Post #1 by @Rick44 (2021-10-23 14:23 UTC)

<p>Hi!<br>
I’m really a total noob for this, I just watched some tutorials online without finding my answer, so I don’t know if it’s even possible with this software.</p>
<p>I would like to create a 3d reconstruction model based on only one sequence of 100-200 black and white slices in JPGs.<br>
This means I only have one point of view (left) of the “object”.<br>
Can I do this?<br>
If it is possible can you point me to one or more ressources on how to do this?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-10-23 15:28 UTC)

<p>This should be no problem, you can load the JPEG images as an image stack and then convert it to a segmentation. See detailed instructions here:</p>
<ul>
<li>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html?highlight=jpeg#load-a-series-of-png-jpeg-or-tiff-images-as-volume">Load a jpeg image stack as a volume</a>. For very large image stacks, I would recommend to use ImageStacks module (in SlicerMorph extension).</li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">Convert a volume to segmentation</a></li>
</ul>

---

## Post #3 by @Rick44 (2021-10-23 22:42 UTC)

<p>Thanks! It worked nicely.<br>
I’ll have to get into the fine settings to have the best result but it’s a real good start, thank you!<br>
Is there a way to increase the resolution of the 3d model? Or does it have to do with the resolution of the initial JPG sequence?</p>

---

## Post #4 by @lassoan (2021-10-23 23:45 UTC)

<p>The resolution is determined by the input images.</p>

---

## Post #5 by @Rick44 (2021-10-24 02:01 UTC)

<p>Sir, you’ve solved my problem.<br>
Thank you</p>

---
