# Recommended Volume Reconstruction Configuration for best Ultrasound 3D reconstruction

**Topic ID**: 43770
**Date**: 2025-07-18
**URL**: https://discourse.slicer.org/t/recommended-volume-reconstruction-configuration-for-best-ultrasound-3d-reconstruction/43770

---

## Post #1 by @orionwiersma (2025-07-18 13:12 UTC)

<p>Hello,</p>
<p>For context I currently use Slicer for Ultrasound reconstruction of bone surfaces. This has been relatively good for outputting the shape of the bone, but the image resolution is far lower than I would like. Additionally there are a lot of gaps between segments which I would like to mesh live if possible.</p>
<p>I was wondering if there was a recommended setting/configuration that generally yields the best results for Ultrasound 3D reconstruction in Slicer. I’ve played around with most of the settings in the Volume Reconstruction module and have found it generally okay for outputting the shape of the bone, but its certainly missing finer details - that I’m able to capture later in post processing.</p>
<p>My current Slicer setup is:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/972a6e3a6529f4ad44bb5a7c47570ea1dca7b681.png" data-download-href="/uploads/short-url/lzh0jJlX5LxZU52lvxRnGfnxHlT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/972a6e3a6529f4ad44bb5a7c47570ea1dca7b681.png" alt="image" data-base62-sha1="lzh0jJlX5LxZU52lvxRnGfnxHlT" width="423" height="375" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">901×798 24.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am also using a live segmenter through the IGT link which is fairly accurate, so I don’t think the image input is causing my output to be lower quality.</p>
<p>If anyone has any recommendations for Slicer setup or additional modules to try, I would appreciate it. I am looking for a higher resolution output which minimizes the gaps in the reconstruction that I currently have.</p>

---

## Post #2 by @ungi (2025-07-20 13:44 UTC)

<p>These settings look good for live volume reconstruction. You could record the sequence while running live reconstruction. The recorded sequence can be used to run an offline reconstruction with hole filling enabled as soon as you stop recording. The output of that will have fewer gaps. You could also try to lower the output spacing during offline reconstruction, and maybe apply a bit of noise filtering on the output volume (e.g. blur with a sigma of 0.5 mm). And of course try to move the ultrasound slower, which reduces both gaps and tracking errors. Most of the artifacts originate in acoustic physics that cannot be easily eliminated. It would be best to develop a separate AI method that runs during the offline volume rendering and filters out artifacts using all tracked ultrasound frames. The live AI only uses the current frame and maybe a few preceding ones.</p>

---

## Post #3 by @max_05ge (2025-10-11 20:45 UTC)

<p>Hello,</p>
<p>Is it possible to contact you to discuss your segmenter directly via the IGT link?</p>
<p>I would also like to be able to obtain bone structure segmentation, whether live or not.</p>

---
