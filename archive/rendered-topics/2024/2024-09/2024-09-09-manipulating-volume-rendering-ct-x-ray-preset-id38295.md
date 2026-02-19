---
topic_id: 38295
title: "Manipulating Volume Rendering Ct X Ray Preset"
date: 2024-09-09
url: https://discourse.slicer.org/t/38295
---

# Manipulating volume rendering CT-X-ray preset 

**Topic ID**: 38295
**Date**: 2024-09-09
**URL**: https://discourse.slicer.org/t/manipulating-volume-rendering-ct-x-ray-preset/38295

---

## Post #1 by @CraigB (2024-09-09 18:08 UTC)

<p>Hello,</p>
<p>I’m new to 3D slicer (and loving it so far), so I apologize if this is a basic question or if what I am trying to do is not feasible. I have a thoracic CT that I’ve uploaded and created segmentations on so that all of the thoracic anatomy is color-coded and can be selected and unselected. My goal with the model is to use it as an interactive means to teach veterinary students canine thoracic radiography more effectively. How I’m going about this is to display the 3D volume rendering using the CT-X-ray preset, which displays a thick slab reconstruction to essentially mimic a radiograph using CT data, thereby allowing me to highlight relevant anatomy using the CT info, but display it as a radiograph for teaching. My issue is that the preset seems to lean a little bit towards being a maximal intensity slab reconstruction (MIP) rather than an average intensity slab reconstruction (which would more accurately reflect a radiograph). As such, the bones stand out really starkly and the lungs and soft tissues are harder to see. I’ve tried adjusting the ‘shift’ slider bar in the volume rendering tab under ‘display’ beneath the CT-X-ray preset, but it seems to mostly just be adjusting the window level. Is there a way to manipulate the preset to make it more like an average intensity slab reconstruction or would that require designing a new preset (which I think is probably way beyond my current skill set)?</p>
<p>I appreciate your help, thank you!</p>
<p>All the best,<br>
Craig</p>

---

## Post #2 by @pieper (2024-09-11 18:46 UTC)

<p>Be sure to review the documentation about what controls are available.  You can edit the transfer functions and get a wide variety of effects.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html</a></p>
<p>If you aren’t able to find something that works for you why don’t you post image examples of what you want to achieve and screenshots of what you have so far and probably someone can give you some ideas.  Ideally use slicer example data so anyone can reproduce or share data if there’s something special about your use case.</p>

---
