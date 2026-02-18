# SPHARM-PDM alignment 

**Topic ID**: 15943
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/spharm-pdm-alignment/15943

---

## Post #1 by @ikhsannk (2021-02-10 23:02 UTC)

<p>Hello, Beatriz, Martin, and others. My name is Ikhsan and I would like to ask a few things regarding SPHARM-PDM.</p>
<p>Firstly, I have looked at the tutorial and worked on the hippocampus example dataset. It functions properly on my laptop and I got the same output with those mentioned in the tutorial, except for the *SPHARM_procalign.vtk file which appears to be missing. My questions are:</p>
<ol>
<li>
<p>How do I get the *SPHARM_procalign.vtk file? I have exactly followed the tutorial (using the hippocampus dataset provided) and tried to use my dataset as well but it doesn’t shows up.</p>
</li>
<li>
<p>Can I use the mean shape that I got from the ShapeVariationAnalyzer as a template for Rigid Procrustes alignment? Or do you have any recommendation which file should I use for the registration template?</p>
</li>
</ol>
<p>Thank you in advance.</p>
<p>Regards,<br>
Ikhsan</p>

---

## Post #2 by @bpaniagua (2021-02-12 20:01 UTC)

<p>Hi Ikhsan,</p>
<p>Thank you for using SPHARM-PDM!</p>
<blockquote>
<p>How do I get the *SPHARM_procalign.vtk file? I have exactly followed the tutorial (using the hippocampus dataset provided) and tried to use my dataset as well but it doesn’t shows up.</p>
</blockquote>
<p>You will need a previously computed spharm model and to use it as registration template</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f018feb2a33ca11f7cb083f3c1c5dcc46bdf0cc1.png" alt="Screen Shot 2021-02-12 at 3.01.05 PM" data-base62-sha1="yg08WxNBnWP0330SLgMdpcAWMdH" width="483" height="127"></p>
<blockquote>
<p>Can I use the mean shape that I got from the ShapeVariationAnalyzer as a template for Rigid Procrustes alignment? Or do you have any recommendation which file should I use for the registration template?</p>
</blockquote>
<p>That is definitely an option, but it does not need to be.</p>
<p>I hope that helps!!<br>
Thanks,</p>
<p>Bea</p>

---

## Post #3 by @ikhsannk (2021-02-16 13:28 UTC)

<p>Hello Bea,</p>
<p>Thank you for the answer, I have now successfully generated the *procalign.vtk file.</p>
<p>If I may ask once again, I have read in some articles that mentioned about the scaling normalization for the head size (intracranial volume) after the rigid-body Procrustes alignment. Can I perform this step on the SPHARM-PDM module, or should I use another module on the SlicerSALT?</p>
<p>I am currently exploring other modules as well, but so far I couldn’t find it on the SPHARM-PDM tutorial.</p>
<p>Thank you once again for your response, I really appreciate it.</p>
<p>Best regards,<br>
Ikhsan</p>

---

## Post #4 by @bpaniagua (2021-02-16 14:40 UTC)

<p>Hi Ikhsan,</p>
<p>Great to hear that you were able to get your procrustes aligned models!</p>
<p>Currently we still do not have a SlicerSALT module to do procrustes alignment (with and without scaling). There is however, a C++ CLI in SPHARM-PDM that does this, it is called <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Modules/CLI/MetaMeshTools/MeshMath.cxx#L225">MeshMath.</a>.</p>
<p>We will definitely look into incorporating this functionality in SlicerSALT soon.<br>
Thank you!</p>
<p>Bea</p>

---

## Post #5 by @ikhsannk (2021-02-16 15:45 UTC)

<p>Hi Bea,</p>
<p>Thank you so much for the quick response. I will try to look deeper into MeshMath while continuing my shape analysis.</p>
<p>Many thanks,<br>
Ikhsan</p>

---
