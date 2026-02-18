# Converting .dcm to .nii.gz

**Topic ID**: 32905
**Date**: 2023-11-19
**URL**: https://discourse.slicer.org/t/converting-dcm-to-nii-gz/32905

---

## Post #1 by @nguess19 (2023-11-19 20:39 UTC)

<p>Howdy,</p>
<p>I am new to Slicer and am trying to convert dicom to nifti files for my project. The only method I have found is SlicerBatchAnonymize. At least one extension I will be using has problems reported with dicom files compared to nifti.</p>
<p>Unfortunately, I get the following errors whenever I try to use it:<br>
1)<br>
2023-11-18 21:04:19.422 Slicer[5291:255759] +[CATransaction synchronize] called within transaction</p>
<p>2023-11-18 21:04:19.660 Slicer[5291:255759] +[CATransaction synchronize] called within transaction<br>
2)<br>
2023-11-18 21:04:25.089 Slicer[5291:255759] +[CATransaction synchronize] called within transaction</p>
<p>2023-11-18 21:04:25.242 Slicer[5291:255759] +[CATransaction synchronize] called within transaction<br>
3)<br>
E: DcmElement: CommandField (0000,0100) larger (828667202) than remaining bytes in file<br>
4)<br>
Export aborted: time data ‘N/A’ does not match format ‘%Y%m%d’</p>
<p>Does anyone know of an alternative extension/method to convert the files?</p>

---

## Post #2 by @rbumm (2023-11-20 00:39 UTC)

<p>Yes, just import the DICOM file via the DICOM manager. Then go to the “Data” module and right click the volume that you want to export as NRRD file.<br>
Select “Export to file…”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6485087ce3daf5a567f83677de52992bf52e2398.png" data-download-href="/uploads/short-url/eleLH3J7VrhENPxnz5dscb91FEs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6485087ce3daf5a567f83677de52992bf52e2398_2_690x390.png" alt="image" data-base62-sha1="eleLH3J7VrhENPxnz5dscb91FEs" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6485087ce3daf5a567f83677de52992bf52e2398_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6485087ce3daf5a567f83677de52992bf52e2398_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6485087ce3daf5a567f83677de52992bf52e2398.png 2x" data-dominant-color="8D8E90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1370×776 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
