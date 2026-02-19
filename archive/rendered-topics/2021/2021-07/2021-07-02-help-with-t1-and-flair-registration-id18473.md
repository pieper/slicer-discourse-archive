---
topic_id: 18473
title: "Help With T1 And Flair Registration"
date: 2021-07-02
url: https://discourse.slicer.org/t/18473
---

# Help with T1 and FLAIR registration

**Topic ID**: 18473
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/help-with-t1-and-flair-registration/18473

---

## Post #1 by @J1234 (2021-07-02 03:18 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 4.11.20210226</p>
<p>New 3D Slicer user here. I have a T1 and a FLAIR image that I need to align in space. I’ve conducted “Registration” → Resample Images (BRAINS) and “warped” the FLAIR, using the T1 as a reference image (since the T1 has the better resolution). Now both have the same image spacing and image origin under “Volumes”. However, the two still don’t appear perfectly aligned in space; my brain tumor segmentations based on one are slightly off for the other.</p>
<p>Are there other steps I can take to align the two that will allow both to keep the same image origin?</p>

---

## Post #2 by @lassoan (2021-07-02 05:08 UTC)

<p>I would recommend to try <a href="https://github.com/lassoan/SlicerElastix#slicerelastix">SlicerElastix</a> and <a href="https://github.com/simonoxen/SlicerANTs">SlicerANTs</a> extensions for registration. They typically works well with their default parameters, while BRAINS often requires extensive experimentation with registration parameters.</p>

---
