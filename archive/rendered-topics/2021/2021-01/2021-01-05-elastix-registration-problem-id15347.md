---
topic_id: 15347
title: "Elastix Registration Problem"
date: 2021-01-05
url: https://discourse.slicer.org/t/15347
---

# Elastix registration problem

**Topic ID**: 15347
**Date**: 2021-01-05
**URL**: https://discourse.slicer.org/t/elastix-registration-problem/15347

---

## Post #1 by @opetne (2021-01-05 10:52 UTC)

<p>Operating system: Windows10<br>
Slicer version:4.11.20200930<br>
Expected behavior:Registration 2 MR volumes<br>
Actual behavior:<br>
Volume registration is started in working directory: C:/Users/petnehazyors/AppData/Local/Temp/Slicer/Elastix/20210105_114326_719</p>
<p>Register volumes…</p>
<p>Error: [WinError 2] The system cannot find the file specified</p>
<p>Error log:<br>
Register volumes using: C:/Users/petnehazyors/AppData/Local/Temp/Slicer/Elastix/20210105_112621_164\elastix.exe: [’-f’, ‘C:/Users/petnehazyors/AppData/Local/Temp/Slicer/Elastix/20210105_114326_719\input\fixed.mha’, ‘-m’, ‘C:/Users/petnehazyors/AppData/Local/Temp/Slicer/Elastix/20210105_114326_719\input\moving.mha’, ‘-out’, ‘C:/Users/petnehazyors/AppData/Local/Temp/Slicer/Elastix/20210105_114326_719\result-transform’, ‘-p’, ‘C:\Users\petnehazyors\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Parameters_Rigid.txt’, ‘-p’, ‘C:\Users\petnehazyors\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\Parameters_BSpline.txt’]</p>
<p>[WinError 2] The system cannot find the file specified</p>

---

## Post #2 by @lassoan (2021-01-07 01:21 UTC)

<p>Does it work with sample data sets (e.g., MRBrainTumor1 and MRBrainTumor2)?</p>
<p>If you enable Advanced / “Keep temporary files” then can you find all the reference input and output files after the registration is completed?</p>

---
