---
topic_id: 24103
title: "Importing H5 Model Using Keras Load Model"
date: 2022-06-29
url: https://discourse.slicer.org/t/24103
---

# Importing .h5 model using keras load_model

**Topic ID**: 24103
**Date**: 2022-06-29
**URL**: https://discourse.slicer.org/t/importing-h5-model-using-keras-load-model/24103

---

## Post #1 by @Zhenchen (2022-06-29 12:53 UTC)

<p>Hello everyone,</p>
<p>I am currently building a module for image segmentation using a Unet model that has already been trained. When I test the module, the execution blocks when calling the function <strong>tensorflow.keras.load_model()</strong> and Slicer does not respond. Unfortunately, there is no error message.</p>
<p>When I try to load the model using the same function in pyCharm with the Python Interpreter being that of Slicer, everything goes well. I also checked the environment variables, it turns out that PYTHONHOME and PYTHONPATH are both the same when running the code inside or outside Slicer.</p>
<p>Has someone had the same problem?  How can I solve it?</p>
<p>Thanks a lot<br>
Zhenchen</p>

---

## Post #2 by @pieper (2022-06-29 13:27 UTC)

<p>Hard to say exactly, but if you’ve done anything that changes the environment variables or paths or tries to mix-and-match different python libs from different distributions that could cause this kind of behavior.</p>
<p>Tensorflow has always worked for me, including loading models, by using <code>pip_install("tensorflow")</code> in Slicer’s python.  Probably start fresh with a new slicer install report what you did step-by-step.</p>

---

## Post #3 by @Zhenchen (2022-06-30 21:24 UTC)

<p>Thank you very much for your response Steve.</p>
<p>In fact, I have tried what you suggested. Firstly, I deleted slicer and installed a new one. After that, I pasted my code about loading of the model into the script of a new Slicer module. Then, I installed all the necessary packages (tensorflow, cv2, tqdm, skimage, etc.) using the command  <code> pip_install("...")</code> in Slicer’s python interactor. Finally, I tested the new module but the problem still exists. The execution blocked at the step of loading of the model by calling the function  <code> tensorflow.keras.models.load_model()</code>.</p>
<p>Besides, I tried to debug with Slicer’s plug-in Debugging tools and PyCharm.  In fact, the information “no frame is available” was shown when I tried to step into <code>model_config = f.attrs.get('model_config')</code> in the file <em>hdf5_format.py</em>. I hope this information could help you…and thanks again for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bebc05b6298300cfd7f8ff0b2f4b728d4acbf51.jpeg" data-download-href="/uploads/short-url/3YZZb0D0hbbPeJBwrV5WPI36Wlj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bebc05b6298300cfd7f8ff0b2f4b728d4acbf51_2_455x375.jpeg" alt="image" data-base62-sha1="3YZZb0D0hbbPeJBwrV5WPI36Wlj" width="455" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bebc05b6298300cfd7f8ff0b2f4b728d4acbf51_2_455x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bebc05b6298300cfd7f8ff0b2f4b728d4acbf51_2_682x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bebc05b6298300cfd7f8ff0b2f4b728d4acbf51_2_910x750.jpeg 2x" data-dominant-color="323334"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1486×1224 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2022-06-30 22:36 UTC)

<p>My guess would be an incompatible hdf5 library being pulled in by one of the pip packages. You wouldn’t be able to debug that with pycharm but there are system tools (<a href="https://docs.microsoft.com/en-us/sysinternals/">such as sysinternals</a> that can help you debug.  If nothing works maybe you could share a reproducible example, e.g. a model file and the script the script that does the install and load that hangs, then maybe someone can trace what’s happening.</p>

---

## Post #5 by @Zhenchen (2022-07-04 11:09 UTC)

<p>Here is the link to my model and the script to load it. Hope someone could help.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1StkldO35vvPAq7JrsLKlzoulFepznkbO/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1StkldO35vvPAq7JrsLKlzoulFepznkbO/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1StkldO35vvPAq7JrsLKlzoulFepznkbO/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1StkldO35vvPAq7JrsLKlzoulFepznkbO/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">load_model.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2022-07-04 12:14 UTC)

<p>HDF5 is a very troublesome library, there are problems with it all the time due to binary incompatibity issues. One solution is to <a href="https://www.tensorflow.org/guide/keras/save_and_serialize">save your model number in the recommended SavedModel file saving format</a> instead of the problematic legacy HDF5 format (referred to as H5 in Keras documentation).</p>

---

## Post #7 by @Zhenchen (2022-07-05 08:58 UTC)

<p>Thank you very much, it works now.</p>

---
