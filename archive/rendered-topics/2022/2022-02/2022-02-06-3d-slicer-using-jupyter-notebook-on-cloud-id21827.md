# 3D slicer using Jupyter notebook on cloud

**Topic ID**: 21827
**Date**: 2022-02-06
**URL**: https://discourse.slicer.org/t/3d-slicer-using-jupyter-notebook-on-cloud/21827

---

## Post #1 by @kianoosh_kargar (2022-02-06 21:15 UTC)

<p>I found that I couldn’t install 3D slicer on my local pc, but I am able to run it on binder from here:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/SlicerNotebooks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/SlicerNotebooks" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/9d8292f15bdd8c02bda86da09b82d51b172f50b9765b4dd32b2883045e201af1/Slicer/SlicerNotebooks" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/SlicerNotebooks" target="_blank" rel="noopener nofollow ugc">GitHub - Slicer/SlicerNotebooks: Examples that illustrate how to use 3D...</a></h3>

  <p>Examples that illustrate how to use 3D Slicer via Jupyter notebooks in Python - GitHub - Slicer/SlicerNotebooks: Examples that illustrate how to use 3D Slicer via Jupyter notebooks in Python</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
But I want to know that is there any tutorial for using 3D Slicer in a jupyter notebook? Is there any difference between the performance of using 3D slicer locally and using Jupyter notebook?</p>

---

## Post #2 by @lassoan (2022-02-10 05:39 UTC)

<p>Performance depends on the computer where you run the Slicer (kernel). If you run the kernel on your computer then there is no performance difference. If you run it on the free <code>binder</code> service then it will be slow, as they don’t give you a very powerful computer and the network bandwidth is limited.</p>
<p>Convenience functions that are specifically developed for Slicer Jupyter notebooks are described on the <a href="https://github.com/Slicer/SlicerJupyter">extension’s project page</a> and API documentation in the <a href="https://github.com/Slicer/SlicerJupyter/tree/master/JupyterNotebooks/JupyterNotebooksLib">Python scripts</a> and demonstrated in the <a href="https://github.com/Slicer/SlicerNotebooks">example notebooks</a>. If you have any questions then you can ask them here.</p>
<p>I’ve updated SlicerJupyter to use the latest xeus-python kernel, so for a few days there may be  I’ll test the changes and fix any errors that comes up in the next few days.</p>

---

## Post #3 by @kianoosh_kargar (2022-02-15 14:34 UTC)

<p>Thank you very mucch for your comprehensive answer</p>

---
