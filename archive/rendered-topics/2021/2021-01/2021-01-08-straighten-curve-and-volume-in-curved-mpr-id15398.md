---
topic_id: 15398
title: "Straighten Curve And Volume In Curved Mpr"
date: 2021-01-08
url: https://discourse.slicer.org/t/15398
---

# Straighten curve and volume in curved mpr

**Topic ID**: 15398
**Date**: 2021-01-08
**URL**: https://discourse.slicer.org/t/straighten-curve-and-volume-in-curved-mpr/15398

---

## Post #1 by @yee_lu (2021-01-08 04:13 UTC)

<p>hello everyone! When i use curved planner reformat and I straighten the curve and volume , I got this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cfdd08cbcfb460b2933947177726a6d81e0e0bf.png" alt="image" data-base62-sha1="1QVwyaTk8zJjls2SxnMpkhRQpdB" width="91" height="316"><br>
How can I get a regular line?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-01-08 22:20 UTC)

<p>This probably happens because the mapping between the original and straightened volumes is ambiguous. See instructions for how to set reformatting parameters to avoid this:</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/PerkLab/SlicerSandbox#adjust-reformatting-parameters-for-robust-mapping" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/31492031?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/PerkLab/SlicerSandbox#adjust-reformatting-parameters-for-robust-mapping" target="_blank" rel="noopener">PerkLab/SlicerSandbox - Adjust reformatting parameters for robust mapping</a></h3>


  <p><span class="label1">Collection of utilities that are not polished implementations but can be useful to users</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
