---
topic_id: 28642
title: "Segmentation Using Paint The Bulb Of Paint Disappears Instea"
date: 2023-03-29
url: https://discourse.slicer.org/t/28642
---

# Segmentation, using paint, the bulb of paint disappears instead of remaining

**Topic ID**: 28642
**Date**: 2023-03-29
**URL**: https://discourse.slicer.org/t/segmentation-using-paint-the-bulb-of-paint-disappears-instead-of-remaining/28642

---

## Post #1 by @khersi (2023-03-29 00:18 UTC)

<p>Operating system :Windows<br>
Slicer version:5.2.2<br>
Expected behavior: When using paint, using the left button of the mouse, when dropping the left button, the area painted should remain colored<br>
Actual behavior: After painting an area, when dropping the left button, the bulb of paint disappears, instead of remainin</p>

---

## Post #2 by @lassoan (2023-03-29 00:24 UTC)

<p>Make sure your masking settings allow painting in that region (Editable area: everywhere; Editable intensity range: unchecked) and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">inside the segmentation’s extents</a>.</p>

---

## Post #3 by @SteveDonie (2023-12-16 20:09 UTC)

<p>I am also a brand new user, following the tutorial at <a href="https://spujol.github.io/ImagePhenotypingTutorial/ImagePhenotypingTutorial_SoniaPujol.pdf" rel="noopener nofollow ugc">https://spujol.github.io/ImagePhenotypingTutorial/ImagePhenotypingTutorial_SoniaPujol.pdf</a> but using my own MRI.</p>
<p>I am seeing the same behavior mentioned above - when I try to paint, it doesn’t seem to ‘stick’ - I paint an area and as soon as I release the mouse button the area goes away. I do have the editable area set to ‘everywhere’ and editable intensity range unchecked. I don’t understand what was meant in Andras’s answer about “inside the segmentation’s extents”.</p>

---

## Post #4 by @SteveDonie (2023-12-16 21:15 UTC)

<p>I ended up discarding the changes I had made and starting over, and I was able to do what I needed. Not sure what the problem was.</p>

---

## Post #5 by @muratmaga (2023-12-17 00:58 UTC)

<p>To understand what’s going on and why it is happening try these steps:</p>
<ol>
<li>Download MRHead and CT Chest sample datasets</li>
<li>Right click on MRHead and choose “segment this”</li>
<li>Create a single segment, and paint somewhere with a paint brush.</li>
<li>While in segment editor, switch <code>Source Volume</code> from MRHead to CTChest</li>
<li>Try to paint any region using Segment_1 and notice that everything you paint immediately disappears.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/858120d3908e2f53ef0d2579f8adbd6b13fce352.png" data-download-href="/uploads/short-url/j329TcJWRjMValevdrS0QeffJJ0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/858120d3908e2f53ef0d2579f8adbd6b13fce352_2_690x153.png" alt="image" data-base62-sha1="j329TcJWRjMValevdrS0QeffJJ0" width="690" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/858120d3908e2f53ef0d2579f8adbd6b13fce352_2_690x153.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/858120d3908e2f53ef0d2579f8adbd6b13fce352.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/858120d3908e2f53ef0d2579f8adbd6b13fce352.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">950×212 15.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That’s because segmentation geometry is determined by the physical extends of the first volume you choose (MRHead). If the second volume has different physical dimensions, existing segmentation and the volume to be segmented does not overlap in physical space, so you can’t paint/segment anything.</p>
<p>In this example we blatantly choose very different volumes to demonstrate what’s going on. Their names are different, their regions are different etc. it may not be that obvious all the time. After double checking that the visibility settings and editable area settings are indeed correct, you can assume you have mismatch between segment geometry and the volume you are trying to segment and that you should double check your steps about how you created the segmentation in the first place.</p>

---
