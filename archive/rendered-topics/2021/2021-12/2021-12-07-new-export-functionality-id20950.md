---
topic_id: 20950
title: "New Export Functionality"
date: 2021-12-07
url: https://discourse.slicer.org/t/20950
---

# New export functionality

**Topic ID**: 20950
**Date**: 2021-12-07
**URL**: https://discourse.slicer.org/t/new-export-functionality/20950

---

## Post #1 by @ebrahim (2021-12-07 15:16 UTC)

<p>Thanks to the feedback and guidance of <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, and <a class="mention" href="/u/jcfr">@jcfr</a>. I am pleased to announce that export functionality is now available in the latest Slicer preview release. Right click on a node in the data module to see a new context menu item that allows you to quickly export an individual node.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f58fe42319d7b109d6f132b5575998d10d9d44f.png" data-download-href="/uploads/short-url/4tjt3pIJAvRyxz0GFIIIwbb1xiD.png?dl=1" title="export04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f58fe42319d7b109d6f132b5575998d10d9d44f_2_690x414.png" alt="export04" data-base62-sha1="4tjt3pIJAvRyxz0GFIIIwbb1xiD" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f58fe42319d7b109d6f132b5575998d10d9d44f_2_690x414.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f58fe42319d7b109d6f132b5575998d10d9d44f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f58fe42319d7b109d6f132b5575998d10d9d44f.png 2x" data-dominant-color="C7CAD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">export04</span><span class="informations">953×573 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Exporting should not interfere with saving. For example, exporting a node that was modified since the last scene save does not prevent that node from being included by default during the next scene save.</p>
<p>Exporting a node with a transform provides the option of applying the transform in the exported file.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d3e25c2c3be1738d815f889875f3c6c5995e67c.png" alt="export03" data-base62-sha1="fApc4o9kHJ3nCmCTtIhaQ5Sj60Y" width="335" height="170"></p>
<p>Simultaneous export of multiple nodes is not yet supported.</p>
<p>Comments, questions, and suggestions are welcome.</p>

---

## Post #2 by @muratmaga (2021-12-07 17:13 UTC)

<aside class="quote no-group" data-username="ebrahim" data-post="1" data-topic="20950">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>Simultaneous export of multiple nodes is not yet supported.</p>
</blockquote>
</aside>
<p>This is great. Does is allow export of multiple files of the same type? Like if I create folder within data and have three volumes nested within, will it allow to export all of them to the specified folder?</p>

---

## Post #3 by @ebrahim (2021-12-07 17:16 UTC)

<blockquote>
<p>Does is allow export of multiple files of the same type?</p>
</blockquote>
<p>No, not yet. This is the next aspect I’ll be looking into.</p>

---

## Post #4 by @muratmaga (2021-12-07 17:18 UTC)

<p>Let us know when you do that, and we will remove the ExportAs from SlicerMorph going forward (I think that’s the only feature currently not covered).</p>

---

## Post #5 by @ebrahim (2022-01-28 14:59 UTC)

<p>Update: <a href="https://discourse.slicer.org/t/multiple-node-export-now-supported/21681" class="inline-onebox">Multiple node export now supported</a></p>

---
