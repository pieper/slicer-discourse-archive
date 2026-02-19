---
topic_id: 2518
title: "Analysis With Spharm Pdm"
date: 2018-04-05
url: https://discourse.slicer.org/t/2518
---

# Analysis with SPHARM-PDM

**Topic ID**: 2518
**Date**: 2018-04-05
**URL**: https://discourse.slicer.org/t/analysis-with-spharm-pdm/2518

---

## Post #1 by @Pilar (2018-04-05 11:27 UTC)

<p>Hi 3D-Slicer users,</p>
<p>I am having problems using the SPHARM-PDM module. I read the user tutorial (May 2017) but when I apply the module, the status says completed with errors.</p>
<p>The purpose of my PhD is to make the comparison between two semi-mandibles (right and left) and find if there is any asymmetry. After doing all the previous steps, and using a voxel-based registration, I get the volume (.vtk) of each one and then I create a new file with the module Model to Model distance, getting the colormap file.</p>
<p>I try to do the SPHARM-PDM analysis with this file (colormap) to do the statistics in a simpler way, but I have errors. Probably it is because I am not clicking or selecting the correct parameters.</p>
<p>Can anybody help me?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2018-04-06 01:41 UTC)

<p><a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/laurapascal">@laurapascal</a> - could you help?</p>

---

## Post #3 by @timeanddoctor (2018-04-06 11:33 UTC)

<p>can you take a screen about what you did detaily?</p>

---

## Post #4 by @Pilar (2018-04-06 13:20 UTC)

<p>Yes, of course.</p>
<p>Firstly, I get the colormap file (.vtk), that It is attached below, using the Model to Model distance Module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3a8b5da8209a4986a1935242d35a2f97a5cb49a.png" data-download-href="/uploads/short-url/wtXQsldN1u6y1nDo5Z2Qi3NcaUi.png?dl=1" title="Captura de pantalla 2018-04-06 a las 15.11.06.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3a8b5da8209a4986a1935242d35a2f97a5cb49a_2_690x433.png" data-base62-sha1="wtXQsldN1u6y1nDo5Z2Qi3NcaUi" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3a8b5da8209a4986a1935242d35a2f97a5cb49a_2_690x433.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3a8b5da8209a4986a1935242d35a2f97a5cb49a_2_1035x649.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3a8b5da8209a4986a1935242d35a2f97a5cb49a.png 2x" data-dominant-color="BFBFDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2018-04-06 a las 15.11.06.png</span><span class="informations">1218×765 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then, I try to use the Shape Analysis Module but the status says “completed with errors”</p>
<p>Maybe, I am not clicking or selecting the correct parameters.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57325048e0e73bde0b42aeb3bbe05e8361845f95.png" data-base62-sha1="crnkQUBbw1Fs8jXTUyYMX1GMkv3" width="536" height="428"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffdafedc6cd4b2fd23d87c4f54547ca5966c42d5.png" data-download-href="/uploads/short-url/AvoWWKK2wmToYtlmiZLyxoLDIWx.png?dl=1" title="Captura de pantalla 2018-04-06 a las 15.13.26.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffdafedc6cd4b2fd23d87c4f54547ca5966c42d5_2_450x500.png" data-base62-sha1="AvoWWKK2wmToYtlmiZLyxoLDIWx" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffdafedc6cd4b2fd23d87c4f54547ca5966c42d5_2_450x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffdafedc6cd4b2fd23d87c4f54547ca5966c42d5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffdafedc6cd4b2fd23d87c4f54547ca5966c42d5.png 2x" data-dominant-color="EBECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2018-04-06 a las 15.13.26.png</span><span class="informations">543×602 43.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Pilar (2018-04-19 16:07 UTC)

<p>Hello users,</p>
<p>I was thinking about that maybe I don’t need to do the SPHARM-PDM again, because I already have a colormap file, done with the two models of the hemimandibles which were superimposed.</p>
<p>And that’s why the software says completed with errors.</p>
<p>Does anybody knows if it is correct?</p>
<p>On the other hand, I can see the basic statistics (mean, percentiles,…) as I attached bellow, but is is posible to get the file with all the numbers. I mean, the distance between every correspondent point</p>
<p>The file that says ValuesOnEachPoint is empty</p>
<p>Thank you in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f937f3e6443ee7e1c52e8347eefb8bfcf88d272c.png" data-download-href="/uploads/short-url/zyGLDpGBMhVmWx6GyZgPSwJzDR2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f937f3e6443ee7e1c52e8347eefb8bfcf88d272c_2_690x85.png" alt="image" data-base62-sha1="zyGLDpGBMhVmWx6GyZgPSwJzDR2" width="690" height="85" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f937f3e6443ee7e1c52e8347eefb8bfcf88d272c_2_690x85.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f937f3e6443ee7e1c52e8347eefb8bfcf88d272c_2_1035x127.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f937f3e6443ee7e1c52e8347eefb8bfcf88d272c_2_1380x170.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1748×216 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5cfdeac92d851b61f0b9e3d60ac2bbd004d81f4.png" data-download-href="/uploads/short-url/sdVq5ehfCbjNO8oDXUEExRXnfcU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cfdeac92d851b61f0b9e3d60ac2bbd004d81f4_2_578x500.png" alt="image" data-base62-sha1="sdVq5ehfCbjNO8oDXUEExRXnfcU" width="578" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cfdeac92d851b61f0b9e3d60ac2bbd004d81f4_2_578x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cfdeac92d851b61f0b9e3d60ac2bbd004d81f4_2_867x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5cfdeac92d851b61f0b9e3d60ac2bbd004d81f4_2_1156x1000.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1174×1014 71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
