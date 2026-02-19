---
topic_id: 25638
title: "Cannot Drag And Drop Segmentation To The Application Window"
date: 2022-10-11
url: https://discourse.slicer.org/t/25638
---

# Cannot drag-and-drop segmentation to the application window and unequal view width on Windows11

**Topic ID**: 25638
**Date**: 2022-10-11
**URL**: https://discourse.slicer.org/t/cannot-drag-and-drop-segmentation-to-the-application-window-and-unequal-view-width-on-windows11/25638

---

## Post #1 by @radiodid (2022-10-11 05:40 UTC)

<p>I used to have 4 equal quadrants while working and now the window with the same settings looks like this and can’t be changed in any way.<br>
Also, I can’t copy existing segmentation lists into Slicer. When transferring files to Slicer, the blocked process icon appears in place of the arrow.</p>
<p>I had this problem once before and solved it by reinstalling the app, but this time I’ve already tried it about a dozen times without getting any results.</p>
<p>Does anyone know how to fix this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6415dd1dc8f69fcec559e4dacb79f3e17074809c.png" data-download-href="/uploads/short-url/ehoAzvyDkexsV8rT9yYKKPLAm9C.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415dd1dc8f69fcec559e4dacb79f3e17074809c_2_690x351.png" alt="image" data-base62-sha1="ehoAzvyDkexsV8rT9yYKKPLAm9C" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415dd1dc8f69fcec559e4dacb79f3e17074809c_2_690x351.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415dd1dc8f69fcec559e4dacb79f3e17074809c_2_1035x526.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415dd1dc8f69fcec559e4dacb79f3e17074809c_2_1380x702.png 2x" data-dominant-color="6B6B77"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×977 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-10-19 06:25 UTC)

<aside class="quote no-group" data-username="radiodid" data-post="1" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9e8a1a/48.png" class="avatar"> radiodid:</div>
<blockquote>
<p>I used to have 4 equal quadrants while working and now the window with the same settings looks like this and can’t be changed in any way.</p>
</blockquote>
</aside>
<p>Does the window size becomes equal once you load an image?</p>
<aside class="quote no-group" data-username="radiodid" data-post="1" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9e8a1a/48.png" class="avatar"> radiodid:</div>
<blockquote>
<p>Also, I can’t copy existing segmentation lists into Slicer. When transferring files to Slicer, the blocked process icon appears in place of the arrow.</p>
</blockquote>
</aside>
<p>This is a limitation of Windows 11. This is the main reason I’m still on Windows 10. Microsoft is supposed to fix it at some point, but right now they say you need to hit Alt-Tab after you started the drag to switch to the bring up the window of the target application.</p>
<aside class="quote no-group" data-username="radiodid" data-post="1" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9e8a1a/48.png" class="avatar"> radiodid:</div>
<blockquote>
<p>I had this problem once before and solved it by reinstalling the app, but this time I’ve already tried it about a dozen times without getting any results.</p>
</blockquote>
</aside>
<p>Which problem? You can reset the application settings by deleting the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">Slicer.ini application settings file</a>.</p>

---

## Post #3 by @radiodid (2022-10-19 08:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which problem?</p>
</blockquote>
</aside>
<p>Both of them - with windows and adding segmentation list</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does the window size becomes equal once you load an image?</p>
</blockquote>
</aside>
<p>No, everything remains the same.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is a limitation of Windows 11. This is the main reason I’m still on Windows 10. Microsoft is supposed to fix it at some point</p>
</blockquote>
</aside>
<p>Yes, I had Windows 11. Unfortunately, I didn’t get an answer quickly, so I reinstalled the system on Windows 10 and now everything works perfectly.<br>
But thanks for the reply anyway. I will be aware of such system limitations in the future.</p>

---

## Post #4 by @lassoan (2022-10-19 17:25 UTC)

<p>Thanks for the additional information. We’ll investigate the view sizing when we switch to Windows11 on developer computers and can reproduce the behavior.</p>

---

## Post #5 by @jamesobutler (2022-10-22 04:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is a limitation of Windows 11. This is the main reason I’m still on Windows 10. Microsoft is supposed to fix it at some point, but right now they say you need to hit Alt-Tab after you started the drag to switch to the bring up the window of the target application.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> This functionality is restored with recently released Windows 11 22H2.</p>

---

## Post #6 by @radiodid (2022-10-22 06:11 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="25638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>This functionality is restored with recently released Windows 11 22H2.</p>
</blockquote>
</aside>
<p>I was offered to upgrade Windows 10 to this version lately, but I don’t want to risk when everything works well.</p>

---
