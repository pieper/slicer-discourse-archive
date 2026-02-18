# Slicer rhomboid voxels in 3D-View

**Topic ID**: 24361
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/slicer-rhomboid-voxels-in-3d-view/24361

---

## Post #1 by @chris_nik (2022-07-18 09:38 UTC)

<p>Hello,<br>
First of all, thank you again for creating Slicer, it really helps my research a lot.</p>
<p>I have the following problem/ question. I am trying to import a 3D-Skeleton.tif (created in ImageJ, width of the skeleton structure is 1 voxel) in Slicer and export an STL model.<br>
I execute the following steps: 1. Import the .tif file in Slicer as LabelMap 2. “Convert LabelMap to Segmentation Node” 3. Open “Segment Editor” Module 4. “Show 3D” with “Surface Smoothing” turned off → the result can be seen in Screenshot 1.</p>
<p>My question is, why do the voxels of the Skeleton get displayed by Slicer as rhomboids or rotated cubes with reduced size? This causes the structure to look like there are holes in it. If you look at Screenshot 1, next to Slicer’s visualisation I have uploaded the ImageJ 3D visualisation. ImageJ displays the voxels as unrotated cubes and where the structure goes in an oblique direction, the adjacent voxels touch each other at their edges. Slicer’s visualisation at those areas leaves empty space beetween adjacent voxels. Can this be changed in Slicer’s settings?</p>
<p>N.B in Screenshot 2 there is Slicer’s visualisation in a sagittal slice. The voxels are unrotated cubes, like ImageJ displays them in its 3D-View, the edges touching when the structure is oblique.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2681fd431fa6e30432450594b025a7f4363c078.png" data-download-href="/uploads/short-url/psg4EEpmV8rWHmfESxTqO5fEjeU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2681fd431fa6e30432450594b025a7f4363c078_2_653x500.png" alt="image" data-base62-sha1="psg4EEpmV8rWHmfESxTqO5fEjeU" width="653" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2681fd431fa6e30432450594b025a7f4363c078_2_653x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2681fd431fa6e30432450594b025a7f4363c078_2_979x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b2681fd431fa6e30432450594b025a7f4363c078_2_1306x1000.png 2x" data-dominant-color="6F7194"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1762×1349 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Screenshot 1: On the left ImageJ 3D-View; on the right Slicer 3D-View of the same .tif</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c7e7bfe152378c26ae9a65f5e20c2eb7b3ac0c.png" data-download-href="/uploads/short-url/kWu0m7vv33HnqgjGUSk5oe8mSUk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c7e7bfe152378c26ae9a65f5e20c2eb7b3ac0c_2_690x475.png" alt="image" data-base62-sha1="kWu0m7vv33HnqgjGUSk5oe8mSUk" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c7e7bfe152378c26ae9a65f5e20c2eb7b3ac0c_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c7e7bfe152378c26ae9a65f5e20c2eb7b3ac0c_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c7e7bfe152378c26ae9a65f5e20c2eb7b3ac0c_2_1380x950.png 2x" data-dominant-color="050403"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1541×1062 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Screenshot 2: Slicer Sagittal View of the same .tif</p>

---

## Post #2 by @mau_igna_06 (2022-07-18 17:00 UTC)

<p>I guess you are forgeting a transform that defines image orientation/position and also to set up correctly the spacing of the image.</p>
<p>Hope it helps</p>

---

## Post #3 by @pieper (2022-07-18 19:12 UTC)

<p>Try turning off surface smoothing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5b99f0126632eb281e6295697105a466d79b4f.png" data-download-href="/uploads/short-url/mATH6yculO70LpCVea78NXZSuR1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5b99f0126632eb281e6295697105a466d79b4f_2_690x324.png" alt="image" data-base62-sha1="mATH6yculO70LpCVea78NXZSuR1" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5b99f0126632eb281e6295697105a466d79b4f_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5b99f0126632eb281e6295697105a466d79b4f_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5b99f0126632eb281e6295697105a466d79b4f.png 2x" data-dominant-color="424A51"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1094×514 68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @chris_nik (2022-07-19 14:37 UTC)

<p>Thank you, I’ll try a transform and adjusting the spacing.</p>

---

## Post #5 by @chris_nik (2022-07-19 14:39 UTC)

<p>Thank you for the idea, Surface smoothing for Show 3D was turned off before I took the screenshots (it was unticked like in your screenshot, I also mentioned that in my post). In fact when there is any Surface smoothing on the 3D Image, it dissapears <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"> (I guess because it is only 1 Voxel wide).</p>

---

## Post #6 by @chris_nik (2022-07-19 16:23 UTC)

<p>Update: I opened my .tif file in ImageJ and saved it as an .nrrd file. Then I imported it in Slicer as a Volume and went “Volume Rendering” → Display Volume (ticked the eye-icon next to the volume). This way I get the result I expect (s. Screenshot 3), however now I can’t export it to STL.<br>
When I try to create a Segmentation from that in order to save it as STL, I get the same result as in Screenshot 1 with the rhomboid voxels.</p>
<p>N.B Interestingly, going out from the wanted Representation of the Volume in Screenshot 3, when I increase the “Shift” Parameter under “Display” in “Volume Rendering” (s. Screenshot 4), I get similar rhomboid voxels as in the Segmentation 3D-View. Is there a way to adjust the same “Shift” Parameter of the Segmentation? (I couldn’t find it)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e458bed31c710eb0f434f3018a4779f7eaa0aef.png" data-download-href="/uploads/short-url/22fGCBUTZKTPoGLXr2RioXJvdGn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e458bed31c710eb0f434f3018a4779f7eaa0aef_2_690x263.png" alt="image" data-base62-sha1="22fGCBUTZKTPoGLXr2RioXJvdGn" width="690" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e458bed31c710eb0f434f3018a4779f7eaa0aef_2_690x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e458bed31c710eb0f434f3018a4779f7eaa0aef_2_1035x394.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e458bed31c710eb0f434f3018a4779f7eaa0aef_2_1380x526.png 2x" data-dominant-color="6E6F8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×976 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Screenshot 3: Skeletonisation in .nrrd format imported as Volume</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a86ae0aab71d7e8d25f73b9379a2af66a6e70ea7.png" data-download-href="/uploads/short-url/o1TclUlPeTS73bqBfvWWHG3nSsf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86ae0aab71d7e8d25f73b9379a2af66a6e70ea7_2_690x262.png" alt="image" data-base62-sha1="o1TclUlPeTS73bqBfvWWHG3nSsf" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86ae0aab71d7e8d25f73b9379a2af66a6e70ea7_2_690x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86ae0aab71d7e8d25f73b9379a2af66a6e70ea7_2_1035x393.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a86ae0aab71d7e8d25f73b9379a2af66a6e70ea7_2_1380x524.png 2x" data-dominant-color="6E6F8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×974 92.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Screenshot 4: Increase of the “Shift” Parameter under “Display” in “Volume Rendering” gives rhomboid voxels</p>

---

## Post #7 by @lassoan (2022-07-19 23:46 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">load the nrrd file as segmentation</a>, disable smoothing (as <a class="mention" href="/u/pieper">@pieper</a> described above), and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file">export the segmentation as STL</a>.</p>
<p>However, I would recommend to use <a href="https://github.com/vmtk/SlicerExtension-VMTK/#the-vmtk-extension-for-3d-slicer">VMTK extension</a> for extraction and analysis of vessel centerlines. It will simplify your workflow and provide better results. You can probably even do all your analysis within Slicer - basic quantifications are already available via GUI and you can run any additional custom analysis using Python scripting.</p>

---

## Post #8 by @chris_nik (2022-07-20 09:56 UTC)

<p>Thank you Andras,</p>
<p>What I am trying to visualise is a skeleton of a segmentation of a suture, so it is not a blood vessel, the VMTK extension would have been very useful otherwise.</p>
<p>Unfortunately the problem I experience (the skeleton being displayed with rhomboid voxels and holes when loaded as segmentation, s. Screenshot 1 from my first post) still persists when I use the method you describe (s. Screenshot 5 below). I had disabled Surface smoothing for Screenshot 1 as well.</p>
<p>However I am starting to think that a surface can’t be displayed otherwise (s. Screenshot 6 from ImageJ when you create a 3D Surface of the same Skeleton → it still has rhomboid voxels and slight holes between adjacent voxels)?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afddef8b1b2a331b48d1ed1003f81f9c877a8493.png" data-download-href="/uploads/short-url/p5N3fsgvPTz1Mt59Xmp4GFn6HKz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afddef8b1b2a331b48d1ed1003f81f9c877a8493_2_689x262.png" alt="image" data-base62-sha1="p5N3fsgvPTz1Mt59Xmp4GFn6HKz" width="689" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afddef8b1b2a331b48d1ed1003f81f9c877a8493_2_689x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afddef8b1b2a331b48d1ed1003f81f9c877a8493_2_1033x393.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afddef8b1b2a331b48d1ed1003f81f9c877a8493_2_1378x524.png 2x" data-dominant-color="656886"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2558×973 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Screenshot 5: Skeleton after applying Andras’ method (notice Surface smoothing is turned off)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acdf1d79d7ff5ba2eedcdb35056db5ad99ac8525.png" data-download-href="/uploads/short-url/oFi96GCHNZIoD9g9jd0Qd20nKcZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acdf1d79d7ff5ba2eedcdb35056db5ad99ac8525_2_671x499.png" alt="image" data-base62-sha1="oFi96GCHNZIoD9g9jd0Qd20nKcZ" width="671" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acdf1d79d7ff5ba2eedcdb35056db5ad99ac8525_2_671x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acdf1d79d7ff5ba2eedcdb35056db5ad99ac8525_2_1006x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acdf1d79d7ff5ba2eedcdb35056db5ad99ac8525.png 2x" data-dominant-color="999BCF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1303×970 20.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Screenshot 6: same Skeleton.nrrd loaded as Surface in ImageJ and exported as STL (notice ImageJ also uses rhomboid voxels when it creates a Surface + holes between adjacent voxels)</p>

---

## Post #9 by @lassoan (2022-07-20 11:27 UTC)

<aside class="quote no-group" data-username="chris_nik" data-post="8" data-topic="24361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ac8455/48.png" class="avatar"> chris_nik:</div>
<blockquote>
<p>What I am trying to visualise is a skeleton of a segmentation of a suture, so it is not a blood vessel, the VMTK extension would have been very useful otherwise.</p>
</blockquote>
</aside>
<p>The original developers of VMTK used it mainly for vascular applications, but it is equally applicable for analysis of any somewhat elongated, tubular-like structures (has been used successfully for airways, intestines, plant roots, etc.). It should work well for sutures, too.</p>
<aside class="quote no-group" data-username="chris_nik" data-post="8" data-topic="24361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ac8455/48.png" class="avatar"> chris_nik:</div>
<blockquote>
<p>However I am starting to think that a surface can’t be displayed otherwise (s. Screenshot 6 from ImageJ when you create a 3D Surface of the same Skeleton → it still has rhomboid voxels and slight holes between adjacent voxels)?</p>
</blockquote>
</aside>
<p>Yes, you are right, you won’t be able to see cube voxels. It is because segmentation is for representing smooth, continuous surfaces. Even if in some representations (such as in binary labelmap) discrete point samples are used, the result is always reconstructed into a smooth surface. For binary labelmap to closed surface conversion we use continuous version of the flying edges algorithm, which creates rhomboids from standalone voxels (and not the discrete version, which creates cubes).</p>
<p>You could run the discrete version manually by using a couple of lines of Python script, but I would not recommend that, because physical reality is never discrete (at least not in our domain). Instead, properly segment the real size of the suture, and then get the smooth continuous centerline curve directly from that, using VMTK.</p>
<p>If you don’t have the original segmentation anymore, just the binary labelmap skeleton then you can use Margin effect in Segment Editor to blow it up into a thicker tube. You can then use VMTK on this thicker segment.</p>

---

## Post #10 by @chris_nik (2022-07-20 12:29 UTC)

<p>Thank you for the detailed explanation, it really helped! : )</p>

---
