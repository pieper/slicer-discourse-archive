---
topic_id: 19279
title: "Crop Sequence Nodes"
date: 2021-08-19
url: https://discourse.slicer.org/t/19279
---

# Crop Sequence Nodes

**Topic ID**: 19279
**Date**: 2021-08-19
**URL**: https://discourse.slicer.org/t/crop-sequence-nodes/19279

---

## Post #1 by @tom.birdsong (2021-08-19 20:35 UTC)

<p>Hi there,</p>
<p>I am trying to decrease the size of an example ultrasound sequence dataset and am wondering if there is a way to crop along the time axis with the Sequences module. “Crop volume sequences” seems to be effective at making spatial adjustments but does not reduce the length of the data set in time.</p>
<p>I’ve discussed with <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> and it sounds like copying a reduced number of sequence nodes into a new sequence is certainly something we can script, but wanted to check if there is support for this in existing tools first.</p>
<p>Is cropping 4D data along the temporal axis currently supported? Thank you!</p>

---

## Post #2 by @lassoan (2021-08-20 18:14 UTC)

<p>There is no such module, but it would not be hard at all to implement it. It would be great if you could work on it. A small Python scripted module would do. We can help you to get started and whenever you get stuck with anything.</p>

---

## Post #3 by @tom.birdsong (2021-08-20 18:46 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I’ll give it a shot. Is the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Developing_and_contributing_extensions_for_3D_Slicer" rel="noopener nofollow ugc">extension tutorial</a> the best place to start?</p>

---

## Post #4 by @lassoan (2021-08-20 18:53 UTC)

<p>I would recommend the “PerkLab’s Slicer bootcamp training materials” on that page.</p>

---
