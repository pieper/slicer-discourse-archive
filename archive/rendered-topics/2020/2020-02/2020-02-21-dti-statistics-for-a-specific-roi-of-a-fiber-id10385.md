---
topic_id: 10385
title: "Dti Statistics For A Specific Roi Of A Fiber"
date: 2020-02-21
url: https://discourse.slicer.org/t/10385
---

# DTI Statistics for a specific ROI of a fiber?

**Topic ID**: 10385
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/dti-statistics-for-a-specific-roi-of-a-fiber/10385

---

## Post #1 by @LearningSlicerYay (2020-02-21 16:49 UTC)

<p>Hi all,</p>
<p>I generated my fiber tracts using interactive markup.<br>
I would like to generate statistics based on a specific region of these tracts. Is there a way I can do this?</p>
<p>Many thanks,</p>

---

## Post #2 by @zhangfanmark (2020-02-21 17:40 UTC)

<p>Hi,</p>
<p>Currently, we support only calculation of summary statistics of the whole fiber tract, e.g., the mean and the maximum FA of all points along the fiber tract.</p>
<p>Computing the statistics of a region of interest will need some coding work. For example, reading the tract in Python, then locating the fiber points of interest to calculate the statistics.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @LearningSlicerYay (2020-02-21 17:58 UTC)

<p>Thanks for your response Fan.</p>
<p>When it’s calculating the statistics, if I have both a negative ROI node on a tract does it take that into account? I’m not sure how the nodes are incorporated into the VTKs…</p>

---

## Post #4 by @zhangfanmark (2020-02-21 18:19 UTC)

<p>Hi,</p>
<p>The tractography statistics module will compute the diffusion parameters stored along the fiber tract. No ROI node will be taken into account. If you want to exclude fibers, you can update the fiber tracts first using negative ROI node. Then run the tractography statistics module. Still, this will calculate the statistics along the whole fiber tract.</p>
<p>Regards,<br>
Fan</p>

---

## Post #5 by @emma1201 (2022-03-28 08:35 UTC)

<p>Hi Fan and slicer fans,</p>
<p>Apologies for replying to an old thread. I am new to slicer and want to know how to read the FA maps into Python to generate per voxel (ie get all the set of information including the coordinate and the FA from DataProbe section B). Should I attempt to import the .nrrd file into python? Are there any tutorials I can refer to on how to get started with extracting the information?(such as <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>)</p>
<p>Thank you so much! Sorry if the answer is very obvious!</p>

---
