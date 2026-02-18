# Slicer crashes when trying to open xtekct .vol files

**Topic ID**: 19077
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-trying-to-open-xtekct-vol-files/19077

---

## Post #1 by @Ntizopoulos_K (2021-08-05 12:14 UTC)

<p>Hi, there!! I am trying to load some .vol files, but the software keeps crashing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef91bcbec6df6de4982819ef856fa62ca07c87e9.jpeg" data-download-href="/uploads/short-url/ybkm4YmOSOEOhmgDygB4AJU2J1D.jpeg?dl=1" title="2021-08-05_125026" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef91bcbec6df6de4982819ef856fa62ca07c87e9_2_690x403.jpeg" alt="2021-08-05_125026" data-base62-sha1="ybkm4YmOSOEOhmgDygB4AJU2J1D" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef91bcbec6df6de4982819ef856fa62ca07c87e9_2_690x403.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef91bcbec6df6de4982819ef856fa62ca07c87e9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef91bcbec6df6de4982819ef856fa62ca07c87e9.jpeg 2x" data-dominant-color="F4F4F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-08-05_125026</span><span class="informations">758×443 40.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-08-05 14:38 UTC)

<p>The <code>.vol</code> file extension is used for many different file formats.</p>
<p>SlicerHeart extension can load 3D ultrasound volumes from GE Kretz .vol files, but based on the other files in the folder, it seems that your .vol file are not this kind.</p>
<p>You can look for a Python package that can convert these proprietary xtekct CT volumes into some standard file formats. <a class="mention" href="/u/muratmaga">@muratmaga</a> can you recommend anything specific?</p>
<p>Or, you can use <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess extension</a> to load the CT. Voxel data should be in the largest file (probably the .vol file), use that as input. You should be able to find the necessary parameters (image size, voxel type, etc.) in the other files.</p>
<p>If you need to load such images regularly then you can write a Python script for it. If you share that Python script then we can help turning it into a file reader plugin, so that you can use the “Add data…” window to load it as any other already supported file formats.</p>
<p>The application should not crash, even if it encounters completely invalid (unexpexted, unsupported) files. If you can share the files with us (upload somewhere and post the link here) then we can make sure that the error is properly reported instead of crashing.</p>

---

## Post #3 by @muratmaga (2021-08-05 20:38 UTC)

<p>Looking</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19077">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can look for a Python package that can convert these proprietary xtekct CT volumes into some standard file formats. <a class="mention" href="/u/muratmaga">@muratmaga</a> can you recommend anything specific?</p>
</blockquote>
</aside>
<p>I think these are from GE microCTs. The vgi should contains the information everything to be able to use RawImageGuess module to import the .VOL file, which is basically raw image data.</p>
<p>In fact we have written a small module for a collaborator so that they can more easily import their GE output into Slicer. However, that module uses a settings file called *.PCR. So, if these are indeed from GE, and you have the 74 full TF1.pcr saved in the same folder, you should be able to use this module.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/chz31/GEVolImport">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/chz31/GEVolImport" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/8348b5acfd2a6bd7d068967f083347209108f0a1da2f20ddd1779f13d28e0fa9/chz31/GEVolImport" class="thumbnail" width="" height=""></div>

<h3><a href="https://github.com/chz31/GEVolImport" target="_blank" rel="noopener">GitHub - chz31/GEVolImport</a></h3>

  <p>Contribute to chz31/GEVolImport development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
