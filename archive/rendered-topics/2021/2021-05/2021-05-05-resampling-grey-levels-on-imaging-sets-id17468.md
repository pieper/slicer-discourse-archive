---
topic_id: 17468
title: "Resampling Grey Levels On Imaging Sets"
date: 2021-05-05
url: https://discourse.slicer.org/t/17468
---

# Resampling grey levels on imaging sets

**Topic ID**: 17468
**Date**: 2021-05-05
**URL**: https://discourse.slicer.org/t/resampling-grey-levels-on-imaging-sets/17468

---

## Post #1 by @mdpy (2021-05-05 12:29 UTC)

<p>I finally have sorted all my raw imaging and labels (only took 3 months of coding!). Since then, I’ve been running some feature extractions on approximately 200 image sets.</p>
<p>However after getting the basic’s running I thought it’d be best to read the literature to get a better idea of how best to approach feature extraction and selection.</p>
<p>One of the things I’ve already come across is how image sets might have different grey levels ranging typically from 32 to 256. Given my imaging set is spread across 5 years I suspect different image sets have different grey levels. I can’t see evidence that pyradiomics resamples imaging to same grey level.</p>
<p>What’s the best approach to resampling grey levels ?</p>
<p>Right now my data approach is</p>
<ol>
<li>Extract raw data from Eclipse (radiotherapy planning system) - images come out as DICOM</li>
<li>Image resampling using plastimatch and sitk  - images returned as nrrd</li>
<li>Feed resampled images into pyradiomics</li>
</ol>
<p>I suspect there is a sitk solution - but haven’t done a deep dive. Wanted to see what people did to normalize their image sets.</p>

---
