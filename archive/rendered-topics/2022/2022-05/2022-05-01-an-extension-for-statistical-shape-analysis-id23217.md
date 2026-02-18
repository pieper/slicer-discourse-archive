# An extension for Statistical shape analysis

**Topic ID**: 23217
**Date**: 2022-05-01
**URL**: https://discourse.slicer.org/t/an-extension-for-statistical-shape-analysis/23217

---

## Post #1 by @gaoyi.cn (2022-05-01 13:08 UTC)

<p>Dear All,</p>
<p>I’m proposing to add an extension that performs the Statistical shape analysis using the 3D Poisson equations.</p>
<p>The repository is at:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/gaoyi/SPoM">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/gaoyi/SPoM" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/45e6228c199d618b6152715d6b9e3770f54c127e3f5dc0b6ad3d8c0993d28959/gaoyi/SPoM" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/gaoyi/SPoM" target="_blank" rel="noopener nofollow ugc">GitHub - gaoyi/SPoM: Statistical Shape Analysis using 3D Poisson Equation---A...</a></h3>

  <p>Statistical Shape Analysis using 3D Poisson Equation---A Quantitatively Validated Approach - GitHub - gaoyi/SPoM: Statistical Shape Analysis using 3D Poisson Equation---A Quantitatively Validated A...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The paper is:<br>
Gao Y, Bouix S. Statistical Shape Analysis using 3D Poisson Equation—A Quantitatively Validated Approach. Medical Image Analysis. 2016 Jan 15.</p>
<p>There is already SPHARM-PDM for shape analysis in the extension and adding this new one would provide another module to compare.</p>
<p>I’m hoping to add this through the extension management system and would like to hear about your suggestions/opinions.</p>
<p>Thanks!<br>
yi</p>

---

## Post #2 by @pieper (2022-05-02 16:43 UTC)

<p>Hi Yi -</p>
<p>That sounds great <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> I don’t do shape analysis myself but we see a lot of questions here on the forum so I know there’s interest.</p>

---

## Post #3 by @muratmaga (2022-05-02 17:15 UTC)

<aside class="quote no-group" data-username="gaoyi.cn" data-post="1" data-topic="23217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi.cn/48/1422_2.png" class="avatar"> gaoyi.cn:</div>
<blockquote>
<p>I’m hoping to add this through the extension management system and would like to hear about your suggestions/opinions.</p>
</blockquote>
</aside>
<p>There are a number of other shape analysis packages, besides SALT/spharm.</p>
<p>SlicerMorph extension has a <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/GPA#readme">Generalized Procrustes Analysis</a> module for landmark-based analysis. And <a href="https://toothandclaw.github.io/how-to-use/">Auto3Dgm extension</a> provides a fully automated way of finding correspondence 3D shapes that do not yield itself classical landmark-based analysis. The output of the auto3Dgm, which are dense points, can be read by our GPA module for interactive PCA decomposition and variance visualization.</p>
<p>So your extension will definitely strengthen the growing number of shape analysis tools within Slicer.</p>

---

## Post #4 by @gaoyi.cn (2022-05-03 06:28 UTC)

<p>Hi,</p>
<p>Thank you so much for your suggestion. Yes, one thing i found amazing about the field of statistical shape analysis when i started working on that guided by Sylvain Bouix back ten years ago was that, the researchers in this field tend to embrace the open source concept a lot. This was very helpful when we were performing the quantitative comparison/analysis among several widely used shape analysis algorithms. we open sourced the Poisson equation based algorithm when the algorithm was publish. However i think on Slicer’s platform, the algorithm should be much easier to be used than a piece of standalone software.</p>
<p>Best,<br>
yi</p>

---

## Post #5 by @gaoyi.cn (2022-05-03 06:29 UTC)

<p>Hi Steve,</p>
<p>Thank you! I’ll work on that! currently it’s a standalone cxx project and i’ll make it a CLI first. I’ll update this thread once i get any progress.</p>
<p>Best,<br>
yi</p>

---

## Post #6 by @lili-yu22 (2024-02-01 01:21 UTC)

<p>teacher gaoyi：<br>
can this extension use?</p>

---
