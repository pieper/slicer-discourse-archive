# Cartilage Thickness

**Topic ID**: 38160
**Date**: 2024-09-02
**URL**: https://discourse.slicer.org/t/cartilage-thickness/38160

---

## Post #1 by @Kowsar_Sheikhi (2024-09-02 15:38 UTC)

<p>Hi,</p>
<p>I need help with the thickness option in 3D Slicer. I followed all the steps to visualize the cartilage thickness, but it isn’t showing the thickness correctly. I suspect the mapping direction for the thickness might be incorrect.</p>
<p>Any sugestion? Thank you for your help.<br>
3dslicer 5.6.2</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bf3eb63b26b17bee47859c85137d3d41cd94446.jpeg" data-download-href="/uploads/short-url/mfCBnZMbXaYqrt6xwlay27i9yu2.jpeg?dl=1" title="thickness.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf3eb63b26b17bee47859c85137d3d41cd94446_2_690x336.jpeg" alt="thickness.PNG" data-base62-sha1="mfCBnZMbXaYqrt6xwlay27i9yu2" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf3eb63b26b17bee47859c85137d3d41cd94446_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf3eb63b26b17bee47859c85137d3d41cd94446_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bf3eb63b26b17bee47859c85137d3d41cd94446_2_1380x672.jpeg 2x" data-dominant-color="B3BDC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thickness.PNG</span><span class="informations">1915×934 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-09-02 15:39 UTC)

<p>Make sure to choose the thickness as “active scalar” in “Scalars” section.</p>

---

## Post #3 by @Kowsar_Sheikhi (2024-09-02 16:10 UTC)

<p>In the Active Scalars section, there are options for Normals, Absolute, Point to Point Vector, Point to Point Along X, Point to Point Along Y, Point to Point Along Z, and Original. There is no thickness option to choose.</p>
<p>I have tried all of these options, and the only one that shows the colormap is Normals (that it is not the correct thickness colormap). The others only display one color.</p>
<p>What should I do?</p>

---

## Post #4 by @lassoan (2024-09-02 16:13 UTC)

<p>“Absolute” should work (I assume that’s absolute distance between the medial surface and the original surface). If you set <code>Scalar Range Mode</code> to <code>Data scalar range (auto)</code>, what is the <code>Displayed range</code>?</p>

---

## Post #5 by @Kowsar_Sheikhi (2024-09-02 16:18 UTC)

<p>No, unfortunately, Absolute is not working.</p>
<p>The displayed range for Normals is -0.99 to 0.99, with the data scalar range set to auto.</p>

---

## Post #6 by @lassoan (2024-09-02 16:19 UTC)

<p>What range is displayed when you choose <code>Absolute</code>?</p>

---

## Post #7 by @Kowsar_Sheikhi (2024-09-02 16:20 UTC)

<p>for Absolute: 0 to 4.15</p>

---

## Post #8 by @lassoan (2024-09-02 16:23 UTC)

<p>That’s great, that indicates that everything works well. The 4.15mm maximum may be in a very small area, so you may see mostly uniform color over the entire surface. You probably want to switch to manual scalar range mode and set a smaller maximum value, like 1mm.</p>

---

## Post #9 by @Kowsar_Sheikhi (2024-09-02 16:28 UTC)

<p>Thank you so much but what should I do to see the thickness? it is still uniform<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/088e2678e5ab319b64ea19f64cf45f6c9829f18e.png" data-download-href="/uploads/short-url/1dGngNIOKrUVckN19oZxqhwOPPo.png?dl=1" title="Absolute" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088e2678e5ab319b64ea19f64cf45f6c9829f18e_2_690x401.png" alt="Absolute" data-base62-sha1="1dGngNIOKrUVckN19oZxqhwOPPo" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088e2678e5ab319b64ea19f64cf45f6c9829f18e_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088e2678e5ab319b64ea19f64cf45f6c9829f18e_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088e2678e5ab319b64ea19f64cf45f6c9829f18e_2_1380x802.png 2x" data-dominant-color="BACEC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Absolute</span><span class="informations">1918×1117 486 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2024-09-02 17:34 UTC)

<p>Minimum should be 0, maximum should be a small number. If 1.0 still appears as uniform then you can decrease it further.</p>

---

## Post #11 by @jay1987 (2024-09-03 01:30 UTC)

<p>why my Active Scalar Options only has Normals Option?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7aedc1c20889d9bbad17159525e0d9428ca04214.jpeg" data-download-href="/uploads/short-url/hxtDScAMUbAYIYmctQfTy7J2A6M.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aedc1c20889d9bbad17159525e0d9428ca04214_2_690x230.jpeg" alt="image" data-base62-sha1="hxtDScAMUbAYIYmctQfTy7J2A6M" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aedc1c20889d9bbad17159525e0d9428ca04214_2_690x230.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aedc1c20889d9bbad17159525e0d9428ca04214_2_1035x345.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7aedc1c20889d9bbad17159525e0d9428ca04214_2_1380x460.jpeg 2x" data-dominant-color="BEA5B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×641 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @Kowsar_Sheikhi (2024-09-03 12:36 UTC)

<p>Do you mean in Absolute? When I set Min to 0, the 3D model disappears. I have changed the Min and Max values multiple times, but it is still uniform…<br>
It is a bit strange, what ´s your idea? Where is the problem?</p>

---

## Post #13 by @lassoan (2024-09-03 12:45 UTC)

<p>Could you save the scene (that contains the original model, the medial surface, and the surface distance computation result) as .mrb file, upload it somewhere (dropbox, onedrive, …) and post the link here?</p>

---

## Post #15 by @lassoan (2024-09-04 06:17 UTC)

<p>It seems that you have not computed the medial surface. Without that, surface-to-surface distance would not be able to get the thickness (thickness = distance of the surface from the medial surface).</p>
<p>You can compute the Voronoi diagram using Extract Centerline module of VMTK extension, which is a good approximation of the medial surface. The module even computes the “radius” (half thickness) for each point of the medial surface.</p>
<p>Set the input Surface and pick any two points as endpoints (they are not used if you don’t specify any outputs in the “Outputs” section; the easiest is to click on Auto-detect). In the “Advanced” section, create an output for the Voronoi diagram. You probably want to increase the <code>Target point count</code> from the default 5k to 10k-30k.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/081c843077c4bf92bb700da25a45120e910702a6.jpeg" data-download-href="/uploads/short-url/19KUMj5tq4uOCfZRUcF4qbw6caq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/081c843077c4bf92bb700da25a45120e910702a6_2_690x362.jpeg" alt="image" data-base62-sha1="19KUMj5tq4uOCfZRUcF4qbw6caq" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/081c843077c4bf92bb700da25a45120e910702a6_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/081c843077c4bf92bb700da25a45120e910702a6_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/081c843077c4bf92bb700da25a45120e910702a6_2_1380x724.jpeg 2x" data-dominant-color="3F3F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1009 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can then visualize the thickness by choosing coloring by “radius”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a53870495a90ad0f5931e865892f1d29009de80.jpeg" data-download-href="/uploads/short-url/3KTmZHwdDDQbzZMhBffg9sy9VoQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a53870495a90ad0f5931e865892f1d29009de80_2_690x361.jpeg" alt="image" data-base62-sha1="3KTmZHwdDDQbzZMhBffg9sy9VoQ" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a53870495a90ad0f5931e865892f1d29009de80_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a53870495a90ad0f5931e865892f1d29009de80_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a53870495a90ad0f5931e865892f1d29009de80_2_1380x722.jpeg 2x" data-dominant-color="474A4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1007 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you need to visualize the cartilage thickness on the original “cartilage” input mesh then you can use the “Model To Model Distance” module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f38ab2e29c26f1f7a4e121412c53bb1c860e2388.jpeg" data-download-href="/uploads/short-url/yKtbxefW87j8Sdz8JFGXi5AnTQI.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f38ab2e29c26f1f7a4e121412c53bb1c860e2388_2_690x362.jpeg" alt="image" data-base62-sha1="yKtbxefW87j8Sdz8JFGXi5AnTQI" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f38ab2e29c26f1f7a4e121412c53bb1c860e2388_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f38ab2e29c26f1f7a4e121412c53bb1c860e2388_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f38ab2e29c26f1f7a4e121412c53bb1c860e2388_2_1380x724.jpeg 2x" data-dominant-color="49494B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1008 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The small red patches are due to the spikes in the medial surface (Voronoi diagram). You can reduce this noise using “Surface toolbox” module, “Uniform remesh” tool (you can reduce number of points to about 5k for strong smoothing) applied to the computed Voronoi diagram. Resampling removes the “radius” scalar, so you need to use “Model to model distance” module to get thickness values.</p>

---

## Post #16 by @Kowsar_Sheikhi (2024-09-04 10:50 UTC)

<p>Thank you so much for your help!! Now I can see the thickness in my model! <img src="https://emoji.discourse-cdn.com/twitter/star_struck.png?v=12" title=":star_struck:" class="emoji" alt=":star_struck:" loading="lazy" width="20" height="20"></p>

---
