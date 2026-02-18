# Is my perfusion file incomplete or am I incorrectly importing it? (DSC -> rCBV)

**Topic ID**: 43399
**Date**: 2025-06-17
**URL**: https://discourse.slicer.org/t/is-my-perfusion-file-incomplete-or-am-i-incorrectly-importing-it-dsc-rcbv/43399

---

## Post #1 by @SegmenterSam (2025-06-17 19:41 UTC)

<p>Hello,</p>
<p>I have a patient with a perfusion MRI which counts 925 slides originally in their electronic file. When exporting this file, our exporting software creates a folder with 37 files (925/25) and loading it into 3DSlicer through the Add DICOM Data module, it loads and is visible as a 3D image with 37 Slices<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d41cd3b058f0bef15082bb176b338f63e873863.png" data-download-href="/uploads/short-url/8JU6wck5d53j7CQezVdvqAsJlOr.png?dl=1" title="Schermafbeelding 2025-06-17 212531" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d41cd3b058f0bef15082bb176b338f63e873863_2_690x400.png" alt="Schermafbeelding 2025-06-17 212531" data-base62-sha1="8JU6wck5d53j7CQezVdvqAsJlOr" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d41cd3b058f0bef15082bb176b338f63e873863_2_690x400.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d41cd3b058f0bef15082bb176b338f63e873863.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d41cd3b058f0bef15082bb176b338f63e873863.png 2x" data-dominant-color="535053"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermafbeelding 2025-06-17 212531</span><span class="informations">1002×582 96.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, the actual file format of these 37 files is a mystery to me as they are just named “file” and not a specific extension. Only through the Add DICOM Data module will they load properly.</p>
<p>A part of me thinks that the 4D data must somehow be embedded in these 37 files since the original is 925 slices and our exporter gives us 925/25 = 37 files. I am wondering if you have any leads for me to find out if this is actually the case, or if my search is futile because the file is just exporting erroneously.</p>
<p>I have tried to save this file as a .nii and loading it in through MultiVolumeImporter but this loads it as a 1 frame MultiVolume. This to me indicates that there is no timedata, but I might also be doing that myself by saving it as a .nii?</p>
<p>My ultimate goal is to use this scan to create an rCBV map of the perfusion scan, using the MultiVolumeImporter and DSCMRI-Analysis modules, and I haven’t been able to yet.</p>
<p>I’m super thankful for any unput or leads on where to go from here.</p>

---

## Post #2 by @pieper (2025-06-17 20:52 UTC)

<p>It’s possible that each of the 37 timepoints is a single volume file, but that’s not very common.  More likely only one timepoint was exported.  One easy way to check is to look at the file size.  If it’s about 128k then it’s probably one MR slice.  If it’s 25 times bigger it might be a full volume in a multiframe format (but again, that’s very rare).</p>

---

## Post #3 by @SegmenterSam (2025-06-18 21:21 UTC)

<p>Hi Pieper,</p>
<p>Thanks for you answer. It seems that it just the single 37 slices without time data then, considering the file size. Thank you for helping me along; at least I now know that the problem is on the data extraction side of things.</p>
<p>Sam</p>

---

## Post #4 by @SegmenterSam (2025-06-20 15:36 UTC)

<p>Hi Pieper,</p>
<p>I have now been able to extract a perfusion MRI in a .nii format (this is the only file I have), which properly loads via the MultiVolumeImporter and shows 80 timeframes in the MultiVolumeExplorer, it also plays here and correctly displays a bolus being administered over time.</p>
<p>Inputting this 80 frame NIfTI MultiVolume and outputting rCBV in DSCMRIAnalysis gives the following errorcode:</p>
<p>Description: ITK ERROR: ITK ERROR: Unrecognized frame identifying DICOM tag name  Image C:/Users/[myname]/AppData/Local/Temp/Slicer/BFJIE_vtkMRMLMultiVolumeNodeB.nrrd does not contain sufficient attributes to support algorithms.</p>
<p>I found this question on previous posts on the forum but didn’t really grasp what the core problem is.</p>
<p>Is this, once again an exporting problem or can I somehow fix this with my .nii file?</p>
<p>I feel like I’m very close to resolving this…</p>
<p>Sam</p>

---

## Post #5 by @pieper (2025-06-20 15:44 UTC)

<p>Unfortunately time-series data comes in all kinds of formats and conventions.  I personally haven’t worked with perfusion MR data with these tools, but generally speaking if things aren’t working “out of the box” you need to do a bit of programming to make it work (and to confirm that you actually have the data you think you have).  The best path is to have the full dicom dataset and make sure it has header data like timing and geometry information needed to correctly interpret the timeseries.  Even then, depending on the vendor or sequence used there may be incompatibilities.</p>
<p>Once you have nii, not only is the timing information gone, but there are possible ambiguities such as left-right flip that may happen, especially for 4D data.  So you need to know exactly what pipeline converted the scan to nii to be really sure you can figure out how to use it.</p>
<p>Sorry to be negative here, but this data is pretty hard to work with due to factors outside our control.  The only real option for robustness is to dig into the details whole pipeline from acquisition to analysis.</p>

---
