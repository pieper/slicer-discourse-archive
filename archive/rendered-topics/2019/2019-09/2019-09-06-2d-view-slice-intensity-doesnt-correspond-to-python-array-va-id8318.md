# 2D View slice intensity doesn't correspond to python array value（Confusion）

**Topic ID**: 8318
**Date**: 2019-09-06
**URL**: https://discourse.slicer.org/t/2d-view-slice-intensity-doesnt-correspond-to-python-array-value-confusion/8318

---

## Post #1 by @mikecsu (2019-09-06 02:40 UTC)

<p>Operating system:win10<br>
Slicer version:slicer 4.10.0/4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,everyone.  I am trying to understand how slicer 2D images present in the form of an array in python.<br>
So i did some work (see the below pic). The result makes me pretty confused,  the intensity in images and the value in the array should be the same, right ?</p>
<p>I hope someone can help me to clear up my confusion.</p>
<p>Thanks in advance .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b0b0ec9ec81fb2a0f6f26daba0c9d88e4dc29ec.png" data-download-href="/uploads/short-url/jQ23GV0qqThQUzazDecIyuWd5EM.png?dl=1" title="%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE(27)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b0b0ec9ec81fb2a0f6f26daba0c9d88e4dc29ec_2_690x388.png" alt="%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE(27)" data-base62-sha1="jQ23GV0qqThQUzazDecIyuWd5EM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b0b0ec9ec81fb2a0f6f26daba0c9d88e4dc29ec_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b0b0ec9ec81fb2a0f6f26daba0c9d88e4dc29ec_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b0b0ec9ec81fb2a0f6f26daba0c9d88e4dc29ec_2_1380x776.png 2x" data-dominant-color="696B71"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE(27)</span><span class="informations">2560×1440 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-09-06 03:42 UTC)

<p>Numpy uses inverse indexing order (k, j, i).</p>
<p>In the example above, <code>va[138, 277, 163]</code> should give you the results you expect.</p>
<p>See further examples in script repository, such as <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates</a></p>

---
