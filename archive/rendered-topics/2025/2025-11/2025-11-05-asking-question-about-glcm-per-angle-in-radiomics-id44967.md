---
topic_id: 44967
title: "Asking question about GLCM per angle in radiomics"
date: 2025-11-05
url: https://discourse.slicer.org/t/44967
last_bumped: 2026-06-26T07:31:31.436Z
---

# Asking question about GLCM per angle in radiomics

**Topic ID**: 44967
**Date**: 2025-11-05
**URL**: https://discourse.slicer.org/t/asking-question-about-glcm-per-angle-in-radiomics/44967

---

## Post #1 by @Nicolas_hsieh (2025-11-05 13:00 UTC)

<p>Hello, I’m new to the Pyradiomics. Recently, I read the document of Pyradiomics. It seems that I can’t use Pyradiomics to calculate GLCM per angle(eg. energy per angles or entropy per angle). Is there any method to calculate GLCM per angle?</p>

---

## Post #2 by @aujinen (2026-06-25 13:30 UTC)

<p>Hello</p>
<p>I think your question might be related following URL;</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://groups.google.com/g/pyradiomics/c/s1tbbvPFgyk">
  <header class="source">
      <img src="https://www.gstatic.com/images/branding/product/1x/groups_32dp.png" class="site-icon" alt="" width="32" height="32">

      <a href="https://groups.google.com/g/pyradiomics/c/s1tbbvPFgyk" target="_blank" rel="noopener nofollow ugc">groups.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://groups.google.com/g/pyradiomics/c/s1tbbvPFgyk" target="_blank" rel="noopener nofollow ugc">Raw 2D (GLCM, GLRLM, etc) matrix</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I checked output of <code>featureClass.P_glcm</code> with following sample python code (2D, 4 directions).</p>
<p><a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/check_P_glcm.ipynb" rel="noopener nofollow ugc">https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/check_P_glcm.ipynb</a></p>
<p>I came across this recently while looking into whether it could be used for educational purposes. Although this question was asked over six months ago and I am unsure if this will be helpful, I wanted to leave a comment.</p>

---

## Post #3 by @aujinen (2026-06-26 02:24 UTC)

<p>The calculation results are provisional.<br>
For now, I have confirmed that there is relevant data inside that can be extracted.<br>
In this provisional version, the output is asymmetric, even though a symmetric GLCM is required.<br>
I am currently preparing an Excel worksheet for instructional purposes covering four directions (0–180°, 45–225°, 90–270°, and 135–215°).<br>
I believe further consideration is needed before presenting this to students.</p>

---

## Post #4 by @aujinen (2026-06-26 03:43 UTC)

<p>After checking with GitHub Copilot, I added code to save internal parameters to a part of glcm.py and placed it in the workspace folder.</p>
<p>In the code within the workspace, you can call the modified glcm.py that uses <code>from glcm import RadiomicsGLCM</code> instead of <code>from radiomics.glcm import RadiomicsGLCM</code>.This might allow us to verify the angle information (depending on the level of problem identification in Copilot).</p>
<p>I just learned about the existence of the symmetrization parameter <code>weightingNorm</code> and set it, but I found that the angle information disappears when applied to check_GLCM_raw.ipynb.</p>
<p>Further verification seems necessary.</p>

---

## Post #5 by @aujinen (2026-06-26 07:31 UTC)

<p>sorry</p>
<p>135–215° → 135–315°</p>

---
