# Cannot load DVF

**Topic ID**: 15807
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/cannot-load-dvf/15807

---

## Post #1 by @toyama (2021-02-03 08:59 UTC)

<p>When I tried to import a DVF (.dcm file) created by another software, the message “Not Dicom File” was displayed.<br>
Please let me know if there is a way to import a DVF created by a software other than 3DSlicer.</p>

---

## Post #2 by @lassoan (2021-02-03 16:24 UTC)

<p>You can import DICOM Spatial Registration Objects into Slicer using DICOM module, after you installed SlicerRT extension.</p>

---

## Post #3 by @toyama (2021-02-04 08:12 UTC)

<p>Thank you for your answer.<br>
Even with “Slicer RT” and “Registration QA” already installed, the message “Not Dicom File” was displayed.<br>
I am importing files from the DICOM module. Is there any special procedure to import DICOM Spatial Registration Objects?</p>

---

## Post #4 by @lassoan (2021-02-04 14:24 UTC)

<aside class="quote no-group" data-username="toyama" data-post="3" data-topic="15807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>the message “Not Dicom File” was displayed.</p>
</blockquote>
</aside>
<p>Where is this displayed?</p>
<aside class="quote no-group" data-username="toyama" data-post="3" data-topic="15807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>I am importing files from the DICOM module. Is there any special procedure to import DICOM Spatial Registration Objects?</p>
</blockquote>
</aside>
<p>DICOM import/export plugins run in the DICOM module, so you use DICOM module as usual.</p>
<p>Can you upload a problematic file to somewhere (dropbox, onedrive, …) and post the link here so that we can have a look?</p>

---

## Post #6 by @toyama (2021-02-05 10:07 UTC)

<p>Dropbox link. Please check it out.<br>
When you load this file, it will look like the image.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/r9deagnk9yji0m8/AADhjEg3qMwoDDGfR8vwEoRga?dl=0https:%2F%2Fwww.dropbox.com%2Fsh%2Fr9deagnk9yji0m8%2FAADhjEg3qMwoDDGfR8vwEoRga?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/r9deagnk9yji0m8/AADhjEg3qMwoDDGfR8vwEoRga?dl=0https:%2F%2Fwww.dropbox.com%2Fsh%2Fr9deagnk9yji0m8%2FAADhjEg3qMwoDDGfR8vwEoRga?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-folder-dropbox-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/sh/r9deagnk9yji0m8/AADhjEg3qMwoDDGfR8vwEoRga?dl=0https:%2F%2Fwww.dropbox.com%2Fsh%2Fr9deagnk9yji0m8%2FAADhjEg3qMwoDDGfR8vwEoRga?dl=0" target="_blank" rel="noopener nofollow ugc">2_2_REG_2017-06-30_094950_._DEFORMABLE.REG_n1__00000</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a761777322e0fa2e4a3a9bcf20bf7d682143133.png" data-download-href="/uploads/short-url/htlgdE9EmexPzGFJkmftWa3F467.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a761777322e0fa2e4a3a9bcf20bf7d682143133_2_690x242.png" alt="image" data-base62-sha1="htlgdE9EmexPzGFJkmftWa3F467" width="690" height="242" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a761777322e0fa2e4a3a9bcf20bf7d682143133_2_690x242.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a761777322e0fa2e4a3a9bcf20bf7d682143133_2_1035x363.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a761777322e0fa2e4a3a9bcf20bf7d682143133_2_1380x484.png 2x" data-dominant-color="7B7C81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1957×687 34.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
