---
topic_id: 1036
title: "Averaging Label Maps"
date: 2017-09-11
url: https://discourse.slicer.org/t/1036
---

# Averaging label maps

**Topic ID**: 1036
**Date**: 2017-09-11
**URL**: https://discourse.slicer.org/t/averaging-label-maps/1036

---

## Post #1 by @Maya_Harary (2017-09-11 13:32 UTC)

<p>Operating system: OS<br>
Slicer version: 4.6.2 r25516</p>
<p>Hello<br>
I am doing volumetric segmentation of lesions in a series of patients (N=7). I have segmented each lesion into 3 regions of interest (which are arranged concentrically around each other) in each patient. I am interested in averaging these labels across the series in order to create an averaged representation of the volume and arrangement of these regions across the population.</p>
<p>Is there any way to do this? I would imagine I would have to define fiducials for each label map. Then import each of the label maps into a new scene and then register them to one another. Once/if I can do that, is there a way to create and averaged label map taking all these volumes into account?</p>
<p>Thanks!<br>
Maya</p>

---

## Post #2 by @lassoan (2017-09-11 13:53 UTC)

<p>You can compute distance map )Simple Filters module, SignedMaurerDistanceMapImageFilterÖ, average the distance maps, and threshold the result.</p>

---
