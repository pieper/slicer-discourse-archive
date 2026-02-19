---
topic_id: 2371
title: "Radiomics Error"
date: 2018-03-20
url: https://discourse.slicer.org/t/2371
---

# Radiomics error

**Topic ID**: 2371
**Date**: 2018-03-20
**URL**: https://discourse.slicer.org/t/radiomics-error/2371

---

## Post #1 by @mgastall (2018-03-20 03:31 UTC)

<p>I get the following error when I am using radiomics:</p>
<p>RadiomicsCLI standard error:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\Andrea\AppData\Roaming\NA-MIC\Extensions-27030\SlicerRadiomics\Lib\Slicer-4.9\cli-modules\SlicerRadiomicsCLIScript”, line 6, in<br>
from radiomics.scripts import commandline<br>
ImportError: cannot import name commandline</p>
<p>Any help would be appreciated. Thank you.</p>

---

## Post #2 by @JoostJM (2018-03-21 09:33 UTC)

<p><a class="mention" href="/u/mgastall">@mgastall</a>, This is indeed a bug in the module, it was caused by a recent update of the commandline interface in PyRadiomics, see also this <a href="https://github.com/Radiomics/pyradiomics/pull/347" rel="nofollow noopener">PR</a>.<br>
I fixed this today in <a href="https://github.com/Radiomics/SlicerRadiomics/commit/5d8e55ccc162a287cb55390f24953827a84bea5c" rel="nofollow noopener">this commit</a>, so it should work in tomorrow’s nightly build.</p>

---

## Post #3 by @mgastall (2018-03-21 21:48 UTC)

<p>Thank you very much. Sorry for the basic question, however, I use editor to draw my ROI or label map. When I try to just use segment editor (as the slice fill in tool is very helpful which is not available in editor) a label map is not created (only a segment) so I cannot use radiomics or cad heterogeneity as it requires a label map. Thank you.</p>

---

## Post #4 by @lassoan (2018-03-21 22:11 UTC)

<p>Export segmentation to labelmap using Segmentations module.</p>

---

## Post #5 by @JoostJM (2018-03-22 08:58 UTC)

<p>The SlicerRadiomics accepts both labelmaps and segments. The necessary conversion is handled by the module logic then.</p>

---
