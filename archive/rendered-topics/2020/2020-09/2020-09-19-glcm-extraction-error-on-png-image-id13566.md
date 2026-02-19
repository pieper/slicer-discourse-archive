---
topic_id: 13566
title: "Glcm Extraction Error On Png Image"
date: 2020-09-19
url: https://discourse.slicer.org/t/13566
---

# GLCM extraction error on .png image

**Topic ID**: 13566
**Date**: 2020-09-19
**URL**: https://discourse.slicer.org/t/glcm-extraction-error-on-png-image/13566

---

## Post #1 by @Shibashis_Sahu (2020-09-19 14:46 UTC)

<p>Operating system: Windows 10<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
HI,<br>
I am new to pyradiomics and getting an error while extracting using GLCM, here is my code:</p>
<p>ig = sitk.ReadImage(’./PAC_14_DN0.png’, sitk.sitkUInt8)<br>
print(ig.GetSize())<br>
print(ig)<br>
image3d = sitk.JoinSeries(ig)<br>
msk = sitk.ReadImage(’./mask1.png’, sitk.sitkUInt8)<br>
print(msk.GetSize())<br>
print(msk)<br>
msk3d = sitk.JoinSeries(msk)</p>
<p>feature = radiomics.glcm.RadiomicsGLCM(image3d, msk3d, label=255)<br>
print(feature.getAutocorrelationFeatureValue())<br>
output:<br>
(190, 250)<br>
Image (0000022AFBBD4110)<br>
RTTI typeinfo:   class itk::Image&lt;unsigned char,2&gt;<br>
Reference Count: 1<br>
Modified Time: 945<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Source: (none)<br>
Source output name: (none)<br>
Release Data: Off<br>
Data Released: False<br>
Global Release Data: Off<br>
PipelineMTime: 935<br>
UpdateMTime: 944<br>
RealTimeStamp: 0 seconds<br>
LargestPossibleRegion:<br>
Dimension: 2<br>
Index: [0, 0]<br>
Size: [190, 250]<br>
BufferedRegion:<br>
Dimension: 2<br>
Index: [0, 0]<br>
Size: [190, 250]<br>
RequestedRegion:<br>
Dimension: 2<br>
Index: [0, 0]<br>
Size: [190, 250]<br>
Spacing: [1, 1]<br>
Origin: [0, 0]<br>
Direction:<br>
1 0<br>
0 1</p>
<p>IndexToPointMatrix:<br>
1 0<br>
0 1</p>
<p>PointToIndexMatrix:<br>
1 0<br>
0 1</p>
<p>Inverse Direction:<br>
1 0<br>
0 1</p>
<p>PixelContainer:<br>
ImportImageContainer (0000022A801703A0)<br>
RTTI typeinfo:   class itk::ImportImageContainer&lt;unsigned __int64,unsigned char&gt;<br>
Reference Count: 1<br>
Modified Time: 941<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Pointer: 0000022A8025DD10<br>
Container manages memory: true<br>
Size: 47500<br>
Capacity: 47500</p>
<p>(190, 250)<br>
Image (0000022AFBBD4680)<br>
RTTI typeinfo:   class itk::Image&lt;unsigned char,2&gt;<br>
Reference Count: 1<br>
Modified Time: 1139<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Source: (none)<br>
Source output name: (none)<br>
Release Data: Off<br>
Data Released: False<br>
Global Release Data: Off<br>
PipelineMTime: 1129<br>
UpdateMTime: 1138<br>
RealTimeStamp: 0 seconds<br>
LargestPossibleRegion:<br>
Dimension: 2<br>
Index: [0, 0]<br>
Size: [190, 250]<br>
BufferedRegion:<br>
Dimension: 2<br>
Index: [0, 0]<br>
Size: [190, 250]<br>
RequestedRegion:<br>
Dimension: 2<br>
Index: [0, 0]<br>
Size: [190, 250]<br>
Spacing: [1, 1]<br>
Origin: [0, 0]<br>
Direction:<br>
1 0<br>
0 1</p>
<p>IndexToPointMatrix:<br>
1 0<br>
0 1</p>
<p>PointToIndexMatrix:<br>
1 0<br>
0 1</p>
<p>Inverse Direction:<br>
1 0<br>
0 1</p>
<p>PixelContainer:<br>
ImportImageContainer (0000022A80171750)<br>
RTTI typeinfo:   class itk::ImportImageContainer&lt;unsigned __int64,unsigned char&gt;<br>
Reference Count: 1<br>
Modified Time: 1135<br>
Debug: Off<br>
Object Name:<br>
Observers:<br>
none<br>
Pointer: 0000022A80275050<br>
Container manages memory: true<br>
Size: 47500<br>
Capacity: 47500<br>
KeyError                                  Traceback (most recent call last)<br>
 in ()<br>
1 # feature.enableAllFeatures()<br>
2 # feature.calculateFeatures()<br>
----&gt; 3 print(feature.getAutocorrelationFeatureValue())</p>
<p>F:\Programs\Anaconda3\lib\site-packages\radiomics\glcm.py in getAutocorrelationFeatureValue(self)<br>
253     Autocorrelation is a measure of the magnitude of the fineness and coarseness of texture.<br>
254     “”"<br>
–&gt; 255     i = self.coefficients[‘i’]<br>
256     j = self.coefficients[‘j’]<br>
257     ac = numpy.sum(self.P_glcm * (i * j)[None, :, :, None], (1, 2))</p>
<p>KeyError: ‘i’</p>
<p>Thanks in advance.</p>

---

## Post #2 by @JoostJM (2020-09-30 11:38 UTC)

<p>This bug occurs due to incorrect usage of the featureclass in standalone version.<br>
Through directly calling the feature function, important initialization steps are skipped.</p>
<p>Recommended usage is through the featureextractor module (as this also implements important preprocessing code and checks). See <a href="https://pyradiomics.readthedocs.io/en/latest/usage.html#interactive-use">interactive use</a>.</p>
<p>Using the feature classes directly is still possible, but only recommended for developers’ use. See <a href="https://pyradiomics.readthedocs.io/en/latest/developers.html#using-feature-classes-directly">using feature classes directly</a></p>

---
