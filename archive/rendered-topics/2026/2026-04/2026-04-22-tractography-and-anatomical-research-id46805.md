---
topic_id: 46805
title: "Tractography and anatomical research"
date: 2026-04-22
url: https://discourse.slicer.org/t/46805
last_bumped: 2026-04-27T09:27:46.000Z
---

# Tractography and anatomical research

**Topic ID**: 46805
**Date**: 2026-04-22
**URL**: https://discourse.slicer.org/t/tractography-and-anatomical-research/46805

---

## Post #1 by @philippepellerin (2026-04-22 10:19 UTC)

<p>Hi, I wonder whether the algorithms used for tractography could be helpful to follow the path of muscle fibres through serial histologic sections</p>

---

## Post #2 by @ebrahim (2026-04-24 01:24 UTC)

<p>Tractography algorithms build up from local directional information (such a diffusion tensor or a fiber orientation distribution) to generate curves. They wouldn’t apply directly to a completely different modality; histological images wouldn’t naturally come with local directional information unless you do something to get that information out of the image intensities.</p>
<p>Some of the ideas in tractography certainly apply! I don’t know how muscle fibers look in histological sections, but if it is natural to preprocess the images such that you end up with local direcitonal information (possibly with probabilities) then it could be reasonable to transfer some ideas from dmri tractography to the task of reconstructing curves out of that representation.</p>

---

## Post #3 by @pieper (2026-04-24 13:07 UTC)

<p><a class="mention" href="/u/philippepellerin">@philippepellerin</a> I think your idea makes sense if the image support it.  I common problem is that histology sections have much more resolution in-plane and less out of plane.  Also the process of cutting and mounting the tissue often leads to misregistration across slices.  Still, if the data supports it, something like a <a href="https://en.wikipedia.org/wiki/Structure_tensor">structure tensor</a> could be used for streamline tracing.</p>

---

## Post #4 by @philippepellerin (2026-04-27 09:27 UTC)

<p>Thanks for your advice. The purpose of my research would be to follow the paths of the fibers of the facial muscles in the set of pictures from the visible Korean project. I can have an idea of the general direction of the path of some bundles on a short distance, but it is very difficult to give a representation as segment. I take that I could do some preprocessing to get some clue about local directional information, but I do not know how to do that, thereafter what I should do to exploit the data.<br>
Thanks for your advice. Best.</p>

---
