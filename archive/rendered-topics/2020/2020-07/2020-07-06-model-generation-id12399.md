---
topic_id: 12399
title: "Model Generation"
date: 2020-07-06
url: https://discourse.slicer.org/t/12399
---

# Model Generation

**Topic ID**: 12399
**Date**: 2020-07-06
**URL**: https://discourse.slicer.org/t/model-generation/12399

---

## Post #1 by @IanH (2020-07-06 16:52 UTC)

<p>Using help given on other posts I’ve made on here I’ve been able to make a nice looking model on the 3D view panel in the software. However, when I export the file to a .obj file it comes through as just a solid block. Does anybody know how to export only certain elements of the segmentation? Or am I able to make a model that can be printed in the 3D slicer software itself? Any help would be appreciated and I have attached pictures.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0f69f6dc6f68b152b7f54d5cf09b495a49afbc9.jpeg" data-download-href="/uploads/short-url/ynEYKaAy8CFeETgKoRTjgr3YN6x.jpeg?dl=1" title="C0000218 Slicer View.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0f69f6dc6f68b152b7f54d5cf09b495a49afbc9_2_690x305.jpeg" alt="C0000218 Slicer View.PNG" data-base62-sha1="ynEYKaAy8CFeETgKoRTjgr3YN6x" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0f69f6dc6f68b152b7f54d5cf09b495a49afbc9_2_690x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0f69f6dc6f68b152b7f54d5cf09b495a49afbc9_2_1035x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0f69f6dc6f68b152b7f54d5cf09b495a49afbc9_2_1380x610.jpeg 2x" data-dominant-color="97979D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">C0000218 Slicer View.PNG</span><span class="informations">1920×850 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76a5cd9792373b1b6c0867dcd1943073493358b1.png" data-download-href="/uploads/short-url/gVBzwCOFfkiXlgldLhi0PiwWgfv.png?dl=1" title="what" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a5cd9792373b1b6c0867dcd1943073493358b1_2_690x426.png" alt="what" data-base62-sha1="gVBzwCOFfkiXlgldLhi0PiwWgfv" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a5cd9792373b1b6c0867dcd1943073493358b1_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a5cd9792373b1b6c0867dcd1943073493358b1_2_1035x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a5cd9792373b1b6c0867dcd1943073493358b1_2_1380x852.png 2x" data-dominant-color="4D4D4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">what</span><span class="informations">1588×981 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-07-06 16:55 UTC)

<p>It seems that you export the “Background” segment, too. You can delete this background segment before exporting. In general, if you don’t want to export some segments then hide them and check “Visible segments only” in the “Export segments to files” window.</p>

---

## Post #3 by @hherhold (2020-07-06 17:21 UTC)

<p>Is there a particular reason you’re using OBJ? I’ve found PLY to be a lot smaller and easier to deal with when moving segmentations to blender. OBJ preserves surface colors, other than that, I haven’t seen any advantage to it.</p>

---

## Post #4 by @lassoan (2020-07-06 17:48 UTC)

<p>Yes, the main advantage of OBJ is that it allows exporting many segments in a single file and the segments can be separated in Blender.</p>

---

## Post #5 by @hherhold (2020-07-06 18:00 UTC)

<p>Well shoot, that’s a pretty big advantage.</p>
<p>I usually only export a couple of segments but I will definitely have to keep OBJ in mind. Thanks!!!</p>

---

## Post #6 by @muratmaga (2020-07-06 18:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12399">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>segments in a single file and the segments can be separated in Blender.</p>
</blockquote>
</aside>
<p>How would you do that in SLicer? Normally, isn’t every segment exported by itself?</p>

---

## Post #7 by @lassoan (2020-07-06 18:29 UTC)

<p>“Export to files” feature (in Segmentations and Segment Editor modules) can export all segments to a single OBJ or STL file.</p>

---

## Post #8 by @muratmaga (2020-07-06 18:34 UTC)

<p>OK. I was wondering why there was only OBJ and STL, but not PLY there. Makes sense now. THanks.</p>

---

## Post #9 by @hherhold (2020-07-06 18:40 UTC)

<p>Hmm. The “Merge into single file” checkbox is greyed out if I select OBJ but enabled if I select STL.</p>

---

## Post #10 by @lassoan (2020-07-06 19:07 UTC)

<p>In case of OBJ, you don’t need to merge the segments, as they remain separate even when they are stored in a single file. I see how it can be confusing, I’ll update the tooltip text and checkbox state to make this more clear.</p>

---
