---
topic_id: 7417
title: "Fmri Module Remember Fmriengine"
date: 2019-07-04
url: https://discourse.slicer.org/t/7417
---

# fMRI module? Remember FMRIEngine?

**Topic ID**: 7417
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/fmri-module-remember-fmriengine/7417

---

## Post #1 by @cutkiller (2019-07-04 17:05 UTC)

<p>A few years back</p>
<p><a href="https://www.slicer.org/wiki/Slicer:Slicer2.6_Release_Notes#FMRIEngine" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Slicer:Slicer2.6_Release_Notes#FMRIEngine</a></p>
<p>FMRIEngine was a module in Slicer. Any idea what happened to it? Was it taken out? Any way of analyzing fMRI data in Slicer nowadays?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2019-07-07 16:06 UTC)

<p>Hi - We took out the fMRIEngine because there there were (and still are) so many free packages that specialize in fMRI processing and they typically generate statistical maps that can be used directly in Slicer for visualization and multimodal analysis.</p>
<p>Now that Slicer’s Preview builds can install most python packages, you can run <code>pip_install('nipy')</code> to get <a href="https://nipy.org/" rel="nofollow noopener">nipy</a>.  I haven’t used it for anything, but I can confirm it installs and imports for me (on mac) so that could be a promising direction to explore.</p>

---
