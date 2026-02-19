---
topic_id: 26344
title: "Nrrd Segmentation File Header"
date: 2022-11-21
url: https://discourse.slicer.org/t/26344
---

# NRRD segmentation file header

**Topic ID**: 26344
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/nrrd-segmentation-file-header/26344

---

## Post #1 by @Francesca_Lo_Iacono (2022-11-21 10:44 UTC)

<p>Hi! I’m developing an automatic segmentation algorithm on python and I am trying to export obtained segmentations in a .nrrd file. Looking at .nrrd file obtained from Slicer I can see some header I can’t understand how to include in the .nrrd file got in python.</p>
<p>Someone can help me finding how to include the right header in my .nrrd file?</p>

---

## Post #2 by @pieper (2022-11-21 19:15 UTC)

<p>You probably will want to use the SlicerIO package:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pypi.org/project/slicerio/">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="32" height="30">

      <a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">PyPI</a>
  </header>

  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.6fecba6f.jpg" class="thumbnail onebox-avatar" width="300" height="300">

<h3><a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">slicerio</a></h3>

  <p>Utilities for 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And set the custom metadata:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmentations.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmentations.html</a></p>

---
