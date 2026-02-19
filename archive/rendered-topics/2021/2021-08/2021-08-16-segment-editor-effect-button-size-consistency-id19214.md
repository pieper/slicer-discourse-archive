---
topic_id: 19214
title: "Segment Editor Effect Button Size Consistency"
date: 2021-08-16
url: https://discourse.slicer.org/t/19214
---

# Segment Editor Effect button size consistency

**Topic ID**: 19214
**Date**: 2021-08-16
**URL**: https://discourse.slicer.org/t/segment-editor-effect-button-size-consistency/19214

---

## Post #1 by @jamesobutler (2021-08-16 18:08 UTC)

<p>Continued originally from:</p>
<aside class="quote quote-modified" data-post="4" data-topic="19208">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/organization-of-segment-editor-effects-into-categories/19208/4">Organization of Segment Editor effects into Categories</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I think in most cases you mean that the effect buttons can be too large at times (not the icon). This being because the text in the button makes it larger rather than the icon. 


I do think the icons do provide some information about what the effect does, but not all the necessary information and neither does the name. The effect buttons already shows a hover tooltip that is the segment effect name, so if we want to enforce equal size segment editor effect buttons by way of equal size icons wi…
  </blockquote>
</aside>

<p>Currently some segment editor effects are larger than others because they have longer text on the button. “Grow from seeds” is a larger size than say “Paint”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/523f67a871ad1e5b1881921f51d17574e9b32cb9.png" alt="image" data-base62-sha1="bJAZOnUfCWsyDdXDFkQOitRuTHP" width="540" height="136"></p>
<p>We could update buttons so the last one in the row does not stretch in the ctkFlowLayout to the layout current bounds. We could also choose to remove the text from the effect buttons and instead rely on the tooltip to provide information about what the button is if it isn’t clear from the icon.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1718aa9a4d209e11665e0c85eb032a2f7c125195.png" alt="image" data-base62-sha1="3ijPq7gpph2PuAvSTd3FUIZAkn3" width="67" height="69"></p>
<p>Do others think the text below the icon for the segment editor effects is critical? I’ve looked at other applications and text for the grouping of tools is not something usually done. I realize there are some special effects like “Grow from seeds” which doesn’t have a known equivalent in a regular image editor so just a icon could not be information. However with many like None, Paint, Draw, Erase, Scissors (lasso), there are known icons that can easily describe the effect on its own.</p>
<p>Photoshop:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/176fcbd61205919d01e8b896bd15cc9e70be18b3.png" data-download-href="/uploads/short-url/3lkvfWXJx4Cu8MqAb8g08ljiNJ9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/176fcbd61205919d01e8b896bd15cc9e70be18b3_2_77x500.png" alt="image" data-base62-sha1="3lkvfWXJx4Cu8MqAb8g08ljiNJ9" width="77" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/176fcbd61205919d01e8b896bd15cc9e70be18b3_2_77x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/176fcbd61205919d01e8b896bd15cc9e70be18b3_2_115x750.png 1.5x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">135×876 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Paint 3D:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58e0ab3e91d579a368151206e0ababb55fbe0cb7.png" alt="image" data-base62-sha1="cGfmPVFBEEkk1xm5S2ItZz5gc1p" width="244" height="162"></p>

---

## Post #2 by @pieper (2021-08-16 18:36 UTC)

<p>The old Editor has just the icons and tooltips with the names.  I found it worked well.  I agree it’s good to avoid scrolling the module panel so saving space is good.  Also keeping the tool icons in a fixed order makes it easier to quickly get to the tool you want (the current Segment Editor tools move as the module panel changes width and I find this leads to confusion).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b4c71a3e811d6441bc0c099f0cb9d17614bff65.png" alt="image" data-base62-sha1="fjcRUWTXJLN7Lmw5yWT9SdWrZCl" width="545" height="238"></p>

---

## Post #3 by @hherhold (2021-08-16 18:55 UTC)

<p>I’m very much in favor of removing the text from the buttons.</p>

---

## Post #4 by @hherhold (2021-08-16 18:55 UTC)

<p>Meaning, use tooltips instead of text embedded with buttons.</p>

---

## Post #5 by @jamesobutler (2021-08-16 18:56 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>the current Segment Editor tools move as the module panel changes width and I find this leads to confusion</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> Are you suggesting that the effects no longer be in a ctkFlowLayout but rather a QGridLayout? If I manually expand the left side panel to be larger the effects would move to try and be on 1 row rather than multiple rows. If a QGridLayout, then on smaller screens the minimum size of the side panel would increase as it couldn’t change from say 8 effects across 2 rows to be say 4 effects across 4 rows.</p>

---

## Post #6 by @pieper (2021-08-16 19:02 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>no longer be in a ctkFlowLayout but rather a QGridLayout</p>
</blockquote>
</aside>
<p>Yes exactly.  I don’t think it’s helpful for the effect buttons to jump around.  If we just use the icons (no text) we can make multiple rows of a reasonable width.  These could be generally grouped by similarity but I wouldn’t bother naming and labeling the groups since I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a> that the concept names aren’t exact, but rows of effects with somewhat similar behavior or interface could be helpful so people remember where to look for a type of operation.</p>

---

## Post #7 by @lassoan (2021-08-16 21:52 UTC)

<p>Text looks nice and saves time for novices, but I agree that it may not worth the space it takes.</p>
<p>Flow layout saves space but not the saving is not that significant and forces users to scan through the complete icon list, so a static grid layout would probably work better.</p>
<p>We can allow users to configure both button label visibility and grid layout column count.</p>
<p>If we hide the Slicer logo at the top and put the Data probe in a dockable widget then probably we don’t need to scroll anymore.</p>
<p>If we need even more vertical space then we could add an option to show the toolbar on the side, using 1 or 2 columns.</p>

---

## Post #8 by @muratmaga (2021-08-17 19:33 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="19214" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Meaning, use tooltips instead of text embedded with buttons.</p>
</blockquote>
</aside>
<p>I also like this idea, with the proviso that font size for these tooltips should a bit bigger than the rest. With my aging eyes, I find it quite difficult to read the contents of tooltips sometimes.</p>

---

## Post #9 by @pieper (2021-08-17 20:07 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I also like this idea, with the proviso that font size for these tooltips should a bit bigger than the rest.</p>
</blockquote>
</aside>
<p>Yes, maybe not a tooltip with a delay, but a label below the rows of buttons that updates instantly as you mouse over the buttons.  Similar in effect to the way the DataProbe updates as you mouse over segments.</p>

---

## Post #10 by @jamesobutler (2021-08-18 00:54 UTC)

<p>I’ll post here again once I post another PR with the suggestions discussed on this thread.</p>

---

## Post #11 by @jamesobutler (2021-08-18 02:38 UTC)

<p>Well here’s a first look for visual impressions. Actually using it can come soon after.</p>
<p>Thoughts on the “Segment Editor Effects” toolbar?</p>
<ul>
<li>
<p>Does it work as a Toolbar? or should it instead be contained inside the Segment Editor module layout?</p>
</li>
<li>
<p>The allowed areas could be anywhere (Left, Top, Right, Bottom) with the default location being the left toolbar area. Should it be allowed anywhere including floatable?</p>
</li>
<li>
<p>Should it only be shown when the Segment Editor module is the selected module? It really depends on other functionality of the module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2deb15e0dc6d91acb1e64910ea35efa79434905c.jpeg" data-download-href="/uploads/short-url/6yd9zHRdNJXHN3V2l4h6DUFNkKw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2deb15e0dc6d91acb1e64910ea35efa79434905c_2_690x370.jpeg" alt="image" data-base62-sha1="6yd9zHRdNJXHN3V2l4h6DUFNkKw" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2deb15e0dc6d91acb1e64910ea35efa79434905c_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2deb15e0dc6d91acb1e64910ea35efa79434905c_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2deb15e0dc6d91acb1e64910ea35efa79434905c_2_1380x740.jpeg 2x" data-dominant-color="919398"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>For a smaller window size there is automatically an expand button to show the other toolbar buttons (Segment Editor effect buttons). It expands like the following to allow the selection of others and then the expand disappears when the mouse hovers away from it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f992a0f01ba38f3e837a96af1ccfccc3e470936.png" data-download-href="/uploads/short-url/bm9S8ngT91Ns9u4tFrcwJpRalrU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f992a0f01ba38f3e837a96af1ccfccc3e470936_2_121x375.png" alt="image" data-base62-sha1="bm9S8ngT91Ns9u4tFrcwJpRalrU" width="121" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f992a0f01ba38f3e837a96af1ccfccc3e470936_2_121x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f992a0f01ba38f3e837a96af1ccfccc3e470936_2_181x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f992a0f01ba38f3e837a96af1ccfccc3e470936.png 2x" data-dominant-color="E9ECEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">205×629 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Regarding tooltip text size, currently it is the same size as other text in the module. If one is difficult to read the others will be difficult to read. Text size would then need to be magnified across the application. I assume this is already handled with the font size setting.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b515e7b641a599d788f214ad749bf69270d8dbdc.png" data-download-href="/uploads/short-url/pPXlVubuRNepyB6mTXKv3aT5ucQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b515e7b641a599d788f214ad749bf69270d8dbdc.png" alt="image" data-base62-sha1="pPXlVubuRNepyB6mTXKv3aT5ucQ" width="517" height="74" data-dominant-color="F3F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">834×120 5.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We can allow users to configure both button label visibility</p>
</blockquote>
</aside>
<ul>
<li>If the Segment Editor Effects are in a toolbar the showing or hiding of text would seem to make sense paired to the current “Show text under icons in toolbar buttons” setting.</li>
</ul>

---

## Post #12 by @jamesobutler (2021-08-18 02:52 UTC)

<p>And of course the more old school method of the segment editor effects directly under the segment table and not movable.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e79a7609b9d3afcb6fe1ddc81696f47f2ad83532.jpeg" data-download-href="/uploads/short-url/x2Re4GbyxzstkTcNcTFa7H4wQbo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e79a7609b9d3afcb6fe1ddc81696f47f2ad83532_2_690x370.jpeg" alt="image" data-base62-sha1="x2Re4GbyxzstkTcNcTFa7H4wQbo" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e79a7609b9d3afcb6fe1ddc81696f47f2ad83532_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e79a7609b9d3afcb6fe1ddc81696f47f2ad83532_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e79a7609b9d3afcb6fe1ddc81696f47f2ad83532_2_1380x740.jpeg 2x" data-dominant-color="8E8F95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @muratmaga (2021-08-18 04:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Does it work as a Toolbar? or should it instead be contained inside the Segment Editor module layout?</p>
</blockquote>
</aside>
<p>Without being able to modify/change the active segment etc, I can’t see the Segment Editor toolbar being used on its own, at least not very effectively.  To me, it feels like it just belongs inside the Editor.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>For a smaller window size there is automatically an expand button to show the other toolbar buttons (Segment Editor effect buttons). It expands like the following to allow the selection of others and then the expand disappears when the mouse hovers away from it.</p>
</blockquote>
</aside>
<p>I like that.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Regarding tooltip text size, currently it is the same size as other text in the module. If one is difficult to read the others will be difficult to read. Text size would then need to be magnified across the application. I assume this is already handled with the font size setting.</p>
</blockquote>
</aside>
<p>I liked what <a class="mention" href="/u/pieper">@pieper</a> said about not being delayed tooltips. Would it be possible to bring a label immediately when I hover over (as oppose to waiting a little while before the tooltip shows up)?</p>
<p>In the module window, would it be possible to make the label of the active effect (Threshold in your screenshot) a bit more prominent (larger font or bold face or something).</p>
<p>Thanks again doing all this work!</p>

---

## Post #14 by @lassoan (2021-08-18 04:39 UTC)

<p>Thank you, this looks promising.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Does it work as a Toolbar? or should it instead be contained inside the Segment Editor module layout?</p>
</blockquote>
</aside>
<p>The widget has to be self-contained (as it is included in many modules now) and we need to allow at least two columns (in the screenshot we already ran out of space with a single column). A simple frame with a grid layout containing QToolButtons should work. Number of columns (or maximum number of rows) could be user-configurable.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The allowed areas could be anywhere (Left, Top, Right, Bottom) with the default location being the left toolbar area. Should it be allowed anywhere including floatable?</p>
</blockquote>
</aside>
<p>QToolBar is quite limited (single column only; dockable only if it is child of the main window, etc.) and if it was outside of the module’s GUI then showing/hiding/positioning would require a lot of extra management. So, I don’t think we can use QToolBar. We could easily make the position/orientation of the button grid user-configurable (horizontal/vertical orientation, left/right/top position), but probably this is not necessary.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Should it only be shown when the Segment Editor module is the selected module? It really depends on other functionality of the module.</p>
</blockquote>
</aside>
<p>Yes, it should only be shown when the corresponding qMRMLSegmentEditorWidget widget is visible. As I wrote above, this could become very complicated if the buttons are not in the widget’s layout.</p>

---

## Post #15 by @jamesobutler (2021-08-18 11:38 UTC)

<p>If the effects are arranged vertically inside the Segment Editor layout should they be to the left of all current widgets in the layout? Would be to the left of help/acknowledgement, to the left of the segment table, to the left of effect options and to the left of masking options.</p>

---

## Post #16 by @jamesobutler (2021-08-18 17:48 UTC)

<p>I guess if the effect buttons have to be within qMRMLSegmentEditorWidget, then they could only extend vertically in the region to the left of the (node selection + segment table + effect options + masking).  It could not extend to the left of the acknowledgement group box area.</p>

---

## Post #17 by @lassoan (2021-08-18 18:20 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="16" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I guess if the effect buttons have to be within qMRMLSegmentEditorWidget</p>
</blockquote>
</aside>
<p>Exactly. Everything has to be inside the segment editor widget.</p>

---

## Post #18 by @jamesobutler (2021-08-19 01:52 UTC)

<p>Here’s an image of the Segment Effects part of qMRMLSegmentEditorWidget with vertical orientation of effect groupbox. Effects fill into a QGridLayout instead of a ctkFlowlayout and fill in the grid in order from top to bottom utilizing 2 columns always. This is so effects at the beginning of the effect ordered list are at the top. Effects at the very end of the list are always near the bottom of the 2 columns. Also a reminder that since more things no longer need a scrollbar to see (masking options), this means the width of the left side bar area is a little bit wider to accommodate the 2 columns. This makes the decision to prioritize not having to scroll over trying to maintain a slightly smaller left side panel width.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ae5d94049def833f1b64a20186d03ec76719032.jpeg" data-download-href="/uploads/short-url/m6hYGPhFsDHDEWTXq1aadH9zCy6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae5d94049def833f1b64a20186d03ec76719032_2_690x370.jpeg" alt="image" data-base62-sha1="m6hYGPhFsDHDEWTXq1aadH9zCy6" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae5d94049def833f1b64a20186d03ec76719032_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae5d94049def833f1b64a20186d03ec76719032_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae5d94049def833f1b64a20186d03ec76719032_2_1380x740.jpeg 2x" data-dominant-color="96999C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the window is small, you have to scroll down to see more effects, just like you would have to scroll to see more of the effects. I think this behavior is fine considering it is part of qMRMLSegmentEditorWidget object.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45e4fb9920d0f9da5ee8ae3cfdacd9473e8d7481.png" data-download-href="/uploads/short-url/9Yjxpn7VLq81X1ZAHfaaBvKgsCt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45e4fb9920d0f9da5ee8ae3cfdacd9473e8d7481_2_690x319.png" alt="image" data-base62-sha1="9Yjxpn7VLq81X1ZAHfaaBvKgsCt" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45e4fb9920d0f9da5ee8ae3cfdacd9473e8d7481_2_690x319.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45e4fb9920d0f9da5ee8ae3cfdacd9473e8d7481_2_1035x478.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45e4fb9920d0f9da5ee8ae3cfdacd9473e8d7481_2_1380x638.png 2x" data-dominant-color="BDC0C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1389×644 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Previously mentioned:</p>
<aside class="quote no-group" data-username="Umesh_Persad" data-post="20" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"><a href="https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029/20">Segment Editor User Interface Improvements</a></div>
<blockquote>
<p>Three key principles of usability are familiarity, consistency and feedback. In other words, if the interface is similar to what people already know and use (standards), it will be easier to use. Menu names, structures and layouts are what users are familiar with using other software. For example, why “Segmentation Effects” versus “Segmentation Tools”.</p>
</blockquote>
</aside>
<p>This would seem that the QGroupBox that currently has the title “Effects” should be changed to “Tools”. Should we begin referring to these as “Segment Editor Tools” to improve user understanding by using familiar terminology?</p>

---

## Post #19 by @muratmaga (2021-08-19 19:03 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="18" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If the window is small, you have to scroll down to see more effects, just like you would have to scroll to see more of the effects. I think this behavior is fine considering it is part of qMRMLSegmentEditorWidget object.</p>
</blockquote>
</aside>
<p>Is the effect groupbox resizable by the user (like making it single row, triple row etc)? If people have only the default segment editor tools, would the second row appear empty?</p>
<p>Otherwise this is looking better to me than our current UI.</p>

---

## Post #20 by @jamesobutler (2021-08-19 20:09 UTC)

<p>The layout is filled in from the top to the bottom. So if there are fewer effects, there will be not as many rows instead of not as many columns.</p>
<p>For it to be resizeable and adjust dynamically like you are suggesting, it would need to be a ctkFlowLayout again instead of a QGridLayout.</p>

---

## Post #21 by @jamesobutler (2021-08-20 01:17 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> The thing about resizing the effect groupbox that goes against some of the negatives talked about previous is that effect buttons would move location when this is resized. If effect buttons should be in the same location for familiarity then this dynamic resize/reorder would go against that idea. If you make it more columns or less columns, then you have to relearn where the expected location of the button is at.</p>
<p>Having a strict grid layout would make sure the buttons are always in the same place and you would scroll down if your screen size was too small to fit them all.</p>

---

## Post #22 by @muratmaga (2021-08-20 01:35 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="20" data-topic="19214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The layout is filled in from the top to the bottom. So if there are fewer effects, there will be not as many rows instead of not as many columns.</p>
</blockquote>
</aside>
<p>This is fine. I was just curious if the width of the groupbox was fixed, but now I understand it works exactly how it is right now, except vertically.</p>

---

## Post #23 by @jamesobutler (2021-08-20 02:39 UTC)

<p>I guess for custom app purposes if you set only say 6 effects to be visible, then not sure if the 3 rows by 2 columns is still valid or if the user would then want 6 rows 1 column. So maybe adjustable as a setting for at least the custom app purposes. Though the custom app developer could probably change the layout to fit their purpose anyway rather than Slicer developers trying to guess what they might want in their custom app.</p>
<p>Regular unmodified Slicer would probably benefit with it always being a 2 column setup.</p>

---

## Post #24 by @lassoan (2021-09-13 19:52 UTC)

<p>Thanks to all the efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, the new Segment Editor layout is now ready - see more information (and provide any feedback and suggestions) in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="19649">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649">New Segment Editor layout - vertical effect toolbar</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks to all the development efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and feedback from the community, the new, more space-efficient Segment Editor user interface is now ready (available in latest Slicer Preview Release). The main difference is that the effect toolbar is vertical, with fixed number of columns and without icon labels. This layout makes it easier to remember where to find an effect (because the same effect always appears at the same place), and the space is used more efficiently (there is less n…
  </blockquote>
</aside>


---
