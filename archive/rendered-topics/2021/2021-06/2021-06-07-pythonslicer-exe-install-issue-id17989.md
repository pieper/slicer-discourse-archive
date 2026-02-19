---
topic_id: 17989
title: "Pythonslicer Exe Install Issue"
date: 2021-06-07
url: https://discourse.slicer.org/t/17989
---

# Pythonslicer.exe install issue

**Topic ID**: 17989
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/pythonslicer-exe-install-issue/17989

---

## Post #1 by @user_ghost (2021-06-07 05:39 UTC)

<p>when i used pythonslicer.exe to install a package called probreg  and it shows there is no a file called python.h<br>
how can i resolve this problems<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ac00eceea3edb09035a1e18e0eec1b966b9b158.png" data-download-href="/uploads/short-url/1x6fUU8p9oDiotEDsLlS5P3vFHO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ac00eceea3edb09035a1e18e0eec1b966b9b158.png" alt="image" data-base62-sha1="1x6fUU8p9oDiotEDsLlS5P3vFHO" width="690" height="281" data-dominant-color="180C0D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1318×537 7.51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-06-07 18:46 UTC)

<p>This means that the Python package maintainer did not provide binaries (“wheels”). In general, this indicates that the package developer did not have sufficient time or knowledge to provide readily usable version of the software (just provides the source code and delegates the task of building the package to the user).</p>
<p>As a workaround, you can install a standard (or anaconda/miniconda) Python-3.6.7 environment and install the package there. If the package can be built in these environments, the created binaries will be available in other environments, such as for 3D Slicer.</p>
<p>However, in general, I would recommend to find alternative packages that are better maintained.</p>

---
