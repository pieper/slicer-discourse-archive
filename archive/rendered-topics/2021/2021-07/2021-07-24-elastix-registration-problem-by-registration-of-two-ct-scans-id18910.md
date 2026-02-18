# Elastix Registration Problem by registration of two CT Scans with completely different Gray Values and artifacts

**Topic ID**: 18910
**Date**: 2021-07-24
**URL**: https://discourse.slicer.org/t/elastix-registration-problem-by-registration-of-two-ct-scans-with-completely-different-gray-values-and-artifacts/18910

---

## Post #1 by @Solli (2021-07-24 20:33 UTC)

<p>Hello,<br>
I have two CT Datasets of a 3D Printed Skull Phantom. One CT Scan is from a clinical CT scanner and the second scan is from an industrial CT scanner. The scan from the clinical CT has Hounsfield values between -1024 and 3072. The scan from the industrial scanner has grey values between 8087 - 12539.Both scans have a different size. The scan of the clinical scanner has a size of 512x512x606 and the industrial scan has a size of 512x512x715.<br>
I attached two screenshots from a axial slice so that you can see the different with the grey values. Now i want to register these two scans. I tried it with the General Registration (Elastix) but it doesn’t work. I dont’t get a registration of both skull bones. But when i used two different scans from a clinical CT it worked well. The problem is that on the industrial ct artifacts are visible. Has somebody an idea how i can get a proper registration results? I thought that maybe the artifacfts are a problem for the registration?<br>
I would be really happy about some help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Best regards<br>
Solveig</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb60d2192c00f183c227c60c254bcdf3bfaea614.jpeg" alt="Phantom Fraunhofer" data-base62-sha1="qJCIUrcMaXP0QrVwp2OMSmNRAi0" width="582" height="442"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b509836ea143d751dbf5168446a1c53b6e9f51fc.jpeg" alt="Phantom UKSH" data-base62-sha1="pPwNSCmomNYLglmhbxTRvfAkRxG" width="582" height="442"></p>

---

## Post #2 by @lassoan (2021-07-25 04:00 UTC)

<p>Before you launch an automatic intensity-based image registration, you must approximately align the scans using manual or semi-automatic methods. See more information here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration" class="inline-onebox">Registration — 3D Slicer documentation</a>.</p>

---

## Post #3 by @Solli (2021-07-25 09:10 UTC)

<p>Hello Andras,<br>
Thank you so much. I used now the landmark registration before i used the elastix.<br>
Here you can see the result of the landmark registration.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc903da59294bb7c4b39449eb7148595e7ab699a.jpeg" alt="landmark registration" data-base62-sha1="vtc4PQxs2G1K7a2gYwQt6B9qTeW" width="373" height="449"></p>
<p>Then i applied the elastix registration.<br>
But i still get a strange result (See the Photo belov)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87ceff2bafc9aef49862f7451f3c8fc13efe6ae8.jpeg" alt="registrierung" data-base62-sha1="jnpWImpNXSuyvDeeS13AvSTRVGg" width="373" height="449"></p>
<p>Do you have any idea why i get this result?<br>
And i also tried to save the result of the landmark registration. But when i exported the transformated images as a dicom they are not transformed. They have the same orientation as before. Maybe you have an idea how i can save the transformed images as a dicom?</p>
<p>Best regards<br>
Solveig</p>

---

## Post #4 by @lassoan (2021-07-25 12:23 UTC)

<p>You may need to be harden the transform on the image before exporting it to DICOM.</p>
<p>From this much information it is hard to tell how to improve the registration. Wrong scale, too homogeneous images, too many b-spline control points, Elastix transform not read correctly (try if you get better result if you generate transformed moving image instead of getting an output transform and applying it to the moving image), etc. You could post a lot more screenshots, registration results you get by varying registration parameters, display the computed transform using Transforms module’s display section, but it would be much easier if you could just share an example pair of 3D images.</p>

---

## Post #5 by @Solli (2021-07-25 16:26 UTC)

<p>I tried different Presets from the Elastix Registration.<br>
In this picture is the result of the rigid all preset.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc47f93b01c46ab328106465c4fbca55506f0621.jpeg" data-download-href="/uploads/short-url/vqHfg8jei5bA3nY2It0jReBE7Nn.jpeg?dl=1" title="test1 rigid all" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc47f93b01c46ab328106465c4fbca55506f0621_2_678x500.jpeg" alt="test1 rigid all" data-base62-sha1="vqHfg8jei5bA3nY2It0jReBE7Nn" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc47f93b01c46ab328106465c4fbca55506f0621_2_678x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc47f93b01c46ab328106465c4fbca55506f0621_2_1017x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc47f93b01c46ab328106465c4fbca55506f0621.jpeg 2x" data-dominant-color="434240"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test1 rigid all</span><span class="informations">1207×889 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>here i tried generic all.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/988f7f25aff5ec905aa1fe7d7d76229e29539d9e.jpeg" data-download-href="/uploads/short-url/lLC0Ymx54OrvHGYtjkAkJyh87YG.jpeg?dl=1" title="ergebniss generic all" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988f7f25aff5ec905aa1fe7d7d76229e29539d9e_2_690x388.jpeg" alt="ergebniss generic all" data-base62-sha1="lLC0Ymx54OrvHGYtjkAkJyh87YG" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988f7f25aff5ec905aa1fe7d7d76229e29539d9e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988f7f25aff5ec905aa1fe7d7d76229e29539d9e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/988f7f25aff5ec905aa1fe7d7d76229e29539d9e_2_1380x776.jpeg 2x" data-dominant-color="7D7D7D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ergebniss generic all</span><span class="informations">1920×1080 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and here i tried an the 3D Ct, 3D MRI multimodal head and neck preset.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c28d41e62bd9c56f66285065e7d3c7070f174430.png" data-download-href="/uploads/short-url/rL5gR93rOm7fL29w98hMEaaE38k.png?dl=1" title="ergebniss1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c28d41e62bd9c56f66285065e7d3c7070f174430_2_690x371.png" alt="ergebniss1" data-base62-sha1="rL5gR93rOm7fL29w98hMEaaE38k" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c28d41e62bd9c56f66285065e7d3c7070f174430_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c28d41e62bd9c56f66285065e7d3c7070f174430_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c28d41e62bd9c56f66285065e7d3c7070f174430_2_1380x742.png 2x" data-dominant-color="6E6E6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ergebniss1</span><span class="informations">1904×1024 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Unfortunately at the moment i don’t know what i can do better in the elastix registration to receive better results. or is there another registration module which can solve my problem? sorry for all the questions but i am new in image registration.</p>

---

## Post #6 by @Solli (2021-07-25 18:08 UTC)

<p>I also tried the BRAINS General registration.<br>
When i used the settings Affine and useGeometryAlign and Affine and useCenterofHeadAlign it is cut of at the top and bottom.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c13eba7728e4502dc28cad24fbe2216804dbfa78.png" data-download-href="/uploads/short-url/rzwxTDG5t7ifOWFVIOPTtOCaMli.png?dl=1" title="brains registration, geometry align affine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c13eba7728e4502dc28cad24fbe2216804dbfa78_2_690x388.png" alt="brains registration, geometry align affine" data-base62-sha1="rzwxTDG5t7ifOWFVIOPTtOCaMli" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c13eba7728e4502dc28cad24fbe2216804dbfa78_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c13eba7728e4502dc28cad24fbe2216804dbfa78_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c13eba7728e4502dc28cad24fbe2216804dbfa78_2_1380x776.png 2x" data-dominant-color="696A6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">brains registration, geometry align affine</span><span class="informations">1920×1080 486 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/297a5fa6c02c6bf84af029be6fb51043d048cb93.jpeg" data-download-href="/uploads/short-url/5UVL9K2jvVXk9yIRTogOfG24lbl.jpeg?dl=1" title="brains registration, center of head align affine" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/297a5fa6c02c6bf84af029be6fb51043d048cb93_2_690x388.jpeg" alt="brains registration, center of head align affine" data-base62-sha1="5UVL9K2jvVXk9yIRTogOfG24lbl" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/297a5fa6c02c6bf84af029be6fb51043d048cb93_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/297a5fa6c02c6bf84af029be6fb51043d048cb93_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/297a5fa6c02c6bf84af029be6fb51043d048cb93_2_1380x776.jpeg 2x" data-dominant-color="7A7A7A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">brains registration, center of head align affine</span><span class="informations">1920×1080 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
