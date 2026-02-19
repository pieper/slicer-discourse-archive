---
topic_id: 12077
title: "Automatic Dark Mode On Mac In Recent Slicer Preview Releases"
date: 2020-06-17
url: https://discourse.slicer.org/t/12077
---

# Automatic dark mode on Mac in recent Slicer Preview releases

**Topic ID**: 12077
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/automatic-dark-mode-on-mac-in-recent-slicer-preview-releases/12077

---

## Post #1 by @smrolfe (2020-06-17 19:06 UTC)

<p>I’m having some issues with the view properties in today’s Mac preview version 29150. The background and some of the text are dark (see below) with the default Slicer appearance settings. I can fix it by toggling between Slicer and Dark Slicer, but it reverts each time the application is opened.</p>
<p>My OS is Catalina, 10.15.5</p>
<p>The extensions are also not loading in the extension manager, but it from <a href="https://discourse.slicer.org/t/extension-manager-problems/11946">this thread</a> it sounds I may need to wait a few hours?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3633a7d86438b02189f24208dd49ee7738fce88e.jpeg" data-download-href="/uploads/short-url/7JusdsxYFnICZcJ81F0oQyVQ7bo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3633a7d86438b02189f24208dd49ee7738fce88e_2_690x416.jpeg" alt="image" data-base62-sha1="7JusdsxYFnICZcJ81F0oQyVQ7bo" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3633a7d86438b02189f24208dd49ee7738fce88e_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3633a7d86438b02189f24208dd49ee7738fce88e_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3633a7d86438b02189f24208dd49ee7738fce88e_2_1380x832.jpeg 2x" data-dominant-color="333437"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2972×1794 445 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2020-06-17 21:15 UTC)

<p>Interesting that the text “Slicer” in the Style combobox is dark and the “Welcome to Slicer” module text in that combobox is dark as well.</p>
<p>This behavior is working correctly when I toggle between style on Windows and is correct on startup of Slicer as well.  There has been some weird things as related to switching style for the DICOM database widget as described <a href="https://github.com/Slicer/Slicer/issues/4803#issuecomment-644255623" rel="noopener nofollow ugc">here</a>. Maybe there are some additional issues caused by CTK widgets that are messing up how the palette gets propagated down.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/199ce394ea8ba38561aa752e03255b509b1c8a2b.png" data-download-href="/uploads/short-url/3EA4kAZQsXtcZlCvqkcfscH0uJt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/199ce394ea8ba38561aa752e03255b509b1c8a2b_2_690x372.png" alt="image" data-base62-sha1="3EA4kAZQsXtcZlCvqkcfscH0uJt" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/199ce394ea8ba38561aa752e03255b509b1c8a2b_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/199ce394ea8ba38561aa752e03255b509b1c8a2b_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/199ce394ea8ba38561aa752e03255b509b1c8a2b_2_1380x744.png 2x" data-dominant-color="3C3C44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1036 80.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @smrolfe (2020-06-17 21:38 UTC)

<p>Yes, the palette on opening is not the same as the dark Slicer style. If I change the style to dark Slicer the text shows up white as usual. Toggling one more time back to the default Slicer style will revert back to white background/dark text, but I have to do this every time I launch.</p>

---

## Post #4 by @jamesobutler (2020-06-17 21:54 UTC)

<p>Got it. So only on start of Slicer with Dark Slicer specified will it have incorrect text color in some widgets on macOS.</p>
<p>From your screenshot the style is showing as “Slicer” in the combobox, but the palette is dark.  Is this dark mode being controlled by macOS?  Or is this an error on start where it is setting the “Dark Slicer” style, but showing the incorrect selection in the settings entry as “Slicer” instead of “Dark Slicer”? Are there any issues in the log?</p>

---

## Post #5 by @jamesobutler (2020-06-17 21:56 UTC)

<p>I noticed from my own screenshot that upon changing to “Dark Slicer” the link text in the Feedback section of the Welcome module is incorrect, but upon collapsing/uncollapsing it is then correct. So maybe just an issue with the widget not updating.</p>

---

## Post #6 by @smrolfe (2020-06-17 22:00 UTC)

<p>It’s the default Slicer style in my screenshot, showing up with dark background and dark text. There’s no settings on my Mac that would effect this. I don’t usually use dark slicer.</p>
<p>So every time I launch with the default Slicer style (not dark Slicer) I am getting dark background/dark text.</p>

---

## Post #7 by @jamesobutler (2020-06-17 22:05 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="6" data-topic="12077">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>So every time I launch with the default Slicer style (not dark Slicer) I am getting dark background/dark text.</p>
</blockquote>
</aside>
<p>And this is a new thing that “Slicer” style shows Dark background? Did it previously look like the following with the regular “Slicer” style with the light color?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3471f603f5039afeb517fd048ea6a4652ab2df5c.png" data-download-href="/uploads/short-url/7tWZiQPnLfQSNpyGZbAZdpHjea0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3471f603f5039afeb517fd048ea6a4652ab2df5c_2_690x373.png" alt="image" data-base62-sha1="7tWZiQPnLfQSNpyGZbAZdpHjea0" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3471f603f5039afeb517fd048ea6a4652ab2df5c_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3471f603f5039afeb517fd048ea6a4652ab2df5c_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/3471f603f5039afeb517fd048ea6a4652ab2df5c_2_1380x746.png 2x" data-dominant-color="66656D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 63.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @smrolfe (2020-06-17 22:08 UTC)

<p>Yes, that’s correct. I noticed the dark background/dark text in yesterday’s release for the first time.</p>

---

## Post #9 by @jamesobutler (2020-06-18 19:21 UTC)

<p>I think this corresponds with the macOS factory build using the latest Qt 5.15 version which was built using the macOS 10.14 SDK which brought support for macOS dark mode.  <a class="mention" href="/u/smrolfe">@smrolfe</a> Do you have Dark Mode turned on for macOS? If you switch to the light mode in macOS and then launch Slicer with the “Slicer” style is it light again and will toggle just the application dark when switching to “Dark Slicer” style?</p>

---

## Post #10 by @smrolfe (2020-06-18 21:13 UTC)

<p>Thanks, I did have dark mode turned on for the macOS and the problem resolved when I switched the OS back to light mode. It does look like the issue is tied to that build, if I launch a preview version from 6/6 and the one from today, you can see the difference (both with MacOS in dark mode).</p>
<p>Is it possible to switch to the dark Slicer style when the MacOS set to dark mode? Or alternatively, allow the the Slicer/Dark Slicer setting to override the OS setting? This seems possible within one session, but doesn’t persist.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/668fa2813e8db0e93ca7324ab7aadde7c0e1c378.png" data-download-href="/uploads/short-url/eDira1J2bHFKFxPvhWjKSuOsG3m.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/668fa2813e8db0e93ca7324ab7aadde7c0e1c378_2_690x382.png" alt="image" data-base62-sha1="eDira1J2bHFKFxPvhWjKSuOsG3m" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/668fa2813e8db0e93ca7324ab7aadde7c0e1c378_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/668fa2813e8db0e93ca7324ab7aadde7c0e1c378_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/668fa2813e8db0e93ca7324ab7aadde7c0e1c378_2_1380x764.png 2x" data-dominant-color="8F9096"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3316×1836 759 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @jamesobutler (2020-06-18 21:57 UTC)

<p>I think we should let macOS handle the light/dark mode transition and make the Slicer style setting option only available for the other platforms that don’t have system wide controlled dark mode.</p>
<p>From your screenshots of the macOS controlled look, the colors are all a little bit darker than what was defined in “Dark Slicer”. I should probably make it so that on Windows the dark mode looks like what is done automatically on macOS when in dark mode.</p>

---

## Post #12 by @jamesobutler (2020-06-18 23:18 UTC)

<p><a class="mention" href="/u/smrolfe">@smrolfe</a> Could you start Slicer and get screenshots using the “Slicer” style with the macOS dark mode enabled for the “Models” and “Segment Editor” module? There are some additional colors that those screenshots would have to make the “Dark Slicer” match more closely.</p>

---

## Post #13 by @lassoan (2020-06-19 00:04 UTC)

<p>These all seem to be standard Qt behavior now. The switch is still manual on Windows, and probably on Linux, too.</p>
<p>We are in quite good shape, we just have to figure out why a few windows and colors are not right, and find a way to make our icons look better in dark mode (and today’s screen resolutions).</p>

---

## Post #14 by @smrolfe (2020-06-23 17:29 UTC)

<p>Sorry for the delayed response <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. I’m attaching the “Models” and “Segment Editor” screenshots. These were taken with macOS in dark mode and “Slicer” style.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e268ce3d554458b7ff138d5bcac3ef95c518d1bf.png" data-download-href="/uploads/short-url/wiUs6CaWLxbhd5voUgXYdpMWoBp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e268ce3d554458b7ff138d5bcac3ef95c518d1bf_2_690x431.png" alt="image" data-base62-sha1="wiUs6CaWLxbhd5voUgXYdpMWoBp" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e268ce3d554458b7ff138d5bcac3ef95c518d1bf_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e268ce3d554458b7ff138d5bcac3ef95c518d1bf_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e268ce3d554458b7ff138d5bcac3ef95c518d1bf_2_1380x862.png 2x" data-dominant-color="484859"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3360×2100 336 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f697c570aa6572cfe36ac7186bba1dab979d86.png" data-download-href="/uploads/short-url/uwO1u7hVss84QJGPZEiaos0r4nY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f697c570aa6572cfe36ac7186bba1dab979d86_2_690x428.png" alt="image" data-base62-sha1="uwO1u7hVss84QJGPZEiaos0r4nY" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f697c570aa6572cfe36ac7186bba1dab979d86_2_690x428.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f697c570aa6572cfe36ac7186bba1dab979d86_2_1035x642.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f697c570aa6572cfe36ac7186bba1dab979d86_2_1380x856.png 2x" data-dominant-color="484859"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3360×2088 350 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @lassoan (2020-08-20 20:30 UTC)

<p>Thanks to a lot of work by <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, we have now fixed all the known issues (except a few that are entered into the issue tracker). Please enter new bug reports in the issue tracker.</p>

---

## Post #16 by @smrolfe (2020-08-21 16:28 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, this looks great on my machine. I really like the option for Slicer Light!</p>

---

## Post #17 by @jamesobutler (2020-08-21 16:36 UTC)

<p>The palette for Slicer light has been the standard view on Windows forever while macOS always had something slightly different. I’m glad you’re able to enjoy this same experience now.</p>
<p>As it relates to switching between styles, macOS probably still has some issues so providing issue reports will be helpful for improving it on that platform.</p>

---
