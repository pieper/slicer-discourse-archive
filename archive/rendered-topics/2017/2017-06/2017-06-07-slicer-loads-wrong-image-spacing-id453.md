# Slicer loads wrong image spacing

**Topic ID**: 453
**Date**: 2017-06-07
**URL**: https://discourse.slicer.org/t/slicer-loads-wrong-image-spacing/453

---

## Post #1 by @Shilpa_Ananth (2017-06-07 16:35 UTC)

<p>Operating system: Windows 64 bit<br>
Slicer version: 4.6.2<br>
Expected behavior: My .dcm file has clear values under the Pixel spacing and the Slice thickness,spacing between slices tags. So these values must be loaded onto image spacing under ‘volumes’.<br>
Actual behavior: Image spacing goes to default value ie 1mm 1mm and 1mm.</p>
<p>Are there any other tags required for this field that I am forgetting to include in my dicom header? I cannot manually change it everytime as I am trying to integrate it with a different process.</p>

---

## Post #2 by @pieper (2017-06-07 17:47 UTC)

<p>You are making these dicom files yourself?  If so maybe you have not encoded the elements correctly.  You can try loading the sample data below and compare your data.</p>
<p><a href="http://slicer.kitware.com/midas3/download/item/279888/deidentifiedMRHead.zip" class="onebox" target="_blank">http://slicer.kitware.com/midas3/download/item/279888/deidentifiedMRHead.zip</a></p>
<p>Also note if you are looking at the vtkImageData on a loaded node, it will have origin 0,0,0 and spacing 1,1,1 because there’s no way to encode orientation in a vtkImageData.  Instead, location of the imaging data in patient space is encoded in the mrml IJKToRAS and transform elements.</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @Shilpa_Ananth (2017-06-07 19:21 UTC)

<p>Thanks for your response!</p>
<p>Not exactly myself, but im just rearranging data. The DICOM header is stored as a dataset with elements. However, my data had a few elements itself as datasets. So I had to bring a few elements back into the main dataset. I was able to successfully bring proper values on slicer with respect to origin. This seems to take information from the Image position(Patient) Tag.</p>
<p>But even though the tags required for Spacing are now present as elements in the main dataset- Pixel spacing, slice thickness, and most of the other relevant data that is included in the header of the file you uploaded, The spacing still shows 1mm 1mm and 1mm. I am not using vtk.</p>
<p>Is there any information as to which tags exactly slicer draws the information from for image spacing? Intuitively it should be the two elements of Pixel spacing and the third element should be slice thickness.</p>

---

## Post #4 by @pieper (2017-06-07 20:23 UTC)

<p>Hi -</p>
<p>PixelSpacing should always give the in-plane sizes in mm.  Be sure it is in a valid dicom format of two DS values (basically decimal strings separated by backslash).</p>
<p>If you use dcmdump from dcmtk it should look something like this:</p>
<pre>(0028,0030) DS [1.000000e+00\1.000000e+00]              #  26, 2 PixelSpacing
</pre>
<p>The out of plane spacing is defined by the distance between the ImagePositionPatient of adjacent slices, not by the SliceThickness, which can be different for a variety of reasons.</p>
<p>If Slicer (or ITK) can’t parse what your file contains you could end up with spacings of 1,1,1.</p>
<p>It’s a slightly different context, but this blog post gives you some background and context:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="http://dclunie.blogspot.com/favicon.ico" class="site-icon" width="32" height="32">
      <a href="http://dclunie.blogspot.com/2013/10/how-thick-am-i-sad-story-of-lonely-slice.html" target="_blank">dclunie.blogspot.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="http://dclunie.blogspot.com/2013/10/how-thick-am-i-sad-story-of-lonely-slice.html" target="_blank">How Thick am I? The Sad Story of a Lonely Slice.</a></h3>

<p>Summary: Single slice regions of interest with no multi-slice context or interval/thickness information may need to be reported as area only...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>HTH,<br>
Steve</p>

---

## Post #5 by @Shilpa_Ananth (2017-06-08 14:16 UTC)

<p>Thanks steve!</p>
<p>I’ve checked, and the slice thickness even coincides with the distance between the imagepositionpatient of adjacent slices.<br>
And the pixel spacing seems to be the right format.Here is my ouput from python: I am using the pydicom toolbox.</p>
<blockquote>
<blockquote>
<p>original_image.data_element(“PixelSpacing”).value<br>
[‘0.65562321835365’, ‘0.65562321835365’]</p>
</blockquote>
</blockquote>
<p>The image is a multiframe image. Is that the problem? It had its image position patient of each slice under per frame functional group sequence! So maybe it is unable to find the proper spacing?</p>
<p>Shilpa</p>

---

## Post #6 by @pieper (2017-06-08 19:04 UTC)

<p>Hi -</p>
<p>Multiframe DICOM images should be loadable in Slicer – is there any chance<br>
you can share a deidentified example?  Yes, having the ImagePositionPatient<br>
values in the per-frame functional groups is the right place and Slicer<br>
should be looking there.</p>
<p>-Steve</p>

---

## Post #7 by @lassoan (2017-06-08 19:53 UTC)

<p>Reading spacing correctly for multi-frame volumes has been added to ITK a couple of years ago. It might have broken since, as probably automatic testing of DICOM parsing is quite limited in ITK. Probably we should add tests for that in Slicer.</p>

---

## Post #8 by @Shilpa_Ananth (2017-06-08 20:40 UTC)

<p>Unfortunately, I won’t be able to do that(share the image). This is an abdominal CT from Philips medical systems. I did download another standard multiframe from nema onto slicer and that does give proper values in the volume fields lifted right off the header but the rendered volume is well away from the origin of the RAS (The pink box) .</p>
<p>The nema image and this image does have a few differences. for example, the<br>
(5200, 9229)  Shared Functional Groups Sequence   1 item(s) ----<br>
tag in my file does not have image orientation under the plane orientation sequence. My file has it just under all the per-frame functional groups. A couple of other extra tags were there under (5200,9299) for the nema image too! These were absent from mine.</p>
<p>However 5200,9229 does have the<br>
(0028, 9110)  Pixel Measures Sequence   1 item(s) ----<br>
(0018, 0050) Slice Thickness                     DS: ‘3.00000’<br>
(0028, 0030) Pixel Spacing                       DS: [‘0.597656’, ‘0.597656’]<br>
tag which should be the only tag that contains relevant information.</p>
<p>The standard NEMA image I checked with is from <a>ftp://medical.nema.org/MEDICAL/Dicom/Multiframe/CT/</a></p>
<p>Thanks for your help anyway. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Maybe I should try and convert this into separate images first!</p>

---

## Post #9 by @pieper (2017-06-08 21:34 UTC)

<p>Understood - it’s always toughest to debug dicom files that can’t be shared.</p>
<p>Since it looks like you know your way around the header with pydicom you should be able to easily generate a basic nrrd file.  You can probably even make a .nhdr that is just a few lines of ascii and points to the raw data in the original dicom file.</p>
<p>good luck</p>

---

## Post #10 by @fedorov (2017-06-09 13:50 UTC)

<aside class="quote no-group" data-username="Shilpa_Ananth" data-post="8" data-topic="453">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/7ea924/48.png" class="avatar"> Shilpa_Ananth:</div>
<blockquote>
<p>tag in my file does not have image orientation under the plane orientation sequence. My file has it just under all the per-frame functional groups</p>
</blockquote>
</aside>
<p>It is a known issue with the datasets produced by some vendors, and the ITK reader is not robust enough to look for these attributes in the per-frame FG(s!) when they are missing in the shared FG.</p>

---

## Post #11 by @Shilpa_Ananth (2017-06-09 13:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a80b8a6b6ea24a4c9aad9a61440b3094f6b64700.png" data-download-href="/uploads/short-url/nYAWkIQQgFdM7imI7YpUxCuoXLi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a80b8a6b6ea24a4c9aad9a61440b3094f6b64700.png" alt="image" data-base62-sha1="nYAWkIQQgFdM7imI7YpUxCuoXLi" width="690" height="363" data-dominant-color="151515"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">969×511 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I did try moving it to the shared functional groups too. No luck.</p>
<p>Thanks Steve and Andrey!</p>

---

## Post #12 by @fedorov (2017-06-09 14:01 UTC)

<p>How did you move it?</p>
<p>Does it pass the <a href="http://www.dclunie.com/dicom3tools/dciodvfy.html">validator</a> after you modified the dataset?</p>

---

## Post #13 by @evan (2019-09-24 16:33 UTC)

<p>I have been experiencing this DICOM spacing &amp; thickness error recently on quite a few DICOM sets.</p>
<p>The files have the following tags in metadata:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a726d9e28e0168d842aa4c312f9421081a9c7d9.png" alt="image" data-base62-sha1="1upW1UpfB7owy7289uP2rSWydFD" width="569" height="111"><br>
On load the error <code>Irregular volume geometry detected (maximum error of 931.5 mm is above tolerance threshold of 0.001 mm)</code> is displayed. The Volumes module shows the default spacing (1mm, 1mm, 1mm) and I must manually enter the correct values. Like <a class="mention" href="/u/shilpa_ananth">@Shilpa_Ananth</a> I am also looking to integrate this into another process so manual entry is not ideal. I did test <strong>Acquisition geometry regularization</strong> in <em>Application Settings</em>&gt;<em>DICOM</em>, which does fix visualization in the slicer viewer. However, this created resolution errors when performing transformations on the volume.</p>
<p>Here is a faulting <a href="https://uwoca-my.sharepoint.com/:u:/g/personal/esimps27_uwo_ca/EdKwNKrGv-NLg_mJU-pFgEABQMqUyaXUD-H0gQpf67oLXw?e=ZjkjJW" rel="noopener nofollow ugc">anonymized DICOM set</a> to test.</p>

---

## Post #14 by @pieper (2019-09-24 18:26 UTC)

<p>Hi <a class="mention" href="/u/evan">@evan</a> -</p>
<p>Thanks for sharing the data and describing what you see.  I can replicate the issue with your data.  This happens when the underlying ITK reader cannot interpret your data as a proper volume with equal spacing in all axes.  This can happen if there are missing slices or it can happen if the slice ordering is not consistent (SliceThickness and SpacingBetweenSlices are not used for this, only the per-slice ImagePositionPatient and ImageOrientationPatient).  In this data there must be some issue that ITK doesn’t deal with or else the data is just wrong (I didn’t look at your data closely to see what the issue is here).</p>
<p>The <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L555-L718"><code>Acquisition geometry regularization</code></a> code detects this error and can correct for it when enabled.  It creates a non-linear transform to put the slices back in the correct places as defined by the position and orientation.</p>
<p>You can use the <code>Harden Transform</code> button in the Transforms module to apply the non-linear regularization transform to the data and then you can use it for other operations.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59a0009b8cd529691aa3ff9247975b58f404ceb5.png" alt="image" data-base62-sha1="cMRiuWVAHT9MRfhIWRMd2vvOcND" width="334" height="146"></p>

---

## Post #15 by @evan (2019-09-27 19:52 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, thanks for the response and useful information!</p>
<p>I iterated through the slices and couldn’t seem to find a missing slice or order inconsistency.</p>
<p>I tried the Acquisition geometry regularization again with Harden Transform. Here is an example of the transform resolution I’m seeing.</p>
<p>Before harden:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b808793132a81928172e831ae7eaad0dae9b7f35.png" data-download-href="/uploads/short-url/qg20xE9yj7c0HuRlTF3PtKFbFul.png?dl=1" title="Without%20harden" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b808793132a81928172e831ae7eaad0dae9b7f35_2_690x251.png" alt="Without%20harden" data-base62-sha1="qg20xE9yj7c0HuRlTF3PtKFbFul" width="690" height="251" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b808793132a81928172e831ae7eaad0dae9b7f35_2_690x251.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b808793132a81928172e831ae7eaad0dae9b7f35_2_1035x376.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b808793132a81928172e831ae7eaad0dae9b7f35.png 2x" data-dominant-color="52514F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Without%20harden</span><span class="informations">1091×397 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After harden:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5319749ef4ee4f5a605f78c0b6d67a5c5a9d00d.png" data-download-href="/uploads/short-url/pQUFyHGufkHoz8TzyGpdkayp5Xn.png?dl=1" title="Hardened" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5319749ef4ee4f5a605f78c0b6d67a5c5a9d00d_2_690x233.png" alt="Hardened" data-base62-sha1="pQUFyHGufkHoz8TzyGpdkayp5Xn" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5319749ef4ee4f5a605f78c0b6d67a5c5a9d00d_2_690x233.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5319749ef4ee4f5a605f78c0b6d67a5c5a9d00d_2_1035x349.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5319749ef4ee4f5a605f78c0b6d67a5c5a9d00d.png 2x" data-dominant-color="444341"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Hardened</span><span class="informations">1090×369 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @pieper (2019-09-27 20:39 UTC)

<p>Looks like progress - you can control the resampling resolution using other methods:  <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Resampling" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/Resampling</a></p>

---

## Post #18 by @pieper (2019-09-27 23:45 UTC)

<p>It’s a complex process actually, so the only real way to know is to look at the source code.  The best short answer is it uses the <code>ImagePositionPatient</code> tags of the slices in a volume together with <code>PixelSpacing</code>.</p>
<p>At the center of things is some code that <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/970e7fa9ce42f9d3da78c47213a320abc382d613/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L483" rel="nofollow noopener">applies a number of heuristics</a>.  I’m not a huge fan of this code, but it was developed by people who had access to file types that are not available for testing.</p>

---

## Post #22 by @issakomi (2019-10-01 01:29 UTC)

<blockquote>
<p>I’m not a huge fan of this code</p>
</blockquote>
<p>BTW, <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/970e7fa9ce42f9d3da78c47213a320abc382d613/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L514" rel="noopener nofollow ugc">this switch</a> is useless, forced Tag is (<a href="https://github.com/InsightSoftwareConsortium/ITK/blob/970e7fa9ce42f9d3da78c47213a320abc382d613/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L506" rel="noopener nofollow ugc">0028,0030</a>), so VR is always <em>DS</em> in <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Modules/ThirdParty/GDCM/src/gdcm/Source/DataDictionary/gdcmDefaultDicts.cxx" rel="noopener nofollow ugc">dictionary</a>, this switch was simply copy/pasted, <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/970e7fa9ce42f9d3da78c47213a320abc382d613/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L1321" rel="noopener nofollow ugc">s. here</a> and <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/970e7fa9ce42f9d3da78c47213a320abc382d613/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L510" rel="noopener nofollow ugc">dictionary lookup above</a> is useless too, it is loop.</p>

---

## Post #23 by @issakomi (2019-10-01 11:48 UTC)

<p><a href="https://github.com/InsightSoftwareConsortium/ITK/pull/1280" rel="nofollow noopener">PR</a></p>

---

## Post #24 by @Juicy (2019-10-10 06:53 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> ,</p>
<p>Do you mind briefly explaining what Apply regularization transform actually does? I have used it to fix gantry tilt issues and to fix issues like the one described above, but I don’t understand what it is.</p>
<p>Also I notice that it is not enabled by default. It seems to do a good job of fixing errors so is there any reason why I shouldn’t leave this setting enabled all the time?</p>
<p>Thanks for your contributions to Slicer!</p>

---

## Post #25 by @pieper (2019-10-11 18:25 UTC)

<p>Hi <a class="mention" href="/u/juicy">@Juicy</a> - I’m glad it works for you!</p>
<p>The commit message linked below has more of the details.  Happy to answer other questions if it’s not clear.  It’s a particularly gratifying piece of code because the problem had bothered me for years and finally the nonlinear transform support in Slicer matured to the point that this approach is at least fairly straightforward and I believe it solves the problem the “Right Way”.</p>
<p>When the feature was new we disabled it by default, but for <a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Acquisition_transform" rel="nofollow noopener">Slicer5 we plan to turn it on by default</a>.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/b7650af3c27f34fc894bfdd587f2a4c02ba62a8b" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/b7650af3c27f34fc894bfdd587f2a4c02ba62a8b" target="_blank" rel="nofollow noopener">ENH: model DICOM acquisition geometry (addresses #4409)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-10-20" data-time="12:57:03" data-timezone="UTC">12:57PM - 20 Oct 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="nofollow noopener">
          <img alt="pieper" src="https://avatars0.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
        
      </div>

      <div class="lines" title="changed 2 files with 278 additions and 6 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/b7650af3c27f34fc894bfdd587f2a4c02ba62a8b/files" target="_blank" rel="nofollow noopener">
          <span class="added">+278</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Add a step to the DICOMScalarVolumePlugin to check that the loaded
volume node's slice geometry matches what is expected from
the position and...</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #26 by @evan (2019-11-04 19:11 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>Would you mind explaining how to properly harden the volume with the transform that results from the <em>Apply regularization transform</em> option?</p>
<p>As previously mentioned the volume resolution is severely degraded after using the <em>Harden Transform</em> function. I followed the link (<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Resampling" rel="nofollow noopener">resampling documentation</a>) you provided, but could not figure out how to achieve this. Is there a way to do this without degrading resolution?</p>
<p>Thanks</p>

---

## Post #27 by @lassoan (2019-11-04 19:32 UTC)

<p>Harden transform applies the original resolution of the volume to the resampled volume. If the original resolution was low or highly anisotropic then you may see visible degradation. In this case, probably the simplest is to use <code>Crop volume</code> module with “Interpolated cropping” and “Isotropic spacing” enabled and with a “Spacing scale” that is low enough to preserve all relevant details but still large enough so that you don’t end up with a huge image (something between 0.2-0.8 should work).</p>

---

## Post #28 by @evan (2019-11-12 19:48 UTC)

<p>Thanks for the response! I followed those steps and was able to resample the volume. I am seeking an “automatic” or “one-click” solution to fix this DICOM spacing error as I have a large batch of samples to process with this issue. I see now that it must be manually handled via the Volumes or Crop Volume modules. If I end up programming a simple module to help with this I will reference it here.</p>

---

## Post #29 by @Davide_Punzo (2023-11-13 08:44 UTC)

<p>NOTE: Support for regularization transform hardening in DICOM Scalar plugin has been added. See <a href="https://discourse.slicer.org/t/enh-support-regularization-transform-hardening-in-dicom-scalar-plugin/32772">link</a>.</p>
<p>Although the resamplig <a href="https://discourse.slicer.org/t/slicer-loads-wrong-image-spacing/453/27">step</a> with Crop Volume for the moment is not applied automatically.</p>

---
