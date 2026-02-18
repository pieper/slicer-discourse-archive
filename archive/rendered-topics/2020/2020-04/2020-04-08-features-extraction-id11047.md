# Features extraction

**Topic ID**: 11047
**Date**: 2020-04-08
**URL**: https://discourse.slicer.org/t/features-extraction/11047

---

## Post #1 by @Tonyale1975 (2020-04-08 20:14 UTC)

<p>Good morning Pyradiomics community.<br>
Is it possible to extract characteristics from an image without informing the mask (region of interest)? that is, I want to extract characteristics from the whole image.</p>
<p>Thanks.</p>

---

## Post #2 by @codecrazer (2020-04-08 23:52 UTC)

<p>Try using boxes based method</p>

---

## Post #3 by @JoostJM (2020-04-16 12:48 UTC)

<p>This depends on what you want to acchieve, Currently PyRadiomics requires you to provide a mask, always. However, if you want to extract from the whole image, you can easily generate a ‘full’ mask in python:</p>
<pre><code class="lang-auto">import SimpleITK as sitk
import numpy as np

im = sitk.ReadImage('path/to/image.nrrd')
ma_arr = np.ones(im.GetSize()[::-1])  # reverse the order as image is xyz, array is zyx
ma = sitk.GetImageFromArray(ma_arr)
ma.CopyInformation(im)  # Copy geometric info

from radiomics.featureextractor import RadiomicsFeatureExtractor

extractor = RadiomicsFeatureExtractor('path/to/params.yml')
features = extractor.execute(im, ma)
</code></pre>
<p>Be aware that this gives features about the texture of the entire image! i.e. a single value per image, for the entire image. If you want more local information, try using voxel-based radiomics:</p>
<p><code>extractor.execute(im, ma, voxelBased=True)</code></p>
<p>Be aware that this process will take some time as features are calculated for each voxel!</p>

---

## Post #5 by @zhosseinpour (2020-04-23 20:41 UTC)

<p>Hello every body</p>
<p>I need to provide glcm feature maps in different directions. using the guideline I could provide the maps but it gives me just one map per feature, which I think is the weighted average of different directions.<br>
I would appreciate any help to figure it out.<br>
Thanks</p>

---

## Post #6 by @JoostJM (2020-04-27 15:45 UTC)

<p>Hi Zahra,<br>
what you want is possible, but requires you to deep-dive into the code.<br>
Basically, by default, separate GLCM matrices are calculated for the different directions. You can access them in the numpy array <code>P_glcm</code> in the GLCM feature class. When features are calculated, they are calculated separately on each glcm matrix, and just before returning, a mean is taken over the different directions (last line in the feature functions). You could implent your own version of a GLCM feature class by copying the original one and modifying this last line.</p>

---

## Post #7 by @zhosseinpour (2020-04-27 19:30 UTC)

<p>Thank you very much for your reply. For now I used Scikit-image library, however it does not calculate all the features. So, I did the same thing (access to the matrix to use my calculation) there. But I think pyradiomic is much faster and it is better if can do the same thing using pyradiomic. Thanks again</p>

---

## Post #8 by @Fan_Xu (2022-04-18 12:48 UTC)

<p>Hi, sorry to bother you. But I have tried the ‘full’ mask in PyRadiomics and there exists an error: No labels found in this mask (i.e. nothing is segmented)!.</p>
<p>Then, I check the source code of PyRadiomics and the following codes means that there will be an error when there is only one kind of label in the mask file.</p>
<p>if len(labels) == 1 and labels[0] == 0:<br>
raise ValueError(‘No labels found in this mask (i.e. nothing is segmented)!’)</p>
<p>I wonder how to deal with such problem. Can you give me some idea? Thanks for your kindness!</p>

---

## Post #9 by @pieper (2022-04-18 12:55 UTC)

<p>That check is telling you that there are no non-zero values in your mask and that you need to create a segmentation.</p>

---

## Post #10 by @Marianna_Inglese (2022-09-22 13:42 UTC)

<p>May I ask you if there is a way to keep the dimension of the image also for the feature map?<br>
the size of im (and ma) are 128 x 128 x 35 and I get a feature map (for the entropy, for example) with size  13 x 20 x 17.<br>
Why??<br>
Thank you.<br>
Marianna</p>

---

## Post #11 by @Jesutofunmi (2022-11-02 14:12 UTC)

<p>Hi, I am new to image features extraction and pyradiomics has been the easiest tool for me. I tried the example on voxel radiomics and the result gave a .nnrd simpleITK image for each feature. How do I convert it to float? Thank you</p>
<p><a class="mention" href="/u/joostjm">@JoostJM</a></p>

---
