---
topic_id: 43237
title: "Loading Deca Module"
date: 2025-06-05
url: https://discourse.slicer.org/t/43237
---

# Loading DeCA module

**Topic ID**: 43237
**Date**: 2025-06-05
**URL**: https://discourse.slicer.org/t/loading-deca-module/43237

---

## Post #1 by @philippepellerin (2025-06-05 15:35 UTC)

<p>Hi, I think that this one is for Muratmaga.<br>
I am interested in the DeCA module, since I understood that it was able to create a template out of a series of segmented skulls, a function which would be very usefull for my researches.<br>
Since the module code is in Github, I went to this adress <a href="https://github.com/smrolfe/DeCA" class="inline-onebox" rel="noopener nofollow ugc">GitHub - smrolfe/DeCA: Dense Correspondence Analysis (DeCA) toolkit</a>.<br>
I downloaded the .zip file in my download folder.<br>
In 3DSlicer i opened the module “extensions manager” click on the folder icone (top right) from the drop menu I select the Zip file, but I got this message error. Where am I wrong?<br>
Thanks for any help.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e976a34d385ebf2c9918f67f7bfd79f57c14ddd.jpeg" data-download-href="/uploads/short-url/2555xPuQWCh9w7Ch8yEYWjtqVAx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e976a34d385ebf2c9918f67f7bfd79f57c14ddd_2_690x402.jpeg" alt="image" data-base62-sha1="2555xPuQWCh9w7Ch8yEYWjtqVAx" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e976a34d385ebf2c9918f67f7bfd79f57c14ddd_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e976a34d385ebf2c9918f67f7bfd79f57c14ddd_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e976a34d385ebf2c9918f67f7bfd79f57c14ddd_2_1380x804.jpeg 2x" data-dominant-color="D9DBE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1431×835 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-06-05 16:06 UTC)

<ol>
<li>the official DeCA repository is <a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerDenseCorrespondenceAnalysis: Dense Correspondence Analysis for Surfaces</a> (the one you linked is a development fork).</li>
<li>You are using an outdated version of Slicer (5.0.2)</li>
</ol>
<p>Install the latest stable or preview, and DeCA will be in the extension catalogue (though search for the full extension name DenseCorrespondenceAnalysis).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> when are you guys planning to improve the search functionality in the extension catalogue to search for all the keywords?</p>

---

## Post #3 by @philippepellerin (2025-06-05 16:14 UTC)

<p>Great, I am on a trip abroad with my old laptop but, now I am eager to be back home to run the module and create the templates which are an old dream !</p>
<p>Envoyé de mon iPhone</p>

---

## Post #4 by @lassoan (2025-06-07 14:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>when are you guys planning to improve the search functionality in the extension catalogue to search for all the keywords?</p>
</blockquote>
</aside>
<p>This would need changing of the extensions manager frontend, so a task best suited for <a class="mention" href="/u/jcfr">@jcfr</a>. I haven’t found an open issue for this. To put it on <a class="mention" href="/u/jcfr">@jcfr</a>’s roadmap, the best would be to add an issue to <a href="https://github.com/KitwareMedical/slicer-extensions-webapp/issues">slicer-extensions-webapp repository</a>. Maybe it is not difficult to implement this, but he may have many other priorities.</p>

---

## Post #5 by @muratmaga (2025-06-08 01:06 UTC)

<p>OK I opened a thread <a href="https://github.com/KitwareMedical/slicer-extensions-webapp/issues/198" class="inline-onebox" rel="noopener nofollow ugc">Improve search capabilities for extensions · Issue #198 · KitwareMedical/slicer-extensions-webapp · GitHub</a></p>

---

## Post #6 by @philippepellerin (2025-06-14 08:34 UTC)

<p>Good morning, back home, I installed the DeCA module. I can’t find help on this module.<br>
I understand that I need to create directories for models, landmarks and DeCA outputs.<br>
How I name the files to do models and landmarks corresponding? etc…<br>
Thank for help.</p>

---

## Post #7 by @muratmaga (2025-06-14 20:54 UTC)

<p>Make sure you are using the latest stable or the preview. If you are using the stable, do check whether you have the latest DeCA. We have revamped the UI couple months back, and now all you have to point out is where the data sits. Folder structure of the output and downstream work is now handled by the module itself.</p>
<p>See the latest tutorials:</p>
<p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/DeCA_1" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/DeCA_1 at main · SlicerMorph/Tutorials · GitHub</a> (general shape analysis with optional asymmetry analysis).<br>
<a href="https://github.com/SlicerMorph/Tutorials/tree/main/DeCA_2" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/DeCA_2 at main · SlicerMorph/Tutorials · GitHub</a> (asymmetry specific workflow)<br>
<a href="https://github.com/SlicerMorph/Tutorials/tree/main/DeCAL" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/DeCAL at main · SlicerMorph/Tutorials · GitHub</a> (automated dense semilandmarking with DecA)</p>

---

## Post #8 by @jamesobutler (2025-06-14 22:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="43237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>or the preview.</p>
</blockquote>
</aside>
<p>DenseCorrespondenceAnalysis extension currently has a build failure for latest Slicer preview following the update to Python 3.12. See the following:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8466#issuecomment-2972734519">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8466#issuecomment-2972734519" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?u=77e23f0a30df57a25f193983b30b27790f224a1c&amp;v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a> - <a href="https://github.com/Slicer/Slicer/pull/8466#issuecomment-2972734519" target="_blank" rel="noopener nofollow ugc">ENH: Upgrade from python 3.9.10 to 3.12.10</a>
      </h4>



    <div class="branches">
      <code>main</code> ← <code>jcfr:transition-from-python-3.9-to-3.12-repushed</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Extensions to be updated:

SyntaxWarning reported as build error:
- [ ] Slice<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8466" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">rCineTrack: https://slicer.cdash.org/viewBuildError.php?buildid=3828759  
- [x] Sandbox: https://slicer.cdash.org/viewBuildError.php?buildid=3828421  
- [x] SlicerHeart: https://slicer.cdash.org/viewBuildError.php?buildid=3828775  
- [ ] SPHARM-PDM: https://slicer.cdash.org/viewBuildError.php?buildid=3828707  
- [ ] SlicerNetsim: https://slicer.cdash.org/viewBuildError.php?buildid=3828803  
- [ ] SlicerAIGT: https://slicer.cdash.org/viewBuildError.php?buildid=3828723  
- [ ] Breast_DCEMRI_FTV: https://slicer.cdash.org/viewBuildError.php?buildid=3828436  
- [ ] CMFreg: https://slicer.cdash.org/viewBuildError.php?buildid=3828445  
- [ ] PickAndPaintExtension: https://slicer.cdash.org/viewBuildError.php?buildid=3828641  
- [ ] Q3DC: https://slicer.cdash.org/viewBuildError.php?buildid=3828652  
- [ ] OpenDose3D: https://slicer.cdash.org/viewBuildError.php?buildid=3828588  
- [ ] XNATSlicer: https://slicer.cdash.org/viewBuildError.php?buildid=3828911  
- [ ] ShapeRegressionExtension: https://slicer.cdash.org/viewBuildError.php?buildid=3828706  
- [ ] flywheel_connect: https://slicer.cdash.org/viewBuildError.php?buildid=3828912  
- [ ] pipelines: https://slicer.cdash.org/viewBuildError.php?buildid=3828642  
- [ ] MeshStatisticsExtension: https://slicer.cdash.org/viewBuildError.php?buildid=3828575  
- [ ] MHubRunner: https://slicer.cdash.org/viewBuildError.php?buildid=3828565  
- [x] TotalSegmentator: https://slicer.cdash.org/viewBuildError.php?buildid=3828884  
- [x] PedicleScrewSimulator: https://slicer.cdash.org/viewBuildError.php?buildid=3828607  
- [ ] DenseCorrespondenceAnalysis: https://slicer.cdash.org/viewBuildError.php?buildid=3828466  
- [ ] SlicerConda: https://slicer.cdash.org/viewBuildError.php?buildid=3828408

Needs updated Python 3.12 package hashes:
- [ ] ShapeVariationAnalyzer: https://slicer.cdash.org/viewBuildError.php?buildid=3829016

Can’t build a python package whl:
- [ ] SlicerRadiomics: need GCC &gt;= 9.3 https://slicer.cdash.org/viewBuildError.php?buildid=3828316

disutils deprecation warning:
- [x] PortPlacement: https://slicer.cdash.org/viewBuildError.php?buildid=3828749</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @muratmaga (2025-06-15 01:03 UTC)

<p>Thanks for reporting. We will check.</p>

---

## Post #10 by @philippepellerin (2025-06-15 06:19 UTC)

<p>Thank you so much for this wonderful tool.<br>
I got my first human skull template which is very effective for the study of craniofacial malformations</p>
<p>Envoyé de mon iPhone</p>

---

## Post #11 by @muratmaga (2025-06-15 18:30 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="10" data-topic="43237">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>effective for the study of craniofacial malformations</p>
</blockquote>
</aside>
<p>If you are working with CT images (as opposed to surface scans), you might want to try the template building in our SlicerANTsPy. This will allow you to build a volumetric template from the CT scans. You can optionally allow for initial LM based rigid initialization.</p>
<p>It is in a rough (from documentation point of view), but usable state: <a href="https://github.com/SlicerMorph/SlicerANTSpy" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerANTsPy: module and GUI for antspy</a></p>

---

## Post #12 by @philippepellerin (2025-06-16 07:11 UTC)

<p>Hi, SlicerANTSpy looks great, but it lacks a manual for non-geeks like me.</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #13 by @muratmaga (2025-06-16 15:08 UTC)

<p>There is not much to it really. Choose a folder of NRRD, and if you have landmarks choose a folder of LMs (again this is optional and only needed if you want to do a LM based rigid initialization).</p>
<p>Then choose the SyNQuick as the registration and probably do at least 3 iterations…</p>

---

## Post #14 by @philippepellerin (2025-09-12 13:29 UTC)

<p>Hi, I have created a set of 19 Skull Atlas templates from 184 normal CT scans, ranging from birth to 76 years old, using the DeCA module.I am very happy with it and would be happy to share it with anyone interested (upon request). I would like, as suggested by Murat Maga, to try the SlicerANTSpy, I downloaded it on the 5.9-2025-09-11 ,but I can’t find it among the modules menu. What is the problem? When I open the extensions display, SlicerANTSpy is visible but it does not appear in the extensions’ menu and the extension research can’t find it…</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>
<p>2025</p>

---

## Post #15 by @muratmaga (2025-09-12 14:49 UTC)

<p>Extensions may not be available for every version of the preview releases for various reasons. As far as I can tell, it is available for a recent preview release (r33931). Follow this link to download that version of Slicer and try installing and using ANTsPy</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://download.slicer.org/?offset=-1">
  <header class="source">
      <img src="https://download.slicer.org/assets/favicons/favicon-32x32.png?v=Gv63MLlwnz" class="site-icon" alt="" width="32" height="32">

      <a href="https://download.slicer.org/?offset=-1" target="_blank" rel="noopener">3D Slicer</a>
  </header>

  <article class="onebox-body">
    <img width="128" height="128" src="https://download.slicer.org/assets/img/3d-slicer-128x128.png" class="thumbnail onebox-avatar" alt="">

<h3><a href="https://download.slicer.org/?offset=-1" target="_blank" rel="noopener">Download 3D Slicer</a></h3>

  <p>3D Slicer is a free, open source software for visualization, processing, segmentation, registration, and analysis of medical, biomedical, and other 3D images and meshes; and planning and navigating image-guided procedures.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @philippepellerin (2025-09-18 13:58 UTC)

<p>I downloaded the r33931 and installed the SlicerANTsPY, but I can’t find the extension in the module menu. I am working with MacOS Sequoia 15.6</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #17 by @muratmaga (2025-09-18 16:50 UTC)

<p>You mean after you install SlicerANTsPy and restarted slicer, if you do search for ants (CTRL+F), it doesn’t show? What is in the SlicerMorph sub menu?</p>
<p>Can you share a full log?</p>

---

## Post #18 by @philippepellerin (2025-09-19 11:49 UTC)

<p>Yes, I did that: downloaded r33931, then after SlicerANTsPY, restarted. I can’t see SlicerANTsPY in the menu, nor in any sub-menu, but as you can see in the screen grab, there is a folder somewhere with this name…SlicerANTsPY never came up in the menu and submenu.<br>
Thank for your help. Best regards</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5406f6d52a35a9973ed8f1f89512612d86378549.png" data-download-href="/uploads/short-url/bZl1Kv6XuMPPtf33XlbUpTrqU4N.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="320" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5406f6d52a35a9973ed8f1f89512612d86378549.png" data-base62-sha1="bZl1Kv6XuMPPtf33XlbUpTrqU4N" height="208"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">640×416 94.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>P.S. It is another topic, when building up my set of skull emplates with DeCA I had an issue with the Skull Atlas 1155-1355d. The result obtained through the analysis of 11 models and markups was incoherent. I redid it several times, I checked for an error in the models and markups, and could not find any explanation. When checking the landmarks with GPA I found a model named PCA Warped Volume, which looks good as a mean statistical model.</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #19 by @muratmaga (2025-09-19 14:39 UTC)

<p>Thats the one. Everything in Antspy is registration based</p>

---

## Post #20 by @philippepellerin (2025-09-20 15:07 UTC)

<p>I can’t see how to create a mean statistical volume with the tools available under the name ANTs</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #21 by @muratmaga (2025-09-20 17:47 UTC)

<p>ANTs works with volumes, not 3D models. If you organize the original scans, and the landmarks that you created on the disk (not in the Slicer scene), you can create a volumetric template by using the Templates tab</p>
<p>I didn’t really have time to write a tutorial. There are some additional steps that are important to consider (e.g., selection of the initial template, or how to create one if there is no reference template). but give it a try as is, and if you think you find it useful, I can provide those points.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/912912d9db5c5dec3e819392b0ce16cbd51c1aae.png" data-download-href="/uploads/short-url/kI9erWwHzA6dor6X863T4EJUuvA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/912912d9db5c5dec3e819392b0ce16cbd51c1aae_2_690x368.png" alt="image" data-base62-sha1="kI9erWwHzA6dor6X863T4EJUuvA" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/912912d9db5c5dec3e819392b0ce16cbd51c1aae_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/912912d9db5c5dec3e819392b0ce16cbd51c1aae.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/912912d9db5c5dec3e819392b0ce16cbd51c1aae.png 2x" data-dominant-color="F0F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">932×498 43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @philippepellerin (2025-09-20 17:52 UTC)

<p>I will, because it looks good, and come back in touch<br>
Best</p>
<p>Envoyé de mon iPhone</p>

---

## Post #23 by @philippepellerin (2025-09-20 17:54 UTC)

<p>If I succeed, I will write a tutorial <img src="https://emoji.discourse-cdn.com/twitter/grinning_face_with_smiling_eyes.png?v=14" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:" loading="lazy" width="20" height="20"></p>
<p>Envoyé de mon iPhone</p>

---

## Post #24 by @muratmaga (2025-09-20 21:59 UTC)

<p>Sounds good. Go ahead and proceed with using one of your actual samples as a reference. However, the more appropriate way would be to rigidly register all those samples into a common orientation (using groupwise tab), and average them at that space, and then use that to initialize the template building process.</p>
<p>That is not incorporated into the ANTsPY yet properly, but there is simple script that you can pretty much copy and edit the path to the rigidly aligned volumes, and paste it into the Python console in Slicer:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerANTsPy/blob/main/Scripts/AverageImage.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerANTsPy/blob/main/Scripts/AverageImage.py" target="_blank" rel="noopener">github.com/SlicerMorph/SlicerANTsPy</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerANTsPy/blob/main/Scripts/AverageImage.py" target="_blank" rel="noopener">Scripts/AverageImage.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerANTsPy/blob/main/Scripts/AverageImage.py" rel="noopener"><code>main</code></a>
</div>


      <pre><code class="lang-py">import slicer
import ants
import os
import time

# Function to create a Slicer node from an ANTSImage
def nodeFromANTSImage(antsImage, name):
    import ants
    
    imageNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', name)


    tempFilePath = os.path.join(
        slicer.app.temporaryPath,
        "tempImage_{0}.nii.gz".format(time.time()),
    )
    ants.image_write(antsImage, tempFilePath)

    storageNode = slicer.vtkMRMLVolumeArchetypeStorageNode()
    storageNode.SetFileName(tempFilePath)
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerANTsPy/blob/main/Scripts/AverageImage.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #25 by @philippepellerin (2025-09-21 08:26 UTC)

<p>Sorry I can’t find such a display as this one:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdb2e2bf3d4f068ef93ef7bbc32d1a0abbeff230.png" data-download-href="/uploads/short-url/tlH8PcwFwtgTHXG03O6GYVMChGg.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="320" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdb2e2bf3d4f068ef93ef7bbc32d1a0abbeff230.png" data-base62-sha1="tlH8PcwFwtgTHXG03O6GYVMChGg" height="165"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">640×330 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I tried to copy, as suggested , the above script, and paste it in the console, but I got an error message : hereafter you’ll find the log</p>
<p>import slicer</p>
<p>import ants</p>
<p>import os</p>
<p>import time</p>
<h1><a name="p-128621-function-to-create-a-slicer-node-from-an-antsimage-1" class="anchor" href="#p-128621-function-to-create-a-slicer-node-from-an-antsimage-1" aria-label="Heading link"></a>Function to create a Slicer node from an ANTSImage</h1>
<p>def nodeFromANTSImage(antsImage, name):</p>
<p>import ants</p>
<p>imageNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’, name)</p>
<p>tempFilePath = os.path.join(</p>
<p>slicer.app.temporaryPath,</p>
<p>“tempImage_{0}.nii.gz”.format(time.time()),</p>
<p>)</p>
<p>ants.image_write(antsImage, tempFilePath)</p>
<p>storageNode = slicer.vtkMRMLVolumeArchetypeStorageNode()</p>
<p>storageNode.SetFileName(tempFilePath)</p>
<p>storageNode.ReadData(imageNode, True)</p>
<p>os.remove(tempFilePath)</p>
<p>return imageNode</p>
<h1><a name="p-128621-input-directory-of-aligned-images-such-as-from-ants-registraion-groupwise-registration-2" class="anchor" href="#p-128621-input-directory-of-aligned-images-such-as-from-ants-registraion-groupwise-registration-2" aria-label="Heading link"></a>Input directory of aligned images (such as from ANTs Registraion Groupwise Registration)</h1>
<p>input_directory = “D:/ANTsData/MouseOutputs”</p>
<h1><a name="p-128621-end-pattern-for-selecting-the-transformed-images-from-the-input-directory-3" class="anchor" href="#p-128621-end-pattern-for-selecting-the-transformed-images-from-the-input-directory-3" aria-label="Heading link"></a>End pattern for selecting the transformed images from the input directory</h1>
<p>filename_end_pattern = “transformed.nii.gz”</p>
<p>filePaths = <span class="chcklst-box fa fa-square-o fa-fw"></span></p>
<p>for file in os.listdir(input_directory):</p>
<p>if file.endswith(filename_end_pattern):</p>
<p>filePaths.append(os.path.join(input_directory, file))</p>
<p>averagedANTSImage = ants.math.average_images(filePaths)</p>
<p>averagedImageNode = nodeFromANTSImage(averagedANTSImage, “AverageImage”)</p>
<p>slicer.util.setSliceViewerLayers(background=averagedImageNode, fit=True)</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 2, in </p>
<p>ModuleNotFoundError: No module named ‘ants’</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #26 by @muratmaga (2025-09-21 15:38 UTC)

<p>What is the version of Slicer you are using and can you send a acreenshot of your antsRegistration module?</p>

---

## Post #27 by @philippepellerin (2025-09-22 08:26 UTC)

<p>I have previously tried with 3 different issues, and each time I get this menu(attached). Before I answer your mail, I downloaded the issue 5.9.0-2025-09-20 released yesterday, and I have the good menu. I will try to use it and will let you know.<br>
But, anyway, since the interest, for me, is to superpose the Normal skull with a skull of interest, only the models, with their edition and display abilities, are worthy, since the superposition of volume rendering is very difficult to read.<br>
If you wish to have a look at my work, you may have a good idea by watching this tutorial on YouTube <a href="https://youtu.be/hJTWZDnqZ3k" rel="noopener nofollow ugc">https://youtu.be/hJTWZDnqZ3k</a><br>
I may, as well, share a folder with the Atlas if you like. I wonder whether the Slicer community could be interested.<br>
Best regards, and, again, thanks for the nice tools that you provide. Best regards.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/250e16b8e19e25de36ba9594e029615a4899ed1e.jpeg" data-download-href="/uploads/short-url/5hNQMUeBqfRHJ0fF0wHldbEKxOe.jpeg?dl=1" title="5.9.0-2025-08-11.jpeg" rel="noopener nofollow ugc"><img alt="5.9.0-2025-08-11.jpeg" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/250e16b8e19e25de36ba9594e029615a4899ed1e.jpeg" data-base62-sha1="5hNQMUeBqfRHJ0fF0wHldbEKxOe" width="267" height="241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5.9.0-2025-08-11.jpeg</span><span class="informations">267×241 16.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>philippe pellerin</p>
<p><a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #28 by @philippepellerin (2025-09-22 09:13 UTC)

<p>I don’t understand. I had the good menu, then I restarted the application, and now it is back to the previous, incomplete menu!<br>
this is a grab screen<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e567df659c4c897ce7f587c9dfee13d1ed77ee61.png" data-download-href="/uploads/short-url/wJpSZ2olEWGLKrVaLHyr9sNDc8F.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="320" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e567df659c4c897ce7f587c9dfee13d1ed77ee61.png" data-base62-sha1="wJpSZ2olEWGLKrVaLHyr9sNDc8F" height="160"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">640×320 54.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #29 by @philippepellerin (2025-09-22 09:16 UTC)

<p>I got the right menu back when I disable the other extensions…</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #30 by @cpinter (2025-09-22 09:25 UTC)

<p>Can you enable again the other extensions, start the application, and see what errors are in the Python console? It is possible that a previous error of another module prevented this one from being set up properly.</p>

---

## Post #31 by @philippepellerin (2025-09-22 09:30 UTC)

<p>This is what I copy from the console:</p>
<p>Python 3.12.10 (main, Sep 21 2025, 23:13:54) [Clang 14.0.6 (<a href="https://github.com/tru/llvm-release-build" rel="noopener nofollow ugc">https://github.com/tru/llvm-release-build</a> 686807a176470032c208f27 on darwin</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[VTK] Warning: In vtkSlicerTerminologiesModuleLogic.cxx, line 3351</p>
<p>[VTK] vtkSlicerTerminologiesModuleLogic (0x600000659400): LoadAnatomicContextFromFile is deprecated. Use LoadRegionContextFromFile instead.</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #32 by @philippepellerin (2025-09-22 09:44 UTC)

<p>The problem is fixed when I disable the SlicerANTs extension<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f58941b19744ea619c94a0b340a45dda4cd55bb3.png" data-download-href="/uploads/short-url/z273aPhfju3StMKNWZ4BaQrknEn.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="320" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f58941b19744ea619c94a0b340a45dda4cd55bb3.png" data-base62-sha1="z273aPhfju3StMKNWZ4BaQrknEn" height="145"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">640×290 54.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #33 by @cpinter (2025-09-22 11:39 UTC)

<p>This warning is harmless, it will not prevent anything.</p>
<p>Did you copy this with SlicerANTs enabled? There was nothing else?</p>

---

## Post #34 by @philippepellerin (2025-09-22 13:33 UTC)

<p>Another error log in the console, if it could help</p>
<p>Python 3.12.10 (main, Sep 21 2025, 23:13:54) [Clang 14.0.6 (<a href="https://github.com/tru/llvm-release-build" rel="noopener nofollow ugc">https://github.com/tru/llvm-release-build</a> 686807a176470032c208f27 on darwin</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-33957/SlicerANTsPy/lib/Slicer-5.9/qt-scripted-modules/ANTsRegistration.py”, line 341, in setup<br>
self.ui.outputForwardTransformComboBox.connect(<br>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>
AttributeError: ‘’ object has no attribute ‘outputForwardTransformComboBox’. Did you mean: ‘outputTransformComboBox’?<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-33957/SlicerANTsPy/lib/Slicer-5.9/qt-scripted-modules/ANTsRegistration.py”, line 522, in enter<br>
self.initializeParameterNode()<br>
File “/Applications/Slicer.app/Contents/Extensions-33957/SlicerANTsPy/lib/Slicer-5.9/qt-scripted-modules/ANTsRegistration.py”, line 564, in initializeParameterNode<br>
self.setParameterNode(<br>
File “/Applications/Slicer.app/Contents/Extensions-33957/SlicerANTsPy/lib/Slicer-5.9/qt-scripted-modules/ANTsRegistration.py”, line 605, in setParameterNode<br>
self.updateGUIFromParameterNode()<br>
File “/Applications/Slicer.app/Contents/Extensions-33957/SlicerANTsPy/lib/Slicer-5.9/qt-scripted-modules/ANTsRegistration.py”, line 630, in updateGUIFromParameterNode<br>
self.ui.outputForwardTransformComboBox.setCurrentNode(<br>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<br>
AttributeError: ‘’ object has no attribute ‘outputForwardTransformComboBox’. Did you mean: ‘outputTransformComboBox’?</p>
<p>philippe pellerin<br>
<a href="mailto:philippepellerin@me.com">philippepellerin@me.com</a></p>

---

## Post #35 by @jamesobutler (2025-09-22 14:35 UTC)

<p>What is the difference between SlicerAnts and SlicerAntsPy? They both contain a qt-scripted-module that is a file name <code>antsregistration.py</code>. I could see how that may mess up some loading module logic.</p>
<p>I am able to replicate the above mentioned traceback where it is getting confused of <code>outputTransformComboBox</code> from SlicerAnts and <code>outputForwardTransformComboBox</code> of SlicerAntsPy.</p>

---

## Post #36 by @muratmaga (2025-09-22 15:09 UTC)

<p>There is no reason to have AntsPy and Ants extensions simultaneously installed and I suspect thats the problem.</p>
<p>Antspy bring the full antspy package which is image quantification and segmentation libraries built on top of Ants. Ants extension only provides the AntsRegistration function.</p>
<p>While antspy does provide the same registration function we did not expose all possible parameters that one can possinbly pass to an ants registration call. So if the focus is single.pairwise registration, SlicerAnts extension is preferred.</p>
<p>If you need additional features such aa template building, groupwise, jacobian etc, you may use Antspy.</p>
<p>Having said that it might be good to have a check for ants extension checl in antspy and ask user to uninstall to use install antspy</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> what do you think?</p>

---

## Post #37 by @philippepellerin (2025-09-23 09:21 UTC)

<p>I built a template with ANTsPY. It worked fine, but the final result, even after iterations, is a bit blurred, and I can’t find my usual landmarks to orient the volume. Thus, for my research, going through skull segmentation and model creation is a better path to analysing craniofacial malformation. But thanks for suggesting this idea.</p>

---
