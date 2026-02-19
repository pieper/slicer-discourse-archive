---
topic_id: 22871
title: "Create Dicom Series Using Python"
date: 2022-04-08
url: https://discourse.slicer.org/t/22871
---

# Create DICOM series using python

**Topic ID**: 22871
**Date**: 2022-04-08
**URL**: https://discourse.slicer.org/t/create-dicom-series-using-python/22871

---

## Post #1 by @Shambhavi_Malik (2022-04-08 09:08 UTC)

<p>I have nifti (.nii.gz) scalar volumes and I wanted to convert them into DICOM format and extract information from the metadata (IOP and IPP). I had done this manually using the 3D Slicer GUI. As there are multiple nifti files that need to be converted, I wanted to automate the process using the Slicer Python interface. Please see the code below.</p>
<pre><code class="lang-auto">import slicer
volume = slicer.util.loadVolume('C:/Users/shamb/Downloads/110122_CE_2ch.nii.gz')
dicomWrite = slicer.modules.createdicomseries
</code></pre>
<p>I am stuck after this step. Manually, I would go to the CreateDICOMSeries module, choose the input volume and select apply. Is there a way to implement these steps in the python interface?</p>

---

## Post #2 by @Shambhavi_Malik (2022-04-08 11:49 UTC)

<p>Edit:<br>
I have also come across the DICOMExportScalarVolume from DICOMLib and tried nifti to DICOM conversion. Please see the code below:</p>
<pre><code class="lang-auto">import slicer
from DICOMLib import DICOMExportScalarVolume
volume = slicer.util.loadVolume('C:/Users/shamb/OneDrive/Desktop/test/110122_CE_2ch.nii.gz')
DICOMExportScalarVolume(volumeNode = volume, studyUID = None, tags = None, directory = 'C:/Users/shamb/Downloads/')
</code></pre>
<p>This code snippet runs successfully and generates a DICOMExportScalarVolume object. But upon examining the DICOM metadata no information is visible. Please see the image attached.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48ed598c697542da1ff1d9b3a63717ab920014cf.png" data-download-href="/uploads/short-url/ap8TDSrSLkLBl6q3JKGegiGspJ5.png?dl=1" title="Screenshot (122)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ed598c697542da1ff1d9b3a63717ab920014cf_2_690x366.png" alt="Screenshot (122)" data-base62-sha1="ap8TDSrSLkLBl6q3JKGegiGspJ5" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ed598c697542da1ff1d9b3a63717ab920014cf_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ed598c697542da1ff1d9b3a63717ab920014cf_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48ed598c697542da1ff1d9b3a63717ab920014cf_2_1380x732.png 2x" data-dominant-color="F1F4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (122)</span><span class="informations">1920×1019 91.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I did not face this issue while using the CreateDICOMSeries module GUI.<br>
I can’t figure out where I’m going wrong and would greatly appreciate some help.<br>
Thanks in advance!</p>

---

## Post #3 by @lassoan (2022-04-09 12:11 UTC)

<p>If you just need to export images then you can use the CreateDICOMSeries module. It is a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">CLI module that you can run from Python</a>.</p>
<p>If you want to be able to export other DICOM data objects (e.g., segmentation, RT structure set, …) then you can use export plugins of the DICOM module as shown in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format">script repository</a>.</p>

---

## Post #4 by @Shambhavi_Malik (2022-04-09 12:22 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a> this works!</p>

---
