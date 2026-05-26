---
topic_id: 41181
title: "Is there any way slicer can be used to generate synthetic data"
date: 2025-01-21
url: https://discourse.slicer.org/t/41181
last_bumped: 2026-02-25T15:27:52.053Z
---

# Is there any way slicer can be used to generate synthetic data

**Topic ID**: 41181
**Date**: 2025-01-21
**URL**: https://discourse.slicer.org/t/is-there-any-way-slicer-can-be-used-to-generate-synthetic-data/41181

---

## Post #1 by @maniron (2025-01-21 06:00 UTC)

<p>Hi,</p>
<p>I am trying to figure out is there a way that slicer could be used to generate synthetic data, I am trying to edit the medical images and generate a new one out of the edited one is there a way I could achieve this using slicer .<br>
Kindly help me out</p>

---

## Post #2 by @ciro.raggio (2025-01-24 06:21 UTC)

<p>The <a href="https://ciroraggio.github.io/SlicerImageAugmenter/tutorial" rel="noopener nofollow ugc">ImageAugmenter</a> extension can be helpful. It’s available in the Preview Release of 3D Slicer (currently v5.7.0).</p>

---

## Post #3 by @maniron (2025-01-24 07:30 UTC)

<p>but whether this extention can only be used with CT, cause I looking for Ultrasound data</p>

---

## Post #4 by @ciro.raggio (2025-01-24 12:35 UTC)

<p>It can be used with any kind of volume, not just CTs. In this case, I don’t know if it can be the best option, but you can try it.</p>

---

## Post #5 by @ciro.raggio (2026-02-25 15:27 UTC)

<p><a class="mention" href="/u/maniron">@maniron</a> You can now use the ModalityConverter extension to generate synthetic images using AI models! <a href="https://github.com/ciroraggio/SlicerModalityConverter" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ciroraggio/SlicerModalityConverter: SlicerModalityConverter is an open-source 3D Slicer extension designed for medical image-to-image (I2I) translation. The ModalityConverter module integrates multiple deep learning models trained for different kind of I2I translation, providing a user-friendly interface.</a></p>

---
