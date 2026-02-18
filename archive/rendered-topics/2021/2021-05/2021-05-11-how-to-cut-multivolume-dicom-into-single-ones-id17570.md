# How to cut multivolume dicom into single ones?

**Topic ID**: 17570
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/how-to-cut-multivolume-dicom-into-single-ones/17570

---

## Post #1 by @Mikolaj_Drab (2021-05-11 13:34 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior: I load multivolume (contrast enhaced dyn) dicom to make a subtraction.<br>
Actual behavior: When the multivolume dicom is loaded, Slicer only shows the first frame (without contrast) and I can’t find how to even see what other frames look like not mention to make subtraction.<br>
Can anyone help me?</p>

---

## Post #2 by @JanWitowski (2021-05-11 18:54 UTC)

<p>A few things that would help to understand this problem:</p>
<ol>
<li>When you go to your DICOM browser → select “Advanced” → Examine, do you get a list of sequences that you can select? A screenshot would be helpful</li>
<li>Try loading your study as a volume sequence (Application Settings → DICOM → Preferred multi-volume import format)</li>
<li>You can also try <a href="https://github.com/rordenlab/dcm2niix" rel="noopener nofollow ugc">dcm2niix</a>, I remember it was being recommended around here for converting multiframe DICOM to nifti/nrrd and then loading that format</li>
<li>If it’s possible, sharing a sample anonymized study with us would be helpful in troubleshooting</li>
</ol>

---

## Post #3 by @lassoan (2021-05-13 06:16 UTC)

<p>I would recommend to load 4D volumes as volume sequences as <a class="mention" href="/u/janwitowski">@JanWitowski</a> described above and then use the toolbar to browse frames. You can display multiple timepoints of the same volume sequence by creating a new browser node in Sequences module.</p>
<p>You can find step-by-step instructions for computing motion-compensated subtraction for segmentation of small vessels in this <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/">segmentation recipe</a>.</p>
<p>Note that you may also browse or access frames and perform operations on them using numpy as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#sequences">examples in the script repository</a>.</p>

---
