# How versatile is the HD Brain Extraction extension?

**Topic ID**: 43426
**Date**: 2025-06-19
**URL**: https://discourse.slicer.org/t/how-versatile-is-the-hd-brain-extraction-extension/43426

---

## Post #1 by @sulli419 (2025-06-19 17:06 UTC)

<p>Hi,</p>
<p>I am wondering how well the HD Brain Extraction extension might work on anatomical scans of mouse brains.  Has anyone tried this?  Were any efforts made to make this trained model more robust/generalizable/versatile, at least for different human datasets?  Are there other easy to use deep learning models in slicer that might work for mouse brains?</p>
<p>p.s., My old approach was just to install an extension and give it try, but this seemed like it was destabilizing slicer and also not all of the large extension files were uninstalling with slicer.  Hence why I’m inquiring first now.</p>
<p>Keep finding new things I love about slicer.  Your work is much appreciated!</p>
<p>Steve</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/lassoan/SlicerHDBrainExtraction?tab=readme-ov-file#hdbrainextraction">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerHDBrainExtraction?tab=readme-ov-file#hdbrainextraction" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/f4140c4e7db206f610adcd3febc14708/lassoan/SlicerHDBrainExtraction?tab=readme-ov-file#hdbrainextraction" class="thumbnail">

  <h3><a href="https://github.com/lassoan/SlicerHDBrainExtraction?tab=readme-ov-file#hdbrainextraction" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerHDBrainExtraction: 3D Slicer extension for accessing HD-BET brain...</a></h3>

    <p><span class="github-repo-description">3D Slicer extension for accessing HD-BET brain extraction tool for skull stripping in brain MRI images.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @sulli419 (2025-07-21 20:40 UTC)

<p>I finally got around to testing this.  I have to say it works surprisingly well on mouse brains, if others would like to try it out.  For a volume of 26 images it was about 90% accurate, with most the errors being on the Z edges.  It took one or two minutes to doctor up with the 3d brush and the mask was perfectly extracted.</p>
<p>By the way, I needed to increase the voxel size (at least by a factor of 10 isotropically) for the program to work (closer to human size).  This makes me think so long as you get the scaling right this method could work for any animal brain MR.</p>

---
