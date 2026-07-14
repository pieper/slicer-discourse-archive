---
topic_id: 44967
title: "Asking question about GLCM per angle in radiomics"
date: 2025-11-05
url: https://discourse.slicer.org/t/44967
last_bumped: 2026-07-14T01:06:23.335Z
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

## Post #14 by @aujinen (2026-07-01 13:41 UTC)

<p>I just posted about the issues related “Using Radiomics.jl from other languages” on the radiomics.jl site.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/pzaffino/Radiomics.jl/issues/25">
  <header class="source">

      <a href="https://github.com/pzaffino/Radiomics.jl/issues/25" target="_blank" rel="noopener nofollow ugc">github.com/pzaffino/Radiomics.jl</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/pzaffino/Radiomics.jl/issues/25" target="_blank" rel="noopener nofollow ugc">Issue with passing parameters from Python to Julia via juliacall</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-07-01" data-time="13:33:04" data-timezone="UTC">01:33PM - 01 Jul 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/aujinen" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/55919851?v=4" class="onebox-avatar-inline" width="20" height="20">
          aujinen
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When attempting to call the following code—which runs without issues in Julia—fr<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">om Python via JuliaCall, passing the parameter `slices_2d=[(3,1)]` causes it to fail. 
I haven't explored all possible patterns, but they all result in failure. I haven't found a satisfactory answer even after checking GitHub Copliot.

### Julia (without issues)
```
using NIfTI
using Radiomics
using Printf

# Load 2D test image and segmentation mask
img = niread("forRadiomicsTest.nii.gz")
mask = niread("forSegmentation.seg.nii.gz")

# Extract voxel spacing from image header
spacing = [img.header.pixdim[2], img.header.pixdim[3], img.header.pixdim[4]]

# Extract radiomics features
# features = Radiomics.extract_radiomic_features(img.raw, mask.raw, spacing; slices_2d=[(3,1)], features=[:glcm], bin_width=1)

features = Radiomics.extract_radiomic_features(img.raw, mask.raw, spacing; slices_2d=[(3,1)], features=[:glcm], bin_width=1, get_raw_matrices=true)

mat = features["raw_glcm_matrices"]
# --&gt; get GLCM matrix per angle with normarization
```

### Python (with issues)
```
from juliacall import Main as jl
jl.seval('import Pkg; Pkg.add("Radiomics")')

import SimpleITK as sitk
import numpy as np

# Load 2D images
img_sitk = sitk.ReadImage('./forRadiomicsTest.nii.gz')
mask_sitk = sitk.ReadImage('./forSegmentation.seg.nii.gz')

# Convert to numpy arrays
img = sitk.GetArrayFromImage(img_sitk)
mask = sitk.GetArrayFromImage(mask_sitk)

# Extract spacing information
spacing = img_sitk.GetSpacing()

radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d=[(3,1)])
### --&gt; JuliaError
# JuliaError                                Traceback (most recent call last)
# Cell In[7], line 1
# ----&gt; 1 radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d=[(3,1)])
#
# File ~\.julia\packages\PythonCall\5WGSP\src\JlWrap\any.jl:263, in __call__(self, *args, **kwargs)
#     261     return ValueBase.__dir__(self) + self._jl_callmethod($(pyjl_methodnum(pyjlany_dir)))
#     262 def __call__(self, *args, **kwargs):
# --&gt; 263     return self._jl_callmethod($(pyjl_methodnum(pyjlany_call)), args, kwargs)
#     264 def __bool__(self):
#     265     return True
###

### === The alternative code commented out below also halted with the same error.
# radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d=[3,1])
# radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d=(3,1))
# radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d=((3,1)))
###

julia_slices = jl.seval("[(3,1)]")
radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d=julia_slices)

### --&gt; JuliaError
# JuliaError                                Traceback (most recent call last)
# Cell In[31], [line 2](vscode-notebook-cell:?execution_count=31&amp;line=2)
#      1 # Extract radiomic features
# ----&gt; [2](vscode-notebook-cell:?execution_count=31&amp;line=2) radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d = julia_slices)
#
# File ~\.julia\packages\PythonCall\5WGSP\src\JlWrap\any.jl:263, in __call__(self, *args, **kwargs)
#     261     return ValueBase.__dir__(self) + self._jl_callmethod($(pyjl_methodnum(pyjlany_dir)))
#     262 def __call__(self, *args, **kwargs):
# --&gt; [263](https://file+.vscode-resource.vscode-cdn.net/d%3A/pyradiomics/workspace/~/.julia/packages/PythonCall/5WGSP/src/JlWrap/any.jl:263)     return self._jl_callmethod($(pyjl_methodnum(pyjlany_call)), args, kwargs)
#     264 def __bool__(self):
#     265     return True
###

kwargs = jl.seval("slices_2d = [(3, 1)]")
radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, **kwargs)
### --&gt; TypeError 
# TypeError                                 Traceback (most recent call last)
# Cell In[25], line 1
# ----&gt; 1 radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, **kwargs)
#       2 
#       3 # radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, slices_2d=[3,1])
#
# TypeError: extract_radiomic_features argument after ** must be a mapping, not VectorValue
###

### === The alternative code commented out below also halted with the same error.
# kwargs = jl.seval("slices_2d = [3, 1]")
# kwargs = jl.seval("slices_2d = (3, 1)")
# kwargs = jl.seval("slices_2d = ((3, 1))")
### 

####=== The alternative code commented out below also halted with the other error.
radiomic_features = jl.Radiomics.extract_radiomic_features(img, mask, spacing, kwargs)```
###</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @aujinen (2026-07-04 18:26 UTC)

<p>Thanks to the assistance of Mr. Aldo Giuliani, the issue regarding parameter conversion when using Julia’s <code>radiomics.jl</code> from Python has been resolved.</p>
<p>I incorporated this information into materials I created for students in Japan.</p>
<p><a href="https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/radiomics_julia_2D.ipynb" rel="noopener nofollow ugc">https://github.com/aujinen/pyradiomics_edu/blob/master/workspace/radiomics_julia_2D.ipynb</a></p>

---

## Post #16 by @aujinen (2026-07-05 11:10 UTC)

<p>I finally understand the specific difference between the <code>weightingNorm</code> parameter  [None] and [‘no_weighting’].</p>
<p>I have revised this post. I previously posted under the mistaken impression that the rotational dependence of GLCM is controlled by the <code>weightingNorm</code> parameter.</p>
<p>I now understand that the difference between <code>[None]</code> and <code>['no_weighting']</code> for this parameter lies in the extent to which image anisotropy is preserved. <code>[None]</code> preserves anisotropy more strongly, whereas <code>['no_weighting']</code> preserves it to a lesser degree—meaning the data is more prone to relative averaging.</p>

---

## Post #17 by @aujinen (2026-07-14 01:06 UTC)

<p>I had suspected that sensitivity to anisotropy might differ between [None] and [‘no_weighting’], but it appears one cannot categorically state which offers higher sensitivity. While the relationship does not hold perfectly due to the asymmetry in where the normalization process is applied, the two generally follow the relationship defined by Jensen’s inequality for convex functions.</p>
<p>In any case, regarding anisotropy, it might be better to directly use the “GLCM” for each angle obtained during the [None] calculation process.</p>

---
