---
topic_id: 44967
title: "Asking question about GLCM per angle in radiomics"
date: 2025-11-05
url: https://discourse.slicer.org/t/44967
last_bumped: 2026-06-29T10:32:00.276Z
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

## Post #6 by @aujinen (2026-06-27 21:49 UTC)

<p>I modified the local <code>glcm.py</code> file within the workspace to enable the extraction of angular information and unnormalized GLCMs. Although I had assumed the matrices were unsymmetric, verification of the results revealed that the order of the array elements differed from that of a standard GLCM. This was confirmed by comparing the output with results from simulations performed using Julia’s <code>radiomics.jl</code> and Excel.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/normal_ordered_GLCM_sample.png">
  <header class="source">

      <a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/normal_ordered_GLCM_sample.png" target="_blank" rel="noopener nofollow ugc">github.com/aujinen/pyradiomics_edu</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/normal_ordered_GLCM_sample.png" target="_blank" rel="noopener nofollow ugc">workspace/normal_ordered_GLCM_sample.png</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/normal_ordered_GLCM_sample.png" rel="noopener nofollow ugc"><code>master</code></a>
</div>


  This file is binary. <a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/normal_ordered_GLCM_sample.png" target="_blank" rel="noopener nofollow ugc">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/check_P_glcm.ipynb" rel="noopener nofollow ugc">https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/check_P_glcm.ipynb</a></p>

---

## Post #7 by @aujinen (2026-06-28 01:33 UTC)

<p>I have updated the Excel file containing the explanation of the “weightingNorm” parameter for Japanese students.</p>
<p>A summarized version in English (PDF) has also been posted in the same location.</p>
<aside class="onebox pdf" data-onebox-src="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB/blob/master/GLCM-example.pdf">
  <header class="source">

      <a href="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB/blob/master/GLCM-example.pdf" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB/blob/master/GLCM-example.pdf" target="_blank" rel="noopener nofollow ugc"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://github.com/aujinen/Microsoft-Excel-sheets-with-Macro-VB/blob/master/GLCM-example.pdf" target="_blank" rel="noopener nofollow ugc">GLCM-example.pdf</a></h3>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @PaoloZaffino (2026-06-28 18:16 UTC)

<p>If we can provide support for Radiomics.jl, just let us know</p>

---

## Post #9 by @PaoloZaffino (2026-06-28 18:22 UTC)

<p><a class="mention" href="/u/aujinen">@aujinen</a>  if you want, Radiomics.jl can also provide the raw texture matrices.<br>
See the section “Extraction raw matrices from Texture Features” in the <a href="https://www.radiomicsjl.org/example.html" rel="noopener nofollow ugc">example </a>page.</p>

---

## Post #10 by @aujinen (2026-06-29 00:09 UTC)

<p>Thank you for your kindly suggestions and detail information.</p>
<p>I have already been able to obtain GLCM values ​​in angle units using radiomics.jl as follows.</p>
<p>`features = Radiomics.extract_radiomic_features(img.raw, mask.raw, spacing; slices_2d=[(3,1)], features=[:glcm], bin_width=1, get_raw_matrices=true)`</p>
<p>I am using this Julia function call result to verify whether it is being retrieved correctly from within PyRadiomics.</p>
<p>Since that is a Julia topic, I thought it was inappropriate for this forum, so I haven’t provided details, but for my student education, the language I mainly use is Python, and I am looking for a way to call radiomics.jl from Python.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.radiomicsjl.org/cross_languages.html">
  <header class="source">
      <img src="https://raw.githubusercontent.com/pzaffino/Radiomics.jl/refs/heads/main/Logo%20Radiomicsjl.png" class="site-icon" alt="" width="542" height="499">

      <a href="https://www.radiomicsjl.org/cross_languages.html" target="_blank" rel="noopener nofollow ugc">radiomicsjl.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.radiomicsjl.org/cross_languages.html" target="_blank" rel="noopener nofollow ugc">Cross Languages- Radiomics.jl</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Currently, it is not working correctly with parameter passing during the call. The problem is with the part “slices_2d=[(3,1)]”.</p>
<p>If it is acceptable to discuss it in this thread, I would appreciate any information you can provide.</p>

---

## Post #11 by @PaoloZaffino (2026-06-29 08:18 UTC)

<p><a class="mention" href="/u/aujinen">@aujinen</a> you can open an issue <a href="https://github.com/pzaffino/Radiomics.jl/issues" rel="noopener nofollow ugc">here</a>, we can discuss (and fix the bug) on github</p>

---

## Post #12 by @aujinen (2026-06-29 09:06 UTC)

<p>As it had been a while since I last ran Julia—and because I only installed and verified pyradiomics.jl and its Python interface two days ago—I hadn’t realized there was a GitHub repository for it until now.<br>
Thank you. If I am unable to resolve the issue after conducting a few more tests regarding parameter passing with Python, I will certainly make use of its issues.</p>

---

## Post #13 by @aujinen (2026-06-29 10:32 UTC)

<p><strong>Summary of a provisional method to obtain angle-specific GLCMs using PyRadiomics</strong></p>
<p><strong>Note:</strong> As verification was performed only on 2D samples, there is no guarantee of proper operation with large datasets, including 3D data.</p>
<p><strong>Strategy:</strong> Add <code>self.</code> to the copy of internal variable you want to access to make it accessible from the outside, such as <code>self.XXX = XXX.copy()</code>.</p>
<p><strong>Issue:</strong> Memory consumption increases. Since this results in a version different from the original <code>glcm.py</code>, I believe it is necessary to fork the repository and manage it separately, as I have done.</p>
<p>To obtain individual GLCMs with angle information, it was found that you need to add code to the <code>_calculateMatrix(self, voxelCoordinates=None)</code> function in <code>glcm.py</code> to make four parameters accessible externally. Please refer to the following link for the internal parameters to be retrieved:</p>
<p><a href="https://github.com/aujinen/pyradiomics_edu/blame/master/workspace/glcm.py" rel="noopener nofollow ugc">https://github.com/aujinen/pyradiomics_edu/blame/master/workspace/glcm.py</a></p>
<p>The procedure for obtaining GLCMs in angle units from the four parameters is as follows.<br>
Please refer to the following link for details and the results of the verification experiment:</p>
<p><a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/check_P_glcm.ipynb" rel="noopener nofollow ugc">https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/check_P_glcm.ipynb</a></p>
<p>If the target is a normalized GLCM, skip step 2.</p>
<p>Step 1<br>
Set ‘weightingNorm’ to None</p>
<p>Step 2<br>
Multiply the sum of the obtained internal parameters <code>sumP_glcm</code> by <code>P_glcm</code> to return to the GLCM before normalization.</p>
<p>Step 3<br>
By reordering the array elements using <code>&lt;matrix&gt;.[:,:,:,::-1].transpose(0,3,2,1)</code>, the original symmetric GLCM with angles can be obtained.</p>
<p>The internal arrangement of the matrix elements differs from the standard GLCM pattern; the layout appears to have been modified to improve computation speed.</p>

---
