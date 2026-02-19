---
topic_id: 17173
title: "Problem With Radiomics When Bin Width Set To 0 01"
date: 2021-04-19
url: https://discourse.slicer.org/t/17173
---

# Problem with Radiomics when Bin Width set to 0.01

**Topic ID**: 17173
**Date**: 2021-04-19
**URL**: https://discourse.slicer.org/t/problem-with-radiomics-when-bin-width-set-to-0-01/17173

---

## Post #1 by @Marg (2021-04-19 14:28 UTC)

<p>Hi. I am using 3D Slicer version 4.11.2020930. Last week I was able to perform Radiomics extraction with bin width 0.01 with no issues. Today on the same data set I get a blank table when Bin Width is set to 0.01. It seems to work OK for all other bin widths (at least the few others I tried).</p>
<p>A portion of the error log:<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - [2021-04-19 14:47:20] I: radiomics.featureextractor: Calculating features for original image<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - [2021-04-19 14:47:20] I: radiomics.featureextractor: Computing firstorder<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - [2021-04-19 14:47:20] I: radiomics.featureextractor: Computing glcm<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - [2021-04-19 14:47:20] E: radiomics.script: Feature extraction failed!<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - Traceback (most recent call last):<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\scripts\segment.py”, line 70, in _extractFeatures<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     feature_vector.update(extractor.execute(imageFilepath, maskFilepath, label, label_channel))<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\featureextractor.py”, line 330, in execute<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     featureVector.update(self.computeFeatures(inputImage, inputMask, imageTypeName, *<em>inputKwargs))<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\featureextractor.py”, line 517, in computeFeatures<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     for (featureName, featureValue) in six.iteritems(featureClass.execute()):<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\base.py”, line 185, in execute<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     self._calculateSegment()<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\base.py”, line 224, in _calculateSegment<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     for success, featureName, featureValue in self._calculateFeatures():<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\base.py”, line 231, in _calculateFeatures<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     self._initCalculation(voxelCoordinates)<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\glcm.py”, line 111, in _initCalculation<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     self.P_glcm = self._calculateMatrix(voxelCoordinates)<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -   File “C:\Users\jwjmc\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\glcm.py”, line 139, in _calculateMatrix<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -     P_glcm, angles = cMatrices.calculate_glcm(<em>matrix_args)<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - MemoryError<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - [2021-04-19 14:47:20] I: radiomics.script: Processing results…<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - [2021-04-19 14:47:20] I: radiomics.script: Finished segment-based extraction successfully…<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) -<br>
[CRITICAL][Qt] 19.04.2021 14:47:20 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLLabelMapVolumeNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 19.04.2021 14:47:20 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - Extraction complete<br>
[INFO][Stream] 19.04.2021 14:47:20 [] (unknown:0) - Cleaning up…</p>

---

## Post #2 by @pieper (2021-04-19 15:46 UTC)

<aside class="quote no-group" data-username="Marg" data-post="1" data-topic="17173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/34f0e0/48.png" class="avatar"> Marg:</div>
<blockquote>
<p>MemoryError</p>
</blockquote>
</aside>
<p>means your computer ran out of memory, probably because that’s a small bin width relative to the range of data files.  If you ran the same data before and it worked maybe this time you have too many other things running at the same time using memory.</p>

---
