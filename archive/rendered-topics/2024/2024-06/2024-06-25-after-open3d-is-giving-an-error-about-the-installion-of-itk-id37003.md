---
topic_id: 37003
title: "After Open3D Is Giving An Error About The Installion Of Itk"
date: 2024-06-25
url: https://discourse.slicer.org/t/37003
---

# After open3d is giving an error about the installion of itk

**Topic ID**: 37003
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/after-open3d-is-giving-an-error-about-the-installion-of-itk/37003

---

## Post #1 by @yijie3091 (2024-06-25 13:22 UTC)

<p>Operating system:windows<br>
Slicer version:5.6.2<br>
Expected behavior:ALPACA run successfully.<br>
Actual behavior:When I run ALPACA,it will show"Issue while installing the ITK Python packages."after the open3d<br>
Python 3.9.10 (main, Jun 19 2024, 15:19:10) [MSC v.1939 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/itk/<br>
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/itk/<br>
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/itk/<br>
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/itk/<br>
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/itk/<br>
Could not fetch URL <a href="https://pypi.org/simple/itk/:" rel="noopener nofollow ugc">https://pypi.org/simple/itk/:</a> There was a problem confirming the ssl certificate: HTTPSConnectionPool(host=‘<a href="http://pypi.org" rel="noopener nofollow ugc">pypi.org</a>’, port=443): Max retries exceeded with url: /simple/itk/ (Caused by SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))) - skipping<br>
ERROR: Could not find a version that satisfies the requirement itk==5.3.0 (from versions: none)<br>
ERROR: No matching distribution found for itk==5.3.0<br>
Traceback (most recent call last):<br>
File “C:/Users/18797/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 126, in setup<br>
import itk<br>
ModuleNotFoundError: No module named ‘itk’</p>

---

## Post #2 by @muratmaga (2024-06-25 16:05 UTC)

<p>Open3D hasn’t been used in ALPACA for over a year now. Version in the current stable (5.6.2) uses ITK libraries and that’s what is trying to download.</p>
<p>All your errors are certificate errors, meaning your computer cannot download files due to incorrect certificates. This can happen in networks with tight security settings and firewalls with self-signed certificates.</p>
<p>Is there another connection you can try, a public wifi perhaps?</p>

---

## Post #3 by @yijie3091 (2024-06-25 16:12 UTC)

<p>I install the itk 5.3.0 in the python，but when i run the alpaca，it still occur the surface“Issue<br>
while installing the ITK Python package”.How can i deal with it？<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7e8fff30c90be6ce6e608c8dfc15ae6c4088205.jpeg" data-download-href="/uploads/short-url/x5zuIv8WrIwW0rwa3H9bts1WtRX.jpeg?dl=1" title="IMG_1113.jpeg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7e8fff30c90be6ce6e608c8dfc15ae6c4088205_2_690x388.jpeg" data-base62-sha1="x5zuIv8WrIwW0rwa3H9bts1WtRX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7e8fff30c90be6ce6e608c8dfc15ae6c4088205_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7e8fff30c90be6ce6e608c8dfc15ae6c4088205_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7e8fff30c90be6ce6e608c8dfc15ae6c4088205_2_1380x776.jpeg 2x" data-dominant-color="9D9792"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1113.jpeg</span><span class="informations">1920×1080 388 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/528237954d6dc296d86331ec6b15b5017ac40096.jpeg" data-download-href="/uploads/short-url/bLU8LPbkKtxy18SEJEMy39Bi4Wq.jpeg?dl=1" title="4da9087bd9868ce1454f5547d2a7358f.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/528237954d6dc296d86331ec6b15b5017ac40096_2_690x419.jpeg" data-base62-sha1="bLU8LPbkKtxy18SEJEMy39Bi4Wq" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/528237954d6dc296d86331ec6b15b5017ac40096_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/528237954d6dc296d86331ec6b15b5017ac40096_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/528237954d6dc296d86331ec6b15b5017ac40096_2_1380x838.jpeg 2x" data-dominant-color="C1C0BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4da9087bd9868ce1454f5547d2a7358f.jpg</span><span class="informations">1620×985 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Murat Maga via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;于2024年6月26日 周三00:05写道：</p>

---

## Post #4 by @muratmaga (2024-06-25 16:52 UTC)

<p>You are not displaying the whole log file, so I can’t tell what’s the “issue”. I suspect it is the same as before SSL certificate issue. The only solution to that is to try on another network.</p>

---

## Post #5 by @muratmaga (2024-06-25 17:20 UTC)

<p>If you cannot find a working network, you can try to download this zip file. It should have all libraries for ALPACA already loaded in it. Unzip, and launch Slicer from that folder.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://app.box.com/s/xziombnoti3jbrc8hqp236v95ghcz2c2">
  <header class="source">
      <img src="https://cdn01.boxcdn.net/_assets/img/favicons/favicon-32x32-VwW37b.png" class="site-icon" width="32" height="32">

      <a href="https://app.box.com/s/xziombnoti3jbrc8hqp236v95ghcz2c2" target="_blank" rel="noopener">app.box.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://cdn01.boxcdn.net/app-assets/preview/box-social.jpeg" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://app.box.com/s/xziombnoti3jbrc8hqp236v95ghcz2c2" target="_blank" rel="noopener">Slicer-5.6.2-Win.zip | Powered by Box</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @yijie3091 (2024-06-27 11:27 UTC)

<p>Thanks very much！The zip is useful!</p>

---
