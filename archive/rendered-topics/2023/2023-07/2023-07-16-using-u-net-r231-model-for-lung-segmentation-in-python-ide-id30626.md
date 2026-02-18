# Using U-net (R231) model for lung segmentation in Python IDE

**Topic ID**: 30626
**Date**: 2023-07-16
**URL**: https://discourse.slicer.org/t/using-u-net-r231-model-for-lung-segmentation-in-python-ide/30626

---

## Post #1 by @Nima_Yousefi (2023-07-16 05:23 UTC)

<p>Hi,</p>
<p>I want to use U-net model for lung segmentation and create it’s mask, I read the descriptive text on “<a href="https://github.com/JoHof/lungmask" class="inline-onebox" rel="noopener nofollow ugc">GitHub - JoHof/lungmask: Automated lung segmentation in CT</a>” but unfortunately it didn’t help me enough.<br>
Is there any source code about it?</p>
<p>Thanks.</p>

---

## Post #2 by @rbumm (2023-07-16 10:23 UTC)

<p>In which Python IDE do you want to use lungmask AI?</p>
<p>You should be able to run lungmask <a href="https://github.com/JoHof/lungmask#as-a-python-module">as descibed on their GitHub website</a> like</p>
<pre><code class="lang-auto">from lungmask import LMInferer
import SimpleITK as sitk

inferer = LMInferer()

input_image = sitk.ReadImage(INPUT)
segmentation = inferer.apply(input_image)  # default model is U-net(R231)
</code></pre>

---

## Post #3 by @Nima_Yousefi (2023-07-16 16:53 UTC)

<p>Thank you for your reply Dr bumm.</p>
<p>I want to use it in Spyder.<br>
Yes as I mentioned, it didn’t help me for some part of my work.<br>
For example how can i use it with Pyradiomics package for feature extraction?</p>

---

## Post #4 by @curtislisle (2023-07-16 17:16 UTC)

<p>The code provided by Dr.Bumm should work in Spyder. Just be sure to install the lungmask and simpleitk packages first using any package manager, such as pip and be sure Spyder is using the right Python interpreter.</p>
<p>Pyradiomics is a package separate from lungmask. For pyradiomics, you can call it from Python also. The examples included with the PyRadiomics repository were helpful to me, hopefully it will work for you if you follow the included examples.</p>

---
