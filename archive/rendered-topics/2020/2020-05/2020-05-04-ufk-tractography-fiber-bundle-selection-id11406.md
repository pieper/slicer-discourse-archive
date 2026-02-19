---
topic_id: 11406
title: "Ufk Tractography Fiber Bundle Selection"
date: 2020-05-04
url: https://discourse.slicer.org/t/11406
---

# UFK Tractography - Fiber Bundle Selection

**Topic ID**: 11406
**Date**: 2020-05-04
**URL**: https://discourse.slicer.org/t/ufk-tractography-fiber-bundle-selection/11406

---

## Post #1 by @flavceschi (2020-05-04 18:44 UTC)

<p>Hello,<br>
I have to extract several fiber bundles by Multiple-Manual ROI Labeling.</p>
<p>What I am doing after having converted the DICOMs into NRRD is to</p>
<ol>
<li>create a brain mask</li>
<li>create a whole-brain UKF tractography using as input label map the brain mask</li>
<li>in the editor module I draw with different colors my ROIs.</li>
<li>under - UKF Tract - Tract ROI Selection I use as label map the one created in the editor module (step 3), and I use the whole brain tractography created at step 2 as input fiber bundle. I then indicate the inclusion labels separated by a comma</li>
</ol>
<p>The output gives me again the whole brain fibers and not only the tracts I drew in step 3. Is it because I should add exclusion labels?</p>
<p>(I instead get the tracts I want to extract correctly if I do the same process by creating a whole-brain-tractography from the Tract Seeding module and then do the same step in UKF ROI selection. But I would like to start from the UFK whole brain to have a two-tensor).</p>
<p>Thank you in advance for the help<br>
F</p>

---
