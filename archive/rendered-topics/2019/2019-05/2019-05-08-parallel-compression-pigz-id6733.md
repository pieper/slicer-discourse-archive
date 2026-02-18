# Parallel compression pigz

**Topic ID**: 6733
**Date**: 2019-05-08
**URL**: https://discourse.slicer.org/t/parallel-compression-pigz/6733

---

## Post #1 by @muratmaga (2019-05-08 18:41 UTC)

<p>There was a discussion sometime ago about perhaps enabling pigz (parallel gzip) with Slicer. <a href="https://discourse.slicer.org/t/how-to-unset-default-compress-option-during-save/4488/7" class="inline-onebox">How to unset default 'compress' option during save - #7 by pieper</a></p>
<p>At the time, question was lack of a windows port. I see there is one:<br>
<a class="mention" href="/u/pieper">@pieper</a> would this help?<br>
<a href="https://blog.kowalczyk.info/software/pigz-for-windows.html" class="onebox" target="_blank" rel="noopener">https://blog.kowalczyk.info/software/pigz-for-windows.html</a></p><aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/kjk/pigz" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/95f5daf3ccdfe4f5e1664d1b806e6527dcb7fe6492bcc2c9eba0fe08e87f5182/kjk/pigz" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/kjk/pigz" target="_blank" rel="noopener">kjk/pigz</a></h3>


  <p><span class="label1">A Windows port of pigz - a parallel implementation of gzip for modern multi-processor, multi-core machines.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2019-05-09 02:51 UTC)

<p>It is a complicated topic. Such changes should happen at lower level, in ITK and there are plans for it, see <a href="https://discourse.itk.org/t/adding-parallel-compression-to-metaio/1835/15" rel="nofollow noopener">https://discourse.itk.org/t/adding-parallel-compression-to-metaio/1835/15</a>.</p>
<p>Unfortunately, for me it seems that the discussion does not seem to converge to a reasonable solution (see my comments there).</p>

---

## Post #3 by @muratmaga (2019-05-09 05:08 UTC)

<p>That’s unfortunate. Breaking the nrrd compatibility between  itk and non-itk based programs would be a pretty bad idea.</p>

---
