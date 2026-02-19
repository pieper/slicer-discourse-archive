---
topic_id: 40989
title: "Global Fw Fa Inquiry Whitematteranalysis"
date: 2025-01-08
url: https://discourse.slicer.org/t/40989
---

# 'Global' FW/FA Inquiry - whitematteranalysis

**Topic ID**: 40989
**Date**: 2025-01-08
**URL**: https://discourse.slicer.org/t/global-fw-fa-inquiry-whitematteranalysis/40989

---

## Post #1 by @kvandeloo (2025-01-08 01:28 UTC)

<p>I’m using whitematteranalysis for whole-brain tractography analysis (<a href="https://whitematteranalysis.readthedocs.io/en/latest/subject-specific-tractography-parcellation.html#" class="inline-onebox" rel="noopener nofollow ugc">Tutorial - whitematteranalysis 0.4.0 documentation</a>). Using this tutorial, I’m able to derive FA and FW from anatomical tracts and/or 800 fibre clusters as per the ORG white matter atlas. I’m interested in deriving ‘whole-brain’ or ‘global’ FW/FA - is it adequate to sum FA/FW values across the 800 clusters for each subject, or is there a better way to do this?</p>

---

## Post #2 by @ljod (2025-05-20 15:56 UTC)

<p>Apologies for the slow response. We have a script to correctly average values across fiber clusters taking into account the number of points within each fiber cluster. Its code is located here: <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/bin/wm_average_tract_measures.py" class="inline-onebox" rel="noopener nofollow ugc">whitematteranalysis/bin/wm_average_tract_measures.py at master · SlicerDMRI/whitematteranalysis · GitHub</a></p>

---
