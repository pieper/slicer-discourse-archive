# Question about SlicerDMRI / whitematteranalysis

**Topic ID**: 27125
**Date**: 2023-01-09
**URL**: https://discourse.slicer.org/t/question-about-slicerdmri-whitematteranalysis/27125

---

## Post #1 by @Joshuazzzs (2023-01-09 10:55 UTC)

<p>Hi!<br>
The row names in the first column of the final.CSV file represent exactly which part of the brain’s fiber bundle? I don’t know what these abbreviations mean. For example, what does “T_AF_Left” mean?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c460fe6123eccd2396db4908eac7c92c8c27ee6.png" data-download-href="/uploads/short-url/k0UX6dctWVGh9GvHwbMzkTRPg5o.png?dl=1" title="83689aee50ce45ae07424ff106ec4bf" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c460fe6123eccd2396db4908eac7c92c8c27ee6_2_690x360.png" alt="83689aee50ce45ae07424ff106ec4bf" data-base62-sha1="k0UX6dctWVGh9GvHwbMzkTRPg5o" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c460fe6123eccd2396db4908eac7c92c8c27ee6_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c460fe6123eccd2396db4908eac7c92c8c27ee6_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c460fe6123eccd2396db4908eac7c92c8c27ee6_2_1380x720.png 2x" data-dominant-color="DADCDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">83689aee50ce45ae07424ff106ec4bf</span><span class="informations">1384×723 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @zhangfanmark (2023-01-09 18:26 UTC)

<p>Hi!</p>
<p>These are the abbreviations of the anatomical tracts in <a href="http://dmri.slicer.org/atlases/" rel="noopener nofollow ugc">the ORG atlas</a>. You can look up the full names here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerDMRI/ORG-Atlases/blob/master/Tracts-in-ORG-800FC-100HCP.md">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/ORG-Atlases/blob/master/Tracts-in-ORG-800FC-100HCP.md" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/ORG-Atlases/blob/master/Tracts-in-ORG-800FC-100HCP.md" target="_blank" rel="noopener nofollow ugc">SlicerDMRI/ORG-Atlases/blob/master/Tracts-in-ORG-800FC-100HCP.md</a></h4>


      <pre><code class="lang-md">## Anatomical tracts available in the ORG-800FC-100HCP atlas. 

Overall, there are 58 deep white matter fiber tracts from the association, cerebellar, commissural and projection tracts, and 16 superficial tract categories according to the brain lobes. Except for the 7 corpus callosum (CC) tracts and the middle cerebellar peduncle (MCP) tract that cross the hemispheres (C), others are hemispheric (LR).

* Association tracts
    * arcuate fasciculus (AF) – LR
    * cingulum bundle (CB) – LR
    * extreme capsule (EmC) – LR
    * inferior longitudinal fasciculus (ILF) – LR
    * inferior occipito-frontal fasciculus (IoFF) – LR
    * middle longitudinal fasciculus (MdLF) – LR
    * superior longitudinal fasciculus I (SLF I) – LR
    * superior longitudinal fasciculus II (SLF II) – LR
    * superior longitudinal fasciculus II (SLF III) – LR
    * uncinate fasciculus (UF) – LR

* Cerebellar tracts
    * cortico-ponto-cerebellar (CPC) – LR
    * inferior cerebellar peduncle (ICP) – LR
    * intracerebellar input and Purkinje tract (Intra-CBLM-I&amp;P) – LR 
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerDMRI/ORG-Atlases/blob/master/Tracts-in-ORG-800FC-100HCP.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Regards,<br>
Fan</p>

---
