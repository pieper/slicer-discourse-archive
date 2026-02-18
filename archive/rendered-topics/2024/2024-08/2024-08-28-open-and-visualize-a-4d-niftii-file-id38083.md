# Open and visualize a 4D niftii file?

**Topic ID**: 38083
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/open-and-visualize-a-4d-niftii-file/38083

---

## Post #1 by @theanega (2024-08-28 12:28 UTC)

<p>Hi all!</p>
<p>I’m having trouble opening a 4D NIfTI file in 3D Slicer. The file contains 6 concatenated 3D voxelwise maps of a segmented tumor, created using nibabel in Python.<br>
The file I’m trying to open has dimensions (x, y, z, 6) because it contains 6 voxelwise maps (ADC, AKC, T2, etc.) so there are 6 volumes.</p>
<p>While I can view it properly in FSLeyes, Slicer doesn’t recognize it as a 4D volume.<br>
I’ve tried loading it normally and using the MultiVolume Explorer module, but Slicer is not recognizing it. Is there a specific way to load 4D NIfTIs in Slicer that I’m missing?</p>
<p>Any guidance would be greatly appreciated. Thanks!</p>

---

## Post #2 by @cpinter (2024-08-28 12:51 UTC)

<p>I’m working on an improvement to Slicer that will be able to handle higher dimension volumes and load them as a sequence.</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/cpinter/Slicer/tree/volume-sequence-io-5D">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/cpinter/Slicer/tree/volume-sequence-io-5D" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/cpinter/Slicer/tree/volume-sequence-io-5D" target="_blank" rel="noopener">GitHub - cpinter/Slicer at volume-sequence-io-5D</a></h3>

  <p><a href="https://github.com/cpinter/Slicer/tree/volume-sequence-io-5D" target="_blank" rel="noopener">volume-sequence-io-5D</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
The only difference from your use case is that this work expects to support 5D images, where the voxel values are not simple scalars but vectors (e.g. displacement vector or RGBA)</p>
<p>I assume loading into a sequence will be acceptable to you. If so, can you please share this file so that I can see if this reader I’m working on can handle it and if not, what would be needed?</p>

---
