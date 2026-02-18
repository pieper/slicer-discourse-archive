# Brush size control by key

**Topic ID**: 4899
**Date**: 2018-11-28
**URL**: https://discourse.slicer.org/t/brush-size-control-by-key/4899

---

## Post #1 by @Ash_Alarfaj (2018-11-28 11:12 UTC)

<p>Problem report for Slicer 4.10.0 macosx-amd64: [please describe expected and actual behavior]</p>
<p>when press shift mouse wheel it does not work (increase/decrease) brush size, for erase option.<br>
thanks for your great efforts but as I’ve used the 3 d slicer programme and tried 3 versions still the 4.8 one is the best. it is faster and all actions are greatly doing well.</p>
<p>regards<br>
Ashwaj</p>

---

## Post #2 by @lassoan (2018-11-28 14:16 UTC)

<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="1" data-topic="4899">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>when press shift mouse wheel it does not work (increase/decrease) brush size, for erase option.</p>
</blockquote>
</aside>
<p>It works well for me - just tested on Windows. Could someone please try to reproduce this on Mac, too?</p>
<p>Try it while the mouse is over a slice viewer. You may also clicking in the viewer before starting to use shift+wheel (you can do right-click, to not erase anything at the click position).</p>
<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="1" data-topic="4899">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>still the 4.8 one is the best</p>
</blockquote>
</aside>
<p>Slicer-4.10 has <a href="https://discourse.slicer.org/t/slicer-4-10-summary-highlights-and-changelog/4610">many very important improvements and hundreds of fixes</a>, so I would definitely recommend it over Slicer-4.8. Please report any specific problems that you encounter.</p>
<p>Overall performance should be greatly improved (in some cases up to a factor of 10x), but since rendering pipeline in underlying VTK library has been completely reworked, utilizes and requires most modern OpenGL API, in some cases we observed slight performance decrease (such as slice browsing performance may be slower by 10-20%, especially on older systems). Try to upgrade your graphics drivers and let us know about any specific issues.</p>

---

## Post #3 by @Ash_Alarfaj (2018-11-28 15:14 UTC)

<p>Thanks a lot for your consideration, my driver is upgraded to the latest version</p>
<p>please see the attachment to make sure I did understand what you mean by the driver.</p>
<p>all the best</p>
<p>Ashwaj</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/568af752c0ca654c78036a4b5816d69adef37c8a.png" data-download-href="/uploads/short-url/clANlHBchZEo76U1erLcvETBSb0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/568af752c0ca654c78036a4b5816d69adef37c8a_2_690x322.png" alt="image" data-base62-sha1="clANlHBchZEo76U1erLcvETBSb0" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/568af752c0ca654c78036a4b5816d69adef37c8a_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/568af752c0ca654c78036a4b5816d69adef37c8a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/568af752c0ca654c78036a4b5816d69adef37c8a.png 2x" data-dominant-color="E3E1E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">986×461 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @ihnorton (2018-11-28 15:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4899">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could someone please try to reproduce this on Mac, too?</p>
</blockquote>
</aside>
<p>Yes, I can reproduce. Works fine in 4.8.1, doesn’t work in 4.10.</p>

---

## Post #5 by @lassoan (2018-11-29 04:24 UTC)

<p>I’ve added a ticket to track this problem: <a href="https://issues.slicer.org/view.php?id=4661" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4661</a>.</p>

---

## Post #6 by @Ash_Alarfaj (2018-12-06 11:34 UTC)

<p>Hi Mr Issoan<br>
I am wondering, do you replace 3d slicer version 4.8 with the latest  4.10. so 4.8 no longer exist? There is a problem in the last version on mac, the uploaded images are not seen in the viewer, and also the DCM icon does not work. I hope you keep version 4.8 because it seems to me the most convenient one.</p>
<p>regards</p>
<p>Ashwaj</p>

---

## Post #7 by @lassoan (2018-12-07 01:04 UTC)

<p>Slicer-4.8.1 is still available, you can find installation packages on the download page (click on “older releases”). However, we can only offer very limited support for obsolete releases.</p>
<p>If you clarify what you mean by “uploaded images are not seen in the viewer”? What images? How do you display them? Can you attach a screenshot? Can you see images available in SampleData module?</p>
<p>“the DCM icon does not work” What is a DCM icon? Do you mean the Subject Hierarchy module icon on the toolbar does not work anymore? The module has been merged with Data module, so you need to update favorite module list in Application settings / Modules section (remove “Subject Hierarchy” , add “Data”).</p>

---

## Post #8 by @cpinter (2018-12-07 12:45 UTC)

<p>I have a hunch it’s about the DICOM browser. Please look for the browser behind the Slicer window (cmd+tab). If you cannot import images then set a database folder that’s writable (need to open the settings panel on top row)</p>

---
