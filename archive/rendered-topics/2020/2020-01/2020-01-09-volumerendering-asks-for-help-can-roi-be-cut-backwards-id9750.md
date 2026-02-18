# Volumerendering asks for help: can roi be cut backwards? 

**Topic ID**: 9750
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/volumerendering-asks-for-help-can-roi-be-cut-backwards/9750

---

## Post #1 by @Shicong (2020-01-09 06:45 UTC)

<p>I asked if the roi-cut of the volumerender-like body could be reversed? making the panel visible outside and invisible inside. I studied the code, or not, thanks for the support, thanks!<br>
As shown in the following figure, add two lines of code in the red box, or not. ???!<br>
<a href="/404" data-orig-href="upload://xpnYNw1tLMYWlpRLd43BI9ekZTq.png">pic1|690x354</a> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfd74d3344081ec005e12bebedc171afe4659196.png" data-download-href="/uploads/short-url/rn6tEGZIHHGMZzsPKnuYAWlpoF0.png?dl=1" title="pic2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfd74d3344081ec005e12bebedc171afe4659196_2_690x245.png" alt="pic2" data-base62-sha1="rn6tEGZIHHGMZzsPKnuYAWlpoF0" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfd74d3344081ec005e12bebedc171afe4659196_2_690x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfd74d3344081ec005e12bebedc171afe4659196_2_1035x367.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfd74d3344081ec005e12bebedc171afe4659196_2_1380x490.png 2x" data-dominant-color="C4C2DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic2</span><span class="informations">1608×573 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Shicong (2020-01-09 07:32 UTC)

<p>vtkmrmlannotationroid pairs like have inside out flag, but also should have outside in flag, but no, is it<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bfa27271f83c80ead46ab35b708c723b9e15663.png" data-download-href="/uploads/short-url/6h2tQCYbWbdJrkhijBSLvQdRz3R.png?dl=1" title="pic3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bfa27271f83c80ead46ab35b708c723b9e15663.png" alt="pic3" data-base62-sha1="6h2tQCYbWbdJrkhijBSLvQdRz3R" width="690" height="249" data-dominant-color="2F2E2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic3</span><span class="informations">1177×426 47.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2020-01-09 13:43 UTC)

<p>We don’t have that feature exposed in the UI. You would need to provide a custom shader something like what’s described below.  It’s possible but not integrated in the app.</p>
<div class="lazyYT" data-youtube-id="yiEI_yBMu8k" data-youtube-title="SlicerPRISM 2018 06 28" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/MultiVolumeRendering/README.md" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/MultiVolumeRendering/README.md" target="_blank">NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/MultiVolumeRendering/README.md</a></h4>
<pre><code class="lang-md">Back to [Projects List](../../README.md#ProjectsList)

# Programmable MultiVolume Rendering Project

## Key Investigators

- Simon Drouin (MNI)
- Csaba Pinter (Queen's)
- Steve Pieper (Isomics)
- Jean-Christophe Fillion-Robin (Kitware)


# Project Description

## Objective

* Review the newly exposed GLSL hooks in VTK as a mechanism to add features to Slicer's Volume Rendering 
* Possible features to explore
  * Optimized performance/quality for multiple overlapping volumes
  * Custom clipping or other rendering features
</code></pre>

  This file has been truncated. <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW28_2018_GranCanaria/Projects/MultiVolumeRendering/README.md" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Shicong (2020-01-10 01:59 UTC)

<p>Thank you very much, I wish you a happy working life! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---
