---
topic_id: 37218
title: "Crippling Lag During Segmentation On A Strong Computer"
date: 2024-07-05
url: https://discourse.slicer.org/t/37218
---

# CRIPPLING LAG during segmentation on a strong computer

**Topic ID**: 37218
**Date**: 2024-07-05
**URL**: https://discourse.slicer.org/t/crippling-lag-during-segmentation-on-a-strong-computer/37218

---

## Post #1 by @hari_seldon (2024-07-05 16:15 UTC)

<p>Hello, getting desperate here. I am in the Segment Editor removing voxels from 256x256x256 cubes in the 3D viewport. I engage the eraser tool and select “sphere brush” and “edit in 3D views”, and then when I go into the 3D view to erase voxels it is impossible due to lag.</p>
<p>Napari trivially erases in 3D with zero lag, so there must be some unnecessary computation in Slicer. Does anyone know what is happening here and how to mitigate it, and can explain exactly how to do so?</p>
<p>Thank you so much!!! I really appreciate it.</p>

---

## Post #2 by @pieper (2024-07-05 16:24 UTC)

<p>Rebuilding the surface model will always take some time, but try turning off smoothing and switching to surface nets, at least while editing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f7438c63947d27d0143b6864240b72b13fcd9c9.png" data-download-href="/uploads/short-url/kt3hv4KPB5sP2KBkWHPdW8fnCoF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f7438c63947d27d0143b6864240b72b13fcd9c9_2_690x215.png" alt="image" data-base62-sha1="kt3hv4KPB5sP2KBkWHPdW8fnCoF" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f7438c63947d27d0143b6864240b72b13fcd9c9_2_690x215.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f7438c63947d27d0143b6864240b72b13fcd9c9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f7438c63947d27d0143b6864240b72b13fcd9c9.png 2x" data-dominant-color="C1C4D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">761×238 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @hari_seldon (2024-07-05 16:38 UTC)

<p>Thanks for the response, this has very little effect. There must be constant re-computation of every voxel in the space for the amount of lag there is. We went through this with some in-house software a while back and it took a fair bit of effort to solve.</p>
<p>There’s also some issues where Slicer is performing computations single-threaded - if I use the scissor tool past a certain zoom level, I’ll sit there for 3 minutes while it tries to figure out which 30 voxels to erase. So there’s two issues there, Slicer isn’t performing actions multi-threaded, and something is going wrong past a certain zoom threshold.</p>
<p>Is there a paid dev team for Slicer that has a list of things they work on, with a public facing bug list kind of thing?</p>

---

## Post #4 by @pieper (2024-07-05 16:40 UTC)

<p>Everything is very open, and you can look at <a href="http://slicer.org">slicer.org</a> for the resources like github issues etc including people you can hire to work on special projects.  If you can fund projects to improve the software that would be much appreciated.</p>

---

## Post #5 by @lassoan (2024-07-07 15:53 UTC)

<p>Most likely the fix is really easy we just need to figure out what is exactly slow.</p>
<p>Surface nets still uses Taubin smoothing by default, so you need to enable surface net smoothing (or disable smoothing) for much faster updates.</p>
<p>You can also improve surface generation speed by reducing the number of triangles by using smoothing effect before enabling “Show 3D”.</p>
<p>You can also avoid costly recomputation of a conplex mesh by editing segments independently by enabling “allow overlap” and editing smaller, simpler segments.</p>
<p>There are many more potential approaches and parameters to adjust, but I would rather learn a bit more about what your application is to avoid shooting in the dark. Could you post a few screenshots and describe the overall goal of your project and what segmentation task you would like to do?</p>

---

## Post #6 by @hari_seldon (2024-07-07 21:17 UTC)

<p>Oh great yes thanks. CTscan data off a particle accelerator. I am trying to pull instances of ancient papyrus sheets out of an initial semantic mask for the Vesuvius Challenge. Cubes are 256x256x256 voxels (says mm in Slicer but the conversion appears to be naive). I use the scissor tool and eraser tool in 3D, and then I use the eraser, island, and brush tools in 2D. The eraser tool is laggy in 2D, and wildly laggy in 3D. Eraser tool always is sphere. The base matte green in the images is the semantic mask.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dba2dc3985b3cfb507ac50f8e140c816909d1c96.jpeg" data-download-href="/uploads/short-url/vkZuxd3zQCw79HxjstBd6D2DUI6.jpeg?dl=1" title="Screenshot from 2024-07-02 01-01-37" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2dc3985b3cfb507ac50f8e140c816909d1c96_2_673x500.jpeg" alt="Screenshot from 2024-07-02 01-01-37" data-base62-sha1="vkZuxd3zQCw79HxjstBd6D2DUI6" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2dc3985b3cfb507ac50f8e140c816909d1c96_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2dc3985b3cfb507ac50f8e140c816909d1c96_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dba2dc3985b3cfb507ac50f8e140c816909d1c96_2_1346x1000.jpeg 2x" data-dominant-color="8F9197"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-07-02 01-01-37</span><span class="informations">1920×1426 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15f83c79b0266f71fa6e26d9d8c78c01882afdf0.png" data-download-href="/uploads/short-url/38lRYpdmycmxiQd2lxqfbIqqsAU.png?dl=1" title="Screenshot from 2024-06-26 16-26-40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15f83c79b0266f71fa6e26d9d8c78c01882afdf0_2_530x500.png" alt="Screenshot from 2024-06-26 16-26-40" data-base62-sha1="38lRYpdmycmxiQd2lxqfbIqqsAU" width="530" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15f83c79b0266f71fa6e26d9d8c78c01882afdf0_2_530x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15f83c79b0266f71fa6e26d9d8c78c01882afdf0_2_795x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15f83c79b0266f71fa6e26d9d8c78c01882afdf0.png 2x" data-dominant-color="848CAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-06-26 16-26-40</span><span class="informations">850×801 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43220af28e4e5fbd2ca20bb87cd67cccd9b262a.jpeg" data-download-href="/uploads/short-url/uhaCy7gYDI2Tsq1RKHSq98nxQE2.jpeg?dl=1" title="Screenshot from 2024-06-30 21-11-38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d43220af28e4e5fbd2ca20bb87cd67cccd9b262a_2_543x499.jpeg" alt="Screenshot from 2024-06-30 21-11-38" data-base62-sha1="uhaCy7gYDI2Tsq1RKHSq98nxQE2" width="543" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d43220af28e4e5fbd2ca20bb87cd67cccd9b262a_2_543x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d43220af28e4e5fbd2ca20bb87cd67cccd9b262a_2_814x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d43220af28e4e5fbd2ca20bb87cd67cccd9b262a_2_1086x998.jpeg 2x" data-dominant-color="7C777E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-06-30 21-11-38</span><span class="informations">1830×1685 287 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2f78723e8e1f1c01a77ebf0113b8c9bb02b9737.jpeg" data-download-href="/uploads/short-url/pxdjzWt01AVSaBE3CXPuJBkWEzd.jpeg?dl=1" title="Screenshot from 2024-06-29 00-06-40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f78723e8e1f1c01a77ebf0113b8c9bb02b9737_2_688x500.jpeg" alt="Screenshot from 2024-06-29 00-06-40" data-base62-sha1="pxdjzWt01AVSaBE3CXPuJBkWEzd" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f78723e8e1f1c01a77ebf0113b8c9bb02b9737_2_688x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f78723e8e1f1c01a77ebf0113b8c9bb02b9737_2_1032x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f78723e8e1f1c01a77ebf0113b8c9bb02b9737_2_1376x1000.jpeg 2x" data-dominant-color="707484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-06-29 00-06-40</span><span class="informations">1920×1395 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/730cd8d81d92380c37e7ed0a83ba2102eeacab0d.jpeg" data-download-href="/uploads/short-url/gpMqTqyZfokbUbe8Wwk839TzGmp.jpeg?dl=1" title="Screenshot from 2024-07-02 18-19-15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/730cd8d81d92380c37e7ed0a83ba2102eeacab0d_2_540x500.jpeg" alt="Screenshot from 2024-07-02 18-19-15" data-base62-sha1="gpMqTqyZfokbUbe8Wwk839TzGmp" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/730cd8d81d92380c37e7ed0a83ba2102eeacab0d_2_540x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/730cd8d81d92380c37e7ed0a83ba2102eeacab0d_2_810x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/730cd8d81d92380c37e7ed0a83ba2102eeacab0d_2_1080x1000.jpeg 2x" data-dominant-color="7A7F81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-07-02 18-19-15</span><span class="informations">1816×1679 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pieper (2024-07-07 21:27 UTC)

<p><a class="mention" href="/u/hari_seldon">@hari_seldon</a> you should offer to share whatever prize money you win to help fund Slicer development <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @lassoan (2024-07-07 22:33 UTC)

<p>Slow update after 2D editing means 3D surface generation takes time. Surface nets and surface nets smoothing should mostly address this, but there are additional options to make things even faster.</p>
<p>Note that you can use Slicer (for example, Fiducial registration wizard module in SlicerIGT extension or Baffle planner module in SlicerHeart extension with a few small modifications) to flatten the pages, thwn you can extract the page using Crop volume module, and then finally display the text (if the ink has different density than the paper) using Volume rendering module. You don’t need to spend time with erasing small pieces or filter out noise because Slicer can straighten the entire thick slab around each page and volume rendering can display a readable image even at the presence of lots of noise.</p>

---

## Post #9 by @hari_seldon (2024-07-08 01:47 UTC)

<p>Surface nets + surface net smoothing makes things a little bit less laggy, but it is still far too laggy to use. What else can I do?</p>
<p>As for the rest here, it unfortunately does not apply. All the pages in the green semantic mask are connected, and the purpose of this process is to disconnect them into individual coloured instances, and then take these instances and attempt to train neural networks to automate the creation of instances.</p>
<p>Then eventually (if that ever works) geometry processing techniques are used to grab a mesh off one surface and then neural networks are used to display ink that is invisible to the naked eye (carbon ink on carbonized papyrus).</p>

---

## Post #10 by @cpinter (2024-07-08 11:37 UTC)

<p>In the case of such complex surfaces the conversion from labelmap to closed surface can be really slow. In our field we usually don’t have such complexity (lots of layers, branches, holes), but for example if you simply threshold an image (e.g. any sample data), it is similarly complex, and indeed, surface conversion is quite slow until you further process it.</p>
<p>If the suggestions above don’t help, not even disabling smoothing altogether, then the only thing you can do is do the editing in 2D without seeing the 3D and only turn it on when you need it.</p>
<p>If you always need 3D, maybe partition the image and work on a few segments at a time.</p>
<p>The suggestions of <a class="mention" href="/u/lassoan">@lassoan</a> are great, but if you only have to segment to train a network then maybe not applicable. Please take a second look at them though.</p>

---

## Post #11 by @mau_igna_06 (2024-07-08 18:04 UTC)

<p>What about setting up a custom volume rendering shader (e.g. “labelmap masking”) in the 3D views context manager to crop on 3D with scissors effect. I think that may work without needing to recreate the 3D mesh with each cut. Core devs may clarify if this approach is possible.</p>

---

## Post #12 by @pieper (2024-07-08 18:15 UTC)

<p>Yes, if one is open to doing custom programming then there are a lot of possible optimizations.  A shader is one possibility, but it may also be possible to facilitate this particular task with masking and volume rendering.</p>

---

## Post #13 by @hari_seldon (2024-07-09 06:43 UTC)

<p>I’ll see if these functions have a use case for people, they sound quite interesting and powerful. What we are working with right now is a piece of geometry processing code which takes a volumetric  instance from slicer and gives back a mesh of the inner-facing papyrus surface, rendered and textured with the original CTscan data, and flattened for ink detection algorithms.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7d86201cfe7ca9a2fce2afedd5dc64bf77d13fa.png" alt="Screenshot from 2024-07-07 09-18-24" data-base62-sha1="x4ZTpEzCIO4Lo3qJqHKe9Iau1TQ" width="254" height="495"></p>

---

## Post #14 by @hari_seldon (2024-07-09 06:48 UTC)

<p>Yes the advice so far has removed a significant amount of lag from the 2D view, which is glorious!! It really adds up as the hours go by.</p>

---

## Post #15 by @hari_seldon (2024-07-09 06:55 UTC)

<p>I’ll explore and see if anyone can write code for Slicer. Coding for Napari has happened quite a bit due to the ease of python scripting, but I think people might be having a harder time with Slicer.</p>
<p>Quick question - is there a way to hide all the segments simultaneously in the segment editor, instead of clicking on 20 eyeballs in the sidebar? We would like to hide and show the masks a dozen times per minute.</p>

---

## Post #16 by @pieper (2024-07-09 12:11 UTC)

<aside class="quote no-group" data-username="hari_seldon" data-post="15" data-topic="37218">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/c6cbf5/48.png" class="avatar"> hari_seldon:</div>
<blockquote>
<p>is there a way to hide all the segments simultaneously</p>
</blockquote>
</aside>
<p>You can multi-select (shift-click) and right click Toggle Visibility in the Data module.</p>

---

## Post #17 by @hari_seldon (2024-07-09 16:32 UTC)

<p>Ok thanks. So I would have to program a hotkey to “hide all segments” and “show all segments”. Is that sort of thing possible to program in Slicer?</p>

---

## Post #18 by @pieper (2024-07-09 17:45 UTC)

<p>Yes, the full application is scriptable.  E.g. see: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures</a></p>

---

## Post #19 by @lassoan (2024-07-09 18:50 UTC)

<aside class="quote no-group" data-username="hari_seldon" data-post="13" data-topic="37218">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/c6cbf5/48.png" class="avatar"> hari_seldon:</div>
<blockquote>
<p>What we are working with right now is a piece of geometry processing code which takes a volumetric instance from slicer and gives back a mesh of the inner-facing papyrus surface, rendered and textured with the original CTscan data, and flattened for ink detection algorithms</p>
</blockquote>
</aside>
<p>If you extract a thin surface from the volume (for example, using <code>Probe model with volume</code> module) then your signal to noise ratio will hugely decrease, because only a small fraction of voxels are sampled and if the surface extraction method has any imperfections then you might not even work with the most informative voxels. Instead, you can extract a thick slice around the papyrus sheet (unwrap the volume not a surface) thereby preserving all information that the image contains. You then may not even need much post-processing, because with the right transfer functions volume rendering may clearly show the ink.</p>
<p>3D Slicer is fully python scriptable, and most of newly added modules are implemented in Python. You can also pip install any Python package and use it in your Slicer modules. It should be easier to get started with Slicer than with napari, as you get a fully configured Python environment and GUI application in one, including Python console, slice and 3D views, and rich GUI. I would recommend napari if you work with 2D or 2.5D microscopy images, but for 3D images Slicer offers much more.</p>

---
