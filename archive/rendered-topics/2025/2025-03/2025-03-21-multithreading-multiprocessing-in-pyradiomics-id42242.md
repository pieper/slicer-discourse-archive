# Multithreading/Multiprocessing in Pyradiomics

**Topic ID**: 42242
**Date**: 2025-03-21
**URL**: https://discourse.slicer.org/t/multithreading-multiprocessing-in-pyradiomics/42242

---

## Post #1 by @annapurna11 (2025-03-21 02:35 UTC)

<p>Hi everyone! I am working on a project focussed on extraction of radiomic features (GLCM features) for prostrate cancer diagnosis. (Voxel-based). The code is too slow and single-threaded. Scanning of a single image takes around 12 hours and not much CPU is being used up in the process either. I have been trying to figure out how to use the jobs parameter to make the code faster and multithreaded. Also I would like to know if there are other methods I can try to make the code run faster.</p>

---

## Post #2 by @pieper (2025-03-21 13:14 UTC)

<p>If you have several images to process you could try the parallel processing approach to launch python jobs in multiple processes.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/pieper/SlicerParallelProcessing">
  <header class="source">

      <a href="https://github.com/pieper/SlicerParallelProcessing" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/060e8176278e31ea0f53d9054a20760b/pieper/SlicerParallelProcessing" class="thumbnail">

  <h3><a href="https://github.com/pieper/SlicerParallelProcessing" target="_blank" rel="noopener">GitHub - pieper/SlicerParallelProcessing: Slicer modules for running subprocesses to operate...</a></h3>

    <p><span class="github-repo-description">Slicer modules for running subprocesses to operate on data in parallel</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
