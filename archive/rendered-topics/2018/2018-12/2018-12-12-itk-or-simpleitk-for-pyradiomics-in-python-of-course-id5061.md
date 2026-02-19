---
topic_id: 5061
title: "Itk Or Simpleitk For Pyradiomics In Python Of Course"
date: 2018-12-12
url: https://discourse.slicer.org/t/5061
---

# Itk or SimpleItk for PyRadiomics (in python, of course)

**Topic ID**: 5061
**Date**: 2018-12-12
**URL**: https://discourse.slicer.org/t/itk-or-simpleitk-for-pyradiomics-in-python-of-course/5061

---

## Post #1 by @MachadoL (2018-12-12 19:52 UTC)

<p>Operating system: Linux Mint 18<br>
Slicer version:<br>
Expected behavior: Import and read images through Itk Pack<br>
Actual behavior: It gives some errors</p>
<p>Hey guys… what up?</p>
<p>I am working with PyRadiomics in some python scripts and I saw that the examples use SimpleITK for leading the images into the processing pipeline… I’ve tried doing the same with whole ITK pack (imread() function),<br>
but it dioesn’t work propperly…</p>
<p>Is there any constraint on the usage of SimpleITK for Pyradiomics operations?</p>
<ul>
<li>at the end, I post the Error Message!</li>
</ul>
<p>Thanks for yout comensts!<br>
hugs!</p>
<pre><code> Traceback (most recent call last):
 File "FeatureClassExtraction.py", line 49, in &lt;module&gt;
 firstOrderFeatures = radiomics.firstorder.RadiomicsFirstOrder(image, mask, **settings)
 File "/home/leonardo/anaconda3/lib/python3.6/site-packages/radiomics/firstorder.py", line 32, in __init__
 super(RadiomicsFirstOrder, self).__init__(inputImage, inputMask, **kwargs)
 File "/home/leonardo/anaconda3/lib/python3.6/site-packages/radiomics/base.py", line 88, in __init__
 self._initSegmentBasedCalculation()
 File "/home/leonardo/anaconda3/lib/python3.6/site-packages/radiomics/base.py", line 91, in  
 _initSegmentBasedCalculation
 self.imageArray = sitk.GetArrayFromImage(self.inputImage)
 File "/home/leonardo/anaconda3/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 3412, in 
 GetArrayFromImage
 arrayView = GetArrayViewFromImage(image)
 File "/home/leonardo/anaconda3/lib/python3.6/site-packages/SimpleITK/SimpleITK.py", line 3388, in 
 GetArrayViewFromImage
 pixelID = image.GetPixelIDValue()
AttributeError: 'itkImageSS3' object has no attribute 'GetPixelIDValue'</code></pre>

---

## Post #2 by @lassoan (2018-12-12 20:32 UTC)

<p>If you use Slicer and you end up calling code in  <code>/home/leonardo/anaconda3/lib/python3.6/site-packages/radiomics</code> then it’s an issue. Any idea how that could have happened? Have you installed SlicerRadiomics extension and trying to use that?</p>
<p>If you only use ITK/SimpleITK/pyradiomics in anaconda and not in Slicer then you may get your questions answered in the <a href="http://discourse.itk.org" rel="nofollow noopener">ITK forum</a>.</p>

---

## Post #3 by @fedorov (2018-12-13 15:17 UTC)

<p>If I understood the issue correctly, you are getting this error because the output of itk-python image read and SimpleITK image read is not the same. I thought I saw somewhere a recipe to go between the two outputs, but I can’t find it. I would suggest to ask on ITK forum how to convert output of imread to a SimpleITK image. You could probably do it by copying the buffer and initializing attributes, or using numpy array as an intermediate, but maybe there is already a convenience function that does everything.</p>

---

## Post #4 by @MachadoL (2018-12-13 17:49 UTC)

<p>Thank you Guys…<br>
Yeah… the point is that I am using outside SlicerRadiomics extension… I’m using PyRadiomics directly trhough pythoin script… abd the problem sounds to be that PyRadiomics input images HAVE TO BE SimpleITK::ImageType… and if I use a ITK::ImageType it gets that error…</p>
<p>I’ll try Itk Forum… but that was helpful anyway… thank you!</p>

---
