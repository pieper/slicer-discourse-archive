---
topic_id: 684
title: "General Registration Brains Returns Joint Pdf Summed To Zero"
date: 2017-07-12
url: https://discourse.slicer.org/t/684
---

# General registration (BRAINS) returns "Joint PDF summed to zero" error

**Topic ID**: 684
**Date**: 2017-07-12
**URL**: https://discourse.slicer.org/t/general-registration-brains-returns-joint-pdf-summed-to-zero-error/684

---

## Post #1 by @Rewati_Kulkarni (2017-07-12 19:45 UTC)

<p>Operating system: Mac OSX 10.9.5<br>
Slicer version: 4.7</p>
<p>I am trying to run a registration in the BRAINS module, that is somewhat unique and different from the sample cases given online. I have a grayscale FA scalar volume image file (obtained from a DTI volume file), and I have generated an FEM mask of the actual brain section used, by means of a Matlab code. The FEM mask consists of 80-odd slices, and the file format is NifTI. I followed the protocol for BRAINS general reg. per the tutorial for DTI registration on the Slicer forum. The steps I followed and the parameters I used are as follows:</p>
<ol>
<li>
<p>Load the FAV1 file.</p>
</li>
<li>
<p>Load the FEM masks. I loaded this as a directory, since I have 80 individual slices which I can load in 3D slicer in a way that I can scroll through them as a volume file. They start with slice # slice001, and go upwards in number. [<strong>Note: in the option bar where the foreground and background can be selected, only slice001 shows up, but I can still scroll through all 80 slices]</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49038249a18302071e8ba4fde4587d011506711d.png" alt="image" data-base62-sha1="apUn8AQJnmDNYyItT2Xifzq2qnP" width="283" height="103"></p>
</li>
<li>
<p>I then chose to keep the FAV1 file as my foreground at 0.5 opacity, and the FEM mask directory, slice001, as my background. <strong>[Note: Changing the visibility of the files does not help at all. I am able to only see the file I load last, whichever it may be].</strong></p>
</li>
<li>
<p>I opened the Gen. reg. BRAINS module, and set the parameters like this. Basically, I did not alter anything except the fixed and moving image inputs. All other default numerical parameters were the same. I used the B-spline method.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/019664421c299abb81085239d85d356ce2401457.png" data-download-href="/uploads/short-url/e2GMAyHGgarG7pCQCJPz5S6S2P.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/019664421c299abb81085239d85d356ce2401457_2_290x500.png" alt="image" data-base62-sha1="e2GMAyHGgarG7pCQCJPz5S6S2P" width="290" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/019664421c299abb81085239d85d356ce2401457_2_290x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/019664421c299abb81085239d85d356ce2401457_2_435x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/019664421c299abb81085239d85d356ce2401457.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">544×936 82.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>The registration completes with errors (and barely takes a second or 2 to complete). The error is as follows:</p>
</li>
</ol>
<p><em>General Registration (BRAINS) standard error:</em></p>
<p><em>WARNING: In /Users/kitware/Dashboards/Nightly/Slicer-0-build/ITKv4/Modules/Numerics/Optimizersv4/src/itkLBFGSBOptimizerv4.cxx, line 116</em><br>
<em>LBFGSBOptimizerv4 (0x104b0e210): LBFGSB optimizer does not support scaling. All scales are set to one.</em></p>
<p><em>libc++abi.dylib: terminating with uncaught exception of type itk::ExceptionObject: /Users/kitware/Dashboards/Nightly/Slicer-0-build/BRAINSTools/BRAINSCommonLib/BRAINSFitHelperTemplate.hxx:1552:</em><br>
_itk::ERROR: Exception caught: _<br>
<em>itk::ExceptionObject (0x107a00c08)</em><br>
_Location: “unknown” _<br>
<em>File: /Users/kitware/Dashboards/Nightly/Slicer-0-build/ITKv4/Modules/Registration/Metricsv4/include/itkMattesMutualInformationImageToImageMetricv4.hxx</em><br>
<em>Line: 205</em><br>
<em>Description: itk::ERROR: MattesMutualInformationImageToImageMetricv4(0x104b02930): Joint PDF summed to zero</em></p>
<p><em>General Registration (BRAINS) standard output:</em></p>
<p><em>Original Fixed image origin[0, 0, 0, 0]</em><br>
<em>TranformTypes: BSpline(1 of 1).</em></p>
<p><em>=============================== ITKv4 Registration: Starting Transform Estimations for BSpline(1 of 1).===============================</em></p>
<p><em>Initialized BSpline transform is set to be an identity transform.</em><br>
_  - Number of parameters = 9945_<br>
<em>– WARNING: Only one in every 663 parameters is printed on screen.</em></p>
<p>_ - Cost Function Convergence Factor : 2e+13_<br>
_ - Projected Gradient Tolerance     : 1e-05_<br>
_ - Maximum Number of Corrections    : 25_<br>
_ - Maximum Number of Evaluations    : 900_<br>
_ - Maximum Number of Iterations     : 1500_</p>
<p><em>*** Running bspline registration (meshSizeAtBaseLevel = [14, 10, 12]) ***</em></p>
<p>After this point, I really don’t know what else I can do. I have tried different combinations of file loading, but nothing seems to work. I even centered the 2 files to the same origin, but I was still unable to view them together. I would be happy to provide the files if need be.</p>
<p>Sorry for the long post, but I would really like some insight into fixing this issue! Thank you in advance!</p>

---

## Post #2 by @lassoan (2017-07-12 20:55 UTC)

<aside class="quote no-group" data-username="Rewati_Kulkarni" data-post="1" data-topic="684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/8edcca/48.png" class="avatar"> Rewati_Kulkarni:</div>
<blockquote>
<p>Joint PDF summed to zero</p>
</blockquote>
</aside>
<p>This error typically occurs when the fixed and moving images do not overlap. Either translate them manually to be approximately in the same position and harden the transform; or try one of the automatic initial alignment options.</p>

---

## Post #3 by @lassoan (2017-07-13 03:20 UTC)

<aside class="quote no-group" data-username="Rewati_Kulkarni" data-post="1" data-topic="684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/8edcca/48.png" class="avatar"> Rewati_Kulkarni:</div>
<blockquote>
<p>Changing the visibility of the files does not help at all. I am able to only see the file I load last, whichever it may be</p>
</blockquote>
</aside>
<p>This is because the two volumes don’t overlap at all (this confirms that the “Joint PDF summed to zero” error is due to non-overlapping contours). Until you align the volumes, you will only see one of them at a time. After you switch volume, click the small rectangle icon at the top of slice view controller to reset the field of view.</p>
<p>You can align the volumes by using Transforms or Landmark Registration module. You may skip manual alignment and try to get <code>General registration (BRAINS)</code> compute initial alignment by using <code>useMomentsAlign</code> or <code>useGeometryAlign</code> option in <code>Transform initialization settings</code>.</p>

---

## Post #4 by @Rewati_Kulkarni (2017-07-13 12:40 UTC)

<p>Is that why I’m unable to view both images when I load them? because they<br>
do not overlap?<br>
However, as mentioned in my post, I ensured that both their centers were<br>
situated at 0,0,0. Shouldn’t this be solving the problem?</p>
<p><em>Rewati Kulkarni</em></p>
<p><em>Research Assistant, Injury Biomechanics Lab.</em></p>
<p>University of Pennsylvania,<br>
Department of Bioengineering<br>
<em>+1 267-648-7960</em> | <em><a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a> <a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a></em></p>

---

## Post #5 by @lassoan (2017-07-13 13:08 UTC)

<p>Choose one image in the red slice viewer, the other in the green slice viewer, and on both of them reset the field of view and show it in 3D (click the small rectangle and the eye icon in the slice view controller, complete the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Data_Loading_and_3D_Visualization">basic 3D Slicer tutorials</a> if you are not sure how to do these). Then you’ll see the 3D position of these volumes and check if they overlap or not.</p>

---

## Post #6 by @fedorov (2017-07-13 15:33 UTC)

<aside class="quote no-group" data-username="Rewati_Kulkarni" data-post="4" data-topic="684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/8edcca/48.png" class="avatar"> Rewati_Kulkarni:</div>
<blockquote>
<p>I ensured that both their centers were situated at 0,0,0. Shouldn’t this be solving the problem?</p>
</blockquote>
</aside>
<p>You mentioned that some of your data is generated some Matlab code.</p>
<p>It is quite possible that the results you saved from that code lose the direction/spacing information about the image. I am not sure what you mean by the above, but no, it is not sufficient that origins of the images are identical. You must consider directions and spacing, and confirm the datasets make sense when visualized as suggested by <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #7 by @lassoan (2017-07-13 15:40 UTC)

<p>I would recommend to use nrrdread.m and nrrdwrite.m functions (available in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge extension</a> or can be downloaded from <a href="https://subversion.assembla.com/svn/slicerrt/trunk/MatlabBridge/src/MatlabCommander/commandserver/">here</a>). These are well tested and set preserve origin, spacing, and directions information properly.</p>
<p>By the way, why don’t you use the  <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge extension</a> for running your Matlab code? It takes care of passing images and other parameters between Slicer and your Matlab functions.</p>

---

## Post #8 by @Rewati_Kulkarni (2017-07-13 18:43 UTC)

<p>Thank you for all your responses! I was able to fix the issue and get the registration working.</p>

---

## Post #9 by @ihnorton (2018-04-20 14:03 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/gen-registration-brains-fails-despite-overlap-of-series/2644/2">Gen Registration (Brains) fails despite overlap of series</a></p>

---
