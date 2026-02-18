# features extract with .png image

**Topic ID**: 23049
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/features-extract-with-png-image/23049

---

## Post #1 by @JY_C (2022-04-20 11:29 UTC)

<p>I want to extract features with HE image, and I save the tiles with .png file. Here is my code:</p>
<p>image = sitk.ReadImage(‘test.png’) # dim=(1024, 1024, 3)</p>
<p>mask_arr = np.ones(image.GetSize()[::-1])<br>
mask = sitk.GetImageFromArray(mask_arr)</p>
<p>firstOrderFeatures = firstorder.RadiomicsFirstOrder(image, mask)</p>
<p>Traceback (most recent call last):<br>
File “/data/chenzhi/.pycharm_helpers/pydev/pydevd.py”, line 1483, in _exec<br>
pydev_imports.execfile(file, globals, locals)  # execute the script<br>
File “/data/chenzhi/.pycharm_helpers/pydev/_pydev_imps/_pydev_execfile.py”, line 18, in execfile<br>
exec(compile(contents+"\n", file, ‘exec’), glob, loc)<br>
File “/data/chenzhi/Chenjy/Pathomics/paper_repetition/features_extract.py”, line 20, in <br>
firstOrderFeatures = firstorder.RadiomicsFirstOrder(image, mask, voxelBased=False)<br>
File “/data/chenzhi/.conda/envs/Chenjy/lib/python3.7/site-packages/radiomics/firstorder.py”, line 37, in <strong>init</strong><br>
self.discretizedImageArray = self._applyBinning(self.imageArray.copy())<br>
File “/data/chenzhi/.conda/envs/Chenjy/lib/python3.7/site-packages/radiomics/base.py”, line 115, in _applyBinning<br>
matrix, _ = imageoperations.binImage(matrix, self.maskArray, **self.settings)<br>
File “/data/chenzhi/.conda/envs/Chenjy/lib/python3.7/site-packages/radiomics/imageoperations.py”, line 155, in binImage<br>
binEdges = getBinEdges(parameterMatrix[parameterMatrixCoordinates], **kwargs)<br>
File “/data/chenzhi/.conda/envs/Chenjy/lib/python3.7/site-packages/radiomics/imageoperations.py”, line 116, in getBinEdges<br>
minimum = min(parameterValues)<br>
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()</p>

---

## Post #2 by @JoostJM (2022-05-03 07:34 UTC)

<p>Hello <a class="mention" href="/u/jy_c">@JY_C</a>,</p>
<p>There are 2 main problems with your code. The first one has to do with your input image. .png yields a color image, meaning it has 3 color channels. PyRadiomics requires grayscale (i.e. 1 value per pixel). There are many other topic reporting this ‘issue’ and how to fix it.</p>
<p>The second ‘problem’ is that you are using the FirstOrder class directly. While this will yield results, nearly all preprocessing is skipped. It is better to use the featureextractor module and enable only ‘firstorder’.</p>

---
