# Simultaneous segmentation of multiple vertebral bodies

**Topic ID**: 19697
**Date**: 2021-09-16
**URL**: https://discourse.slicer.org/t/simultaneous-segmentation-of-multiple-vertebral-bodies/19697

---

## Post #1 by @Siegmund_Lang (2021-09-16 08:49 UTC)

<p>Dear Slicer Support Team,</p>
<p>i am looking for a convenient method to simultaneously segment multiple vertebral bodies, similar as seen in this youtube tutorial on serial smooth of the segmentations:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="Wcz44sSCS9Y" data-video-title="How to serially smooth segmentations in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Wcz44sSCS9Y" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Wcz44sSCS9Y/maxresdefault.jpg" title="How to serially smooth segmentations in 3D Slicer" width="" height="">
  </a>
</div>

<p>Is there a tutorial video how to do so? The goal is to get a separate segmentation for each vertebral body.</p>
<p>Thank you very much.<br>
Siegmund</p>

---

## Post #2 by @dzenanz (2021-09-16 13:32 UTC)

<p>Depending on what you consider “convenient”, my PhD project could fit the bill. Here is a <a href="https://github.com/dzenanz/SpineSource" rel="noopener nofollow ugc">slightly updated version of source code on GitHub</a>, <a href="https://www.cg.informatik.uni-siegen.de/publicationPDFbyID?ID=603" rel="noopener nofollow ugc">paper</a> and <a href="https://www.cg.informatik.uni-siegen.de/en/spine-segmentation-and-analysis" rel="noopener nofollow ugc">project background</a>.</p>
<p>A group from Magdeburg continued research in the same direction, here are some papers:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pubmed.ncbi.nlm.nih.gov/26861655/">
  <header class="source">
      <img src="https://cdn.ncbi.nlm.nih.gov/coreutils/nwds/img/favicons/favicon.ico" class="site-icon" width="" height="">

      <a href="https://pubmed.ncbi.nlm.nih.gov/26861655/" target="_blank" rel="noopener nofollow ugc">PubMed</a>
  </header>

  <article class="onebox-body">
    <img src="https://cdn.ncbi.nlm.nih.gov/pubmed/persistent/pubmed-meta-image.png" class="thumbnail" width="" height="">

<h3><a href="https://pubmed.ncbi.nlm.nih.gov/26861655/" target="_blank" rel="noopener nofollow ugc">On computerized methods for spine analysis in MRI: a systematic review - PubMed</a></h3>

  <p>The diversity of MRI sequences and settings still poses challenges to computerized spine analysis. Further research is necessary to implement methods that are actually applicable in practice, e.g., in clinical routine or for study purposes....</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pubmed.ncbi.nlm.nih.gov/29512508/">
  <header class="source">
      <img src="https://cdn.ncbi.nlm.nih.gov/coreutils/nwds/img/favicons/favicon.ico" class="site-icon" width="" height="">

      <a href="https://pubmed.ncbi.nlm.nih.gov/29512508/" target="_blank" rel="noopener nofollow ugc">PubMed</a>
  </header>

  <article class="onebox-body">
    <img src="https://cdn.ncbi.nlm.nih.gov/pubmed/persistent/pubmed-meta-image.png" class="thumbnail" width="" height="">

<h3><a href="https://pubmed.ncbi.nlm.nih.gov/29512508/" target="_blank" rel="noopener nofollow ugc">Vertebral body segmentation in wide range clinical routine spine MRI data -...</a></h3>

  <p>These results illustrate the robustness of our segmentation approach towards the variety of MR image data, which is a pivotal aspect for clinical usefulness and reliable diagnosis.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.sciencedirect.com/science/article/abs/pii/S0169260718307417">
  <header class="source">
      <img src="https://sdfestaticassets-us-east-1.sciencedirectassets.com/shared-assets/13/images/favSD.ico" class="site-icon" width="" height="">

      <a href="https://www.sciencedirect.com/science/article/abs/pii/S0169260718307417" target="_blank" rel="noopener nofollow ugc">sciencedirect.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://ars.els-cdn.com/content/image/1-s2.0-S0169260719X00103-cov150h.gif" class="thumbnail" width="" height="">

<h3><a href="https://www.sciencedirect.com/science/article/abs/pii/S0169260718307417" target="_blank" rel="noopener nofollow ugc">Combining convolutional neural networks and star convex cuts for fast whole...</a></h3>

  <p>Background and Objective: We propose an automatic approach for fast vertebral body segmentation in three-dimensional magnetic resonance images of the …</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://link.springer.com/chapter/10.1007/978-3-030-32251-9_1">
  <header class="source">
      <img src="https://link.springer.com/oscar-static/images/favicons/springerlink/favicon-eb9f5576a3.ico" class="site-icon" width="48" height="48">

      <a href="https://link.springer.com/chapter/10.1007/978-3-030-32251-9_1" target="_blank" rel="noopener nofollow ugc">SpringerLink</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:153/232;"><img src="https://static-content.springer.com/cover/book/978-3-030-32251-9.jpg" class="thumbnail" width="153" height="232"></div>

<h3><a href="https://link.springer.com/chapter/10.1007/978-3-030-32251-9_1" target="_blank" rel="noopener nofollow ugc">A CNN-Based Framework for Statistical Assessment of Spinal Shape and...</a></h3>

  <p>The extraction of spines from medical records in a fast yet accurate way is a challenging task, especially for large data sets. Addressing this issue, we present a framework based on convolutional neural networks for the reconstruction of the spinal...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Spine segmentation from CT is easier and usually yields better results. References in the above papers are a good starting point.</p>
<p>A good general purpose tool which can be applied to spine segmentation is “grow from seeds” segmentation effect in Slicer’s SegmentEditor. Here is an example of seeds and the result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c21bd9f058a85bb57739afefad64c924db79fcc.jpeg" data-download-href="/uploads/short-url/40REOwD3rmRFj9udIE9Ud4coWBK.jpeg?dl=1" title="GrowCutSeeds" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c21bd9f058a85bb57739afefad64c924db79fcc_2_570x500.jpeg" alt="GrowCutSeeds" data-base62-sha1="40REOwD3rmRFj9udIE9Ud4coWBK" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c21bd9f058a85bb57739afefad64c924db79fcc_2_570x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c21bd9f058a85bb57739afefad64c924db79fcc_2_855x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c21bd9f058a85bb57739afefad64c924db79fcc_2_1140x1000.jpeg 2x" data-dominant-color="46464C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GrowCutSeeds</span><span class="informations">1920×1684 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d06e6dff927b60b2dc869fa44ff442c8d49ceee.jpeg" data-download-href="/uploads/short-url/dgXbTH3yOi6nl2FIWxB5w5dXv6C.jpeg?dl=1" title="GrowCutResults" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d06e6dff927b60b2dc869fa44ff442c8d49ceee_2_570x500.jpeg" alt="GrowCutResults" data-base62-sha1="dgXbTH3yOi6nl2FIWxB5w5dXv6C" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d06e6dff927b60b2dc869fa44ff442c8d49ceee_2_570x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d06e6dff927b60b2dc869fa44ff442c8d49ceee_2_855x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d06e6dff927b60b2dc869fa44ff442c8d49ceee_2_1140x1000.jpeg 2x" data-dominant-color="454348"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GrowCutResults</span><span class="informations">1920×1684 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>These seeds are placed just to demonstrate the method, I was not attempting to make a good segmentation. But I think this is a viable method, and it has been part of Slicer for a while now.</p>

---

## Post #3 by @Siegmund_Lang (2021-09-17 14:54 UTC)

<p>Dear Dženan Zukić,</p>
<p>thank you for the quick and substantiated answer. And congratulations on your most interesting PhD project. I am a trauma surgeon and we are initializing a project, aiming to integrate 3D segmentation in our clinical research. Your advice and the proposed papers help a lot.</p>
<p>I have found a slicer  extension for the automatic segmentation of the cervical spine. Would a similar feature be conceivable for the thoraco-lumbar spine?</p>

---

## Post #4 by @dzenanz (2021-09-17 15:02 UTC)

<p>I guess asking the author of this extension to add support for thoracic and lumbar spine would make sense. I don’t know whether he still actively works on the project or maintains this extension. You could perhaps ask him directly? His email address could be found in the <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCervicalSpine/commits/master" rel="noopener nofollow ugc">git log</a> of the extension. I don’t know whether he has a forum profile, and if so what is his username.</p>

---

## Post #5 by @lassoan (2021-09-17 19:43 UTC)

<aside class="quote no-group" data-username="Siegmund_Lang" data-post="1" data-topic="19697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/siegmund_lang/48/8753_2.png" class="avatar"> Siegmund_Lang:</div>
<blockquote>
<p>simultaneously segment multiple vertebral bodies, similar as seen in this youtube tutorial</p>
</blockquote>
</aside>
<p>We created that model using “Grow from seeds” effect, similarly to how <a class="mention" href="/u/dzenanz">@dzenanz</a> described above, with two additions for CT:</p>
<ul>
<li>On CT images you can see the facet joints as well, and there usually no clear separation between the vertebrae, so it is important to set an “Editable intensity range” (from about 150-250HU to maximum) using Threshold effect, to restrict region growing to bone region. The editable intensity range makes painting the seeds easier (you don’t need to worry about painting into soft tissue) and must be done before starting Grow from seeds.</li>
<li>Cancellous bone inside vertebrae have the same density as soft tissues, therefore the bones will appear hollow after segmentation. You can fill all internal holes using <a href="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d">this code snippet</a> (after clicking “Apply” in Grow from seeds effect).</li>
</ul>
<p>I captured a screen capture video of how I do this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="wMMi0QIrCvc" data-video-title="Semi-automatic vertebra segmentation on CT" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wMMi0QIrCvc" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wMMi0QIrCvc/maxresdefault.jpg" title="Semi-automatic vertebra segmentation on CT" width="" height="">
  </a>
</div>

<p>The goal of the video was to keep it short. As always, you can get more accurate segmentation by spending more time with reviewing and correcting automatic segmentation results.</p>

---
