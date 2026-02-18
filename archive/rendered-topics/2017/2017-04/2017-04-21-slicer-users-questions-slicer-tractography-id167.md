# [slicer-users] questions Slicer Tractography

**Topic ID**: 167
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/slicer-users-questions-slicer-tractography/167

---

## Post #1 by @ihnorton (2017-04-21 16:06 UTC)

<p><code>from MSc. Alberto Villagrán on slicer-users:</code></p>
<p>Hello</p>
<p>I am working with Tractography module of 3DSlicer in wrist. do you have<br>
any protocol of Quality Assurance or validation of the represented tracts?</p>
<p>Thanks for your attention</p>
<p>Best regards.</p>
<p>MSc. Alberto Villagrán.</p>

---

## Post #2 by @ihnorton (2017-04-21 16:15 UTC)

<p>Hi Alberto,</p>
<p>Visual inspection of both tractography and the underlying tensor glyphs is recommended. For tensor glyphs, use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Volumes">Volumes module</a> to enable “Glyphs on Slices Display”:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a16810acf219da1677cdd3a689d992453472a963.png" alt="image" data-base62-sha1="n1RPxpUZzPaOtUMgGKMCTyauSGL" width="202" height="167"></p>
<p>As far as validation, that’s a complicated subject. Various groups have done ex-vivo work with tracers and comparison of histologically-derived white matter to tractography. Here are two papers that come to mind immediately, I’m sure you can find more by looking at the citations for these (and similar keywords):</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pubmed.ncbi.nlm.nih.gov/17604650/">
  <header class="source">
      <img src="https://cdn.ncbi.nlm.nih.gov/coreutils/nwds/img/favicons/favicon.ico" class="site-icon" width="" height="">

      <a href="https://pubmed.ncbi.nlm.nih.gov/17604650/" target="_blank" rel="noopener">PubMed</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://cdn.ncbi.nlm.nih.gov/pubmed/persistent/pubmed-meta-image-v2.jpg" class="thumbnail">

<h3><a href="https://pubmed.ncbi.nlm.nih.gov/17604650/" target="_blank" rel="noopener">Comparison of fiber tracts derived from in-vivo DTI tractography with 3D...</a></h3>

  <p>Since the introduction of diffusion weighted imaging (DWI) as a method for examining neural connectivity, its accuracy has not been formally evaluated. In this study, we directly compared connections that were visualized using injected neural tract...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3773464/">
  <header class="source">
      <img src="https://www.ncbi.nlm.nih.gov/coreutils/nwds/img/favicons/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3773464/" target="_blank" rel="noopener">PubMed Central (PMC)</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://www.ncbi.nlm.nih.gov/corehtml/pmc/pmcgifs/pmc-card-share.jpg?_=0" class="thumbnail">

<h3><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3773464/" target="_blank" rel="noopener">The Geometric Structure of the Brain Fiber Pathways</a></h3>

  <p>The structure of the brain as a product of morphogenesis is difficult to reconcile with the observed complexity of cerebral connectivity. We therefore analyzed relationships of adjacency and crossing between cerebral fiber pathways in four nonhuman...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
