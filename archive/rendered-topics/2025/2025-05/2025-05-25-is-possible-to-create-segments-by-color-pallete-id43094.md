---
topic_id: 43094
title: "Is Possible To Create Segments By Color Pallete"
date: 2025-05-25
url: https://discourse.slicer.org/t/43094
---

# Is possible to create segments by color pallete?

**Topic ID**: 43094
**Date**: 2025-05-25
**URL**: https://discourse.slicer.org/t/is-possible-to-create-segments-by-color-pallete/43094

---

## Post #1 by @GioM (2025-05-25 19:36 UTC)

<p>Hi all, is it possible to select all the voxels of an image by specifying a color?<br>
I have some CT maps of the brain that highlight the areas with different colors, the simplest one has only one color per map.<br>
This is an example.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97ab85ab8d6fd419a53ca274264c983b84a9b512.png" data-download-href="/uploads/short-url/lDJA7jhkxTX2WQOh5TqgliufYrM.png?dl=1" title="Immagine 2025-05-25 104706" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97ab85ab8d6fd419a53ca274264c983b84a9b512.png" alt="Immagine 2025-05-25 104706" data-base62-sha1="lDJA7jhkxTX2WQOh5TqgliufYrM" width="231" height="250" data-dominant-color="4C3A4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Immagine 2025-05-25 104706</span><span class="informations">687×741 9.13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there any integrated Slicer tool or exention (or maybe a Python script) to do so?<br>
Thanks in advice.</p>

---

## Post #2 by @lassoan (2025-05-25 19:44 UTC)

<p>All segment editor effects currently use a single channel. If you want to select a region based on exact RGB match then you can use a simple Python command as shown in this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">example in the script repository</a>.</p>

---
