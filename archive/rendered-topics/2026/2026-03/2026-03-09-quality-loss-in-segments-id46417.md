---
topic_id: 46417
title: "Quality Loss In Segments"
date: 2026-03-09
url: https://discourse.slicer.org/t/46417
---

# Quality loss in segments 

**Topic ID**: 46417
**Date**: 2026-03-09
**URL**: https://discourse.slicer.org/t/quality-loss-in-segments/46417

---

## Post #1 by @Skulleditor (2026-03-09 20:12 UTC)

<p>Hello everyone,</p>
<p>I am working with a micro-CT dataset of a snake skull in <strong>3D Slicer (v5.8)</strong> and I am experiencing some difficulty with the segmentation workflow.</p>
<p>When I visualize the dataset using <strong>Volume Rendering</strong>, the skull appears very detailed and the surface structures (such as teeth and thin bones) look sharp. However, when I create a segmentation using <strong>Segment Editor → Threshold</strong>, the resulting segment already seems to lose some surface detail. The 3D model generated from the segment appears slightly smoother and less detailed compared to the original volume rendering.</p>
<p>This loss of detail seems to occur <strong>during the creation of the segment itself</strong>, rather than during later steps like removing artifacts.</p>
<p>My goal is to:</p>
<ul>
<li>
<p>isolate the skull from the CT volume</p>
</li>
<li>
<p>remove small floating artifacts around it</p>
</li>
<li>
<p>preserve as much surface detail as possible in the final 3D model</p>
</li>
</ul>
<p>I would like to know if there is a recommended workflow or settings in Slicer to <strong>preserve higher surface resolution when creating a segmentation</strong>.</p>
<p>Thank you very much!</p>

---

## Post #2 by @pieper (2026-03-09 20:18 UTC)

<p>A good way to do this is to increase the resolution of the segmentation with respect to the source data (change this with the segmentation geometry dialog).</p>
<p>If you paste your question and this answer into google you’ll no doubt get more details from the AI.</p>

---

## Post #3 by @Skulleditor (2026-03-09 20:37 UTC)

<p>It worked here, thank you very much! I was having trouble finding this information, as I’m learning to use the software on my own. I really appreciate your help.</p>

---

## Post #4 by @muratmaga (2026-03-10 02:36 UTC)

<aside class="quote no-group" data-username="Skulleditor" data-post="3" data-topic="46417">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/skulleditor/48/82063_2.png" class="avatar"> Skulleditor:</div>
<blockquote>
<p>as I’m learning to use the software on my own.</p>
</blockquote>
</aside>
<p>Given that you are  working with microCT you’ll probably benefit from reviewing our SlicerMorph Tutorials <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials · GitHub</a></p>

---
