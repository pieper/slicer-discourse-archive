---
topic_id: 5087
title: "Improving Manual Segmentation Of Mri Images Using Automatic"
date: 2018-12-16
url: https://discourse.slicer.org/t/5087
---

# Improving manual segmentation of MRI images using automatic methods

**Topic ID**: 5087
**Date**: 2018-12-16
**URL**: https://discourse.slicer.org/t/improving-manual-segmentation-of-mri-images-using-automatic-methods/5087

---

## Post #1 by @Javier_Salazar (2018-12-16 00:29 UTC)

<p>Operating system: Windows 10 Education (latest)<br>
Slicer version: 4.10.0</p>
<p>Hello everyone!</p>
<p>I would like to know if there are any ways to improve manual segmentation of objects done using (paintbrush, draw, etc…) to get the most accurate representation in MRI images. I have included a picture of the contours I have for one specific slice:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85f32ac1f0c062085b2f8ed6c0bc1b35981e4099.png" data-download-href="/uploads/short-url/j6Yua9eApdHu6OfjUt78ZNz7xgt.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85f32ac1f0c062085b2f8ed6c0bc1b35981e4099_2_647x500.png" alt="Capture" data-base62-sha1="j6Yua9eApdHu6OfjUt78ZNz7xgt" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85f32ac1f0c062085b2f8ed6c0bc1b35981e4099_2_647x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85f32ac1f0c062085b2f8ed6c0bc1b35981e4099_2_970x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85f32ac1f0c062085b2f8ed6c0bc1b35981e4099.png 2x" data-dominant-color="737272"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1012×782 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have tried the extension ‘SegmentEditorExtraEffects’ and using Fast Marching to generate better contours but it does not work well for my purpose. I would like the contours to “move” slightly to find the boundary of the objects without the object becoming greatly deformed. I have tried looking for active contours/diffusion snakes extentions and found this Sobolev Segmenter that would fit my purpose perfectly. However, it does not show up in extensions manager and was last updated 5 years ago so it seems to be discontinued and not workable in the current version. (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SobolevSegmenter" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SobolevSegmenter</a>). I also saw that there is a Robust Statistics Segmenter tool available but this requires Approx. Volume parameter, intensity homogeneity, and other input parameters that makes this method non-ideal. In summary, are there any segmentation tools close to this Sobolev Segmenter? If not, is there an easy way to export data/labelmap such that I can load it in another program to perform this? I know Matlab has built in active contours method but it would be ideal to keep segmentation “in-house” so that I can quickly visualize the segmentation and change parameters to get the best results.</p>
<p>Additional info: I have multiple slices segmented that form 3d models in the 3d section. Any 3D deformable model algorithms would also work great if someone can point me in the right direction.</p>
<p>Any help is greatly appreciated,<br>
Thank you for reading,<br>
Javier.</p>

---

## Post #2 by @lassoan (2018-12-16 00:49 UTC)

<p>Grow from seeds effect may work well for this case. The segmentation shown in the image is already quite good. In what aspects would you like to improve segmentation?</p>

---

## Post #3 by @Javier_Salazar (2018-12-16 01:07 UTC)

<p>Hello Mr. Lasso,</p>
<p>Thank you for the very quick reply. I have used grow from seeds and the results are included below.<br>
It seems grow from seeds deforms the contours much more than necessary unless I am doing something wrong. Is there anything else that I can use? Either in house or other programs?</p>
<p>Grow from seeds:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3e8fc273368c0f40c6ee46cc410df0625dbda75.jpeg" data-download-href="/uploads/short-url/wwbykMNPpJEnImfWvUeDykTRjwx.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3e8fc273368c0f40c6ee46cc410df0625dbda75_2_690x420.jpeg" alt="PNG" data-base62-sha1="wwbykMNPpJEnImfWvUeDykTRjwx" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3e8fc273368c0f40c6ee46cc410df0625dbda75_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3e8fc273368c0f40c6ee46cc410df0625dbda75_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3e8fc273368c0f40c6ee46cc410df0625dbda75_2_1380x840.jpeg 2x" data-dominant-color="A09D9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1522×927 394 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Watershed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2ff5dae20312eaf4a1d662b304a6bd7952da45bf.jpeg" data-download-href="/uploads/short-url/6QhblCkfjSGiXCkYtcobpUPk5qf.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff5dae20312eaf4a1d662b304a6bd7952da45bf_2_690x409.jpeg" alt="PNG" data-base62-sha1="6QhblCkfjSGiXCkYtcobpUPk5qf" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff5dae20312eaf4a1d662b304a6bd7952da45bf_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff5dae20312eaf4a1d662b304a6bd7952da45bf_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff5dae20312eaf4a1d662b304a6bd7952da45bf_2_1380x818.jpeg 2x" data-dominant-color="9D9C99"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1549×919 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Fast Marching:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f17f6a3266c4068f3880533bc3d7b6b13d2f8f5.jpeg" data-download-href="/uploads/short-url/4r48REnNDzLV0ZXcWOSXWdRBCwl.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f17f6a3266c4068f3880533bc3d7b6b13d2f8f5_2_690x384.jpeg" alt="PNG" data-base62-sha1="4r48REnNDzLV0ZXcWOSXWdRBCwl" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f17f6a3266c4068f3880533bc3d7b6b13d2f8f5_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f17f6a3266c4068f3880533bc3d7b6b13d2f8f5_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f17f6a3266c4068f3880533bc3d7b6b13d2f8f5_2_1380x768.jpeg 2x" data-dominant-color="949494"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1684×939 440 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Notice the dots that it makes on the outline of the bladder (middle area - orange contour). It moved the contours too much and caused extra areas on the left.</p>
<p>These segmentations will be used as atlases/deformable models so it’s important for it to be as accurate as possible.</p>

---

## Post #4 by @lassoan (2018-12-16 01:41 UTC)

<p>Fast marching is not suitable for this segmentation task: it works only for segmenting structures that have very different intensity compared to surrounding region; and it only can work with one segment at a time.</p>
<p>Grow from seeds will work but you need to place the seeds in a sensible way. Typically you start with painting in the center of the segment:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83366b1b45f39af976c6d5b26eaab6b15afd08d2.png" data-download-href="/uploads/short-url/iIL8EaaPAUlH614SMm5Q5qPUSv8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83366b1b45f39af976c6d5b26eaab6b15afd08d2_2_690x483.png" alt="image" data-base62-sha1="iIL8EaaPAUlH614SMm5Q5qPUSv8" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83366b1b45f39af976c6d5b26eaab6b15afd08d2_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83366b1b45f39af976c6d5b26eaab6b15afd08d2_2_1035x724.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83366b1b45f39af976c6d5b26eaab6b15afd08d2_2_1380x966.png 2x" data-dominant-color="A9A9A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1598×1119 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Prostate MRI images are typically not aligned to patient axes, therefore it is recommended to align slice viewers by clicking the “Align slice views” button (see red arrow).</p>
<p>After you’ve painted the initial seeds, click “Initialize” and you should see something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/002b6ea762677a5ae58f3a69d028d2a77680ee83.png" data-download-href="/uploads/short-url/1v3iiL8zfJRPEtcy72sohn4IYr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002b6ea762677a5ae58f3a69d028d2a77680ee83_2_690x444.png" alt="image" data-base62-sha1="1v3iiL8zfJRPEtcy72sohn4IYr" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002b6ea762677a5ae58f3a69d028d2a77680ee83_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002b6ea762677a5ae58f3a69d028d2a77680ee83_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002b6ea762677a5ae58f3a69d028d2a77680ee83_2_1380x888.png 2x" data-dominant-color="ABAFAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1608×1037 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After this, switch to Paint effect and keep painting in areas where previewed segmentation result needs corrections. When you are done, go back to Grow from seeds effect and click Apply to accept the previewed result.</p>
<p>The original segmentations that you showed in your images above are already quite good. What do you need to improve in these segmentations?</p>

---

## Post #5 by @Javier_Salazar (2018-12-16 02:27 UTC)

<p>Mr. Lasso,</p>
<p>Thanks for the tutorial on growing from seeds. I’ll be sure to utilize it in the future. I agree that the segmentations are good but because the user (me) defined the labels manually then that means I added error to my segmentations as there is variation added from me moving my mouse to make the contours. I wanted to minimize the error as I plan to use the data for atlas segmentation or deformable model segmentation for a research paper my team is working on. The best contour possible would be one that is based on image data (math based) and not user defined by draw, paintbrush, etc… since I may have included areas that don’t belong to the segmentation as shown here:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e56bd8624babbf4f097691bed0f7404c1db2c140.png" alt="Capture" data-base62-sha1="wJyoGlXRugHg3oxpmlumcu63LoI" width="399" height="164"><br>
By using an active contour model, we can find the “best” segmentation based on edge information in the images instead of using the user defined “good” segmentations. Since the segmentations will be used as inputs for other programs/code, it’s usually a good idea to minimize error as some algorithms could propagate and amplify error.</p>
<p>It looks like I will have to do this in matlab/python using nrrd files and coding my own algorithm, but if you or anyone knows of an easier solution, please let me know!</p>
<p>I may just use the “good” segmentations and see how the results work out and revisit this at a later time.</p>
<p>Javier</p>

---

## Post #6 by @lassoan (2018-12-16 03:02 UTC)

<p>Segmenting the bladder on MRI is trivial and Grow from seeds will give you very accurate results.</p>
<p>Segmenting the prostate on MRI is hard and simple active contour based methods will not help much because the difficulty is not accurately drawing the contour but knowing which contour corresponds to the prostate boundary. Also, when you generate ground truth for training and evaluating (semi)automatic segmentation methods, you do not want to use (semi)automatic methods because then the resulting segmentation would be biased or could contain other errors. For ground-truth prostate segmentation, a good approach could be to segment every N-th slice very carefully and interpolate between them using Fill between slices effect.</p>
<aside class="quote no-group" data-username="Javier_Salazar" data-post="5" data-topic="5087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ecb155/48.png" class="avatar"> Javier_Salazar:</div>
<blockquote>
<p>It looks like I will have to do this in matlab/python using nrrd files and coding my own algorithm, but if you or anyone knows of an easier solution, please let me know!</p>
</blockquote>
</aside>
<p>Prostate segmentation on MRI is a <em>very</em> widely studied problem, with hundreds of research papers written about it. Do not even consider coming up with a new algorithm from scratch before carefully evaluating existing methods and implementing a few promising ones.</p>
<p>You may try Slicer’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DeepInfer">DeepInfer extension</a>, which can segment prostate on MRI using deep learning based method.</p>
<p>Also note that there are also huge databases of prostate MRIs with accurate segmentation created by expert clinicians, so you might not even need to generate more ground-truth data.</p>

---

## Post #7 by @Javier_Salazar (2018-12-16 03:28 UTC)

<p>I was considering active contours (using the manual segmentations as initial contour) but with a rigid contour parameter that would allow the contour to only deviate slightly. I would not be using active contours with the whole images as the masks, only the manual segmentation that would “move” so I would be aware of what contour corresponds to what.</p>
<p>I wasn’t aware of this problem using semi automatic methods for other semi automatic methods, thank you for bringing this to my attention. This isn’t prostate segmentation but female pelvic floor segmentation. Also, my sentence of “coding my own algorithm” is badly worded I meant to say writing my own script/program using functions/libraries in matlab/python. I would not come up with a new algorithm that would be a dissertation in itself haha.</p>
<p>I have already tried Slicer’s Deepinfer but there aren’t any models suitable for the problem. They only have a few models there. I hope they can add more in the future, this is an awesome feature for slicer to have.</p>
<p>Would you happen to know where I can find these databases? We have MRI data for 5 patients only and I could not find any resources online for datasets. Due to the limited dataset (50 slices per orientation(axial, etc…) per patient), I did not investigate a neural network approach to segmentation. Could you point me in the right direction or point me to someone that knows about ground truth data related to the female pelvic floor?</p>

---

## Post #8 by @lassoan (2018-12-16 15:49 UTC)

<aside class="quote no-group" data-username="Javier_Salazar" data-post="7" data-topic="5087">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ecb155/48.png" class="avatar"> Javier_Salazar:</div>
<blockquote>
<p>Would you happen to know where I can find these databases?</p>
</blockquote>
</aside>
<p>You can find hundreds of pelvic MRIs (mostly male, due to high occurrence of prostate cancer) in <a href="http://www.cancerimagingarchive.net/">TCIA</a>, in <a href="http://prostatemrimagedatabase.com/">Prostate MRI Image database</a>, and on various challenge websites (such as <a href="https://grand-challenge.org/challenges/">Grand Challenge</a>).</p>
<p>TCIA: Image download from TCIA is greatly simplified by “TCIA browser” extension in Slicer, especially when you download only a handful of images. You may find TCGA-CESC cervical cancer MRI collection relevant (unfortunately no segmentation is available for this collection).</p>

---
