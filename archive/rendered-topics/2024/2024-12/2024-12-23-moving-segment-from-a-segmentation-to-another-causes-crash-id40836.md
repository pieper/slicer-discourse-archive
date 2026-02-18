# Moving segment from a segmentation to another causes crash

**Topic ID**: 40836
**Date**: 2024-12-23
**URL**: https://discourse.slicer.org/t/moving-segment-from-a-segmentation-to-another-causes-crash/40836

---

## Post #1 by @Julien_D (2024-12-23 20:18 UTC)

<p>Hello,</p>
<p>I’m trying to add a geometry (a 25mm x 20mm cylinder created in Fusion 360) in an STL format and then move it to my Segmentation with my other segments but doing so causes the app to run out of memory. I need to move it to the main Segmentation to do boolean operations with my segments.</p>
<ol>
<li>I add the STL file and then convert it to segmentation node.</li>
<li>I drag the segment from the newly created segmentation to the one I already had.<br>
(so far, this doesnt cause any issue)</li>
<li>When I try to save, I get the app running out of memory message.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf7dc932fec4fa01f97d2591f35e7fe42e49f19.png" data-download-href="/uploads/short-url/sXxunXAwGSM9RxX8ak1jeaMNo25.png?dl=1" title="Error 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf7dc932fec4fa01f97d2591f35e7fe42e49f19.png" alt="Error 2" data-base62-sha1="sXxunXAwGSM9RxX8ak1jeaMNo25" width="245" height="264"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error 2</span><span class="informations">245×264 7.74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cea023b7babb6ee732fd86fbc01d3c0a962471e.png" data-download-href="/uploads/short-url/6pkmWy8DtYNzO20m4EQYkF7ccRE.png?dl=1" title="Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cea023b7babb6ee732fd86fbc01d3c0a962471e.png" alt="Error" data-base62-sha1="6pkmWy8DtYNzO20m4EQYkF7ccRE" width="506" height="236"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error</span><span class="informations">506×236 10.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I use version 5.6.2. Had the same issue on two PC:</p>
<ul>
<li>Win 11, 32 GB of RAM</li>
<li>Win 10, 16 GB of RAM</li>
</ul>
<p>Anyone has encouter the same kind of problem?<br>
Thanks!</p>

---

## Post #2 by @muratmaga (2024-12-24 00:47 UTC)

<p>What is the resolution of the segmentation you are trying to import the cylinder model? Perhaps it is too fine? Conversely what is the resolution (segmentation geometry) of the segmentation once you converted from the model?</p>

---
