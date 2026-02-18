# Crop volume broken in Linux

**Topic ID**: 17228
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/crop-volume-broken-in-linux/17228

---

## Post #1 by @manjula (2021-04-21 15:56 UTC)

<p>Slicer version - 4.13.0-2021-04-03 r29809 / 057dea2 and 4.13.0-2021-04-18 r29854</p>
<p>OS - Linux - Garuda Linux</p>
<p>The crop volume seems to not work and I just tried the latest preview release as well and there also it is not working.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/119e4268a7cc0aa098c4d9a4ca2b550b0b2d8506.jpeg" data-download-href="/uploads/short-url/2vRbxP5EYwcTsKky4KSz4aqHDEO.jpeg?dl=1" title="Screenshot_22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119e4268a7cc0aa098c4d9a4ca2b550b0b2d8506_2_690x388.jpeg" alt="Screenshot_22" data-base62-sha1="2vRbxP5EYwcTsKky4KSz4aqHDEO" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119e4268a7cc0aa098c4d9a4ca2b550b0b2d8506_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119e4268a7cc0aa098c4d9a4ca2b550b0b2d8506_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119e4268a7cc0aa098c4d9a4ca2b550b0b2d8506_2_1380x776.jpeg 2x" data-dominant-color="9D9DAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_22</span><span class="informations">1920×1080 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-04-21 18:28 UTC)

<p>It works on my local linux build.  Were there messages in the error log?</p>

---

## Post #3 by @manjula (2021-04-22 09:37 UTC)

<p>I did some digging to strangely find out that this problem happens with the two Volumes files I was using only. When I tried a different volume it worked well. <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"> There are no error logs.<br>
Sample Chest CT was cropped successfully.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/715db09662b838725763b8483588c84b859f1518.jpeg" data-download-href="/uploads/short-url/gaSGnPORJEESe0HoCmNiTShCrby.jpeg?dl=1" title="Screenshot_24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/715db09662b838725763b8483588c84b859f1518_2_690x388.jpeg" alt="Screenshot_24" data-base62-sha1="gaSGnPORJEESe0HoCmNiTShCrby" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/715db09662b838725763b8483588c84b859f1518_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/715db09662b838725763b8483588c84b859f1518_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/715db09662b838725763b8483588c84b859f1518_2_1380x776.jpeg 2x" data-dominant-color="A098AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_24</span><span class="informations">1920×1080 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, the mandible in dicom format was successfully cropped.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/770b888a1086b3ed4014f316e83fc843b1979388.png" data-download-href="/uploads/short-url/gZ7wNO3txnK8lOS2Znk7YM5Zfmg.png?dl=1" title="Screenshot_28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/770b888a1086b3ed4014f316e83fc843b1979388_2_690x388.png" alt="Screenshot_28" data-base62-sha1="gZ7wNO3txnK8lOS2Znk7YM5Zfmg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/770b888a1086b3ed4014f316e83fc843b1979388_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/770b888a1086b3ed4014f316e83fc843b1979388_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/770b888a1086b3ed4014f316e83fc843b1979388_2_1380x776.png 2x" data-dominant-color="8F8B9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_28</span><span class="informations">1920×1080 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, two nrrd volumes I tried cropping still do not work and there is no error logs.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc3393055a7d8671b9c77682e6126b9f815ba75a.jpeg" data-download-href="/uploads/short-url/vpZxxkfXTP3hkCh1XXprrfDNBmG.jpeg?dl=1" title="Screenshot_26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc3393055a7d8671b9c77682e6126b9f815ba75a_2_690x388.jpeg" alt="Screenshot_26" data-base62-sha1="vpZxxkfXTP3hkCh1XXprrfDNBmG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc3393055a7d8671b9c77682e6126b9f815ba75a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc3393055a7d8671b9c77682e6126b9f815ba75a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc3393055a7d8671b9c77682e6126b9f815ba75a_2_1380x776.jpeg 2x" data-dominant-color="928FA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_26</span><span class="informations">1920×1080 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2021-04-22 11:25 UTC)

<p>Hmm… can you share a file that doesn’t work?</p>

---

## Post #5 by @manjula (2021-04-22 12:49 UTC)

<p>After deleting all Slicer folders and fresh download of the preview release it works as usual. In any case here is the first file that did not work.</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1VenhwkTY7sNhtpfP4QTDiNXuZjeIvldp/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1VenhwkTY7sNhtpfP4QTDiNXuZjeIvldp/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1VenhwkTY7sNhtpfP4QTDiNXuZjeIvldp/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">MandibleVolume.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @pieper (2021-04-22 12:58 UTC)

<p>Okay, glad it’s working now.  Perhaps there was an issue in the temp directory.  Let us know if it happens again in a reproducible way.</p>

---
