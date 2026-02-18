# Segment Statistics Module

**Topic ID**: 34014
**Date**: 2024-01-29
**URL**: https://discourse.slicer.org/t/segment-statistics-module/34014

---

## Post #1 by @Tati (2024-01-29 09:14 UTC)

<p>Hello all,<br>
I have installed the 5.6.1 version of 3D slicer. My problem is related to the segment statistic module; it does not show the Input and Output fields. Could you please guide me on this matter?</p>

---

## Post #2 by @muratmaga (2024-01-29 16:52 UTC)

<p>On windows 5.6.1 Segment Statistics works as intended. Have you actually loaded a segmentation, and a scalar volume into your scene? Can you provide a screenshot?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9675aaf50e22afc148e773f79396436036ba1d7c.png" data-download-href="/uploads/short-url/lt1INWtuLhi7vKYCpzDUgHCUM20.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9675aaf50e22afc148e773f79396436036ba1d7c.png" alt="image" data-base62-sha1="lt1INWtuLhi7vKYCpzDUgHCUM20" width="690" height="236" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×288 4.74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Tati (2024-01-30 10:49 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="34014">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>On windows 5.6.1 Segment Statistics works as intended. Have you actually loaded a segmentation, and a scalar volume into your scene? Can you provide a screenshot?</p>
</blockquote>
</aside>
<p>I have been trying to share a screenshot but I cannot find any relevant icon here. Could you please guide me on how can I attach it?<br>
By the way, the segment statistic module on my screen does not have any field both for input and for output like your screen</p>

---

## Post #4 by @muratmaga (2024-01-30 15:09 UTC)

<p>I simply use whatever screen capture tool the operating system provides. In windows it is called snip. You can google for it</p>

---

## Post #5 by @Tati (2024-01-30 17:22 UTC)

<p>Thanks for your explanation. I think there is a misunderstanding here; I could capture it but I cannot find any icon to share the capture here.</p>

---

## Post #6 by @muratmaga (2024-01-30 19:31 UTC)

<p>You should be able to paste an image into the discourse, as if pasting text.</p>

---

## Post #8 by @Tati (2024-02-04 10:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d602e7de40c778f15bdf52c1a3ea3e965854bd0.png" data-download-href="/uploads/short-url/dk2tjOHVP7X2Q1jM81Su1tghsWY.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d602e7de40c778f15bdf52c1a3ea3e965854bd0_2_690x443.png" alt="Capture" data-base62-sha1="dk2tjOHVP7X2Q1jM81Su1tghsWY" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d602e7de40c778f15bdf52c1a3ea3e965854bd0_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d602e7de40c778f15bdf52c1a3ea3e965854bd0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d602e7de40c778f15bdf52c1a3ea3e965854bd0.png 2x" data-dominant-color="E0DFDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1029×661 53.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks for the guidance.<br>
The screen capture has been attached.<br>
Thanks for your assistance.</p>

---

## Post #9 by @muratmaga (2024-02-04 19:44 UTC)

<p>There is something wrong with your Segment Statistics menu. Since this is a core Slicer module, I would suggest uninstalling and reinstalling Slicer from fresh, and see if that fixes. if it doesn’t, (that’s no module menu is visible), please provide the full Slicer log file (CTRL +0).</p>

---

## Post #10 by @Tati (2024-02-04 20:48 UTC)

<p>Sure, I’ll do that.<br>
Thanks for your assistance.</p>

---

## Post #11 by @lassoan (2024-02-05 23:09 UTC)

<p>Extensions can register additional statistics computation plugins. Probably one of the extensions that  you are installed are not up-to-date and causes an error when the Segment Statistics module is initialized. Please have a look at the application log, you will find the name of the extension in the error message. Let us know which extension was the culprit and also report the problem in that extension’s issue tracker.</p>

---
