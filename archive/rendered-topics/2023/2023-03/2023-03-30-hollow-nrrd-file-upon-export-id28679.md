# Hollow Nrrd File Upon Export

**Topic ID**: 28679
**Date**: 2023-03-30
**URL**: https://discourse.slicer.org/t/hollow-nrrd-file-upon-export/28679

---

## Post #1 by @kristinbindas (2023-03-30 12:23 UTC)

<p>Hi everyone.</p>
<p>I have been playing around with my MicroCT DCM files and exporting them as NRRD files. I need them to eventually use in shapeworks. Before using the smoothing filters, the full bone shape showed up fine on shapeworks. However, shapeworks will not preform the correct analyzes unless the shape is smoothed. I used the smoothing filter with Gaussian (as the rest of the options lead the program to crash) and when I upload the nrrd file into shapeworks, it now only shows a hollow shape of the bone, with no top or bottom layer. Has anyone had this problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89b76fb19122467b3b9a337ad62d2965c1fb25d7.png" data-download-href="/uploads/short-url/jEiqhxFAVUP9DBVzhG557qXztUX.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89b76fb19122467b3b9a337ad62d2965c1fb25d7_2_690x464.png" alt="Capture" data-base62-sha1="jEiqhxFAVUP9DBVzhG557qXztUX" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89b76fb19122467b3b9a337ad62d2965c1fb25d7_2_690x464.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89b76fb19122467b3b9a337ad62d2965c1fb25d7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89b76fb19122467b3b9a337ad62d2965c1fb25d7.png 2x" data-dominant-color="2C2718"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">856×576 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2023-03-30 16:47 UTC)

<p>It is not clear where you are doing your image processing prior to ShapeWorks. If it is in Slicer, you should be able to visualize what the bone looks like after smoothing (also it is not clear to me whether you are running the smoothing on the intensity data or a labelmap) and trace down where the issue is coming from.</p>

---

## Post #3 by @kristinbindas (2023-03-31 00:42 UTC)

<p>Hi there,</p>
<p>These are the steps I took to process the data. First, I uploaded my DCM data. Then I used the drawing tool to create outlines of multiple layers of the bones, including first and last layer. I attached that image below. After this point, I used the fill between slices tool to create a full 3D image of the bone. I lastly used the Gaussian smoothing tool with 3.00 mm to smooth the bone. After exporting this as an nrrd labelmap, I tried uploading to shape works, which is where I gained the imagine below.</p>
<p>Other steps I have taken to try to process my data is by uploading the dcm files and by using the threshold tool to create a 3D image of the bone. However, this leave many inconsistencies and holes in the bone. I tried using the Gaussian smoothing tool to smooth it, but it makes the bone fully disappear. If I use any other smoothing tool (median, opening, closing, etc), slicer crashes.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1798e687b8e1edfa367bb14b9d4ee3829690627.jpeg" data-download-href="/uploads/short-url/n2tiXMylny1cc9OVsV6kQsbkX2L.jpeg?dl=1" title="IMG_0553.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1798e687b8e1edfa367bb14b9d4ee3829690627_2_375x500.jpeg" data-base62-sha1="n2tiXMylny1cc9OVsV6kQsbkX2L" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1798e687b8e1edfa367bb14b9d4ee3829690627_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1798e687b8e1edfa367bb14b9d4ee3829690627_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1798e687b8e1edfa367bb14b9d4ee3829690627_2_750x1000.jpeg 2x" data-dominant-color="7D7D97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0553.jpg</span><span class="informations">3024×4032 3.71 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2023-03-31 02:29 UTC)

<p>Can you share your dicom dataset? I am not sure why you are manually tracing the outlines as you have done in the screenshot? It is too much work, and prone to errors as you have encountered.</p>

---

## Post #5 by @kristinbindas (2023-03-31 16:01 UTC)

<p>Hi there, I will attach one of the DCM data sets.</p>
<p>I used the method of tracing multiple slices and interpolating between them in order to create a smooth bone. In order to properly analyze the bone in shapeworks, the bone must be smooth and not have many holes/inconsistencies, which is the case with the threshold tool.<br>
<a href="https://drive.google.com/file/d/13R2kAURw5h7JsNkEqP9Xj_05eORJnPrH/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="" height="">001 DCM Files.zip</a><img src="//ssl.gstatic.com/ui/v1/icons/common/x_8px.png" width="" height=""></p>

---

## Post #6 by @muratmaga (2023-03-31 16:15 UTC)

<p>Looks like you didn’t share it publicly.</p>

---

## Post #7 by @kristinbindas (2023-03-31 16:16 UTC)

<p>Sorry about that. Just granted you access!</p>

---

## Post #8 by @muratmaga (2023-03-31 17:25 UTC)

<p>Couple things</p>
<ol>
<li>You can easily use existing tools in segment editor to create a cortical bone outline with a combintation of threshold effect, dilate/erode, shrink/expand and logical operators. (see the screenshot below).</li>
<li>You get a hollow surface, that because that’s what you have.</li>
<li>If you need the surface to be capped, you need to expand the dimensions of your Volume (i.e., you need to 0 pad), and manually fill the very top and bottom slices. This is doable with the CropVolume module, just expand the ROI slightly in all three views.</li>
<li>When you are running smoothing filters, you need to be mindful of the voxel spacing. if you ran like 5mm kernel size (which is 83x83x83 voxels for your dataset), it is likely it will crash because of the memory consumption. For your dataset meaningful kernel size would be about 0.1-0.5mm</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e31356fd160f5f92e3f7b2bb2a3fd191e74a20b6.jpeg" data-download-href="/uploads/short-url/woNOUo51MMSllMxT8ejW9hLVBIO.jpeg?dl=1" title="Screen Shot 2023-03-31 at 10.21.39 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31356fd160f5f92e3f7b2bb2a3fd191e74a20b6_2_423x500.jpeg" alt="Screen Shot 2023-03-31 at 10.21.39 AM" data-base62-sha1="woNOUo51MMSllMxT8ejW9hLVBIO" width="423" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31356fd160f5f92e3f7b2bb2a3fd191e74a20b6_2_423x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31356fd160f5f92e3f7b2bb2a3fd191e74a20b6_2_634x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e31356fd160f5f92e3f7b2bb2a3fd191e74a20b6_2_846x1000.jpeg 2x" data-dominant-color="484952"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-31 at 10.21.39 AM</span><span class="informations">1894×2236 669 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @kristinbindas (2023-04-03 21:45 UTC)

<p>Hi again,</p>
<p>Thanks so much for your help. I have one more question for you. Most of my DCM files are right tibias, but I have a few left ones. I would like to mirror the 3D volume to match the right tibia. I tried this by exporting the volume as an STL file, then using the surface toolbox module to mirror the volume, then exporting the mirrored stl file back to an nrrd labelmap. However, this led to an error in exporting the NRRD file. I can’t find any other way online for how to properly mirror the image. Can you help?</p>

---

## Post #10 by @muratmaga (2023-04-04 00:48 UTC)

<p>You can use the FlipImage filter in SimpleFilters to mirror your volume first, and then do the segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67139cf54fbdd00ad0f1c7c0e5196e1b34d96775.png" data-download-href="/uploads/short-url/eHRcqdkqtIvBiKUolcdm97NdFbv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67139cf54fbdd00ad0f1c7c0e5196e1b34d96775.png" alt="image" data-base62-sha1="eHRcqdkqtIvBiKUolcdm97NdFbv" width="562" height="500" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">565×502 7.98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @kristinbindas (2023-04-04 16:29 UTC)

<p>I tried that, but I an receiving an error message: &lt;class ‘slicer.util.MRMLNodeNotFoundException’&gt;. any thoughts?</p>

---

## Post #12 by @muratmaga (2023-04-04 16:31 UTC)

<p>Not sure, which version of slicer and what operating system?</p>

---

## Post #13 by @kristinbindas (2023-04-04 16:37 UTC)

<p>I believe I am using the most recent version of slicer, as I downloaded it only a few months ago. I am currently on a Mac, though.</p>

---

## Post #14 by @muratmaga (2023-04-04 16:47 UTC)

<p>OK. I can repllicate this error with your dataset. Not sure why.</p>
<p>Also I tried with the MRHead, while it doesn’t generate an error, it doesn’t mirror the image either.</p>
<p>This is a question for developers <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a>. this is the full log starting with DICOM import</p>
<pre><code class="lang-auto">Switch to module:  "DICOM"
['C:/Users/murat/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerDcm2nii/lib/Slicer-5.2/qt-scripted-modules\\Resources\\bin\\dcm2niix', '-n', '-1', '-s', 'y', '-f', '%p_%t_%s', '-i', 'y', '-o', 'C:/Users/murat/AppData/Local/Temp/Slicer\\tmpp8_s0f2l', 'C:/Users/murat/AppData/Local/Temp/Slicer\\tmpp8_s0f2l\\input-dicom-files.txt']
Chris Rorden's dcm2niiX version v1.0.20230210  (JP2:OpenJPEG) (JP-LS:CharLS) MSC1930  (64-bit Windows)
Found 168 files in 'C:/Users/murat/AppData/Local/Temp/Slicer\tmpp8_s0f2l\input-dicom-files.txt'
Found 168 DICOM file(s)
Warning: PatientOrient (0018,5100) not specified (issue 642).
Warning: Unable to determine manufacturer (0008,0070), so conversion is not tuned for vendor.
	1764499720	C:/Users/murat/AppData/Local/Temp/Slicer\tmpp8_s0f2l\Linear_Attenuation_[1_cm]_(3035)_20221027122619_3035
 C:/Users/murat/Downloads/dicoms/C0002716_00000.DCM
Conversion required 0.259000 seconds.
Loading with imageIOName: GDCM
WARNING: In D:\D\S\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478
ImageSeriesReader (00000228A88989E0): Non uniform sampling or missing slices detected,  maximum nonuniformity:9.64072e-05


Irregular volume geometry detected, but maximum error is within tolerance (maximum error of 5.32934e-05 mm, tolerance threshold is 0.001 mm).
Switch to module:  "Data"
Switch to module:  "Volumes"
Switch to module:  "SimpleFilters"
myFilter = FlipImageFilter()
myFilter.SetDebug(False)
myFilter.SetFlipAboutOrigin(False)
myFilter.SetFlipAxes((True, False, False))
myFilter.SetNumberOfThreads(16)
myFilter.SetNumberOfWorkUnits(0)
</code></pre>
<p>and then this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc2e2faf42bb5a91ca897f36bf3ec1f9c9b7326a.png" alt="image" data-base62-sha1="vpNZOW0thpRjAC4DLeAvNDH7AqS" width="435" height="120"></p>

---

## Post #15 by @lassoan (2023-04-04 17:52 UTC)

<p><code>slicer.util.MRMLNodeNotFoundeException</code> is due to Simple Filters module cannot deal with special characters in the filename. The problem is that it seems to look up nodes by name.</p>
<p>A workaround is to rename the image (e.g., <code>3035: Linear Attenuation [1-cm] (3035)</code> to <code>3035: Linear Attenuation</code>).</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/kristinbindas">@kristinbindas</a> It would be great if you could <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#i-want-to-report-a-problem">submit a bug report</a> for this to make sure we don’t forget about fixing it.</p>

---

## Post #16 by @muratmaga (2023-04-04 18:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="28679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be great if you could <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#i-want-to-report-a-problem">submit a bug report </a> for this to make sure we don’t forget about fixing it.</p>
</blockquote>
</aside>
<p>Done. See <a href="https://github.com/Slicer/Slicer/issues/6925" class="inline-onebox">Simple Filters module cannot deal with special characters in the filename · Issue #6925 · Slicer/Slicer · GitHub</a></p>
<p>What about not mirroring? This is with MRHead:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01d540acd7bdd45b1428647b30d8ccb92a6501ff.jpeg" data-download-href="/uploads/short-url/gdmSY7K9zq27GPIQuhYJQlR3av.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01d540acd7bdd45b1428647b30d8ccb92a6501ff_2_690x395.jpeg" alt="image" data-base62-sha1="gdmSY7K9zq27GPIQuhYJQlR3av" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01d540acd7bdd45b1428647b30d8ccb92a6501ff_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01d540acd7bdd45b1428647b30d8ccb92a6501ff_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01d540acd7bdd45b1428647b30d8ccb92a6501ff_2_1380x790.jpeg 2x" data-dominant-color="95949C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1935×1109 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @lassoan (2023-04-05 03:53 UTC)

<p>Mirroring of an image is a very risky operation (may lead to “wrong side” mistakes), so it is rarely done and has not been made easily accessible. FlipImageFilter works well, but it just flips the voxel order in memory, but keeps the physical position of the voxels unchanged.You can see the difference in the IJK to RAS direction matrix in Volumes module / Information.</p>
<p>If you want to physically flip the image then after you apply the FlipImageFilter, you also need to apply and harden a mirroring transformation matrix (e…g, diagonal of <code>[-1, 1, 1, 1]</code>). You need the FlipImageFilter because without that the transform would make the volume’s IJK coordinate system a left-handed coordinate system, which may lead to problems (for example, I’m not sure if NIFTI can store images that use a left-handed voxel coordinate system; models that are generated from such inverted images may have inverted normals, …).</p>

---

## Post #18 by @kristinbindas (2023-04-05 16:11 UTC)

<p>Thank you for your help. I only need the image to be flipped to compare geometry to other images. I had success with your method, however attached is an image of how the bone shows up in 3D. I am wondering why this is the case and if it would cause any issues when opening up the nrrd file in shapeworks?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bedec552ebf0065231609378774f0e5fb6f1d4d6.png" data-download-href="/uploads/short-url/rew0dTIxb1F4AwSpyYhCqA9MvhI.png?dl=1" title="Screen Shot 2023-04-05 at 12.09.08 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bedec552ebf0065231609378774f0e5fb6f1d4d6_2_672x500.png" alt="Screen Shot 2023-04-05 at 12.09.08 PM" data-base62-sha1="rew0dTIxb1F4AwSpyYhCqA9MvhI" width="672" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bedec552ebf0065231609378774f0e5fb6f1d4d6_2_672x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bedec552ebf0065231609378774f0e5fb6f1d4d6_2_1008x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bedec552ebf0065231609378774f0e5fb6f1d4d6_2_1344x1000.png 2x" data-dominant-color="999CD1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-04-05 at 12.09.08 PM</span><span class="informations">1654×1230 88.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @muratmaga (2023-04-05 16:42 UTC)

<aside class="quote no-group" data-username="kristinbindas" data-post="18" data-topic="28679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kristinbindas/48/65526_2.png" class="avatar"> kristinbindas:</div>
<blockquote>
<p>however attached is an image of how the bone shows up in 3D. I am wondering why this is the case</p>
</blockquote>
</aside>
<p>Not sure what you are asking here? Can you specify what you think the issue is?</p>

---

## Post #20 by @kristinbindas (2023-04-05 18:21 UTC)

<p>Hi, sorry about that. The box around the bone is way larger than the bone itself, and it is making it so the bone does not show up on shapeworks when I upload it</p>

---

## Post #21 by @muratmaga (2023-04-05 18:59 UTC)

<p>That long bounding box simply means there is something else loaded in your scene (it may not be visible). If you export your segmentation as a label map ,(which i believe is what shape work expects) and save it, it should be fine.<br>
If shape works doesn’t show that file, you probably need to ask them what format is necessary.</p>

---
