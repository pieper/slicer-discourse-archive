---
topic_id: 33294
title: "Conversion Of Fa Fractional Anisotropy Map To Dicom Failing"
date: 2023-12-08
url: https://discourse.slicer.org/t/33294
---

# Conversion of FA (Fractional Anisotropy) map to DICOM failing

**Topic ID**: 33294
**Date**: 2023-12-08
**URL**: https://discourse.slicer.org/t/conversion-of-fa-fractional-anisotropy-map-to-dicom-failing/33294

---

## Post #1 by @snnstuff (2023-12-08 04:10 UTC)

<p>I’m trying to convert a FA map in nifti format to DICOM format.  I tried intermediary steps of converting the nifti file to NRRD first (and TIF), but the output has no contrast.  DICOM files are created, but the image contrast is incorrect.</p>
<p>On the DICOM, it looks like all the image values are either 0 or 1.</p>
<p>Any thoughts on how to fix this?</p>
<p>Many thanks for your help.</p>

---

## Post #2 by @pieper (2023-12-08 13:07 UTC)

<p>Traditional dicom files do not support floating point, only integer types.  There is a way to provide rescale parameters (<a href="https://www.kitware.com/dicom-rescale-intercept-rescale-slope-and-itk/">slope and intercept</a>).  You could have a look at how commercial scanners/workstations represent FA maps and just copy that format.</p>

---

## Post #3 by @Chris_Rorden (2023-12-27 18:49 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> for completeness, it is worth noting that <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_8.2.html" rel="noopener nofollow ugc">DICOM</a> does support float32 (Float Pixel Data: 7FE0,0008) and float64 (Double Float Pixel Data: 7FE0,0009), but these representations are very rare (I have only personally seen them in context of radiotherapy). I do not think many DICOM tools support these datatypes, so for practical purposes it may be worth avoiding creating these datatypes.</p>
<p>My own solution to this problem would be to save the data as signed 16-bit integers. I would multiply the each voxel’s FA value by x32000, and then set the <a href="https://www.kitware.com/dicom-rescale-intercept-rescale-slope-and-itk/" rel="noopener nofollow ugc">rescale slope (0028,1053)</a> to 1/32000, with the rescale intercept (0028,1052) set to zero. The int16 supports integer values of -32768…32768 but the conservative 32000 could in theory retain edges for higher order interpolation.</p>
<p>I always set our scanner to discard FA images as we can derive better images after we process with degibbs, dwidenoise, eddy and topup. However, I will keep this in mind and see if I can acquire some sample data to show how Siemens does save their FA maps. As I recall, Siemens does not store spatial transforms for their FA and colored direction-modulated-by-FA  images, so I do not think I would copy them too carefully.</p>

---

## Post #4 by @pieper (2023-12-28 02:33 UTC)

<p>Thanks for the extra info <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a>.  Yes, there are some more modern options (rare, as you say).  I suggested “traditional” approaches because I guessed that <a class="mention" href="/u/snnstuff">@snnstuff</a> probably wants some kind of interoperable solution.  But even for that there are options so the answer, as usual, really is ‘it depends on why you want to export to dicom’.</p>

---

## Post #5 by @snnstuff (2023-12-28 03:38 UTC)

<p>Thanks for the information…  yes, I compute my own FA maps offline after a proper preprocessing pipeline.</p>
<p>I ended up multiplying each voxel value on the source NIFTI FA maps by 1000 then doing the conversion to DICOM.</p>
<p>This certainly produced a DICOM image with contrast similar  to the source NIFTI image (although, I’m now guessing not identical based on the prior posts).</p>
<p>Given that the DICOM FA maps are sometimes downloaded from PACS and used with 3rd party software (research ROI analysis or VBA; or more critically, tractography for surgical navigation) the accuracy and values matter. The optimal scenario would be saving the DICOM in floating point given potential use with 3rd party software to retain the expected range of voxel values between 0 and 1.</p>

---

## Post #6 by @pieper (2023-12-28 04:02 UTC)

<p>Yes, if you need to put the images through a clincial PACS, then following the traditional method of scaling by 1000 (or 32000 as Chris suggests) and storing as an MR image or secondary capture is a reasonable path.  You’d really want to reverse engineer from the end use (e.g. surgical navication system) to determine the highest fidelity format it can consume.</p>
<p>You may also want to generate an additional Parametric Map series, which floating point pixels with header fields like <code>QuantityValueCode</code> and <code>MeasurementMethodCode</code> to be very explicit about what the data is meant to represent and how you calculated it.  This information about the <a href="https://qiicr.org/">dcmqi</a> tools should give you a good idea how to do that:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://qiicr.gitbook.io/dcmqi-guide/opening/cmd_tools/dicom-parametric-map-support">
  <header class="source">
      <img src="https://4046500763-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/spaces%2F-KzyAedGvZPZ3Qhr88HS%2Favatar.png?generation=1511797994213344&amp;alt=media" class="site-icon" width="256" height="256">

      <a href="https://qiicr.gitbook.io/dcmqi-guide/opening/cmd_tools/dicom-parametric-map-support" target="_blank" rel="noopener">qiicr.gitbook.io</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://app.gitbook.com/share/space/thumbnail/-KzyAedGvZPZ3Qhr88HS/page/-KzyAf9cilFeFZ8CRbuY.png?color=%23f47c24&amp;logo=https%3A%2F%2F4046500763-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-KzyAedGvZPZ3Qhr88HS%252Favatar.png%3Fgeneration%3D1511797994213344%26alt%3Dmedia&amp;theme=default" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://qiicr.gitbook.io/dcmqi-guide/opening/cmd_tools/dicom-parametric-map-support" target="_blank" rel="noopener">Parametric maps</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note that some PACS may be set to refuse to accept SOP classes that they don’t expect.</p>

---
