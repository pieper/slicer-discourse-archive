---
topic_id: 47715
title: "Slicer 5.12.3 plans and fixing the macOS stable extension packages"
date: 2026-07-22
url: https://discourse.slicer.org/t/47715
last_bumped: 2026-07-22T17:36:08.189Z
---

# Slicer 5.12.3 plans and fixing the macOS stable extension packages

**Topic ID**: 47715
**Date**: 2026-07-22
**URL**: https://discourse.slicer.org/t/slicer-5-12-3-plans-and-fixing-the-macos-stable-extension-packages/47715

---

## Post #1 by @ebrahim (2026-07-22 16:59 UTC)

<p>Yesterday we merged <a href="https://github.com/Slicer/Slicer/pull/9302">Slicer#9302</a> which worked out the cause of the issue with macOS C++ extension packages on Slicer 5.12, and which hopefully resolved  the issue.</p>
<p>Today there’s good evidence from the nightly packages that the issue is resolved:</p>
<ul>
<li>Yesterday’s MarkupsToModel: <a href="https://slicer-packages.kitware.com/#item/6a5fa0982eb3d967f03121e1" class="inline-onebox">SPKC</a> (see the large file size, indicating duplicated libraries)</li>
<li>Today’s: <a href="https://slicer-packages.kitware.com/#item/6a60ddab2eb3d967f0320816" class="inline-onebox">SPKC</a> (much smaller!)</li>
</ul>
<p>Time to cut Slicer 5.12.3? <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> ? Any other commits we should include besides <a href="https://github.com/Slicer/Slicer/commit/2c4c53aaa487c1bfde9237b12a92f6a8b60b61b9">2c4c53a</a>?</p>
<p>I am thinking this time I will keep the <code>pre_release</code> attribute as True until we test that the problem is really resolved on macOS, preventing anything from becoming available on the download page until we are ready.</p>

---

## Post #2 by @pieper (2026-07-22 17:36 UTC)

<p>Confirmed - MarkupsToModel and SlicerRT work for me on today’s mac build.  Yes for 5.12.3 <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
