---
topic_id: 1333
title: "Head Ct Mri Fusion Registration"
date: 2017-10-31
url: https://discourse.slicer.org/t/1333
---

# Head CT MRI fusion/registration

**Topic ID**: 1333
**Date**: 2017-10-31
**URL**: https://discourse.slicer.org/t/head-ct-mri-fusion-registration/1333

---

## Post #1 by @NaglisR (2017-10-31 15:13 UTC)

<p>Hi everyone, I have only recently started using 3D Slicer and have a rather specific question:<br>
I am trying to fuse the images of the same person head MRI and CT scans. I have tried the general registration (BRAINS) module, which works but the results are not yet satisfactory. Therefore I want to find out if this task is overall manageable and if so, what are the best ways/modules to do so?<br>
Thanks</p>

---

## Post #2 by @pieper (2017-10-31 15:28 UTC)

<p>I’d suggest starting with the material here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Registration/RegistrationLibrary" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Registration/RegistrationLibrary</a></p>

---

## Post #3 by @lassoan (2017-11-01 12:54 UTC)

<p>I find that <strong>General Registration (Elastix)</strong> module often works much better and usually it doesn’t require any parameter tuning. The module will show up in Registration category after you install <strong>SlicerElastix extension</strong>.</p>

---

## Post #4 by @Amir_Zolal (2017-12-02 06:07 UTC)

<p>Hello,</p>
<p>this is a very important registration step for instance in verifying the<br>
results of DBS lead implantation by superimposing the postop CT onto the<br>
preop T1 / T2 / SWI etc. However, none of the common registration method<br>
work well (with the exception of Brainlab - but then, export and further<br>
analysis with another tool is not possible). I tried flirt, ants, elastix<br>
(SlicerElastix extension, as you suggested Andras), I think that the strong<br>
contrast on the tissue-air-interface in CT causes the problem. I ended up<br>
using landmark registration in MIPAV, but thats far from optimal.</p>
<p>Did anyone find a way how to perform a fast rigid registration of CT to T1<br>
MRI with acceptable results?</p>
<p>And - St. P. the registration library doesn’t have an example for this case.</p>
<p>Thanks,</p>
<p>Amir</p>

---

## Post #5 by @lassoan (2017-12-02 06:16 UTC)

<p>Elastix worked really well for me for any reasonable registration problem that I threw at it. If you use a suitable metric (such as mutual information), then strong<br>
contrast on the tissue-air-interface in CT should just help the registration . What kind of registration error did you have? Can you share a data set where you have registration issues?</p>
<p>Note that there are great rigid/affine/deformable landmark registration modules in Slicer. For images that are already somewhat aligned you can use <code>Landmark registration</code> module. For general cases, you can use <code>Fiducial registration wizard</code> module in SlicerIGT extension.</p>

---

## Post #6 by @lassoan (2017-12-02 06:28 UTC)

<aside class="quote no-group" data-username="Amir_Zolal" data-post="4" data-topic="1333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amir_zolal/48/9423_2.png" class="avatar"> Amir_Zolal:</div>
<blockquote>
<p>this is a very important registration step for instance in verifying the results of DBS lead implantation by superimposing the postop CT onto the preop T1 / T2 / SWI etc.</p>
</blockquote>
</aside>
<p>Registration of pre/post-op images of a same patient is a single-step intra-patient registration - should be quite easy.</p>
<p>Do I understand correctly that you register pre/post-op images to each other by registering each to an atlas? That would not be ideal, as you need to register twice (instead of just once), and inter-patient (patient-to-atlas) registration is a much more difficult problem than intra-patient registration.</p>

---

## Post #7 by @Amir_Zolal (2017-12-02 07:53 UTC)

<p>Yes, you understand correctly, I register pre and post op images to each<br>
other, the postop images have the electrodes in them (which might be a part<br>
of the problem). Is there a way to modify the parameters of elastix<br>
directly in SlicerElastix or load a different parameter set other than the<br>
presets?</p>
<p>I can also share the data (if you have the time to help), just tell me the<br>
preferred way and I will send the files.</p>
<p>A</p>

---

## Post #8 by @lassoan (2017-12-02 14:54 UTC)

<p>To modify Elastix registration parameters, open <code>Advanced</code> section and click <code>Show database folder</code> button. It should show the registration preset database folder. You can edit ElastixParameterSetDatabase.xml to add new presets (name, description, etc. and a list of registration steps) and edit/add .txt files to edit registration steps.</p>
<p>If you upload a set of images to dropbox, onedrive, google drive, … and post the link here then I can have a quick look</p>

---

## Post #9 by @Amir_Zolal (2017-12-02 17:32 UTC)

<p>These are the files,</p>
<p>preop T1 and postop CT</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/ypmhr7yjlnq6k10/CTMRIReg.tar.xz?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/ypmhr7yjlnq6k10/CTMRIReg.tar.xz?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/ypmhr7yjlnq6k10/CTMRIReg.tar.xz?dl=0" target="_blank" rel="noopener nofollow ugc">CTMRIReg.tar.xz</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks for the help Andras!</p>
<p>Amir</p>

---

## Post #10 by @lassoan (2017-12-03 02:26 UTC)

<p>Thank you, I had a look at the images and indeed registration is not trivial. Probably the best would be to do a literature review to see how others have approached this task before, but here are a few ideas that you may try:</p>
<ul>
<li>If you want to make sure that the brain is registered correctly then skull stripping (removing the skull from images) may help. For MRI images, you can use SwissSkillStripper extension (or ROBES or SkullStripper). For CT images, you may use SwissSkullStripper extension, too, but use a CT instead of an MRI as atlas volume. You can use any head CT and corresponding brain labelmap image.</li>
<li>You may improve initial registration by landmark registration (either using <code>Landmark registration</code> module; or <code>Fiducial registration wizard</code> module in SlicerIGT extension). Then, use a registration optimizer that can restrict maximum translation and rotation to make sure it finds solution around the initial guess.</li>
<li>Check out Elastix parameter file database (<a href="http://elastix.bigr.nl/wiki/index.php/Parameter_file_database">http://elastix.bigr.nl/wiki/index.php/Parameter_file_database</a>)</li>
<li>Check out Slicer <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">registration case library</a> and <a href="https://www.slicer.org/wiki/Documentation/4.8/FAQ/Registration">Registration FAQ</a>
</li>
</ul>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> have you registered these kind of images in the past? Would you have any suggestions?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d28d45c4e0c293ce3598eaccf8b66037d11e1e.jpeg" data-download-href="/uploads/short-url/g64A4Yu59bIjJg5ONI1EBwLODsq.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/70d28d45c4e0c293ce3598eaccf8b66037d11e1e_2_689x477.jpg" alt="image" data-base62-sha1="g64A4Yu59bIjJg5ONI1EBwLODsq" width="689" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/70d28d45c4e0c293ce3598eaccf8b66037d11e1e_2_689x477.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/70d28d45c4e0c293ce3598eaccf8b66037d11e1e_2_1033x715.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d28d45c4e0c293ce3598eaccf8b66037d11e1e.jpeg 2x" data-dominant-color="414141"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1240×858 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @eeros (2017-12-03 07:30 UTC)

<p>Hi,<br>
I have registered this kind of images and I tried the registration using<br>
your data. After I  increased the percentage of samples from 0.002 to 0.02<br>
I got the results show in the attached screen capture. Is this registration<br>
good enough or what kind of problems did you mean? I used General<br>
Registration (BRAINS) modules of Slicer 4.8.</p>
<p>Most important parameters:<br>
Fixed Image: T1<br>
Moving Image Volume; CT<br>
Percentage of samples: 0.02<br>
Output settings: Slicer linear transform<br>
Initialization: None/off<br>
Registration phases: RIgid (6 DOF)<br>
Cost Metric: MMI</p>
<p>To still increase the registration accuracy (if needed)  I would try to<br>
mask the registration to that part of the brain where the electrodes of<br>
interest are located.<br>
​</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d85f09b6f885836aa1068e366b83de9bc573fa28.png" data-download-href="/uploads/short-url/uS6KAHar6MUmZq4msHQYSpIBAYo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d85f09b6f885836aa1068e366b83de9bc573fa28_2_690x303.png" alt="image" data-base62-sha1="uS6KAHar6MUmZq4msHQYSpIBAYo" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d85f09b6f885836aa1068e366b83de9bc573fa28_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d85f09b6f885836aa1068e366b83de9bc573fa28_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d85f09b6f885836aa1068e366b83de9bc573fa28_2_1380x606.png 2x" data-dominant-color="484848"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1389×611 398 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @ihnorton (2017-12-03 15:33 UTC)

<p><a class="mention" href="/u/eeros">@eeros</a> looks good!</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> the volume of disturbed area is very small relative to the total head volume, so I have usually been able to register these kind of images in BRAINSFit with just manual initialization and some parameter fiddling like this (the commercial navigation system we use in AMIGO works out of box for these kind of images – my recollection is that they use some variation on AIR).</p>

---

## Post #14 by @Amir_Zolal (2017-12-03 18:50 UTC)

<p>Hi,</p>
<p>I have tested increasing the samples percentage, which worked in that<br>
particular case, looks really like some “fiddling” is necessary.  In some<br>
other cases, I didn’t succeed, even with masking of the electrodes. All<br>
very work intensive.</p>
<p>Interestingly, Brainlab has a very robust solution - in neurosurgery, CT-MR<br>
registrations are necessary on … weekly, not daily … but still regular<br>
basis.  Does anybody have any knowledge of what algorithm they use?</p>
<p>Thanks in advance,</p>
<p>Amir</p>

---

## Post #15 by @pieper (2017-12-04 13:15 UTC)

<p>I’d also suggest trying DRAMMS - it has worked well on many different registration scenarios:</p>
<p><a href="http://www.med.upenn.edu/sbia/dramms.html" class="onebox" target="_blank">http://www.med.upenn.edu/sbia/dramms.html</a></p>

---

## Post #16 by @kopachini (2019-01-15 18:29 UTC)

<p>Hello everyone,</p>
<p>is it possible to make fusion of 3 studies (arterial, venous and late excretion phase in CT urography)? And than after the fusion where I will have arteries, veins and calices and ureters in one place to make segmentation of each part as done normally without fusion?</p>
<p>And a practical question, if I want to make a fusion of the one part of the abdomen (kidneys) should I first crop every study separately or when studies are fused together?</p>

---

## Post #17 by @kopachini (2019-01-15 19:35 UTC)

<p>And I have issue with registration of the images.<br>
When I want to chose moving image volume, only one study appears (bone CT scan), there is no MR study that I have loaded together with bone study as seen on the pic.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e813e83ee54f85a8c7b07fc479a46520c6333f18.jpeg" data-download-href="/uploads/short-url/x73qipstLZoHzfXbkD2gxVcw8Wc.jpeg?dl=1" title="fusion1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e813e83ee54f85a8c7b07fc479a46520c6333f18_2_689x374.jpeg" alt="fusion1" data-base62-sha1="x73qipstLZoHzfXbkD2gxVcw8Wc" width="689" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e813e83ee54f85a8c7b07fc479a46520c6333f18_2_689x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e813e83ee54f85a8c7b07fc479a46520c6333f18_2_1033x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e813e83ee54f85a8c7b07fc479a46520c6333f18.jpeg 2x" data-dominant-color="C6C7D9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fusion1</span><span class="informations">1196×650 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>intel core i7 7700HQ 2.80 GHz<br>
16GB RAM<br>
64x operating system<br>
Windows 10 Home</p>

---

## Post #18 by @pieper (2019-01-15 21:55 UTC)

<p>Hi <a class="mention" href="/u/kopachini">@kopachini</a> -</p>
<p>Regarding the registration of multiple phases, yes it will probably work.  You’ll just need to experiment.</p>
<p>Not sure exactly what you are asking regarding the cropping.  You can crop the volumes either before or after transforming them.  You might want to crop just the kidney to make registration more accurate and quicker.</p>
<p>Regarding the MR not showing in the selector, it’s probably not a scalar volume.  Perhaps it loaded as a diffusion or multivolume.</p>

---

## Post #19 by @kopachini (2019-01-16 18:57 UTC)

<p>I solved that problem… issue was that I tried to load two studies at once and then the second study was loaded as multivolume. when I loaded one study at the time, I continued without a problem.</p>
<p>Only, I had the idea of fusion a bit different… I thought that when I make fusion before segmentation, when I start to segment I will have two phases or MR times on one stack combined, but there are still two separate phases that I need to change in between. But nevermind, that works, too <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #20 by @lassoan (2019-01-17 05:44 UTC)

<p>You can display two frames at a time (one as background, another one as foreground volume) and fade between them. Basic Slicer visualization tutorials should cover this, but if not then let us know and we give step-by-step instructions.</p>

---

## Post #21 by @kopachini (2019-01-17 19:14 UTC)

<p>Thank you for reply. I manage that as well as segmentation of different anatomical structures on two fused studies. I wanted to say that in my head I thought that when I make fusion of two studies they will appear as merged into only one… but process of fading  works just fine, too <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I didn’t tried to fuse 3 different studies (don’t have idea how to do it)</p>

---

## Post #22 by @Saima (2019-10-23 05:30 UTC)

<p>Hi Andras,<br>
swiss skull stripper not giving good results. some portion of the brain is missed by it. what can I use instead of this or is there a way to change the parameters of the algorithm it is using</p>
<p>thanks</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #23 by @lassoan (2019-10-23 13:33 UTC)

<p>You can create your own atlas and mask image that better represents your patient population.</p>

---

## Post #24 by @mubafz (2021-06-24 15:51 UTC)

<p>Hi Amir,</p>
<p>Did you end up working out whats the best way in Slicer for pre-implant MRI/Post-op for precise registration.</p>
<p>I am just browsing through looking for info on this and came across this three year old thread.</p>
<p>Regards,<br>
M</p>

---

## Post #25 by @lassoan (2021-06-25 22:01 UTC)

<p>Many things have changed in the past 2-3 years. Therefore, instead of reviving an old thread, it may be better to start a new one. Describe your high-level goal, the specific problem you have, and provide images (at least screenshots).</p>

---

## Post #26 by @Ella1 (2022-08-25 19:31 UTC)

<p>This link is not active anymore.<br>
I mean when I click on any file in the download section, Error 404 has appeared.<br>
Would you provide another link?<br>
Thanks</p>

---

## Post #27 by @Atefeh.Zeinoddini (2025-05-07 00:56 UTC)

<p>Hi, Do you have suggestion for robust registration of CT and MRI? I am looking for a preferably free software, do you have recommendations? many thanks</p>

---

## Post #28 by @mikebind (2025-05-07 17:06 UTC)

<p>In my experience <a href="https://github.com/ANTsX/ANTs" rel="noopener nofollow ugc">ANTs</a> works very well for this, and is available in Slicer through the extension <a href="https://github.com/netstim/SlicerANTs" rel="noopener nofollow ugc">SlicerANTs</a>.  It has many settings for deformable registration, but if you just want to do rigid registration, the “Rigid” preset works well. You will need to read enough to understand and make a selection in the Initial Moving Transform section and understand Slicer enough to apply the resulting transform or view the generated transformed image volume.</p>

---
