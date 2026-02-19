---
topic_id: 411
title: "Prepare Labelmap For Parenchyma Analysis"
date: 2017-06-01
url: https://discourse.slicer.org/t/411
---

# Prepare labelmap for parenchyma analysis

**Topic ID**: 411
**Date**: 2017-06-01
**URL**: https://discourse.slicer.org/t/prepare-labelmap-for-parenchyma-analysis/411

---

## Post #1 by @broccoli (2017-06-01 13:59 UTC)

<p>I want to use the Parenchyma Analysis module, but want to use a segmentation that was done by different software.</p>
<p>What I tried:</p>
<ul>
<li>Convert the surface mesh to a label map using the Model to Label Map module.</li>
<li>Use this label map as Label Map Volume in Parenchyma Analysis.</li>
</ul>
<p>This did not work, my next idea was to try and devide the lung mesh into upper, middle and lower parts for the left and right lungs by:</p>
<ol>
<li>Let the Parenchyma Analysis module generate a partial lung label map.</li>
<li>Convert the partial lung label map to a model with the Model Maker module.</li>
<li>Importing the surface mesh as a model in the Segmentations module, as well as the model created in step 2.</li>
<li>My idea was to cut the model from the surface mesh, to devide it into the upper, middle and lower parts as the model created in step 2 has. However, when trying to use any of the Effects in the Segmentation module, a window opens and asks to change the master representation from closed surface to binary labelmap. After clicking on Yes, 3D Slicer does not respond and I need to restart the software.</li>
</ol>
<p>What would be a solution to be able to use my surface mesh?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2017-06-02 03:17 UTC)

<p>Use the latest nightly version of Slicer, it has lots of improvements and fixes.</p>
<aside class="quote no-group" data-username="broccoli" data-post="1" data-topic="411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a183cd/48.png" class="avatar"> broccoli:</div>
<blockquote>
<p>Convert the partial lung label map to a model with the Model Maker module.</p>
</blockquote>
</aside>
<p>No need. Import it directly into the Segmentation node (in Segmentations module, Import/export … section).</p>
<aside class="quote no-group" data-username="broccoli" data-post="1" data-topic="411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a183cd/48.png" class="avatar"> broccoli:</div>
<blockquote>
<p>when trying to use any of the Effects in the Segmentation module, a window opens and asks to change the master representation from closed surface to binary labelmap. After clicking on Yes, 3D Slicer does not respond and I need to restart the software.</p>
</blockquote>
</aside>
<p>This should work correctly with the latest nightly version, but if not then let us know.</p>

---

## Post #3 by @broccoli (2017-06-15 12:16 UTC)

<p>Thanks for the tip to import the labelmap directly, I had overlooked this option.<br>
After reducing the size of the imported mesh it worked, although converting to binary labelmap still took some time (about an hour). I think it was a memory problem.</p>

---

## Post #4 by @lassoan (2017-06-15 12:37 UTC)

<p>Thanks for the update, I’m glad that it worked.</p>
<p>You can usually reduce size of high-resolution meshes by 80-95% without any visible difference by using Surface toolbox module decimate function with a factor of 0.8 to 0.95.</p>

---

## Post #5 by @Molly (2019-08-16 15:51 UTC)

<p>Hi, did you finally geti it? I’m trying to do the same - use the parenchyma analysis with a segmentation made by another software, but I can’t even start. In what format has the segmentation to be saved for a correct import in 3d slicer?<br>
Thanks</p>

---

## Post #6 by @lassoan (2019-08-17 19:29 UTC)

<p>What software did you use to create the initial segmentation? What file formats it can save into?</p>

---

## Post #7 by @Molly (2020-04-15 09:39 UTC)

<p>Hello, sorry for this late answer, I had to drop my project but now I have some time to spend on it!I hope to find you well.<br>
I use pulmonary toolkit to create the initial segmentation, a plugin on Mat-Lab. It can save the segmentaion in: dicom (.dcm), Matlab matrix (.mat), nifti (.nii) and metaheader and raw data (mhd).</p>

---

## Post #8 by @Molly (2020-04-15 10:46 UTC)

<p>Pulmonary toolkit can also generate “lobe mesh”, but when I import it, the position is incorrect (coordinates are different between ct-scan and imported mesh).</p>

---

## Post #9 by @lassoan (2020-05-20 00:07 UTC)

<p>Most likely it is a RAS/LPS coordinate system mismatch. In recent Slicer Preview Releases, you can choose preferred coordinate system when opening a model in Add data dialog.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5baca478bb4b767fdc11cbfeb2c0a436de0fca0d.png" data-download-href="/uploads/short-url/d4ZkKaoS6ILUUEYpgdqAf6OT8Hr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5baca478bb4b767fdc11cbfeb2c0a436de0fca0d_2_690x266.png" alt="image" data-base62-sha1="d4ZkKaoS6ILUUEYpgdqAf6OT8Hr" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5baca478bb4b767fdc11cbfeb2c0a436de0fca0d_2_690x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5baca478bb4b767fdc11cbfeb2c0a436de0fca0d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5baca478bb4b767fdc11cbfeb2c0a436de0fca0d.png 2x" data-dominant-color="F5F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">909×351 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
