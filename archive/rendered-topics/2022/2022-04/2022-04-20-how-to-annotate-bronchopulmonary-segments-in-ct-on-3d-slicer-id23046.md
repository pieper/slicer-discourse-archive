# How to annotate Bronchopulmonary segments in CT on 3D Slicer ?

**Topic ID**: 23046
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/how-to-annotate-bronchopulmonary-segments-in-ct-on-3d-slicer/23046

---

## Post #1 by @Joris_Fournel (2022-04-20 11:28 UTC)

<p>Hello to all the community here,</p>
<p>Me and my research team are currently hitting a wall in trying to identify a process in 3D slicer to annotate Bronchopulmonary segments in CT with 3D Slicer.<br>
Which brings me on this forum to ask for help!</p>
<p>Thanks in advance,<br>
Joris</p>

---

## Post #2 by @rbumm (2022-04-20 13:19 UTC)

<p>Hello Joris,</p>
<p>You may want to try the Lung CT Segmenter module of the  <strong>Lung CT Analyzer extension</strong> which includes an <a href="https://discourse.slicer.org/t/lung-ct-segmenter-with-local-threshold-airway-segmentation/22065">option for airway segmentation</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0804d71351003c86b65a8c2b3730b33113729b03.png" data-download-href="/uploads/short-url/18WbLfNwQYKikzFSWIQbNMV3muL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0804d71351003c86b65a8c2b3730b33113729b03_2_485x500.png" alt="image" data-base62-sha1="18WbLfNwQYKikzFSWIQbNMV3muL" width="485" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0804d71351003c86b65a8c2b3730b33113729b03_2_485x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0804d71351003c86b65a8c2b3730b33113729b03.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0804d71351003c86b65a8c2b3730b33113729b03.png 2x" data-dominant-color="F5F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">518×533 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I manually annotated one of the segmentations like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aac3a2c0f5590f1a87fbdbc04e61f4524424a130.jpeg" data-download-href="/uploads/short-url/omEjH3pV022X8bVeFWMntdkSjhm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aac3a2c0f5590f1a87fbdbc04e61f4524424a130_2_520x500.jpeg" alt="image" data-base62-sha1="omEjH3pV022X8bVeFWMntdkSjhm" width="520" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aac3a2c0f5590f1a87fbdbc04e61f4524424a130_2_520x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aac3a2c0f5590f1a87fbdbc04e61f4524424a130.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aac3a2c0f5590f1a87fbdbc04e61f4524424a130.jpeg 2x" data-dominant-color="9B98C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">724×695 65.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is no computerized bronchopulmonary segment <em>annotation</em> available in Slicer yet - it would probably be interesting to train AI on a set of segmentations to do this automatically or use the VMTK for centerline calculations.</p>

---

## Post #3 by @Kedar_Hibare (2022-04-20 16:33 UTC)

<p>Hi,<br>
I am an Interventional Pulmonologist and for us all navigating to a PPL (Peripheral Pulmonary Nodule) is the most important aspect to reach and do some diagnostic work… I wish to know if Slicer has a fly-through option endoscopically and if any code can be written for the same? I am a doctor and can’t write code I would appreciate if someone from the Slicer team can help as this it is the most important function with which we can be supported. This would be useful for all Interventional Pulmonologists</p>
<p>Another application is when patients have airway abnormalities and we could be helped with 3D models for stents (moulds) making,…</p>
<p>Can someone please connect and help</p>
<p>Warm Regards<br>
Dr Kedar Hibare<br>
Interventional Pulmonologist<br>
Narayana Health City Bangalore India<br>
<a href="mailto:kedarhibare@gmail.com">kedarhibare@gmail.com</a></p>

---

## Post #4 by @pieper (2022-04-20 17:28 UTC)

<p>The built-in endoscopy module provides some of that functionality.  You can add more tools with the VMTK extension and the Chest Imaging Platform.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/endoscopy.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/endoscopy.html</a></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/33c8a9992ee622e11cd2ee152e86fac335e447a4bfe10f7a7154835f12a358dd/vmtk/SlicerExtension-VMTK" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener">GitHub - vmtk/SlicerExtension-VMTK</a></h3>

  <p>Contribute to vmtk/SlicerExtension-VMTK development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://chestimagingplatform.org/workstation-slicer-cip">
  <header class="source">
      <img src="https://chestimagingplatform.org/profiles/openscholar/themes/hwpi_basetheme/favicon.png" class="site-icon" width="32" height="32">

      <a href="https://chestimagingplatform.org/workstation-slicer-cip" target="_blank" rel="noopener">chestimagingplatform.org</a>
  </header>

  <article class="onebox-body">
    <img src="https://chestimagingplatform.org/" class="thumbnail onebox-avatar" width="32" height="32">

<h3><a href="https://chestimagingplatform.org/workstation-slicer-cip" target="_blank" rel="noopener">Workstation (SlicerCIP)</a></h3>

  <p>Extension to the Slicer that integrates:</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Joris_Fournel (2022-04-20 20:33 UTC)

<p>Hi Rudolf,<br>
Thanks for the suggestion, I’ll take a look at this module!<br>
But I have a strong intuition that bronchopulmonary segments can be annotated using a wise combination of the existing segmentation tools in Slicer. A more experienced user could come up with it. To me the difficulty lies in drawing huge cuts, in dividing the wider lung region into the smaller segments, I ignore what tool can perform this operation from a set of points placed on the segments border for example.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd75a79a4db0e9758fdf81fdfb5de8cc462a1ef0.png" data-download-href="/uploads/short-url/AacSbR4oneUg9RJ37mSTNg4Onh6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd75a79a4db0e9758fdf81fdfb5de8cc462a1ef0.png" alt="image" data-base62-sha1="AacSbR4oneUg9RJ37mSTNg4Onh6" width="690" height="492" data-dominant-color="F5E4E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">770×550 22.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
