# Motion correction in DSCMRIAnalysis?

**Topic ID**: 3621
**Date**: 2018-08-01
**URL**: https://discourse.slicer.org/t/motion-correction-in-dscmrianalysis/3621

---

## Post #1 by @Kyu_Sung_Choi (2018-08-01 01:02 UTC)

<p>Dear Dr. Fedorov,</p>
<p>I have a question about DSCMRIAnalysis module.<br>
<strong>1. Is there a motion correction, noise thresholding, and leakage correction function implemented in the module?</strong></p>
<p>Actually I am trying to register rCBV maps obtained from DSC images using DSCMRIAnalysis module to T1WI images, however it seems that the brain boundary of rCBV map is slightly different from that of DSC images, which makes it difficult to registered to T1WI images perfectly.<br>
I figured out that the problem is “motion” during the acquisition of multiple volumes of DSC images.</p>
<p>Since I do not have much background knowledge about the implementation of DSCMRIAnalysis, I’ve found some softwares - namely, NordicICE - that provide motion correction, noise thresholding, and leakage correction making better quality of registration.<br>
(Moreover, there is a function called “MCFLIRT” in FSL software, which is used for motion correction for registration of fMRI - T2* images quite similar to DSC images except the contrast agent.)<br>
However, I’m not sure that motion correction, noise thresholding, and leakage correction is a common and essential preprocessing in the DSC MRI analysis field.</p>
<p><strong>2. Is it common to have the DSC images motion corrected, noise thresholded as well as leakage corrected before the construction of rCBV maps?</strong><br>
<em>In other words, is it possible to be accepted when I submit papers without motion correction, noise thresholded as well as leakage corrected when making rCBV maps?</em></p>
<p>Always appreciate your help!</p>
<p>Sincerely,<br>
Kyu Sung</p>

---

## Post #2 by @lassoan (2018-08-01 06:31 UTC)

<p>You can use Sequence registration extension for motion correction of image sequences. It expects Sequence node as input, so if you have your image data as MultiVolume node then you have to save it to file and then load as “Volume Sequence”.</p>

---
