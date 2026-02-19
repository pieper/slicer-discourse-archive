---
topic_id: 36280
title: "Deep Learning Model For Segmenting Many Of Same Things"
date: 2024-05-20
url: https://discourse.slicer.org/t/36280
---

# Deep learning model for segmenting many of same things

**Topic ID**: 36280
**Date**: 2024-05-20
**URL**: https://discourse.slicer.org/t/deep-learning-model-for-segmenting-many-of-same-things/36280

---

## Post #1 by @muratmaga (2024-05-20 15:57 UTC)

<p>This is not really Slicer related, but maybe relevant in context of upcoming PW.</p>
<p>Is anyone aware of a DL architecture that can be used to train and segment things that look similar, but doesn’t necessarily have a fixed count. Biological examples would be vertebra in fishes or snakes, tooth in alligators, crocodyles, salamanders, scales in lizards and many other animals, cell nuclei etc…</p>
<p>The idea would be the user would only label a few of those those in a given dataset, and the model would extract all of them, regardless of how many there are.</p>
<p>I don’t think current implementations of UNet would work, since you have to designate all the classes beforehand.</p>

---

## Post #2 by @pieper (2024-05-20 16:40 UTC)

<p>Have you tried the <a href="https://github.com/mazurowski-lab/SlicerSegmentWithSAM">Segment Anything Models?  They take</a>.  Seems like they would be well suited to this if you are able to provide some input about which structure you want.</p>

---

## Post #3 by @mau_igna_06 (2024-05-20 17:18 UTC)

<p>It would be nice to have an AI that can segment all bones in a CT as separated structures on a single segment (this would need to ignore cartilage I guess). Then using islands effect you could separate them easily <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @muratmaga (2024-05-20 19:03 UTC)

<p>I tried sometime ago, but didn’t manage to get it working (neither as extension nor as GH).</p>

---

## Post #5 by @pieper (2024-05-20 19:13 UTC)

<p>Agreed, there’s more work to be done but SAM seems like a good approach for what you asked.</p>

---
