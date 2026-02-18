# Controlling the z on fiducial markups

**Topic ID**: 16655
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/controlling-the-z-on-fiducial-markups/16655

---

## Post #1 by @rebecca-green (2021-03-20 04:38 UTC)

<p>Has anyone had an issue with fiducial markups ending up on the inside or in front or behind a surface? Is there anyway to control this when placing in 3D?</p>

---

## Post #2 by @muratmaga (2021-03-20 04:42 UTC)

<p>No, normally when fiducials are placed, they are constrained to the surface (setting below is the default). Can share an example?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0078f229c9c349b949fc8f06243d54d53ce4d3cd.png" data-download-href="/uploads/short-url/4b7MqTS95FdJhwN6J2EUFKMWHX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0078f229c9c349b949fc8f06243d54d53ce4d3cd.png" alt="image" data-base62-sha1="4b7MqTS95FdJhwN6J2EUFKMWHX" width="347" height="500" data-dominant-color="F0F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">531×763 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @rebecca-green (2021-03-20 13:53 UTC)

<p>Yeah, I checked the placement mode setting. It seems to have been some sort of a bug and/or issue with VTK multivolume rendering (which somehow got turned on). I restarted my computer and changed to Ray casting and that solved it.<br>
Thanks Murat!!!</p>

---

## Post #4 by @muratmaga (2021-03-20 14:52 UTC)

<p>Yes, multi volume rendering is experimental and may have some issues. If It is keep coming back as default (after you restart slicer), check application settings-&gt;volume rendering to make sure that it is not set as default for some reason.</p>

---
