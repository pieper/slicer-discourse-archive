---
topic_id: 18474
title: "Error In Extractfeatures When Using Pyradiomics In Slicer"
date: 2021-07-02
url: https://discourse.slicer.org/t/18474
---

# Error in _extractFeatures when using pyradiomics in Slicer

**Topic ID**: 18474
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/error-in-extractfeatures-when-using-pyradiomics-in-slicer/18474

---

## Post #1 by @retidani18 (2021-07-02 03:19 UTC)

<p>Hi !</p>
<p>I am trying to do radiomic analysis on a 3D lung sample. The segmentation is ready but I only get an error massage. It looks like there is some problem with the masks but I am not sure at all. Any suggestions?</p>
<p>Here is the whole massage from the code:<br>
Starting RadiomicsCLI for RBC_train_largesmallarteryplusspeackle_segment_Speckle</p>
<p>…Done</p>
<p>[2021-07-01 21:38:26] I: radiomics.script: Starting PyRadiomics (version: v3.0.1.post4+gad5b2de)</p>
<p>[2021-07-01 21:38:26] I: radiomics.script: Processing input…</p>
<p>[2021-07-01 21:38:26] I: radiomics.featureextractor: Loading parameter file C:/Users/lantis.user/AppData/Local/Temp/Slicer\RadiomicsLogicParams.json</p>
<p>[2021-07-01 21:38:26] I: radiomics.featureextractor: Applying custom setting overrides: {‘label’: 1, ‘correctMask’: True}</p>
<p>[2021-07-01 21:38:26] I: radiomics.script: Input valid, starting sequential extraction from 1 case(s)…</p>
<p>[2021-07-01 21:38:26] I: radiomics.script: Processing case 1</p>
<p>[2021-07-01 21:38:26] I: radiomics.featureextractor: Calculating features with label: 1</p>
<p>[2021-07-01 21:38:26] I: radiomics.featureextractor: Loading image and mask</p>
<p>[2021-07-01 21:38:36] E: radiomics.script: Feature extraction failed!</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\Users\lantis.user\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerRadiomics\Lib\site-packages\radiomics\scripts\segment.py”, line 70, in _extractFeatures</p>
<p>feature_vector.update(extractor.execute(imageFilepath, maskFilepath, label, label_channel))</p>
<p>File “C:\Users\lantis.user\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerRadiomics\Lib\site-packages\radiomics\featureextractor.py”, line 272, in execute</p>
<p>image, mask = self.loadImage(imageFilepath, maskFilepath, generalInfo, **_settings)</p>
<p>File “C:\Users\lantis.user\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\SlicerRadiomics\Lib\site-packages\radiomics\featureextractor.py”, line 382, in loadImage</p>
<p>raise ValueError(‘Error reading mask Filepath or SimpleITK object’)</p>
<p>ValueError: Error reading mask Filepath or SimpleITK object</p>
<p>[2021-07-01 21:38:37] I: radiomics.script: Processing results…</p>
<p>[2021-07-01 21:38:37] I: radiomics.script: Finished segment-based extraction successfully…</p>
<p>Extraction complete</p>
<p>Cleaning up…</p>

---

## Post #2 by @fedorov (2021-09-28 19:57 UTC)

<p>I have not been able to identify the exact issue so far, but as a workaround you can export your segmentation as a labelmap (using the section below from the Segmentations module), and then use theresulting labelmap node as “Input regions” parameter in the Radiomics module. This worked for me.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dae46cd03a4cbeae709404ca634d8857db4e793c.png" alt="image" data-base62-sha1="vepubVRIg2vbQK8cCpQHeZNQuRu" width="502" height="243"></p>

---

## Post #3 by @fedorov (2021-09-28 20:30 UTC)

<p>I filed an issue, will try to get back to it: <a href="https://github.com/AIM-Harvard/SlicerRadiomics/issues/67" class="inline-onebox">Cannot use the module with input mask defined by a segmentation node · Issue #67 · AIM-Harvard/SlicerRadiomics · GitHub</a>.</p>

---
