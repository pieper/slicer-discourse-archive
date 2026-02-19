---
topic_id: 13963
title: "Trajectory Calculation For Stereotaxic Frames"
date: 2020-10-09
url: https://discourse.slicer.org/t/13963
---

# Trajectory calculation for stereotaxic frames

**Topic ID**: 13963
**Date**: 2020-10-09
**URL**: https://discourse.slicer.org/t/trajectory-calculation-for-stereotaxic-frames/13963

---

## Post #1 by @Gaston (2020-10-09 20:18 UTC)

<p>Good morning, Maybe you can help me. I am looking for an extension or a method that allows to calculate coordinates and angle of a trajectory between an input point and a target point.<br>
To be able to be used in stereotactic frames.</p>

---

## Post #2 by @lassoan (2020-10-10 00:19 UTC)

<p>Angle computation from point coordinates is fairly straightforward. How far did you get and what step you are stuck at?</p>
<p>What is your workflow? How do you register your stereotactic frame coordinate system to your image coordinate system?</p>

---

## Post #3 by @Gaston (2020-10-12 14:35 UTC)

<p>Dear Andras, the stereotactic frame, is brand crw.  Regarding where I got stuck, it is at the beginning.  I would like to know if there is an easy procedure to do this in slicer. Thanks</p>

---

## Post #4 by @lassoan (2020-10-12 14:52 UTC)

<p>Whatever you want to do should be easily doable, as Slicer has a wide range of calibration, registration, planning, and visualization tools for stereotactic surgery. If you can describe what your intended workflow then we can tell how to implement it in Slicer. For example, what imaging do you do, how do you identify target position, do you use a localizer frame to determine the head ring position or identify landmarks on the ring, do you have a computational model of the stereotactic system (position of rotation and translation axes, relative to landmarks or localizer frame, or this model is yet to be built), …?</p>

---

## Post #5 by @Gaston (2020-10-13 19:29 UTC)

<p>Hello Andras, thank you very much for answering.<br>
The images we use are MRI and CT<br>
We use a frame of reference during imaging procedures.<br>
Then with the frame references we calculate the center, and then we calculate the coordinates of the target with respect to the center.<br>
I do not currently have a computational model of the stereotaxic system.</p>

---

## Post #6 by @JBeninca (2021-04-08 10:34 UTC)

<p>Hello. I ´ve been working for a while in a project like you describe.<br>
it´s applied to a Micromar Stereotactic device,which has its fiducials in 90o angles.<br>
It has 2 versions: one with just the fiducial calculus for registration and a second one with some graphic functions, objects, that show where de the arc an biopsy needle are in the brain.<br>
it was published in a medical journal.: <a href="http://neurotarget.com/numero.php?idn=30" class="inline-onebox" rel="noopener nofollow ugc">Revista NeuroTarget | Vanguardia en Neurociencia</a></p>
<p>in page 37.-<br>
Please tell me if its the kind of software you are looking for.- Thanks</p>

---

## Post #7 by @JBeninca (2021-04-10 15:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c235dbfc74412908b54f5a31618f0f98f740a5cd.jpeg" data-download-href="/uploads/short-url/rI41nPQLE2XONTAK02pCVLBEpsN.jpeg?dl=1" title="Figura_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c235dbfc74412908b54f5a31618f0f98f740a5cd_2_618x500.jpeg" alt="Figura_3" data-base62-sha1="rI41nPQLE2XONTAK02pCVLBEpsN" width="618" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c235dbfc74412908b54f5a31618f0f98f740a5cd_2_618x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c235dbfc74412908b54f5a31618f0f98f740a5cd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c235dbfc74412908b54f5a31618f0f98f740a5cd.jpeg 2x" data-dominant-color="A58F9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figura_3</span><span class="informations">756×611 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-04-14 15:07 UTC)

<p>This looks nice, thanks for sharing. Is it open-source? If yes, the you could consider submitting to the extensions index so that users can find it more easily.</p>

---

## Post #9 by @JBeninca (2021-04-15 10:04 UTC)

<p>hello. Yes, it´s open source.<br>
it is a scripted widget.- I don t know if it has to be written in C or something like that.<br>
I ask you for some advice on how to publish it.</p>

---

## Post #10 by @pieper (2021-04-15 11:20 UTC)

<aside class="quote no-group" data-username="JBeninca" data-post="9" data-topic="13963">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jbeninca/48/10039_2.png" class="avatar"> JBeninca:</div>
<blockquote>
<p>I ask you for some advice on how to publish it.</p>
</blockquote>
</aside>
<p>Scripted is fine for an extension.  The steps linked below describe how to make a formal extension.  There are several steps involved and there’s a general expectation you’ll be available to answer questions and do some maintenance from time to time (e.g. if Slicer core changes).  If you don’t want to sign up for that you can just make your code available online, perhaps in github, and post a link here so it can be an example for future developers.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html</a></p>

---

## Post #11 by @JBeninca (2021-05-20 20:55 UTC)

<p>Hi, we´had developed a module that calculates the target and path of stereotatic frames.<br>
you can get it here:</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">

      <a href="https://github.com/JBeninca/SlicerStereotaxia" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://repository-images.githubusercontent.com/360472023/5852fc00-a340-11eb-82bc-894727422c5f" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/JBeninca/SlicerStereotaxia" target="_blank" rel="noopener nofollow ugc">JBeninca/SlicerStereotaxia</a></h3>


  <p><span class="label1">Slicer stereotatic frame 3D coordinates calculus.-</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>in fact, there are 2 modules, one with graphics and the other without.<br>
in our hospital we use it with a Micromar frame, that has the fiducials with 90° degrees., but you can adapt it .</p>

---

## Post #12 by @lassoan (2021-05-21 04:14 UTC)

<p>Very nice! Would you could consider submitting this to the extensions index so that users can more easily find and install it?</p>

---

## Post #13 by @Glenn (2021-09-29 09:01 UTC)

<aside class="quote no-group" data-username="JBeninca" data-post="11" data-topic="13963">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jbeninca/48/10039_2.png" class="avatar"> JBeninca:</div>
<blockquote>
<p>JBeninca/SlicerStereotaxia</p>
</blockquote>
</aside>
<p>Hello, I am particularly interested in your extension, but I can’t install it. Can you give me some guidance?thanks。</p>

---

## Post #14 by @JBeninca (2021-09-29 18:27 UTC)

<p>Let me see. I need 2-3 days. Thanks</p>

---

## Post #15 by @Glenn (2021-09-30 03:39 UTC)

<p>ok，I am looking forward to your guidance,</p>
<p>thank you fou your reply.! <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=10" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #16 by @JBeninca (2021-10-07 11:48 UTC)

<p>hi, sorry for delay.-</p>
<p>to get the modules working you must:</p>
<p>1- download zip from   <a href="https://github.com/JBeninca/SlicerStereotaxia" class="inline-onebox" rel="noopener nofollow ugc">GitHub - JBeninca/SlicerStereotaxia: Slicer stereotatic frame 3D coordinates calculus.-</a></p>
<p>2 - unzip and move to:  /where_you_want_directory</p>
<p>3 - open 3DSlicer</p>
<p>4 - Edit-&gt; Applications settings → Modules → additional module path → Add</p>
<p>5 - select: /where_you_want_directory</p>
<p>6 - restart 3DSlicer</p>
<p>7 - you will find the 2 new modules in “Stereotaxia”</p>
<p>there is a paciente.nrrd file for example.</p>
<p>have luck.-</p>
<p>thanks . Jorge.-</p>

---

## Post #17 by @JBeninca (2021-10-07 11:49 UTC)

<p>I´m actually using 3DSlicer version 4.11.20210226</p>

---

## Post #18 by @slicer365 (2021-10-07 12:45 UTC)

<p>Actually it also works well in Slicer 4.13.</p>
<p>However，I don’t know how to use it，could you help provide more tutorial or a video?</p>

---

## Post #19 by @Xestance (2022-01-01 07:49 UTC)

<p>Dear All<br>
Greetings. I am a new member of the 3d slicer community and i wish to ask can i use 3d slicer solely for stereotactic procedures starting from image fusion between more than 2 images and target localization up to fiducial marking for entry and target.<br>
I am using both crw and brw frames</p>
<p>Thanks alot. Yours</p>

---

## Post #20 by @Greydon_Gilmore (2022-01-01 20:39 UTC)

<p><a class="mention" href="/u/xestance">@Xestance</a> <a class="mention" href="/u/gaston">@Gaston</a> <a class="mention" href="/u/slicer365">@slicer365</a> <a class="mention" href="/u/glenn">@Glenn</a></p>
<p>I have been developing an extension for stereotactic planning that supports Leksell, BRW, and CRW frames. This extension allows pre-op planning (with coordinates in ACPC and frame space), visualization of intraop MER, post-op electrode localization, and VTA modelling.</p>
<p>The documentation site (WIP): <a href="http://trajectoryguide.greydongilmore.com/" rel="noopener nofollow ugc">trajectoryguide.greydongilmore.com/</a></p>
<p>Let me know if you’d be interested in trying it out.</p>
<p>Greydon</p>

---

## Post #21 by @Xestance (2022-01-02 06:36 UTC)

<p>Yes sir im interested in it.</p>

---

## Post #22 by @Xestance (2022-01-04 17:55 UTC)

<p>I have checked the documentation site it is very promising… and I hope to try the module. thanks a lot</p>

---

## Post #23 by @Michele_Bailo (2022-01-08 12:04 UTC)

<p>Thanks for your efforts! I would incredibly interested too!<br>
As a neurosurgeon I routinely prepare preplanning using 3D Slicer first, but then I always have to export the trajectories as RTstructures (basically using a workaround) to import them again in the Leksell Surgiplan software and obtain the final stereotactic coordinates.</p>
<p>MB</p>

---

## Post #24 by @JBeninca (2022-01-23 00:31 UTC)

<p>this is a simple video. Stereotaxia_lite.<br>
you can use the “paciente,nrrd” sample.<br>
link : <a href="https://youtu.be/g5YCd2nOIa0" rel="noopener nofollow ugc">https://youtu.be/g5YCd2nOIa0</a></p>

---

## Post #25 by @jfdoarias (2022-03-14 00:34 UTC)

<p>Thanks a lot, great work, I would like to use this in my surgeries… Can I get this module?, this is a very useful module, thanks again.</p>

---

## Post #26 by @JBeninca (2022-04-01 14:33 UTC)

<p>hi. you can get ti from here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/JBeninca/SlicerStereotaxia">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/JBeninca/SlicerStereotaxia" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:547/500;"><img src="https://repository-images.githubusercontent.com/360472023/5852fc00-a340-11eb-82bc-894727422c5f" class="thumbnail" width="547" height="500"></div>

<h3><a href="https://github.com/JBeninca/SlicerStereotaxia" target="_blank" rel="noopener nofollow ugc">GitHub - JBeninca/SlicerStereotaxia: Slicer stereotatic frame 3D coordinates...</a></h3>

  <p>Slicer stereotatic frame 3D coordinates calculus.- - GitHub - JBeninca/SlicerStereotaxia: Slicer stereotatic frame 3D coordinates calculus.-</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>its free, it takes some time to understand and manage but works fine</p>
<p>we use actually in every stereotatic surgery in hospital. with the Micromar device</p>

---

## Post #27 by @jfdoarias (2022-05-30 19:30 UTC)

<p>Thanks a lot!, I will try it!</p>

---

## Post #29 by @Gonzalo_Rojas_Costa (2022-05-31 19:55 UTC)

<p>How can install JBeninca/SlicerStereotaxia in 3D Slicer?</p>

---

## Post #30 by @JBeninca (2022-06-03 14:16 UTC)

<p>to get the modules working you must:</p>
<p>1- download zip from <a href="https://github.com/JBeninca/SlicerStereotaxia" rel="noopener nofollow ugc">GitHub - JBeninca/SlicerStereotaxia: Slicer stereotatic frame 3D coordinates calculus.- </a></p>
<p>2 - unzip and move to: /where_you_want_directory</p>
<p>3 - open 3DSlicer</p>
<p>4 - Edit-&gt; Applications settings → Modules → additional module path → Add</p>
<p>5 - select: /where_you_want_directory</p>
<p>6 - restart 3DSlicer</p>
<p>7 - you will find the 2 new modules in “Stereotaxia”</p>
<p>there is a paciente.nrrd file for example.</p>
<p>have luck.-</p>

---

## Post #31 by @JBeninca (2022-06-03 19:57 UTC)

<p>it´s not empty:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/JBeninca/SlicerStereotaxia">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/JBeninca/SlicerStereotaxia" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:547/500;"><img src="https://repository-images.githubusercontent.com/360472023/5852fc00-a340-11eb-82bc-894727422c5f" class="thumbnail" width="547" height="500"></div>

<h3><a href="https://github.com/JBeninca/SlicerStereotaxia" target="_blank" rel="noopener nofollow ugc">GitHub - JBeninca/SlicerStereotaxia: Slicer stereotatic frame 3D coordinates...</a></h3>

  <p>Slicer stereotatic frame 3D coordinates calculus.- - GitHub - JBeninca/SlicerStereotaxia: Slicer stereotatic frame 3D coordinates calculus.-</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #32 by @lassoan (2022-06-19 03:09 UTC)

<p><a class="mention" href="/u/jbeninca">@JBeninca</a> Could we add this extension to the Extensions Manager so that users don’t need to go through the trouble of downloading, unzipping, editing settings, etc. but can install the extension using a single click?</p>

---

## Post #33 by @JBeninca (2022-06-19 20:59 UTC)

<p>Yes, of course. I don t have the time to do that. Thanks</p>

---

## Post #34 by @lassoan (2022-06-22 17:26 UTC)

<p>Thank you, I’ve tested your modules and they work very nicely. I’ve submitted a pull request that makes the extension compatible with the Extensions Manager. There are just 3 small things to do on your side to allow your extension to appear in the Extensions manager:</p>
<ul>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> Merge this pull request: <a href="https://github.com/JBeninca/SlicerStereotaxia/pull/1" class="inline-onebox">Fix extension packaging by lassoan · Pull Request #1 · JBeninca/SlicerStereotaxia · GitHub</a>
</li>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> Associate the repository with <code>3d-slicer-extension</code> GitHub topic so that it is listed <a href="https://github.com/topics/3d-slicer-extension">here</a>. To edit topics, click the settings icon in the right side of “About” section header and enter <code>3d-slicer-extension</code> in “Topics” and click “Save changes”. To learn more about topics, read <a href="https://help.github.com/en/articles/about-topics" class="inline-onebox">Classifying your repository with topics - GitHub Docs</a>
</li>
<li>
<span class="chcklst-box checked fa fa-check-square-o fa-fw"></span> Add a LICENSE.md file. I would recommend to choose the permissive <a href="https://choosealicense.com/licenses/mit/">MIT license</a>.</li>
</ul>
<p>Thank you for your contribution!</p>

---

## Post #35 by @JBeninca (2022-06-24 20:23 UTC)

<p>Hello.</p>
<p>I have already made the requested changes and the repository is ready.</p>
<p>Please let me know when I can try to install the module.</p>

---

## Post #36 by @lassoan (2022-06-25 03:47 UTC)

<p>I’ve submitted the s4ext file to the ExtensionsIndex repository, so the extension may be available in the Extensions Manager from tomorrow.</p>

---

## Post #37 by @lassoan (2022-06-25 16:18 UTC)

<p>The Stereotaxia extension is now available in the Extensions manager:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ae9cb349591b2b379f5eeb409bd245cadffd011.jpeg" data-download-href="/uploads/short-url/m6qqJTlVWRYYxAyHBVByKS6Kl4l.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae9cb349591b2b379f5eeb409bd245cadffd011_2_690x443.jpeg" alt="image" data-base62-sha1="m6qqJTlVWRYYxAyHBVByKS6Kl4l" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae9cb349591b2b379f5eeb409bd245cadffd011_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae9cb349591b2b379f5eeb409bd245cadffd011_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ae9cb349591b2b379f5eeb409bd245cadffd011_2_1380x886.jpeg 2x" data-dominant-color="CDD4D5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1233 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you make any changes/improvements in the extension it is automatically made available to users the next day.</p>

---

## Post #38 by @Gaston (2022-06-25 20:17 UTC)

<p>Hi I have slicer 5.0.2 for osx and I can’t see in the extension manager the stereotype extension.</p>

---

## Post #39 by @lassoan (2022-06-26 00:25 UTC)

<p>The name of the extension is Stereotaxia. The extension was submitted quite late yesterday, so probably on macOS it did not arrive in time. It is available already in the Slicer Preview Release (rev 31069) and it should be available in the Slicer Stable Release tomorrow.</p>

---

## Post #40 by @JBeninca (2022-07-04 13:20 UTC)

<p>thanks again Andras. How do i know if it is used?.</p>

---

## Post #41 by @lassoan (2022-07-04 22:39 UTC)

<p>We only know how many times the extension is downloaded (we don’t know how often they use it). You can get these statistics from <code>Extension Download Statistics</code> module of <code>DeveloperToolsForExtensions</code> extension.</p>

---

## Post #42 by @slicer365 (2022-07-25 07:57 UTC)

<p>Is it useful to LekSell  frame?</p>

---

## Post #43 by @JBeninca (2022-07-25 16:33 UTC)

<p>we do use:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://micromar.com/en/aimsystem-stereotactic-system/">
  <header class="source">
      <img src="https://micromar.com/wp-content/uploads/2022/01/favicon-96x96-1.png" class="site-icon" width="" height="">

      <a href="https://micromar.com/en/aimsystem-stereotactic-system/" target="_blank" rel="noopener nofollow ugc" title="10:33PM - 17 January 2022">Micromar – Inspirados pela Vida – 17 Jan 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:665/308;"><img src="https://micromar.com/wp-content/uploads/2022/01/Logo-Micromar-Inspired-By-Life-1.png" class="thumbnail" width="" height=""></div>

<h3><a href="https://micromar.com/en/aimsystem-stereotactic-system/" target="_blank" rel="noopener nofollow ugc">Aimsystem Stereotactic System – Micromar</a></h3>

  <p>The Aimsystem Stereotactic System TM03B, through the principle of Cartesian coordinates (X, Y and Z), reaches targets calculated with great precision.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox wikimedia" data-onebox-src="https://commons.wikimedia.org/wiki/File:Stereotactic_Frame_TM03B_Micromar.jpg">
  <header class="source">

      <a href="https://commons.wikimedia.org/wiki/File:Stereotactic_Frame_TM03B_Micromar.jpg" target="_blank" rel="noopener nofollow ugc">commons.wikimedia.org</a>
  </header>

  <article class="onebox-body">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Stereotactic_Frame_TM03B_Micromar.jpg/500px-Stereotactic_Frame_TM03B_Micromar.jpg" class="thumbnail" width="" height="">

<h3><a href="https://commons.wikimedia.org/wiki/File:Stereotactic_Frame_TM03B_Micromar.jpg" target="_blank" rel="noopener nofollow ugc">File:Stereotactic Frame TM03B Micromar.jpg</a></h3>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>i don´t know if the geometry (of fiducials) are the same.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d310c96fb4b5e74a2545a77a08763730bfd12a7c.png" data-download-href="/uploads/short-url/u7aI8J9hhsduXYjpDvOBQR1cHCc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d310c96fb4b5e74a2545a77a08763730bfd12a7c_2_627x500.png" alt="image" data-base62-sha1="u7aI8J9hhsduXYjpDvOBQR1cHCc" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d310c96fb4b5e74a2545a77a08763730bfd12a7c_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d310c96fb4b5e74a2545a77a08763730bfd12a7c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d310c96fb4b5e74a2545a77a08763730bfd12a7c.png 2x" data-dominant-color="9796AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×552 80.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0c6e47a97b2142f20545c8546e5e42868db7003.png" data-download-href="/uploads/short-url/ym0IwqL1VycygRhmgcWSO8rbM9Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0c6e47a97b2142f20545c8546e5e42868db7003.png" alt="image" data-base62-sha1="ym0IwqL1VycygRhmgcWSO8rbM9Z" width="558" height="500" data-dominant-color="9894CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">623×558 12.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the sides of each square are 140 mm.-<br>
if not, you can modify the soft to get the proper calculations.</p>

---

## Post #44 by @slicer365 (2022-07-26 13:47 UTC)

<p>thank you ! I see, it is different, leksell’s each square is 120mm。</p>

---

## Post #45 by @lassoan (2022-07-26 17:49 UTC)

<p>You can download and locally modify the extension to match your frame. Ideally, you would add a selector to allow choosing the frame.</p>

---

## Post #46 by @JBeninca (2022-08-02 11:38 UTC)

<p>you can change the stereotatic definition in script:</p>
<h2><a name="p-81602-stereotaxiahttpsgithubcomjbenincaslicerstereotaxiatreemainstereotaxiarecursoshttpsgithubcomjbenincaslicerstereotaxiatreemainstereotaxiarecursosmaquina_russell_brownpy-1" class="anchor" href="#p-81602-stereotaxiahttpsgithubcomjbenincaslicerstereotaxiatreemainstereotaxiarecursoshttpsgithubcomjbenincaslicerstereotaxiatreemainstereotaxiarecursosmaquina_russell_brownpy-1" aria-label="Heading link"></a><a href="https://github.com/JBeninca/SlicerStereotaxia/tree/main/Stereotaxia" rel="noopener nofollow ugc">Stereotaxia</a>/<a href="https://github.com/JBeninca/SlicerStereotaxia/tree/main/Stereotaxia/Recursos" rel="noopener nofollow ugc">Recursos</a>/<strong>Maquina_Russell_Brown.py</strong></h2>
<p>there is a class:</p>
<p>class Marco_Micromar():<br>
“”“Clase para encapsular datos del marco MICROMAR TM-03B”“”</p>
<p>which have the 9 points that reference the specific frame .</p>

---

## Post #47 by @jay1987 (2022-08-03 08:58 UTC)

<p>i have some sript error on use trajectoryGuideModules<br>
when i press [Load Data] button ,nothing happen<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46ea56f4383857f85030c7f71a1c3cf4ce301b05.png" data-download-href="/uploads/short-url/a7luAqayCwuPCAfNKFjuGqshCJf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46ea56f4383857f85030c7f71a1c3cf4ce301b05_2_690x263.png" alt="image" data-base62-sha1="a7luAqayCwuPCAfNKFjuGqshCJf" width="690" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46ea56f4383857f85030c7f71a1c3cf4ce301b05_2_690x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46ea56f4383857f85030c7f71a1c3cf4ce301b05_2_1035x394.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46ea56f4383857f85030c7f71a1c3cf4ce301b05_2_1380x526.png 2x" data-dominant-color="585757"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×730 50.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #48 by @jay1987 (2022-08-03 09:26 UTC)

<aside class="quote no-group" data-username="JBeninca" data-post="46" data-topic="13963">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jbeninca/48/10039_2.png" class="avatar"> JBeninca:</div>
<blockquote>
<p>Marco_Micromar(</p>
</blockquote>
</aside>
<p>i change the parameter from 140 to 120 , it’s also not work on leksell frame<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d7bf4f514dcddaf3c510154f0a57e96dedd3d14.jpeg" data-download-href="/uploads/short-url/1VhMzFFXjJMZCCUzwkKnTD0yZQU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d7bf4f514dcddaf3c510154f0a57e96dedd3d14_2_690x252.jpeg" alt="image" data-base62-sha1="1VhMzFFXjJMZCCUzwkKnTD0yZQU" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d7bf4f514dcddaf3c510154f0a57e96dedd3d14_2_690x252.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d7bf4f514dcddaf3c510154f0a57e96dedd3d14_2_1035x378.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d7bf4f514dcddaf3c510154f0a57e96dedd3d14_2_1380x504.jpeg 2x" data-dominant-color="B6B0C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1565×573 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #49 by @JBeninca (2022-08-03 10:28 UTC)

<p>Can you show me how you change the parameters?</p>

---

## Post #50 by @jay1987 (2022-08-03 11:27 UTC)

<p>i just change the parameter from 140 to 120<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e56522e4a17d9caddb4db8d0f154a5edb9720e7.png" alt="image" data-base62-sha1="4knguFzXd2a0XzO6m3pMvjsZ1rx" width="345" height="284"></p>

---

## Post #51 by @Greydon_Gilmore (2022-08-03 23:20 UTC)

<p>To correct some confusion… <a class="mention" href="/u/jay1987">@jay1987</a> is uing my module <strong>trajectoryGuide</strong> and not <strong>Stereotaxia</strong>. <a class="mention" href="/u/jay1987">@jay1987</a> to fix your error you need to first have your dataset in BIDS format: <a href="https://bids.neuroimaging.io/" rel="noopener nofollow ugc">https://bids.neuroimaging.io/</a>.</p>
<p><strong>trajectoryGuide</strong> supports Leksell, BRW, and CRW frame systems.</p>

---

## Post #52 by @jay1987 (2022-08-04 01:59 UTC)

<p>thanks,i try to use slicer to positioning Leksell headframe , i use <strong>Stereotaxia</strong> and <strong>trajectoryGuide</strong> module , both encountered different problems.<br>
in my process to use <strong>trajectoryGuide</strong> module<br>
1.git clone trajectoryGuideModules from github site to local<br>
2.follow the guide of site <a href="https://trajectoryguide.greydongilmore.com/installation.html" rel="noopener nofollow ugc">https://trajectoryguide.greydongilmore.com/installation.html</a> to install module<br>
3.use slicer to load dcm files and save it to nii.gz format<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14c0579c8cd846ab02c2300b66ad403ca5590c03.png" alt="image" data-base62-sha1="2XzDJ0FcoqbM4DGoRAeMdehNtar" width="527" height="122"></p>
<p>4.use Data Import module to load the nii.gz folder<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a36cf9361f097a12ef0f8727267a8a38d98890d5.jpeg" data-download-href="/uploads/short-url/njJiK0AIBVTLWuqIhO7JYL6z8IB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36cf9361f097a12ef0f8727267a8a38d98890d5_2_690x349.jpeg" alt="image" data-base62-sha1="njJiK0AIBVTLWuqIhO7JYL6z8IB" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36cf9361f097a12ef0f8727267a8a38d98890d5_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36cf9361f097a12ef0f8727267a8a38d98890d5_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36cf9361f097a12ef0f8727267a8a38d98890d5_2_1380x698.jpeg 2x" data-dominant-color="AFAFB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×972 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
5.change to Frame Detection module ,and select <strong>Leksell G LF</strong> to Detect Frame Fiducials,after seconds computing ,i got these errors<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4e01ccca00e8cb5febfbad415f5199103ae36ea.jpeg" data-download-href="/uploads/short-url/yWgF1bXiFAYd3kKRA1GwwXnTwRY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e01ccca00e8cb5febfbad415f5199103ae36ea_2_690x362.jpeg" alt="image" data-base62-sha1="yWgF1bXiFAYd3kKRA1GwwXnTwRY" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e01ccca00e8cb5febfbad415f5199103ae36ea_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e01ccca00e8cb5febfbad415f5199103ae36ea_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e01ccca00e8cb5febfbad415f5199103ae36ea_2_1380x724.jpeg 2x" data-dominant-color="8B8A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×1005 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the detail information bellow<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08471cb535345be3440c270ae3606ba93c79e06.png" data-download-href="/uploads/short-url/yjIlWCmhGBuEqyDCAa5g8l6nqrc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08471cb535345be3440c270ae3606ba93c79e06.png" alt="image" data-base62-sha1="yjIlWCmhGBuEqyDCAa5g8l6nqrc" width="690" height="150" data-dominant-color="FDEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">906×197 3.04 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a></p>

---

## Post #53 by @Greydon_Gilmore (2022-08-05 02:33 UTC)

<p><a class="mention" href="/u/jay1987">@jay1987</a> do you mind sharing the frame CT volume?</p>

---

## Post #54 by @jay1987 (2022-08-05 05:22 UTC)

<p>thanks from replying , i don’t known how to upload .rar data , it seems only support png,mp4 data uploading,would you mind leave your email for me ?</p>

---

## Post #55 by @lassoan (2022-08-05 06:51 UTC)

<p>You can upload data to dropbox, OneDrive, Google drive, etc. and post the download link here.</p>

---

## Post #56 by @jay1987 (2022-08-05 07:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="55" data-topic="13963">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>dropbox</p>
</blockquote>
</aside>
<p>thanks lasso,i made a dropbox link here</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/htyh36cfca7i0jz/DataForLeksellFrame.rar?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/htyh36cfca7i0jz/DataForLeksellFrame.rar?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-file-zip-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/s/htyh36cfca7i0jz/DataForLeksellFrame.rar?dl=0" target="_blank" rel="noopener nofollow ugc">DataForLeksellFrame.rar</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a></p>

---

## Post #57 by @JBeninca (2022-08-05 11:59 UTC)

<p>Dear jay1987:</p>
<p>Leksell and Micromar frames are different. So you can´t use the graphical issues (Stereotaxia module),<br>
but the light version (StereotaxiaLite) can support the Leksell with the following changes :</p>
<p>Also: I´ve never worked with a Leksell. I don´t know if the zero in Z is the bottom of the fiducials (I suppose it is) and I don´t know where is the zero in Y ( I assumed its in the middle of the ruler)<br>
fiducials is a square of 120 mm and they are separated 190</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df498473a72dfdfa4d24b16c4f82ad3868b7aeb.png" alt="image" data-base62-sha1="1ZsfrGjhk6bOh06eqke6kkVE64b" width="496" height="456"></p>
<p>if you take an send me a CT-scan of a free Lexsell frame, with the fiducials visibles, I could make a model of it, take the meassures and implemet a version of Stereotaxia with it.</p>

---

## Post #58 by @jay1987 (2022-08-05 12:11 UTC)

<p>Dear JBeninca:</p>
<p>thanks for replying so much<br>
i don’t have a leksell frame data now ,  only have a CT-SCAN with leksell head frame sequence here</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/htyh36cfca7i0jz/DataForLeksellFrame.rar?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/htyh36cfca7i0jz/DataForLeksellFrame.rar?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-zip-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/htyh36cfca7i0jz/DataForLeksellFrame.rar?dl=0" target="_blank" rel="noopener nofollow ugc">DataForLeksellFrame.rar</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #59 by @JBeninca (2022-08-05 13:36 UTC)

<p>Yes, i´ve downloaded it and delete the cranium and make a model of the frame. i think i could incorporate as an option in the module.<br>
I must check some details about the frame: have you used it?</p>
<p>thanks</p>

---

## Post #60 by @JBeninca (2022-08-05 13:37 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/979028b686e82ae208e528a66f6d217f2bec3b74.png" alt="image" data-base62-sha1="lCMXm2opuwUVSByYntVALpNHdwE" width="592" height="456"><br>
Leksell model from your CT scan</p>

---

## Post #61 by @jay1987 (2022-08-07 01:07 UTC)

<p>good job Beninca<br>
Yes, my jobs is to location the head position by leksell head frame , and use it as a component for two hospital<br>
can you integrate the leksell module in your Stereotaxia? it means much for us.</p>

---

## Post #62 by @JBeninca (2022-08-09 18:13 UTC)

<p>I will do the work. i need some time, a couple of weeks. I´m  a neurosurgeon with a lot of work</p>

---

## Post #63 by @jay1987 (2022-08-10 01:43 UTC)

<p>dear <a class="mention" href="/u/jbeninca">@JBeninca</a>:<br>
for my respect.<br>
it’s rare to see a neurosurgeon can coding slicer in china , my work is to integrate all usefull and convenient slicer plugin into a package for neurosurgeon,your work is very valuable for me to keep tracing,thank you very much.</p>

---

## Post #64 by @Greydon_Gilmore (2022-08-23 02:38 UTC)

<p><a class="mention" href="/u/jay1987">@jay1987</a> looking at your frame CT, it looks like your Y-axis is flipped (something I never considered in my implementation).</p>
<p><a class="mention" href="/u/jbeninca">@JBeninca</a> no need to rewrite code for the Leksell. You can see my implementation here: <a href="https://github.com/greydongilmore/trajectoryGuideModules/blob/main/frameDetect/frameDetect.py" class="inline-onebox" rel="noopener nofollow ugc">trajectoryGuideModules/frameDetect.py at main · greydongilmore/trajectoryGuideModules · GitHub</a>. The specific class I wrote for detecting the N-localizers is here: <a href="https://github.com/greydongilmore/trajectoryGuideModules/blob/9c6f99226c4f42e01d88e26badd4b48b79aa0884/helpers/helpers.py#L365" class="inline-onebox" rel="noopener nofollow ugc">trajectoryGuideModules/helpers.py at 9c6f99226c4f42e01d88e26badd4b48b79aa0884 · greydongilmore/trajectoryGuideModules · GitHub</a>.</p>
<p>I’m happy to help out in any way.</p>

---

## Post #65 by @jay1987 (2022-08-23 02:44 UTC)

<p>thank you very much <a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a></p>

---

## Post #66 by @Greydon_Gilmore (2022-08-23 03:07 UTC)

<p>accounting for the flip in the Y-axis I am able to obtain the following segmentation from your CT:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/283cd67e9ce19d29b44f111090599fbd393a4eeb.jpeg" data-download-href="/uploads/short-url/5JXrufe61XcFTp9twfa39oNLxt9.jpeg?dl=1" title="Figure_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/283cd67e9ce19d29b44f111090599fbd393a4eeb_2_600x499.jpeg" alt="Figure_1" data-base62-sha1="5JXrufe61XcFTp9twfa39oNLxt9" width="600" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/283cd67e9ce19d29b44f111090599fbd393a4eeb_2_600x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/283cd67e9ce19d29b44f111090599fbd393a4eeb_2_900x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/283cd67e9ce19d29b44f111090599fbd393a4eeb_2_1200x998.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure_1</span><span class="informations">1600×1332 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You’ll notice some drop-out near the bottom of the N-localizer due to weak localizer signal. However, you do not need all points to calculate Frame coordinates so this won’t affect accuracy. The other thing I’ve noticed is that your frame CT is not centered (the x,y,z axes should be centered on 100). Did you apply a transform to the image prior to sharing?</p>

---

## Post #67 by @jay1987 (2022-08-23 03:10 UTC)

<p>that’s correct ! <a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a><br>
could you please integrate these piece of code in your trajectoryGuideModules?that’s very useful!!</p>

---

## Post #68 by @slicer365 (2022-08-23 11:51 UTC)

<p>A best way for Leksell frame. You can use Fiducial Registration module to register the CT data with the prepared points .</p>

---

## Post #69 by @jay1987 (2022-08-23 11:55 UTC)

<p>yes,it’s work!<br>
but i need to find the x,y,z position and three angles relative to the leksell frame .</p>

---

## Post #70 by @slicer365 (2022-08-23 12:24 UTC)

<p>It is easy，when you adjust the XYZ frame and RAS to be parallel, it can be obtained by simple calculation. Regarding the angle, it can be obtained by the arctangent function.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45e6998c0243a4cfe7b40ccfee770efe9ca5ea87.png" alt="1661257411293" data-base62-sha1="9Yn0crJ9tObgf06zun1gaeUVzPF" width="425" height="336"></p>

---

## Post #71 by @jay1987 (2022-08-23 12:28 UTC)

<p>I understand what you mean,but i dont have a leksell headframe , i can’t judge the result what i caculate , the recent value i get is about 5 degree off to the correct result what i send to my doctor friend to evaluate</p>

---

## Post #72 by @slicer365 (2022-08-23 12:32 UTC)

<p>Do you have the module, maybe I can provide you with the CT data or I can help you test it.</p>

---

## Post #73 by @JBeninca (2022-08-25 14:16 UTC)

<p>Yes , please <a class="mention" href="/u/jay1987">@jay1987</a>, if you can send one or more leksell framed - patient CT scan data , I ´ll will be thankfull</p>

---

## Post #75 by @jfdoarias (2022-11-21 00:57 UTC)

<p>this is a tc with leksell arc: <a href="https://we.tl/t-xlITWNB3xw" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a></p>

---

## Post #76 by @vzapata10 (2024-06-12 15:42 UTC)

<p>Hi Greydon <a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a>,</p>
<p>Thanks for the implementation of trajectoryGuide! It seems great. I have some segmentations of basal ganglia structures that I’m visualizing over the MRI in slicer (they are all co-registered to the T1 space). I want to overlay the MER and implantation notes about the start and end of the STN; those measurements are based on the stereotactic frame’s coordinate system (we use a Leksell frame). I was looking at the website of trajectoryGuide and I think I could accomplish this using your tool.</p>
<p>I already installed all the requirements and upload my data on BIDS format. However, when I run the second step “02: Frame detection” I get the following error in Slicer’s Python console:</p>
<p>“Traceback (most recent call last):<br>
File “C:/Users/zapatav/Desktop/Toolboxes/Slicer/trajectoryGuide/frameDetect/frameDetect.py”, line 685, in onFrameDetectButton<br>
self.logic.runFrameDetection(self.ui.frameFidVolumeCBox.currentNode(), self.frame_settings, self._parameterNode.GetParameter(‘derivFolder’))<br>
File “C:/Users/zapatav/Desktop/Toolboxes/Slicer/trajectoryGuide/frameDetect/frameDetect.py”, line 1165, in runFrameDetection<br>
self.frameDetectInstance = frameDetection(frameFidVolume, derivFolder, frame_settings)<br>
File “C:\Users\zapatav\Desktop\Toolboxes\Slicer\trajectoryGuide\helpers\helpers.py”, line 383, in <strong>init</strong><br>
self.frame_detect()<br>
File “C:\Users\zapatav\Desktop\Toolboxes\Slicer\trajectoryGuide\helpers\helpers.py”, line 1068, in frame_detect<br>
combined=self.NLocalizersSort(component, self.frame_settings[‘n_components’], 2)<br>
File “C:\Users\zapatav\Desktop\Toolboxes\Slicer\trajectoryGuide\helpers\helpers.py”, line 780, in NLocalizersSort<br>
min_threshold=gaps[0][0]<br>
IndexError: list index out of range”</p>
<p>I wanted to ask you if you have seen this before and know how could I fix it, or if is there any forum specifically for trajectoryGuide that I can look at?</p>
<p>Any help would be much appreciated!<br>
Thanks,</p>
<p>Valentina</p>

---

## Post #77 by @Greydon_Gilmore (2024-06-19 23:42 UTC)

<p>Sending you a PM to try and solve this problem.</p>
<p>Greydon</p>

---

## Post #78 by @lassoan (2024-06-22 05:18 UTC)

<p>It would be great if you could keep the discussion public (there could  be a lot to learn). If it is not possible then please suammarize in the end what the issue was and how you solved it.</p>

---

## Post #79 by @Daniel_Leeb (2024-07-17 08:47 UTC)

<p>Hey <a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a>!</p>
<p>I also stumbled across your extension after searching for some tool to detect the Leksell frame. It seems very well implemented and also well documented, but unfortunately I can’t figure out some mistake of mine. I would really appreciate it if you can help me out here.<br>
So I tested it with the dataset provided in the extension first and everything went well.<br>
After I changed my CT scan of a head with a Leksell frame from DICOM to BIDS format (following the tutorial you linked in your documentation), I tried to detect the frame again but without success.</p>
<p>The mouse courser is stuck at the hourglass symbol and the following error message is printed:</p>
<p>“Traceback (most recent call last):<br>
File “C:/Users/Praktikant/Documents/OwnSlicerExtensions/trajectoryGuideModules-main/frameDetect/frameDetect.py”, line 936, in onFrameDetectButton<br>
self.logic.runFrameDetection(self.ui.frameFidVolumeCBox.currentNode(), self.frame_settings, self._parameterNode.GetParameter(‘derivFolder’))<br>
File “C:/Users/Praktikant/Documents/OwnSlicerExtensions/trajectoryGuideModules-main/frameDetect/frameDetect.py”, line 1416, in runFrameDetection<br>
self.frameDetectInstance = frameDetection(frameFidVolume, derivFolder, frame_settings)<br>
File “C:\Users\Praktikant\Documents\OwnSlicerExtensions\trajectoryGuideModules-main\helpers\helpers.py”, line 383, in <strong>init</strong><br>
self.frame_detect()<br>
File “C:\Users\Praktikant\Documents\OwnSlicerExtensions\trajectoryGuideModules-main\helpers\helpers.py”, line 1066, in frame_detect<br>
component=np.vstack(component)<br>
File “C:\Users\Praktikant\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\numpy\core\shape_base.py”, line 289, in vstack<br>
return _nx.concatenate(arrs, 0, dtype=dtype, casting=casting)<br>
ValueError: need at least one array to concatenate”</p>
<p>What I understand out of this error is that no fiducials of the N-shaped frame get detected.<br>
Also interesting is that the frame is indeed moved to the center of RAS without me having to confirm the fiducials first, but the program is still stuck.</p>
<p>In case you want to test it yourself with my dataset, here is the link to it:<br>
<a href="https://drive.google.com/drive/folders/1Wseu8hA481GXpzp6l6GjhS4tudUd9WOo?usp=drive_link" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1Wseu8hA481GXpzp6l6GjhS4tudUd9WOo?usp=drive_link</a></p>
<p>I  would really appreciate your help, because I would like to use your extension for a project of mine. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks,<br>
Daniel</p>

---
