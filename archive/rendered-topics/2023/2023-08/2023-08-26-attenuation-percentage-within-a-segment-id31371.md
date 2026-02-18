# Attenuation percentage within a segment

**Topic ID**: 31371
**Date**: 2023-08-26
**URL**: https://discourse.slicer.org/t/attenuation-percentage-within-a-segment/31371

---

## Post #1 by @Frederico_Lisboa_Nog (2023-08-26 03:14 UTC)

<p>I am quite new at 3D Slicer. I have done some muscle segmentations (HU between -29 to 150) and I would like to further classify the percentage of the segmented area according to a range of attenuation.</p>
<p>Example: 20% between -29 and +50<br>
80% between +50 and +150</p>
<p>I have tried to use LungCTAnalyzer unsuccessfully for this. Is the some extension for this?</p>
<p>Regards</p>

---

## Post #2 by @Frederico_Lisboa_Nog (2023-09-11 03:10 UTC)

<p>Anyone that can help?</p>

---

## Post #3 by @mikebind (2023-09-11 16:37 UTC)

<p>Here is a python script example which would allow you to gather all the voxel values within a given segment into a numpy array, where you could perform whatever binning you would like for further analysis: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" rel="noopener nofollow ugc">Get Histogram of Segmented Region</a></p>

---

## Post #4 by @Frederico_Lisboa_Nog (2023-09-16 21:25 UTC)

<p>Thank you <a class="mention" href="/u/mikebind">@mikebind</a> !</p>

---
