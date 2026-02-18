# Tractography seeding with endpoints

**Topic ID**: 11857
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/tractography-seeding-with-endpoints/11857

---

## Post #1 by @fpsiddiqui91 (2020-06-04 08:22 UTC)

<p>Hello developers,</p>
<p>I was wondering if it is possible to perform seeding tractography with seed and endpoint. I am quite aware that streamline tractography needs only the seeding region. However, in my case, I want to add some endpoints as well to explore the tracts starting from one region and end at the specific region. I do have the seeding label and end label.</p>
<p>I am just not sure how to perform region-based stratigraphy. Is ROI selection in the diffusion module helpful? Can you guide me on how to perform this tractography?</p>
<p>I am importing my seeding and end regions as individual label maps (nii, file). However, I can run ROI tractography with this, but somehow, I don’t know how to use ROI selection to remove certain fibers?<br>
Please note, I have two individual label maps.</p>
<p><a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/lassoan">@lassoan</a>, if anyone of you can help?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2020-06-05 02:25 UTC)

<p>I’m not familiar with details of tractography, but maybe you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/UKFTractography">input brain mask</a>.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> do you have any suggestion?</p>

---

## Post #3 by @pieper (2020-06-05 12:25 UTC)

<p><a class="mention" href="/u/fpsiddiqui91">@fpsiddiqui91</a> probably the methods described in this tutorials will be your best approach.  I.e. do a dense whole-brain tractography and then select the tracts that go through your regions of interest.</p>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://dmri.slicer.org/tutorials/Slicer-4.8/FiberBundleSelectionAndScalarMeasurement.pdf" target="_blank">dmri.slicer.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://dmri.slicer.org/tutorials/Slicer-4.8/FiberBundleSelectionAndScalarMeasurement.pdf" target="_blank"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://dmri.slicer.org/tutorials/Slicer-4.8/FiberBundleSelectionAndScalarMeasurement.pdf" target="_blank">FiberBundleSelectionAndScalarMeasurement.pdf</a></h3>

<p class="filesize">16.39 MB</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @fpsiddiqui91 (2020-06-05 15:31 UTC)

<p>Thank you for your answers <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>I went through this tutorial. I have had some minor problems in selecting labels. I am importing the individual  label maps from .nii file (starting and end region). Since I am importing them, I cannot assign a number/ index to label. (as discussed in page 12 of the tutorial). Can you please let me know ho I can assign the label number to each map so that I can use ROI selection?</p>
<p>Thank you for your answer.</p>

---

## Post #5 by @pieper (2020-06-05 15:57 UTC)

<p>You don’t need to use the same label numbers.  When you get further through the tutorial you’ll see that you enter the label numbers of interest.  The the slides starting around 23 about “Single Label Selection”.</p>

---

## Post #6 by @fpsiddiqui91 (2020-06-05 18:00 UTC)

<p>Thank you for your response, I understand your point. The problem is I want to use two labels (start and end region). I have imported these labels as .nii file.  While using ROI, I have to select labels for inclusion, However, if I use 1,2 with AND logic, I don’t get any tracts.</p>
<p>The reason for that is the command does not know the label with number “2”. My question is how can I assign these labels to my imported label masks.</p>
<p>I hope I am clear.</p>
<p>thank you.</p>

---

## Post #7 by @pieper (2020-06-05 18:25 UTC)

<p>Is the issue that you aren’t sure what numbers correspond to your ROI?  For that you can scoll to the slice and look at the Data Probe in the lower left of the interface to see the label numbers as you mouse over them.</p>

---

## Post #8 by @fpsiddiqui91 (2020-06-06 14:15 UTC)

<p>Thank you for your response <a class="mention" href="/u/pieper">@pieper</a>. Yes, I have already tried this.</p>
<p>The problem is both my label have been assigned the same number, i-e 1, since I have imported .nii  file. Is it possible to merge the labels into one label map and assign different numbers to each label?</p>
<p>I hope I am clear.</p>
<p>Thank you</p>

---

## Post #9 by @pieper (2020-06-06 14:44 UTC)

<p>Hi <a class="mention" href="/u/fpsiddiqui91">@fpsiddiqui91</a>, I’m still not quite getting the issue.  You have an nii file that has labels for two different regions of interest, but you say they both have the number 1?  Maybe you can share some files so that we can have a look.</p>

---

## Post #10 by @lassoan (2020-06-06 15:03 UTC)

<p>Segmentation import form Nifti has been greatly improved in recent Slicer-4.11 versions. If you use this version and in “Add data” window “Description” column you choose “Segmentation” then all the original label values will be preserved. If the original volume had multiple disconnected regions all labeled with the same value then you can use Islands effect in Segment editor module to assign different labels to them.</p>
<p>I’m not sure if tractography module can use segmentation node as input directly, so when you are done with the segmentation you may need to convert it to a labelmap volume node (by right-clicking on it in Data module and selecting “Export visible segments to binary labelmap”).</p>

---

## Post #11 by @fpsiddiqui91 (2020-06-06 15:06 UTC)

<p>Thank you for your response, I actually have too individual .nii file,  each has one label for ROI.  That’s why I think I am getting number 1. If there is a way to merge the labels into one file and assign the number to each ROI, it would solve my problem I guess. Thank you.</p>

---

## Post #12 by @fpsiddiqui91 (2020-06-06 15:08 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>. I have not tried segmentation module yet. I am gonna try it and see if it works or not.</p>
<p>Yes, you can import segmentation node directly as input in tractogaphy module I think. Otherwise I will just convert it onto label map. Thank you so much for your suggestions.</p>

---

## Post #13 by @pieper (2020-06-06 22:03 UTC)

<p>Ah, thanks for the clarification.  In that case probably the easiest is to do it in the python console like:</p>
<pre><code class="lang-auto">a = array("labelmap-node-name")
a *= 2
</code></pre>

---

## Post #14 by @fpsiddiqui91 (2020-06-07 10:47 UTC)

<p>Thanks for the suggestion, I am gonna try this</p>

---
