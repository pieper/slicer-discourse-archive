# Python script for transferring markup fiducial (fcsv file) to Excel

**Topic ID**: 4447
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/python-script-for-transferring-markup-fiducial-fcsv-file-to-excel/4447

---

## Post #1 by @Melanie (2018-10-17 23:39 UTC)

<p>Hi All, could someone help me to write a python script to transfer fssv data (Real time RAS coordinates) in a transformed sequence to excel please.<br>
I  have no programming knowledge, I am afraid. Thanks</p>

---

## Post #2 by @lassoan (2018-10-18 00:08 UTC)

<p>The easiest is to click Copy button in Slicer (in Markups module) and paste into Excel. If you need transformed coordinates then you need to harden the transform on the markup fiducial node in Transforms module before you copying.</p>
<p>You can also open fcsv files directly in Excel and use <em>Data</em> / <em>Text to columns</em> to split values to columns (Delimited, Comma).</p>

---

## Post #3 by @Melanie (2018-10-18 00:26 UTC)

<p>Thank you very much Prof Lasso, I ve tried this but it always pastes the non transformed coordinates even after hardening. ( I go to the transform module and click the hardening transform icon in between the two columns after making sure my output volumes and fiducial node s are on the right side column( transformed side)<br>
Even after this it gives me the same value for all the frames ; that is a the non transformed value of RAS coordinates on my reference frame. Am I doing the steps wrong&gt; Thank you ever so much  for your time Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #4 by @lassoan (2018-10-18 00:50 UTC)

<p>If you harden the transform then it should go from the right side (transformed) to the left (non-transformed), without any visible changes in point positions. When you copy point coordinates, the markups node must be on the left side.</p>

---

## Post #5 by @Melanie (2018-10-18 01:12 UTC)

<p>Thank you very much, I did not see that change happening, meaning I am doing something wrong. I will run this again and see. Thanks a lot.</p>

---

## Post #6 by @stevenagl12 (2019-08-28 11:08 UTC)

<p>What you are doing wrong is, you have to select the fiducials from the column before clicking on the harden button after you’ve transformed them.</p>

---
