# Slicer module panel icon in dark mode

**Topic ID**: 8353
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/slicer-module-panel-icon-in-dark-mode/8353

---

## Post #1 by @lassoan (2019-09-10 01:55 UTC)

<p>I noticed that the “3D Slicer” icon at the top of module panel looks quite ugly in dark mode.</p>
<p>Current icon in default and dark mode:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82fc3a68241419bf98694595637fec50d474a080.png" data-download-href="/uploads/short-url/iGKsYZLI2Ii1mFUL2HQMMW2vObC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82fc3a68241419bf98694595637fec50d474a080_2_690x229.png" alt="image" data-base62-sha1="iGKsYZLI2Ii1mFUL2HQMMW2vObC" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82fc3a68241419bf98694595637fec50d474a080_2_690x229.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82fc3a68241419bf98694595637fec50d474a080_2_1035x343.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82fc3a68241419bf98694595637fec50d474a080_2_1380x458.png 2x" data-dominant-color="B3B3B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1593×530 45.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is not easy to create a version of the icon that looks acceptable in dark mode due to the dark shadow below the icon and the dark letters of the text and lines of the dark lines of the slice contours. I’ve removed the shadow and added bright glow to give some contrast around the gray letters and lines. Here is the result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69f53ac1c1bbb74274dc2a4209f97b3dbe95fa61.png" data-download-href="/uploads/short-url/f7lxfdSf3l9QmWp2kp206sm5Udz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f53ac1c1bbb74274dc2a4209f97b3dbe95fa61_2_690x230.png" alt="image" data-base62-sha1="f7lxfdSf3l9QmWp2kp206sm5Udz" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f53ac1c1bbb74274dc2a4209f97b3dbe95fa61_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f53ac1c1bbb74274dc2a4209f97b3dbe95fa61_2_1035x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f53ac1c1bbb74274dc2a4209f97b3dbe95fa61_2_1380x460.png 2x" data-dominant-color="ABABAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1591×532 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Should we replace the current icon with this revised icon?</strong></p>
<p><strong>Do anyone want to give a try to come up with a better icon that works on both bright and dark background?</strong> Ideally, it would be a single icon and that works for both “dark” and “bright” backgrounds (switching icon based on  background color would need some non-trivial software changes).</p>

---

## Post #2 by @jamesobutler (2019-09-10 04:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="8353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should we replace the current icon with this revised icon?</p>
</blockquote>
</aside>
<p>That is MUCH better than the current look so <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> for a minor improvement.</p>
<p><strong>Regarding general improvements:</strong><br>
I would agree that a major factor should be the icon’s ability to look good on both light and dark backgrounds and for a logo to have a design that has the same feel when using the version for either on light or dark background. Slack had to do a refresh of their logo and icon this year for this very reason. You can read <a href="https://slackhq.com/say-hello-new-logo" class="inline-onebox" rel="noopener nofollow ugc">Say hello, new logo | Slack</a>.</p>
<p>I think color works really well though the current state of the logo is heavy on grayscale which isn’t that great on white or black. I tried reading through the <a href="https://www.slicer.org/w/images/9/9f/3DSlicerBrandGuidelines.pdf" rel="noopener nofollow ugc">3D Slicer Visual Communication Guide</a> to understand the background and usage.</p>
<ul>
<li>The lighter gray for “3D” restricts the ability of the “Slicer” text being white or black depending on the background. I think the text color needs to become the same.</li>
<li>Maybe the “3D” part even gets dropped <img src="https://emoji.discourse-cdn.com/twitter/speak_no_evil.png?v=12" title=":speak_no_evil:" class="emoji" alt=":speak_no_evil:" loading="lazy" width="20" height="20">. It does seem like the “3D” part is dropped in more cases than not including the domain “<a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>”.</li>
<li>Dark support is also important when Slicer runs on macOS Mojave with Qt 5.12+ with macOS dark mode support (built with 10.14 SDK though deployment target could still be 10.12). Mojave is almost a year old and macOS Catalina will be out soon.</li>
</ul>

---

## Post #3 by @rkikinis (2019-09-10 05:28 UTC)

<p>3D Slicer is the registered trademark. USPTO was not willing to trademark Slicer because it’s too broad</p>

---

## Post #4 by @pieper (2019-09-10 12:00 UTC)

<p>Excellent points - it makes good sense to have a new look that takes these points into account.  I added a note on the <a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Additional_proposed_changes_to_be_discussed" rel="nofollow noopener">Slicer5</a> page.</p>
<p>I agree glow looks better in dark mode than the block of white.</p>

---

## Post #5 by @jamesobutler (2019-09-10 13:49 UTC)

<aside class="quote no-group" data-username="rkikinis" data-post="3" data-topic="8353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rkikinis/48/791_2.png" class="avatar"> rkikinis:</div>
<blockquote>
<p>USPTO was not willing to trademark Slicer because it’s too broad</p>
</blockquote>
</aside>
<p>Ah I see. It appears that the mark “Slicer” has been registered several times since “3D Slicer” was originally registered. They must have changed their mind. The Slicer org could probably apply and register “Slicer” if it wanted to pay.</p>
<p><strong>3D Slicer</strong> - 85269905 - IC 009. US 021 023 026 036 038. G &amp; S: Computer software for data visualization and image analysis. Registered February 14, 2012</p>
<p>Slicer - 86141772  - IC 009. US 021 023 026 036 038. G &amp; S: Computer software for processing electronic payments. Registered March 31, 2015</p>
<p>Slicer - 86788945 - IC 008. US 023 028 044. G &amp; S: Hand-operated food processors. Registered December 13, 2016</p>
<p>Slicer - 86788915 - IC 021. US 002 013 023 029 030 033 040 050. G &amp; S: Kitchen utensils. Registered June 27, 2017</p>
<p>Slicer - 87089955 - IC 042. US 100 101. G &amp; S: Providing online nondownloadable software enabling image-based business data analysis of merchandise. Registered June 6, 2017.</p>
<p>Slicer - 87371574 - IC 005. US 006 018 044 046 051 052. G &amp; S: Albumin dietary supplements. Registered April 10, 2018.</p>
<p>Slicer - 87089944 - 	IC 009. US 021 023 026 036 038. G &amp; S: computer software for business intelligence analytics. Registered September 4, 2018.</p>

---

## Post #6 by @lassoan (2019-09-10 17:27 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="8353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It appears that the mark “Slicer” has been registered several times since “3D Slicer” was originally registered.</p>
</blockquote>
</aside>
<p>Maybe the electronic payment company had better lawyers… Anyway, there was no other medical software that was awarded the name “Sicer”.</p>
<p>I’ve updated all the icons in the core application and main modules to have transparent background (most of them already had that) and added a bit of bright highlight in icons that were too dark. They should look exactly the same in the default mode, but in dark mode they look a bit better.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23e39b1496c7f7793baba7c2b11ae6e367e267c3.png" data-download-href="/uploads/short-url/57ulZ6GARg32iFeex8ced8mbpcL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e39b1496c7f7793baba7c2b11ae6e367e267c3_2_690x176.png" alt="image" data-base62-sha1="57ulZ6GARg32iFeex8ced8mbpcL" width="690" height="176" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e39b1496c7f7793baba7c2b11ae6e367e267c3_2_690x176.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e39b1496c7f7793baba7c2b11ae6e367e267c3_2_1035x264.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23e39b1496c7f7793baba7c2b11ae6e367e267c3_2_1380x352.png 2x" data-dominant-color="424048"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1966×504 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>A graphics designer should go through all our icons and update them to make them look more consistent. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> will ask Kitware’s designer about it.</p>

---

## Post #7 by @lassoan (2019-09-11 00:58 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="2" data-topic="8353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I would agree that a major factor should be the icon’s ability to look good on both light and dark backgrounds and for a logo to have a design that has the same feel when using the version for either on light or dark background. Slack had to do a refresh of their logo and icon this year for this very reason. You can read <a href="https://slackhq.com/say-hello-new-logo" class="inline-onebox">Say hello, new logo | Slack</a>.</p>
</blockquote>
</aside>
<p>I like the Slack logo. It would be great if the Slicer logo could be modernized similarly (simplified, flat look, compatible with both bright and dark background, etc.).</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="8353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Maybe the “3D” part even gets dropped</p>
</blockquote>
</aside>
<p>It would be much harder for poeple to find “Slicer” compared to “3D Slicer”. It would be very hard to find projects and papers that use Slicer (if we find something that refers to “3D Slicer” or “3DSlicer” then there is a very high chance that it is about this application). Slicer name would also confuse Slic3r users even more (because Slicer is used for 3D printing, too, and it slices the images).</p>

---

## Post #8 by @jamesobutler (2019-09-11 02:32 UTC)

<p>Yes, the search term “3D Slicer” will find this software better than just “Slicer” so I can see needing to maintain that.</p>
<p><strong>Regarding the <a href="https://www.slicer.org/w/images/9/9f/3DSlicerBrandGuidelines.pdf" rel="noopener nofollow ugc">3D Slicer Visual Communication Guide</a>:</strong><br>
Is there a newer version of this guideline? If so, potentially ignore the below comments.</p>
<ul>
<li>
<p>The horizontal and vertical versions of the logo do not seem to conform to the guideline for the term as the text appears as “3DSlicer” which is defined as being incorrect. Seems like the logo should have a clear space so it is seen as “3D Slicer” which is the official mark.</p>
</li>
<li>
<p>The title of the Wikipedia page (<a href="https://en.m.wikipedia.org/wiki/3DSlicer" class="inline-onebox" rel="noopener nofollow ugc">3D Slicer - Wikipedia</a>) is also “3DSlicer” which doesn’t conform and an edit should probably be issued.</p>
</li>
<li>
<p>The name of the the twitter account is also incorrectly using the term “3DSlicer”.</p>
</li>
<li>
<p>The “small desktop/favicon” logo version is also being incorrectly used for the twitter account. I’ve never seen this cream color used before. Originally from Slicer’s own wiki (?). <a href="https://www.slicer.org/wiki/File:Logo-3DSlicer.png" class="inline-onebox" rel="noopener nofollow ugc">File:Logo-3DSlicer.png - Slicer Wiki</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7379a3fb4f932fb56c1f66308422eec3cbc9597c.jpeg" alt="image" data-base62-sha1="gtxwpApJDVEUVlTPPI2Ubx0rUMQ" width="348" height="411"></p>
</li>
</ul>

---

## Post #9 by @rkikinis (2019-09-11 03:13 UTC)

<p>I am very supportive of an update and improved consistency.</p>
<p>It is difficult to maintain consistency over decades. Creating a new updated version of the guidelines would be greatly appreciated.</p>
<p>The logo has a huge brand recognition and we should make changes cautiously in order not to loose the brand recognition. If you look at NASA ‘s logo over time versus the GE logo over time you will see what I mean.</p>

---

## Post #10 by @Sam_Horvath (2019-09-11 14:12 UTC)

<p>Some items / thoughts:</p>
<ul>
<li>Once we decide how we want to logo updated, we will be able to have the Kitware graphic designer finalize / polish / etc</li>
<li>I think the most direct way to modernize the logo would be to
<ul>
<li>Remove the three thin cut planes from all versions of the logo (use favicon style)</li>
<li>Change text to “3D Slicer”</li>
<li>Switch from shaded to flat coloring</li>
</ul>
</li>
</ul>

---

## Post #11 by @pieper (2019-09-11 17:24 UTC)

<p>I like those suggestions <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">  I can imaging a non-shaded version that is still clearly the slicer logo, but simplified will look cleaner and more modern.</p>

---

## Post #12 by @Davide_Punzo (2020-02-07 09:37 UTC)

<p>Hi all, I was wondering if anyone has started working/planned to work on the Slicer icons when the default style will be the dark style one in Slicer5. For example, the icons in the toolbar may need some work:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bf9c9ca3154ed261579560639f515687906f762.png" data-download-href="/uploads/short-url/hGJTEM5RSSzooZvTeqI4MZJSbzY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bf9c9ca3154ed261579560639f515687906f762_2_690x107.png" alt="image" data-base62-sha1="hGJTEM5RSSzooZvTeqI4MZJSbzY" width="690" height="107" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bf9c9ca3154ed261579560639f515687906f762_2_690x107.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bf9c9ca3154ed261579560639f515687906f762_2_1035x160.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bf9c9ca3154ed261579560639f515687906f762.png 2x" data-dominant-color="D9DCD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1192×185 27.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer icons also do not have a common theme (usually each set being done by the module developers). Maybe we should think to use an icon theme. Probably going for “windows-flat” icons will not be a good idea for 3DSlicer (since flat icons works well if the GUI elements are also very flat), but we could have a common theme. For example the overall overview of the paraview toolbars and icons looks much better:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02a2e36b90d3455bb3f7183405953538f6ef70c7.png" data-download-href="/uploads/short-url/njWnFR3Otle5Xwfr5FirEtTtiv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a2e36b90d3455bb3f7183405953538f6ef70c7_2_690x81.png" alt="image" data-base62-sha1="njWnFR3Otle5Xwfr5FirEtTtiv" width="690" height="81" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02a2e36b90d3455bb3f7183405953538f6ef70c7_2_690x81.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02a2e36b90d3455bb3f7183405953538f6ef70c7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02a2e36b90d3455bb3f7183405953538f6ef70c7.png 2x" data-dominant-color="E0E1DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1005×119 32.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2020-02-07 14:46 UTC)

<p>The icons have been already made compatible with dark background (without that many icons would not be recognizeable at all), but I fully agree that a complete redesign of all icons would be needed - to keep up with current design trends, increased screen resolution, and bright/dark mode requirements.</p>
<p>As far as I remember, <a class="mention" href="/u/jcfr">@jcfr</a> mentioned that Kitware’s designer may give this a try.</p>

---

## Post #14 by @pieper (2020-02-07 17:49 UTC)

<p>We might be able to leverage and extend some of this work: <a href="https://react.ohif.org/elements/icon">https://react.ohif.org/elements/icon</a></p>
<p>Any end users or developers who want to contribute icons would be welcome.  It would be a great way to contribute to the project for people who may not be in-depth developers.</p>

---
