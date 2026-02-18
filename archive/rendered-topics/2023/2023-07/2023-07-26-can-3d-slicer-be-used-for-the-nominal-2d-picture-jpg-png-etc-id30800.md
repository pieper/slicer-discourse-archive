# Can 3D Slicer be used for the nominal 2D picture (jpg/png etc..) label or annotation?

**Topic ID**: 30800
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/can-3d-slicer-be-used-for-the-nominal-2d-picture-jpg-png-etc-label-or-annotation/30800

---

## Post #1 by @Liang_Ma (2023-07-26 13:10 UTC)

<p>Such data (non dicom) have no meta information, so “Add DICOM Data” menu does not recognize them.</p>

---

## Post #2 by @fedorov (2023-07-26 13:10 UTC)

<p>Instead of “Add DICOM Data” you should use menu “File &gt; Add Data” to load non-DICOM images.</p>

---

## Post #3 by @Liang_Ma (2023-07-28 09:54 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Thanks–I just tried to load a png file, but got such error:</p>
<p>Error: Loading /xxx/Pictures/4.png -  load failed.</p>

---

## Post #4 by @waltbobrowski (2023-07-28 14:09 UTC)

<p>You may wish to consider using Imagej software in conjunction with the plugin, Annotator J.<br>
<a href="https://www.molbiolcell.org/doi/10.1091/mbc.E20-02-0156" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.molbiolcell.org/doi/10.1091/mbc.E20-02-0156</a></p>

---

## Post #5 by @waltbobrowski (2023-07-28 14:30 UTC)

<p>Annotating images:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://imagej.net/imagej-wiki-static/Annotating_Images">
  <header class="source">
      <img src="https://imagej.net/imagej-wiki-static/skins/ij2.ico" class="site-icon" width="256" height="256">

      <a href="https://imagej.net/imagej-wiki-static/Annotating_Images" target="_blank" rel="noopener nofollow ugc">ImageJ</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://imagej.net/imagej-wiki-static/Annotating_Images" target="_blank" rel="noopener nofollow ugc">Annotating Images</a></h3>

  <p>All images for publications should include a scale bar. A standard size should be used for the scale bars on all images if possible to help avoid confusion.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Fiji Imagej download:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://imagej.net/software/fiji/downloads">
  <header class="source">
      <img src="https://imagej.net/favicon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://imagej.net/software/fiji/downloads" target="_blank" rel="noopener nofollow ugc">ImageJ Wiki</a>
  </header>

  <article class="onebox-body">
    <img src="https://imagej.github.io/media/icons/imagej2.png" class="thumbnail" width="" height="">

<h3><a href="https://imagej.net/software/fiji/downloads" target="_blank" rel="noopener nofollow ugc">Fiji Downloads</a></h3>

  <p>The ImageJ wiki is a community-edited knowledge base on topics relating to ImageJ, a public domain program for processing and analyzing scientific images, and its ecosystem of derivatives and variants, including ImageJ2, Fiji, and others.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2023-07-28 20:07 UTC)

<aside class="quote no-group" data-username="Liang_Ma" data-post="3" data-topic="30800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/liang_ma/48/66068_2.png" class="avatar"> Liang_Ma:</div>
<blockquote>
<p>Error: Loading /xxx/Pictures/4.png - load failed.</p>
</blockquote>
</aside>
<p>I’ve never come across a png image that Slicer could not load. Could you upload your image somewhere and post the link here?</p>
<aside class="quote no-group" data-username="waltbobrowski" data-post="4" data-topic="30800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/f05b48/48.png" class="avatar"> waltbobrowski:</div>
<blockquote>
<p>You may wish to consider using Imagej software in conjunction with the plugin, Annotator J.</p>
</blockquote>
</aside>
<p>If you need to annotate 2D microscopy images then indeed ImageJ (FIJI) could be a good choice (although it uses a restrictive (GPL) license and it is based on Java), or perhaps Napari is even better (it uses non-restrictive license and based on Python). Of course you can also use Slicer for 2D images, but Slicer’s unique strength is in working with 3D data (images, meshes, transforms, 3D annotations, etc.).</p>

---
