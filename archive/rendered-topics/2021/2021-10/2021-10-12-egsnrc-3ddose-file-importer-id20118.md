---
topic_id: 20118
title: "Egsnrc 3Ddose File Importer"
date: 2021-10-12
url: https://discourse.slicer.org/t/20118
---

# EGSnrc .3ddose File Importer

**Topic ID**: 20118
**Date**: 2021-10-12
**URL**: https://discourse.slicer.org/t/egsnrc-3ddose-file-importer/20118

---

## Post #1 by @pmdg (2021-10-12 14:24 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.2</p>
<p>Hello,</p>
<p>I’m gratefully using SlicerRT to load in .3ddose files to visualise dose distributions created using the EGSnrc Monte Carlo code. One thing I’d like to be able to do would be to also create a volume representing the relative error on the dose for each voxel, as this information is also contained within the .3ddose file. I think this should be fairly straightforward as the errors are stored in the same block format as the doses (see Section 3 (pg 6) <a href="https://nrc-cnrc.github.io/EGSnrc/doc/pirs509f-statdose.pdf" rel="noopener nofollow ugc">https://nrc-cnrc.github.io/EGSnrc/doc/pirs509f-statdose.pdf</a>), so the code at Line 176 here (<a href="https://github.com/SlicerRt/SlicerRT/blob/master/DosxyzNrc3dDoseFileReader/Logic/vtkSlicerDosxyzNrc3dDoseFileReaderLogic.cxx" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT/vtkSlicerDosxyzNrc3dDoseFileReaderLogic.cxx at master · SlicerRt/SlicerRT · GitHub</a>) could be extended to import the next result block representing the errors.</p>
<p>I think I could probably write something specific for my own application but I wondered if it might be something worth adding to the importer?</p>
<p>Thank you for the help!</p>
<p>Paul</p>

---

## Post #2 by @lassoan (2021-10-13 03:32 UTC)

<p>It would be great if you could make that modification to the importer and send a pull request with the suggested changes.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> should be able to help if you have any questions or run into any issues.</p>

---
