# diffusion reader

**Topic ID**: 4758
**Date**: 2018-11-14
**URL**: https://discourse.slicer.org/t/diffusion-reader/4758

---

## Post #1 by @JiDafeng (2018-11-14 14:27 UTC)

<p>Operating system:WINDOS7<br>
Slicer version:4.8.1<br>
Expected behavior:diffusion volume reader<br>
Actual behavior:only scalar volume reader<br>
I want to load DWI or DTI series on the slicer and turn the series files into nrrd files, but there’s only scalar reader which could not load the DWI or DTI correctly.</p>

---

## Post #2 by @pieper (2018-11-14 14:42 UTC)

<aside class="quote no-group" data-username="JiDafeng" data-post="1" data-topic="4758">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ce73a5/48.png" class="avatar"> JiDafeng:</div>
<blockquote>
<p>I want to load DWI or DTI series on the slicer and turn the series files into nrrd files, but there’s only scalar reader which could not load the DWI or DTI correctly.</p>
</blockquote>
</aside>
<p>Unfortunately that’s a complex topic and lots of things can happen.</p>
<p>As a start you can look at the links below to see what other people have done.  If you are still stuck usually the best thing to do is share a sample dataset of the type you are trying to convert (scan of a phantom or anonymized data).</p>
<p><a href="https://discourse.slicer.org/search?q=diffusion%20tags%3Adiffusion">https://discourse.slicer.org/search?q=diffusion%20tags%3Adiffusion</a></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://dmri.slicer.org/docs/">
  <header class="source">

      <a href="https://dmri.slicer.org/docs/" target="_blank" rel="noopener">dmri.slicer.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://dmri.slicer.org/docs/" target="_blank" rel="noopener">Documentation</a></h3>

  <p>Diffusion MRI in 3D Slicer: open-source software for diffusion magnetic resonance imaging
</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @fedorov (2018-11-14 20:45 UTC)

<p>Certain types of DWI can be loaded as multivolumes/sequences using MultVolume DICOM plugin. Make sure it is enabled (toggle “Advanced” checkbox in DICOM Browser), and look at all loadable options to see if a multivolume was recognized.</p>

---

## Post #4 by @ljod (2018-11-14 21:50 UTC)

<p>For DTI, make sure you have installed SlicerDMRI.<br>
<a href="http://dmri.slicer.org/download/" class="onebox" target="_blank" rel="nofollow noopener">http://dmri.slicer.org/download/</a></p>
<p>And try the DWIConverter tutorial here:<br>
<a href="http://dmri.slicer.org/docs/" class="onebox" target="_blank" rel="nofollow noopener">http://dmri.slicer.org/docs/</a></p>

---

## Post #5 by @JiDafeng (2018-11-15 00:52 UTC)

<p>Andrey Fedorov:</p>
<p>Thank you for your advice, I would try to find the adaptive tools such as multivolume reader to load the DTI files.</p>

---

## Post #6 by @ljod (2018-11-15 01:22 UTC)

<p>To clarify, if this is brain (or other) DTI, you should use the DWIConverter. If it is not a DTI acquisition, then try what Andrey suggests.</p>

---

## Post #7 by @fedorov (2018-11-15 03:03 UTC)

<p>I second Lauren’s comment. Multivolume plugin is useless for DTI data.</p>

---
