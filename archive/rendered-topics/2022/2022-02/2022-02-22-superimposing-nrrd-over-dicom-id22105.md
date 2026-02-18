# Superimposing nrrd over DICOM

**Topic ID**: 22105
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/superimposing-nrrd-over-dicom/22105

---

## Post #1 by @AMK (2022-02-22 08:19 UTC)

<p>Hi,</p>
<p>I am developing an extension in Slicer for automatic segmentation and surgical planning. I have been able to perform the automatic segmentation outside the Slicer and then import the file to further modify it. But the designers in my company use an in-built software at the moment (which we are planning to replace with Slicer). So in order for them to start using our initial segmentation results, we are trying to import some capabilities of Slicer into our own software (uses dcmtk). I wanted to know where can I find the source code, specifically for the capability of Slicer to superimpose the segmentation label maps over the DICOM file.</p>
<p>Thanks,<br>
Aamir</p>

---

## Post #2 by @pieper (2022-02-22 18:43 UTC)

<p>It’s complicated and the functionality is spread around in different places, but once the data is loaded the rendering is handled by <code>vtkSliceView*DisplayableManager</code> classes.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/DisplayableManager">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/DisplayableManager" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/DisplayableManager" target="_blank" rel="noopener">Slicer/Libs/MRML/DisplayableManager at master · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/DisplayableManager" target="_blank" rel="noopener">master/Libs/MRML/DisplayableManager</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Some of the core functionality is in the <code>vtkMRMLSlice*Logic</code> classes.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/Logic">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/Logic" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/Logic" target="_blank" rel="noopener">Slicer/Libs/MRML/Logic at master · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/master/Libs/MRML/Logic" target="_blank" rel="noopener">master/Libs/MRML/Logic</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
