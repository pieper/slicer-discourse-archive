# 3D reconstruction from 2D slices

**Topic ID**: 9784
**Date**: 2020-01-12
**URL**: https://discourse.slicer.org/t/3d-reconstruction-from-2d-slices/9784

---

## Post #1 by @Deepa (2020-01-12 17:24 UTC)

<p>I’m trying to reconstruct a 3D volume from the 2D images provided in <a href="https://www.nature.com/articles/s41598-019-49055-7" rel="nofollow noopener">this</a> study (<a href="https://springernature.figshare.com/articles/Images_of_mouse_popliteal_lymph_node_vascular_structure_derived_using_phase-contrast_synchrotron_micro-computed_tomography_CT_/8289869" rel="nofollow noopener">image source</a>).<br>
Post reconstruction, I’d like to filter only blood vessels that range from 1-10 micrometers. I hope the lat part can be done in 3D Slicer.</p>
<p>I followed the instructions given <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" rel="nofollow noopener">here</a> on “How to load data from a sequence of jpg, tif, or png files?”</p>
<p>However, I am not sure how to proceed after loading. I’ve selected the “Volume” tab. I’m not sure how to fill in the details for “Image spacing” in “Volume Information”.</p>
<p>Could someone guide me on how to proceed from here?</p>

---

## Post #2 by @muratmaga (2020-01-12 20:52 UTC)

<p>As explained in the FAQ link, image sequence formats such as tiff, png etc are not well suited for this type data, because they don’t store exactly the information you are looking for. This kind of information should be within the paper. If not contact the authors.</p>
<p>Moreover, they only provided the segmented and cropped binary images, so who knows whether the spacing is the same as original data set. So your best bet is the paper and then the authors.</p>
<p>As for the rendering you will need a fairly beefy GPU to rendering this, as it is about 6GB dataset. If you have GPU that doesn’t have enough GPU RAM, the render window comes blank (I have a laptop with a 4GB GPU so it was empty for me too). It worked fine for me, when I switched to CPU rendering option in the volume rendering module…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/302036a27132248c3a21041a19d0c005961a3d4a.png" data-download-href="/uploads/short-url/6RJW05BDMI3IgX2R4A66A30p51w.png?dl=1" title="Screenshot"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/302036a27132248c3a21041a19d0c005961a3d4a_2_690x447.png" alt="Screenshot" data-base62-sha1="6RJW05BDMI3IgX2R4A66A30p51w" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/302036a27132248c3a21041a19d0c005961a3d4a_2_690x447.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/302036a27132248c3a21041a19d0c005961a3d4a_2_1035x670.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/302036a27132248c3a21041a19d0c005961a3d4a.png 2x" data-dominant-color="464658"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1192×773 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Deepa (2020-01-13 04:49 UTC)

<p>Many thanks for your response. I too have a 4GB GPU on my laptop. Nvidia GeForce 940MX.</p>
<p>I switched to VTK CPU Ray Casting In the Volume rendering tab( I think this is selected by default). Physical memory is 8GB)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af9f9de8d067ce821d2db9af937ca0075a016865.png" data-download-href="/uploads/short-url/p3Dx9Q0X3ilhkRBx60LOc8DeIvP.png?dl=1" title="untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af9f9de8d067ce821d2db9af937ca0075a016865_2_690x306.png" alt="untitled" data-base62-sha1="p3Dx9Q0X3ilhkRBx60LOc8DeIvP" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af9f9de8d067ce821d2db9af937ca0075a016865_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af9f9de8d067ce821d2db9af937ca0075a016865_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af9f9de8d067ce821d2db9af937ca0075a016865_2_1380x612.png 2x" data-dominant-color="767681"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">untitled</span><span class="informations">1887×837 66.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I navigated to “Volumes” option and I have the following settings. Active volume is selected automatically. For now, I am using the default Image Spacing. I will write to the authors and find out the actual spacing. In the paper it is mentioned, “To prepare the image stack for<br>
importation to Imaris, the image stack file was converted to 8-bit, noise was filtered out using a (3×3×3) median filter, and the pipette image and other artefacts were subtracted out”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/138e1785e799aa79253dbc1b8f8f381f6f3c96d5.png" data-download-href="/uploads/short-url/2MZv9exZCKAqoFhl2zv9k1ZZOEl.png?dl=1" title="untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/138e1785e799aa79253dbc1b8f8f381f6f3c96d5_2_690x388.png" alt="untitled" data-base62-sha1="2MZv9exZCKAqoFhl2zv9k1ZZOEl" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/138e1785e799aa79253dbc1b8f8f381f6f3c96d5_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/138e1785e799aa79253dbc1b8f8f381f6f3c96d5_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/138e1785e799aa79253dbc1b8f8f381f6f3c96d5_2_1380x776.png 2x" data-dominant-color="7A7A82"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">untitled</span><span class="informations">1920×1080 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Could you please suggest how to proceed from here?</p>

---

## Post #4 by @muratmaga (2020-01-13 15:47 UTC)

<p>Your screenshots does not show 3D rendering. When you set the method to CPU Raycasting, did you also click on the little eye icon that enables the 3D rendering in the Volume Rendering module?</p>
<p>I can’t think of a effect in the segment editor that will let you choose to retain only a vessels of certain diameter and less. Perhaps VMTK extension does it. Also there might be other methods (using python) to achieve what you want to do…</p>

---

## Post #5 by @lassoan (2020-01-13 17:14 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="9784">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I can’t think of a effect in the segment editor that will let you choose to retain only a vessels of certain diameter and less. Perhaps VMTK extension does it.</p>
</blockquote>
</aside>
<p>Yes, VMTK centerline computaiton module provides diameter values for the extracted vessel tree, which can be used for selectively truncating the model. However, the image above is such a comlex and irregular vascular “tree” that usual method might fail.</p>
<p>If the goal is to just extract vessels of a diameter range then it is very easy to do. If you have a segment that only contains vessels then you can use the Margin effect to shrink diameter of all vessels (this will make all vessels that have smaller diameters than the erosion disappear completely) then use the same effect to grow them back to the original diameter. This results in vessel tree that contains vessels that have diameters over the margin size (or twice the margin size - you need to check the details). To remove large-diameter vessels, you first find them using the same method, then use Logical operators effect to remove them from the image.</p>

---

## Post #6 by @Deepa (2020-01-14 09:20 UTC)

<p>Thanks a lot for the response. I clicked on the little eye icon and I could see the boxes in red, green and yellow windows.</p>
<p>However, I’m not sure how to generate the 3D volumes after this. I selected the "Vector to Scalar Volume " tab. The following is displayed. But I don’t see the “Apply” highlighted. I’m not able to select anything in “Input Vector Volume”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c2a549f46d8f1efc6ce7e7f1e7ab60026a4358a.png" data-download-href="/uploads/short-url/aRMYNeHaHidnaGN6MIbngpEDqPw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c2a549f46d8f1efc6ce7e7f1e7ab60026a4358a_2_690x388.png" alt="image" data-base62-sha1="aRMYNeHaHidnaGN6MIbngpEDqPw" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c2a549f46d8f1efc6ce7e7f1e7ab60026a4358a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c2a549f46d8f1efc6ce7e7f1e7ab60026a4358a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c2a549f46d8f1efc6ce7e7f1e7ab60026a4358a_2_1380x776.png 2x" data-dominant-color="65656D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks a lot. I’ll have a look at VMTK</p>

---

## Post #7 by @muratmaga (2020-01-14 16:42 UTC)

<p>Your image stack was in tiff format. Slicer imports that as a normal scalar volume, you do not need/have a vector volume hence the field is empty. The reason you are not seeing a 3D rendering when you do a volume rendering, is because the volume exceeds the capability of your GPU. Try switching to CPU raycasting (will be slow) or crop and/or downsample your volume using CropVolume module.</p>

---

## Post #8 by @muratmaga (2020-01-14 22:02 UTC)

<p>You might be also forgetting to turn on the little eye icon next to the volume name in the volume rendering module (it is turned off in the screen capture you provided for the cpu rendering issue).</p>

---

## Post #9 by @lassoan (2020-01-14 22:12 UTC)

<p>You can also try enabling/disabling depth peeling in the 3D view controller:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ebe57f0c07c7e75a26ec27c75cf9e7c867b3f73.png" data-download-href="/uploads/short-url/mEjfsPAJtrrHYcL9fegSiIMtE79.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ebe57f0c07c7e75a26ec27c75cf9e7c867b3f73_2_690x411.png" alt="image" data-base62-sha1="mEjfsPAJtrrHYcL9fegSiIMtE79" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ebe57f0c07c7e75a26ec27c75cf9e7c867b3f73_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ebe57f0c07c7e75a26ec27c75cf9e7c867b3f73.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ebe57f0c07c7e75a26ec27c75cf9e7c867b3f73.png 2x" data-dominant-color="B6BAD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">809×483 39 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Deepa (2020-05-15 01:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="9784">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the goal is to just extract vessels of a diameter range then it is very easy to do. If you have a segment that only contains vessels then you can use the Margin effect to shrink diameter of all vessels (this will make all vessels that have smaller diameters than the erosion disappear completely) then use the same effect to grow them back to the original diameter. This results in vessel tree that contains vessels that have diameters over the margin size (or twice the margin size - you need to check the details). To remove large-diameter vessels, you first find them using the same method, then use Logical operators effect to remove them from the image.</p>
</blockquote>
</aside>
<p>Could you please explain if it is possible to do the above using VMTK’s/ 3D Slicer’s  python interface?</p>

---

## Post #11 by @lassoan (2020-05-15 03:17 UTC)

<p>You don’t need VMTK for filtering vessels by their diameter (just use Segment Editor module as described above).</p>
<p>If your vessels are not segmented yet then it is a more complicated problem and the solution depends on what kind of images you have, what vessels you need to segment, and for what purpose. If you need help with this then please create a new topic for it and give details and preferably example images (at least screenshots).</p>

---
