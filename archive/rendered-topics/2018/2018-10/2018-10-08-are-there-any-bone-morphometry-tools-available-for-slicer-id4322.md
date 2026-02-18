# Are there any bone morphometry tools available for Slicer?

**Topic ID**: 4322
**Date**: 2018-10-08
**URL**: https://discourse.slicer.org/t/are-there-any-bone-morphometry-tools-available-for-slicer/4322

---

## Post #1 by @muratmaga (2018-10-08 17:33 UTC)

<p>For example, is this implemented</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITKBoneMorphometry">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/InsightSoftwareConsortium/ITKBoneMorphometry" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/4caa46eda6a39d0dfb54849a6d2b561fc4cd6cd68534cb5e89552359b1f33a12/InsightSoftwareConsortium/ITKBoneMorphometry" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/InsightSoftwareConsortium/ITKBoneMorphometry" target="_blank" rel="noopener">GitHub - InsightSoftwareConsortium/ITKBoneMorphometry: ITK filters that...</a></h3>

  <p>ITK filters that quantify bone morphometry. Contribute to InsightSoftwareConsortium/ITKBoneMorphometry development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>or what would it take to make it available?</p>
<p>Best</p>

---

## Post #2 by @lassoan (2018-10-08 20:50 UTC)

<p>I think you can now bundle ITK remote modules into Slicer extensions - <a class="mention" href="/u/jcfr">@jcfr</a> can confirm. If not, then you can either get it implemented or wait for Slicer’s Python3 support (expected within about 6 months).</p>
<p>Once you have the algorithms available in Slicer, all you have to do is to expose features in a Python scripted module(s). Depending on how polished user interface you need, this could take 1-2 weeks to implement.</p>

---

## Post #3 by @pieper (2018-10-08 21:05 UTC)

<p>Or maybe <a class="mention" href="/u/thewtex">@thewtex</a>, <a class="mention" href="/u/bpaniagua">@bpaniagua</a>, and <a class="mention" href="/u/jbvimort">@jbvimort</a> are already planning to add this to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BoneTextureExtension">bone texture extension</a>?</p>

---

## Post #4 by @jcfr (2018-10-23 18:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>now bundle ITK remote modules into Slicer extension</p>
</blockquote>
</aside>
<p>This is indeed possible. Let me know if you have specific questions.</p>

---

## Post #5 by @muratmaga (2018-10-23 18:43 UTC)

<p>I am assuming this means building Slicer from scratch. Does the regular set of instructions apply, or is there something specific to make the ITK Bonemorphometry available?</p>

---

## Post #6 by @jcfr (2018-10-23 18:58 UTC)

<p>Since the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BoneTextureExtension">BoneTextureExtension</a> extension is already built daily and includes the <a href="https://github.com/Kitware/BoneTextureExtension/tree/master/SuperBuild"><code>ITKBoneMorphometry</code> and <code>ITKFeatureTexture</code> remote modules</a>, you could simply install the extension from within Slicer.</p>
<p>See <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-10-23&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=buildname&amp;compare1=63&amp;value1=BoneTextureExtension&amp;field2=groupname&amp;compare2=61&amp;value2=Extensions-Nightly">CDash build report</a></p>

---
