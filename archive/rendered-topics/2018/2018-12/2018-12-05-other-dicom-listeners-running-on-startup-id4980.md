# "other DICOM listeners running" on startup

**Topic ID**: 4980
**Date**: 2018-12-05
**URL**: https://discourse.slicer.org/t/other-dicom-listeners-running-on-startup/4980

---

## Post #1 by @fedorov (2018-12-05 21:27 UTC)

<p>I recently started seeing the message below every time on startup. I don’t start any listeners knowingly. Is this message expected?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68ebd8a9f4458c3f70b1c3b195a0f574066dcb47.png" alt="image" data-base62-sha1="eYaXevqmtxGzDEQgYIlPNAYEJ7x" width="312" height="113"></p>

---

## Post #2 by @lassoan (2018-12-05 21:45 UTC)

<p>The error message means that the DICOM module detects running processes that have <code>storescp</code> in their name. Do you actually have such processes running?</p>

---

## Post #3 by @fedorov (2018-12-05 21:48 UTC)

<p>No, not to my knowledge. I do not think I knowingly started any storescp processes. I guess I should investigate whether this is caused by any of the extensions first … Let me disable all extensions and see if I still get this popup.</p>

---

## Post #4 by @lassoan (2018-12-05 22:03 UTC)

<p>Storescp may be run by other applications with DICOM networking features, not just by Slicer. When Slicer reports that this process is found, run <code>ps -A</code> to confirm.</p>

---

## Post #5 by @fedorov (2018-12-05 22:07 UTC)

<p>Ah, good point! Indeed, I see it running with <code>ps</code>. But it is running from the Slicer application folder. And it is not stopped when I close Slicer. If I uninstall all extensions, it is still started when I start Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfe60f46a35d4a8c456ad361e8f5a489badcd343.png" data-download-href="/uploads/short-url/rnC62w2OMq5ITCRxW0oH9rb4bOb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfe60f46a35d4a8c456ad361e8f5a489badcd343.png" alt="image" data-base62-sha1="rnC62w2OMq5ITCRxW0oH9rb4bOb" width="690" height="115" data-dominant-color="151515"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×134 18.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-12-05 22:12 UTC)

<p>I think this is a Slicer core feature. Check if “Start listener when Slicer starts” checkbox is enabled in the DICOM module (in the module panel).</p>

---

## Post #7 by @fedorov (2018-12-05 22:28 UTC)

<p>Yes, indeed - it was checked. I don’t recall checking it though, and when it is checked, I would expect Slicer to shut it down on application exit. But in any case, the issue I had is resolved - no more automatic startup, and the popup is gone. Thank you!</p>

---

## Post #8 by @pieper (2018-12-06 01:36 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="4980">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I would expect Slicer to shut it down on application exit.</p>
</blockquote>
</aside>
<p>Yes, it is supposed to, at least it used to.</p>

---
