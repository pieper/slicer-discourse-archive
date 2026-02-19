---
topic_id: 28303
title: "Slicerlookingglass Extension Slicer Models Are Stretched And"
date: 2023-03-11
url: https://discourse.slicer.org/t/28303
---

# SlicerLookingGlass Extension: Slicer models are stretched and distorted on the Quilt

**Topic ID**: 28303
**Date**: 2023-03-11
**URL**: https://discourse.slicer.org/t/slicerlookingglass-extension-slicer-models-are-stretched-and-distorted-on-the-quilt/28303

---

## Post #1 by @mircat (2023-03-11 02:18 UTC)

<p>Hello!</p>
<p>When generating a quilt using the SlicerLookingGlass Module, the Slicer model becomes stretched, resulting in a blurry and distorted image on the Looking Glass Portrait. See image below. I have a cube model which is elongated as a rectangular prism in the quilt.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5ede4152b06f3ca275232d38d153bbb4a6f3177.png" data-download-href="/uploads/short-url/uwvnzwXi793EaQgZjl7IKcRkI4v.png?dl=1" title="distorted cube" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5ede4152b06f3ca275232d38d153bbb4a6f3177_2_690x322.png" alt="distorted cube" data-base62-sha1="uwvnzwXi793EaQgZjl7IKcRkI4v" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5ede4152b06f3ca275232d38d153bbb4a6f3177_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5ede4152b06f3ca275232d38d153bbb4a6f3177_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5ede4152b06f3ca275232d38d153bbb4a6f3177_2_1380x644.png 2x" data-dominant-color="A3A5AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">distorted cube</span><span class="informations">1918×896 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I first encountered blurriness on the Looking Glass Portrait I was able to resolve it by changing settings in Windows so that the scaling of the Looking Glass was at 100% instead of 250%.</p>
<p>Strangely, the blurriness of the display has returned despite the Windows scaling still being set at 100%.</p>
<p>I also notice that the quilt produced by Slicer is a 9x5. Is there a way to change the source code of the SlicerLookingGlass extension so that the quilt can be an 8x6, which is recommended by Looking Glass Factory for my Portrait display?</p>

---

## Post #2 by @lassoan (2023-03-11 16:41 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> can you help with this?</p>

---

## Post #3 by @jcfr (2023-03-20 14:03 UTC)

<p>Thanks for the details report.</p>
<p>The SlicerLookingGlass needs to be updated to build against the latest version of the associated VTK modules.</p>
<p>Waiting we allocate resources to work on this, let me know if you would some guidance to work on the update.</p>

---
