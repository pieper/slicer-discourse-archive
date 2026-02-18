# Loading StealthStation archive

**Topic ID**: 2771
**Date**: 2018-05-07
**URL**: https://discourse.slicer.org/t/loading-stealthstation-archive/2771

---

## Post #1 by @banderies (2018-05-07 20:50 UTC)

<p>I am trying to process targets created by a StealthStation S7. These targets are collected in the operating room while taking stereotactic biopsies. I have the full stealth archive, including all of the analyze format images (which I have not figured out how to open yet), and .xml files containing the registration transform matrix and all of the surgical plans (i.e. entry points and targets). I was hoping someone on this forum might have had some experience working with this data, as I have not found much online. This is how I am guessing the system works:</p>
<p>Original MRI series space --&gt; analyze image format (or some proprietary version) stored on the S7 (unknown space, except that there is some transform information in the image headers) --&gt; tracer or fiducial registration of the patient in the OR (I have this matrix) --&gt; targets collected in “OR Space”.</p>
<p>I need to create the matrix to get from the “OR space,” or whatever space the targets were collected in, back to the original MRI series space. I have written some code to pull the tracer registration matrix from the archive, and have tried transforming the target points, both through the registration matrix and its inverse, but none of the resulting points match up with any of the original series spaces. Therefore, I am thinking there is another transformation step in between the original MRI series and the patient registration step. I am assuming this transformation occurs when the S7 loads the original DICOMs and converts them to the analyze image format.</p>
<p>At the moment, I might be able to work backwards from the data I have if I could only load the analyze image format images in Slicer. So far I have not been able to get Slicer to load them.</p>
<p>I would greatly appreciate it if anyone here has any ideas.</p>

---

## Post #2 by @lassoan (2020-12-09 17:07 UTC)

<p>It seems that this message fell through the cracks (probably because it was originally posted in the “Community” category instead of “Support”). If you still need help with this then let us know.</p>

---
