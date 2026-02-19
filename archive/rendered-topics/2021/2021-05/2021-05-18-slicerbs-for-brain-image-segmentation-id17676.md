---
topic_id: 17676
title: "Slicerbs For Brain Image Segmentation"
date: 2021-05-18
url: https://discourse.slicer.org/t/17676
---

# SlicerBS for brain image segmentation

**Topic ID**: 17676
**Date**: 2021-05-18
**URL**: https://discourse.slicer.org/t/slicerbs-for-brain-image-segmentation/17676

---

## Post #1 by @Mehran (2021-05-18 14:03 UTC)

<p>Dear members,<br>
I shared a new brain segmentation module using deep learning to extract brain and Tsallis entropy for segmentation. If you work on brain images, please have a look and let me know any feedback.<br>
You need to download SlicerBS (<a href="https://github.com/Mehrancd/SlicerBS" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Mehrancd/SlicerBS: A Slicer module for brain extraction and segmentation</a>) and add it to Slicer-&gt;Edit-&gt;Application Settings-&gt;Modules, then add the path of the module to “Additional module paths” and restart. The module needs TensorFlow, scikit, etc. which automatically will be installed. If you receive an error, push apply again and probably will solve it. If you need a fast processing, you should increase the voxel size using “resample scaler volume” tool. More detail about algorithm: <a href="https://doi.org/10.1016/j.mri.2019.11.002" rel="noopener nofollow ugc">https://doi.org/10.1016/j.mri.2019.11.002</a>)<br>
and how to use: <a href="https://www.youtube.com/watch?v=gH4dkXm3B2E&amp;t=51s" class="inline-onebox" rel="noopener nofollow ugc">SlicerBS: Extract and segment brain on MRI images into White Matter, Grey Matter and CSF - YouTube</a><br>
Mehran</p>

---

## Post #2 by @pieper (2021-05-18 21:02 UTC)

<p>Cool work, thanks for making it available <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #3 by @lassoan (2021-05-19 04:42 UTC)

<p>Thank you, this is really nice work! It took 36 minutes on my ultrabook (including downloading and installing all dependencies), but it gave meaningful results for the MRHead volume with default options:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dc0e218fc41c4fc8a61c4e7a9e19554f54246a4.jpeg" data-download-href="/uploads/short-url/b5Q0XOGPRftGqR6cVtzMv2xgo0Q.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4dc0e218fc41c4fc8a61c4e7a9e19554f54246a4_2_690x420.jpeg" alt="image" data-base62-sha1="b5Q0XOGPRftGqR6cVtzMv2xgo0Q" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4dc0e218fc41c4fc8a61c4e7a9e19554f54246a4_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4dc0e218fc41c4fc8a61c4e7a9e19554f54246a4_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4dc0e218fc41c4fc8a61c4e7a9e19554f54246a4_2_1380x840.jpeg 2x" data-dominant-color="C8C8C9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1375 541 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>A few suggestions:</p>
<ul>
<li>Save segmentation result into a segmentation node. It takes just a few lines of Python script to convert a labelmap volume node to segmentation node. Set the correct segment names.</li>
<li>Ask the user before starting to download&amp;install enourmous packages, such as tensorflow (right now, the application may remain unresponsive for so long during the installation that, most users would think that the application crashed. See an example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package">script repository</a>.</li>
<li>Instead of lengthy explanation of what the user should do in what order, simplify the user interface. For example, you could create two sections: brain mask extraction and brain segmentation. Remove the “Only extract brain mask” option and instead disable brain segmentation section until a valid brain mask is created or selected. Add a node selector for brain mask (the user may have a brain mask computed already). Disable segmentation section until a valid brain mask is selected. Add more meaningful names for q, alpha, beta, gamma parameters (you can keep the letters in a parentheses in parentheses after the meaningful name, for cross-referencing with the cited paper). Describe meaning of each parameter in tooltips, in a way that is relevant for end uses (description of “Brain extract param” is a good example, it is understandable for the end user).</li>
<li>Fix typos: “param” (use full word - parameter), “higer” in tooltip, tooltip contradicts with help text (higher “brain extract param” will result in larger or smaller volume? larger would be a bit more intuitive).</li>
<li>I would recommend to rename the extension to have a more descriptive name, such as TsallisBrainSegmentation. SlicerBS is not descriptive enough and in North America you don’t want your extension to be associated with <a href="https://www.urbandictionary.com/define.php?term=BS">BS</a>.</li>
<li>Remove <code>__pycache__</code> folders from the repository</li>
<li>Submit this to the extension manager so that users can find it and install it much more easily.</li>
</ul>

---

## Post #4 by @Mehran (2021-05-19 06:39 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the great suggestions which I was waiting for.</p>

---

## Post #5 by @Mehran (2021-05-28 08:33 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> again. I tried to follow the comments and improve the module (except some which I did not know how) with a new name <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> . In addition, I fixed some issues to improve the accuracy. Please have a look and let me know your feedback. You can resample the head image (e.g., 2x2x2) to decrease time consumption considerably.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Mehrancd/TsallisBrainSegmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Mehrancd/TsallisBrainSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/49b3e3c161e0ede9b9d2ab5295208046fba0aff465fc916e80d225917bc11d73/Mehrancd/TsallisBrainSegmentation" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Mehrancd/TsallisBrainSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub - Mehrancd/TsallisBrainSegmentation: A Slicer module for brain...</a></h3>

  <p>A Slicer module for brain extraction and segmentation - GitHub - Mehrancd/TsallisBrainSegmentation: A Slicer module for brain extraction and segmentation</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/772b5eac639e6b4adb19e288410e9e1f6b615579.jpeg" data-download-href="/uploads/short-url/h0dJMmYAlLXZlR1mppynDRSOThf.jpeg?dl=1" title="TBS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772b5eac639e6b4adb19e288410e9e1f6b615579_2_690x439.jpeg" alt="TBS" data-base62-sha1="h0dJMmYAlLXZlR1mppynDRSOThf" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772b5eac639e6b4adb19e288410e9e1f6b615579_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772b5eac639e6b4adb19e288410e9e1f6b615579_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772b5eac639e6b4adb19e288410e9e1f6b615579_2_1380x878.jpeg 2x" data-dominant-color="B1B0B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TBS</span><span class="informations">1564×996 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-05-28 20:48 UTC)

<p>Great, thanks for the update! If you have any specific question (any problems or suggestions that you could not fix) then let us know. If everything is ready then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distributing-an-extension">send a pull request to the ExtensionsIndex</a>.</p>

---

## Post #7 by @slicer365 (2021-05-29 12:39 UTC)

<p>I don’t know why I always fail to install tensorflow.</p>

---

## Post #8 by @lassoan (2021-05-29 13:01 UTC)

<p>The pip install looks good. You have a few harmless warnings:</p>
<ol>
<li>Since you don’t use the command-line from Slicer’s Python environment it is perfectly fine to not adding scripts to the path.</li>
<li>If you want, you can update pip, but it very rarely makes any difference.</li>
</ol>
<p>The error is in your Python code: you call <code>GetDimensions()</code> method for a variable that is set to <code>None</code>. I would recommend to set up a debugger as described <a href="https://github.com/SlicerRt/SlicerDebuggingTools#debuggingtools-extension-for-3d-slicer">here</a>, because then you don’t need to guess what’s happening or add temporary log messages, but you can very easily step through the code and see what goes wrong.</p>

---

## Post #9 by @Mehran (2021-05-29 13:55 UTC)

<p>try the latest version might solve it.</p>

---

## Post #10 by @danielgreenwood (2021-05-31 18:43 UTC)

<p>Great work and very useful to know. Thanks for sharing, I appreciate this work! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #11 by @Mehran (2021-05-31 18:49 UTC)

<p>Thanks <a class="mention" href="/u/danielgreenwood">@danielgreenwood</a></p>

---

## Post #12 by @zhang_han (2023-08-17 03:01 UTC)

<p>Thanks for sharing, I want to save the segmentation result as obj file separately, can this plugin save the segmentation result into the segmentation node separately?</p>

---

## Post #13 by @Mehran (2023-08-17 08:52 UTC)

<p>Hi <a class="mention" href="/u/zhang_han">@zhang_han</a> , if I understand well, you want to save label map as segmentation node. To to this, you only need to right-click on label and convert it to segmentation node in Data module. you also can convert each label (GM, WM, CSF) again to binary label map using right-click in the same module.</p>

---

## Post #14 by @zhang_han (2023-08-18 03:49 UTC)

<p>I’ve successfully exported the file. Thanks for your response!</p>

---
