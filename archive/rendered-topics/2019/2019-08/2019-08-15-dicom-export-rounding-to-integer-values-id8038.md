# DICOM Export Rounding to Integer Values

**Topic ID**: 8038
**Date**: 2019-08-15
**URL**: https://discourse.slicer.org/t/dicom-export-rounding-to-integer-values/8038

---

## Post #1 by @madeline (2019-08-15 01:19 UTC)

<p>Hi all,</p>
<p>I am assuming it is a setting I am not able to locate on Slicer, so I’m hopeful this will be an easy question to answer! The problem I am having is that all my DICOM exports seem to convert the values in my PK maps (e.g. K-trans) into whole integer numbers upon export. This is problematic when most values are lying between 0-1 and thus I can’t get an accurate measurement of my ROI’s.</p>
<p>I have attempted exporting in the same subject folder as the original images, adjusting the DICOM settings and re-opening in several other image analysis software’s  (ImageJ, MATLAB etc.).</p>
<p>Any assistance on this will be highly appreciated!</p>
<p>Best,<br>
Maddie</p>

---

## Post #2 by @cpinter (2019-08-15 13:35 UTC)

<p>I’m not a DICOM expert but as far as I know integer is the only available scalar type for images. RT dose tackles this problem by specifying a scaling factor, which is applied when loading, and this is how it achieves floating point values.<br>
What modality are you trying to export it to? Do you know if there is a DICOM modality specified for PK maps?</p>

---

## Post #3 by @madeline (2019-08-16 00:01 UTC)

<p>I originally import MRI sequences in DICOM format to Slicer. Then use the PKModeling Module to generate the maps. I don’t know of a specific modality for these maps, but know that prior to export, they definitely have float values included- Exporting loses the scaling factor implemented in the program. Slightly lost for ideas.</p>

---

## Post #4 by @lassoan (2019-08-16 00:30 UTC)

<p>Until very recently DICOM did not support floating-point voxel types at all (its use is still extremely limited), but instead you store integer voxels and scaling information (rescale slope, intercept, and type values; or modality LUT) as <a class="mention" href="/u/cpinter">@cpinter</a> described above.</p>
<p>Are you sure you need the result in DICOM format? Do you have examples of PK maps stored in DICOM? What do you plan to do with the exported data set?</p>

---

## Post #5 by @madeline (2019-08-16 02:23 UTC)

<p>I can’t upload a .dcm file format here however below is a screenshot showing what happens: Between the conversion of the PK map in Slicer after generation (left-float variables)–&gt; Re-opening the map in Slicer after DICOM export (right)–&gt; Opening the same DICOM image in MATLAB (bottom) : <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bff8f56fb62e7fc417d6fd3734b6dec46d6d7968.jpeg" data-download-href="/uploads/short-url/rogAu90lNE8qA1daxOyBpCmiARO.jpeg?dl=1" title="Picture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff8f56fb62e7fc417d6fd3734b6dec46d6d7968_2_665x500.jpeg" alt="Picture2" data-base62-sha1="rogAu90lNE8qA1daxOyBpCmiARO" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff8f56fb62e7fc417d6fd3734b6dec46d6d7968_2_665x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff8f56fb62e7fc417d6fd3734b6dec46d6d7968_2_997x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bff8f56fb62e7fc417d6fd3734b6dec46d6d7968_2_1330x1000.jpeg 2x" data-dominant-color="4E4A62"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture2</span><span class="informations">1432×1076 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My analysis on the images I need to perform in MATLAB which has a simple DICOM reader function that I have used in the past. Perhaps saving in another format you’d suggest that keeps float variables and is easily implemented to MATLAB could be a better option (e.g. TIFF)?</p>

---

## Post #6 by @lassoan (2019-08-16 04:39 UTC)

<p>To share data between Slicer and Matlab, I would not recommend using DICOM, especially if you want to minimize information loss and you don’t have a clear idea how PK maps should be stored in DICOM in a standard-compliant way.</p>
<p>Probably the most forward-looking solution is to not bother with Matlab anymore and implement your analysis in Python. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" rel="nofollow noopener">here</a>.</p>
<p>Second option is to use Slicer’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" rel="nofollow noopener">MatlabBridge extension</a>, which allows running a function implemented in Matlab directly from Slicer (the bridge takes care of passing data between Slicer and Matlab).</p>
<p>Third option is to save the image to a nrrd file and manually read it into Matlab using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m" rel="nofollow noopener">nrrdread.m</a>.</p>

---

## Post #7 by @madeline (2019-08-20 01:27 UTC)

<p>Is there a way to check if you are losing data between Slicer and MATLAB? I found an alternative method using advice given from the <a href="https://discourse.slicer.org/t/normalization-calibration/1420/5" class="inline-onebox">Normalization/calibration - #5 by fedorov</a> thread , and in particular using the ShiftScaleImageFilter on each of the maps. Since now I know DICOM format only accepts integer values on Slicer, then by scaling each map by 1000 (or to whichever accuracy needed) prior to export, then you can keep the decimal values and just re-scale back within MATLAB easy enough (see image below). Not sure about data-loss in this process though.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4db66cd74c5c2b0afd6605a68ef3e4ec310ef99.png" data-download-href="/uploads/short-url/un1hWANifZcnIZmecjfrRcDcYm5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4db66cd74c5c2b0afd6605a68ef3e4ec310ef99_2_319x249.png" alt="image" data-base62-sha1="un1hWANifZcnIZmecjfrRcDcYm5" width="319" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4db66cd74c5c2b0afd6605a68ef3e4ec310ef99_2_319x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4db66cd74c5c2b0afd6605a68ef3e4ec310ef99_2_478x373.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d4db66cd74c5c2b0afd6605a68ef3e4ec310ef99_2_638x498.png 2x" data-dominant-color="4042A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1722×1347 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2019-08-21 16:30 UTC)

<p>Both Slicer and Matlab supports floating-point voxels, so you can save the image as is into nrrd file in Slicer and load it into Matlab. No need to convert the voxels to integer.</p>

---

## Post #9 by @madeline (2019-08-25 10:46 UTC)

<p>I have got the nrrd reader up and running, and it is a much easier method to implement! Thank you Andras.</p>

---

## Post #10 by @fedorov (2019-08-26 15:44 UTC)

<aside class="quote no-group" data-username="madeline" data-post="7" data-topic="8038">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e47774/48.png" class="avatar"> madeline:</div>
<blockquote>
<p>Since now I know DICOM format only accepts integer values on Slicer</p>
</blockquote>
</aside>
<p>Slicer can also load floating-point parametric map objects, if you install Quantitative Reporting extension. Those parametric maps are not very common, but DICOM does support floating point <code>PixelData</code> for parametric maps.</p>

---
