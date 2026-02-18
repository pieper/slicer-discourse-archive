# How can I display the parametric map from multivolume analysis as a colormap?

**Topic ID**: 3589
**Date**: 2018-07-27
**URL**: https://discourse.slicer.org/t/how-can-i-display-the-parametric-map-from-multivolume-analysis-as-a-colormap/3589

---

## Post #1 by @Kyu_Sung_Choi (2018-07-27 00:36 UTC)

<p>Dear Dr.Fedorov,</p>
<p>Thank you for your awesome work and kind comments.<br>
However, I have another question using DSCMRIAnalysis module.<br>
How can I display the grayscale rCBV map acquired by DSCMRIAnalysis as a colormap?<br>
I obtained the grayscale rCBV map (attached below, upper) but want to display this rCBV map as a colormap.<br>
I think technicians usually upload the rCBV map as a colormap on PACS.<br>
Moreover, most papers upload their rCBV map as a colormap.<br>
Actually I use fslview, but it returns a colormap like the one I attached below (middle), which is a bit different from the ones in most papers (attached below, lower).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa90431dedc7ae7a5f9b6420007eeae5bfa544b0.png" alt="image" data-base62-sha1="zKArLIyeevKIOo6CGD7fb6torIc" width="331" height="356"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d23f10a777765389296de717956a456922cb373.png" alt="image" data-base62-sha1="8IS84hKuVyBnr1Eeq0aMKENnPnZ" width="306" height="321"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/006160e1dbf94a86d81e877bf1fe92cef01962fc.jpeg" alt="image" data-base62-sha1="3mDcMSe3JQnFbqZuTrA5aj15A8" width="241" height="270"><br>
Is there any recommendation or appropriate functions in DSCMRIAnalysis module?<br>
Thank you in advance!</p>
<p>All the best,<br>
Kyu Sung</p><aside class="quote" data-post="8" data-topic="3421">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-can-i-convert-dicom-series-to-nrrd-files-in-batch-mode/3421/8">How can I convert DICOM series to NRRD files in batch mode?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It could be that the extensions were not yet built/packaged at the time you tried. Looking at the dashboard <a href="http://slicer.cdash.org/index.php?project=SlicerPreview" rel="noopener nofollow ugc">here</a>, the package of DSCAnalysis extension is now ready, so you should try again.
  </blockquote>
</aside>


---

## Post #2 by @fedorov (2018-07-27 14:26 UTC)



---

## Post #3 by @fedorov (2018-07-27 14:28 UTC)

<p><a class="mention" href="/u/kyu_sung_choi">@Kyu_Sung_Choi</a> I made the topic public, since I do not see anything sensitive in the content, and I think other users might benefit from the answer.</p>
<p>The mapping from the image voxel values to the color is handled via a lookup table that every volume in Slicer has assigned. By default, scalar volumes are assigned grayscale color map. To change that, you should select “Volumes” module, and you can change the assigned lookup table. You can try the one “ColdToHotRainbow”.</p>

---

## Post #4 by @Kyu_Sung_Choi (2018-07-30 04:08 UTC)

<p>Okay, it works perfect.<br>
Thanks!</p>

---

## Post #5 by @tigerhu7 (2018-08-10 10:45 UTC)

<p>Hello speled,<br>
I got similar picture, I can get Ktrans in grey but not in color.<br>
Could you tell me how you managed that?<br>
Thank you so much!</p>
<p>-Tiger<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b987748383ccaa9177737b30de453fbc46837ac1.png" data-download-href="/uploads/short-url/qtgxGv2us2jNYqgb7XYaYiJnZVD.png?dl=1" title="aaa" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b987748383ccaa9177737b30de453fbc46837ac1_2_442x500.png" alt="aaa" data-base62-sha1="qtgxGv2us2jNYqgb7XYaYiJnZVD" width="442" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b987748383ccaa9177737b30de453fbc46837ac1_2_442x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b987748383ccaa9177737b30de453fbc46837ac1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b987748383ccaa9177737b30de453fbc46837ac1.png 2x" data-dominant-color="929192"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">aaa</span><span class="informations">633×716 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @fedorov (2018-08-10 14:45 UTC)

<p><a class="mention" href="/u/tigerhu7">@tigerhu7</a> I moved your question to the topic where this was answered earlier - please go to the topic on discourse, read above this post, and let us know if you have further questions.</p>

---

## Post #7 by @tigerhu7 (2018-08-13 00:58 UTC)

<p>Thank you so much !!</p>

---

## Post #8 by @tigerhu7 (2018-08-13 02:01 UTC)

<p>Dear Dr Fedorov,<br>
It worked, thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6a12253010e63914a1f84637f32d940a54fdbfd.png" data-download-href="/uploads/short-url/q3C7VeRCgMg3QR4qiwK8Edh3odv.png?dl=1" title="ppp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6a12253010e63914a1f84637f32d940a54fdbfd_2_493x499.png" alt="ppp" data-base62-sha1="q3C7VeRCgMg3QR4qiwK8Edh3odv" width="493" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6a12253010e63914a1f84637f32d940a54fdbfd_2_493x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6a12253010e63914a1f84637f32d940a54fdbfd_2_739x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6a12253010e63914a1f84637f32d940a54fdbfd.png 2x" data-dominant-color="666580"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ppp</span><span class="informations">813×824 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>May I ask you some additional questions?<br>
(1) on the volume module, I set the output ktrans image display-&gt;lookup table-&gt;ColdToHotRainbow, and illustrate image of a certain frame and Ktrans image together, the blue dim background (as is on the pic) is bit annoying. Is there a way to clear blue background?<br>
(2) for the ktrans map, I would like to get the exact value of each pixel (voxel), is there a way to extract the data?<br>
I read your previous conversation with <a href="https://discourse.slicer.org/u/kirezgik">kirezgik</a>, are those values Ktrans map, ve map values? If so, how could I extract them?</p><aside class="quote quote-modified" data-post="3" data-topic="622">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/kirezgik/48/202_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/how-to-analyze-dce-mri-data/622/3">How to analyze DCE-MRI data</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Thank you! I installed the extension and analyzed the data. This is the chart I got: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5b8b3083c118fb56768e6d9cf16619bfe62b3ccb.jpg" data-download-href="/uploads/short-url/d3PF2zYIrQwEeB5r86EIWSdkuyD.jpg?dl=1" title="PKmodeling.jpg" rel="noopener nofollow ugc">[image]</a> 
And  it autogenerates a DoubleArray file with an extension .mcsv and it includes this result: 

<a name="nolabels-1" class="anchor" href="#nolabels-1"></a>nolabels
0,5813.11,0 
6.94764e+006,4719.33,0 
1.38953e+007,4900.67,0 
2.08429e+007,5255.11,0 
2.77906e+007,5131.78,0 
3.47382e+007,5241.11,0 
4.16859e+007,5384.22,0 
4.86335e+007,4986.33,0 
5.55811e+007,5158.11,0 
6.25288e+007,5173.11,0 
6.94764e+007,5138.44,0 
7.64241e+007,5346.67,0 
8.33717e+007,6408.22,0 …
  </blockquote>
</aside>

<p>Sorry for my maybe silly questions, I am a newbie in 3DSlicer. I find this community is very nice and kind. And most of all, I am very grateful to all the contributors!!!</p>
<p>-Tiger Hu</p>

---

## Post #9 by @tigerhu7 (2018-08-13 06:48 UTC)

<p><a href="https://discourse.slicer.org/u/fedorov">fedorov</a></p>
<p>Dr Fedorov,<br>
To clear blue background, I figured out. Adjusting threshold makes it work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f683eb4d815b6f9fa65bf5c6505389ba3509626.png" data-download-href="/uploads/short-url/ib5YUN2fjwG6MPnSjrsXszt4fNY.png?dl=1" title="threshold" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f683eb4d815b6f9fa65bf5c6505389ba3509626_2_690x270.png" alt="threshold" data-base62-sha1="ib5YUN2fjwG6MPnSjrsXszt4fNY" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f683eb4d815b6f9fa65bf5c6505389ba3509626_2_690x270.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f683eb4d815b6f9fa65bf5c6505389ba3509626_2_1035x405.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f683eb4d815b6f9fa65bf5c6505389ba3509626_2_1380x540.png 2x" data-dominant-color="ABADB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">threshold</span><span class="informations">1381×541 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I still do not understand the values in .mcsv file.</p>
<p>-Tiger Hu</p>

---

## Post #10 by @fedorov (2018-08-13 13:53 UTC)

<aside class="quote no-group" data-username="tigerhu7" data-post="8" data-topic="3589">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tigerhu7/48/67201_2.png" class="avatar"> tigerhu7:</div>
<blockquote>
<p>I would like to get the exact value of each pixel (voxel)</p>
</blockquote>
</aside>
<p>When you save the Ktrans/ve map into a file (eg NRRD), it will contain values for each voxel arranged in a 3d array. You can use any software that supports specific format to get values at the individual voxels (e.g., Matlab, SimpleITK, itk-python). Where do you want to use that map?</p>

---

## Post #12 by @tigerhu7 (2018-08-13 14:16 UTC)

<p>Dr Fedorov,<br>
I would like to use this map in Matlab.<br>
Do I need special code to open it?<br>
Thanks,</p>
<p>-Tiger Hu</p>

---

## Post #13 by @fedorov (2018-08-13 14:19 UTC)

<p>Excellent, thank you for the details! In this case, you should look into the MatlabBridge extension. You can send the output of PkModeling directly into Matlab with minimum effort. I personally do not use Matlab and do not have a lot of experience, but everyone I know who tried it could figure out the usage from documentation.</p>
<p>Please see documentation here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge</a></p>
<p>I copy Andras who developed that module, and Sharon who is working with me and used it specifically with the DCE analysis functionality in Slicer: <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/speled">@speled</a>.</p>

---

## Post #14 by @tigerhu7 (2018-08-13 14:22 UTC)

<p>Dr Fedorov,<br>
Thank you so so much for your quick reply.<br>
I will read this document and give it a try.</p>
<p>-Tiger Hu</p>

---
