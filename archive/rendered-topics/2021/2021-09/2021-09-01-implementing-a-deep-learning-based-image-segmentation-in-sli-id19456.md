# Implementing a deep learning based image segmentation in Slicer3D

**Topic ID**: 19456
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/implementing-a-deep-learning-based-image-segmentation-in-slicer3d/19456

---

## Post #1 by @Aamir_Khan (2021-09-01 08:02 UTC)

<p>Hello,</p>
<p>I am trying to develop a deep learning based image segmentation of pelvic bone region. During my search for open source training dataset I came across a paper which has already implemented a good strategy for doing so. The paper is implemented in Pytorch and makes use of MONAI framework in the process. I am attaching the link of the github repository.</p>
<p>[GitHub - ICT-MIRACLE-lab/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models”.]</p>
<p>(<a href="https://github.com/ICT-MIRACLE-lab/CTPelvic1K" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ICT-MIRACLE-lab/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bon</a>)</p>
<p>I wanted to ask as to how much time would it take to transfer the implementation from PYtorch format to start using it in Slicer3D for the segmentation purposes?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-09-01 14:11 UTC)

<p>You can use pytorch directly in Slicer now, so it should be pretty straightforward to bring that into Slicer.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/fepegar/SlicerPyTorch">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/fepegar/SlicerPyTorch" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/b4eb5349dd8502095aa720ba819bd2b8061706cf0205bedd3c8a93640e7db1b2/fepegar/SlicerPyTorch" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/fepegar/SlicerPyTorch" target="_blank" rel="noopener">GitHub - fepegar/SlicerPyTorch: This extension contains only a module with...</a></h3>

  <p>This extension contains only a module with some tools to install PyTorch inside Slicer, using the best possible version. - GitHub - fepegar/SlicerPyTorch: This extension contains only a module with...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
