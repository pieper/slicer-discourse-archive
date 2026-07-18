---
topic_id: 47660
title: "Slicer crashes on startup due to SlicerVMTK extension"
date: 2026-07-17
url: https://discourse.slicer.org/t/47660
last_bumped: 2026-07-17T21:06:16.230Z
---

# Slicer crashes on startup due to SlicerVMTK extension

**Topic ID**: 47660
**Date**: 2026-07-17
**URL**: https://discourse.slicer.org/t/slicer-crashes-on-startup-due-to-slicervmtk-extension/47660

---

## Post #1 by @aabrown100-git (2026-07-17 19:08 UTC)

<p><strong>Issue</strong>: On Slicer 5.12.2, Slicer crashes on startup after restarting Slicer following installation of <code>SlicerVMTK</code>. The startup log shows module loading failures in <code>SlicerVMTK</code> due to unresolved dylib dependencies, including <code>libdcmjp2kcs.20.dylib</code> looking for <code>libopenjp2.7.dylib</code> and <code>libssl.1.1.dylib</code> referencing a bad install name (<code>/D/S/A/OpenSSL/libcrypto.1.1.dylib</code>). The crash happens during module instantiation while Slicer is loading extensions.</p>
<p><strong>Specs</strong>: macOS Tahoe on 2026 MacBook Pro with M5 Pro chip</p>
<p><strong>Other</strong>: I also tried installing <code>SlicerVMTK</code> on Slicer 5.10.0 and did not encounter any issues.</p>

---

## Post #2 by @muratmaga (2026-07-17 19:20 UTC)

<p>This macos specific, and related to this bug being tracked: <a href="https://github.com/Slicer/Slicer/pull/9263" class="inline-onebox" rel="noopener nofollow ugc">COMP: Update DCMTKcs to fix OpenJPEG over-linking on macOS by lassoan · Pull Request #9263 · Slicer/Slicer · GitHub</a></p>
<p>Until that’s fixed and a new patch release is cut, your easiest option is to use windows or linux version.</p>

---

## Post #3 by @aabrown100-git (2026-07-17 19:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="47660">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>COMP: Update DCMTKcs to fix OpenJPEG over-linking on macOS by lassoan · Pull Request <span class="hashtag-raw">#9263</span> · Slicer/Slicer · GitHub</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> for the info. I see that PR is merged and I don’t see any linked issues. Is there other work to be done to fix this bug?</p>

---

## Post #4 by @muratmaga (2026-07-17 19:33 UTC)

<p>I do not know if there are any other work that needs to be done, but cutting a new release from scratch (like this) in itself takes a few days. Meanwhile I think the previews are fine (though I didn’t try it personnally).</p>

---

## Post #5 by @ebrahim (2026-07-17 21:06 UTC)

<p>The PR fixing the original issue is merged, but for some macOS-specific reason that I don’t yet understand there is a further problem that only applies to signed+notarized releases. The preview releases are unsigned, making them okay</p>

---
