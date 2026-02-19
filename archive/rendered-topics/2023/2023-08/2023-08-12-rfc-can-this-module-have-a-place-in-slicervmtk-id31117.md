---
topic_id: 31117
title: "Rfc Can This Module Have A Place In Slicervmtk"
date: 2023-08-12
url: https://discourse.slicer.org/t/31117
---

# RFC : can this module have a place in SlicerVMTK?

**Topic ID**: 31117
**Date**: 2023-08-12
**URL**: https://discourse.slicer.org/t/rfc-can-this-module-have-a-place-in-slicervmtk/31117

---

## Post #1 by @chir.set (2023-08-12 17:20 UTC)

<p>Hi all,</p>
<p>I’m wondering if this module, <a href="https://github.com/chir-set/Tools7/tree/master/ArterialCalcificationPreProcessor/" rel="noopener nofollow ugc">Arterial calcification pre-processor</a>, may be <em>moved</em> to SlicerVMTK.</p>
<p>It grows an input diseased arterial lumen segment to isolate dense calcifications in the wall within a calculated intensity range and a specified margin.</p>
<p>From the surgical perspective, it <em>is</em> very satisfactory, giving a focused feeling of what we’ll be dealing with.</p>
<p>From the technical perspective, it may be considered as a deviation from the ‘Vascular modeling’ paradigm, since it does segment nor describe a vascular tree. Additionally, this module does not use the VMTK libraries, but rather the ‘Segment editor’.</p>
<p>It has some limitations well described on the homepage, reasons for which it is termed as a ‘pre-processor’.</p>
<p>Thank you for any input.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @pieper (2023-08-12 17:45 UTC)

<p>Maybe other interested parties can chime in, but I’m generally in favor of extensions having broader sets of generally related features rather than having just one or two modules.  This makes things easier to manage IMO.  So that would be a yes to your idea <a class="mention" href="/u/chir.set">@chir.set</a> .</p>

---

## Post #3 by @chir.set (2023-08-13 15:22 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="31117">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>So that would be a yes</p>
</blockquote>
</aside>
<p>The module is merged in <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/94" rel="noopener nofollow ugc">#94</a>.</p>
<p>Thank you for your support <a class="mention" href="/u/pieper">@pieper</a>.</p>

---
