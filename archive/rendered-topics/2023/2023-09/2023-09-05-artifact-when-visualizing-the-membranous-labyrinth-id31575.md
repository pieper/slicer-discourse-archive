---
topic_id: 31575
title: "Artifact When Visualizing The Membranous Labyrinth"
date: 2023-09-05
url: https://discourse.slicer.org/t/31575
---

# Artifact when Visualizing the Membranous Labyrinth

**Topic ID**: 31575
**Date**: 2023-09-05
**URL**: https://discourse.slicer.org/t/artifact-when-visualizing-the-membranous-labyrinth/31575

---

## Post #1 by @Ismael_Aran (2023-09-05 16:36 UTC)

<p>Hi everyone! I am working with micro-CT scans of human bony labyrinths, and I have come across these white lines inside (attached in the color picture). I’m unsure if these lines represent the membranous labyrinth, which might be visible inside of the bony labyrinth due to different tissue properties. To confirm this, I applied a density derivative using the Gradient Magnitude Recursive Gaussian Image Filter (attached in the black and white picture). This filter highlights changes in image brightness (HU). As the membrane is different from the fluid, it has a higher brightness intensity. The same occurs with the walls of the channel. Often, it is complicated to observe these variations in brightness when working with very soft and thin tissues such as the membrane. In these cases, one can use the brightness derivative in the image to try to identify if there is any type of structure that is difficult to observe. As can be seen in the image, no solid structure (black color) is visible in the central part of the channel, unlike what is seen at the edges. Therefore, I suspect that this is an artifact, probably caused by the rendering algorithm. Can someone assist me with this? I’m uncertain whether the membranous labyrinth (elastic tissue) can be observed within the bony labyrinth (bony tissue) because X-rays may not penetrate beyond the surface of the bony structure. The micro-CT that I study do not have contrast.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76a980c2703a582b6fcb39e762f39f756267a475.jpeg" data-download-href="/uploads/short-url/gVJuZMOJmZd1TDWWLVm4cwjSHyd.jpeg?dl=1" title="artifacts" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76a980c2703a582b6fcb39e762f39f756267a475.jpeg" alt="artifacts" data-base62-sha1="gVJuZMOJmZd1TDWWLVm4cwjSHyd" width="690" height="483" data-dominant-color="755A64"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">artifacts</span><span class="informations">875×613 31.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f2afda3a22cccc0dc903fa8b1c05ca552e91251.png" data-download-href="/uploads/short-url/mI41yyu5oeLAviX0M9WvZFnetlD.png?dl=1" title="derivative" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f2afda3a22cccc0dc903fa8b1c05ca552e91251.png" alt="derivative" data-base62-sha1="mI41yyu5oeLAviX0M9WvZFnetlD" width="690" height="337" data-dominant-color="CFCECF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">derivative</span><span class="informations">964×472 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-05 16:54 UTC)

<p>The bright lines in the center of the tubular structure is just how the light is reflected from the surface. If you find it confusing then you can either change the material properties to be less shiny by setting the specular reflection to 0 (in Volume Rendering module → Advanced → Volume Properties → Advanced → Material). You can also change the lighting setup by using “Lights” module of the “Sandbox” extension.</p>

---

## Post #3 by @Ismael_Aran (2023-09-05 17:56 UTC)

<p>Thank you for the fast response. As you mentioned, the central brightness in the canal was caused by specular reflection. Do you think that the Gradient Magnitude Recursive Gaussian Image Filter is suitable for detecting soft tissue structures inside?</p>
<p>I mentioned this because some authors have used normal CT scans to visualize the membranous labyrinth inside the bony labyrinth by adjusting certain algorithm parameters (Tanioka, 2020: <a href="https://www.nature.com/articles/s41598-020-66520-w" class="inline-onebox" rel="noopener nofollow ugc">Vestibular Aging Process from 3D Physiological Imaging of the Membranous Labyrinth | Scientific Reports</a>). I attempted to replicate this process using CBCT and microCT images in 3D Slicer, but I was unable to visualize the membranous labyrinth.</p>

---
