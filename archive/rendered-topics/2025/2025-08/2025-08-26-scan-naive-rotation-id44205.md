# Scan naive rotation

**Topic ID**: 44205
**Date**: 2025-08-26
**URL**: https://discourse.slicer.org/t/scan-naive-rotation/44205

---

## Post #1 by @Shirly_Someck (2025-08-26 10:36 UTC)

<p>Hi,</p>
<p>I want to rotate a scan in a naive way, like this button in word</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8d5fbc598bef4521cf4a0341b723600965bb789.png" alt="image" data-base62-sha1="o5AFHdXJeshEjwNXaQKlKz12uyR" width="71" height="69"></p>
<p>for example, turn this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69588d1992f091f39ebd74c1775796c18404b717.jpeg" data-download-href="/uploads/short-url/f1VQYl7QdFQpTQq2TBXuuBblGiH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69588d1992f091f39ebd74c1775796c18404b717.jpeg" alt="image" data-base62-sha1="f1VQYl7QdFQpTQq2TBXuuBblGiH" width="690" height="402" data-dominant-color="251F1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×409 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>into:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc45b70b8ea7083adf67e5ce2f1901c18bd6522.jpeg" data-download-href="/uploads/short-url/46u3ShHVDHhxjb2HHVHEpcdQ3tw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc45b70b8ea7083adf67e5ce2f1901c18bd6522_2_690x448.jpeg" alt="image" data-base62-sha1="46u3ShHVDHhxjb2HHVHEpcdQ3tw" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc45b70b8ea7083adf67e5ce2f1901c18bd6522_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc45b70b8ea7083adf67e5ce2f1901c18bd6522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc45b70b8ea7083adf67e5ce2f1901c18bd6522.jpeg 2x" data-dominant-color="6E6969"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">859×558 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Shift didn’t work…</p>
<p>Thanks in advance!</p>
<p>Shirly</p>

---

## Post #2 by @muratmaga (2025-08-26 13:39 UTC)

<p>Go to Data module. Right click on the visibility (eye) icon of your volume, and choose “Enable Interactions”. Then use widgets that appear in slice views to arbitrarily rotate your volume.</p>

---

## Post #3 by @Shirly_Someck (2025-08-28 09:04 UTC)

<p>Thanks for your response, however I was looking for rotation of the view, not of the volume.</p>
<p>Specifically, I am interested in rotating the axial slice view only, similarly to the function of panning by clicking on the mouse wheel. Is there a way to do that?</p>

---

## Post #4 by @muratmaga (2025-08-28 09:52 UTC)

<p>See user manual on 2d view specifically reformat widget.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" target="_blank" rel="noopener">User Interface — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Shirly_Someck (2025-08-31 14:04 UTC)

<p>Thanks, I am familiar with the reformat widget, it is not quite what I am looking for.</p>
<p>I don’t wish to change the slice plane, only to spin the existing view in the same plane</p>

---

## Post #6 by @muratmaga (2025-09-01 11:40 UTC)

<p>Don’t think that’s possible for 2D views without the use of the reformat widget and/or transforms.</p>
<p>The closest I can think of is to enable the slice view in 3D viewer, and then use the CMD/ALT (mac/windows) click to rotate the view in plane.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da6c0eb5d4035396f80e20a2912d26499b87433d.jpeg" data-download-href="/uploads/short-url/vafBeInJvB2GU0oCpc4ResQM0Nv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6c0eb5d4035396f80e20a2912d26499b87433d_2_690x451.jpeg" alt="image" data-base62-sha1="vafBeInJvB2GU0oCpc4ResQM0Nv" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6c0eb5d4035396f80e20a2912d26499b87433d_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6c0eb5d4035396f80e20a2912d26499b87433d_2_1035x676.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da6c0eb5d4035396f80e20a2912d26499b87433d.jpeg 2x" data-dominant-color="707086"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×786 68.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Shirly_Someck (2025-09-08 15:22 UTC)

<p>ok, thanks, I tried to test what you suggested but ALT doesn’t seem to have any effect..</p>
<p>I’m using slicer 5.8.1 on a windows</p>

---

## Post #8 by @muratmaga (2025-09-08 15:32 UTC)

<p>Sorry it seems CTRL on windows. See the keyboard shortcuts:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-views">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-views" target="_blank" rel="noopener">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-views" target="_blank" rel="noopener">User Interface — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
