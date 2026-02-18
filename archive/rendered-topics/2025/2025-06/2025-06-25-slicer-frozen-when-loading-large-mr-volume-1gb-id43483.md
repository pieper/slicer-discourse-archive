# Slicer frozen when loading large MR volume (>1GB)

**Topic ID**: 43483
**Date**: 2025-06-25
**URL**: https://discourse.slicer.org/t/slicer-frozen-when-loading-large-mr-volume-1gb/43483

---

## Post #1 by @joved81744 (2025-06-25 13:17 UTC)

<p>Hey guys… <img src="https://emoji.discourse-cdn.com/twitter/waving_hand.png?v=14" title=":waving_hand:" class="emoji" alt=":waving_hand:" loading="lazy" width="20" height="20"></p>
<p>Slicer (v5.2.2) crashes or freezes when I load a large MR volume (1.2 GB NIfTI). The progress bar gets stuck at ~30 %, and no console errors appear. Restarting works, but fails again on the same file.</p>
<p>Things I have tried:</p>
<ul>
<li>Converted NIfTI to compressed (.nii.gz) – same issue</li>
<li>Increased “–max-memory” via command line</li>
<li>Tested on two different workstations (16 GB, 32 GB RAM)</li>
</ul>
<p>I also joined <a href="https://www.igmguru.com/digital-marketing-programming/flutter-training-in-chennai" rel="noopener nofollow ugc">flutter training in chennai</a> Has anyone faced this? Any suggestions on config flags, debug logs, or memory settings I’m missing?</p>
<p>Thanks in advance… <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=14" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @muratmaga (2025-06-25 16:23 UTC)

<aside class="quote no-group" data-username="joved81744" data-post="1" data-topic="43483">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ce7236/48.png" class="avatar"> joved81744:</div>
<blockquote>
<p>Slicer (v5.2.2) crashes o</p>
</blockquote>
</aside>
<p>Please try with the latest stable (5.8.1) or the preview version first, and then report. 5.2.2 is few years old, not developed anymore.</p>

---
