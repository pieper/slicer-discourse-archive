---
topic_id: 22454
title: "Why Are My Semi Landmarks Not Uniformly Distributed"
date: 2022-03-11
url: https://discourse.slicer.org/t/22454
---

# Why are my semi-landmarks not uniformly distributed?

**Topic ID**: 22454
**Date**: 2022-03-11
**URL**: https://discourse.slicer.org/t/why-are-my-semi-landmarks-not-uniformly-distributed/22454

---

## Post #1 by @yyl (2022-03-11 14:16 UTC)

<p>version 4.11<br>
i use the creatsemiLMpatches to generate semi-landmarks,Is there any way to make the semi-landmarks distribution on the surface more uniform?<br>
thank you very much!!!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bc037bf4c0d99d309b0b58e7afb853efae15cbf.jpeg" alt="image" data-base62-sha1="fncUFoGiLtaOqBKfqrs25JZ47uf" width="534" height="426"></p>

---

## Post #2 by @smrolfe (2022-03-14 19:36 UTC)

<p>The semi-landmark patches work best when the underlying surface can be modeled well by a triangular patch. Areas of high curvature are going to create challenges for sampling regularity, like what you are seeing here. We’re currently working on an update to this module that will allow interactive adjustment of the patches.</p>
<p>If you don’t need to constrain your point positions with manual landmarks, you could try the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/PseudoLMGenerator" rel="noopener nofollow ugc">Pseudo-landmark Generator</a> in the SlicerMorph extension as an alternative.</p>

---

## Post #3 by @yyl (2022-03-15 00:06 UTC)

<p>I want to limit the semi-landmarks to the zygomatic arch so maybe PseudoLMGenerator doesn’t work for me, right?</p>

---

## Post #4 by @smrolfe (2022-03-15 16:50 UTC)

<p>You can still use the PseudoLMGenerator by either cropping the template to just this region before generating the points, or by generating pseudo-landmarks for the whole template and editing the landmark set with the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/MarkupEditor" rel="noopener nofollow ugc">MarkupEditor</a>.</p>
<p>These pseudo-landmarks will not have a relationship to the manual landmarks, but once you’ve generated a set on the template image, you can transfer them to each individual image to enforce geometric homology (details in this <a href="https://doi.org/10.1002/ajpa.24214" rel="noopener nofollow ugc">paper</a>).</p>

---

## Post #5 by @yyl (2022-03-16 00:00 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="4" data-topic="22454" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>You can still use the PseudoLMGenerator by either cropping the template to just this region before generating the points, or by generating pseudo-landmarks for the whole template and editing the landmark set with the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/MarkupEditor" rel="noopener nofollow ugc">MarkupEditor</a>.</p>
<p>These pseudo-landmarks will not have a relationship to the manual landmarks, but once you’ve generated a set on the template image, you can transfer them to each individual image to enforce geometric homology (details in this <a href="https://doi.org/10.1002/ajpa.24214" rel="noopener nofollow ugc">paper </a>).</p>
</blockquote>
</aside>
<p>THANKS!!!Very happy to hear this, because I set the landmarks on the zygomatic arch, then  I should transfer the surface semi-landmarks I set to the next model surface through transfersemiLM , right?</p>

---

## Post #6 by @smrolfe (2022-03-16 18:45 UTC)

<p>If you have existing manual landmarks on each model you can use the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM" rel="noopener nofollow ugc">ProjectSemiLM</a> module to transfer the points, otherwise you can use <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ALPACA" rel="noopener nofollow ugc">ALPACA</a>.</p>

---
