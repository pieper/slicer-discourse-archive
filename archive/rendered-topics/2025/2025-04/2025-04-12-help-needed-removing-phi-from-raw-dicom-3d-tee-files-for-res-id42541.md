# Help Needed: Removing PHI from Raw DICOM (3D TEE) Files for Research Collaboration. De-identification

**Topic ID**: 42541
**Date**: 2025-04-12
**URL**: https://discourse.slicer.org/t/help-needed-removing-phi-from-raw-dicom-3d-tee-files-for-research-collaboration-de-identification/42541

---

## Post #1 by @federica-pixel (2025-04-12 08:14 UTC)

<p>Hi everyone,</p>
<p>I’m currently working on a research project involving 3D transesophageal echocardiography (TEE) data. I’ve exported raw DICOM files from hospital imaging systems (GE and/or Philips), and these datasets are crucial for continuing my analysis and collaboration with external research partners.</p>
<p>However, I’m facing a serious issue: I’m unable to properly anonymize the raw DICOM files. Despite trying various tools, patient information such as name, surname, address, and other identifying data still remains either in the metadata or, in some cases, visibly embedded in the images themselves.</p>
<p>To proceed with my work in compliance with data protection standards and ethical requirements, I need to completely remove all personally identifiable information (PHI) from both the metadata and the image content.</p>
<p>Has anyone dealt with this issue before—particularly with raw 3D TEE DICOMs from GE or Philips systems? Any guidance on reliable anonymization tools or workflows would be incredibly appreciated.</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @pieper (2025-04-12 19:12 UTC)

<p>They may not be exactly what you need, but probably these are close.  Ultrasound DICOM is notoriously tricky to work with and there may be special cases.  SlicerHeart focuses on kids, so TTE rather than TEE, but maybe the scanner details are different.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/06c691be0022af397849cdbb2f0d8ea6/SlicerHeart/SlicerHeart" class="thumbnail">

  <h3><a href="https://github.com/SlicerHeart/SlicerHeart" target="_blank" rel="noopener">GitHub - SlicerHeart/SlicerHeart: 3D Slicer extension for cardiac analysis</a></h3>

    <p><span class="github-repo-description">3D Slicer extension for cardiac analysis</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerUltrasound/SlicerUltrasound">
  <header class="source">

      <a href="https://github.com/SlicerUltrasound/SlicerUltrasound" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/7c98bb01451ba98d6ae417a917f87ff1/SlicerUltrasound/SlicerUltrasound" class="thumbnail">

  <h3><a href="https://github.com/SlicerUltrasound/SlicerUltrasound" target="_blank" rel="noopener">GitHub - SlicerUltrasound/SlicerUltrasound: Modules for 3D Slicer </a></h3>

    <p><span class="github-repo-description">Modules for 3D Slicer </span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
