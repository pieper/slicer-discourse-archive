# Export nrrd file from mhd file for 600 patients

**Topic ID**: 36638
**Date**: 2024-06-07
**URL**: https://discourse.slicer.org/t/export-nrrd-file-from-mhd-file-for-600-patients/36638

---

## Post #1 by @hk_y (2024-06-07 09:37 UTC)

<p>Operating system: mac os python 3.12<br>
Slicer version:4.8.1<br>
Expected behavior:I’ve 600 patients’ segmentation results of mhd/zraw files. I want to export them to NRRD files in 3D Slicer. However, applying this operation to each patient individually would be too time-consuming. Do you have any suggestions? I want use python to solve this problem.</p>

---

## Post #2 by @pieper (2024-06-07 09:52 UTC)

<p>This would be a pretty simple script - have you looked at examples in the script repository?  Or you could ask a chatbot for advice and the come back here if you have specific questions.</p>

---

## Post #3 by @hk_y (2024-06-07 10:28 UTC)

<p>I have read the script repository, but I still have some problems. Could you please point out the specific script to me from the script repository, I will add the loops to it later. Thanks so much.</p>

---

## Post #4 by @muratmaga (2024-06-07 17:20 UTC)

<p>This looks like what you need.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pypi.org/project/slicerio/">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.35549fe8.ico" class="site-icon" width="32" height="30">

      <a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">PyPI</a>
  </header>

  <article class="onebox-body">
    <img width="300" height="300" src="https://pypi.org/static/images/twitter.abaf4b19.webp" class="thumbnail onebox-avatar">

<h3><a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">slicerio</a></h3>

  <p>Utilities for 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Read the files and write them to the new format and loop over your file list.</p>

---

## Post #5 by @hk_y (2024-06-13 09:18 UTC)

<p>Thanks！ It helps a lot!</p>

---
