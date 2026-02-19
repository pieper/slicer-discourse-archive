---
topic_id: 19961
title: "Rendering At Higher Than 8 Bits Per Pixel"
date: 2021-10-01
url: https://discourse.slicer.org/t/19961
---

# Rendering at higher than 8 bits per pixel

**Topic ID**: 19961
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/rendering-at-higher-than-8-bits-per-pixel/19961

---

## Post #1 by @rprueckl (2021-10-01 21:01 UTC)

<p>After a long time and another investigation of a related issue connected with color lookup tables, I found the reason for the behavior and why for color lookup tables a scalar range different from 0 to 255 does not really produce meaningful output:</p>
<p>The reason is that the <a href="https://vtk.org/doc/nightly/html/classvtkImageMapToWindowLevelColors.html#details" rel="noopener nofollow ugc">vtkImageMapToWindowLevelColors</a> filter in <a href="https://github.com/Slicer/Slicer/blob/7a532d54df88a5ac034966e8e04d4b4b23a0362c/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx#L70" rel="noopener nofollow ugc">vtkMRMLScalarVolumeDisplayNode</a> always outputs unsigned char. This output from 0 to 255 is then mapped to the colors according to the lookup table.</p>
<p>This basically prevents using more than 256 colors for a volume. I ran into this limitation when I wanted to map fMRI images with some transparent colors in the area around 0 with a colormap containing 1024 colors. Due to the limited resolution of the pipeline, the one or two color entries in the map with 0 opacity were sometimes simply not used and everything was therefore displayed fully opaque.</p>
<p>IMHO for the future it would be great to think about using a filter with a higher resolution for the window/level calculation. This would enable a greater fidelity of displayed volumes.</p>

---

## Post #2 by @lassoan (2021-10-01 22:32 UTC)

<p>Monitors generally only support 8-bit dynamic range for each channel. To get larger dynamic range, you would need a specialty monitor, special graphics card, and rendering pipeline that supports this; or use the luminance trick (create a carefully crafted RGB lookup table and a grayscale monitor). These are all out of Slicer’s scope: either happen at lower level in VTK; or rely on a workaround that can be implemented without changing anything in the application (luminance trick). See more information about this <a href="https://discourse.vtk.org/t/10-bit-per-channel-rgb/2262">here</a>.</p>

---

## Post #3 by @Chris_Rorden (2021-10-03 11:40 UTC)

<p>It is worth noting that high dynamic range (HDR) <a href="https://support.apple.com/guide/motion/intro-to-wide-color-gamut-and-hdr-motn3f5342e9/mac" rel="noopener nofollow ugc">wide color</a> are available. My M1 MacBook Air reports <a href="https://developer.apple.com/documentation/appkit/nsimagerep/1533157-bitspersample" rel="noopener nofollow ugc">16 bits per sample</a> for the internal Retina display. According to the documentation, some Apple devices use 10-bits per components, and others that report 16 bits per sample will <a href="https://developer.apple.com/library/archive/samplecode/DeepImageDisplayWithOpenGL/Introduction/Intro.html#//apple_ref/doc/uid/TP40016622" rel="noopener nofollow ugc">dither the data</a> to 8-bits.</p>
<p>However, in general I think the human eye has a hard time distinguishing more that 256 luminance levels. For scalar volumes, I am not convinced the 8-bit limit imposes much constrain (assuming you have chosen a good window level and window center). The need for more than 256 colors are more for non-scalar data like atlases.</p>

---

## Post #4 by @rprueckl (2021-10-04 08:30 UTC)

<p>I think that color information with 8 bits per channel is definitely enough for the vast majority of cases. My question was not going into the direction of expanding this. However, we cannot exploit the 16.7 million colors but are limited to 256 for a volume to be used.<br>
Also here I think that this limitation is not problematic in general.<br>
vtkImageMapToWindowLevelColors probably was designed primarily for display purposes. However, with a configurable output range, it would probably be usable more flexibly, on the one hand for higher-resolution lookup tables for display purposes or on the other hand also for use within data processing pipelines.<br>
I also know that the filter is part of VTK and is not maintained within Slicer, so the post may have been better placed in there forum.<br>
However, I wanted to post this as a follow-up to my initial question about the relationship between</p>
<ul>
<li>the scalar range of a lookup table that can be manipulated in the Colors module of Slicer</li>
<li>the number of colors in the colormap</li>
<li>the window/level and threshold controls in the Volumes module.</li>
</ul>
<p>What I have to realize is a customizable fMRI display facility with two threshold/window/level ranges such that the volume can be transparent in the areas around 0 to be able to see the MRI that lies underneath.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/145c4314811686fdda3f60cf5253f6ca2251dce8.jpeg" data-download-href="/uploads/short-url/2U7dDiltrXhkPbd4JxgSf0fsoUE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/145c4314811686fdda3f60cf5253f6ca2251dce8_2_400x500.jpeg" alt="image" data-base62-sha1="2U7dDiltrXhkPbd4JxgSf0fsoUE" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/145c4314811686fdda3f60cf5253f6ca2251dce8_2_400x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/145c4314811686fdda3f60cf5253f6ca2251dce8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/145c4314811686fdda3f60cf5253f6ca2251dce8.jpeg 2x" data-dominant-color="5F5E61"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">495×618 46.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I didn’t want to change Slicer’s internals here, so I initially used the built-in fMRI lookup table and set the middle values (e.g. 21 and 22) to fully transparent, according to the settings in my custom UI. As the table only has 42 colors, and 0 is supposed always to be in the center, I started to generate tables according to the desired settings, with customizable tables for each of the both ranges, at first with 256 colors, then with 1024, thinking I could increase the resolution to a ‘sufficient’ level. This is where I encountered the limitation.<br>
Of course this is an improvised solution. The proper way of doing this would be having a pipeline that allows thresholding and extraction of window/level for two different ranges, and displaying them with two different lookup tables. In this case, the 256-color limitation of the filter mentioned above would again be no limitation.<br>
Another option would be to duplicate the volume and handle each of them separately, but this would be harder to maintain and is not very intuitive for the user, who loads one file.</p>

---
