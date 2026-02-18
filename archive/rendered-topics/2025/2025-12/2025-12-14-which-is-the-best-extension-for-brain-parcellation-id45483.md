# Which is the best extension for Brain parcellation?

**Topic ID**: 45483
**Date**: 2025-12-14
**URL**: https://discourse.slicer.org/t/which-is-the-best-extension-for-brain-parcellation/45483

---

## Post #1 by @Suhaim (2025-12-14 09:57 UTC)

<p>Hi,<br>
Is there any extension in 3D-Slicer which offers <strong>automated brain segmentation</strong> for parts such as - Amygdala, Hippocampus, Insula etc.? Which extension has the best accuracy?<br>
I was able to find <a href="https://github.com/HOA-2/SlicerNeuroSegmentation/tree/main" rel="noopener nofollow ugc">SlicerNeuroSegmentation</a>, but it seems to have a dependency on FreeSurfer and I was wondering if a more stand-alone module exists in 3d-Slicer.<br>
Thanks!</p>

---

## Post #2 by @pieper (2025-12-14 14:49 UTC)

<p>I think FreeSurfer with <a href="https://github.com/PerkLab/SlicerFreeSurfer">SlicerFreeSurfer</a> is your best bet, especially the new <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/SuperSynth">SuperSynth</a> tool to handle pretty much any brain scan.  It’s not integrated directly with Slicer but it’s easy to install and use on it’s own.</p>
<p>Here’s an example applying SuperSynth to the MRHead SampleData that includes a color table to use if loading the nifti file directly.</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/11DS7pSSIdOaT9zB0xJ4-kDHzAFuhIssI/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/11DS7pSSIdOaT9zB0xJ4-kDHzAFuhIssI/view?usp=sharing" target="_blank" rel="noopener">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/11DS7pSSIdOaT9zB0xJ4-kDHzAFuhIssI/view?usp=sharing" target="_blank" rel="noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/11DS7pSSIdOaT9zB0xJ4-kDHzAFuhIssI/view?usp=sharing" target="_blank" rel="noopener">MRHead-SuperSynth.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The results look good to me, especially considering this is a scan from over 20 years ago.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2a090a3898181f248e6b87b1de89f0a3dfd908f.jpeg" data-download-href="/uploads/short-url/pucZUPGhiDjDqkdMy0KwuTNAq6z.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a090a3898181f248e6b87b1de89f0a3dfd908f_2_690x400.jpeg" alt="image" data-base62-sha1="pucZUPGhiDjDqkdMy0KwuTNAq6z" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a090a3898181f248e6b87b1de89f0a3dfd908f_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a090a3898181f248e6b87b1de89f0a3dfd908f_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2a090a3898181f248e6b87b1de89f0a3dfd908f_2_1380x800.jpeg 2x" data-dominant-color="605555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1542×894 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Suhaim (2025-12-15 05:14 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, thanks for the quick reply. I will use this extension and get back to you.<br>
It seems a standalone extension in 3D-Slicer doesn’t exist as of now for brain parcellation?</p>

---
