---
topic_id: 25282
title: "Vol File Not Loading"
date: 2022-09-15
url: https://discourse.slicer.org/t/25282
---

# .vol file not loading

**Topic ID**: 25282
**Date**: 2022-09-15
**URL**: https://discourse.slicer.org/t/vol-file-not-loading/25282

---

## Post #1 by @rbaheti (2022-09-15 19:20 UTC)

<p>Hi,<br>
I’m trying to upload an ultrasound with a .vol extension. I don’t have more information like which machine was used to create the ultrasound or the software version used by the machine. When I load the scan it shows me the option to load it as a volume and then an error comes up.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbbdccfa08560369ebd323af07b430e28c8c863f.png" alt="image" data-base62-sha1="vlVd9qUyUSdn8atpsUJXvj8XnhZ" width="427" height="209"></p>
<p>The file doesn’t load as a GE/Kretz volume image. I’m not sure how to convert it into another format (like .mha or .nrrd). I’m also checking out other packages and softwares like TomoVision but no fruitful result so far.</p>

---

## Post #2 by @pieper (2022-09-15 20:26 UTC)

<p><code>.vol</code> could mean anything since people may use it for arbitrary data formats.</p>
<p>If it happens to be an uncompressed volume then this might work:</p>
<aside class="quote quote-modified" data-post="1" data-topic="9219">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219">New extension: RawImageGuess - for loading of images from unrecognized file format</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    There are proprietary image file formats the 3D Slicer does not recognize and so refuses to load. <a class="mention" href="/u/nagy.attila">@nagy.attila</a> in collaboration with Slicer core developers created an extension that can be used to load data from files that use an unknown format. 
<a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess extension</a> offers a number of parameters (image header size, dimensions, pixel type, etc.) that users can adjust and see the resulting image in real-time. This makes it possible to guess the image format in a couple of minutes. 
See a demo …
  </blockquote>
</aside>


---

## Post #3 by @rbaheti (2022-09-15 22:55 UTC)

<p>I tried using RawImageGuess but it did gave a very weird output.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e68a26c1904d7dec322cf52659ccacd64ba454da.jpeg" data-download-href="/uploads/short-url/wTrNZ0ujVNS5igZRM553BSrnU8i.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68a26c1904d7dec322cf52659ccacd64ba454da_2_690x187.jpeg" alt="image" data-base62-sha1="wTrNZ0ujVNS5igZRM553BSrnU8i" width="690" height="187" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68a26c1904d7dec322cf52659ccacd64ba454da_2_690x187.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68a26c1904d7dec322cf52659ccacd64ba454da_2_1035x280.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e68a26c1904d7dec322cf52659ccacd64ba454da_2_1380x374.jpeg 2x" data-dominant-color="181715"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1429×389 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2022-09-15 23:12 UTC)

<p>It looks like there might be an uncompressed image there (indicate by the diagonal patterns).  You can try adjusting the guess parameters to see if you can get something workable.</p>

---

## Post #5 by @lassoan (2022-09-16 04:06 UTC)

<p>You can enable detailed logging of DICOM loading by in menu → Edit / Application Settings / DICOM / Detailed logging → check. After this, click Examine and check the content of the application log.</p>

---
