# MultiFrame DICOM: problem with DicomScalarVolumPlugin proglem

**Topic ID**: 8223
**Date**: 2019-08-29
**URL**: https://discourse.slicer.org/t/multiframe-dicom-problem-with-dicomscalarvolumplugin-proglem/8223

---

## Post #1 by @pdeman (2019-08-29 08:00 UTC)

<p>I am having a problem opening multiframe (volume) dicom.</p>
<p>the geometry is not loaded correctly (pixel spacing, slice thickness etc …).<br>
it tries to open it using DICOMScalarVolumPlugin.py and line 640 approximately, in sliceCornersFromDICOM, it “wants” a list of uids.<br>
but as it is a multiframe dicom, it has only one uid for the whole volume.</p>
<p>I don’t get why it is looking for more than one uid in case of multiframe dicom.</p>
<p>is there a way to load the geometry correctly ?</p>

---

## Post #2 by @Chris_Rorden (2019-08-29 11:54 UTC)

<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerDcm2nii" rel="nofollow noopener">SlicerDcm2nii extension</a> should be able to convert enhanced multi-frame images.</p>

---

## Post #3 by @pieper (2019-08-29 11:55 UTC)

<p>That’s a good point - currently the acquisition geometry correction only works for a series of single frames, not for multiframe dicom.  Does your volume actually need geometry correction?  Maybe turn it off (in dicom app preferences) and let us know - possibly this needs better error checking.</p>

---

## Post #4 by @pdeman (2019-08-29 12:01 UTC)

<p>What do you mean by geometry correction ?</p>
<p>it doesn’t take into account the pixel spacing and slice thickness.<br>
while my dicom segment storage, yes.<br>
so I end up with the “raw image” and the segmentation in different “space”.</p>

---

## Post #5 by @pieper (2019-08-29 12:10 UTC)

<p>In the application settings you can enable or disable a geometry regularization - it adds a nonlinear transform to account for irregularly spaced slice (e.g. missing slices) or for things like gantry tilt.  The transform allows you to work with the data as is, or harden the transform at whatever resolution you need.  But as I mentioned it’s only implemented for single frame dicom.  If it’s not enabled multiframe images are delegated to ITK’s reader (either GDCM or DCMTK depending on the settings).</p>
<p>We don’t see very many multiframe datasets, so this path doesn’t get tested much.  Maybe you can describe how the data was acquired, and maybe even shared a deidentified sample (like a volunteer or a phantom).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f06e6190d57b2fabc6207e7f946d9f7d54780856.png" data-download-href="/uploads/short-url/yiX5aqHccIT3GwhnEdLc9z37Zr0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f06e6190d57b2fabc6207e7f946d9f7d54780856_2_690x292.png" alt="image" data-base62-sha1="yiX5aqHccIT3GwhnEdLc9z37Zr0" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f06e6190d57b2fabc6207e7f946d9f7d54780856_2_690x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f06e6190d57b2fabc6207e7f946d9f7d54780856_2_1035x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f06e6190d57b2fabc6207e7f946d9f7d54780856_2_1380x584.png 2x" data-dominant-color="E6E9EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1622×688 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Chris_Rorden (2019-08-29 12:42 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> if you want sample datasets, there are several enhanced Philips MRI datasets available from the <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Computed_Tomography_.28CT.2C_CAT.29" rel="nofollow noopener">dcm2niix wiki</a>. You can find a Siemens enhanced XA10 dataset at the <a href="https://github.com/neurolabusc/dcm_qa_stc" rel="nofollow noopener">dcm_qa_stc repository</a>. The advent of XA10 will effectively force Siemens MR users to enhanced DICOM: the unenhanced 2D images are huge and slow, while the mosaics remove many of the tags required for subsequent analyses (slice position and angulation in particular).</p>
<p>I have never seen an enhanced DICOM CT with gantry tilt. But this may simply because I mostly work in MR. If you do find one that you can share, I would like to take a look.</p>

---

## Post #7 by @pdeman (2019-08-29 13:38 UTC)

<p>I am currently working on opthalmic OCT, and I “generate” myself the DICOM files from the raw data using DCMTK. but yes more and more CT and MRI come in MultiFrame DICOM now.</p>

---

## Post #8 by @Chris_Rorden (2019-08-29 14:36 UTC)

<p><a class="mention" href="/u/pdeman">@pdeman</a> are you using <a href="https://support.dcmtk.org/docs/img2dcm.html" rel="nofollow noopener">img2dcm</a>?  That tool only takes JPEG or BMP inputs. Be aware that JPEG images are limited to 8-bit precision per component (e.g. R,G,B) and are lossy. While BMP is lossless, I think it is also limited to 8-bit precision (e.g. 16, 24 and 32 bits per pixel are shared between components). If your plan is to get this data into Slicer, why not create NRRD files? This would have a simple text data that could describe your raw data with full precision.</p>

---

## Post #9 by @pdeman (2019-08-29 14:59 UTC)

<p>no I am using dcmtk using c++, basically dcmdata, dcmfg, dcmiod and dcmseg dll.<br>
my plan is to get this data into dicom format, put them on a pacs system, use “basic dicom viewer” from hospitals and slicer to view better the segmentation because basic dicom viewer are not optimal for the dicom segmentation storage</p>

---

## Post #10 by @Chris_Rorden (2019-08-29 15:10 UTC)

<p>That sounds like a great approach. Given that dcmtk uses the BSD License, perhaps you might consider sharing your solution on Github. I think a lot of people would find this really useful. The dcmtk code is a great foundation to use - they have done an outstanding job.</p>
<p>As a general comment, enhanced DICOM is very new, and Siemens (XA10) and Philips have taken slightly different approaches. I think many tools still need to be upgraded to handle these files, and several tools have been tuned for these specific vendors. If you find situations where you have DICOM-compliant images that confuse dcm2niix, please consider generating an issue on the dcm2niix Github page. I am sure there will be teething problems for tools as we adapt to this new format.</p>

---

## Post #11 by @pdeman (2019-09-17 08:32 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="10" data-topic="8223">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>Given that dcmtk uses the BSD License, perhaps you might consider sharing your solution on Github.</p>
</blockquote>
</aside>
<p>the export for now is completely mixed with the rest of the software and haven’t done anything particular for now.<br>
I do not have dicom that confuse dcm2niix I think. I will try. MRIConvert works fine with them but I will try dcm2niix.<br>
I haven’t found how to install :<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerDcm2nii#Modules" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Extensions/SlicerDcm2nii - Slicer Wiki</a><br>
I installed  SlicerDMRI which seemed linked, but it didn’t change anything to load the dicom.</p>

---

## Post #12 by @Chris_Rorden (2019-09-23 14:19 UTC)

<p><a class="mention" href="/u/pdeman">@pdeman</a>  were you able to resolve this and if so what was the solution? On Slicer 4.10.2 on MacOS I can install the dcm2niix module like this:</p>
<ol>
<li>View-&gt;Extension Manager, search and install “SlicerDcm2nii” extension</li>
<li>Show “All Modules” and choose Dcm2niixGUI, select the “Input Directory” and select “Apply”</li>
</ol>

---
