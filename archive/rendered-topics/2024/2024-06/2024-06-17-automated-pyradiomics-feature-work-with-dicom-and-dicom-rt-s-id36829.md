---
topic_id: 36829
title: "Automated Pyradiomics Feature Work With Dicom And Dicom Rt S"
date: 2024-06-17
url: https://discourse.slicer.org/t/36829
---

# Automated PyRadiomics Feature work with DICOM and DICOM RT structure

**Topic ID**: 36829
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/automated-pyradiomics-feature-work-with-dicom-and-dicom-rt-structure/36829

---

## Post #1 by @youngchanseo (2024-06-17 02:35 UTC)

<p>Hello.</p>
<p>I have already installed pyradiomics and Slicer RT via extension manager.</p>
<p>In the DICOM RT structure file, there are contour data for regions of interest (ROIs) [1]) of the tumor shape.<br>
In the DICOM file, I have an MRI of the patient.<br>
I searched for Radiomics in the 3d slicer’s module and ran it. I put the DICOM RT file in the “input regions” and the MR image in the “Input Image Volume”.<br>
As shown in the image below, I was able to successfully extract the Radiomics Features from the MR image of the ROI (Tumor).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287.jpeg" data-download-href="/uploads/short-url/xdJaCbALZcW307ZZZENt5cjS62P.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_483x500.jpeg" alt="image" data-base62-sha1="xdJaCbALZcW307ZZZENt5cjS62P" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_483x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_724x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8d505b29f3e7f83e19ddacd274c81a6b0d3a287_2_966x1000.jpeg 2x" data-dominant-color="3C3B58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×1207 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i need to do these operations multiple times. So I want to do these labor intensive things automatically.<br>
Is it possible to automate this with python code?<br>
For example, I have 100 RT structure (outlined tumor regions) DICOM files and 100 DICOM (MR brain) images, can I use code to automatically extract features in pyRadiomics &amp; 3d slicer to do the work at once?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419.png" data-download-href="/uploads/short-url/3B3UGvw9q0PfN2II0BuV6m8sZWV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419_2_690x337.png" alt="image" data-base62-sha1="3B3UGvw9q0PfN2II0BuV6m8sZWV" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/193710cbbe9342f360ea7963dc4a0d2db99a9419.png 2x" data-dominant-color="C9C6CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">995×486 75.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to do this with the python code with Google colab &amp; gpt4 (microsoft bing), but i failed to do it.</p>
<p>Here is the code:</p>
<p>"# Install necessary libraries<br>
!pip install pydicom<br>
!pip install pyradiomics<br>
!pip install SimpleITK</p>
<h1><a name="p-112789-mount-google-drive-1" class="anchor" href="#p-112789-mount-google-drive-1" aria-label="Heading link"></a>Mount Google Drive</h1>
<p>from google.colab import drive<br>
drive.mount(‘/content/gdrive’)</p>
<h1><a name="p-112789-import-libraries-2" class="anchor" href="#p-112789-import-libraries-2" aria-label="Heading link"></a>Import libraries</h1>
<p>import os<br>
import pydicom<br>
import SimpleITK as sitk<br>
from radiomics import featureextractor<br>
import six</p>
<h1><a name="p-112789-set-file-paths-3" class="anchor" href="#p-112789-set-file-paths-3" aria-label="Heading link"></a>Set file paths</h1>
<p>dicom_dir = “/content/gdrive/MyDrive/MNG_Sample_001”<br>
mask_file = os.path.join(dicom_dir, “RTSS.dcm”)</p>
<h1><a name="p-112789-load-dicom-files-4" class="anchor" href="#p-112789-load-dicom-files-4" aria-label="Heading link"></a>Load DICOM files</h1>
<p>dicom_files = [os.path.join(dicom_dir, f) for f in os.listdir(dicom_dir) if f.startswith(‘IMG’) and f.endswith(‘.dcm’)]<br>
dicom_files.sort(key=lambda x: int(x.split(‘IMG’)[-1].split(‘.dcm’)[0]))</p>
<h1><a name="p-112789-load-dicom-image-5" class="anchor" href="#p-112789-load-dicom-image-5" aria-label="Heading link"></a>Load DICOM image</h1>
<p>reader = sitk.ImageSeriesReader()<br>
reader.SetFileNames(dicom_files)<br>
image = reader.Execute()</p>
<h1><a name="p-112789-load-dicom-rt-structure-set-file-as-mask-6" class="anchor" href="#p-112789-load-dicom-rt-structure-set-file-as-mask-6" aria-label="Heading link"></a>Load DICOM RT Structure Set file as mask</h1>
<p>mask = sitk.ReadImage(mask_file)</p>
<h1><a name="p-112789-set-pyradiomics-parameters-7" class="anchor" href="#p-112789-set-pyradiomics-parameters-7" aria-label="Heading link"></a>Set PyRadiomics parameters</h1>
<p>params = {}<br>
params[‘binWidth’] = 25<br>
params[‘resampledPixelSpacing’] = None<br>
params[‘interpolator’] = ‘sitkBSpline’<br>
params[‘enableCExtensions’] = True</p>
<p>extractor = featureextractor.RadiomicsFeatureExtractor(**params)</p>
<h1><a name="p-112789-extract-features-8" class="anchor" href="#p-112789-extract-features-8" aria-label="Heading link"></a>Extract features</h1>
<p>result = extractor.execute(image, mask)</p>
<h1><a name="p-112789-print-results-9" class="anchor" href="#p-112789-print-results-9" aria-label="Heading link"></a>Print results</h1>
<p>for key, val in six.iteritems(result):<br>
print(“\t%s: %s” % (key, val))<br>
"</p>
<p>[1] <a href="https://kr.mathworks.com/help/images/create-and-display-3-d-mask-of-dicom-rt-contour-data.html" rel="noopener nofollow ugc">Create and Display 3-D Mask of DICOM-RT Contour Data - MATLAB &amp; Simulink - MathWorks 한국</a></p>

---
