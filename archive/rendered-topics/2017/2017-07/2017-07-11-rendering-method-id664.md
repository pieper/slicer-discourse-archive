---
topic_id: 664
title: "Rendering Method"
date: 2017-07-11
url: https://discourse.slicer.org/t/664
---

# Rendering method

**Topic ID**: 664
**Date**: 2017-07-11
**URL**: https://discourse.slicer.org/t/rendering-method/664

---

## Post #1 by @phil.dunn (2017-07-11 13:00 UTC)

<p>Hi, when rotating a Volume within the ‘volume rendering’ module, the detail shown in the render drops to a low level and then takes time to render back up to full resolution. Presumably this is down to the computational power avalible, therefore I’d like to change the rendering option from ‘VTK CPU Ray Casting’ to something else that uses the GPU, however there are no other options in the drop down box on the pannel on the left nor in the setting control box.</p>
<p>Can someone give me some help / advice to get the settings changed or otherwise increase rendering performance.</p>
<p>Thanks<br>
Phil</p>

---

## Post #2 by @jcfr (2017-07-11 13:22 UTC)

<p>Hi Phil,</p>
<p>Could you try with the nightly build available at <a href="http://download.slicer.org">http://download.slicer.org</a> ?</p>
<p>As depicted on the screenshot, you should be able to select between CPU and CPU method.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/4e0d88f39bd916c4c14aa5061b9ddb697dc8c7f3.jpg" data-download-href="/uploads/short-url/b8ueXhuL5YweZc3W4RwHeknW4jF.jpg?dl=1" title="Screenshot from 2017-07-11 09-18-58.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4e0d88f39bd916c4c14aa5061b9ddb697dc8c7f3_2_690x462.jpg" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4e0d88f39bd916c4c14aa5061b9ddb697dc8c7f3_2_690x462.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4e0d88f39bd916c4c14aa5061b9ddb697dc8c7f3_2_1035x693.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e0d88f39bd916c4c14aa5061b9ddb697dc8c7f3.jpeg 2x" data-dominant-color="ADADC1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2017-07-11 09-18-58.jpg</span><span class="informations">1232×825 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @chir.set (2017-07-11 13:29 UTC)

<p>Le mardi 11 juillet 2017 15:11:02 CEST vous avez écrit :</p>
<blockquote>
<p>to something else that uses the GPU</p>
</blockquote>
<p>But GPU rendering is the most efficient way, and you might even need ‘Maximum<br>
quality’ for a good experience. You will need an adequate driver for the GPU<br>
in any case, on any platform.</p>

---
