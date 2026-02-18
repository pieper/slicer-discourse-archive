# Unable to export segmentation object

**Topic ID**: 33146
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/unable-to-export-segmentation-object/33146

---

## Post #1 by @arfei1234 (2023-11-30 13:55 UTC)

<p>Hi,</p>
<p>I’ve been trying to export my segmentation object as dicom and am unable to do so.<br>
I am using the latest nightly build 5.7.0 and the latest SlicerRT and Quantitative Reporting plugin with all the dependencies.</p>
<p>I have tried to reinstall Slicer and reset the config file, but still unable to export the seg obj. Scalar volume and all other DICOM export function works</p>
<p>Heres the error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76e7ceaa15e49ad847fbbf6c1c25936f1a2cbfc0.jpeg" data-download-href="/uploads/short-url/gXSZ9r4FkdxR070fyI42DEIfGFy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e7ceaa15e49ad847fbbf6c1c25936f1a2cbfc0_2_527x500.jpeg" alt="image" data-base62-sha1="gXSZ9r4FkdxR070fyI42DEIfGFy" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e7ceaa15e49ad847fbbf6c1c25936f1a2cbfc0_2_527x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e7ceaa15e49ad847fbbf6c1c25936f1a2cbfc0_2_790x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76e7ceaa15e49ad847fbbf6c1c25936f1a2cbfc0_2_1054x1000.jpeg 2x" data-dominant-color="EAE9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1358×1288 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Error log:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efaecd070e3b6ffefdbe2a0a1a363ff1c4058ced.jpeg" data-download-href="/uploads/short-url/yckCJ197XFWYdhPzcXfE2fuLrad.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efaecd070e3b6ffefdbe2a0a1a363ff1c4058ced_2_381x500.jpeg" alt="image" data-base62-sha1="yckCJ197XFWYdhPzcXfE2fuLrad" width="381" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efaecd070e3b6ffefdbe2a0a1a363ff1c4058ced_2_381x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efaecd070e3b6ffefdbe2a0a1a363ff1c4058ced_2_571x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/efaecd070e3b6ffefdbe2a0a1a363ff1c4058ced_2_762x1000.jpeg 2x" data-dominant-color="EFE9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">956×1254 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70f563d6fbf74876b0846720718ca4470f169c14.jpeg" data-download-href="/uploads/short-url/g7hdMFycbF85NVfVBrto2ZNfCoQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70f563d6fbf74876b0846720718ca4470f169c14_2_370x500.jpeg" alt="image" data-base62-sha1="g7hdMFycbF85NVfVBrto2ZNfCoQ" width="370" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70f563d6fbf74876b0846720718ca4470f169c14_2_370x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70f563d6fbf74876b0846720718ca4470f169c14_2_555x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70f563d6fbf74876b0846720718ca4470f169c14_2_740x1000.jpeg 2x" data-dominant-color="EEE8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">914×1232 74.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb995acae1a9565967f07cbff212592212fe757d.jpeg" data-download-href="/uploads/short-url/zTKpamJxmaDOOCqoTHRJQTjMKip.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb995acae1a9565967f07cbff212592212fe757d_2_293x500.jpeg" alt="image" data-base62-sha1="zTKpamJxmaDOOCqoTHRJQTjMKip" width="293" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb995acae1a9565967f07cbff212592212fe757d_2_293x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb995acae1a9565967f07cbff212592212fe757d_2_439x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb995acae1a9565967f07cbff212592212fe757d_2_586x1000.jpeg 2x" data-dominant-color="EDE8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">898×1532 95.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1394308270933d823c5279adeb47c0ae45f81114.jpeg" data-download-href="/uploads/short-url/2Ncz7sE2dtG8ogEE0wB1z8BkUpS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1394308270933d823c5279adeb47c0ae45f81114_2_529x500.jpeg" alt="image" data-base62-sha1="2Ncz7sE2dtG8ogEE0wB1z8BkUpS" width="529" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1394308270933d823c5279adeb47c0ae45f81114_2_529x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/1394308270933d823c5279adeb47c0ae45f81114_2_793x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1394308270933d823c5279adeb47c0ae45f81114.jpeg 2x" data-dominant-color="EEE8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">946×894 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot!</p>

---

## Post #2 by @cpinter (2023-11-30 14:01 UTC)

<p>It seems that the terminology is somehow invalid. If you double-click the color for your segments, does the correct terminology appear in every case, or does it default to something?</p>

---

## Post #3 by @arfei1234 (2023-12-01 01:09 UTC)

<p>Hi，</p>
<p>I checked the terminology and assigned to correct category. However this did not fix the issue. Seems the terminology was not the issue.</p>
<p>I check the error log and found SlicerRTimport export plugin was not detected</p>
<p>Error log:<br>
DICOM Plugin failed: module ‘modules’ has no attribute ‘dicomrtimportexport’</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-5.4/qt-scripted-modules/DICOMLib/DICOMUtils.py”, line 744, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/SlicerRT/lib/Slicer-5.4/qt-scripted-modules/DicomRtImportExportPlugin.py”, line 41, in examineForImport<br>
slicer.modules.dicomrtimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)<br>
AttributeError: module ‘modules’ has no attribute ‘dicomrtimportexport’</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-5.4/qt-scripted-modules/DICOMLib/DICOMUtils.py”, line 744, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examineForImport(fileLists)<br>
File “/Applications/Slicer.app/Contents/Extensions-31938/SlicerRT/lib/Slicer-5.4/qt-scripted-modules/DicomSroImportExportPlugin.py”, line 40, in examineForImport<br>
slicer.modules.dicomsroimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)<br>
AttributeError: module ‘modules’ has no attribute ‘dicomsroimportexport’</p>
<p>Is the SlicerRT import export module critical for Seg Object export? I have ensured that SlicerRT plugin has been installed and enabled. Is it possible to install the plugin from file?</p>
<p>Thanks</p>

---
