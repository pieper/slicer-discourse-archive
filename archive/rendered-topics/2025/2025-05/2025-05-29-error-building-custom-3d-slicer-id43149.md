# Error building custom 3D Slicer

**Topic ID**: 43149
**Date**: 2025-05-29
**URL**: https://discourse.slicer.org/t/error-building-custom-3d-slicer/43149

---

## Post #1 by @nicofutur8 (2025-05-29 14:52 UTC)

<p>Hello everyone!</p>
<p>I want to build a custom Slicer3D using your template by Kitware. I followed steps thoroughly but, at the end of the building phase, i get an error envolving some kind of VTK feature called vtkTeemPython.</p>
<p>i don’t know from where this error comes and Visual Studio’s traceback is not helping to be honest…</p>
<p>The error code is MSB8066 and its something like that:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95d6abf8ad05d2b0efd2dfea0fc353e9c147fda6.png" data-download-href="/uploads/short-url/lnx4Fb3b7nhQr5sZDMJrI1U8rHM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95d6abf8ad05d2b0efd2dfea0fc353e9c147fda6.png" alt="image" data-base62-sha1="lnx4Fb3b7nhQr5sZDMJrI1U8rHM" width="690" height="79" data-dominant-color="353536"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1073×124 6.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d94c0e5dc66c10d065969d20c0e1211f482e524.png" data-download-href="/uploads/short-url/mu1Fhg4RM6NVg1tNhBNOxIys0cY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d94c0e5dc66c10d065969d20c0e1211f482e524.png" alt="image" data-base62-sha1="mu1Fhg4RM6NVg1tNhBNOxIys0cY" width="690" height="153" data-dominant-color="4B4B4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1100×245 7.75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could anyone help me finding out what is happening?<br>
Thanks in advance</p>

---

## Post #2 by @cpinter (2025-06-02 10:34 UTC)

<p>First of all, I’d try running the superbuild again, without deleting anything. Sometimes there are hiccups that simply resuming the build fixes.</p>
<p>If you see the same error, then please share the whole log, because then it is possible that there are other issues that cause this one.</p>

---

## Post #3 by @nicofutur8 (2025-06-03 10:00 UTC)

<p>Hello Csaba!</p>
<p>I’ve tried like 30 times to rebuild it with no success <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=14" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>Here’s the full log of my last build:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/b0e9c27af2a74a1768bfc73d6960196a20250603095734/d56ee2?t_exp=1749203854&amp;t_lsid=a38681cf-725b-4f36-916f-800280500e68&amp;t_network=link&amp;t_rid=b2F1dGgyfHNsYWNrfFQwMjhBQUI5M0NOLVUwMjhBUVNIMDlM&amp;t_s=download_link&amp;t_ts=1748944680">
  <header class="source">
      <img src="https://wetransfer.com/favicon.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/b0e9c27af2a74a1768bfc73d6960196a20250603095734/d56ee2?t_exp=1749203854&amp;t_lsid=a38681cf-725b-4f36-916f-800280500e68&amp;t_network=link&amp;t_rid=b2F1dGgyfHNsYWNrfFQwMjhBQUI5M0NOLVUwMjhBUVNIMDlM&amp;t_s=download_link&amp;t_ts=1748944680" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://wetransfer.com/downloads/b0e9c27af2a74a1768bfc73d6960196a20250603095734/d56ee2?t_exp=1749203854&amp;t_lsid=a38681cf-725b-4f36-916f-800280500e68&amp;t_network=link&amp;t_rid=b2F1dGgyfHNsYWNrfFQwMjhBQUI5M0NOLVUwMjhBUVNIMDlM&amp;t_s=download_link&amp;t_ts=1748944680" target="_blank" rel="noopener nofollow ugc">last build</a></h3>

  <p>1 file sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I could not copypaste it due to its size.<br>
Tell me if I could do anything please<br>
Thanks in advance!<br>
Nico</p>

---

## Post #4 by @jcfr (2025-06-03 16:04 UTC)

<p>Thanks for your patience with the process <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>
<p>Could you share the error copying the relevant text ?</p>
<p>You may be able to find the actual issue by scrolling up in the log.</p>
<p>For sake of transparency and visibility, avoid uploading the details onto third-party website.</p>

---

## Post #5 by @jcfr (2025-06-03 16:05 UTC)

<p>For reference, the discussion has been moved into the issue tracker.<br>
See <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/issues/99">https://github.com/KitwareMedical/SlicerCustomAppTemplate/issues/99</a></p>
<p>An update will be posted here once the issue has been sorted out.</p>

---

## Post #6 by @cpinter (2025-06-04 10:31 UTC)

<p>Alright. I posted my suggestion on the ticket. The first issue seems to be an easy one.</p>

---
