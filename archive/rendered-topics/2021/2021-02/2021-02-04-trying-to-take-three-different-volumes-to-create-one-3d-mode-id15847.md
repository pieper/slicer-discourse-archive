# Trying to take three different volumes to create one 3d model (beginner of 3d slicer)

**Topic ID**: 15847
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/trying-to-take-three-different-volumes-to-create-one-3d-model-beginner-of-3d-slicer/15847

---

## Post #1 by @Guy_Ma (2021-02-04 20:09 UTC)

<p>Operating system:Windows 10<br>
Slicer version: Latest<br>
Expected behavior: I want to use the views that I set in the panels for the 3d model<br>
Actual behavior: Only uses one volume, which makes the 3d model poor quality (because the other two views are pixelated</p>
<p>Im not sure exactly how to do this. I had an MRI recently, and I want to make an interactive model with the scans I got. But when I set it at only one of the volumes, only one of the views is good quality. So I tried setting the other two with the better quality ones (from other volumes) and it only uses one of the volumes at a time. Is it possible to make a new volume using the good quality views only? Thanks!</p>

---

## Post #2 by @lassoan (2021-02-05 04:05 UTC)

<p>MRI images that are acquired like this are good for humans to browse through, but not well suited for 3D volume reconstruction. See more details in this and related posts: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2" class="inline-onebox">Combining volumes - what am I missing? - #2 by lassoan</a></p>

---

## Post #4 by @Guy_Ma (2021-02-06 09:24 UTC)

<p>How do I use NiftyMic? Does it allow me to create a new volume from the three seperate views? I need more information.</p>

---

## Post #5 by @lassoan (2021-02-06 14:30 UTC)

<p>Yes niftymic does exactly that. The only complication is that each method that fills in the huge gaps between the slices only work for the specific anatomy that it is designed for, because you need lots of assumptions to make up a lot of information that is missing from the images.</p>
<p>Niftymic is developed for and reported to work well for infant brain images. If you need to reconstruct such images then there is a good chance that it will work well for you. It may be usable for reconstructing a knee MRI, too, but then probably you will need to tune many parameters. You can start with running niftymic as is, by following instructions on their website, and then ask help from the developers if results are not satisfactory.</p>
<p>If you figure out something, let us know. Many other people are struggling with this and it would be good to know if these superresolution methods work well in practice.</p>

---

## Post #6 by @pieper (2022-06-17 14:22 UTC)

<p>FYI, I was just shown an example where <a href="https://github.com/gift-surg/NiftyMIC#niftymic-applied-to-fetal-brain-mri">NiftyMIC</a> was used to reconstruct a tibia CT dataset with axial, sagittal, and coronal volumes with low out of plane resolution and the results looked pretty good.  So it’s not just for fetal MRI.</p>

---

## Post #7 by @lassoan (2022-06-17 14:30 UTC)

<p>It would be great if you could show some example images or post a link to any paper that will be published about it.</p>

---

## Post #8 by @pieper (2022-06-20 23:42 UTC)

<p>Here is an example available in Daniel’s repo.  The top row is one of the input sets that you can see is crispest in the sagittal plane.  The bottom row is the result of the NiftyMIC process.  In the volume rendering the NiftyMIC result is on the right.  To my eye a definite improvement.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/haehn/blum">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/haehn/blum" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/4ce998c6ece8e0bdd1e998dd8f3b606ab42e9c59e0c42024624cef7f1a2ed7cd/haehn/blum" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/haehn/blum" target="_blank" rel="noopener">GitHub - haehn/blum</a></h3>

  <p>Contribute to haehn/blum development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/745eeb36a3ba34e765bfdeb448104738fe6f9af5.jpeg" data-download-href="/uploads/short-url/gBsKrNPFjMHl4EcjCNLANFdaj4h.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745eeb36a3ba34e765bfdeb448104738fe6f9af5_2_626x500.jpeg" alt="image" data-base62-sha1="gBsKrNPFjMHl4EcjCNLANFdaj4h" width="626" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745eeb36a3ba34e765bfdeb448104738fe6f9af5_2_626x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745eeb36a3ba34e765bfdeb448104738fe6f9af5_2_939x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/745eeb36a3ba34e765bfdeb448104738fe6f9af5_2_1252x1000.jpeg 2x" data-dominant-color="393938"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1659×1325 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/979f5c881a55e56eacdcf71a3aeeea55d7ccaeff.jpeg" data-download-href="/uploads/short-url/lDjwL4da9BUu2iFrmtyMRxsvu6H.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/979f5c881a55e56eacdcf71a3aeeea55d7ccaeff_2_690x275.jpeg" alt="image" data-base62-sha1="lDjwL4da9BUu2iFrmtyMRxsvu6H" width="690" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/979f5c881a55e56eacdcf71a3aeeea55d7ccaeff_2_690x275.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/979f5c881a55e56eacdcf71a3aeeea55d7ccaeff_2_1035x412.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/979f5c881a55e56eacdcf71a3aeeea55d7ccaeff_2_1380x550.jpeg 2x" data-dominant-color="9D99B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1658×661 74.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2022-06-24 12:24 UTC)

<p>Thank you, this looks promising. The enhanced slices seems to sharper, a definite improvement over the original images. The 3D reconstruction is not entirely convincing, because although the staircase artifacts in the reconstructed surface are gone, the surface is still not smooth but has some kind of bumpy grid pattern. The bone thickness seems to be quite different, too, but maybe that’s just due to slightly different volume rendering settings.</p>

---
