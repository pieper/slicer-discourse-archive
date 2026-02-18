# Segment Editor: Threshold with masking

**Topic ID**: 5042
**Date**: 2018-12-11
**URL**: https://discourse.slicer.org/t/segment-editor-threshold-with-masking/5042

---

## Post #1 by @ihnorton (2018-12-11 15:21 UTC)

<p>I am trying to use the Segment Editor Threshold tool with a mask. I select a subregion, the segment named <code>mask</code> in yellow, and set that segment as the <code>Editable Area</code>. Then I add a second segment, and select an intensity range with the Threshold tool. The preview extends outside the mask, but that’s ok. The view is [1] below. Next I select a range and hit <code>Apply</code>, which results in a subtraction from the <code>mask</code> segment, rather than Segment_2 containing only the thresholded region inside <code>mask</code>. Is this expected, a bug, or user error?</p>
<p>(I’ve also managed several times to get in a state in which none of the tools are responsive until I delete all segments, but I don’t have a reproduction workflow yet)</p>
<h1><a name="p-18764-h-1-1" class="anchor" href="#p-18764-h-1-1" aria-label="Heading link"></a>1</h1>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23dc2a021a46ce3f416294ce6b9ac49ef763b3ab.png" data-download-href="/uploads/short-url/57eptm8nMaC39Go0CR1CbsID2fV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23dc2a021a46ce3f416294ce6b9ac49ef763b3ab_2_421x500.png" alt="image" data-base62-sha1="57eptm8nMaC39Go0CR1CbsID2fV" width="421" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23dc2a021a46ce3f416294ce6b9ac49ef763b3ab_2_421x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23dc2a021a46ce3f416294ce6b9ac49ef763b3ab_2_631x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23dc2a021a46ce3f416294ce6b9ac49ef763b3ab.png 2x" data-dominant-color="CBCCCB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">757×898 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h1><a name="p-18764-h-2-2" class="anchor" href="#p-18764-h-2-2" aria-label="Heading link"></a>2</h1>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dd6c71a05484f9a8f2e60c44f054f31bf32f364.png" data-download-href="/uploads/short-url/do8yXMuOlvp3dta2WK9t6tJK0vy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dd6c71a05484f9a8f2e60c44f054f31bf32f364.png" alt="image" data-base62-sha1="do8yXMuOlvp3dta2WK9t6tJK0vy" width="172" height="145"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">172×145 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ihnorton (2018-12-11 15:34 UTC)

<p>This is Slicer 4.10.0 on macOS 10.13 by the way.</p>

---

## Post #3 by @lassoan (2018-12-11 15:50 UTC)

<p>What you describe seems to be the expected behavior: if in masking section “Overwrite other segments” is left at default value of “All segments” then you overwrite the mask segment when you draw in another segment.</p>
<p>For masking with a segment, I usually hide the mask segment and set “Overwrite other segments” to “Visible segments”.</p>

---

## Post #4 by @ihnorton (2018-12-11 16:41 UTC)

<p>Ok, that works. Thanks! I had tried setting “Overwrite other segments” to “None”, but that didn’t seem to work.</p>
<p>One minor thing I noticed, not sure if it is worth a bug report: switching the selected segment while the Threshold tool is active removes the content of the previously-selected segment. (<a href="https://www.dropbox.com/s/v9h0qynbreokpi0/thr-screencap.gif?dl=0" rel="nofollow noopener">screencap</a>)</p>

---

## Post #5 by @lassoan (2018-12-11 21:57 UTC)

<p>Thanks for reporting. Opacity of the segment is set to 0 and not reverted if we switch to another segment (you can restore it in Segmentations module / Display / Advanced). I’ll fix this.</p>

---

## Post #6 by @lassoan (2018-12-12 14:56 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="4" data-topic="5042">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>One minor thing I noticed, not sure if it is worth a bug report: switching the selected segment while the Threshold tool is active removes the content of the previously-selected segment.</p>
</blockquote>
</aside>
<p>This has been fixed now (in r27625).</p>

---
