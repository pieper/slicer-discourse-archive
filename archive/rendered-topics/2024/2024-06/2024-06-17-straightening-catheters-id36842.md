# Straightening Catheters

**Topic ID**: 36842
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/straightening-catheters/36842

---

## Post #1 by @Jessica_de_Kort (2024-06-17 18:52 UTC)

<p>Hi there, I have curved catheter predicted models and I want the first half of the prediction to be straight and the second half to keep its predicted curvature. Is there a module that would allow me to adjust this curvature?</p>

---

## Post #2 by @lassoan (2024-06-17 19:28 UTC)

<p>Yes, sure, you can straighten the image of a catheter and surrounding structures using <code>Curved Planar Reformat</code> module in <code>Sandbox</code> extension.</p>

---

## Post #3 by @Jessica_de_Kort (2024-06-17 20:48 UTC)

<p>Thank you!</p>
<p>I tried to open up extensions and it shows there are 0 extensions available. I can’t look up or search through any available extensions. I tried to adjust the settings and reopen slicer but nothing has worked. Any suggestions of how to fix this so I can install Sandbox? I downloaded the Zip file of Sandbox to install it but it wouldn’t accept the zip file.</p>

---

## Post #4 by @lassoan (2024-06-17 21:25 UTC)

<p>Most likely your computer is behind a very restrictive institutional network firewall. If you have access to a web browser then you can still download and install extensions manually as described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection">Extensions Manager documentation</a>.</p>

---

## Post #5 by @Jessica_de_Kort (2024-06-19 16:57 UTC)

<p>Even after following the instructions and opening extensions manager in my web browser, it still looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0c0d6c13b03e347bc0decf1f3b7e029bfd7f46b.png" data-download-href="/uploads/short-url/w4g6KbiFoXQ9jf5HKfiR5whRvnR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c0d6c13b03e347bc0decf1f3b7e029bfd7f46b_2_690x433.png" alt="image" data-base62-sha1="w4g6KbiFoXQ9jf5HKfiR5whRvnR" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c0d6c13b03e347bc0decf1f3b7e029bfd7f46b_2_690x433.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c0d6c13b03e347bc0decf1f3b7e029bfd7f46b_2_1035x649.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0c0d6c13b03e347bc0decf1f3b7e029bfd7f46b.png 2x" data-dominant-color="FDFDFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1352×850 16.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-06-22 11:49 UTC)

<p>There might have been something wrong with the specific Slicer version that you installed, as that address shows an empty page for me, too. However, for example the latest release has extensions available - see <a href="https://extensions.slicer.org/catalog/All/32906/win" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a></p>
<p>Please install the latest Slicer Stable Release or the latest Slicer Preview Release and extensions will be available for those.</p>

---
