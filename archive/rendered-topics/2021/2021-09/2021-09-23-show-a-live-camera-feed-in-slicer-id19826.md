# Show a live camera feed.in slicer

**Topic ID**: 19826
**Date**: 2021-09-23
**URL**: https://discourse.slicer.org/t/show-a-live-camera-feed-in-slicer/19826

---

## Post #1 by @Chintha_Siva_Prasad (2021-09-23 14:13 UTC)

<p>I am getting real time images from a camera. How can I show them in slicer three d windows? If I try to use load volume function then we will be loaded with a huge number of volumes. So is there a way to just update an image that is already present in slicer. And can we show a image that is opened in python script.</p>

---

## Post #2 by @pll_llq (2021-09-23 20:08 UTC)

<p>You might want to look at how streaming with Plus Toolkit and OpenIGTLink works.</p>
<p><a href="https://plustoolkit.github.io/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://plustoolkit.github.io/</a><br>
<a href="http://openigtlink.org/" class="onebox" target="_blank" rel="noopener nofollow ugc">http://openigtlink.org/</a></p>

---

## Post #3 by @Chintha_Siva_Prasad (2021-09-24 01:24 UTC)

<p>Can I get Script documentation for these libraries??</p>

---

## Post #4 by @lassoan (2021-09-24 02:35 UTC)

<p>There is no need for scripting (at least to get started). You create your whole system just by using the GUI, set up connections, specify configuration files, etc. and just save the scene. To start streaming and show the data all you need is to load that scene. Tutorials are available <a href="http://www.slicerigt.org/wp/user-tutorial/">here</a>.</p>

---

## Post #5 by @Chintha_Siva_Prasad (2021-09-24 03:26 UTC)

<p>I want to automate the things sir, so I require scripts for my purpose.</p>

---

## Post #6 by @lassoan (2021-09-24 05:01 UTC)

<p>All you need in your script is to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadScene">load the scene</a> that you prepared.</p>
<p>At this level there is step-by-step tutorial and no documentation is generated but you can find description of classes and methods where they are declared (in header files in C++, in the py files in Python). You are also expected to learn from examples, and by reading code, and asking specific questions.</p>
<p>You can find the source code of some existing applications in these repositories:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/LumpNav">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/LumpNav" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/43381c470ee918f6ac860644a72da70fa53dc5874180716315eda0387e9064af/SlicerIGT/LumpNav" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/LumpNav" target="_blank" rel="noopener">GitHub - SlicerIGT/LumpNav: Slicer extension for ultrasound-guided breast...</a></h3>

  <p>Slicer extension for ultrasound-guided breast tumor resection (lumpectomy) - GitHub - SlicerIGT/LumpNav: Slicer extension for ultrasound-guided breast tumor resection (lumpectomy)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/ExampleGuideletExtension">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/ExampleGuideletExtension" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/0e0e82c761f035c76ea0f2712b119b235c3515be8248d41a86b26fa488d509b4/SlicerIGT/ExampleGuideletExtension" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/ExampleGuideletExtension" target="_blank" rel="noopener">GitHub - SlicerIGT/ExampleGuideletExtension</a></h3>

  <p>Contribute to SlicerIGT/ExampleGuideletExtension development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/OMTCentralLineTraining">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/OMTCentralLineTraining" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/3cab662e8be90afba83a16d2fb2385313e10e7a5f412417d27092c7604491e3d/SlicerIGT/OMTCentralLineTraining" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/OMTCentralLineTraining" target="_blank" rel="noopener">GitHub - SlicerIGT/OMTCentralLineTraining: Inexpensive open-source system for...</a></h3>

  <p>Inexpensive open-source system for practicing hand-hand coordination for US guided needle insertions. - GitHub - SlicerIGT/OMTCentralLineTraining: Inexpensive open-source system for practicing hand...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/CathNav">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/CathNav" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/76d7dbdde55ac4f27a49a18ebf350c65f261e5846894a753b4ee255995a06472/SlicerIGT/CathNav" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/CathNav" target="_blank" rel="noopener">GitHub - SlicerIGT/CathNav: A guidelet for 3D Slicer for needle guidance in...</a></h3>

  <p>A guidelet for 3D Slicer for needle guidance in breast brachytherapy (catheter navigation). - GitHub - SlicerIGT/CathNav: A guidelet for 3D Slicer for needle guidance in breast brachytherapy (cathe...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/UsNeedleGuide">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/UsNeedleGuide" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/2e64289086cad16e4f469a0de7277fd32f1f1ce365f36a1c1f120c91af55f0fd/SlicerIGT/UsNeedleGuide" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/UsNeedleGuide" target="_blank" rel="noopener">GitHub - SlicerIGT/UsNeedleGuide: Software for mechanical needle guide</a></h3>

  <p>Software for mechanical needle guide. Contribute to SlicerIGT/UsNeedleGuide development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
