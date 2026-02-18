# Compounded Markup for osteotomy

**Topic ID**: 44607
**Date**: 2025-09-27
**URL**: https://discourse.slicer.org/t/compounded-markup-for-osteotomy/44607

---

## Post #1 by @Hans_Peter (2025-09-27 13:06 UTC)

<p>I want to perform a repeatable osteotomy with a certain shape using Slicer. Essentially I need a modified plane Markup, where the section crossing the bone is not simply horizontal, but for ex. a Z-shape pattern. As I am not a programmer in any way, I sought to consult the community here first for help. Is there an extension that allows for the construction of more complex markups? Or is an all new, custom markup required for this? Thanks in advance</p>

---

## Post #2 by @pieper (2025-09-27 13:27 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> might be able to give some advice here.  Have a look at his <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">extension</a>.</p>

---

## Post #3 by @mau_igna_06 (2025-09-27 15:12 UTC)

<blockquote>
<p>Z-shape pattern</p>
</blockquote>
<p>You can achieve that using the <code>ModelClip</code> module of the <code>ModelClip</code> extension, see use case below:</p><div class="youtube-onebox lazy-video-container" data-video-id="4I-9qnmvCLY" data-video-title="Digital Orthognathic Planning with Free &amp; Open-Source 3D Slicer" data-video-start-time="740" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=4I-9qnmvCLY&amp;t=740" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/4I-9qnmvCLY/maxresdefault.jpg" title="Digital Orthognathic Planning with Free &amp; Open-Source 3D Slicer" width="690" height="388">
  </a>
</div>

<p>I’m interested in developing such new markup, with n neighboring planes that share a side, but it is not on the top of my priority list currently</p>
<p>Thanks for the tag Steve <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
