---
topic_id: 48329
title: "OsteotomyCuts: a new extension for multi-segment osteotomy planning (orthognathic and craniofacial)"
date: 2026-09-29
url: https://discourse.slicer.org/t/48329
last_bumped: 2026-09-29T02:44:08.000Z
---

# OsteotomyCuts: a new extension for multi-segment osteotomy planning (orthognathic and craniofacial)

**Topic ID**: 48329
**Date**: 2026-09-29
**URL**: https://discourse.slicer.org/t/osteotomycuts-a-new-extension-for-multi-segment-osteotomy-planning-orthognathic-and-craniofacial/48329

---

## Post #1 by @manjula (2026-09-29 02:23 UTC)

<p>Hi everyone,</p>
<p>I’d like to share a small extension I created with CluadeCode: <strong>OsteotomyCuts</strong>.</p>
<p>For years my biggest frustration with virtual planning in Slicer was cutting. Cuts were hard to predict, and complex osteotomies (a stepped Le Fort I, a BSSO, a chevron genioplasty) were difficult or impossible to make cleanly. So I tried to solve it for myself.</p>
<p>I’m not a software developer. I built this with <strong>Claude Code (Pro)</strong>, directing and testing every step myself, over about two days alongside clinical work. The actual development time with Claude Code was a few hours. Everything, from the code, tests and documentation to the logo, was produced with Claude Code or Claude under my direction and checked by me.</p>
<p><strong>What it does (Phase 1)</strong></p>
<ul>
<li>Draw an <strong>osteotomy line</strong> of any shape on the bone and set the <strong>saw direction</strong>. The bone is divided into <strong>closed, printable bone segments</strong>.</li>
<li><strong>Saw blade thickness</strong>, <strong>cut depth</strong> and <strong>cut reach</strong>, so a cut stops where you want it.</li>
<li><strong>Several osteotomy lines in one step</strong> (e.g. the horizontal and pterygomaxillary cuts of a Le Fort I). Le Fort I, II and III, BSSO, genioplasty and segmental cuts can all be built this way.</li>
<li><strong>Symmetrical cuts:</strong> mirror an osteotomy to the other side across a midline plane, or make a line symmetric.</li>
<li><strong>Structures to protect:</strong> add the nerve canal or tooth roots with a safe distance; the preview turns green, amber or red, and you’re warned before cutting.</li>
<li><strong>Model quality checks</strong>, and an optional <strong>“Create solid bone model”</strong>. You don’t normally need it, but it helps when a segmentation has holes or internal surfaces and a cut doesn’t behave.</li>
</ul>
<p>The multi-segment cuts, symmetrical cuts and safety-distance check are features I haven’t found in the planning tools I’ve used, so I hope they’re useful to others.</p>
<p>It’s research and planning software, <strong>not a medical device</strong>. There’s a clear disclaimer and a first-use terms dialog. It’s free and open source under GPL-3.0-or-later.</p>
<p><strong>What’s next</strong></p>
<p>This is Phase 1. Next I plan to add <strong>guided templates</strong> (Le Fort I, BSSO, genioplasty, segmental), followed by segment repositioning and other planning tools. The longer-term aim is a <strong>free, complete orthognathic planning workflow in Slicer</strong>, validated against commercial software, for colleagues who can’t afford high licence fees.</p>
<p><strong>Links</strong></p>
<ul>
<li>Repository: <a href="https://github.com/cmfsx/SlicerOsteotomyCuts" class="inline-onebox" rel="noopener nofollow ugc">GitHub - cmfsx/SlicerOsteotomyCuts: 3D Slicer extension for multi-segment osteotomy planning in orthognathic and craniofacial surgery · GitHub</a></li>
<li>DOI: [Zenodo DOI]</li>
<li>Quick Video: [<a href="https://youtu.be/yZYDwWlut5I" rel="noopener nofollow ugc">link or video</a>]</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bf05e500ba794e800f28d2096a46577ebef8bb8.jpeg" data-download-href="/uploads/short-url/aPMNqwXgHsTDX7vnpdlqIdbKu2A.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf05e500ba794e800f28d2096a46577ebef8bb8_2_690x347.jpeg" alt="2" data-base62-sha1="aPMNqwXgHsTDX7vnpdlqIdbKu2A" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf05e500ba794e800f28d2096a46577ebef8bb8_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf05e500ba794e800f28d2096a46577ebef8bb8_2_1035x520.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf05e500ba794e800f28d2096a46577ebef8bb8_2_1380x694.jpeg 2x" data-dominant-color="AB8B85"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1918×965 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29c3b6484ef67de343a326731c05315c68340baa.jpeg" data-download-href="/uploads/short-url/5XsT1aL78mlG6NLmI1x7iUcmbLc.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3b6484ef67de343a326731c05315c68340baa_2_690x353.jpeg" alt="1" data-base62-sha1="5XsT1aL78mlG6NLmI1x7iUcmbLc" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3b6484ef67de343a326731c05315c68340baa_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3b6484ef67de343a326731c05315c68340baa_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29c3b6484ef67de343a326731c05315c68340baa_2_1380x706.jpeg 2x" data-dominant-color="C2C4C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1914×980 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’d be very grateful if you’d try it and tell me what’s wrong: bugs, clinical logic, the interface, anything. Criticism is welcome. I’ve submitted it to the Extensions Index <a href="https://github.com/Slicer/ExtensionsIndex/pull/2403" rel="noopener nofollow ugc">[PR link]</a>; any help from the core developers in getting it there, or advice on doing things the Slicer way, would be much appreciated.</p>
<p>Thank you to the Slicer community for such a remarkable platform.</p>
<p>Manjula Herath</p>

---

## Post #2 by @Bhawana (2026-09-29 02:44 UTC)

<p><strong>Hi Manjula, I came across your OsteotomyCuts project and found it very interesting. I have around 5 years of experience in medical image annotation, particularly MRI annotation and segmentation. I would be interested in contributing to medical imaging/3D Slicer projects, especially annotation, segmentation, testing, or clinical data work. Please let me know if you have any paid project or collaboration opportunities where my experience could be useful. Thank you.</strong></p>

---
