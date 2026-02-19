---
topic_id: 4792
title: "I Cannot Remove Ridges In 3D Segmentation"
date: 2018-11-19
url: https://discourse.slicer.org/t/4792
---

# I cannot remove "ridges" in 3D segmentation

**Topic ID**: 4792
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/i-cannot-remove-ridges-in-3d-segmentation/4792

---

## Post #1 by @nwskelley (2018-11-19 04:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9195209a43ef8caf6103e25de91c2d0624c89d9.jpeg" data-download-href="/uploads/short-url/xg5uXSIKtT2QwexG65i6DMoQtEl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9195209a43ef8caf6103e25de91c2d0624c89d9_2_690x382.jpeg" alt="image" data-base62-sha1="xg5uXSIKtT2QwexG65i6DMoQtEl" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9195209a43ef8caf6103e25de91c2d0624c89d9_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9195209a43ef8caf6103e25de91c2d0624c89d9_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9195209a43ef8caf6103e25de91c2d0624c89d9.jpeg 2x" data-dominant-color="6C6D72"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1322×732 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hello! I am a surgeon trying to segment a hip joint for 3-D printing. I have become pretty good at isolating the femur and pelvis bones making different segments, however, I’ve noticed in all of my models I have these “ridges” or “steps” on the side of the segmented model. When I set the master file as axial, I notice the steps in the axial plane. In this picture, I used the sagittal file and have these ridges in that plane.</p>
<p>The CT DICOMs I’m using have high resolution cuts in axial, sagittal, and coronal planes, but 3D slicer is making me pick one for the master volume for segmenting. When it picks the master volume, it’s creating these other planes but they are usually much lower resolution. In the attached image you can see the sagittal plane is very smooth and anatomic, but the coronal plane made from the master file has multiple steps or ridges.</p>
<p>Questions:</p>
<ol>
<li>Are these ridges the product of the DICOM data I’m putting in 3-D slicer–in other words, should I tell the radiologist to take a different type of CT scan?</li>
<li>Can I tell 3D slicer to use the high resolution inputs from the axial, coronal, and sagittal data instead of it selecting only one for the master file and then creating the other low-resolution views?</li>
<li>Is there any way to smooth these ridges in the attached image with the current DICOM data? I tried the smoothing function and changing the kernal size, but that only helped a little.</li>
</ol>
<p>Thank you very much for your time and consideration!</p>

---

## Post #2 by @lassoan (2018-11-19 05:08 UTC)

<aside class="quote no-group" data-username="nwskelley" data-post="1" data-topic="4792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f07891/48.png" class="avatar"> nwskelley:</div>
<blockquote>
<p>The CT DICOMs I’m using have high resolution cuts in axial, sagittal, and coronal planes, but 3D slicer is making me pick one for the master volume for segmenting.</p>
</blockquote>
</aside>
<p>Unfortunately, this is a common image acquisition problem. See for example <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">this discussion</a>. Maybe imaging techs don’t know that such scans are not well suited for 3D reconstruction or high-resolution 3D reconstruction is not a priority.</p>
<p>Anyway, you can address this by forcing the segmentation’s internal labelmap representation to have isotropic voxel spacing.</p>
<p>Example: Bone segmentation with thresholding. 3D surface representation is created with surface smoothing disabled, master volume’s interpolation is disabled to see voxel boundaries more clearly.</p>
<p>Using the master volume’s spacing (0.7 x 0.7 x 2.5):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d42ff3b313e0b7c866a456eb0434dbe78cffdfd6.png" data-download-href="/uploads/short-url/uh5XxspYh3jmpelfbNE15UkatE2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d42ff3b313e0b7c866a456eb0434dbe78cffdfd6_2_546x500.png" alt="image" data-base62-sha1="uh5XxspYh3jmpelfbNE15UkatE2" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d42ff3b313e0b7c866a456eb0434dbe78cffdfd6_2_546x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d42ff3b313e0b7c866a456eb0434dbe78cffdfd6_2_819x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d42ff3b313e0b7c866a456eb0434dbe78cffdfd6_2_1092x1000.png 2x" data-dominant-color="8B928F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1292×1182 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Enable “Isotropic spacing” in the segmentation geometry window (resulting spacing: 0.7 x 0.7 x 0.7) and then re-thresholding (see how blocky the master volume is and how smooth the segmentation(:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bf540d03f2886ffa3322ec1e431dafbf72e2551.png" data-download-href="/uploads/short-url/8ypCDPLGyUsj3zzZvqTQAQ8p649.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bf540d03f2886ffa3322ec1e431dafbf72e2551_2_383x500.png" alt="image" data-base62-sha1="8ypCDPLGyUsj3zzZvqTQAQ8p649" width="383" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bf540d03f2886ffa3322ec1e431dafbf72e2551_2_383x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bf540d03f2886ffa3322ec1e431dafbf72e2551_2_574x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3bf540d03f2886ffa3322ec1e431dafbf72e2551_2_766x1000.png 2x" data-dominant-color="EEF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">929×1210 79.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d2f3bfa14d9cd290c058d28dc511a986d3da7c4.png" data-download-href="/uploads/short-url/fzTf57nrQQviX8eVaXsn8XbKt80.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d2f3bfa14d9cd290c058d28dc511a986d3da7c4_2_547x500.png" alt="image" data-base62-sha1="fzTf57nrQQviX8eVaXsn8XbKt80" width="547" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d2f3bfa14d9cd290c058d28dc511a986d3da7c4_2_547x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d2f3bfa14d9cd290c058d28dc511a986d3da7c4_2_820x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d2f3bfa14d9cd290c058d28dc511a986d3da7c4_2_1094x1000.png 2x" data-dominant-color="8B928F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1294×1182 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After applying Smoothing effect (method: Closing; Kernel size: 5x5x5 pixels) and enabling surface smoothing (factor=0.5):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/498300db41d39e41ba8198efeef46681d6698b59.png" data-download-href="/uploads/short-url/aujwMnTj7UMO2NjIoMTVcg2N34Z.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498300db41d39e41ba8198efeef46681d6698b59_2_546x500.png" alt="image" data-base62-sha1="aujwMnTj7UMO2NjIoMTVcg2N34Z" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498300db41d39e41ba8198efeef46681d6698b59_2_546x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498300db41d39e41ba8198efeef46681d6698b59_2_819x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498300db41d39e41ba8198efeef46681d6698b59_2_1092x1000.png 2x" data-dominant-color="8B918F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1289×1180 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2018-11-19 13:50 UTC)

<p>Nice answer <a class="mention" href="/u/lassoan">@lassoan</a>!</p>
<p><a class="mention" href="/u/nwskelley">@nwskelley</a> I would just add that if you work with your radiologist and technologist you should be able to optimize the scanner to image the details you are looking for.  There are lots of parameters that trade off radiation dose, processing time, etc.</p>
<p>Specifically, modern spiral/helical CTs can reconstruct at arbitrary spacing for a given beam thickness, current, and table speed, so you may be able to get more slices from the scanner’s raw data (say at 1mm or 0.5mm spacing) that have more detail than you can get from resampling the 2.5mm slices after the fact.  It’s probably best to get these in the axial plane, which is the acquisition plane of the CT.</p>
<p>Also there are different reconstruction kernel options that may provide better contrast for the features of interest (e.g. hard tissue compared to soft tissue).</p>
<p>Let us know how it goes - I’m sure other people will also be interested in best practices for acquiring and processing this kind of data.</p>

---

## Post #4 by @nwskelley (2018-11-19 15:22 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a>. That is extremely helpful!</p>
<p>So, what I’ve learned is that I need to talk to the radiology team before obtaining these scans to obtain a better protocol for imaging the bone ROI and obtain the high resolution/thin cuts in one plane–likely the axial plane.</p>
<p>I was looking forward to trying <a class="mention" href="/u/lassoan">@lassoan</a> technique using isotropic spacing in the segmentation geometry window, but when I applied it to my program (version 4.9.0) I noticed that I do not have that box he is pointing to with the arrow. Next to the master volume drop down menu, I do not have that cube to click on. This is what my screen shows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f685556a2313afcea04651314264191c0ffa6bc0.png" data-download-href="/uploads/short-url/zaP7FJpVTsrrp521P8PpiY4R7TW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f685556a2313afcea04651314264191c0ffa6bc0_2_690x360.png" alt="image" data-base62-sha1="zaP7FJpVTsrrp521P8PpiY4R7TW" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f685556a2313afcea04651314264191c0ffa6bc0_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f685556a2313afcea04651314264191c0ffa6bc0_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f685556a2313afcea04651314264191c0ffa6bc0.png 2x" data-dominant-color="E6EBF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×562 39.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I noticed on the slicer 3D website they’ve had an update, and I was going to try to download that later today. If you have any other tips for reaching the segmentation geometry window, I’ll try that.</p>
<p>Thank you both again–I really appreciate your time and assistance!</p>

---

## Post #5 by @cpinter (2018-11-19 15:34 UTC)

<aside class="quote no-group" data-username="nwskelley" data-post="4" data-topic="4792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/f07891/48.png" class="avatar"> nwskelley:</div>
<blockquote>
<p>tips for reaching the segmentation geometry window</p>
</blockquote>
</aside>
<p>This is a recent addition to 3D Slicer. Please download the new stable version 4.10.</p>
<p>Or better yet, an even newer 4.11 nightly, which contains further <a href="https://discourse.slicer.org/t/improved-3d-preview-during-segmentation/4795/1">features</a> that help with segmentation.</p>

---
