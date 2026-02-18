# Issues loading own nrrd file into SlicerWeb Jupyter(Binder tutorial)

**Topic ID**: 12679
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/issues-loading-own-nrrd-file-into-slicerweb-jupyter-binder-tutorial/12679

---

## Post #1 by @allihuwa (2020-07-22 13:43 UTC)

<p>Hello,</p>
<p>I am trying to load my own nrrd file to be able to manipulate a volume rendering through the slicerweb notebook extension that runs on jupyter.</p>
<p>I am trying to change this example code given on this tutorial:<br>
</p><aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://mybinder.org/static/favicon.ico?v=7102bb857703a0fece6d039a6777fc3f" class="site-icon" width="51" height="51">
      <a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb" target="_blank" rel="nofollow noopener">mybinder.org</a>
  </header>
  <article class="onebox-body">
    <img src="https://mybinder.org/static/images/logo_square.png" class="thumbnail onebox-avatar" width="217" height="217">

<h3><a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb" target="_blank" rel="nofollow noopener">GitHub: slicer/SlicerNotebooks/master</a></h3>

<p>Click to run this interactive environment. From the Binder Project: Reproducible, sharable, interactive computing environments.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>But when I change the download url, and filename to my own github link, I get stuck at the nodeNames attribute and list index. I keep getting an error message saying “list index out of range” but when I check the nrrd file on my downloaded slicer version, there is a volume node present when I check the volume rendering module. Is there a specific renaming or something I have to do in this module before I save my nrrd file for this to work?</p>

---

## Post #2 by @lassoan (2020-07-22 14:09 UTC)

<p>Can you post the code snippet that does not work?</p>

---

## Post #3 by @allihuwa (2020-07-23 10:11 UTC)

<p>Hello Iassoan, thanks for the quick reply. After trying around the solution ended up being changing the volume node name and nrrd filename, I guess I was using special characters which didn’t want to work.</p>
<p>Thanks again!</p>

---
