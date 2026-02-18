# How to connect two video streams into slicer using plus server

**Topic ID**: 35611
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/how-to-connect-two-video-streams-into-slicer-using-plus-server/35611

---

## Post #1 by @David.Xu (2024-04-19 02:40 UTC)

<p>I have two cameras to access, how to achieve through plus server and openigtlinkif . The access of a single camera has been completed, how to modify the configuration parameters of plus server when accessing two cameras at the same time? The corresponding parameter file is PlusDeviceSet_Server_MmfColorVideoCapture.xml</p>

---

## Post #2 by @David.Xu (2024-04-19 06:15 UTC)

<p>I have successfully imported two video streams with a resolution of 640x480. However, when I adjusted the resolution of both streams to 1920x1080, the Plus Server failed to start. I need high-resolution images with a frame rate of 20fps. Is there a way to achieve this using Plus?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47d79201114007eb8a7b2af00e438442a1a8fb3b.png" data-download-href="/uploads/short-url/afxKYBqcagABR88DNwde1F1MlxV.png?dl=1" title="lQLPJwjA19L136XNBoPNCH6wUqQerLglyRMGDt3NzSWNAA_2174_1667" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d79201114007eb8a7b2af00e438442a1a8fb3b_2_652x499.png" alt="lQLPJwjA19L136XNBoPNCH6wUqQerLglyRMGDt3NzSWNAA_2174_1667" data-base62-sha1="afxKYBqcagABR88DNwde1F1MlxV" width="652" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d79201114007eb8a7b2af00e438442a1a8fb3b_2_652x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d79201114007eb8a7b2af00e438442a1a8fb3b_2_978x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47d79201114007eb8a7b2af00e438442a1a8fb3b_2_1304x998.png 2x" data-dominant-color="FCFAFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">lQLPJwjA19L136XNBoPNCH6wUqQerLglyRMGDt3NzSWNAA_2174_1667</span><span class="informations">2174×1667 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1019309f8e071b3d0adabc1af079c03dd53730a.jpeg" data-download-href="/uploads/short-url/tOXabWDKzTvAU6GtPLECOSAxMlY.jpeg?dl=1" title="lQLPKctkP61uL6XNBtbNC8OwxbAy-x77BJcGDt3NzSWNAQ_3011_1750" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1019309f8e071b3d0adabc1af079c03dd53730a_2_690x401.jpeg" alt="lQLPKctkP61uL6XNBtbNC8OwxbAy-x77BJcGDt3NzSWNAQ_3011_1750" data-base62-sha1="tOXabWDKzTvAU6GtPLECOSAxMlY" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1019309f8e071b3d0adabc1af079c03dd53730a_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1019309f8e071b3d0adabc1af079c03dd53730a_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1019309f8e071b3d0adabc1af079c03dd53730a_2_1380x802.jpeg 2x" data-dominant-color="E5E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">lQLPKctkP61uL6XNBtbNC8OwxbAy-x77BJcGDt3NzSWNAQ_3011_1750</span><span class="informations">1920×1116 597 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @David.Xu (2024-04-19 07:01 UTC)

<p>How to set frame rate in XML file.</p>

---

## Post #4 by @David.Xu (2024-04-19 11:19 UTC)

<p>When I use Plus to connect a 1080P camera, I find that the frame rate is quite low. However, when I connect the same 1080P camera directly using OpenCV, the frame rate is normal.</p>

---

## Post #5 by @Sunderlandkyl (2024-04-19 14:10 UTC)

<p>You can specify <strong>AcquisitionRate</strong> to change the desired framerate.</p>
<p><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html#DeviceAcquisitionRate" class="onebox" target="_blank" rel="noopener nofollow ugc">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html#DeviceAcquisitionRate</a></p>

---

## Post #6 by @David.Xu (2024-04-22 02:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37bd78d678091f78158afd7c071bf0b90011b165.png" data-download-href="/uploads/short-url/7X6czBut4lLXXE6CwgsTQYbi44Z.png?dl=1" title="1713753872690" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37bd78d678091f78158afd7c071bf0b90011b165_2_484x500.png" alt="1713753872690" data-base62-sha1="7X6czBut4lLXXE6CwgsTQYbi44Z" width="484" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37bd78d678091f78158afd7c071bf0b90011b165_2_484x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37bd78d678091f78158afd7c071bf0b90011b165_2_726x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37bd78d678091f78158afd7c071bf0b90011b165_2_968x1000.png 2x" data-dominant-color="F8F5F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1713753872690</span><span class="informations">1372×1417 93.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I add this parameter, but the frame rate is still low.</p>

---

## Post #7 by @David.Xu (2024-04-22 13:51 UTC)

<p>And I change VideoFormat to “NV12” and “MJPG”, but It doen’t work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84604e527a7c2d26c42b36ce8e2138510b02cb66.png" data-download-href="/uploads/short-url/iT3mmhTNtv14THyg33mKANBYlw2.png?dl=1" title="1713793762524" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84604e527a7c2d26c42b36ce8e2138510b02cb66_2_546x500.png" alt="1713793762524" data-base62-sha1="iT3mmhTNtv14THyg33mKANBYlw2" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84604e527a7c2d26c42b36ce8e2138510b02cb66_2_546x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84604e527a7c2d26c42b36ce8e2138510b02cb66_2_819x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84604e527a7c2d26c42b36ce8e2138510b02cb66_2_1092x1000.png 2x" data-dominant-color="FAF8FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1713793762524</span><span class="informations">1621×1482 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0c7aaba27659785dbba056ca8c328a87d0662a1.png" data-download-href="/uploads/short-url/w4uJJTQ77x1LnGcIkeg3zNW5TSp.png?dl=1" title="1713793790783" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c7aaba27659785dbba056ca8c328a87d0662a1_2_690x372.png" alt="1713793790783" data-base62-sha1="w4uJJTQ77x1LnGcIkeg3zNW5TSp" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c7aaba27659785dbba056ca8c328a87d0662a1_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c7aaba27659785dbba056ca8c328a87d0662a1_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0c7aaba27659785dbba056ca8c328a87d0662a1_2_1380x744.png 2x" data-dominant-color="FCEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1713793790783</span><span class="informations">2440×1317 509 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35bc4557a2ec0ebeabcfb495dfbf1e9e0f385c31.png" data-download-href="/uploads/short-url/7FmFOqAQ8BDOSpt1gkXT1RZOYEN.png?dl=1" title="1713793867911" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bc4557a2ec0ebeabcfb495dfbf1e9e0f385c31_2_644x499.png" alt="1713793867911" data-base62-sha1="7FmFOqAQ8BDOSpt1gkXT1RZOYEN" width="644" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bc4557a2ec0ebeabcfb495dfbf1e9e0f385c31_2_644x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bc4557a2ec0ebeabcfb495dfbf1e9e0f385c31_2_966x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35bc4557a2ec0ebeabcfb495dfbf1e9e0f385c31_2_1288x998.png 2x" data-dominant-color="FCEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1713793867911</span><span class="informations">1852×1437 399 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Sunderlandkyl (2024-04-22 13:55 UTC)

<p>Have you tried using the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpenCVVideo.html" rel="noopener nofollow ugc">OpenCVVideo device</a> to see if the performance is better?</p>

---

## Post #9 by @David.Xu (2024-04-22 13:58 UTC)

<p>Yes, the frame rate in opencv is 30FPS, but when using plus server is 5FPS.</p>

---
