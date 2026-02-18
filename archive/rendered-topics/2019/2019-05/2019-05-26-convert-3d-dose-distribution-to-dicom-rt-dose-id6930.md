# Convert 3D dose distribution to DICOM RT dose

**Topic ID**: 6930
**Date**: 2019-05-26
**URL**: https://discourse.slicer.org/t/convert-3d-dose-distribution-to-dicom-rt-dose/6930

---

## Post #1 by @ToufikDZ (2019-05-26 14:06 UTC)

<p>Operating system: windows 7 64bit<br>
Slicer version: 4.8.0<br>
Expected behavior: DICOM dose distribution<br>
Actual behavior:</p>
<p>Hello,<br>
I got 3D dose distribution from Monte Carlo simulation. I want to know if 3D slicer can convert the 3D dose distribution to DICOM RT dose file in order to compare the DVHs.<br>
Thanks in advance.</p>

---

## Post #2 by @cpinter (2019-05-27 13:30 UTC)

<aside class="quote no-group" data-username="ToufikDZ" data-post="1" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ToufikDZ:</div>
<blockquote>
<p>dose distribution from Monte Carlo simulation</p>
</blockquote>
</aside>
<p>What format is it in? What do you use for MC simulation?</p>

---

## Post #3 by @Hamburgerfinger (2019-05-27 15:27 UTC)

<p>You can generally do this with the Slicer RT extension, but you need to also output the geometry, I.e. “region” or “cell” or however your code calls it, as a voxel type labelmap. Then you can use the DVH functionality of Slicer RT.</p>
<p>Note: Uncheck “show dose volumes only” because even though your volume is a dose volume, it’s probably not RT dose volume so it won’t immediately show up. The results will be displayed as “intensity volume histogram” but it’s equivalent to DVH.</p>

---

## Post #4 by @cpinter (2019-05-27 15:29 UTC)

<aside class="quote no-group" data-username="Hamburgerfinger" data-post="3" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/eb9ed0/48.png" class="avatar"> Hamburgerfinger:</div>
<blockquote>
<p>You can generally do this with the Slicer RT extension</p>
</blockquote>
</aside>
<p>SlicerRT only supports a few RT application specific formats, so what you write is not quite true. I need to know what format it is in.</p>

---

## Post #5 by @ToufikDZ (2019-05-27 20:49 UTC)

<p>The dose distribution is in text format, I use Penelope for MC simulation.</p>

---

## Post #6 by @ToufikDZ (2019-05-27 20:57 UTC)

<p>The DICOM files are RT format (.dcm). I got the DVH from this file.<br>
My problem is the monte carlo dose. How to do to plot the DVH of the monte carlo dose simulated with Penelope?</p>

---

## Post #7 by @ToufikDZ (2019-05-27 21:02 UTC)

<p>How to output the geometry? (my geometry is a voxel phantom)<br>
My idea is to convert the 3D dose distribution to DICOM format and with the help of the DVH functionality of Sliser RT i plot the DVH.</p>

---

## Post #8 by @cpinter (2019-05-27 21:02 UTC)

<aside class="quote no-group" data-username="ToufikDZ" data-post="5" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ToufikDZ:</div>
<blockquote>
<p>text format</p>
</blockquote>
</aside>
<p>Can I see such a file please? It might be quite simple to add a reader plugin for it, similarly to <a href="https://github.com/SlicerRt/SlicerRT/tree/master/VffFileReader">this optical CT file format</a> for example.</p>

---

## Post #9 by @ToufikDZ (2019-05-27 21:04 UTC)

<p>Text format is for the 3D dose distribution result from MC simulation and not CT file.</p>

---

## Post #10 by @ToufikDZ (2019-05-27 21:05 UTC)

<p>How can I send it to you, please?</p>

---

## Post #11 by @cpinter (2019-05-27 21:05 UTC)

<aside class="quote no-group" data-username="ToufikDZ" data-post="7" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ToufikDZ:</div>
<blockquote>
<p>My idea is to convert the 3D dose distribution to DICOM format and with the help of the DVH functionality of Sliser RT i plot the DVH</p>
</blockquote>
</aside>
<ul>
<li>You can use the Dose Volume Histogram module to calculate and plot DVHs</li>
<li>You don’t need to convert the dose to DICOM for DVH calculation, but you can if you want. You can export RT dose from the Data module, if the dose is under a study and is converted to dose volume</li>
</ul>

---

## Post #12 by @cpinter (2019-05-27 21:06 UTC)

<aside class="quote no-group" data-username="ToufikDZ" data-post="10" data-topic="6930" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ToufikDZ:</div>
<blockquote>
<p>How can I send it to you, please?</p>
</blockquote>
</aside>
<p>Any file sharing service will do. We usually use Dropbox, OneDrive, or similar.</p>
<p>To another of your questions: the geometry will probably be in the header of the text file, same as in the case of the other importer I used as example above.</p>

---

## Post #13 by @ToufikDZ (2019-05-27 21:16 UTC)

<p>For the first option: As far as I know, the dose volume (RT dose) and segmentation (RT structure) files are requered for the DVH to calculate and plot the DVHs, and these files can only be obtained from DICOM files.<br>
Please, tell me how can i plot the DVH with 3D dose distribution file.<br>
Thanks in advance.</p>

---

## Post #14 by @cpinter (2019-05-27 21:21 UTC)

<aside class="quote no-group" data-username="ToufikDZ" data-post="13" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ToufikDZ:</div>
<blockquote>
<p>tell me how can i plot the DVH with 3D dose distribution file</p>
</blockquote>
</aside>
<p>The dose does not need to come from DICOM. However, we need to read it from your file, for which probably we’ll need to add a new file loader. Please refer to my explanations above.</p>

---

## Post #15 by @ToufikDZ (2019-05-27 22:13 UTC)

<p>Here is the file:<br>
<a href="https://drive.google.com/open?id=1joK-fOnqvwOIyTPEQg4I8CrH3hYJpakT" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1joK-fOnqvwOIyTPEQg4I8CrH3hYJpakT</a></p>

---

## Post #16 by @ToufikDZ (2019-05-27 22:48 UTC)

<p>I wonder how can this be done without volumes! the dose distribution file does not contain any geometry or volumes.</p>

---

## Post #17 by @Hamburgerfinger (2019-05-28 00:05 UTC)

<p>You usually have to run a separate tally, or calculation mode to output the geometry from your MC program.  I haven’t used the PENELOPE code, but for example in many  particle transport<br>
codes, there is an option to sample the material number (integer) , or region ID (integer) number in the voxel mesh (instead, or at the same time as, the dose tally) – there should be a description of how to do this within<br>
PENELOPE’s documentation.  Not sure if this helps, but how I usually make DVHs in Slicer is to:</p>
<p>a) run the dose simulation with the MC code to get 3D dose distribution which is imported into Slicer as a ‘volume’ (a reader may need to be made for it as cpinter mentioned)</p>
<p>b) run the geometry option with the MC code to get a voxel representation of the geometry, and import that into Slicer as a segmentation, or as a ‘labelmap’ which can be immediately converted to segmentation within Slicer</p>
<p>c) then calculate DVH within the DVH module of the slicer RT add-on</p>
<p>(Attachment mg_info.txt is missing)</p>

---

## Post #18 by @cpinter (2019-05-28 13:15 UTC)

<aside class="quote no-group" data-username="ToufikDZ" data-post="16" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ToufikDZ:</div>
<blockquote>
<p>the dose distribution file does not contain any geometry or volumes</p>
</blockquote>
</aside>
<p>Dose distribution is typically a 3D image which we call volume in medical image computing. Is your data not a 3D image?</p>

---

## Post #19 by @ToufikDZ (2019-05-28 15:21 UTC)

<p>My data is 3D image.</p>

---

## Post #20 by @cpinter (2019-05-28 15:40 UTC)

<p>I don’t have access to the data you shared. I clicked on Request access, please let me know once you granted it and I can download it.</p>

---

## Post #21 by @ToufikDZ (2019-05-28 16:11 UTC)

<p>I send the links again. The first link is for voxel dose distribution, the second one is for 3D dose distribution.<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1cUzDR1U-q-EDymA7Pf4DCoVgyBk-KRCq/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1cUzDR1U-q-EDymA7Pf4DCoVgyBk-KRCq/view?usp=drive_open" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1cUzDR1U-q-EDymA7Pf4DCoVgyBk-KRCq/view?usp=drive_open" target="_blank" rel="nofollow noopener">tallyVoxelDoseDistrib.dat</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<a href="https://drive.google.com/open?id=1joK-fOnqvwOIyTPEQg4I8CrH3hYJpakT" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1joK-fOnqvwOIyTPEQg4I8CrH3hYJpakT</a></p>

---

## Post #22 by @cpinter (2019-05-28 17:31 UTC)

<p>Indeed the geometry is not contained by these files. You will probably need to export them seperately as <a class="mention" href="/u/hamburgerfinger">@Hamburgerfinger</a> mentioned above.</p>
<p>The files otherwise seem to be straightforward to load, it should be easy to write an importer.</p>

---

## Post #23 by @ToufikDZ (2019-05-28 21:04 UTC)

<p>What do you mean by geometry, please? Is the geometry file (phantom) used for simulation? if so here is the link to it:<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1CVy3LlQ-7O47Gcs8M8l59e0GWiHoVbPR/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1CVy3LlQ-7O47Gcs8M8l59e0GWiHoVbPR/view?usp=drive_open" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1CVy3LlQ-7O47Gcs8M8l59e0GWiHoVbPR/view?usp=drive_open" target="_blank" rel="nofollow noopener">Phantom.vox</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I think the easiest way to plot the DVH is by using the DICOM RT dose file. My idea is to use the original DICOM RT dose file and replace the dose distribution by the data obtained from MC simulation. By the way, I use for simulation the code Penelope/penEasy.<br>
Is there a way to do that with Slicer, please?</p>

---

## Post #24 by @Hamburgerfinger (2019-05-28 23:51 UTC)

<p>So it looks like you have the ‘region labels’ in the left column, where you have 5 different regions defined (it looks like they have been defined by thresholding of CT data), see Labelmap.png, attached.  Here 5 is red, 4 is magenta, 3<br>
is blue, 2 is green, and 1 is yellow.</p>
<p>Then in the right column, you have the density in each voxel; see Density.png, attached.</p>
<p>So yes in principle this is the geometry you need to define as a segmentation in Slicer for DVH.  One issue is, in your region label map, bone for instance mostly has a region label of ‘5’ but there are other non-bone structures that also<br>
have this label; soft tissue mostly has a region label of ‘4’ but there are other non-tissue structures with this label also; etc.  So you could use these regions for DVH, but there will be some error due to the other non-tissue structure with the same labels<br>
in your dataset.</p>
<p>To fix this, you could import the data in the left column into Slicer as a segmentation, and edit it in the segment editor, and then use for DVH.  Or you could import the density map (or, better, use the CT it was derived from) segment<br>
the regions of interest, and use that for DVH.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89cc2858cd18f7b049f406e95902a1f4e056dac2.png" data-download-href="/uploads/short-url/jF0OMDac9XAgsePhgUxJ7PNnRnA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89cc2858cd18f7b049f406e95902a1f4e056dac2.png" alt="image" data-base62-sha1="jF0OMDac9XAgsePhgUxJ7PNnRnA" width="503" height="499" data-dominant-color="938A73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">901×895 77.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9c27d769a3fbe2d4eaf05a58d2644ed370b5636.png" data-download-href="/uploads/short-url/sMQFcWI7ma5V49aTTurkp4vAhdY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9c27d769a3fbe2d4eaf05a58d2644ed370b5636_2_542x500.png" alt="image" data-base62-sha1="sMQFcWI7ma5V49aTTurkp4vAhdY" width="542" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9c27d769a3fbe2d4eaf05a58d2644ed370b5636_2_542x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9c27d769a3fbe2d4eaf05a58d2644ed370b5636_2_813x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9c27d769a3fbe2d4eaf05a58d2644ed370b5636.png 2x" data-dominant-color="C3C3C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">900×830 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @ToufikDZ (2019-05-30 20:45 UTC)

<p>Thank you very much for these explanation.<br>
In fact the region of interest is a small volume in the soft tissue region defined in the DICOM files. I want to use this region for DVH. For that I want to convert my file to DICOM file.</p>

---

## Post #26 by @cpinter (2019-05-30 20:57 UTC)

<p>If you have means to convert this to any type of file that can be read from Slicer (nrrd, nifti, mha, etc.), then your problem is solved. Otherwise a reader needs to be implemented for this file format.</p>

---

## Post #27 by @bode (2019-07-26 07:42 UTC)

<p>Hello cpinter,</p>
<p>I just read the discussion. I am looking for an Viewer/ Reader which is able to handle .3ddose files from DOSXYZnrc. Is it possible to Import and visualize .3ddose files and maybe convert them to DICOM RT files for further comparisons in a Treatment planning system?</p>
<p>Kind regards, bode</p>

---

## Post #28 by @cpinter (2019-07-26 12:35 UTC)

<p>Yes. Have the SlicerRT extension installed, drag&amp;drop the 3ddose file onto Slicer, then do DICOM export as usual: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>
<p>That said you can do comparisons using SlicerRT. It has DVH and gamma comparison tools.</p>

---

## Post #29 by @DUONG_Thanh_Tai (2022-09-01 20:13 UTC)

<p>Hi everyone,</p>
<p>I have the 3ddose file from the Monte Carlo simulation. After that, I converted the 3ddose file to Dicom format.<br>
My question is:<br>
(1) with the same 3ddose, but the DVH plotted directly from the 3ddose differs from the DVH plotted from the Dicom format.</p>
<p>(2) The dose value in 3ddose is about 2.3716289e-18, but the DVH shows the value of the x-axis is from 0 to 60000. What is the unit of the x-axis?</p>

---

## Post #30 by @cpinter (2022-09-02 10:02 UTC)

<aside class="quote no-group" data-username="DUONG_Thanh_Tai" data-post="29" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/duong_thanh_tai/48/10533_2.png" class="avatar"> DUONG_Thanh_Tai:</div>
<blockquote>
<p>I converted the 3ddose file to Dicom format.</p>
</blockquote>
</aside>
<p>Please describe exactly how you did this.</p>
<p>Also please check the scalar range of both dose volumes in the Volumes module. Maybe exporting trimmed or rescaled the scalars.</p>

---

## Post #31 by @DUONG_Thanh_Tai (2022-09-02 13:16 UTC)

<p>Hi Csaba Pinter,</p>
<p>Thank you for your response.</p>
<p>The 3ddose file was converted to RTdose.dcm and then I input the 3ddose and RTdose.dcm to Slicer RT and plot two DVHs. The DVH plotted from the 3ddose is about two times different with the DVH plotted from RTdose.dcm<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e077253b4dc54855e879817d1f297a131e31584.png" data-download-href="/uploads/short-url/6zbUUlQznWCylGLsJPsifJcc0VS.png?dl=1" title="DVH" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e077253b4dc54855e879817d1f297a131e31584_2_690x157.png" alt="DVH" data-base62-sha1="6zbUUlQznWCylGLsJPsifJcc0VS" width="690" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e077253b4dc54855e879817d1f297a131e31584_2_690x157.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e077253b4dc54855e879817d1f297a131e31584_2_1035x235.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e077253b4dc54855e879817d1f297a131e31584_2_1380x314.png 2x" data-dominant-color="D8D8D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DVH</span><span class="informations">1906×434 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #32 by @cpinter (2022-09-02 13:25 UTC)

<aside class="quote no-group" data-username="DUONG_Thanh_Tai" data-post="31" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/duong_thanh_tai/48/10533_2.png" class="avatar"> DUONG_Thanh_Tai:</div>
<blockquote>
<p>The 3ddose file was converted to RTdose.dcm</p>
</blockquote>
</aside>
<p>How <em>exactly</em>? This was my first question.</p>
<p>Please also answer the second question about the scalar ranges.</p>

---

## Post #33 by @DUONG_Thanh_Tai (2022-09-02 13:57 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="32" data-topic="6930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>scalar ranges</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>Please see the picture</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f4b816288306eff3064c5fcf04353b386b0840f.png" data-download-href="/uploads/short-url/91VQIidZY1jYSph2C2WkN3P2ejZ.png?dl=1" title="RTdose.dcm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f4b816288306eff3064c5fcf04353b386b0840f_2_690x306.png" alt="RTdose.dcm" data-base62-sha1="91VQIidZY1jYSph2C2WkN3P2ejZ" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f4b816288306eff3064c5fcf04353b386b0840f_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f4b816288306eff3064c5fcf04353b386b0840f_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f4b816288306eff3064c5fcf04353b386b0840f.png 2x" data-dominant-color="35373C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RTdose.dcm</span><span class="informations">1064×472 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/290dcd4fb640a8674729eae3fc3fb3682d55b96d.png" data-download-href="/uploads/short-url/5Rb96NXDHJ4VOTp1iRspmznQWNT.png?dl=1" title="3ddose" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/290dcd4fb640a8674729eae3fc3fb3682d55b96d_2_690x306.png" alt="3ddose" data-base62-sha1="5Rb96NXDHJ4VOTp1iRspmznQWNT" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/290dcd4fb640a8674729eae3fc3fb3682d55b96d_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/290dcd4fb640a8674729eae3fc3fb3682d55b96d_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/290dcd4fb640a8674729eae3fc3fb3682d55b96d.png 2x" data-dominant-color="34363B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3ddose</span><span class="informations">1063×472 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #34 by @cpinter (2022-09-02 16:24 UTC)

<p>Thanks! The scalar range as you can see is very different: (8, 61439) vs (4.067, 27853.7). You will need to revise the way you converted the volume to DICOM, but since you don’t provide details about how you did that I cannot help you there.</p>

---

## Post #35 by @Rafael_Scatena (2023-06-02 18:17 UTC)

<p>Convert result of the simulation to a .nrrd dose volume with ITK toolkit. Then Slicer will be able to read it</p>

---

## Post #36 by @rblowe (2024-02-09 11:30 UTC)

<p><a class="mention" href="/u/rafael_scatena">@Rafael_Scatena</a> : Can you describe how this is done? Any hint would be appreciated.</p>

---
