---
topic_id: 24179
title: "Vesselness With No Contrast"
date: 2022-07-05
url: https://discourse.slicer.org/t/24179
---

# Vesselness with no contrast

**Topic ID**: 24179
**Date**: 2022-07-05
**URL**: https://discourse.slicer.org/t/vesselness-with-no-contrast/24179

---

## Post #1 by @KateDelb (2022-07-05 07:53 UTC)

<p>Dear,</p>
<p>I am currently using the vesselness filter to extract vessels from MRI images. However, this filter automatically assumes that the vessels are highlighted compared to the background, however my vessels are darker than the background.<br>
I’ve tried tuning the contrast parameter, but this doesnt help as the system still sees higher intensity structures as vessels. Is there a way to remedy this?</p>

---

## Post #2 by @mau_igna_06 (2022-07-05 12:02 UTC)

<p>I thimk you can invert the image using simplefilters module?</p>
<p>Hope it helps</p>

---
