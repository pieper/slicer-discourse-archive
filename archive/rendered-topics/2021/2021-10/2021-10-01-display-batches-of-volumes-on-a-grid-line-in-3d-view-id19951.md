---
topic_id: 19951
title: "Display Batches Of Volumes On A Grid Line In 3D View"
date: 2021-10-01
url: https://discourse.slicer.org/t/19951
---

# Display batches of volumes on a grid/line in 3D view

**Topic ID**: 19951
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/display-batches-of-volumes-on-a-grid-line-in-3d-view/19951

---

## Post #1 by @JonasLamy (2021-10-01 14:17 UTC)

<p>Hi,</p>
<p>I’ve been using slicer for over 2 years now, it is a great software but the highly modular aspect is a pain to use sometimes.</p>
<p>In particular, visualizing batches of results is really time consuming…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c16767ba44e53482c60cb2be35f476caef454bb.jpeg" data-download-href="/uploads/short-url/6i18neZ8cxusVhKfICfaCEFOWhR.jpeg?dl=1" title="volumes_3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c16767ba44e53482c60cb2be35f476caef454bb_2_531x500.jpeg" alt="volumes_3D" data-base62-sha1="6i18neZ8cxusVhKfICfaCEFOWhR" width="531" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c16767ba44e53482c60cb2be35f476caef454bb_2_531x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c16767ba44e53482c60cb2be35f476caef454bb_2_796x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c16767ba44e53482c60cb2be35f476caef454bb.jpeg 2x" data-dominant-color="D6D2D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volumes_3D</span><span class="informations">972×915 73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Usually, to get this type of visualization, I have to manually go over all the volumes, set the right property for intensities and colors, change the volumes origin and maybe use a transform…</p>
<p>Here are my questions:</p>
<ul>
<li>
<p>Is there a tool to group volumes and apply property changes on a group ? Something along the line of transforms but for properties…</p>
</li>
<li>
<p>Is there an existing tool to display volumes along a line or a grid ? I tried to assign several linear transforms to the same volume, but I couldn’t do so…</p>
</li>
<li>
<p>Would it be possible for 2D views to have an option to de-correlate origin positions when putting 2 volumes on the same view ? With the set up above, I can’t superpose the volumes with the groundtruth…</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f6be83ec9ffd511cb329946d61d55b1c4b8b11b.png" data-download-href="/uploads/short-url/bkAUracIRfT9NKY8zTXjmPsaoYz.png?dl=1" title="volumes_2D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f6be83ec9ffd511cb329946d61d55b1c4b8b11b_2_654x499.png" alt="volumes_2D" data-base62-sha1="bkAUracIRfT9NKY8zTXjmPsaoYz" width="654" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f6be83ec9ffd511cb329946d61d55b1c4b8b11b_2_654x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f6be83ec9ffd511cb329946d61d55b1c4b8b11b_2_981x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f6be83ec9ffd511cb329946d61d55b1c4b8b11b.png 2x" data-dominant-color="1F1410"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volumes_2D</span><span class="informations">1217×930 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Cheers,<br>
Jonas</p>

---

## Post #2 by @lassoan (2021-10-01 19:42 UTC)

<p>You can use examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> how to set up everything you need with a short Python script. If you want to avoid copy-pasting then you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">convert the script into a small Python scripted module</a>.</p>

---

## Post #3 by @pieper (2021-10-01 19:44 UTC)

<p>You can look at the <a href="https://github.com/pieper/CompareVolumes">CompareVolumes</a> module for ideas.</p>

---
