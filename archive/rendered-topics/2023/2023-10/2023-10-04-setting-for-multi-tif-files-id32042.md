---
topic_id: 32042
title: "Setting For Multi Tif Files"
date: 2023-10-04
url: https://discourse.slicer.org/t/32042
---

# Setting for multi tif files

**Topic ID**: 32042
**Date**: 2023-10-04
**URL**: https://discourse.slicer.org/t/setting-for-multi-tif-files/32042

---

## Post #1 by @jp_jp_jp (2023-10-04 20:59 UTC)

<p>Hi, I have a group of tif files that are slicers of the subject, so now what I am doing is adding the folder of the tif files, then Slicer will show me the whole object, but when the CT scanning was performed, there was a voxel spacing, I didn’t find place to input this number, thank you!</p>

---

## Post #2 by @muratmaga (2023-10-04 21:35 UTC)

<p>If you use the <code>Imagestack</code> module within the SlicerMorph, your life will be a bit simpler. You can see the tutorial for the Imagestacks at the <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a> (and others)</p>
<p>Meanwhile if you need to fix the spacing, go to <code>Volumes</code> module and manually edit the spacing as provided to you by the imaging lab, and then remember to re-save your file.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cb9e3b474e242f7d7f5cc6ae1c93140ae8df65d.png" alt="Screen Shot 2023-10-04 at 2.37.24 PM" data-base62-sha1="mmsKBIw7R0Ig3vgLm7a6MfbJerP" width="670" height="500"></p>

---
