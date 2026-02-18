# Multivolume cardiac segmentation

**Topic ID**: 5430
**Date**: 2019-01-20
**URL**: https://discourse.slicer.org/t/multivolume-cardiac-segmentation/5430

---

## Post #1 by @sarvpriya1985 (2019-01-20 22:15 UTC)

<p>Hello everyone,<br>
This may seem a repeat request. I have been trying to segment multiple cardiac phases. So far this is the work sequence I have been using.</p>
<ol>
<li>Import dicom file as volume.</li>
<li>Sequence browser module.</li>
<li>Created a new sequence.</li>
<li>For the selected frame I did threshold segmentation.</li>
<li>However this segmentation gets transferred to all other frames that is not correct.</li>
<li>Even if I accept the segmentations created on all frames, I can’t play that as cine file.</li>
</ol>
<p>I have tried several methods but no success so far. As told by Andras, I completed the Slicer Igt tutorial as well for Fiducial registration but not sure how to apply that in this aspect.<br>
If anyone could share their work similar to this, would greatly appreciate.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @pieper (2019-01-20 22:48 UTC)

<p>Hi Sarv -</p>
<p>Andras is out on vacation for a while, and of course he’s the most knowledgeable about those specific tools (Segment Editor and Sequences).  If you have data you can share so that people can try to replicate your steps then maybe someone can help you get past your sticking points.</p>
<p>-Steve</p>

---

## Post #3 by @sarvpriya1985 (2019-01-21 00:07 UTC)

<p>Thanks for replying Steve. Andras has been providing much needed help but I am unable to replicate those. What I am requesting is performing manual segmentation for all cardiac  phases and then combine them to play as a cine file. I tried sequence registration as told by Andras but it didn’t work well. I am sharing the file here and would appreciate if anyone could help me in doing that.</p>
<p>Thanks,<br>
Sarv<br>
<a href="https://iowa-my.sharepoint.com/:f:/g/personal/spriya_uiowa_edu/EuSlc2OcnvZNuAZt8OR2jFQBD1vD_f2bnr8Q9S42Ga9sqw?e=sQsLAn" rel="nofollow noopener">Multiphase cardiac CT data</a></p>

---
