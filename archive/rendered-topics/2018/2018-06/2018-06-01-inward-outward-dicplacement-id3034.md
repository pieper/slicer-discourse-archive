---
topic_id: 3034
title: "Inward Outward Dicplacement"
date: 2018-06-01
url: https://discourse.slicer.org/t/3034
---

# Inward_outward dicplacement

**Topic ID**: 3034
**Date**: 2018-06-01
**URL**: https://discourse.slicer.org/t/inward-outward-dicplacement/3034

---

## Post #1 by @Olof (2018-06-01 08:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fb2e8fab44ba8bf433d9b611504b310e329f012.jpeg" data-download-href="/uploads/short-url/dEAFI5TDrCknyE8x7gBwZ33RVZ0.jpg?dl=1" title="Left_bvfTD_sd_old" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fb2e8fab44ba8bf433d9b611504b310e329f012_2_689x438.jpg" alt="Left_bvfTD_sd_old" data-base62-sha1="dEAFI5TDrCknyE8x7gBwZ33RVZ0" width="689" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fb2e8fab44ba8bf433d9b611504b310e329f012_2_689x438.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5fb2e8fab44ba8bf433d9b611504b310e329f012_2_1033x657.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fb2e8fab44ba8bf433d9b611504b310e329f012.jpeg 2x" data-dominant-color="321549"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Left_bvfTD_sd_old</span><span class="informations">1240×788 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Dear Martin and Beatriz,</p>
<p>running spharm I am a bit confused by my results. On the left side it seems to be a displacement towards the medial part of the brain … causing an deflation of the medial anterior and medial posterior hippocampus.<br>
But on the right side we see the opposite pattern  … thus an inflation of the most medial anterior and posterior hippocampus.<br>
Of course we can manipulate this changing the orders of the groups in the shapeanalysis mancova on the right side (which provides us with the same pattern as on the left side) … but results seem to indicate opposite movement on the left and right side of the hippocampus<br>
Have you seen this before? Or is there something I am missing here?</p>
<p>Thanks<br>
OLof</p>

---

## Post #2 by @bpaniagua (2018-06-01 12:36 UTC)

<p>Hi Olof,</p>
<p>Do you also have vector maps we can look at for these absolute distance maps? Also, what is the registration used for these surfaces before you start the quantification process i.e. procrustes aligned, ellipsoid aligned, some other external registration?<br>
Thank you!</p>
<p>Bea</p>

---

## Post #3 by @Olof (2018-06-01 12:42 UTC)

<p>Basically we did as you previously suggested. We run one subjects and then use this subjects as registration template for all other subjects.<br>
So we use the procrustes aligned for the group analysis - what you see is the statistical fdr and the diff mesh</p>

---

## Post #4 by @doganarda (2018-07-11 12:02 UTC)

<p>Hi everyone,</p>
<p>I need to run statistical shape analysis on SPHARM-PDM reconstructed (I did the SPHARM analysis on Slicer3D) and I have been trying to figure out how to run shapeAnalysis MANCOVA for a while now (I even tried to look into very old versions of SPHARM PDM toolbox, I guess 1.12 and even though I can run shapeAnalysisMANCOVA through terminal, I am having some errors and I am not really comfortable with using the old versions).</p>
<p>I know this topic is really not related to my problem but I have come across this topic while trying to figure out how to run shapeAnalysisMANCOVA on Slicer Salt - I have it installed on my computer but I cannot access to any statistical analysis. My aim is to compare 20 hippocampi reconstructed through SPHARM-PDM and I was wondering if any of you could help me figure out how to get to the point (the image posted here looks very much like what I want to carry out on my study). How can I run any statistical shape analysis using shape analysis mancova on Slicer Salt?</p>
<p>Sorry to bother you, I would appreciate any help and thanks in advance.<br>
Kind regards,<br>
Arda</p>

---
