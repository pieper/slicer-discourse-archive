# fluorescent data extraction

**Topic ID**: 2705
**Date**: 2018-04-26
**URL**: https://discourse.slicer.org/t/fluorescent-data-extraction/2705

---

## Post #1 by @FungalSlicer (2018-04-26 15:52 UTC)

<p>Hey guys,</p>
<p>I am looking for a way to extract data from stacked fluorescent image data of specific tip-growing fungi. I already remodeled the surface and reduced it to a centerline (which i managed to load into 3Dslicer as a Surface file). Now I would like to stepwise reduce dimensionality by walking along the centerline, averaging the intensities over circle planes perpendicular to it upto the apex.</p>
<p>Do you have any tool or workflow in mind to do this?</p>
<p>Thx in advance,   Philipp</p>

---

## Post #2 by @pieper (2018-04-26 20:36 UTC)

<p>If I understand what you are asking for, this will require some programming (python scripting).  Maybe you could add some images to better illustrate what you are trying to calculate.</p>

---

## Post #3 by @ihnorton (2018-04-26 20:38 UTC)

<p>You might want to look at CellProfiler:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="http://cellprofiler.org/images/favicon.ico" class="site-icon" width="32" height="32">
      <a href="http://cellprofiler.org/" target="_blank">cellprofiler.org</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="http://cellprofiler.org/" target="_blank">CellProfiler</a></h3>

<p>CellProfiler is a free open-source software for measuring and analyzing cell images</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2018-04-26 22:18 UTC)

<p>Probably the method you are looking for is curved multiplanar reformatting (MPR). Result is a set of images orthogonal to a curve, which you can further process as a volume to perform measurements, get statistics, etc.</p>
<p>Curved MPR images can be obtained as shown in this video:</p>
<div class="lazyYT" data-youtube-id="thExIlffL0I" data-youtube-title="Curved multi-planar reconstruction (MPR) view in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>You would need to save images taken along the curve and paste it into a volume, which you may be able to do using ScreenCapture module. If I remember correctly, <a class="mention" href="/u/stevenagl12">@stevenagl12</a> is developing a module to automate this.</p>

---

## Post #5 by @FungalSlicer (2018-04-27 09:31 UTC)

<p>The curved multi-planar reconstruction Looks quite close to what I am trying to do. But as far as I see their example, the curve they set up is basically in one z-layer, which allows for y-plane to be transversing, perpendicular to the line. In my case the organisms centerline reaches across several z-layers. The view would have to be adjusted to be perpensicular to the (possibly better smooth) centerline.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> I failed to upload a tif stack here, but it’s growth looks close to the image attached</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14aa7083f30e765098d7af70477c4bc395cf08ec.jpeg" data-download-href="/uploads/short-url/2WOIi5iNEXM1dFrFRcv9Io8mdTm.jpg?dl=1" title="large" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14aa7083f30e765098d7af70477c4bc395cf08ec_2_690x420.jpg" alt="large" data-base62-sha1="2WOIi5iNEXM1dFrFRcv9Io8mdTm" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14aa7083f30e765098d7af70477c4bc395cf08ec_2_690x420.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14aa7083f30e765098d7af70477c4bc395cf08ec_2_1035x630.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14aa7083f30e765098d7af70477c4bc395cf08ec.jpeg 2x" data-dominant-color="2A2F2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">large</span><span class="informations">1280×780 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>I tried LineProfiler ( by <a class="mention" href="/u/lassoan">@lassoan</a>) also, but I assume it only handles straight lines ?!</li>
</ul>
<p>I might ask <a class="mention" href="/u/stevenagl12">@stevenagl12</a>  about his progress. According to his post he s looking for a similar thing</p>

---
