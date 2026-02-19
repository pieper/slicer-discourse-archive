---
topic_id: 26050
title: "B Matrix Rotation"
date: 2022-11-03
url: https://discourse.slicer.org/t/26050
---

# B-matrix rotation

**Topic ID**: 26050
**Date**: 2022-11-03
**URL**: https://discourse.slicer.org/t/b-matrix-rotation/26050

---

## Post #1 by @batel (2022-11-03 12:04 UTC)

<p>Hi all,<br>
I wonder if there is a way of doing B-matrix rotation on slicer.<br>
I want to change my gradient directions according to the changes that were done in the registration of motion and deddy currents corrections. is it posible?<br>
Thanks,<br>
BY</p>

---

## Post #2 by @pieper (2022-11-03 12:36 UTC)

<p>These resources should help.  If you have rotated bvec files (e.g. from FSL eddy current correction) you can convert them to nrrd for use with ukf tractography and other tools in Slicer.</p>
<p><a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:Nrrd_format" class="onebox" target="_blank" rel="noopener">https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:Nrrd_format</a></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pnlbwh/conversion">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/95040f3ebb5e490ea0e9620c341640aca65546b491d4444fa03c1bbe9e52b1dc/pnlbwh/conversion" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pnlbwh/conversion" target="_blank" rel="noopener">GitHub - pnlbwh/conversion: Various mri conversion/modification scripts</a></h3>

  <p>Various mri conversion/modification scripts. Contribute to pnlbwh/conversion development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
