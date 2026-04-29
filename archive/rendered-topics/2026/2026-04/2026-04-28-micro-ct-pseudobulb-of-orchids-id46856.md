---
topic_id: 46856
title: "Micro Ct Pseudobulb Of Orchids"
date: 2026-04-28
url: https://discourse.slicer.org/t/46856
---

# Micro-CT Pseudobulb of Orchids: 

**Topic ID**: 46856
**Date**: 2026-04-28
**URL**: https://discourse.slicer.org/t/micro-ct-pseudobulb-of-orchids/46856

---

## Post #1 by @Akhmad_Fauzan (2026-04-28 15:32 UTC)

<p>I’m having trouble with my 3D volume rendering. I am currently trying to render a 3D volume of a pseudobulb. The object appears as a thin, flattened disk rather than a full 3D structure. Could this be an issue with the ‘Image Spacing’ or ‘Voxel Size’ not being read correctly from the metadata, or is it simply because the Z-dimension is too low? Any advice on how to make it look more representative would be appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc.png" data-download-href="/uploads/short-url/86xcpKKwYNb3jW4RQUNMjPmHUny.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_690x345.png" alt="image" data-base62-sha1="86xcpKKwYNb3jW4RQUNMjPmHUny" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38ce8480feab9dc1309cc5609a6988be21af7afc_2_1380x690.png 2x" data-dominant-color="3A3D3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×958 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-04-28 16:58 UTC)

<p>Do you know the actual z spacing?  If so you can type it in.  Otherwise it may be in the header in a format slicer doesn’t understand so you need to dig it out manually.</p>
<p>In general though this data is highly anisotropic (only 10 slices) so don’t expect a lot of 3D info. The segmentation you have is pretty meaningless, but you could try just volume rendering directly to see the internal structure in 3D.</p>

---
