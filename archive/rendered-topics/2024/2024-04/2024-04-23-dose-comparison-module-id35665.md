---
topic_id: 35665
title: "Dose Comparison Module"
date: 2024-04-23
url: https://discourse.slicer.org/t/35665
---

# Dose comparison module

**Topic ID**: 35665
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/dose-comparison-module/35665

---

## Post #1 by @azam (2024-04-23 04:36 UTC)

<p>Hi every one<br>
slicer version: 5.2.2<br>
I have 2 RT Dos exported from the treatment planning system. I want to compare these 2 dose distributions using the Dose Comparison module in 3 D  slicer. my CT slice thickness is 5mm. but I want to calculate gamma index with 3%/3mm.<br>
Can 3D Slicer do this calculations accurately or should the CT Slice thickness be less than 5 mm?<br>
can you help me?<br>
thanks a lot</p>

---

## Post #2 by @cpinter (2024-04-29 11:43 UTC)

<p>I apologize that right now I have time only for a very quick answer, but maybe this will help you make progress.</p>
<p>I just checked and in SlicerRT itself there is no resampling done on the input volumes. Looking at Plastimatch (the library that does the actual comparison), I can give you two hints:</p>
<ol>
<li>Read the paper based on which the algorithm was implemented, see <a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/gamma_dose_comparison.h#L22" class="inline-onebox">src/util/gamma_dose_comparison.h · master · plastimatch / plastimatch · GitLab</a></li>
<li>There are indications in the code for some resampling to be performed, see <a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/src/util/gamma_dose_comparison.cxx#L274" class="inline-onebox">src/util/gamma_dose_comparison.cxx · master · plastimatch / plastimatch · GitLab</a><br>
Please dig a bit more to see when exactly and how (if you have some programming knowledge or willingness to read some code)</li>
</ol>
<p>Good luck!</p>

---
