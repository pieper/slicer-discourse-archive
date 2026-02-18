# Fixes label for dicom image

**Topic ID**: 24116
**Date**: 2022-06-30
**URL**: https://discourse.slicer.org/t/fixes-label-for-dicom-image/24116

---

## Post #1 by @Van_Tran_Sang_Huynh (2022-06-30 12:09 UTC)

<p>I use dicom dataset for feature extraction. But I got an error about ‘label’. Hoping for help</p>
<p>from <strong>future</strong> import print_function<br>
import six<br>
import os  # needed navigate the system to get the input data</p>
<p>import matplotlib.pyplot as plt<br>
import SimpleITK as sitk<br>
import pydicom as dicom</p>
<p>import radiomics<br>
from radiomics import featureextractor  # This module is used for interaction with pyradiomics</p>
<h1><a name="p-80238-get-the-testcase-1" class="anchor" href="#p-80238-get-the-testcase-1" aria-label="Heading link"></a>Get the testCase</h1>
<p>maskPath =(‘D:/NSCLC data CT paitent/manifest-1603198545583/NSCLC-Radiomics/LUNG1-001/09-18-2008-StudyID-NA-69331/300.000000-Segmentation-9.554/1-1.dcm’)<br>
imagePath = (‘D:/NSCLC data CT paitent/manifest-1603198545583/NSCLC-Radiomics/LUNG1-001/09-18-2008-StudyID-NA-69331/0.000000-NA-82046/1-068.dcm’)<br>
<a class="hashtag-cooked" href="/tag/radiomics" data-type="tag" data-slug="radiomics" data-id="99" data-style-type="icon" data-icon="tag"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>radiomics</span></a>.getTestCase<br>
image = sitk.ReadImage(imagePath)<br>
mask = sitk.ReadImage(maskPath)<br>
ndImg = sitk.GetArrayFromImage(image)<br>
ndLbl = sitk.GetArrayFromImage(mask)<br>
plt.imshow(ndImg[0])<br>
plt.show()<br>
plt.imshow(ndLbl[0])<br>
plt.show()</p>
<p>if imagePath is None or maskPath is None:  # Something went wrong, in this case PyRadiomics will also log an error<br>
raise Exception(‘Error getting testcase!’)  # Raise exception to prevent cells below from running in case of “run all”</p>
<h1><a name="p-80238-additonally-store-the-location-of-the-example-parameter-file-stored-in-pyradiomicsexamplesexamplesettings-2" class="anchor" href="#p-80238-additonally-store-the-location-of-the-example-parameter-file-stored-in-pyradiomicsexamplesexamplesettings-2" aria-label="Heading link"></a>Additonally, store the location of the example parameter file, stored in \pyradiomics\examples/exampleSettings</h1>
<p>paramPath = os.path.join(‘..’, ‘examples’, ‘exampleSettings’, ‘Params.yaml’)<br>
print(‘Parameter file, absolute path:’, os.path.abspath(paramPath))</p>
<h1><a name="p-80238-instantiate-the-extractor-3" class="anchor" href="#p-80238-instantiate-the-extractor-3" aria-label="Heading link"></a>Instantiate the extractor</h1>
<p>extractor = featureextractor.RadiomicsFeatureExtractor()</p>
<p>print(‘Extraction parameters:\n\t’, extractor.settings)<br>
print(‘Enabled filters:\n\t’, extractor.enabledImagetypes)<br>
print(‘Enabled features:\n\t’, extractor.enabledFeatures)</p>
<p>settings = {‘label’: 255}</p>
<p>extractor = radiomics.featureextractor.RadiomicsFeatureExtractor(additionalInfo=True, **settings)</p>
<p>result = extractor.execute(imagePath, maskPath)</p>
<p>print(‘Result type:’, type(result))  # result is returned in a Python ordered dictionary)<br>
print(‘’)<br>
print(‘Calculated features’)<br>
for key, value in six.iteritems(result):<br>
print(‘\t’, key, ‘:’, value)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec70297df3698af7863a5c4a94b1195e8bee6c11.png" data-download-href="/uploads/short-url/xJCZkmUSXGUc0Qm2XeiVp9Qp13X.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec70297df3698af7863a5c4a94b1195e8bee6c11_2_690x388.png" alt="image" data-base62-sha1="xJCZkmUSXGUc0Qm2XeiVp9Qp13X" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec70297df3698af7863a5c4a94b1195e8bee6c11_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec70297df3698af7863a5c4a94b1195e8bee6c11_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec70297df3698af7863a5c4a94b1195e8bee6c11_2_1380x776.png 2x" data-dominant-color="FAF2F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 459 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
