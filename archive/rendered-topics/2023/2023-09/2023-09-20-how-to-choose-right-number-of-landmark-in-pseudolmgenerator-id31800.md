---
topic_id: 31800
title: "How To Choose Right Number Of Landmark In Pseudolmgenerator"
date: 2023-09-20
url: https://discourse.slicer.org/t/31800
---

# How to choose right number of landmark in PseudoLMGenerator?

**Topic ID**: 31800
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/how-to-choose-right-number-of-landmark-in-pseudolmgenerator/31800

---

## Post #1 by @zariliusra (2023-09-20 10:42 UTC)

<p>Does lower tolerance spacing and having more landmarks make it easier to get a statistical shape model?</p>

---

## Post #2 by @muratmaga (2023-09-20 15:19 UTC)

<p>That’s not an easy question to answer. Some papers suggest more dense sampling of the geometry does help. But then some statistical procedures become computationally unfeasible if you are using thousands of points.</p>
<p>For mammal skulls we typically shoot for low few hundreds. For me it is far more important how regularized and smooth the points are then the absolute number of points.</p>

---

## Post #3 by @zariliusra (2023-09-21 08:11 UTC)

<p>Thank you very much, doc. Are there any papers that give information about how to make the landmarks smooth and regular? Please give some advice on how to set good landmarks.</p>

---

## Post #4 by @muratmaga (2023-09-21 16:06 UTC)

<aside class="quote no-group" data-username="zariliusra" data-post="3" data-topic="31800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zariliusra/48/66436_2.png" class="avatar"> zariliusra:</div>
<blockquote>
<p>bout how to make the landmarks smooth and regular</p>
</blockquote>
</aside>
<p>I am not aware of any papers specifically on that. That’s usually a function of how the the underlying 3D model is derived, whether the vertices are roughly equally distributed on the model etc… If you run one of your models with PseudoLMGenerator and choose the “model geometry” option, you can quickly see what the point distribution looks like and whether you need to smoothing and edit your model more (or not).</p>

---

## Post #5 by @zariliusra (2023-09-23 08:52 UTC)

<p>Thank you very much for your kindness Professor Murat Maga</p>

---
