---
topic_id: 43059
title: "Automated Dental Tools Ali Fail"
date: 2025-05-23
url: https://discourse.slicer.org/t/43059
---

# Automated Dental Tools ALI fail

**Topic ID**: 43059
**Date**: 2025-05-23
**URL**: https://discourse.slicer.org/t/automated-dental-tools-ali-fail/43059

---

## Post #1 by @eric6 (2025-05-23 11:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f0acb14d01b95b19ab7f15113e31f854ce5840.png" data-download-href="/uploads/short-url/qfd1eTat64NscoKu5q3VfyVhuEg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f0acb14d01b95b19ab7f15113e31f854ce5840.png" alt="image" data-base62-sha1="qfd1eTat64NscoKu5q3VfyVhuEg" width="690" height="113" data-dominant-color="2B2B2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1420×234 16.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Been trying to run ALI on 5.2.2 but this “ModuleNotFoundError: No module named ‘pydicom.pixels’” keeps popping up. Also tried 5.4.0, 5.6.1, and 5.8.1 and different kinds of error messages appeared. Any fixes to this?</p>

---

## Post #2 by @jamesobutler (2025-05-23 16:02 UTC)

<p>xref conversation regarding <code>pydicom.pixels</code> compatibility issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools/issues/136">
  <header class="source">

      <a href="https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools/issues/136" target="_blank" rel="noopener nofollow ugc">github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools/issues/136" target="_blank" rel="noopener nofollow ugc">ModuleNotFoundError: No module named 'pydicom.pixels' on ALI</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-05-23" data-time="02:38:07" data-timezone="UTC">02:38AM - 23 May 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/eeeric6" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/212992737?v=4" class="onebox-avatar-inline" width="20" height="20">
          eeeric6
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I was trying to run ALI on 5.2.2 but failed due to the error described in the to<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">pic. Any fixes to this?

[VTK] ALI_CBCT standard error:
[VTK] Traceback (most recent call last):
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerAutomatedDentalTools\lib\Slicer-5.2\cli-modules\ALI_CBCT.py", line 59, in &lt;module&gt;
[VTK]     import dicom2nifti
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\__init__.py", line 19, in &lt;module&gt;
[VTK]     from dicom2nifti.convert_dicom import dicom_series_to_nifti
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\convert_dicom.py", line 17, in &lt;module&gt;
[VTK]     import dicom2nifti.common as common
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\common.py", line 16, in &lt;module&gt;
[VTK]     from pydicom.pixels import apply_modality_lut
[VTK] ModuleNotFoundError: No module named 'pydicom.pixels'
[VTK] 
[VTK] During handling of the above exception, another exception occurred:
[VTK] 
[VTK] Traceback (most recent call last):
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerAutomatedDentalTools\lib\Slicer-5.2\cli-modules\ALI_CBCT.py", line 62, in &lt;module&gt;
[VTK]     import dicom2nifti
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\__init__.py", line 19, in &lt;module&gt;
[VTK]     from dicom2nifti.convert_dicom import dicom_series_to_nifti
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\convert_dicom.py", line 17, in &lt;module&gt;
[VTK]     import dicom2nifti.common as common
[VTK]   File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\common.py", line 16, in &lt;module&gt;
[VTK]     from pydicom.pixels import apply_modality_lut
[VTK] ModuleNotFoundError: No module named 'pydicom.pixels'
[VTK] ALI_CBCT completed with errors


 ========= PROCESSED ========= 

ALI_CBCT standard output:

No module named 'logic'

[notice] A new release of pip is available: 23.0 -&gt; 25.1.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip



 ========= ERROR ========= 

CLI execution failed: 
 
ALI_CBCT standard error:

Traceback (most recent call last):
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerAutomatedDentalTools\lib\Slicer-5.2\cli-modules\ALI_CBCT.py", line 59, in &lt;module&gt;
    import dicom2nifti
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\__init__.py", line 19, in &lt;module&gt;
    from dicom2nifti.convert_dicom import dicom_series_to_nifti
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\convert_dicom.py", line 17, in &lt;module&gt;
    import dicom2nifti.common as common
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\common.py", line 16, in &lt;module&gt;
    from pydicom.pixels import apply_modality_lut
ModuleNotFoundError: No module named 'pydicom.pixels'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\SlicerAutomatedDentalTools\lib\Slicer-5.2\cli-modules\ALI_CBCT.py", line 62, in &lt;module&gt;
    import dicom2nifti
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\__init__.py", line 19, in &lt;module&gt;
    from dicom2nifti.convert_dicom import dicom_series_to_nifti
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\convert_dicom.py", line 17, in &lt;module&gt;
    import dicom2nifti.common as common
  File "C:\Users\echau\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\dicom2nifti\common.py", line 16, in &lt;module&gt;
    from pydicom.pixels import apply_modality_lut
ModuleNotFoundError: No module named 'pydicom.pixels'</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
