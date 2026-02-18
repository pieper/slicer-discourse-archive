# 3D slicer for confocal microscopy Z stack tiffs

**Topic ID**: 42449
**Date**: 2025-04-06
**URL**: https://discourse.slicer.org/t/3d-slicer-for-confocal-microscopy-z-stack-tiffs/42449

---

## Post #1 by @Aro_Nugawela (2025-04-06 02:09 UTC)

<p>Sorry if I’ve posted in the wrong community/thread this is my first time on this forum.</p>
<p>I have a series of confocal scanning sections across a 3D tissue models. Encoded into the metadata is the scaling of the images (x=1612 um, y =1612 I’m, z = 817 um with 5um separation between the 163 planes), In tiff format. I have tried importing using slicemorph (following a YouTube tutorial), but this seems to be scaled to the pixel sizes on the XY and number of planes for the Z (IE. 6240×6240x163), which is causing a lot of issues in terms of creating a 3D model for it. The spacing also defaults to 1mm × 1mm× 1mm and 0.0002 × 0.0002 × 0.0002.</p>
<p>The end goal here is to produce a 3D rendering which can be translated into a CAD file. I’ve checked these files on other softwares (including imageJ as standard) and it seems to load the correct metadata, including the sectioning.</p>
<p>Has anyone had any issues like this before. It’s my first time using 3D slicer so any help is appreciated. Thanks!</p>

---

## Post #2 by @muratmaga (2025-04-06 02:38 UTC)

<aside class="quote no-group" data-username="Aro_Nugawela" data-post="1" data-topic="42449">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/aro_nugawela/48/79907_2.png" class="avatar"> Aro_Nugawela:</div>
<blockquote>
<p>metadata is the scaling of the images (x=1612 um, y =1612 I’m, z = 817 um with 5um separation between the 163 planes), In tiff format. I have tried importing using slicemorph (following a</p>
</blockquote>
</aside>
<p>This seems to be the physical bounds of the image volume. <code>ImageStacks</code> expects you to enter the correct scaling manually. That 1.0x1.0x1.0 is just simply a place holder (it is a common resolution for medical imaging).</p>
<p>So 5 micron (or rather 0.005 as units in Slicer are all mms) seems reasonable given the ROI bounds and the number of slices you reported. But you still need to find out what the resolution in X and Y fields are. In confocal they tend to be much higher resolution than slice spacing. If your metadata does not show you that, then you might be able to get a close enough approximation by dividing the X and Y lengths reported to the X Y image dimension (in pixels). For example if your images are 1024x1024, dividing 1612/1024 will give you the resolution of 1.57 micron/px. Then you can enter this to the XY fields of spacing as 0.00157.</p>
<aside class="quote no-group" data-username="Aro_Nugawela" data-post="1" data-topic="42449">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/aro_nugawela/48/79907_2.png" class="avatar"> Aro_Nugawela:</div>
<blockquote>
<p>(following a YouTube tutorial), but this seems to be scaled to the pixel sizes on the XY and number of planes</p>
</blockquote>
</aside>
<p>I am not sure what tutorial that would be. Official SlicerMorph tutorials are here:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/Tutorials">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/9e38f1261de95a8d831d2264a4683f8b/SlicerMorph/Tutorials" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/Tutorials" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a></h3>

    <p><span class="github-repo-description">SlicerMorph module tutorials</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Specifically <a href="https://github.com/SlicerMorph/Tutorials/blob/main/ImageStacks/README.md" rel="noopener nofollow ugc">this is the link to the ImageStacks tutorial with some toy microCT data</a></p>

---
