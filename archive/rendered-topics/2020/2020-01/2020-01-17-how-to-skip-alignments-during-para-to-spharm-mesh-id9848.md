---
topic_id: 9848
title: "How To Skip Alignments During Para To Spharm Mesh"
date: 2020-01-17
url: https://discourse.slicer.org/t/9848
---

# How to skip alignments during para to spharm mesh

**Topic ID**: 9848
**Date**: 2020-01-17
**URL**: https://discourse.slicer.org/t/how-to-skip-alignments-during-para-to-spharm-mesh/9848

---

## Post #1 by @Oh_jeongseok (2020-01-17 07:52 UTC)

<p>Hello, I’m using 3D Slicer and SPHARM extentions.</p>
<p>I tried making surface ssm with tibias. To apply this methods, I align all models before using SPHARM(picture on right).</p>
<p>However, while SPHARM module is running, the alignments were changed.<br>
(the picture on the left is result of alignment which is done by SPHARM module)<br>
I tried to run with using registration templetes but the results were same.</p>
<p>So, I want to know if it can do SPHARM mesh generation without doing align again(suppose the models are all aligned already like picture on the right)</p>
<p>Thank you for read this question.!<br>
<a href="/404" data-orig-href="upload://wgXIX3nHKKn22Rjzi5vw6hmwJj3.png">Screenshot from 2020-01-17 14-33-35|690x391</a></p>
<p>Regards,<br>
Jeongseok</p>

---

## Post #2 by @Oh_jeongseok (2020-01-17 13:24 UTC)

<p>Operating system: ubuntu 16.04<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8369379a4b23335be754fd7d0efa71a95acc17a.png" data-download-href="/uploads/short-url/x8fHvToAnXRWY8nmAdi6ebT3Jq2.png?dl=1" title="Screenshot from 2020-01-17 14-33-35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8369379a4b23335be754fd7d0efa71a95acc17a_2_690x391.png" alt="Screenshot from 2020-01-17 14-33-35" data-base62-sha1="x8fHvToAnXRWY8nmAdi6ebT3Jq2" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8369379a4b23335be754fd7d0efa71a95acc17a_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8369379a4b23335be754fd7d0efa71a95acc17a_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8369379a4b23335be754fd7d0efa71a95acc17a_2_1380x782.png 2x" data-dominant-color="29172E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-01-17 14-33-35</span><span class="informations">1850×1049 419 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello,</p>
<p>I tried making surface ssm with tibias. To apply this methods, I align all models before using SPHARM(picture on right).</p>
<p>However, while SPHARM module is running, the alignments were changed.<br>
(the picture on the left is result of SPHARM module’s doing alignment)<br>
I tried to run with using registration templetes but the results were same.</p>
<p>So, I want to know if it can do SPHARM mesh generation without doing align again(suppose the models are all aligned already like picture on the right)</p>
<p>Thank you for read this question.</p>
<p>Regards,<br>
Jeongseok</p>

---

## Post #3 by @bpaniagua (2020-01-17 21:28 UTC)

<p>Hi Jeonseonk</p>
<p>Sorry to hear you are having trouble.<br>
What output files are you showing in that display? What is the suffix appended by the module?</p>
<p>Thanks,<br>
Bea</p>

---

## Post #4 by @Oh_jeongseok (2020-01-19 22:57 UTC)

<p>The left side is capture of __surf_SPHARM_ellalign.vtk s and colormap attribute was paraPhi , and right side is of __surf_SPHARM.vtk s.</p>
<p>I’m using 3D slicer, so I didn’t use command lines. I changed  iteration numbers, subdivision levels and registration templete options. As I mentioned above, I tried without templete option too but it doesn’t changed. I also tried flip option but it was not really good.</p>
<p>Thank you,<br>
Jeongseok.</p>

---

## Post #5 by @bpaniagua (2020-01-20 14:09 UTC)

<p>Hi,</p>
<p>First, you need to work only with the *surf_SPHARM.vtk cases. In those (that right now are flipped), you will need to manually enforce flips (see pp. 44 in the <a href="https://docs.google.com/presentation/d/1ZZ6UpONwTl_GKk66Kde9Brq0PIDujw2pKavm1RD1SBo/present?slide=id.p44">SPHARM tutorial</a>) since some of your tibias are wider in the upside than the downside.</p>
<p>This will mean identifying those cases that are flipped and enforce the right alignment for those cases.<br>
When you recompute those flips then you will be able to use the *ellalign.vtk cases.</p>
<p>Hope that helps!<br>
Bea</p>

---

## Post #6 by @Oh_jeongseok (2020-01-21 08:19 UTC)

<p>Hi,</p>
<p>Thank you for your suggestion. However, I have some more questions.</p>
<ol>
<li>Can I skip alignment process?<br>
Either I use flip or not, it seems like that do ellipsoid align to find poles and then make the mesh, and after this process, multiply the inverse of transformation matrix to go back to original location. It might be the *surf_SPHARM.vtk s. The figures are results with some flip options but no flip to 1~6th models, but alignments are changed and the *surf_SPHARM.vtk s are also affected by that… So I take care about ellalign things and try to find skipping alignment process.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/873a3674962b40787e4d5d6d80e37007f0f50871.png" data-download-href="/uploads/short-url/jihb4QysDs5hBOc6lHpxtMzDkqt.png?dl=1" title="ellaligned_Screenshot from 2020-01-21 16-48-38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/873a3674962b40787e4d5d6d80e37007f0f50871_2_690x327.png" alt="ellaligned_Screenshot from 2020-01-21 16-48-38" data-base62-sha1="jihb4QysDs5hBOc6lHpxtMzDkqt" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/873a3674962b40787e4d5d6d80e37007f0f50871_2_690x327.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/873a3674962b40787e4d5d6d80e37007f0f50871_2_1035x490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/873a3674962b40787e4d5d6d80e37007f0f50871.png 2x" data-dominant-color="38244F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ellaligned_Screenshot from 2020-01-21 16-48-38</span><span class="informations">1282×608 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Is GenParaMesh process necessary to solve this problem? I’m now thinking this can occur because from GenParaMesh process also affected with alignments that I didn’t expect. I didn’t check ‘Overwrite’ options in GenParaMesh process so that I can use existing files.</li>
</ol>
<p>If I have wrong concept, please let me know.</p>
<p>because english is not native language, I couldn’t explain simple and clear. Please understand me.<br>
Thank you for your help.<br>
Jeongseok</p>

---

## Post #7 by @bpaniagua (2020-01-21 14:16 UTC)

<p>Hi Jeongseok</p>
<p>For what i see, the only way you will be able to use all your data is to flip certain cases (for what i can see 11B07, 11b09, 11B21, 11B23 and 11B24). The flip process is very fast, it only re-runs paratospharmmesh. What i would do is:</p>
<ol>
<li>First generate all possible flips for one of those cases, just to find the right flip for your data.</li>
<li>Once the right flip has been identified, run it for all the cases that require flipping.</li>
</ol>
<p>We incorporated all of this in the new module to make it easier, before we used bash scripts that just re-run ParaToSPHARMMesh. Let me know if you rather use that.</p>
<p>HTH<br>
Bea</p>

---
