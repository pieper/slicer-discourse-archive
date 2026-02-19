---
topic_id: 622
title: "How To Analyze Dce Mri Data"
date: 2017-07-04
url: https://discourse.slicer.org/t/622
---

# How to analyze DCE-MRI data

**Topic ID**: 622
**Date**: 2017-07-04
**URL**: https://discourse.slicer.org/t/how-to-analyze-dce-mri-data/622

---

## Post #1 by @kirezgik (2017-07-04 19:49 UTC)

<p>Operating system: Microsoft Windows 7 Enterprise<br>
Slicer version: Slicer 4.7.0 nightly build<br>
Expected behavior: Quantitative analysis of DCE MRI and measuring parameters like K trans and fractional value<br>
Actual behavior: Is there a way to do the quantitative analysis of DCE MRI of pancreatic tumor? I can only do semiquantitative analysis and create the plotting chart which shows the time-signal intensity curves of different ROIs, as it is discussed in this tutorial:</p>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf" target="_blank" rel="nofollow noopener">MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf</a></h3>

<p class="filesize">1984.43 KB</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks.</p>

---

## Post #2 by @fedorov (2017-07-05 15:25 UTC)

<p>This functionality is provided in a separate extension: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/PkModeling">https://www.slicer.org/wiki/Documentation/Nightly/Modules/PkModeling</a></p>

---

## Post #3 by @kirezgik (2017-07-20 15:54 UTC)

<p>Thank you! I installed the extension and analyzed the data. This is the chart I got:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5b8b3083c118fb56768e6d9cf16619bfe62b3ccb.jpg" data-download-href="/uploads/short-url/d3PF2zYIrQwEeB5r86EIWSdkuyD.jpg?dl=1" title="PKmodeling.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5b8b3083c118fb56768e6d9cf16619bfe62b3ccb_2_690x398.jpg" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5b8b3083c118fb56768e6d9cf16619bfe62b3ccb_2_690x398.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5b8b3083c118fb56768e6d9cf16619bfe62b3ccb_2_1035x597.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5b8b3083c118fb56768e6d9cf16619bfe62b3ccb_2_1380x796.jpg 2x" data-dominant-color="C1C1CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PKmodeling.jpg</span><span class="informations">1726×997 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And  it autogenerates a DoubleArray file with an extension .mcsv and it includes this result:</p>
<h1><a name="p-2851-nolabels-1" class="anchor" href="#p-2851-nolabels-1" aria-label="Heading link"></a>nolabels</h1>
<p>0,5813.11,0<br>
6.94764e+006,4719.33,0<br>
1.38953e+007,4900.67,0<br>
2.08429e+007,5255.11,0<br>
2.77906e+007,5131.78,0<br>
3.47382e+007,5241.11,0<br>
4.16859e+007,5384.22,0<br>
4.86335e+007,4986.33,0<br>
5.55811e+007,5158.11,0<br>
6.25288e+007,5173.11,0<br>
6.94764e+007,5138.44,0<br>
7.64241e+007,5346.67,0<br>
8.33717e+007,6408.22,0<br>
9.03193e+007,8021.33,0<br>
9.7267e+007,9395.11,0<br>
1.04215e+008,10528.4,0<br>
1.11162e+008,11141.3,0<br>
1.1811e+008,11415.9,0<br>
1.25058e+008,11819.1,0<br>
1.32005e+008,12122.1,0<br>
1.38953e+008,12290.1,0<br>
1.459e+008,13023.7,0<br>
1.52848e+008,13199.8,0<br>
1.59796e+008,13763.8,0<br>
1.66743e+008,13793.6,0<br>
1.73691e+008,14089.1,0<br>
1.80639e+008,14338.1,0<br>
1.87586e+008,15036.4,0<br>
1.94534e+008,14694.1,0<br>
2.01482e+008,14811.1,0<br>
2.08429e+008,15017.1,0<br>
2.15377e+008,15197.2,0<br>
2.22325e+008,15255.7,0<br>
2.29272e+008,15586.6,0<br>
2.3622e+008,15690.2,0<br>
2.43167e+008,15757.6,0<br>
2.50115e+008,15632.6,0<br>
2.57063e+008,15837.7,0<br>
2.6401e+008,16271.6,0<br>
2.70958e+008,16341.7,0<br>
2.77906e+008,16426.1,0<br>
2.84853e+008,15834.7,0<br>
2.91801e+008,16637.7,0<br>
2.98749e+008,16571.2,0<br>
3.05696e+008,16795.2,0<br>
3.12644e+008,16796.2,0<br>
3.19592e+008,17083.7,0<br>
3.26539e+008,17202.4,0<br>
3.33487e+008,17062.8,0<br>
3.40434e+008,17013.9,0<br>
3.47382e+008,17579.1,0<br>
3.5433e+008,17424.3,0<br>
3.61277e+008,17485.4,0<br>
3.68225e+008,17526.3,0<br>
3.75173e+008,17495,0<br>
3.8212e+008,17643.1,0<br>
3.89068e+008,17620,0<br>
3.96016e+008,17980,0<br>
4.02963e+008,17697,0<br>
4.09911e+008,17534.4,0<br>
4.16859e+008,17951.7,0<br>
4.23806e+008,18114.4,0<br>
4.30754e+008,17758.4,0<br>
4.37701e+008,17475.2,0<br>
4.44649e+008,18047.6,0<br>
4.51597e+008,18049.3,0<br>
4.58544e+008,18114.2,0<br>
4.65492e+008,18143.8,0<br>
4.7244e+008,17907.7,0<br>
4.79387e+008,18021.4,0<br>
4.86335e+008,18113.4,0<br>
4.93283e+008,18072.1,0<br>
5.0023e+008,18285.4,0<br>
5.07178e+008,18129,0<br>
5.14126e+008,18383.8,0<br>
5.21073e+008,18435.2,0<br>
5.28021e+008,18395.6,0<br>
5.34968e+008,18353.1,0<br>
5.41916e+008,18423.4,0<br>
5.48864e+008,18134.6,0<br>
5.55811e+008,18456.9,0<br>
5.62759e+008,18157.1,0<br>
5.69707e+008,18588,0<br>
5.76654e+008,18521.9,0<br>
5.83602e+008,18377.3,0<br>
5.9055e+008,18373.1,0<br>
5.97497e+008,18445.3,0<br>
6.04445e+008,18636.2,0<br>
6.11393e+008,18641,0<br>
6.1834e+008,18625.8,0</p>
<p>Is this what we are supposed to get? It`d be very helpful to see a module including the steps for analysis and the parameters.</p>
<p>Thanks.</p>

---

## Post #4 by @fedorov (2017-07-26 19:42 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> sorry for the late response.</p>
<p>When you analyze this kind of data, you typically are interested in the Ktrans and ve maps that it produces. You can, for example, look at the changes in Ktrans to evaluate response to therapy, as done in <a href="http://www.sciencedirect.com/science/article/pii/S1936523314800193">this paper</a>, for example (tool labeled “BWH-3D Slicer” in that paper is PkModeling).</p>
<p>The parameters are documented on this page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/PkModeling">https://www.slicer.org/wiki/Documentation/Nightly/Modules/PkModeling</a>. The most important parameters that you probably would need to change are “T1 Tissue value” (since the default is the estimated tissue value for human healthy prostate - you would need to do some literature review to see what value makes sense to use in your case) and “r1 Relaxivity Value of the contrast agent” (you can consult the referenced publication and choose the value that corresponds to the contrast agent used in your acquisition).</p>
<p>You should also experiment with manually defined AIF by creating a label corresponding to the vessel closest to the area you want to analyze, and passing that label as “AIF Mask image” parameter.</p>

---

## Post #5 by @kirezgik (2017-08-16 16:37 UTC)

<p>Thank you for your response and suggestions <a class="mention" href="/u/fedorov">@fedorov</a>. The paper and documentation for PkModeling helped us quite a lot. We changed the parameters as you suggested and created labels using Editor module but it did not create any Ktrans map as an output. In parameters and IO section, do we need change anything?  While creating labels, we labeled multiple slices, do we supposed to label 1 slice only instead?</p>
<p>I`d appreciate your feedback.<br>
Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fcac4b75142e4ba1aad1e919eaed207e4edc403.png" data-download-href="/uploads/short-url/2fHAFkDFuYlx2o4Uy46MHeXm1B9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcac4b75142e4ba1aad1e919eaed207e4edc403_2_690x353.png" alt="image" data-base62-sha1="2fHAFkDFuYlx2o4Uy46MHeXm1B9" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcac4b75142e4ba1aad1e919eaed207e4edc403_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcac4b75142e4ba1aad1e919eaed207e4edc403_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcac4b75142e4ba1aad1e919eaed207e4edc403_2_1380x706.png 2x" data-dominant-color="B7B6B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1883×966 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @fedorov (2017-08-16 16:41 UTC)

<aside class="quote no-group" data-username="kirezgik" data-post="5" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kirezgik/48/202_2.png" class="avatar"> kirezgik:</div>
<blockquote>
<p>it did not create any Ktrans map as an output</p>
</blockquote>
</aside>
<p>Looking at the screenshot you shared - it did create the output Ktrans. Did you try to change window/level?</p>
<p>With Ktrans map the range is very small, so it can be tricky sometime to set it up properly using the mouse. You can use Volumes module to set Window to something like 5, and Level to 2.5 and see if it helps.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2e7ce1d1eafe12865c76958976557f8306464d1.png" data-download-href="/uploads/short-url/yEQbESkskkXhwc7bXdtS81RypKF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2e7ce1d1eafe12865c76958976557f8306464d1_2_470x500.png" alt="image" data-base62-sha1="yEQbESkskkXhwc7bXdtS81RypKF" width="470" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2e7ce1d1eafe12865c76958976557f8306464d1_2_470x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2e7ce1d1eafe12865c76958976557f8306464d1_2_705x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2e7ce1d1eafe12865c76958976557f8306464d1.png 2x" data-dominant-color="F3F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">890×945 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @kirezgik (2017-08-17 20:50 UTC)

<p>Yes, we tried changing the window level but it did not work. The biggest values for Window is 0.12 and for Level 0.05 as you can see in the screenshot below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6f628b5e564c26499e758eb7337a72a24db9e6a.png" data-download-href="/uploads/short-url/q6yi9UE9axQL0CKPWTnTekQymTg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6f628b5e564c26499e758eb7337a72a24db9e6a_2_690x347.png" alt="image" data-base62-sha1="q6yi9UE9axQL0CKPWTnTekQymTg" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6f628b5e564c26499e758eb7337a72a24db9e6a_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6f628b5e564c26499e758eb7337a72a24db9e6a_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6f628b5e564c26499e758eb7337a72a24db9e6a_2_1380x694.png 2x" data-dominant-color="939393"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1799×905 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I`d like to send the link for this image file, in case you might want to test:<br>
<a href="https://mdacc.box.com/s/1wtmtcz83b5qqb225mmbntd291n2c9da" class="onebox" target="_blank" rel="noopener nofollow ugc">https://mdacc.box.com/s/1wtmtcz83b5qqb225mmbntd291n2c9da</a></p>
<p>Thanks.</p>

---

## Post #8 by @fedorov (2017-08-18 14:22 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> I can’t access the file at the link you shared</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2421f0ad365ea1a2cae18959173efc9c2eb799b.jpeg" alt="image" data-base62-sha1="pqWExwPB4jiWUTQdIKHTgAogUjx" width="464" height="466"></p>

---

## Post #9 by @fedorov (2017-08-18 14:46 UTC)

<aside class="quote no-group" data-username="kirezgik" data-post="7" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kirezgik/48/202_2.png" class="avatar"> kirezgik:</div>
<blockquote>
<p>Yes, we tried changing the window level but it did not work. The biggest values for Window is 0.12 and for Level 0.05 as you can see in the screenshot below.</p>
</blockquote>
</aside>
<p>Also, just in case you didn’t realize this - the map will only be initialized inside the ROI you prescribed. In the screenshot you shared, the ROI is covered with the label overlay. You will need to hide the ROI overlay to see the map.</p>

---

## Post #10 by @kirezgik (2017-08-18 15:20 UTC)

<p>Sorry, I just sent an invitation for the shared folder. You should be able to have access now.<br>
When I hide the overlay, this is the map I can see:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a770aa00cf1b174faaeed807113db8a6c7cb78.png" data-download-href="/uploads/short-url/xc9vJI051OyiU8dxKfmCvvz62PS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8a770aa00cf1b174faaeed807113db8a6c7cb78_2_690x347.png" alt="image" data-base62-sha1="xc9vJI051OyiU8dxKfmCvvz62PS" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8a770aa00cf1b174faaeed807113db8a6c7cb78_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8a770aa00cf1b174faaeed807113db8a6c7cb78_2_1035x520.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8a770aa00cf1b174faaeed807113db8a6c7cb78_2_1380x694.png 2x" data-dominant-color="8E8E8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1795×903 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @fedorov (2017-08-18 16:28 UTC)

<p>I only see the input DICOM series in the folder you shared.</p>
<p>About the visualization, most likely it is just the case that you need a very narrow window to see the variation. Try moving the mouse around the ROI to get a feeling of the true range of data within the ROI. Even better, you can run LabelStatistics module setting your ROI as segmentation, and Ktrans as input image. Then adjust W/L setting based on the min/max you get from LabelStatistics.</p>

---

## Post #12 by @kirezgik (2017-08-22 20:11 UTC)

<p>Hi, I shared the DCEMRI KTrans map file too. Also I just uploaded a ppt which shows the steps we have been applying. There must be something wrong with either the data itself or the analysis process we are following.</p>

---

## Post #13 by @fedorov (2017-08-22 23:39 UTC)

<p>Thanks for sharing the data, that really helps.</p>
<p>Indeed, there is a problem with the analysis.</p>
<p>To investigate this issue, I created concentration-converted multivolume for the dataset, and saved the fitted curve as shown below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5221e310481868735837e634f1c262348cc642dc.png" data-download-href="/uploads/short-url/bIzKOu7X99kHVcf2AI0GROcjNwM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5221e310481868735837e634f1c262348cc642dc_2_599x500.png" alt="image" data-base62-sha1="bIzKOu7X99kHVcf2AI0GROcjNwM" width="599" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5221e310481868735837e634f1c262348cc642dc_2_599x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5221e310481868735837e634f1c262348cc642dc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5221e310481868735837e634f1c262348cc642dc.png 2x" data-dominant-color="F1F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">889×741 81.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Once this is done, these two multivolumes can be selected in Multivolume Explorer to visually evaluate the quality of the fit, which shows that indeed that fit does not make any sense.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/673ac5ba34e4fe7d3a5a6e1c1e5deb59fb133d76.png" data-download-href="/uploads/short-url/eJd67l5e0iDWPYugyFK8mNSbFXw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/673ac5ba34e4fe7d3a5a6e1c1e5deb59fb133d76.png" alt="image" data-base62-sha1="eJd67l5e0iDWPYugyFK8mNSbFXw" width="690" height="404" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">882×517 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At this point, I don’t know what is going on.</p>
<p>One thing I see immediately is that the region you marked as “blood” does not seem to correspond to a feeding artery. You should see a characteristic sharp early uptake in the blood vessel region, more like the area highlighted with crosshairs in the screenshot below. But when I try that, I don’t get results that make much more sense.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1f4c9179869e943a5ec74133151228a938da414.jpeg" data-download-href="/uploads/short-url/tXmeZLhTose5DgnKEHssbyQUWlm.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d1f4c9179869e943a5ec74133151228a938da414_2_690x415.jpg" alt="image" data-base62-sha1="tXmeZLhTose5DgnKEHssbyQUWlm" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d1f4c9179869e943a5ec74133151228a938da414_2_690x415.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d1f4c9179869e943a5ec74133151228a938da414_2_1035x622.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d1f4c9179869e943a5ec74133151228a938da414_2_1380x830.jpg 2x" data-dominant-color="ADADAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1493×898 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure when I will have time to investigate in more detail, but I will ask some people working with me to see if they can look into it.</p>

---

## Post #14 by @kirezgik (2017-09-19 17:09 UTC)

<p>Hi again!<br>
Could you have time to investigate the issue more detailed or ask someone? We wonder if it is really related with our DICOM dataset as <a class="mention" href="/u/malaterre">@malaterre</a> mentioned in <code>ERROR with DCE MRI loading in DICOM Browser</code> case or the analysis route or modules.</p>

---

## Post #15 by @fedorov (2017-09-19 21:50 UTC)

<p>I am pretty sure it is unrelated to the loading of DICOM, but to the analysis process. I asked <a class="mention" href="/u/mschwier">@mschwier</a> to look into this, but I don’t know if he had time…</p>

---

## Post #16 by @mschwier (2017-09-19 22:36 UTC)

<p>I’m sorry, I got sucked into some other issues and forgot about looking into this one. I’ll run it through a debugger the next days and see if I see smth.</p>

---

## Post #17 by @mschwier (2017-09-25 19:30 UTC)

<p>Something that strikes me as unusual in the input data: The trigger times span a time frame of more than 600.000.000 ms, which is about a week. With 90 frames the interval between two frames is about 2 hours. Is that correct?</p>

---

## Post #18 by @fedorov (2017-09-25 19:52 UTC)

<p><a class="mention" href="/u/mschwier">@mschwier</a> indeed, this can’t be correct! That’s a good lead …</p>

---

## Post #19 by @mschwier (2017-09-25 20:10 UTC)

<p>I’m trying to see smth in the debugger with the unusual trigger times in mind. <a class="mention" href="/u/kirezgik">@kirezgik</a>, if you have any info about the trigger times in the data or could double check your data with regard to this, that would be great.</p>

---

## Post #20 by @fedorov (2017-09-25 22:09 UTC)

<p><a class="mention" href="/u/mschwier">@mschwier</a> I think we should figure out the temporal resolution first.</p>
<p><a class="mention" href="/u/kirezgik">@kirezgik</a> can you please let us know (or ask the manufacturer of the equipment) how to properly interpret the temporal resolution of this DCE acquisition from the DICOM data they generate?</p>
<p>Basically, when we parse DCE series, we look for certain attributes to provide information about time stamps for the individual time frames. In this particular case, TriggerTime appears to be the attribute that seems to indicate time, but it jumps from 0 to 9074472.1875 for the second time frame. According to the standard, TriggerTime units is msec, and in the case of your data it does not appear to be the case.</p>

---

## Post #21 by @mschwier (2017-09-26 13:38 UTC)

<p>Temporal Resolution (0020,0110) is 77196.0256347656 ≈ 1,29 minutes according to the DICOM tags. This seems more reasonable.</p>

---

## Post #22 by @fedorov (2017-09-26 13:48 UTC)

<p>Indeed, but not “reasonable enough”. Temporal resolution should be on the order of 5 sec (the smaller the better) for a meaningful analysis. 1.29 min can’t be right, we would not see the dynamics we see in the data with that resolution.</p>

---

## Post #23 by @kirezgik (2017-09-26 15:15 UTC)

<p>Hi,<br>
Thanks <a class="mention" href="/u/mschwier">@mschwier</a> and <a class="mention" href="/u/fedorov">@fedorov</a>  for your investigations. I`ve just contacted with someone who oversees the MRI equipment. He said the following:</p>
<ol>
<li>The images are not gated so you can ignore the trigger times.</li>
<li>The DICOM headers from this system aren’t always perfectly accurate.</li>
<li>The temporal resolution will be the TR x the number of phase encoding repetitions. (You’ll have to check the TR for each individial DCE scan because most are 53.335 but some are 69.746 because there were more slices added to the slice package) To calculate the temporal resolution it would be 53.335 x 96= 5120.16 ms.</li>
</ol>

---

## Post #24 by @mschwier (2017-10-03 22:01 UTC)

<p>Hi <a class="mention" href="/u/kirezgik">@kirezgik</a>,</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> changed the temporal resolution manually to see if this fixes the problem. Unfortunately the curve fitting still looks as wrong as before. This means we’ll have to debug deeper into the computations to see what is the cause for this. We’ll try to extract a tiny sample from your image and see if we can reproduce the error with this sample. With a small sample it is a bit easier to retrace the computations.</p>

---

## Post #25 by @speled (2017-10-12 23:10 UTC)

<p>Hello!<br>
I had a look at the data. First of all, I could not visually identify any ROIs that could be used to define the AIF, so possibly you may need to estimate that. Just for testing, I used some voxels that exhibited AIF characteristics (sharp peak etc.) but were probably more related to motion than to blood vessels.<br>
With this ‘AIF’ I was able to calculate a Ktrans map in the kidney - see below - albeit the values were higher than expected, probably due to the AIF being extremely innaccurate, and the T1 values unknown. Remember to input a BAT frame number in the Advanced options. The Output Fitted data did not align with the actual data but perhaps that is a problem with the fitted data output of the module and not with the fitting procedure. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ceb795396ed09ad2b559dc8877916c4d5c95cddf.jpeg" data-download-href="/uploads/short-url/tuHGnhXqmWxPmxlEe26F6fu6V4P.jpg?dl=1" title="49 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ceb795396ed09ad2b559dc8877916c4d5c95cddf_2_690x416.jpg" alt="49 PM" data-base62-sha1="tuHGnhXqmWxPmxlEe26F6fu6V4P" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ceb795396ed09ad2b559dc8877916c4d5c95cddf_2_690x416.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ceb795396ed09ad2b559dc8877916c4d5c95cddf_2_1035x624.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ceb795396ed09ad2b559dc8877916c4d5c95cddf_2_1380x832.jpg 2x" data-dominant-color="B5A2A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">49 PM</span><span class="informations">3104×1872 770 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Sharon</p>

---

## Post #26 by @speled (2017-10-19 21:18 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a>, <a class="mention" href="/u/fedorov">@fedorov</a> and <a class="mention" href="/u/mschwier">@mschwier</a> - I did find some vessels for the AIF and analyzed the mouse data using my own DCE analysis program using MatlabBridge in Slicer and the results look fine - see below Ktrans map and fitted data graph. After giving it some more thought, I think that in the PkModeling module perhaps the function that generates the fitted data reads parameters from the Bruker perfusion dataset header incorrectly e.g. reads the sequence TR in msec when it is expecting seconds or something like that.<br>
-Sharon<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f185606bec24ff58b031bae71bf0b5e5ffdc8585.png" data-download-href="/uploads/short-url/ysAPmQWMpXNp1kItQsOIetoEj0p.png?dl=1" title="05 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185606bec24ff58b031bae71bf0b5e5ffdc8585_2_690x405.png" alt="05 PM" data-base62-sha1="ysAPmQWMpXNp1kItQsOIetoEj0p" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185606bec24ff58b031bae71bf0b5e5ffdc8585_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185606bec24ff58b031bae71bf0b5e5ffdc8585_2_1035x607.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f185606bec24ff58b031bae71bf0b5e5ffdc8585_2_1380x810.png 2x" data-dominant-color="939293"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">05 PM</span><span class="informations">1692×994 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #27 by @kirezgik (2017-10-30 19:07 UTC)

<p>Hi Sharon <a class="mention" href="/u/speled">@speled</a>,</p>
<p>Based on the ROIs we identified, it seems difficult to define the AIF manually because of the small spatial dimensions or the location of the tumor in mice. So we will try to use some proposed algoritms to automatically define the AIFs, that way we can have a more accurate AIF and Ktrans map, hopefully.<br>
Could you please share the Matlab script you used for your analysis? Then we can try it here in our Slicer.</p>
<p>Thanks for your help,<br>
Ezgi</p>

---

## Post #28 by @Jin (2017-12-04 07:51 UTC)

<p>Hi. fedorov!<br>
How can I change the original DCE-MR datas into MRMLMultiVolume, and when I use the MultiVolumeImporter to get the data, but I don’t kown how to fill in the parameters in advanced setting, thanks very much!</p>

---

## Post #29 by @fedorov (2017-12-04 16:45 UTC)

<aside class="quote no-group" data-username="Jin" data-post="28" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/4af34b/48.png" class="avatar"> Jin:</div>
<blockquote>
<p>How can I change the original DCE-MR datas into MRMLMultiVolume</p>
</blockquote>
</aside>
<p>You need to load the DICOM series from the DICOM Browser module. How do you load the data right now and what happens?</p>
<aside class="quote no-group" data-username="Jin" data-post="28" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/4af34b/48.png" class="avatar"> Jin:</div>
<blockquote>
<p>and when I use the MultiVolumeImporter to get the data, but I don’t kown how to fill in the parameters in advanced setting, thanks very much!</p>
</blockquote>
</aside>
<p>Which parameter are you trying to set? All except the first two are for creating output volumes. “Constant BAT” applies only to UseCostantBAT, and should be set to the multivolume frame where you see the beginning of the contrast uptake.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7209d5ef151b5258c65e4c1a8f29c9e928668438.png" alt="image" data-base62-sha1="ggPvhd075xPZEueHnEnyjL19xRS" width="617" height="228"></p>

---

## Post #30 by @Jin (2017-12-05 13:23 UTC)

<p>Thanks for help！When I use the MultiVolumeImporter to acquire the 4D image, I get some parameter like RE, RT and FA, etc, but I don’t know the Initial value, step, Frame identifying DICOM tag, how can I get those parameter?<br>
The original DICOM data contain 1920 slices, and 60 frames. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa9cf999a56d98551549aeed83bf9b142ab93c77.png" data-download-href="/uploads/short-url/oljudqydbz3ld3GpfuPBRZYZ6uz.png?dl=1" title="1512479061(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9cf999a56d98551549aeed83bf9b142ab93c77_2_690x370.png" alt="1512479061(1)" data-base62-sha1="oljudqydbz3ld3GpfuPBRZYZ6uz" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9cf999a56d98551549aeed83bf9b142ab93c77_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9cf999a56d98551549aeed83bf9b142ab93c77_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa9cf999a56d98551549aeed83bf9b142ab93c77_2_1380x740.png 2x" data-dominant-color="939398"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1512479061(1)</span><span class="informations">1920×1031 84.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Can I send the data to you?</p>

---

## Post #31 by @Jin (2017-12-05 13:32 UTC)

<p>And when I load the data from the DICOM Browser, I get some deformation images, and it can not be used in pkmodeling.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa4af88d19a55e7e9af5bdceff34611a627387c6.png" data-download-href="/uploads/short-url/zIbZvmO8UAbvFj2CYZyx7nQ2eFg.png?dl=1" title="c" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa4af88d19a55e7e9af5bdceff34611a627387c6_2_690x370.png" alt="c" data-base62-sha1="zIbZvmO8UAbvFj2CYZyx7nQ2eFg" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa4af88d19a55e7e9af5bdceff34611a627387c6_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa4af88d19a55e7e9af5bdceff34611a627387c6_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa4af88d19a55e7e9af5bdceff34611a627387c6_2_1380x740.png 2x" data-dominant-color="97979D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">c</span><span class="informations">1920×1031 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #32 by @fedorov (2017-12-05 18:00 UTC)

<p>Sure, you can send me your de-identified dataset and I can take a look.</p>

---

## Post #33 by @fedorov (2017-12-13 20:02 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> we are preparing for the NA-MIC Project week that will take place at MIT Jan 8-12 (see <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston">https://na-mic.github.io/ProjectWeek/PW27_2018_Boston</a>). We will have a focused project to investigate issues in PkModeling, and will specifically look into the issues that are reproducible with the dataset you kindly shared (see specific project here: <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/ModelFittingTools/">https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/ModelFittingTools/</a>).</p>
<p>You are more than welcome to join project week - this will give you a great opportunity to learn more about Slicer,  work with the developers, and refine Slicer DCE analysis implementation. We would be very happy to see you at the project week!</p>
<p>If you are not there, following the project week we should have more understanding, if not the solution, to the problems you identified.</p>

---

## Post #34 by @kirezgik (2018-01-08 16:41 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a>, I am sorry I missed this message and have not seen earlier. I could not join anyways, but I appreciate your effort and helps to solve this issue. Hope you can have a better idea and maybe solution to that at the end of the project week. I look forward to hearing your updates soon.<br>
Thanks.</p>

---

## Post #35 by @kirezgik (2018-05-10 19:04 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a>, I was wondering if you have any updates regarding to this issue.</p>

---

## Post #36 by @fedorov (2018-05-12 19:12 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> no, unfortunately we do not have any new results. <a class="mention" href="/u/speled">@speled</a> and <a class="mention" href="/u/mschwier">@mschwier</a> did not identify the issue at the project week, and I have not been able to make time to investigate this myself. I am sorry!</p>
<p>Are you a developer yourself? Would you be comfortable investigating this issue? We could perhaps give you some pointers?</p>

---

## Post #37 by @speled (2018-05-14 13:08 UTC)

<p>Hello <a class="mention" href="/u/kirezgik">@kirezgik</a>, (cc: <a class="mention" href="/u/fedorov">@fedorov</a>,<a class="mention" href="/u/mschwier">@mschwier</a>)<br>
The issue is probably not in the PK Modeling module, but in the multivolume loading of Bruker data - specifically in recognition of the frametime. I will probably be working on correcting this during Project Week in June. I do not have your problematic original data anymore - if you share it I think I can send you a solution.<br>
all best<br>
Sharon</p>

---

## Post #38 by @kirezgik (2018-05-14 15:18 UTC)

<p>Hi, I am not a developer myself, so I`d appreciate your help for that. <a class="mention" href="/u/speled">@speled</a>  I just shared the original data with you.<br>
Thanks,<br>
Ezgi</p>

---

## Post #39 by @speled (2018-05-15 13:57 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a> (cc: <a class="mention" href="/u/fedorov">@fedorov</a>)<br>
After you load the multivolume data, and save it (e.g. as .nhdr and .raw.gz) look at this field:<br>
MultiVolume.FrameLabels:=0.0,9074472.1875,18148944.375,27223416.5625,…<br>
This is a list of 90 values, and here it looks like the frametime is 9074472.1875 milliseconds, i.e. 151 minutes!<br>
The frametime is usually in the range of 1-8 seconds…<br>
Here’s how to correct this manually in the .nhdr file.</p>
<p>In the Slicer Dicom browser, highlight your DCE dataset and click the ‘metadata’ button at the bottom. You will see these fields:<br>
0018,0080	RepetitionTime	65.64288<br>
0018,0089	NumberOfPhaseEncodingSteps   96<br>
Usually, the frametime in 2D sequences is the Repetition Time multiplied by the phase encoding steps. In this case that would be 6.3017 seconds.<br>
So you should replace the FrameLabels list in the .nhdr file by 0,6301.7,etc…<br>
Here is a Matlab script that generates the new list:<br>
TR=65.6429;<br>
numtimepoints=90;<br>
PE=96;<br>
%-----<br>
framelabels=[0:TR<em>PE:TR</em>PE*(numtimepoints-1)];<br>
newstring=sprintf(’%0.3f,’,framelabels);<br>
% take off final comma…<br>
newstring=newstring(1:end-1)</p>
<p>Let me know how this works for you?<br>
all best<br>
Sharon</p>

---

## Post #40 by @fedorov (2018-05-15 14:12 UTC)

<p><a class="mention" href="/u/speled">@speled</a> the issue of temporal resolution has already been discussed - see this post: <a href="https://discourse.slicer.org/t/how-to-analyze-dce-mri-data/622/23" class="inline-onebox">How to analyze DCE-MRI data - #23 by kirezgik</a>. That did not help.</p>
<aside class="quote no-group" data-username="kirezgik" data-post="23" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kirezgik/48/202_2.png" class="avatar"> kirezgik:</div>
<blockquote>
<p>The temporal resolution will be the TR x the number of phase encoding repetitions. (You’ll have to check the TR for each individial DCE scan because most are 53.335 but some are 69.746 because there were more slices added to the slice package) To calculate the temporal resolution it would be 53.335 x 96= 5120.16 ms.</p>
</blockquote>
</aside>

---

## Post #41 by @speled (2018-05-15 14:29 UTC)

<p><a class="mention" href="/u/kirezgik">@kirezgik</a>, <a class="mention" href="/u/fedorov">@fedorov</a> - so what is the problem? PK Modeling works for me with this data set.<br>
What does not work is the “Output Fitted Data 4D” feature.</p>

---

## Post #42 by @fedorov (2018-05-17 18:12 UTC)

<aside class="quote no-group" data-username="speled" data-post="41" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/speled/48/1554_2.png" class="avatar"> speled:</div>
<blockquote>
<p>PK Modeling works for me with this data set.</p>
</blockquote>
</aside>
<p>I did not realize this was the case. What AIF did you use?</p>

---

## Post #43 by @speled (2018-05-17 18:30 UTC)

<p>Hi – sorry I was not aware that the frame time issue had been figured out (since it was not brought up when we discussed Andrew and Jihun’s mouse data).</p>
<p>Attached is the AIF label map that I used – voxels found using an automated algorithm applied to an artery.</p>
<p>Best</p>
<p>Sharon</p>

---

## Post #44 by @fedorov (2018-07-06 15:04 UTC)

<p>3 posts were split to a new topic: <a href="/t/dce-analysis-fitted-signal-curve-does-not-make-sense/3403">DCE analysis - Fitted signal curve does not make sense</a></p>

---

## Post #47 by @fedorov (2018-07-06 15:00 UTC)

<p>A post was split to a new topic: <a href="/t/dce-analysis-ktrans-is-calculated-only-in-a-single-small-points/3402">DCE analysis - Ktrans is calculated only in a single small points</a></p>

---

## Post #48 by @fedorov (2018-08-10 14:44 UTC)

<p>A post was merged into an existing topic: <a href="/t/how-can-i-display-the-rcbv-map-acquired-by-dscmrianalysis-as-a-colormap/3589/5">How can I display the rCBV map acquired by DSCMRIAnalysis as a colormap?</a></p>

---

## Post #49 by @tigerhu7 (2018-08-14 02:35 UTC)

<p>Dear Dr Fedorov,<br>
Hello again!<br>
I am using pkModeling module on a liver tumor analysis project.<br>
I have a question, that on <a href="https://www.sciencedirect.com/science/article/pii/S1936523314800193" rel="nofollow noopener">Huang2014</a>, it says pkModeling(BWH-3DSlicer) is using Tofts model. The paper was published 4 years ago.<br>
I would like to make sure whether there is a upgraded model (for example Extended Tofts Model, or FXR-SSM) that is used in Slicer 4.9.0 nightly build version.<br>
The question come up in my mind, because on <a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/mrm.21066" rel="nofollow noopener">this paper</a>, it gives different definititions,<br>
[Tofts model Huang14]=[Kety model Parker06]<br>
[Extended Tofts model Huang14]=[Tofts model Parker06]<br>
which confused me.<br>
Thank you so much everytime!</p>
<p>–Tiger Hu</p>

---

## Post #50 by @fedorov (2018-08-14 13:57 UTC)

<p>Tiger, we did not add any new models to PkModeling since the Huang2014 paper.</p>

---

## Post #51 by @tigerhu7 (2018-08-14 15:25 UTC)

<p>Dear Dr Fedorov,<br>
Since there is an option of computing fpv(i.e vp) with 3-parameter model,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85d4956b0c3fdb9e13ad391994101f481264ad57.png" alt="%E5%9B%BE%E7%89%871" data-base62-sha1="j5UXDOyIl8vcGFWyW2Pu1cbQQrJ" width="477" height="247"><br>
I assume you are using extended Tofts model, not Kety model<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e22eaf3c4ddfc356a928e3e9eaea43112c644158.png" alt="%E5%9B%BE%E7%89%872" data-base62-sha1="wgTVCJuEWWHq1jyRjnxP6T9CRx6" width="447" height="95"><br>
because extended Tofts model contains 3 parameters Ktrans, vp and ve, and Kety model only contains 2.<br>
I will double check the results from calculation with pkmodeling module.<br>
Thanks again!<br>
-Tiger Hu</p>

---

## Post #52 by @fedorov (2018-08-14 16:42 UTC)

<p>Both of those models (with and without fpv) were present at the time of the analysis reported in the Huang2014 paper, I think we just included one of those in the paper.</p>

---

## Post #53 by @tigerhu7 (2018-08-15 01:16 UTC)

<p>Dear Dr Fedorov,<br>
Thank you for making it clear!</p>
<p>-Tiger Hu</p>

---

## Post #54 by @KHATRINA (2018-12-20 18:07 UTC)

<aside class="quote no-group quote-modified" data-username="kirezgik" data-post="1" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kirezgik/48/202_2.png" class="avatar"> kirezgik:</div>
<blockquote>
<p>Actual behavior: Is there a way to do the quantitative <a href="https://downloader.vip/torrent-sites/" rel="noopener nofollow ugc">Torrent</a>    <a href="https://downloader.vip/turbotax/" rel="noopener nofollow ugc">TurboTax</a> <a href="https://downloader.vip/gogoanime/" rel="noopener nofollow ugc">Gogoanime</a> analysis of DCE MRI of pancreatic tumor? I can only do semiquantitative analysis and create the plotting chart which shows the time-signal intensity curves of different ROIs, as it is discussed in this tutorial:</p>
</blockquote>
</aside>
<p>Actual behavior: Is there a way to do the quantitative analysis of DCE MRI of pancreatic tumor? I can only do semiquantitative analysis and create the plotting chart which shows the time-signal intensity curves of different ROIs, as it is discussed in this tutorial:</p>

---

## Post #55 by @fedorov (2018-12-20 19:08 UTC)

<aside class="quote no-group" data-username="KHATRINA" data-post="54" data-topic="622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/58f4c7/48.png" class="avatar"> KHATRINA:</div>
<blockquote>
<p>Is there a way to do the quantitative analysis of DCE MRI of pancreatic tumor?</p>
</blockquote>
</aside>
<p>Yes, you can use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/PkModeling">PkModeling extension</a> for pharmacokinetic analysis of DCE</p>

---

## Post #60 by @fedorov (2019-11-21 17:45 UTC)

<p>3 posts were split to a new topic: <a href="/t/pkmodeling-tutorial/9257">PkModeling tutorial</a></p>

---

## Post #63 by @ThymusTheTrain (2023-10-21 22:17 UTC)

<p>I tried following the tutorial linked in the OP, but after I load the test data I am unable to select anything for the Input Multivolume. I am using Slicer 5.</p>
<p>Could someone please guide me on how to properly load the data?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/191c850fa3c7658747decbec4ffa521e855393ab.png" data-download-href="/uploads/short-url/3A92u5InW5Wpu0UUHmrYhXLyGtZ.png?dl=1" title="DCE_Slicer_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/191c850fa3c7658747decbec4ffa521e855393ab_2_690x399.png" alt="DCE_Slicer_1" data-base62-sha1="3A92u5InW5Wpu0UUHmrYhXLyGtZ" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/191c850fa3c7658747decbec4ffa521e855393ab_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/191c850fa3c7658747decbec4ffa521e855393ab_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/191c850fa3c7658747decbec4ffa521e855393ab_2_1380x798.png 2x" data-dominant-color="2E2E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DCE_Slicer_1</span><span class="informations">2522×1462 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/723fd7c8f84490e8a6fc47d3439e8f58f74e710e.jpeg" data-download-href="/uploads/short-url/giHdii1KMg6C6eZGWtgTYdL3850.jpeg?dl=1" title="DCE_Slicer_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/723fd7c8f84490e8a6fc47d3439e8f58f74e710e_2_690x267.jpeg" alt="DCE_Slicer_2" data-base62-sha1="giHdii1KMg6C6eZGWtgTYdL3850" width="690" height="267" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/723fd7c8f84490e8a6fc47d3439e8f58f74e710e_2_690x267.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/723fd7c8f84490e8a6fc47d3439e8f58f74e710e_2_1035x400.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/723fd7c8f84490e8a6fc47d3439e8f58f74e710e_2_1380x534.jpeg 2x" data-dominant-color="36353B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DCE_Slicer_2</span><span class="informations">2534×982 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #64 by @smati_wissem (2024-01-11 11:41 UTC)

<p>How can I extract the AIF mask, please</p>

---
