# Segmenting t2 mri lesions

**Topic ID**: 37061
**Date**: 2024-06-27
**URL**: https://discourse.slicer.org/t/segmenting-t2-mri-lesions/37061

---

## Post #1 by @cueball2001 (2024-06-27 08:38 UTC)

<p>Hello</p>
<p>Im new here and a complete newbie to all of this so please explain in laymen terms please lol</p>
<p>What i am trying to do is on my brain mri there is quite a few lesions so what i would like to is segment the grey and white matter and then the lesions in the white matter i have tried a few ways which is very time consuming and results are not great.</p>
<p>Thanks in advance<br>
Stewart</p>

---

## Post #2 by @pieper (2024-06-27 12:11 UTC)

<p>You could start with SynthSeg, which works well but wasn’t trained on anything with lesions, so using the results of that you could go in and edit with threshold to add in the lesions.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/BBillot/SynthSeg?tab=readme-ov-file#try-it-in-one-command-">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/BBillot/SynthSeg?tab=readme-ov-file#try-it-in-one-command-" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/fb246c53aab12e48708d93950da2af35b1e6663218ca6cf7ca92bc30bd96ff0f/BBillot/SynthSeg" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/BBillot/SynthSeg?tab=readme-ov-file#try-it-in-one-command-" target="_blank" rel="noopener">GitHub - BBillot/SynthSeg: Contrast-agnostic segmentation of MRI scans</a></h3>

  <p>Contrast-agnostic segmentation of MRI scans. Contribute to BBillot/SynthSeg development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
