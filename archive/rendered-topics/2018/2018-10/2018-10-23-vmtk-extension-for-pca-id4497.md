# VMTK extension for PCA

**Topic ID**: 4497
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/vmtk-extension-for-pca/4497

---

## Post #1 by @14jwkn (2018-10-23 10:43 UTC)

<p>Hello, I’m new to this and so far I’ve been using this tutorial (<a href="https://na-mic.org/w/images/a/aa/VMTK_Slicer_3.6.3_Updated_OCT_2011.pdf" rel="nofollow noopener">https://na-mic.org/w/images/a/aa/VMTK_Slicer_3.6.3_Updated_OCT_2011.pdf</a>). I’ve been trying to do a segmentation for the PCA on a t1 divided by t2 MRI scan. I haven’t been able to get it to work, and I have a few questions.</p>
<ol>
<li>What would be the optimal amount and optimal placement for the seeds for vesselness and level set segmentation?</li>
<li>When I do vesselness filtering, the preview displays the red parts filtered correctly but the output after the filtering is a black outline around the same parts. Is this an error and does it affect segmentation?</li>
<li>I read that the optimal settings for blood vessel segmentation include reducing blob-like structures threshold and increasing plate-like structures threshold. Are there other alterations I could do to troubleshoot?</li>
<li>Are there more resources where I could read about VMTK in Slicer specifically? The other tutorials I’ve read are about VMTK only.</li>
</ol>

---

## Post #2 by @pieper (2018-10-23 17:06 UTC)

<p>You could have a look at the project writeup by <span class="mention">@haehn</span> <a href="https://www.slicer.org/w/images/e/e8/Haehn-Slicer_VMTK_student_research_project.pdf">https://www.slicer.org/w/images/e/e8/Haehn-Slicer_VMTK_student_research_project.pdf</a></p>

---
