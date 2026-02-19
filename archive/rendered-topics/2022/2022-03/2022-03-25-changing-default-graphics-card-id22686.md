---
topic_id: 22686
title: "Changing Default Graphics Card"
date: 2022-03-25
url: https://discourse.slicer.org/t/22686
---

# Changing default graphics card

**Topic ID**: 22686
**Date**: 2022-03-25
**URL**: https://discourse.slicer.org/t/changing-default-graphics-card/22686

---

## Post #1 by @Jasmine_Croghan (2022-03-25 19:14 UTC)

<p>Hi all,</p>
<p>3DSlicer is defaulting to using the integrated graphics card in my computer, but I have a much more powerful discrete graphics card I would like it to use. I’m not seeing an option in the GUI or anything obvious in the program files to help me define which graphics card it uses, and I cannot find anything useful searching the forums.</p>
<p>I think it will significantly increase the performance of anything that needs to display lots of landmarks or a 3D model if I do this, since my copy stutters badly when I mouse over a landmark in Markups module, for instance, and I cannot realtime morph the 3D model in SlicerMorph without a good few minutes of nonresponsive time.</p>
<p>Thankful for any help you can provide.</p>
<p>-Jasmine</p>

---

## Post #2 by @rbumm (2022-03-25 20:26 UTC)

<p>Hi,</p>
<p>Selecting “VTK GPU Raycasting” speeds up “Volume rendering” in ThreeDView  …</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd1521ee0b8c491e41bce0018b7cbb618e80c27f.png" data-download-href="/uploads/short-url/tgf9MbCwcMOsZwYsX4rRcXpfO6b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd1521ee0b8c491e41bce0018b7cbb618e80c27f_2_412x500.png" alt="image" data-base62-sha1="tgf9MbCwcMOsZwYsX4rRcXpfO6b" width="412" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd1521ee0b8c491e41bce0018b7cbb618e80c27f_2_412x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd1521ee0b8c491e41bce0018b7cbb618e80c27f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd1521ee0b8c491e41bce0018b7cbb618e80c27f.png 2x" data-dominant-color="EAEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">597×723 35.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards<br>
Rudolf</p>

---

## Post #3 by @lassoan (2022-03-25 22:20 UTC)

<p>In general, software applications do not have control over what GPU will render them. Therefore, if you have multiple GPUs and the default selection is not optimal then you must change it in your operating system settings. See instructions for example <a href="https://www.makeuseof.com/windows-10-choose-preferred-gpu/">here</a>.</p>

---
