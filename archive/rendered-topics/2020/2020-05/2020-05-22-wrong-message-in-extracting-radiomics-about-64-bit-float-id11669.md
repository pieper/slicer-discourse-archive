# Wrong message in extracting radiomics about 64-bit float

**Topic ID**: 11669
**Date**: 2020-05-22
**URL**: https://discourse.slicer.org/t/wrong-message-in-extracting-radiomics-about-64-bit-float/11669

---

## Post #1 by @zhangqw (2020-05-22 14:06 UTC)

<p>When I extracted from 3D segment, some could be extracted but some failed, the wrong messgae is as follows:</p>
<pre><code class="lang-auto">[2020-05-22 21:40:45] E: radiomics.script: Feature extraction failed!
Traceback (most recent call last):
  File "D:\python37\lib\site-packages\pyradiomics-2.2.0.post7+gac7458e-py3.7-win-amd64.egg\radiomics\scripts\segment.py", line 70, in _extractFeatures
    feature_vector.update(extractor.execute(imageFilepath, maskFilepath, label, label_channel))
  File "D:\python37\lib\site-packages\pyradiomics-2.2.0.post7+gac7458e-py3.7-win-amd64.egg\radiomics\featureextractor.py", line 267, in execute
    image, mask = self.loadImage(imageFilepath, maskFilepath, generalInfo)
  File "D:\python37\lib\site-packages\pyradiomics-2.2.0.post7+gac7458e-py3.7-win-amd64.egg\radiomics\featureextractor.py", line 380, in loadImage
    image = imageoperations.normalizeImage(image, **self.settings)
  File "D:\python37\lib\site-packages\pyradiomics-2.2.0.post7+gac7458e-py3.7-win-amd64.egg\radiomics\imageoperations.py", line 595, in normalizeImage
    image *= scale
  File "D:\python37\lib\site-packages\SimpleITK\SimpleITK.py", line 4277, in __mul__
    return Multiply( self, float(other) )
  File "D:\python37\lib\site-packages\SimpleITK\SimpleITK.py", line 50876, in Multiply
    return _SimpleITK.Multiply(*args)
RuntimeError: Exception thrown in SimpleITK Multiply: c:\d\vs14-win64-pkg\simpleitk\code\common\include\sitkMemberFunctionFactory.hxx:196:
sitk::ERROR: Pixel type: vector of 64-bit float is not supported in 3D byclass itk::simple::MultiplyImageFilter
</code></pre>

---

## Post #2 by @JoostJM (2020-05-23 14:01 UTC)

<p>Your pixeltype is a vector of 64-bit float, i.e. a color image. PyRadiomics is designed to extract from gray-scale images. What is the input data you are using? You could consider extracting a single color channel, or taking the mean across color channels.</p>

---

## Post #3 by @zhangqw (2020-05-24 14:05 UTC)

<p>I used MRI image. It was a gray-scale image.</p>

---

## Post #4 by @JoostJM (2020-06-07 09:13 UTC)

<p>What file type did you use? If it is something like .png or .jpg, your image may indeed be grayscale and look like that, but because the underlying format is a color format, it is still stored as a color image and therefore not accepted by PyRadiomics.<br>
Moreover, formats like .png and .jpg do not contain the geometric space information (i.e. how the image data array translates to a real-world volume). This is especially important when calculating shape features, but also if you want to resample to different spacing or use distance weighting in GLRLM and/or GLCM.</p>
<p>When possible, I usually advise to use NRRD or NIFTII format, which can store grayscale as truly grayscale, and contains the geometry information. There are several tools available to convert DICOMs into this format.</p>

---

## Post #5 by @wangzhuo (2022-03-06 08:16 UTC)

<p>您好，我出现了和您相同的问题（sitk::ERROR: Pixel type: vector of 64-bit float is not supported in 3D byclass itk::simple::MultiplyImageFilter），请问您最后是怎么解决的呢？万分感谢</p>

---

## Post #6 by @wangzhuo (2022-03-06 20:30 UTC)

<p>When I extracted from 3D segment, some could be extracted but some failed, the wrong message is as follows:</p>
<pre><code class="lang-auto">C:\Users\admin\AppData\Local\JetBrains\PyCharmCE2021.2\demo\PyCharmLearningProject\venv\lib\site-packages\radiomics\generalinfo.py:72: ComplexWarning: Casting complex values to real discards the imaginary part
  im_arr = sitk.GetArrayFromImage(image).astype('float')
Traceback (most recent call last):
  File "D:/pythonProject/特征提取修改后均为nrrd格式.py", line 78, in &lt;module&gt;
    featureVector = extractor.execute(imageName, maskName)
  File "C:\Users\admin\AppData\Local\JetBrains\PyCharmCE2021.2\demo\PyCharmLearningProject\venv\lib\site-packages\radiomics\featureextractor.py", line 272, in execute
    image, mask = self.loadImage(imageFilepath, maskFilepath, generalInfo, **_settings)
  File "C:\Users\admin\AppData\Local\JetBrains\PyCharmCE2021.2\demo\PyCharmLearningProject\venv\lib\site-packages\radiomics\featureextractor.py", line 395, in loadImage
    image = imageoperations.normalizeImage(image, **kwargs)
  File "C:\Users\admin\AppData\Local\JetBrains\PyCharmCE2021.2\demo\PyCharmLearningProject\venv\lib\site-packages\radiomics\imageoperations.py", line 583, in normalizeImage
    image = sitk.Normalize(image)
  File "C:\Users\admin\AppData\Local\JetBrains\PyCharmCE2021.2\demo\PyCharmLearningProject\venv\lib\site-packages\SimpleITK\SimpleITK.py", line 43696, in Normalize
    return _SimpleITK.Normalize(image1)
RuntimeError: Exception thrown in SimpleITK Normalize: d:\a\1\sitk\code\common\include\sitkMemberFunctionFactory.hxx:158:
sitk::ERROR: Pixel type: complex of 64-bit float is not supported in 3D by class itk::simple::NormalizeImageFilter.
</code></pre>

---

## Post #7 by @JoostJM (2022-03-11 08:53 UTC)

<p>The image you are using contains a complex pixel type, this is not supported by PyRadiomics. Best solution would be to extract either the real or imaginary component and run pyradiomics on that image.</p>

---
