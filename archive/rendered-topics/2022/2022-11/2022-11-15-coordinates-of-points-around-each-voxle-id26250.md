# Coordinates of points around each voxle

**Topic ID**: 26250
**Date**: 2022-11-15
**URL**: https://discourse.slicer.org/t/coordinates-of-points-around-each-voxle/26250

---

## Post #1 by @ZSoltani (2022-11-15 17:23 UTC)

<p>Hello all,</p>
<p>I need to extract the coordinates of corner points around each voxel, for all voxels. Is there any way to do that?</p>
<p>The resolution of the voxels are shown in the below picture, after turning off the interpolation option.</p>
<p>Thanks,<br>
Zahra</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3134f1325b7cdbcb5c89e55eaade682d07550c9f.png" data-download-href="/uploads/short-url/71iP5ZaKbHZq4ThlDlazuNDZSGP.png?dl=1" title="Screenshot from 2022-11-15 12-17-37" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3134f1325b7cdbcb5c89e55eaade682d07550c9f_2_690x397.png" alt="Screenshot from 2022-11-15 12-17-37" data-base62-sha1="71iP5ZaKbHZq4ThlDlazuNDZSGP" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3134f1325b7cdbcb5c89e55eaade682d07550c9f_2_690x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3134f1325b7cdbcb5c89e55eaade682d07550c9f_2_1035x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3134f1325b7cdbcb5c89e55eaade682d07550c9f_2_1380x794.png 2x" data-dominant-color="929298"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-15 12-17-37</span><span class="informations">2163×1246 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-11-15 23:19 UTC)

<p>Yes, the mapping between voxel coordinates (IJK in Slicer) and world, or RAS coordinates is defined by the IJKToRAS matrix.  There are <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-centroid-of-a-segment-in-world-ras-coordinates">examples</a> of this mapping.  The IJK of 0,0,0 maps to the center of the first voxel in the volume, so you need to add 1/2 voxel offsets in all directions to get the coordinates of the corners.</p>

---

## Post #3 by @ZSoltani (2022-11-17 18:56 UTC)

<p>Thanks Steve for your reply.<br>
Zahra</p>

---
