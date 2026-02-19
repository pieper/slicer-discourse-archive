---
topic_id: 26037
title: "Incorporate Gmsh In 3D Slicer"
date: 2022-11-02
url: https://discourse.slicer.org/t/26037
---

# Incorporate Gmsh in 3d Slicer

**Topic ID**: 26037
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/incorporate-gmsh-in-3d-slicer/26037

---

## Post #1 by @ZSoltani (2022-11-02 14:27 UTC)

<p>Dear 3D Slicer community,</p>
<p>Is it possible to incorporate Gmsh in 3D Slicer?</p>
<p>Thank you in advance for your help,<br>
Zahra</p>

---

## Post #2 by @muratmaga (2022-11-03 03:57 UTC)

<aside class="quote no-group" data-username="ZSoltani" data-post="1" data-topic="26037">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zsoltani/48/17166_2.png" class="avatar"> ZSoltani:</div>
<blockquote>
<p>Gmsh</p>
</blockquote>
</aside>
<p>While it might be possible, it is unlikely that you will find anyone helping you due to the incompatible licensing (looks like GMSH is using GPL). In general there is a reluctance of supporting libraries released under GPL.  See the answer in this thread. <a href="https://discourse.slicer.org/t/incorporate-cgal-in-3d-slicer/25963/2" class="inline-onebox">Incorporate CGAL in 3D Slicer - #2 by lassoan</a></p>

---

## Post #3 by @lassoan (2022-11-03 12:00 UTC)

<p>Yes, we are avoiding investing time into supporting GPL code and instead try to make things work with restriction-free alternatives.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> has been considering adding  <a href="https://github.com/wildmeshing/fTetWild">fTetWild</a> as an additional mesher for SegmentMesher extension. Could you try fTetWild to see if it fulfills your needs?</p>

---

## Post #4 by @ZSoltani (2022-11-03 14:54 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for your replies.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I wasn’t aware of fTetWild. We will try it to see how results will be in comparison with TetGen in SegmentMesher.</p>

---
