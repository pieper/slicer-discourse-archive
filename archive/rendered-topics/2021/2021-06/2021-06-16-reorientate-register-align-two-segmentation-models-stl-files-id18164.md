# Reorientate/Register/Align two segmentation models/STL Files

**Topic ID**: 18164
**Date**: 2021-06-16
**URL**: https://discourse.slicer.org/t/reorientate-register-align-two-segmentation-models-stl-files/18164

---

## Post #1 by @Solli (2021-06-16 12:34 UTC)

<p>Hello,<br>
I started working with slicer.<br>
I have two different CT Series from the skull. In both images i segmented the bones of the skull. Now i want to compare the model and calculate with the Module Segment comparison the Dice coefficient and the Hausdorff distance. The goal is to find out if the segmented skull of the second CT serie is smaller than the skull of the first serie and to compare with Dice the similarity between both skulls.<br>
Now the problem is that one model is at the top of the bos and one at the bottom and the orientation of the model at the top is not right(anterior and posterior is switched)</p>
<p>Has anyone an idea how i can solve this problem?<br>
I attached a foto of my problem.</p>
<p>Best regards Solveig</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10f0e7cecc77c81aecc1349579a67ca6de2ed48f.png" data-download-href="/uploads/short-url/2pRMbtuSHPDn4mzy2SNmt2aXQsL.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10f0e7cecc77c81aecc1349579a67ca6de2ed48f_2_212x500.png" alt="grafik" data-base62-sha1="2pRMbtuSHPDn4mzy2SNmt2aXQsL" width="212" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10f0e7cecc77c81aecc1349579a67ca6de2ed48f_2_212x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10f0e7cecc77c81aecc1349579a67ca6de2ed48f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10f0e7cecc77c81aecc1349579a67ca6de2ed48f.png 2x" data-dominant-color="9B9AD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">302×709 12.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-06-17 03:32 UTC)

<p>Before you can compare the segmentations, you must align them. You can use registration methods described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">documentation</a>. For example, registration using Fiducial registration wizard, optionally followed by Model registration should work.</p>

---

## Post #3 by @Solli (2021-06-17 15:47 UTC)

<p>Hey Andras,</p>
<p>Thank you so much!! It worked well with the Model Registration and after i used the Segment Comparison to compute the Dice coefficient and the Hausdorff distance !! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
Best Regards<br>
Solveig</p>

---
