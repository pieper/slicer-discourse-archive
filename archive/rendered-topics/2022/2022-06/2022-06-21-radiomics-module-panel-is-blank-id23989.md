---
topic_id: 23989
title: "Radiomics Module Panel Is Blank"
date: 2022-06-21
url: https://discourse.slicer.org/t/23989
---

# Radiomics module panel is blank

**Topic ID**: 23989
**Date**: 2022-06-21
**URL**: https://discourse.slicer.org/t/radiomics-module-panel-is-blank/23989

---

## Post #1 by @harad (2022-06-21 11:48 UTC)

<p>Thank you. My experience in Windows is that SlicerRadiomics is available in list of extensions and installs in all 3D Slicer versions, always shows up in INFORMATICS, but does not work in any version later than 4.10.<br>
When started in versions past 4.10, SlicerRadiomics menu remains blank after it is started. Any feedback will be appreciated.  Cheers, Marko</p>

---

## Post #2 by @lassoan (2022-06-21 15:24 UTC)

<p>SlicerRadiomics works well on my Windows and Linux computers.</p>
<p>When you first switch to Radiomics module then it downloads <code>dateutil</code> and <code>pywavelets</code> packages from PyPI, which typically takes a few seconds. If you open the Python console then you should see something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97566e9403d95b3e6e06da7a83f66ee73568232e.png" data-download-href="/uploads/short-url/lANhdcyDVAJHnMuTXAncucWsF7o.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97566e9403d95b3e6e06da7a83f66ee73568232e_2_690x361.png" alt="image" data-base62-sha1="lANhdcyDVAJHnMuTXAncucWsF7o" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97566e9403d95b3e6e06da7a83f66ee73568232e_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97566e9403d95b3e6e06da7a83f66ee73568232e_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97566e9403d95b3e6e06da7a83f66ee73568232e_2_1380x722.png 2x" data-dominant-color="A7A7AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1005 71.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If your computer is behind a restrictive firewall or proxy server then pip may fail and so the module will not start up. Or if something is unusual in how your computer or Slicer is set up then maybe pip cannot download and install the package due to some file access restrictions.</p>
<p>Have a look at the Python console to see what error messages you get and we can go from there.</p>

---

## Post #3 by @harad (2022-06-22 11:51 UTC)

<p>Many thanks Andras, your quick advice has resolved the issue entirely!!!<br>
The problem was either the firewall or proxy. Cheers, Marko</p>

---
