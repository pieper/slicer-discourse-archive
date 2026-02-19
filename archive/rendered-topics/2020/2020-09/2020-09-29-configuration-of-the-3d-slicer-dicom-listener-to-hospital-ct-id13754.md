---
topic_id: 13754
title: "Configuration Of The 3D Slicer Dicom Listener To Hospital Ct"
date: 2020-09-29
url: https://discourse.slicer.org/t/13754
---

# Configuration of the 3D Slicer DICOM Listener to Hospital CT

**Topic ID**: 13754
**Date**: 2020-09-29
**URL**: https://discourse.slicer.org/t/configuration-of-the-3d-slicer-dicom-listener-to-hospital-ct/13754

---

## Post #1 by @Amy_Morton (2020-09-29 18:36 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.10.2<br>
Expected behavior: a dialog with accessible port configurations<br>
Actual behavior: none found</p>
<p>Beyond the ‘Start Listener’ button in the DICOM module, I cannot configure the listener such that datasets can be pushed to my PC from the the hospital CT scanner (same LAN).</p>

---

## Post #2 by @pieper (2020-10-01 21:31 UTC)

<p>Hi -</p>
<p>It’s a little buried, but the listener configuration (Storage Port and Storage AETITLE) is in the Query dialog.  Set them and then they are used when you start the listener.  If you enter those values in your modality it should be able to push to Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6489a21917b80649d26d5f30f8e4728795d8d9af.png" data-download-href="/uploads/short-url/eloCJKMayDhfrkteEv5FQkwyBFZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6489a21917b80649d26d5f30f8e4728795d8d9af_2_690x404.png" alt="image" data-base62-sha1="eloCJKMayDhfrkteEv5FQkwyBFZ" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6489a21917b80649d26d5f30f8e4728795d8d9af_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6489a21917b80649d26d5f30f8e4728795d8d9af.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6489a21917b80649d26d5f30f8e4728795d8d9af.png 2x" data-dominant-color="ECEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">859×503 99.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Amy_Morton (2020-10-07 13:25 UTC)

<p>Thanks Steve,</p>
<p>I know this thread was referenced elsewhere… if others had similar lingering questions, I wanted to follow-up with what helped me:</p>
<p>This very well written python implementation of the dcmtk library helped sooooo much! I’m still working my way through connectivity to my hospital ct- but I no longer feel lost, wandering in the dark. Cheers!</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://pydicom.github.io/pynetdicom/stable/tutorials/create_scu.html/../_static/favicon.ico" class="site-icon" width="" height="">
      <a href="https://pydicom.github.io/pynetdicom/stable/tutorials/create_scu.html#dicom-networking" target="_blank" rel="noopener nofollow ugc">pydicom.github.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://pydicom.github.io/pynetdicom/stable/tutorials/create_scu.html#dicom-networking" target="_blank" rel="noopener nofollow ugc">Writing your first SCU — pynetdicom 1.5.3 documentation</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @pieper (2020-10-07 14:17 UTC)

<p>That’s great Amy.  Thanks for the link to the pynetdicom docs.  Agreed, that’s a good way to go and maybe we should make use of that in Slicer somehow.  The current Slicer implementation is based on dcmtk, which is also great, but can be a challenge to use.  The python implementation could be a lot more flexible.</p>

---
