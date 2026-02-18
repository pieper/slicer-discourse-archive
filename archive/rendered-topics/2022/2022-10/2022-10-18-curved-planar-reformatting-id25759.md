# Curved planar reformatting

**Topic ID**: 25759
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/curved-planar-reformatting/25759

---

## Post #1 by @anusree_sunilkumar (2022-10-18 15:35 UTC)

<p>I have been trying to implement curved planar reformatting using the code from this github link <a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" rel="noopener nofollow ugc">Computing a panoramic X-ray from a cone-beam dental CT. Demonstration of how an image can be resampled along a curve - the code is not optimized for performance or quality and distance along curve is not scaled (we simply used all point indices instead of retrieving point indices based on desired distance along curve). · GitHub</a><br>
I am not getting the intended result with the newer version(Mine is same as the one in the comment posted by <span class="mention">@ndavoudi</span>). Also I need to try it on my own dataset. Please guide me.<br>
My intention is to generate a panoramic view of my 3d CT dataset.<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2022-10-18 16:20 UTC)

<p>That code was completely reworked and made much more robust and a module with a convenient GUI was created from it. The “Cuved Planar Reformat” module is available in the Sandbox extension and you can use it either via GUI or <a href="https://github.com/PerkLab/SlicerSandbox/blob/8235ee89a2e5223dc63a9a6dfa7c316708afb066/CurvedPlanarReformat/CurvedPlanarReformat.py#L395-L430">Python script</a>.</p>

---

## Post #3 by @anusree_sunilkumar (2022-10-19 09:10 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/694c9318abab2acece4b7a185042052f9a9df50b.png" data-download-href="/uploads/short-url/f1wc4t0VKofNOXPu7vyOk3Vvr1F.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/694c9318abab2acece4b7a185042052f9a9df50b_2_690x294.png" alt="image" data-base62-sha1="f1wc4t0VKofNOXPu7vyOk3Vvr1F" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/694c9318abab2acece4b7a185042052f9a9df50b_2_690x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/694c9318abab2acece4b7a185042052f9a9df50b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/694c9318abab2acece4b7a185042052f9a9df50b.png 2x" data-dominant-color="A8A8A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">889×380 69.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I tried using the module. This is what I am getting. Not sure if I am doing it right way.</p>

---

## Post #4 by @lassoan (2022-10-19 13:23 UTC)

<p>Yes, this looks perfect.</p>

---
