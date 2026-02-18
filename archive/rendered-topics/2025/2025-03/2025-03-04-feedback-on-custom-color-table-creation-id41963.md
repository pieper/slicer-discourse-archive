# Feedback on custom color table creation

**Topic ID**: 41963
**Date**: 2025-03-04
**URL**: https://discourse.slicer.org/t/feedback-on-custom-color-table-creation/41963

---

## Post #1 by @muratmaga (2025-03-04 18:04 UTC)

<p>I am reviewing the newly integrated functionality. Everything seems to work well, but I think we need some clarification and some minor functionality tweak.</p>
<ol>
<li>When I am creating my own custom color table with terminologies, do I need to create 0 Background entry with color (0,0,0) or is that automatically appended? Because all color tables I am aware of that has that entry. and it wasn’t clear to me. If it is necessary, perhaps auto-populate that field.</li>
<li>I have a little issue with opacity being always 0  for all blank entries, which complicated setting the color from the palette. But it is a minor one. I suspect most of the time people will either choose from the terminology module or enter the RGB code in the table. Otherwise table creation seems to work well.</li>
<li>When I am using this color table during segmentation, Terminology selector seems to keep defaulting to Slicer’s own terminology. Can we make the change that Terminology module opens with the latest selected terminology/color table from the top drow down.</li>
</ol>
<p>I will keep reviewing more thoroughly, but things seems to work well for me beyond these minor issues.</p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> and everyone else who contributed to the discussion and implementation.</p>

---

## Post #2 by @lassoan (2025-03-04 20:39 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>When I am creating my own custom color table with terminologies, do I need to create 0 Background entry with color (0,0,0) or is that automatically appended?</p>
</blockquote>
</aside>
<p>No need for defining a color for the 0 value for segmentations.</p>
<p>0 always corresponds to background, so it is never mapped to a segment. Its only use is when somebody applies the color table to display a labelmap volume and he wants to set a background color&amp;opacity.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I have a little issue with opacity being always 0 for all blank entries, which complicated setting the color from the palette. But it is a minor one. I suspect most of the time people will either choose from the terminology module or enter the RGB code in the table. Otherwise table creation seems to work well.</p>
</blockquote>
</aside>
<p>An entry can be made undefined by clicking the delete color (red <code>-</code>) button above the color table. The color will not be undefined if you set to a specific color (even if you set it to, RGBA=(0,0,0,0)).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>When I am using this color table during segmentation, Terminology selector seems to keep defaulting to Slicer’s own terminology. Can we make the change that Terminology module opens with the latest selected terminology/color table from the top drow down.</p>
</blockquote>
</aside>
<p>The terminology for a segment is copied from the previous segment. You got the default terminology because you added all your segments, which were all set to the default terminology entry.</p>
<p>The solution is to add the first segment, set the terminology from the color table, and then add all the other segments.</p>
<p>We could tune this behavior to make it more intuitive. We could probably avoid setting a default terminology when adding a new segment (leave the terminology undefined). Then we would always look up the context from any previous segment that has defined terminology.</p>

---

## Post #3 by @muratmaga (2025-03-05 00:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The solution is to add the first segment, set the terminology from the color table, and then add all the other segments.</p>
</blockquote>
</aside>
<p>OK. That helped, and it kept bringing the right color table. However, after adding a few more segments, this message popped up:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c159f04bbce0b96375e0488c2c2c6df3fc99540.png" data-download-href="/uploads/short-url/fq9TaWkjIzvasIcjDMgQqrax0Dm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c159f04bbce0b96375e0488c2c2c6df3fc99540_2_690x405.png" alt="image" data-base62-sha1="fq9TaWkjIzvasIcjDMgQqrax0Dm" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c159f04bbce0b96375e0488c2c2c6df3fc99540_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c159f04bbce0b96375e0488c2c2c6df3fc99540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c159f04bbce0b96375e0488c2c2c6df3fc99540.png 2x" data-dominant-color="D9DCE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">692×407 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I presume I need to choose “Keep using the terminology selector”?</p>

---

## Post #4 by @lassoan (2025-03-05 01:14 UTC)

<p>It seems that you keep clicking on the color box, so the application is guessing that you just want to change colors and may be frustrated to see a terminology selector. You can confirm that you want to keep using the terminology selector even when clicking the color box by selecting “Keep using terminology selector”.</p>
<p>It is all supposed to be self-explanatory, so the fact that you need to ask for clarification means that we need to improve things. Let us know if you have any suggestions about what and how to change.</p>

---

## Post #5 by @muratmaga (2025-03-05 01:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is all supposed to be self-explanatory, so the fact that you need to ask for clarification means that we need to improve things. Let us know if you have any suggestions about what and how to change.</p>
</blockquote>
</aside>
<p>I don’t think I clicked on the colors, but the actual terms. So here are my steps:</p>
<ol>
<li>I created a custom color table with 6 entries from Uberon</li>
<li>Loaded a volume and right-click to start the segmentation</li>
<li>I added a blank segments, which initialized as Segment_1, I double-click the name and the terminology module came. I chose my color table, and then picked up a term.</li>
<li>I added another blank segment, which came as Segment_1 (or might have been Segment_2), which I double-clicked to set. Terminology selector came with my color table prepopulated (as I wanted it to be). I picked up another term.</li>
<li>I repeat this procedure and at the 5th or 6th one, this window came up.</li>
</ol>
<p>Am I missing a step?</p>

---

## Post #6 by @lassoan (2025-03-05 05:31 UTC)

<p>Thanks for the further testing. I’ve checked the implementation and the actions that we count is the number of times the user selects a custom segment name or color (it does not matter if you double-click on the color box or the segment name). However, when the user chose a color from the color table, it was always counted as a custom segment name/color selection. I’ll submit a fix tomorrow.</p>

---

## Post #7 by @cpinter (2025-03-05 14:37 UTC)

<p>Thanks for the discussion!</p>
<p>I don’t understand the issue with the custom colors/names. Can you please explain what you <a class="mention" href="/u/lassoan">@lassoan</a> found the problem was and how should we fix it?</p>

---

## Post #8 by @muratmaga (2025-03-05 16:30 UTC)

<p>I think the main issue is clicks to choose a proper label for a segment from color table should not count towards that popup message, because that’s the intended usage, and it confuses the user (making them think they are not doing something right).</p>
<p>The popup meant to bring back the older renaming style for people who do NOT want to use terminology module.</p>
<p>At least that’s the issue I am trying to resolve.</p>

---

## Post #9 by @cpinter (2025-03-05 16:42 UTC)

<p>Thanks! I’m curious of the explanation of <a class="mention" href="/u/lassoan">@lassoan</a> because as I recall this feature was not supposed to do this, so just want to know what went wrong and what we want to do instead.</p>

---

## Post #10 by @muratmaga (2025-03-07 05:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>No need for defining a color for the 0 value for segmentations.</p>
<p>0 always corresponds to background, so it is never mapped to a segment. Its only use is when somebody applies the color table to display a labelmap volume and he wants to set a background color&amp;opacity.</p>
</blockquote>
</aside>
<p>Maybe I am doing something wrong, but this is the labelmap I am getting when I use <code>Segmentations</code> module to export a labelmap from a segmentation I created using color table:</p>
<p>This is the actual segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d09e76eab5ec973adb9552f546f4b88b117317fd.jpeg" data-download-href="/uploads/short-url/tLwOZLogYwOGVvaHCisJUbvqTRb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d09e76eab5ec973adb9552f546f4b88b117317fd_2_690x248.jpeg" alt="image" data-base62-sha1="tLwOZLogYwOGVvaHCisJUbvqTRb" width="690" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d09e76eab5ec973adb9552f546f4b88b117317fd_2_690x248.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d09e76eab5ec973adb9552f546f4b88b117317fd_2_1035x372.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d09e76eab5ec973adb9552f546f4b88b117317fd_2_1380x496.jpeg 2x" data-dominant-color="8B8D90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×691 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is with the exported labelmap<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df277992a9337506546c1c9639a5478e5c9e017.jpeg" data-download-href="/uploads/short-url/1ZnGOSr15LIt9BODT9u3P9FW0Kj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df277992a9337506546c1c9639a5478e5c9e017_2_690x377.jpeg" alt="image" data-base62-sha1="1ZnGOSr15LIt9BODT9u3P9FW0Kj" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df277992a9337506546c1c9639a5478e5c9e017_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df277992a9337506546c1c9639a5478e5c9e017_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df277992a9337506546c1c9639a5478e5c9e017_2_1380x754.jpeg 2x" data-dominant-color="B6A9B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1051 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To create the labelmap, I went to the segmentations module, choose Export labelmap, click on <code>Use Color Table Values</code> and specified my custom color table.</p>
<p>If I don’t do that, but simply right-click in SH to export as a labelmap, I don’t get my Color Table 0 being assigned to the background, but then assigned indices are not the ones I specified in the color table (Based on color table lateral parasympasial foramen, blue segment, should have label value of 3, but instead it got 1, since it is the first segment)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/837ebffb0326e6d76d956a54c5eb5701691efd66.jpeg" data-download-href="/uploads/short-url/iLg6LkO2GoFrPIGZwLIXGBjOgSi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/837ebffb0326e6d76d956a54c5eb5701691efd66_2_690x376.jpeg" alt="image" data-base62-sha1="iLg6LkO2GoFrPIGZwLIXGBjOgSi" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/837ebffb0326e6d76d956a54c5eb5701691efd66_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/837ebffb0326e6d76d956a54c5eb5701691efd66_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/837ebffb0326e6d76d956a54c5eb5701691efd66_2_1380x752.jpeg 2x" data-dominant-color="A6A4A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1049 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Perhaps these types of color table entries should start from 1, instead of 0?</p>

---

## Post #11 by @cpinter (2025-03-07 10:41 UTC)

<p>Thanks for the feedback! I’ll look into this today.</p>

---

## Post #12 by @lassoan (2025-03-07 12:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Perhaps these types of color table entries should start from 1, instead of 0?</p>
</blockquote>
</aside>
<p>Yes, the issue is that the bacground label is missing.</p>
<p>Did you create the color table manually? Did you set a color and terminology for the background (label value=0)?</p>
<p>If yes then we have to somehow make it more difficult to specify a color and terminology for label=0, because a custom background is very rarely needed (and never needed if you use the color table for segmentation conversion). Maybe a warning popup or hiding the label=0 entry by default would be sufficient?</p>

---

## Post #13 by @muratmaga (2025-03-07 15:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Did you create the color table manually? Did you set a color and terminology for the background (label value=0)?</p>
</blockquote>
</aside>
<p>I used the colors module to create the table. The first entry for “0”, hence I asked whether I should create a background label at the beginning of this thread. So it appears, while I don’t need to create an explicit 0=background label, I also shouldn’t have created a specific label entry at 0, but instead start from 1.</p>
<p>is that correct way of explaining? Is there any reason 0 is not auto-populated as a background?</p>

---

## Post #14 by @lassoan (2025-03-07 19:10 UTC)

<p>The label=0 entry is always left empty by default. You only ever see the background label if you explicitly uncheck the “Hide empty colors” checkbox. If you add colors using the green “+” button (same way as for segments) then you never ever see the background label and never get tempted to specify some custom name or color for it.</p>
<p>But I completely understand that since the spinbox for modifying the number of colors is displayed quite prominently, you may decide to use that to increase the table size, and then you don’t understand why you don’t see any change, so you uncheck the “Hide empty colors” checkbox, which then shows the background color as well.</p>
<p>Maybe moving the “Number of colors” entry to some advanced section could help. Or maybe even better would be to have a separate checkbox to show the background label (in an advanced section, so that only very advanced users would find it)?</p>

---

## Post #15 by @muratmaga (2025-03-07 21:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="41963">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You only ever see the background label if you explicitly uncheck the “Hide empty colors” checkbox. If you add colors using the green “+” button (same way as for segments) then you never ever see the background label and never get tempted to specify some custom name or color for it.</p>
</blockquote>
</aside>
<p>Actually my usage was different: After I click on create a new color table button, instead of using + or -, I simply entered the number of labels I wanted in the field that says “Number of Colors”, as I thought that was expected of me.</p>
<p>Now, I understand for this use case I need to use the + and - buttons, but I am not sure it is quite obvious.</p>

---

## Post #16 by @muratmaga (2025-03-07 21:59 UTC)

<p>I still think it might be a good idea to slightly differentiate this type of color table creation from regular color table? That way maybe the number of colors is not an editable field?</p>

---

## Post #17 by @lassoan (2025-03-07 22:10 UTC)

<p>Yes, we definitely need to change the GUI to make it easier to use as intended. Hiding the background color even if showing other undefined colors will be needed but maybe also the number of colors spinbox can be moved to an advanced section.</p>

---
