---
topic_id: 11874
title: "How To Quantify The Measurements Obtained From The Vtk File"
date: 2020-06-05
url: https://discourse.slicer.org/t/11874
---

# How to quantify the measurements obtained from the vtk file

**Topic ID**: 11874
**Date**: 2020-06-05
**URL**: https://discourse.slicer.org/t/how-to-quantify-the-measurements-obtained-from-the-vtk-file/11874

---

## Post #1 by @danila (2020-06-05 08:08 UTC)

<p>Hi 3DSlicer experts,</p>
<p>I am working on a new project.</p>
<p>My first goal is to quantify the change of a jaw before and after an orthognathic surgery (therefore comparing the pre and post CBCT).</p>
<p>Following the tutorial I found on the DCBIA team website, I made the segmentation of the anterior skull base at t0 and t1 with the ITK-SNAP software.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aad3db73a45cd7102c0a680cc2a28f92a356af2.png" data-download-href="/uploads/short-url/8n4Rm4L7IFrSOsU1Qh4u5X6BfHQ.png?dl=1" title="immagine 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_690x431.png" alt="immagine 1" data-base62-sha1="8n4Rm4L7IFrSOsU1Qh4u5X6BfHQ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3aad3db73a45cd7102c0a680cc2a28f92a356af2_2_1380x862.png 2x" data-dominant-color="2D382D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 1</span><span class="informations">2880×1800 577 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I do the landmarks approximation about the two scans with Slicer and subsequently the recording performed on voxel relating to the skull base (using: basaline scan - T1; basaline segmentation - segmentation of anterior skull base at T1; follow-up scan - T2landmarks; follow-up segmentation - segmentation of skull base at T2landmarks).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f.jpeg" data-download-href="/uploads/short-url/wWvSfhqMX0e4WAmcHe59ouhgZGL.jpeg?dl=1" title="immagine 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_690x431.jpeg" alt="immagine 2" data-base62-sha1="wWvSfhqMX0e4WAmcHe59ouhgZGL" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6e2dd86a1c38f3217b6d4398fd2f053a11ba19f_2_1380x862.jpeg 2x" data-dominant-color="9A9AA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 2</span><span class="informations">2880×1800 733 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After the registration I have segmented the first mandible on the t1 scan and the second mandible on the t2 scan obtained from the voxel recording.  Then I transformed the segmentations of the two mandible into 3D surface models.  I uploaded the two models on Slicer and I apply the module “model to model distance”:</p>
<p>Choose file (s) to add:<br>
Modelmandible_T1.vtk and Modelmandible_T2.vtk</p>
<p>Model to model Distance:<br>
Parameter set: Create new CommandLineModule<br>
Source Model: Modelmandible_T2.vtk<br>
Target Model: Modelmandible_T1.vtk<br>
VTK output file: Create new model<br>
Distance:<br>
If i choose corresponding_point_to_point the message that appears is this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9386d297e096c5566c82782840716c7578f4031f.jpeg" data-download-href="/uploads/short-url/l352KjXxNXH6w9JWvdj3SU3Mw7Z.jpeg?dl=1" title="unamend 5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9386d297e096c5566c82782840716c7578f4031f_2_690x431.jpeg" alt="unamend 5" data-base62-sha1="l352KjXxNXH6w9JWvdj3SU3Mw7Z" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9386d297e096c5566c82782840716c7578f4031f_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9386d297e096c5566c82782840716c7578f4031f_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9386d297e096c5566c82782840716c7578f4031f_2_1380x862.jpeg 2x" data-dominant-color="CBCDE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unamend 5</span><span class="informations">1600×1000 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Instead choosing signed_closest_point</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e208f1dc2dd32060dd82b6f403f47ca380431cc.png" data-download-href="/uploads/short-url/dqGDER1gMdaTyHRcCtOyoKy9l9O.png?dl=1" title="immagine 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_690x431.png" alt="immagine 4" data-base62-sha1="dqGDER1gMdaTyHRcCtOyoKy9l9O" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e208f1dc2dd32060dd82b6f403f47ca380431cc_2_1380x862.png 2x" data-dominant-color="B6BAD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 4</span><span class="informations">2880×1800 784 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I save the vtk file that I get from this last operation renamed “color map.vtk”.</p>
<p>I open the shape analysis view module and choose “color map.vtk”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de.png" data-download-href="/uploads/short-url/1l9LFRA5Msnincwqen12E3gjC9g.png?dl=1" title="immagine 5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_690x382.png" alt="immagine 5" data-base62-sha1="1l9LFRA5Msnincwqen12E3gjC9g" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0966700bebbc214e1a13d7d9bb49ec5dfefbb5de_2_1380x764.png 2x" data-dominant-color="6B6286"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">immagine 5</span><span class="informations">2880×1598 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My question is how to quantify the measurements obtained from the vtk file, after using the model to model distance extension.</p>
<p>The second goal of my study is to compare the post-operative CT with the virtual planning made with the Simplant software, which allows you to export the STL file of the project.</p>
<p>I hope you can help me</p>

---
