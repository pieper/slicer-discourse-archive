---
topic_id: 30925
title: "How Can I Do A Gamma Analysis Of The Areas With A Dose Great"
date: 2023-08-02
url: https://discourse.slicer.org/t/30925
---

# How can I do a gamma analysis of the areas with a dose greater than 200 in both film images

**Topic ID**: 30925
**Date**: 2023-08-02
**URL**: https://discourse.slicer.org/t/how-can-i-do-a-gamma-analysis-of-the-areas-with-a-dose-greater-than-200-in-both-film-images/30925

---

## Post #1 by @David_yan (2023-08-02 03:49 UTC)

<p>The film is irradiated with an accelerator to obtain a dose distribution. The low-dose area is not the focus of our analysis, and the gamma analysis of the entire film will affect the judgment. How can I perform gamma analysis only on regions greater than 200 dose values?</p>

---

## Post #2 by @David_yan (2023-08-11 13:38 UTC)

<p>The film is irradiated with an accelerator to obtain a dose distribution. The low-dose area is not the focus of our analysis, and the gamma analysis of the entire film will affect the judgment. How can I perform gamma analysis only on regions greater than 200 dose values?</p>

---

## Post #3 by @lassoan (2023-08-11 13:41 UTC)

<p>You can go to Segment Editor module, add a new segment, use Threshold effect to select region that has voxel value &gt; 200, then use this segmentation as input in the Dose comparison module.</p>

---
