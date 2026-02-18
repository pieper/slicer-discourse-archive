# Loading nrrd data in python Jupyter notebook script

**Topic ID**: 22637
**Date**: 2022-03-22
**URL**: https://discourse.slicer.org/t/loading-nrrd-data-in-python-jupyter-notebook-script/22637

---

## Post #1 by @Hanne1234 (2022-03-22 14:01 UTC)

<p>Hi,</p>
<p>I am new working with the PyRadiomics package and I have a very basic question. How to load in the data in the Jupyter Notebook script?<br>
I used 3D slicer to perform a segmentation on a PET image and I want to load this in the PyRadiomics package on python. However, I am not sure where to start with loading the nrrd file. I downloaded the pynrrd package (not even sure if this is necessary) but when I perform ‘import pynrrd’ it already gives the error that there is no module named ‘nrrd’.</p>
<p>So therefore, my question is, what is the first step in loading a dataset?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2022-03-22 17:19 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://pypi.org/project/pynrrd/">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="32" height="30">

      <a href="https://pypi.org/project/pynrrd/" target="_blank" rel="noopener">PyPI</a>
  </header>

  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.6fecba6f.jpg" class="thumbnail onebox-avatar" width="300" height="300">

<h3><a href="https://pypi.org/project/pynrrd/" target="_blank" rel="noopener">pynrrd</a></h3>

  <p>Pure python module for reading and writing NRRD files.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You need to install pynrrd and import nrrd.</p>

---

## Post #3 by @lassoan (2022-03-22 17:58 UTC)

<p>If you want to load a nrrd file into a volume node then you can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-volume-from-file">loadVolume function</a>.</p>

---

## Post #4 by @Hanne1234 (2022-03-27 11:32 UTC)

<p>Thank you for your answer! Is it correct that the load volume function is used in 3D slicer? Since I cannot find a Python package what supports this. I am actually searching for a method that can load the nrrd data files in Python so I can perform feature extraction using PyRadiomics.</p>

---

## Post #5 by @lassoan (2022-04-02 02:17 UTC)

<p>You can load nrrd images into numpy array without using Slicer using the <code>pynrrd</code> or similar package. This is used for example in <a href="https://pypi.org/project/slicerio/">slicerio</a> for reading segmentations from nrrd files.</p>

---

## Post #6 by @emma1201 (2022-04-09 17:17 UTC)

<p>Hi Mr Lasso,</p>
<p>Apologies for bringing up an old thread as I am also a Slicer beginner. I am also trying to load an nrrd image into numpy array in Python. However, I am struggling to make sense of the output of the numpy array. What does it mean that I get an array of all 0s and how does one interpret this? I am also not sure what to make of the headers. Do let me know if this is not the appropriate place to post this and if I should try another forum. Thank you! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6770abdba912e3cff6619458de1bbcba65002073.png" data-download-href="/uploads/short-url/eL4zKD9yhy3x8lJiYFTieTITLgL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6770abdba912e3cff6619458de1bbcba65002073.png" alt="image" data-base62-sha1="eL4zKD9yhy3x8lJiYFTieTITLgL" width="549" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">844×768 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2022-04-09 18:18 UTC)

<p>You only see the first and last values in a couple of rows and columns. If the image has a black border it is fine to have all zeros there. You can check the minimum and maximum value in the array to see if indeed all you have is zeros.</p>

---

## Post #8 by @emma1201 (2022-04-12 16:49 UTC)

<p>Thank you so much for the very quick reply!</p>

---
