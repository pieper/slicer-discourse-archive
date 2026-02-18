# 3D visualization of varying BMD

**Topic ID**: 43314
**Date**: 2025-06-11
**URL**: https://discourse.slicer.org/t/3d-visualization-of-varying-bmd/43314

---

## Post #1 by @S_Motch_Perrine (2025-06-11 15:01 UTC)

<p>I am wondering if you have any suggestions for me on how to tackle this task in 3D Slicer. I have four genotypes of mice for a rather complex phenotype, and want to visualize the differences in BMD across all the bones of the skull. Specimens were scanned alongside a hydroxy apatite phantom. I would also like to show differences in bone thickness in a separate figure - as this may or may not correspond with the BMD of a bone but may instead reflect disorganization of bone growth. Thank you!</p>

---

## Post #2 by @muratmaga (2025-06-11 15:46 UTC)

<p>Visualization is the easy part; i.e., as long as you can convert the intensities in voxels to BMD using your phantom. Once you get that, you can make a 3D segmentation of your skull, and use the “Probe Volume with a Model” that’s one option (volume in this case being the BMD values for that skull).</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/modules/probevolumewithmodel.html">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/probevolumewithmodel.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/probevolumewithmodel.html" target="_blank" rel="noopener nofollow ugc">Probe Volume With Model — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
