# Why can't my engrave function be apply?

**Topic ID**: 23809
**Date**: 2022-06-10
**URL**: https://discourse.slicer.org/t/why-cant-my-engrave-function-be-apply/23809

---

## Post #1 by @sunwei921119 (2022-06-10 12:23 UTC)

<p>Hello, why can’t my engrave function be apply? I tried several versions of it. Is there anything wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8e4f089727911c7600c2c986c0922dc45e18f4b.jpeg" data-download-href="/uploads/short-url/xehgZ8wFPILhqtay46sJanQNwkr.jpeg?dl=1" title="mmexport1654848487261" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8e4f089727911c7600c2c986c0922dc45e18f4b_2_690x347.jpeg" alt="mmexport1654848487261" data-base62-sha1="xehgZ8wFPILhqtay46sJanQNwkr" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8e4f089727911c7600c2c986c0922dc45e18f4b_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8e4f089727911c7600c2c986c0922dc45e18f4b_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8e4f089727911c7600c2c986c0922dc45e18f4b.jpeg 2x" data-dominant-color="C8A8B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1654848487261</span><span class="informations">1366×688 70.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mau_igna_06 (2022-06-10 14:17 UTC)

<p>I think you need to click on the engrave option then click apply</p>

---

## Post #3 by @lassoan (2022-06-10 15:21 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> is right that you need to click the Apply button, but in the latest Slicer version the effect is indeed does not work well because the default plane placement mode was changed from 3-point to single-point. I’ll submit a fix today.</p>

---

## Post #4 by @muratmaga (2022-06-10 17:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="23809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>de was changed from 3-point to single-point. I’ll submit a fix today.</p>
</blockquote>
</aside>
<p>Would it be possible to have an option to change the default plane placement mode? Like setting the markup glpyh and colors as a preference (Save To Defaults, Restore Defaults).</p>

---

## Post #5 by @lassoan (2022-06-11 01:13 UTC)

<p>Change the default plane type could be used as a workaround, but the single-point mode is much more powerful and flexible than the 3-point mode.</p>
<p>I’ve updated the Engrave effect in SegmentEditorExtraEffects extension and it is now very easy to resize and reposition the text:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="dVDfktQm7OI" data-video-title="Engrave or emboss 3D text into segmented images" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=dVDfktQm7OI" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/dVDfktQm7OI/maxresdefault.jpg" title="Engrave or emboss 3D text into segmented images" width="" height="">
  </a>
</div>


---

## Post #6 by @sunwei921119 (2022-06-11 11:07 UTC)

<p>I updated segmenteditorextraeffects, but I still can’t click apply because I’m in China and haven’t updated it?</p>

---

## Post #7 by @lassoan (2022-06-11 12:28 UTC)

<p>You need to wait a few more hours for the SegmentEditorExtraEffects <code>git719b242</code> version to appear on the dashboard:</p>
<ul>
<li><a href="https://slicer.cdash.org/index.php?project=SlicerStable">Dashboard for Slicer Stable Release</a></li>
<li><a href="https://slicer.cdash.org/index.php?project=SlicerPreview">Dashboard for Slicer Preview Release</a></li>
</ul>

---

## Post #8 by @sunwei921119 (2022-06-12 07:54 UTC)

<p>Thank you very much. It has been solved.</p>

---

## Post #9 by @cpinter (2025-03-28 09:26 UTC)

<p>A post was merged into an existing topic: <a href="/t/engraving-with-segmenteditorextraeffects/42338/2">Engraving with SegmentEditorExtraEffects</a></p>

---
