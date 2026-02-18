# The brain i stripped from T1 volume can render in 3D window,but can't see any info in 2D window

**Topic ID**: 24920
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/the-brain-i-stripped-from-t1-volume-can-render-in-3d-window-but-cant-see-any-info-in-2d-window/24920

---

## Post #1 by @jay1987 (2022-08-25 12:37 UTC)

<p>the data i have saved in mrb file in dropbox</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/m1atbjh7ck7ekms/325.mrb?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/m1atbjh7ck7ekms/325.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/m1atbjh7ck7ekms/325.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">325.mrb</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
the scene like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/fff477e9c1bd7c4cd0742cb0380570b5d38d848f.jpeg" data-download-href="/uploads/short-url/AwhwCoNfMDPmYl97aPU1vc1iYGP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/fff477e9c1bd7c4cd0742cb0380570b5d38d848f_2_690x497.jpeg" alt="image" data-base62-sha1="AwhwCoNfMDPmYl97aPU1vc1iYGP" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/fff477e9c1bd7c4cd0742cb0380570b5d38d848f_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/fff477e9c1bd7c4cd0742cb0380570b5d38d848f_2_1035x745.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/fff477e9c1bd7c4cd0742cb0380570b5d38d848f.jpeg 2x" data-dominant-color="0E0C0B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1137×819 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
i have tryed most of the lookup table,but can’t see 2D info<br>
i tryed to convert volume to labelmap volume ,it can be seen in 2D window,but it’s not what i want<br>
i don’t known how to see the volume in 2D window , is there something wrong with the volume?</p>

---

## Post #2 by @pieper (2022-08-25 14:51 UTC)

<p>Your scene is corrupted (the volume display node is missing).  Can you describe how you ended up with this?  It should never happen through normal use of the application so if you have a way to reproduce it let us know.  If this happened due to some script or editing the mrml file you’ll need to debug your process.</p>
<p>To get the volume back you can just save it and reload or you can change the mrb file extension to .zip and open the contents.</p>

---

## Post #3 by @jay1987 (2022-08-26 01:41 UTC)

<p>thanks pieper<br>
i use your solution to fix my bugs,it’s work!!<br>
I Added these Code</p>
<p>brain_volume.RemoveAllDisplayNodeIDs()<br>
brain_volume.CreateDefaultDisplayNodes()</p>

---
