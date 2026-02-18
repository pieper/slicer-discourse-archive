# Move a model along a straight line by script

**Topic ID**: 28046
**Date**: 2023-02-25
**URL**: https://discourse.slicer.org/t/move-a-model-along-a-straight-line-by-script/28046

---

## Post #1 by @slicer365 (2023-02-25 07:49 UTC)

<p>Dear friends<br>
I have creat a model by Slicer, I can get the model’s node ID,</p>
<p>now I want to move the model along a straight line by script,   let the direction of movement is parallel to this line.</p>
<p>I can creat a line by Markups module, then get the line’s nodeID.</p>
<p>or I just get two points’RAS on the line</p>
<p>Anyone can tell me how to write a python script? Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21b5199aa30a6c0c943a8b2707b0af6bb53f16f3.png" data-download-href="/uploads/short-url/4ObLdhmp3BP9x0Vfw6aPYEyy99h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21b5199aa30a6c0c943a8b2707b0af6bb53f16f3_2_517x264.png" alt="image" data-base62-sha1="4ObLdhmp3BP9x0Vfw6aPYEyy99h" width="517" height="264" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21b5199aa30a6c0c943a8b2707b0af6bb53f16f3_2_517x264.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21b5199aa30a6c0c943a8b2707b0af6bb53f16f3_2_775x396.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21b5199aa30a6c0c943a8b2707b0af6bb53f16f3_2_1034x528.png 2x" data-dominant-color="CCCBF8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1607×820 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-02-25 17:14 UTC)

<p>You should be able to copy the way the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py">endoscopy module</a> does this.  Look for the <code>self.transform</code> and how it is used to move the cursor model along the path.</p>

---
