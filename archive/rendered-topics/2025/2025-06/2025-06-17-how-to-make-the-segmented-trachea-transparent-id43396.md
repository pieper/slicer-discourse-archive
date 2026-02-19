---
topic_id: 43396
title: "How To Make The Segmented Trachea Transparent"
date: 2025-06-17
url: https://discourse.slicer.org/t/43396
---

# How to make the segmented trachea transparent

**Topic ID**: 43396
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/how-to-make-the-segmented-trachea-transparent/43396

---

## Post #1 by @linyao (2025-06-17 16:53 UTC)

<p>Hello all. I am a radiologist and have found 3DSlicer to be incredibly useful.</p>
<p>For my research I have the chest CT data where there is  a foreign body with soft tissue intensity in the trachea. I hope to present the foreign body with the trachea in 3D. I used segment editor tool and add two VOIs, one for the foreign body and another for the trachea, I click “show 3D”. but find the foreign body  is not visible due to the shelter of the trachea.<br>
how can I make the trachea transparent to better show the foreign body in the trachea in 3D?</p>
<p>Thank you very much.</p>

---

## Post #2 by @muratmaga (2025-06-17 16:56 UTC)

<p>You can control the opacity of individual segments through the Segmentations module.</p>

---

## Post #3 by @pieper (2025-06-17 17:05 UTC)

<p><a class="mention" href="/u/linyao">@linyao</a> You may also want to experiment with the <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">ColorizeVolume module</a> in the Sandbox extension.  It allows you to use your segmentations to control the volume rendering of the CT data in various ways.</p>

---
