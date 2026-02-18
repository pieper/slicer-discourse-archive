# Difference in STL file exported from 3DSlicer and created in Matlab

**Topic ID**: 25850
**Date**: 2022-10-23
**URL**: https://discourse.slicer.org/t/difference-in-stl-file-exported-from-3dslicer-and-created-in-matlab/25850

---

## Post #1 by @SimoneCR (2022-10-23 13:02 UTC)

<p>I have a 512x512x331 DICOM volume of a CT scan, with voxel size of 0.723x0.723x0.8. I manually segmented (Region Growing) it in 3DSlicer to retain the femur head only. Exporting this segment to STL file, I can see that it has consistent difference in size from the one I read in Matlab. In Matlab, I obtained the femur segment reading the DICOM and cropping it using the binary labelmap taken from the same 3DSlicer segmentation: when I create the corresponding STL file with <code>stlwrite</code> (from Exchange) I can appreciate this difference in the dimensions.</p>
<p>So I thought it must be some reading options of <code>stlwrite</code> and I rescaled the vertices I obtained from this according to the original voxel size: the differences become much more slight but not negligible, at least in the z-dimension (almost 2-3 mm, as if 3 or 4 slices are missing).<br>
What is strange is that the segmentation has 147 slice, 0.8 mm each: so I should have a piece 117.6mm tall, but neither the 3DSlicer output (119.64mm) nor the Matlab “scaled” one (116.8mm) are correct. I can understand the problem in Matlab, maybe because of the function used, but should the 3DSlicer output not reproduce the real size? Do you think that the fact that SliceThickness is 1mm can be a problem? PS I create STL faces and verticecs using isosurface and isocaps.</p>
<p>Can anyone help me with this? It depends on the Matlab function or on some 3DSlicer settings?</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2022-10-23 14:01 UTC)

<aside class="quote no-group" data-username="SimoneCR" data-post="1" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>In Matlab, I obtained the femur segment reading the DICOM and cropping it using the binary labelmap taken from the same 3DSlicer segmentation</p>
</blockquote>
</aside>
<p><code>dicomread</code> only provides a dump of voxels in a 3D array. It is up to you to reconstruct an image in physical space and determine its geometry (origin, spacing, axis directions). Often the slices are axial, equally spaced, and difference vector between slice positions is parallel to the slice normal. If all these assumptions are true, then you can get slice spacing by computing position difference between two neighbor slices (<code>SliceThickness</code> value does as slice spacing), and then use pixel spacing and slice spacing to scale the isosurface obtained from the voxel array to get correct physical size. If any of the assumptions are incorrect then this simplistic scaling will result in incorrect physical sizes.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="1" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>Do you think that the fact that SliceThickness is 1mm can be a problem?</p>
</blockquote>
</aside>
<p>SliceThickness does not play any role in determining geometry in phsycial space. It just gives information about how much an image is focused on the image plane.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="1" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>should the 3DSlicer output not reproduce the real size? Do you think that the fact that SliceThickness is 1mm can be a problem?</p>
</blockquote>
</aside>
<p>3D Slicer reconstructs image geometry correctly if none of the above mentioned assumptions are true (or reports a warning if it cannot deal with some special cases), tested by many users, on all kinds of imaging devices and various imaging protocols.</p>
<p>Therefore, most likely the mesh that you get from 3D Slicer is correct. However, if you have any doubts, acquire an image of an object of known physical size and make measurements. If you find any potential issues then send us the DICOM files for investigation (upload the DICOM files to onedrive/dropbox/google drive and post the link here).</p>

---

## Post #3 by @SimoneCR (2022-10-23 15:10 UTC)

<p>Thank you very much for your reply.<br>
The assumptions you described are all true. When I asked if SliceThickness can be a problem, I meant if it can be a problem that slice are 1mm thick but voxel only 0.8mm (there is overlapping).<br>
Indeed, I “trust” 3DSlicer the most but I can’t figure out why, if my segment covers just 147 slices and they are all 0.8 thick, I don’t get an exported STL of 117.6 mm. And the same for Matlab, even if I scaled it correctly with slice and pixel spacings. Moreover, I used to add a background slice over and under the model to “close” it, but this made the size grow; I solved using isocaps, but I am still not convinced.<br>
I have read that checking the Acquisition Geometry Regularization can affect the result, it is possible?</p>

---

## Post #4 by @lassoan (2022-10-24 02:19 UTC)

<p>Acquisition geometry regularization applies a non-linear transform to the voxel array to warp it to the physical space. It is necessary for dealing with varying slice spacing, non-parallel slices, gantry tilt, etc. If you are sure that all the assumptions that I described are true, then acquisition geometry regularization is not necessary.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="3" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>if my segment covers just 147 slices and they are all 0.8 thick, I don’t get an exported STL of 117.6 mm</p>
</blockquote>
</aside>
<p>How do you know that your segment covers 147 slices? What is the size of the extracted isosurface?</p>
<p>Image value at the image boundary is undefined. We only know the voxel value at the center of the last voxel, but the image boundary is 0.5 voxel away from it. It is up to the software application to decide what to do with that half voxel (crop it or extrapolate using voxel duplication, mirroring, wrapping, etc.). So, if the expected size is just up to 2x half voxel off then I would not worry about it. If you want to measure the size of an object then make sure there is at least one voxel border around it.</p>
<p>Also note that the segmentation’s binary labelmap representation stores discrete point samples. To reconstruct the continuous signal, i.e., the object’s actual shape, you need to apply smoothing to the discrete samples. This smoothing may erode sharp tips, which again can make a few-voxel difference when you measure long, thin objects. If this may affect you then make sure to acquire images at sufficiently high resolution (so that 1-2 voxel size difference does not cause any significant difference).</p>

---

## Post #5 by @SimoneCR (2022-10-24 10:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you are sure that all the assumptions that I described are true,</p>
</blockquote>
</aside>
<p>Is there a method to assure those assumptions? For example, GantryTitl attribute value is 0, and I can check the thickness of all slices, but for the others?</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How do you know that your segment covers 147 slices?</p>
</blockquote>
</aside>
<p>When I look in the axial representation of the femur segmentation label, I can count 147 slices where the segment in them, i.e. with “material” inside: if each is 0.8 mm thick, should not I get a 117.6 mm (147*0.8) height? Or should I have a 116.8 mm height (since we are considering not the thickness but the spacing between slice’s centers)? And why is 116.8 mm indeed what I get if I make the difference using the mesaures indicate on the slices toolbar? Sorry if my questions sounds trivial, but I am quite a beginner and I cannot really understand these discrepancies!</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Image value at the image boundary is undefined. We only know the voxel value at the center of the last voxel, but the image boundary is 0.5 voxel away from it.</p>
</blockquote>
</aside>
<p>This, I think, is the most important thing: how can I know how the software computes it? Because I think that the problem is in the slice overlapping</p>

---

## Post #6 by @SimoneCR (2022-10-24 16:47 UTC)

<p>I think I have found the solution or, at least, the cause of my problem.<br>
It seems that I fed Matlab with the binary labelmap originally derived from the first thresholding, while I got the STL from the 3D femur segment: is it possible that some of the smoothing operations I applied, involved the segment only and not the map on the slices? If that is the case, how can I fix it? Because I tried the “export the visible segment to binary labelmap” option but it does not work: I get a binary labelmap, but the dimensions are all upset, not the same as DICOM volume, and so I cannot overlap them in Matlab.</p>

---

## Post #7 by @pieper (2022-10-24 18:46 UTC)

<p><a class="mention" href="/u/simonecr">@SimoneCR</a> I suggest you validate your assumptions on synthetic data, and perhaps then share your full analysis if you still have uncertainties.</p>
<p>Many of us here have given up on matlab and work exclusively in python/slicer so we can give you better help if you find a way to do all your analysis outside of matlab.</p>

---

## Post #8 by @lassoan (2022-10-24 20:26 UTC)

<aside class="quote no-group" data-username="SimoneCR" data-post="6" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>is it possible that some of the smoothing operations I applied, involved the segment only and not the map on the slices</p>
</blockquote>
</aside>
<p>The antialiasing filter applied on the mesh to reconstruct the continuous surface from discrete samples is applied on the surface mesh. If you don’t apply antialiasing filter in Matlab but just use the isosurface function then you’ll have a blocky model instead of the true physical surface and up to a size difference of a voxel, because Matlab’s isosurface function assumes that the voxel values are continuous, while actually they are discrete labels. You either need to apply a low-pass filter on the voxel values before you get the isosurface or you need to apply low-pass filter (spatial smoothing) on the surface mesh.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="6" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>I tried the “export the visible segment to binary labelmap” option but it does not work: I get a binary labelmap, but the dimensions are all upset, not the same as DICOM volume, and so I cannot overlap them in Matlab</p>
</blockquote>
</aside>
<p>There is no such thing as a DICOM volume. DICOM only specifies a list of slices. It is up to you to put together a volume from it. Ordering of voxels, choice of origin, axis directions, etc. are all quite arbitrary. If your arbitrary choices don’t match  the arbitrary choices in Slicer then the raw voxel array will not match up. However, this should not be a problem, because in phyiscal space everything should match up.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="6" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>If that is the case, how can I fix it?</p>
</blockquote>
</aside>
<p>Best practice is to implement your algorithms to work in physical space. If you want to do some operations in voxel space then you resample the images for that operation. This resampling is a standard processing step, provided by all image computing libraries, and it may not necessarily mean that the voxels are interpolated, often it just ends up reordering the voxels, or not changing them at all. But you cannot assume that you can just skip this step.</p>
<p>To make it easier to use Slicer with any software, we added an option to do this resampling in Slicer, before exporting the data. For this, you need to choose a reference image when you export your segmentation and then the segmentation’s voxel array match up with the the reference image’s voxel array. See some more details <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">here</a>.</p>
<hr>
<p>I fully agree with <a class="mention" href="/u/pieper">@pieper</a>’s comment above. 15-20 years ago many of us still used Matlab heavily, but over the years the Python ecosystem went way beyond that you could ever imagine to do in Matlab. We now all use Python and all the tools and libraries that are easily available in Python (supplied with limited C++ algorithm/infrastructure development as needed) to fulfill our medical image computing software needs.</p>

---

## Post #9 by @SimoneCR (2022-10-24 22:41 UTC)

<p>No, sorry, probably I did not explained myself clearly. Let’s leave Matlab aside for now: I noticed that the problem is just and all a little difference between the length of the 3Dsegment I created with Grow from seeds and the corresponding binary labelmap I exported from afterwards.<br>
Do you know how this can happen? Is it possible that I made some changes with the smoothing operators that affect only the 3Dview? Is there a way to get a stl from the “shorter” labelmap, or a labelmap, from the “longer” 3D segment, with the same size and spacing of the original DICOM?<br>
Thanks again, these are my last doubts</p>

---

## Post #10 by @lassoan (2022-10-25 04:32 UTC)

<p>A labelmap contains discrete samples, while the reconstructed 3D surface is continuous. Therefore, there is a slight difference between the two. You can see that if you choose to show the closed surface representation (in red) in slice views, over the binary labelmap representation (green):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a0526b36909ebeb617ee1720e136e34f7deb222.jpeg" data-download-href="/uploads/short-url/5ZJ5AluqlcHbTAYWvo9gQoF52fg.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a0526b36909ebeb617ee1720e136e34f7deb222_2_690x256.jpeg" alt="image" data-base62-sha1="5ZJ5AluqlcHbTAYWvo9gQoF52fg" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a0526b36909ebeb617ee1720e136e34f7deb222_2_690x256.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a0526b36909ebeb617ee1720e136e34f7deb222_2_1035x384.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a0526b36909ebeb617ee1720e136e34f7deb222.jpeg 2x" data-dominant-color="6D6D6C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1150×428 72.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @SimoneCR (2022-10-25 16:59 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a>. Is there a way to have at least an idea of the magnitude of this “approximation”? To speculate about any discrepancies… it can depend on the Slicer version used?<br>
Last thing, for real: how can I check from the DICOM header if slices overlap? Because I am sure that their centers are 0.8 mm away, but SliceThickness is 1 mm: how can I compute the part thickness with, for example, 10 slices? I thought of:<br>
THICKNESS = [(<span class="hashtag">#slices-1</span>)*0.8] + 1 ? With the last (+1) that takes into account the half (0.5 mm) of the first slice and the half of the last slice, since the count starts from the slice centers</p>

---

## Post #12 by @lassoan (2022-10-25 17:49 UTC)

<aside class="quote no-group" data-username="SimoneCR" data-post="11" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a>. Is there a way to have at least an idea of the magnitude of this “approximation”?</p>
</blockquote>
</aside>
<p>This is not an approximation. It is reconstruction of the original continuous signal from discrete samples. If voxel shape is cubic then the difference is less than the size of half voxel.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="11" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>it can depend on the Slicer version used?</p>
</blockquote>
</aside>
<p>You can modify the smoothing factor. This is useful when the image has non-cubic voxels (e.g., 0.2mm pixel spacing within the slice, but 5mm distance between slices), because then you may not want to remove all aliasing artifacts (you accept some staircased appearance so that you see more details within each slice).</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="11" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>Last thing, for real: how can I check from the DICOM header if slices overlap?</p>
</blockquote>
</aside>
<p>SliceThickness gives some approximate indication of how much the image is focused on the slice plane, which may be interesting only in very special cases (e.g., you are looking for a 1mm seed in an image with 10mm spacing and you want to know if not seeing traces of a seed means if the seed is actually not there; but of course you should use higher resolution imaging if you look for small details like this).</p>
<p>Therefore, SliceThickness information is not relevant for 3D reconstruction. Maybe the user could be warned if the thickess is a different magnitude than the distance between slices (because that might indicate incorrect imaging settings, missing slices, etc.), but I’ve never seen such images.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="11" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>THICKNESS = [(<span class="hashtag-raw">#slices-1</span>)*0.8] + 1 ? With the last (+1) that takes into account the half (0.5 mm) of the first slice and the half of the last slice, since the count starts from the slice centers</p>
</blockquote>
</aside>
<p>1.0 and 0.8mm are close enough. It’s not like SliceThickness means that everything in 0.8mm is taken into account and everything beyond is ignored. DICOM does not specify an exact definition of this SliceThickness value, but it is up to the device manufacturers to define it. They may store a value like peak width at half height of the point spread function.</p>

---

## Post #13 by @SimoneCR (2022-10-25 21:41 UTC)

<p>Thank you, this was enlightening.<br>
So, if I have voxel depth=0.8 mm, it means each slice is 0.8 mm thick?<br>
With 101 slices can I more or less confidently say “a priori” I should have a (101-1)*0.8=80 mm thick volume? With possibly +/- 0.4 mm in a reconstruction from a binary labelmap (as it happens in Matlab)?</p>

---

## Post #14 by @muratmaga (2022-10-25 22:18 UTC)

<aside class="quote no-group" data-username="SimoneCR" data-post="13" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>it means each slice is 0.8 mm thick?</p>
</blockquote>
</aside>
<p>No, it means next slice is 0.8mm away in the stack. Remember slice thickness is “gives some approximate indication of how much the image is focused on the slice plane” (from lassoan’s response).</p>
<p>So, yes if you make 101, 101, 101 voxel image, where the image spacing in 3rd dimension is 0.8 mm, if you measure the height of the volume, you will get 80mm.</p>
<p>The best way to convince yourself is to install the ImageMaker extension, arbitrarily create volumes of different voxel sizes and dimensions, and measure things in them. E.g. I created a 101,101,101 volume with 1mm spacing, filled it with a 100mm diameter sphere center on the middle slice (using paint tool), and them measured the diameter of the resultant 3D sphere. The difference is within my measurement error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9ba8c33998186786e3004990d62e51ffa7593c5d.png" data-download-href="/uploads/short-url/md1zXYcGmjfpNlXnA2rpRRNAgBn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9ba8c33998186786e3004990d62e51ffa7593c5d_2_690x477.png" alt="image" data-base62-sha1="md1zXYcGmjfpNlXnA2rpRRNAgBn" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9ba8c33998186786e3004990d62e51ffa7593c5d_2_690x477.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9ba8c33998186786e3004990d62e51ffa7593c5d_2_1035x715.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9ba8c33998186786e3004990d62e51ffa7593c5d_2_1380x954.png 2x" data-dominant-color="A3A6A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1645×1138 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @SimoneCR (2022-10-25 23:57 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> .</p>
<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>No, it means next slice is 0.8mm away in the stack</p>
</blockquote>
</aside>
<p>I see. But is there an attribute/a method to get the real slice thickness? Since, if 0.8 is the spacing between the centers, aren’t we excluding the half of the first and last slice? Shouldn’t we obtain more than 80 mm (with 0.8 mm spacing and 101 slices)?</p>
<p>Very interesting extension.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>The difference is within my measurement error.</p>
</blockquote>
</aside>
<p>How can you say that? If you had achieved 98.2, for example?</p>

---

## Post #16 by @muratmaga (2022-10-26 01:36 UTC)

<p>İt is 99.22 on a line that i manually placed.<br>
That less than 1% of the length. Definitely i am comfortable with that level of measurement error.</p>

---

## Post #17 by @SimoneCR (2022-10-26 08:14 UTC)

<p>Perfect, I got it. I thought there can be a quantitative measure of the error.<br>
And can you try to export the stl of that sphere and see what dimensions it has? For example checking it in netfabb or similar</p>

---

## Post #18 by @muratmaga (2022-10-26 15:57 UTC)

<aside class="quote no-group" data-username="SimoneCR" data-post="17" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>Perfect, I got it. I thought there can be a quantitative measure of the error.</p>
</blockquote>
</aside>
<p>You can, if you want to. Statistical approach is called repeated measures. You can calculate the standard error of your manual measurements, and compare within the context of the actual measurement.</p>
<aside class="quote no-group" data-username="SimoneCR" data-post="17" data-topic="25850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/simonecr/48/17029_2.png" class="avatar"> SimoneCR:</div>
<blockquote>
<p>And can you try to export the stl of that sphere and see what dimensions it has? For example checking it in netfabb or similar</p>
</blockquote>
</aside>
<p>I don’t have bandwidth for that, nor know the software you mention. But you can try. The point is we are fairly confident in the measurements reported by Slicer. Whatever inconsistency you are seeing with Matlab, you have to develop these “synthetic” datasets (with known dimensions) as mentioned by <a class="mention" href="/u/pieper">@pieper</a> and try to figure out where the difference is coming from.</p>

---

## Post #19 by @SimoneCR (2022-10-26 17:46 UTC)

<p>Ok, I got it.<br>
Thank you all for your replies, you have been very helpful.</p>
<p>Best</p>

---
