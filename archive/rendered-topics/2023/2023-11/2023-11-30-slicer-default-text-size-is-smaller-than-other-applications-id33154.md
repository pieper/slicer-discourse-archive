---
topic_id: 33154
title: "Slicer Default Text Size Is Smaller Than Other Applications"
date: 2023-11-30
url: https://discourse.slicer.org/t/33154
---

# Slicer default text-size is smaller than other applications (Windows)

**Topic ID**: 33154
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/slicer-default-text-size-is-smaller-than-other-applications-windows/33154

---

## Post #1 by @mau_igna_06 (2023-11-30 21:56 UTC)

<p>Please see image below showing from left to right a firefox window, visual studio code and Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ef8d1106c5bf6e7da3bc3ebb3dcba27eeaaa76e.png" data-download-href="/uploads/short-url/8Z4GNSPG1EuABq2Sw4eIQU973t4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ef8d1106c5bf6e7da3bc3ebb3dcba27eeaaa76e_2_690x352.png" alt="image" data-base62-sha1="8Z4GNSPG1EuABq2Sw4eIQU973t4" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ef8d1106c5bf6e7da3bc3ebb3dcba27eeaaa76e_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ef8d1106c5bf6e7da3bc3ebb3dcba27eeaaa76e_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ef8d1106c5bf6e7da3bc3ebb3dcba27eeaaa76e_2_1380x704.png 2x" data-dominant-color="38373A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1590×812 97.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hope you can help</p>

---

## Post #2 by @jamesobutler (2023-11-30 22:32 UTC)

<p>The default Slicer font of 8pt is quite small. In my own Slicer custom application we have taken action to increase the app font size to be larger to comply with WCAG 2.0 Guidelines. A lot can be impacted here if too much content was being displayed in a small area where a larger font results in content getting cut off if size policies and layouts were not set to be well responsive. So a long with this we had to update our various modules to be compliant with the larger styling of things. In our case we increased both the size of font and widgets.</p>
<p>Looking at just the menu bar font, shown below is Slicer 8pt at the top, VS Code in the middle and Slicer using 10pt font which is more like VS Code.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35c6c34596ea6d7cf555160fca709b7d4dc31a6f.png" alt="image" data-base62-sha1="7FJ9v0lmDE129xzGnogn8TLGm3t" width="237" height="144"></p>
<p>I changed Slicer’s application font by going to Edit-&gt;Application Settings-&gt;Appearance and change “Font and size”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ead682cb015dea51a447cc4db569a46069d2d55f.png" data-download-href="/uploads/short-url/xvtjz81SHdhMX7JQXVV8L7J3qmb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ead682cb015dea51a447cc4db569a46069d2d55f.png" alt="image" data-base62-sha1="xvtjz81SHdhMX7JQXVV8L7J3qmb" width="690" height="157" data-dominant-color="F3F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">776×177 7.18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
