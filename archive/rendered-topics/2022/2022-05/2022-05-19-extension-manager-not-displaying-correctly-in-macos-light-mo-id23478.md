---
topic_id: 23478
title: "Extension Manager Not Displaying Correctly In Macos Light Mo"
date: 2022-05-19
url: https://discourse.slicer.org/t/23478
---

# Extension Manager not displaying correctly in MacOS Light Mode

**Topic ID**: 23478
**Date**: 2022-05-19
**URL**: https://discourse.slicer.org/t/extension-manager-not-displaying-correctly-in-macos-light-mode/23478

---

## Post #1 by @Doodads (2022-05-19 03:23 UTC)

<p>MacOS Version: 12.2.1<br>
Slicer Version: 4.11.20210226</p>
<p>Opening the extension manager with “Dark” display mode switched off on MacOS 12.2.1 shows a mostly white window; this is fixed when “Dark” mode is switched on. (see images below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356eb3a2d8278f8066959a185778fd247431820b.png" data-download-href="/uploads/short-url/7CGtXzzYIe19EXjyyPe0vgD9Mqn.png?dl=1" title="Screenshot 2022-05-19 at 11.13.27 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/356eb3a2d8278f8066959a185778fd247431820b_2_690x493.png" alt="Screenshot 2022-05-19 at 11.13.27 AM" data-base62-sha1="7CGtXzzYIe19EXjyyPe0vgD9Mqn" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/356eb3a2d8278f8066959a185778fd247431820b_2_690x493.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356eb3a2d8278f8066959a185778fd247431820b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356eb3a2d8278f8066959a185778fd247431820b.png 2x" data-dominant-color="F6F8FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-05-19 at 11.13.27 AM</span><span class="informations">832×595 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/913cec44ac3f968c06406fbc0e3ec9acf5844f23.png" data-download-href="/uploads/short-url/kIPL7lpn31zrkJ1BS94pL5xXg4j.png?dl=1" title="Screenshot 2022-05-19 at 11.13.36 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/913cec44ac3f968c06406fbc0e3ec9acf5844f23_2_690x493.png" alt="Screenshot 2022-05-19 at 11.13.36 AM" data-base62-sha1="kIPL7lpn31zrkJ1BS94pL5xXg4j" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/913cec44ac3f968c06406fbc0e3ec9acf5844f23_2_690x493.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/913cec44ac3f968c06406fbc0e3ec9acf5844f23.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/913cec44ac3f968c06406fbc0e3ec9acf5844f23.png 2x" data-dominant-color="CFCFDA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-05-19 at 11.13.36 AM</span><span class="informations">833×596 74.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2022-05-19 13:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Since this was brought up again, should we reopen <a href="https://github.com/Slicer/Slicer/issues/5118" class="inline-onebox" rel="noopener nofollow ugc">Colors are washed out in extensions manager on macOS Catalina · Issue #5118 · Slicer/Slicer · GitHub</a>?</p>

---

## Post #3 by @lassoan (2022-05-19 13:46 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks for pointing out the related issue.</p>
<p><a class="mention" href="/u/doodads">@Doodads</a></p>
<ol>
<li>Please provide information on your system (e.g., MacBook Pro Mid 2015, Intel Iris Pro 1536 MB).</li>
<li>Please try if these commands fix the display without requiring you to change your macOS settings: <a href="https://github.com/Slicer/Slicer/issues/5118#issuecomment-809905039" class="inline-onebox">Colors are washed out in extensions manager on macOS Catalina · Issue #5118 · Slicer/Slicer · GitHub</a>
</li>
</ol>

---

## Post #4 by @Doodads (2022-06-01 10:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Sorry for taking awhile to get back to you. And thanks for your assistance.</p>
<ol>
<li>MacBook Pro (Retina, 15-inch, Mid 2015) Intel Iris Pro 1536 MB</li>
<li>I tried the “export…” from a terminal window then using “open Slicer.app” to start slicer. This did not work on my system.</li>
</ol>

---

## Post #5 by @lassoan (2022-06-01 11:38 UTC)

<p>Thanks for the additional information. This is a known issue on this system. Since we can only spend time with fixing issues with hardware released in the last 5 years, you need to address this by changing the system to dark mode or try one of the workarounds described <a href="https://github.com/Slicer/Slicer/issues/5118#issuecomment-809905039">here</a>.</p>

---
