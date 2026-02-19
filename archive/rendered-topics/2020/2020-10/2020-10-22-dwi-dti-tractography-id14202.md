---
topic_id: 14202
title: "Dwi Dti Tractography"
date: 2020-10-22
url: https://discourse.slicer.org/t/14202
---

# DWI, DTI, Tractography

**Topic ID**: 14202
**Date**: 2020-10-22
**URL**: https://discourse.slicer.org/t/dwi-dti-tractography/14202

---

## Post #1 by @Mohammed_Alahmari (2020-10-22 10:52 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior: Hi everyone<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c36db264d93b76b2d0b6b1124457a1b13b1762d1.jpeg" data-download-href="/uploads/short-url/rSQ88awWOGlfd8AHKe4ZkHde797.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c36db264d93b76b2d0b6b1124457a1b13b1762d1_2_690x94.jpeg" alt="Capture" data-base62-sha1="rSQ88awWOGlfd8AHKe4ZkHde797" width="690" height="94" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c36db264d93b76b2d0b6b1124457a1b13b1762d1_2_690x94.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c36db264d93b76b2d0b6b1124457a1b13b1762d1_2_1035x141.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c36db264d93b76b2d0b6b1124457a1b13b1762d1.jpeg 2x" data-dominant-color="F9F9F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1201×165 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> ,<br>
I have been given a new DWI project. The project compares different sequencing parameters to visualize the facial nerve. I’m a beginner to the MRI field including DTI and DWI topics. I read the tutorial of SoniaPujol entitled “WhiteMatterExplorationTutorial_SoniaPujol-RonKikinis” and could follow the steps on the tutorial dataset successfully. However, when I tried to apply the same steps to my data, I couldn’t. I tried to find the differences between my data and the dataset of the tutorial and found:</p>
<ul>
<li>The tutorial dataset includes in one file, 41 volumes acquired with 41 different diffusion-sensitizing gradient directions, and one baseline image acquired without diffusion weighting.</li>
<li>While I have 3 images’ files for each sequence parameters:</li>
<li>1 file contains the baseline image (b0)</li>
<li>1 file contains the DW images</li>
<li>1 file contains the T2 images that we want to use for selecting the ROI.<br>
I read about image registrations and masking on the Q&amp;A page, but I get confused, there are too many topics and I don’t know which one suits my data. So, can anyone tell me the steps (in order) I should follow to prepare my data for FN tractography?</li>
</ul>
<p>Attached is a screenshot of my files.</p>
<p>Best regards<br>
Mohammed</p>

---

## Post #2 by @pieper (2020-10-22 18:10 UTC)

<p>Hi <a class="mention" href="/u/mohammed_alahmari">@Mohammed_Alahmari</a> -</p>
<p>Unfortunately it looks like you may only have a partial dataset and there’s not much you can do until you get ahold of some more information.  I’ll give you some hints, but the field of diffusion imaging has a lot of “gotcha” issues that make it very hard to work with data unless you are very familiar with exactly how it was produced (what software and what conventions were used).</p>
<p>If the file marked “DWI” is a raw diffusion weighted scan, then you would need to have the <code>bvals</code> and <code>bvecs</code> files in order to interpret it for tractography.</p>
<p>The fact that it’s got <code>DTI</code> in the filename indicates it may already be estimated tensor voxels, in which case you may be able to load and work with it (try to open it in Slicer and if it’s a tensor it may load, but still may not be correct because conventions vary about how tensors are represented in nii files).</p>
<p>If the file is DTI tensors, then there’s a good chance you can load it and do tractography.  If not, you need to go back and trace the history of the data.  Best if you can start with the dicom.</p>

---

## Post #3 by @Mohammed_Alahmari (2020-10-22 19:33 UTC)

<p>Hi Steve,</p>
<p>Thanks for your reply,</p>
<p>I know it is challenging, especially for someone who is unfamiliar with the field. But, with your hints and the support of the slicer community, I hope to overtake the challenge and enjoy learning something new; )</p>
<p>So sorry, I have also the bvals and bvecs files, I thought they are not necessary.</p>
<p>To be honest, I also do not know if the file I have is DWI or DTI. I guess it is a DTI, I attached the protocol for you to check. I also attached a capture of the files I have.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43312035627389ce266ee32c725063a046ddb786.jpeg" data-download-href="/uploads/short-url/9Apf0BoUcGsuqv7u6lEViCgF3XU.jpeg?dl=1" title="files that I have" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43312035627389ce266ee32c725063a046ddb786_2_690x107.jpeg" alt="files that I have" data-base62-sha1="9Apf0BoUcGsuqv7u6lEViCgF3XU" width="690" height="107" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43312035627389ce266ee32c725063a046ddb786_2_690x107.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43312035627389ce266ee32c725063a046ddb786.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43312035627389ce266ee32c725063a046ddb786.jpeg 2x" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">files that I have</span><span class="informations">1005×157 28.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/806bb8a27e95ab783796f4ec39c74b49a3d0c749.jpeg" data-download-href="/uploads/short-url/ik3UhUWymWEvtWPgj8apxXS4Ro5.jpeg?dl=1" title="protocol" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/806bb8a27e95ab783796f4ec39c74b49a3d0c749_2_188x500.jpeg" alt="protocol" data-base62-sha1="ik3UhUWymWEvtWPgj8apxXS4Ro5" width="188" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/806bb8a27e95ab783796f4ec39c74b49a3d0c749_2_188x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/806bb8a27e95ab783796f4ec39c74b49a3d0c749_2_282x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/806bb8a27e95ab783796f4ec39c74b49a3d0c749_2_376x1000.jpeg 2x" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">protocol</span><span class="informations">392×1039 98.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/951b46360f7dff354c1b6ee1ab41f0c060feda14.jpeg" data-download-href="/uploads/short-url/lh3zPzZO12PuD0vLkrZMuOCS2BC.jpeg?dl=1" title="protocol_" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/951b46360f7dff354c1b6ee1ab41f0c060feda14_2_189x500.jpeg" alt="protocol_" data-base62-sha1="lh3zPzZO12PuD0vLkrZMuOCS2BC" width="189" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/951b46360f7dff354c1b6ee1ab41f0c060feda14_2_189x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/951b46360f7dff354c1b6ee1ab41f0c060feda14_2_283x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/951b46360f7dff354c1b6ee1ab41f0c060feda14.jpeg 2x" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">protocol_</span><span class="informations">363×957 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e3c726b350ba7b0367bb8f93c2fa553cad78704.jpeg" data-download-href="/uploads/short-url/mzOWJv0eiMaMi14aBXlNIcJEaKE.jpeg?dl=1" title="protocol__" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e3c726b350ba7b0367bb8f93c2fa553cad78704_2_301x500.jpeg" alt="protocol__" data-base62-sha1="mzOWJv0eiMaMi14aBXlNIcJEaKE" width="301" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e3c726b350ba7b0367bb8f93c2fa553cad78704_2_301x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e3c726b350ba7b0367bb8f93c2fa553cad78704.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e3c726b350ba7b0367bb8f93c2fa553cad78704.jpeg 2x" data-dominant-color="EFF0EF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">protocol__</span><span class="informations">435×722 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best regards<br>
Mohammed</p>

---

## Post #4 by @pieper (2020-10-22 19:49 UTC)

<p>Okay, yes, if you have the <code>bvals</code> and <code>bvecs</code> files then it should be DWI (the original gradient images).  The latest versions of dcm2niix should be able to convert nii to nrrd in this case, and the converted nrrd should load in Slicer for use with SlicerDMRI.  I’m not sure where the latest features are documented, but <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> or <a class="mention" href="/u/tbillah">@tbillah</a> should be able to give some pointers.</p>
<aside class="quote no-group" data-username="Mohammed_Alahmari" data-post="3" data-topic="14202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alahmari/48/8552_2.png" class="avatar"> Mohammed_Alahmari:</div>
<blockquote>
<p>I hope to overtake the challenge and enjoy learning something new; )</p>
</blockquote>
</aside>
<p>That’s the spirit!</p>

---

## Post #5 by @Mohammed_Alahmari (2020-10-22 19:55 UTC)

<p>Much appreciated Steve!</p>

---

## Post #6 by @tbillah (2020-10-23 22:31 UTC)

<p>Hello all,</p>
<p>With whatever command you have for <code>dcm2niix</code>, just use <code>-e</code> additionally to get NRRD directly from DICOM. <a href="https://github.com/rordenlab/dcm2niix#running" rel="noopener nofollow ugc"><code>dcm2niix</code> help message</a> can be consulted for its use.</p>
<p>However, if you are trying to convert NIFTI to NRRD, use <a href="https://github.com/pnlbwh/conversion#introduction" rel="noopener nofollow ugc"><code>nhdr_write.py</code></a>.</p>

---
