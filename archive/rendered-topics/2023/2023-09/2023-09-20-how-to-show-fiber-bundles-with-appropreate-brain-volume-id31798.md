---
topic_id: 31798
title: "How To Show Fiber Bundles With Appropreate Brain Volume"
date: 2023-09-20
url: https://discourse.slicer.org/t/31798
---

# How to show fiber bundles with appropreate brain volume?

**Topic ID**: 31798
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/how-to-show-fiber-bundles-with-appropreate-brain-volume/31798

---

## Post #1 by @Fumi (2023-09-20 03:03 UTC)

<p>Hi, I am using WMA for DTI tractography and have got anatomical tracts. I just wondering how to show fiber bundles with 3D brain image which is anatomically appropriate. I f I use the own case’s 3D-T1 brain image, the location was not anatomically correct as bellow.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55f89438343db5b18fca361456a8dd62af70a4db.jpeg" data-download-href="/uploads/short-url/cgxa6zYYeEQxSTgfRmTRs5Sdd3l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55f89438343db5b18fca361456a8dd62af70a4db_2_690x307.jpeg" alt="image" data-base62-sha1="cgxa6zYYeEQxSTgfRmTRs5Sdd3l" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55f89438343db5b18fca361456a8dd62af70a4db_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55f89438343db5b18fca361456a8dd62af70a4db_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55f89438343db5b18fca361456a8dd62af70a4db_2_1380x614.jpeg 2x" data-dominant-color="6E6F77"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×853 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Anyone who have any idea for this issue?<br>
Thank you in advance.</p>
<p>Sincerely,<br>
Fumi</p>

---

## Post #2 by @zhangfanmark (2023-09-20 03:22 UTC)

<p>Hi! Looks likes you may have load the tracts as Model. Please make sure you have installed SlicerDMRI and when you load the data select FiberBundle.</p>
<p>Regards<br>
Fan</p>

---

## Post #3 by @Fumi (2023-09-20 03:34 UTC)

<p>Hi Fan, Thank you for a very quick reply!<br>
When I try to chose FiberBundle, it always failed as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eec989f4c5e0777787fd392c9df8fa227f0c8b4.png" data-download-href="/uploads/short-url/6H6RQYsJTlvkpHjQAoKcr9E4IgA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eec989f4c5e0777787fd392c9df8fa227f0c8b4_2_690x462.png" alt="image" data-base62-sha1="6H6RQYsJTlvkpHjQAoKcr9E4IgA" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eec989f4c5e0777787fd392c9df8fa227f0c8b4_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eec989f4c5e0777787fd392c9df8fa227f0c8b4_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eec989f4c5e0777787fd392c9df8fa227f0c8b4.png 2x" data-dominant-color="BBBCDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×767 34 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Of course I already have installed SlicerDMRI.</p>
<p>If an anatomical tract was loaded as FiberBundle, which brain image I should use to show anatomically correctly?</p>
<p>Fumi</p>

---

## Post #4 by @zhangfanmark (2023-09-20 03:55 UTC)

<p>Hi! Can you please show details and see what is the issue? And what version of Slicer that you are using?</p>
<p>If you have successfully ran the pipeline, the dMRI baseline image can be used for anatomical reference. For better tissue contrast you can register T1w or T2w to the dMRI space.</p>
<p>Regards<br>
Fan</p>

---

## Post #5 by @Fumi (2023-09-20 04:09 UTC)

<p>OK, I am now using Slicer5.2.2, and succeeded in showing anatomicaltracts as FiberBundle in another Windows laptop. When I use my Windows note PC, that operation got error. I don’t know why this was happened, I will try reinstall Slicer in my note PC.</p>
<p>Well, I tried showing fiberbundles in baseline image, it was coarse image because of the nature of DTI. (And even in baseline image, fiber bundles seems to be located in incorrect location.) I would like to use 3D-T1 image for bundle-showing, how to resister it to dMRI space?<br>
I would be appreciated if you give an instruction on it!<br>
Thank you for your kind help.</p>
<p>Sincerely<br>
Fumi</p>

---

## Post #6 by @Fumi (2023-09-20 07:01 UTC)

<p>Fan, I tried reainstall Slicer5.2.2 or 5.4.0 either, in both Slicer my laptop PC did not show AnatomycalTracts as FiberBundle with error. The error detail shows just error loading the files. Is there any relation for problem of starage? My laptop is lacking of amount of space.</p>
<p>And as to baseline image, FiberBundles are shown in the anatomically incorrect location like this CorpusCallosum showed in the picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40c4734bf82eaf284531b8c9d25b85784050093b.jpeg" data-download-href="/uploads/short-url/9eXrY2k69ul6yxKOkfb6toNLEMz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40c4734bf82eaf284531b8c9d25b85784050093b_2_690x443.jpeg" alt="image" data-base62-sha1="9eXrY2k69ul6yxKOkfb6toNLEMz" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40c4734bf82eaf284531b8c9d25b85784050093b_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40c4734bf82eaf284531b8c9d25b85784050093b_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40c4734bf82eaf284531b8c9d25b85784050093b.jpeg 2x" data-dominant-color="59536B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1110×714 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know why these are happening?<br>
Any advice would be appreciated.</p>
<p>Fumi</p>

---

## Post #7 by @pieper (2023-09-20 22:46 UTC)

<p>The extensions for 5.4 are <a href="https://discourse.slicer.org/t/new-extensions-can-not-work-on-slicer-5-4-0-on-macos/31535/14">not working on mac correctly</a> and that probably prevents fiber bundles from loading (check the error log).</p>
<p>If you load as models, you need to be sure to specify RAS coordinates.  Fiber bundles are always in RAS because they can also have tensors-per-point that are also in RAS.  You can specify this in the options:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4b56c5d7a3bcdc76c32d379cec475e78b8b6ef9.png" data-download-href="/uploads/short-url/wDfyM4tDu1M7hGD3CuVgOKBvkzn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4b56c5d7a3bcdc76c32d379cec475e78b8b6ef9_2_690x182.png" alt="image" data-base62-sha1="wDfyM4tDu1M7hGD3CuVgOKBvkzn" width="690" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4b56c5d7a3bcdc76c32d379cec475e78b8b6ef9_2_690x182.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4b56c5d7a3bcdc76c32d379cec475e78b8b6ef9_2_1035x273.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4b56c5d7a3bcdc76c32d379cec475e78b8b6ef9_2_1380x364.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1470×388 45.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note to <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> : if anyone is working on the WMA pipeline code it would be good to add the header flag to the generated .vtk / .vtp files to indicate that they are in RAS so they will load correctly as models by default (more info <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#models">here</a>, to match the implementation <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLModelStorageNode.cxx#L480-L506">here</a>.</p>

---

## Post #8 by @Fumi (2023-09-21 03:17 UTC)

<p>Steve, Thank you for your comment. I will be aware of RAS when I load as models.<br>
I am using Windows PC, and even in Slicer5.2.2 I could not select Fiberbundle when I put  a AnatomicalTracts data in Slicer. As I would like to use Tractography Display module in SlicerDMRI, now I figure out that I need to load data as FiberBundle.</p>

---

## Post #9 by @pieper (2023-09-21 13:06 UTC)

<aside class="quote no-group" data-username="Fumi" data-post="8" data-topic="31798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/41988e/48.png" class="avatar"> Fumi:</div>
<blockquote>
<p>even in Slicer5.2.2 I could not select Fiberbundle</p>
</blockquote>
</aside>
<p>Interesting.  You have SlicerDMRI installed but you can’t select FiberBundle as a load option for .vtk files?  That should be working on all platforms.</p>

---
