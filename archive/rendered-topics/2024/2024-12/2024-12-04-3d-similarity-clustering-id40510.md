# 3D Similarity Clustering

**Topic ID**: 40510
**Date**: 2024-12-04
**URL**: https://discourse.slicer.org/t/3d-similarity-clustering/40510

---

## Post #1 by @robert-m-muench (2024-12-04 15:00 UTC)

<p>Hi, maybe 3D-slicer with some extensions is the right tool, but I don’t know. I’m searching for input, hints, guidance, or other solutions to the following problem.</p>
<p>I have several thousand (possibly a couple hundred thousand) STL files of manufacturing parts. So, the approach should be scalable.</p>
<p>I want to cluster these parts by geometric similarity. Since the STL files have different orientations and scalings, an invariant approach would most likely make sense.</p>
<p>The clustering should be controllable by making clusters with at least 30 parts or having some similarity measuring ranging from 0% (all parts form one cluster) to 100% (every part is its cluster).</p>
<p>Is 3D-Slicer the right tool for such a task?</p>

---

## Post #2 by @pieper (2024-12-04 15:05 UTC)

<aside class="quote no-group" data-username="robert-m-muench" data-post="1" data-topic="40510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/robert-m-muench/48/78732_2.png" class="avatar"> robert-m-muench:</div>
<blockquote>
<p>Is 3D-Slicer the right tool for such a task?</p>
</blockquote>
</aside>
<p>Not out of the box, no.  It may be a platform where you could visualize results though.</p>
<p>You may find that an approach like this is helpful: <a href="https://arxiv.org/abs/2205.15456" class="inline-onebox">[2205.15456] Registering Image Volumes using 3D SIFT and Discrete SP-Symmetry</a></p>

---

## Post #3 by @robert-m-muench (2024-12-04 18:43 UTC)

<p>I wouldn’t mind using 3D-Slicer as a toolbox, or code some scripts using it.</p>
<p>Thanks for the paper link. I’m unsure it fits what I want to do. Sounds pretty complicated.</p>

---
