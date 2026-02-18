# Input mask for .jpg files

**Topic ID**: 11984
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/input-mask-for-jpg-files/11984

---

## Post #1 by @Khalifa1997 (2020-06-10 18:46 UTC)

<p>Hey there,<br>
I hope you guys are good, currently I am working on .jpg images, however I’d like to use <code>radiomics.featureextractor.RadiomicsFeatureExtractor()</code> the problem I am having however, is with the <code>.execute</code> is that while I do have the image file path, I don’t have the input mask file, I checked out the jupyter notebooks on github and it seems you only use the <code>.getTestCase</code> method to get both the path and the mask file, so if anyone could help me with that I would be very much grateful <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @JoostJM (2020-06-23 09:57 UTC)

<p>The <code>getTestCase</code> function only obtains the example cases included in the PyRadiomics repository (downloading them if necessary).</p>
<p>As to your problem, where do you have your mask if you don’t have a filepath? Is it loaded in Slicer? Or do you create the mask dynamically in a Python script? PyRadiomics also supports you to pass the mask a loaded SimpleITK.Image object instead of a file descriptor pointing to the file that can be loaded a SimpleITK.Image object.</p>
<p>Finally, you mention that you work with .jpg input, this is often a color image (i.e. a vector image with 3 values per pixel). PyRadiomics does not support this, input image is required to be grayscale (scalar pixel datatype). The mask is allowed to be a vector image, where you need to select the index to use for your mask.</p>
<p>HTH,</p>
<p>Joost</p>

---
