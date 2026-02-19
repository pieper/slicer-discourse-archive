---
topic_id: 41212
title: "Need Help On Changing Dicom Modality"
date: 2025-01-22
url: https://discourse.slicer.org/t/41212
---

# Need help on changing dicom modality

**Topic ID**: 41212
**Date**: 2025-01-22
**URL**: https://discourse.slicer.org/t/need-help-on-changing-dicom-modality/41212

---

## Post #1 by @alientex (2025-01-22 09:26 UTC)

<p><strong>Hello,</strong></p>
<p>As per my use case, I want to change the modality of DICOM data when importing a DICOM directory, so that when viewing the DICOM metadata, it reflects the changes I made.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbdc4e61512459f463113a731a600a256ef4aad0.png" data-download-href="/uploads/short-url/t5qVG4eUwCAreiDaraPoCZGCL3a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc4e61512459f463113a731a600a256ef4aad0_2_345x159.png" alt="image" data-base62-sha1="t5qVG4eUwCAreiDaraPoCZGCL3a" width="345" height="159" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc4e61512459f463113a731a600a256ef4aad0_2_345x159.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc4e61512459f463113a731a600a256ef4aad0_2_517x238.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc4e61512459f463113a731a600a256ef4aad0_2_690x318.png 2x" data-dominant-color="EEF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1353×627 20.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can anyone please help me achieve this?</p>

---

## Post #2 by @pieper (2025-01-22 19:02 UTC)

<p>You can write a simple pydicom script to do this, but it’s not avalable in the GUI of Slicer.</p>

---

## Post #3 by @alientex (2025-01-23 03:57 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Could you please show me how to directly change it through the code during the import operation? Also, I want to perform this in C++. Could you please guide me in which file should I make changes?</p>
<p>Thanks for any help.</p>

---

## Post #4 by @pieper (2025-01-23 13:29 UTC)

<p>Chaning the modality is a very unusual action.  Can you describe why you need to do it?</p>
<p>I would suggest doing this in a separate pass, not part of the dicom import operation.  You can find lots of examples in C++ using dcmtk, gdcm, or other toolkits.  But python would be a lot easier.</p>

---
