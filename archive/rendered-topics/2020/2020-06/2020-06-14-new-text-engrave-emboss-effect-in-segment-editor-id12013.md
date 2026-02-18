# New text engrave/emboss effect in Segment Editor

**Topic ID**: 12013
**Date**: 2020-06-14
**URL**: https://discourse.slicer.org/t/new-text-engrave-emboss-effect-in-segment-editor/12013

---

## Post #1 by @lassoan (2020-06-14 02:12 UTC)

<p>A new tool added to Segment Editor for drawing text on segments. Both engrave and emboss modes are available. Text can be placed by defining a plane using 3 points, and then position can be adjusted in 3D, along with text size and depth.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="aOZXwFgcRsY" data-video-title="Draw text on 3D models using Segment editor Engrave tool" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=aOZXwFgcRsY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/aOZXwFgcRsY/maxresdefault.jpg" title="Draw text on 3D models using Segment editor Engrave tool" width="" height="">
  </a>
</div>

<p>The effect is available in SegmentEditorExtraEffects extension for latest Slicer-4.11 Preview Release.</p>

---

## Post #2 by @pieper (2020-06-14 16:46 UTC)

<p>That’s awesome!  Hello back!!</p>

---

## Post #3 by @norus (2020-06-15 06:38 UTC)

<p>congratulation, this is very helpful and makes daily work much easier.</p>
<p>thank´s</p>

---

## Post #4 by @Dexter777 (2020-07-05 18:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6dd6fc8cb9287a25cb6417eb95a57809599f23c.jpeg" data-download-href="/uploads/short-url/nO9GwM1m3LXsVeyR6PJnbo2su5e.jpeg?dl=1" title="6 x 8.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6dd6fc8cb9287a25cb6417eb95a57809599f23c_2_690x368.jpeg" alt="6 x 8.PNG" data-base62-sha1="nO9GwM1m3LXsVeyR6PJnbo2su5e" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6dd6fc8cb9287a25cb6417eb95a57809599f23c_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6dd6fc8cb9287a25cb6417eb95a57809599f23c_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6dd6fc8cb9287a25cb6417eb95a57809599f23c_2_1380x736.jpeg 2x" data-dominant-color="C4BDBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6 x 8.PNG</span><span class="informations">1770×946 371 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hi, Is there a means to get clearer defined text without enlarging<br>
the text beyond the size of the skull? Text height at 6 and depth at 10.</p>
<p>Thank you</p>

---

## Post #5 by @lassoan (2020-07-05 19:18 UTC)

<p>You need to reduce the spacing of the segmentation to allow representation of smaller details. You can change the resolution by clicking on the button next to the master volume selector. You may also try reducing surface smoothing.</p>

---

## Post #6 by @Dexter777 (2020-07-06 22:37 UTC)

<p>Hi Andras,<br>
I’ve tried both suggestions. By reducing the spacing which is currently 1 mm to .7 or .5,  I get an obliterated  model with multiple holes in it. Reducing the surface smoothing gives me a very rough model.<br>
After trying these I get multiple error messages. Lol.</p>
<p>Any suggestions?</p>
<p>Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a98598b76b1497d78e1192aa4d50ffcbc4d157b.png" data-download-href="/uploads/short-url/huwESmbKAjftbW8KUhrBEAUN0iD.png?dl=1" title="Slicer-Emboss" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a98598b76b1497d78e1192aa4d50ffcbc4d157b_2_517x312.png" alt="Slicer-Emboss" data-base62-sha1="huwESmbKAjftbW8KUhrBEAUN0iD" width="517" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a98598b76b1497d78e1192aa4d50ffcbc4d157b_2_517x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a98598b76b1497d78e1192aa4d50ffcbc4d157b_2_775x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a98598b76b1497d78e1192aa4d50ffcbc4d157b.png 2x" data-dominant-color="B3ADBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-Emboss</span><span class="informations">944×571 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2020-07-06 22:42 UTC)

<p>If you reduce the spacing then it probably makes sense to do a bit of anti-alias filtering: a slight Gaussian smoothing (using Smoothing effect). Or, you can set master representation to Closed surface before you change spacing.</p>

---

## Post #8 by @Dexter777 (2020-07-06 23:05 UTC)

<p>Sorry for asking so many questions- Where do I set the master representation to Closed surface? I don’t see that option in the segmentation geometry function.</p>

---

## Post #9 by @lassoan (2020-07-06 23:38 UTC)

<p>You can choose the current master representation in Segmentations module’s Representations section.</p>

---

## Post #10 by @lassoan (2023-04-15 20:22 UTC)

<p>A post was split to a new topic: <a href="/t/allow-engraving-text-on-curved-surfaces-in-segment-editor/28935">Allow engraving text on curved surfaces in Segment Editor</a></p>

---
