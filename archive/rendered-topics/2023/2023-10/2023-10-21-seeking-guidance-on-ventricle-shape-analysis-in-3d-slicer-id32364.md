---
topic_id: 32364
title: "Seeking Guidance On Ventricle Shape Analysis In 3D Slicer"
date: 2023-10-21
url: https://discourse.slicer.org/t/32364
---

# Seeking Guidance on Ventricle Shape Analysis in 3D Slicer

**Topic ID**: 32364
**Date**: 2023-10-21
**URL**: https://discourse.slicer.org/t/seeking-guidance-on-ventricle-shape-analysis-in-3d-slicer/32364

---

## Post #1 by @Julius_Bogomolovas (2023-10-21 12:42 UTC)

<p>Hello 3D Slicer community,</p>
<p>First and foremost, I’d like to express my gratitude for your dedication to developing and maintaining this powerful set of tools for shape analysis. So this is gonna be a multifaceted post, but I will try to explain everything in detail and would be very thankful for guidance.</p>
<p><strong>Objective:</strong> My aim is to measure and statistically evaluate the differences in ventricle shape between WT and mutant animals. I’ve segmented the ventricles from both groups (4-8 per group) and tried two different methods:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd584b4d3434c9cecd67ac49e3da27757cb05270.png" data-download-href="/uploads/short-url/tiz39c5cmmuIfKPR1iAsctF0MnK.png?dl=1" title="Screenshot 2023-10-20 at 4.12.14 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd584b4d3434c9cecd67ac49e3da27757cb05270_2_690x290.png" alt="Screenshot 2023-10-20 at 4.12.14 PM" data-base62-sha1="tiz39c5cmmuIfKPR1iAsctF0MnK" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd584b4d3434c9cecd67ac49e3da27757cb05270_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd584b4d3434c9cecd67ac49e3da27757cb05270_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd584b4d3434c9cecd67ac49e3da27757cb05270.png 2x" data-dominant-color="B4B2A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-20 at 4.12.14 PM</span><span class="informations">1252×528 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li><strong>Pseudo-landmarks Approach:</strong> I generated around 500 pseudo-landmarks, transferred them to all samples using ALPACA, performed GPA in Slicermorph, and ran shape ANOVA in geomorph. This method didn’t yield significant differences between the groups. I suspect the intra-group variability is masking the genuine differences. Is there a method to choose the most telling pseudo-landmarks, akin to the Procrustes distance for landmarks, and perform shape regression based on them? Are there other strategies within this framework you’d recommend?</li>
<li><strong>SHPARM-PDM Approach:</strong> This was a tough one. I faced issues with both the SlicerSALT and 3D Slicer implementations of SHPARM-PDM on Windows 10 during the SegPostProcess step, likely due to binary segmentation issues. Thankfully, it functioned on a Mac with Ventura OS, and I obtained results from ParaToSPHARMMesh. However, the ventricles weren’t aligned properly. I then tried improving the SHPARM correspondence with ALPACA pseudolandmarks. Unfortunately, I faced crashes during the RigidAlignment step on both operating systems. I did manage to execute RigidAlignment in SlicerSalt on Windows 10 but only by choosing Shape Creation&gt;Andvanced&gt;RigidAligment. However, it aligns only the spheres, not the actual objects. I’m contemplating forgoing a detailed SHPARM-PDM analysis and simply computing and comparing the rotation-invariant harmonic spectra. Does anyone have a script for this using ParaToSPHARMMesh outputs? Alternatively, is it feasible to input pre-aligned shapes into SHPARM-PDM, bypassing the need for Correspondence Improvement?</li>
</ol>
<p>Your insights and suggestions will be immensely appreciated. Thank you in advance.</p>

---

## Post #2 by @muratmaga (2023-10-21 20:02 UTC)

<aside class="quote no-group" data-username="Julius_Bogomolovas" data-post="1" data-topic="32364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julius_bogomolovas/48/67968_2.png" class="avatar"> Julius_Bogomolovas:</div>
<blockquote>
<p>transferred them to all samples using ALPACA,</p>
</blockquote>
</aside>
<p>This will be a source of variation, and it will be a function of how well things are registered. You can try a few experiments to see if you can improve the alignment. another thing to consider if your template you create the pseudoLMs with  is a “normal” one, it may create a some bias towards “normalness”, hence again may reduce inter group variation.</p>
<p>Do you have may be 10-12 good anatomical landmarks that you can annotate on your all samples? If so, instead of ALPACA you can use ProjectSemiLM landmarks, which will use the anatomical landmarks to anchor the semiLMs. The key is to have them all over the surface.</p>
<p>One benefit of having some anatomical landmarks, you can have a clear sense whether one ALPACA set of parameters is better than the other (because if you input the optional target landmarks during the interactive session, it will report an RMSE of difference between your manual landmarks and alpaca transferred one). That way you can go accurately about optimizing for registration parameters for alpaca (as opposed to guessing from visuals).</p>
<aside class="quote no-group" data-username="Julius_Bogomolovas" data-post="1" data-topic="32364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julius_bogomolovas/48/67968_2.png" class="avatar"> Julius_Bogomolovas:</div>
<blockquote>
<p>Procrustes distance for landmarks,</p>
</blockquote>
</aside>
<p>PD for individual landmarks is not a meaningful metrics, because ultimately the PD is function of how well rest of the landmarks are also aligned (since this is a least squares optimization).</p>
<p>As for fully automatic shape analysis, there is always some caveats to be aware of (such as a good rigid alignment to initialize the SPHARM). An option is to actually use something like FastModelAlign in SlicerMorph to do the rigid/similarity alignment, and then feed the aligned model to SPHARM.</p>

---

## Post #3 by @bpaniagua (2023-10-25 12:34 UTC)

<blockquote>
<ol>
<li><strong>SHPARM-PDM Approach:</strong> This was a tough one. I faced issues with both the SlicerSALT and 3D Slicer implementations of SHPARM-PDM on Windows 10 during the SegPostProcess step, likely due to binary segmentation issues.</li>
</ol>
</blockquote>
<p>Hi there! I am curious as what might have caused problems on Windows that did not cause them on MacOS. All the algorithms are the same. Yes, binary segmentations will cause problems even when the topology is spherical (i.e. almost holes will create numerical errors)</p>
<blockquote>
<p>Thankfully, it functioned on a Mac with Ventura OS, and I obtained results from ParaToSPHARMMesh. However, the ventricles weren’t aligned properly.</p>
</blockquote>
<p>You will get several results from SPHARM-PDM, and it is true that depending on the subscript your files have, that will indicate they have been aligned to a template. If they are the base triangulation computed by SPHARM they should not be misaligned.</p>
<blockquote>
<p>I did manage to execute RigidAlignment in SlicerSalt on Windows 10 but only by choosing Shape Creation&gt;Andvanced&gt;RigidAligment. However, it aligns only the spheres, not the actual objects.</p>
</blockquote>
<p>This is a intermediate step for improvement of correspondence. With the meshes in correspondence you can align them using procrustes.</p>
<blockquote>
<p>Does anyone have a script for this using ParaToSPHARMMesh outputs?</p>
</blockquote>
<p>Using them how? And what outputs? ParaToSPHARMMesh produces a lot of outputs.</p>
<blockquote>
<p>Alternatively, is it feasible to input pre-aligned shapes into SHPARM-PDM, bypassing the need for Correspondence Improvement?</p>
</blockquote>
<p>See my comment above, you should have regTemplate meshes if you have clicked that option, but the original triangulated meshes should be there also. Could you please show us what the output of each SPHARM-PDM step is?</p>
<p>Thank you,<br>
Bea</p>

---

## Post #4 by @Julius_Bogomolovas (2023-10-26 20:09 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> for insightful suggestions, navigating me through new field of shape quantifications. I will implement your suggestions and let you know how did it go.</p>

---

## Post #5 by @Julius_Bogomolovas (2023-10-26 20:47 UTC)

<p>Dear Bea <a class="mention" href="/u/bpaniagua">@bpaniagua</a>, thank you for your comprehensive comments on SPHARM-PDM analysis.</p>
<ul>
<li>
<p><strong>Regarding failure of SegPostProcess step on PC</strong>. I really did not look into this matter more deeply, but my guess is how computer treats the values of binary segmentation, there are several formats of integers like long, short etc. It seems that MacOS reads “1”, like one whereas PC expects something like “1.00000” doesn’t find it and gets upset. It doesnt seem to be problem of topology, as I do WrapSolidify on segmentations before SPHARM-PDM, and same input works on MacOS, but not PC.</p>
</li>
<li>
<p><strong>Does anyone have a script for this using ParaToSPHARMMesh outputs?</strong><br>
I am a bit new to this, but from my understanding somewhere in ParaToSPHARMMesh there is a file with decomposition of shape into spheric harmonics that I could take and calculate rotation-invariant spectrum [<a href="https://www.cs.jhu.edu/~misha/MyPapers/SGP03.pdf" rel="noopener nofollow ugc">https://www.cs.jhu.edu/~misha/MyPapers/SGP03.pdf</a>], thus instead proper SHPARM-PDM analysis, I could compare differences between these spectra [PMID:32269257].</p>
</li>
<li>
<p><strong>SPHARM-PDM outputs</strong><br>
Here is the link for the SHPARM-PDM outputs:<a href="https://www.dropbox.com/t/XPvfGcv36F9kQs8e" class="inline-onebox" rel="noopener nofollow ugc">Transfer - Dropbox</a><br>
I include below few images of SHPARM: *ellalign and *SPHARM colored according Phi values and indicated aortic root positions which should be aligned. I will follow advice and try to feed rigid aligned shapes into SHPARM-PDM<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef68acdfeb432a378aa0b309931a98e78e1a8b27.jpeg" data-download-href="/uploads/short-url/y9UnDolaZ5OGt2xJHT45WN1dgyz.jpeg?dl=1" title="Screenshot 2023-10-26 at 1.28.45 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef68acdfeb432a378aa0b309931a98e78e1a8b27_2_658x500.jpeg" alt="Screenshot 2023-10-26 at 1.28.45 PM" data-base62-sha1="y9UnDolaZ5OGt2xJHT45WN1dgyz" width="658" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef68acdfeb432a378aa0b309931a98e78e1a8b27_2_658x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef68acdfeb432a378aa0b309931a98e78e1a8b27_2_987x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef68acdfeb432a378aa0b309931a98e78e1a8b27_2_1316x1000.jpeg 2x" data-dominant-color="51415E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-26 at 1.28.45 PM</span><span class="informations">1498×1138 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<p>Thank you!<br>
Julius</p>

---
