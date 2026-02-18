# Segmentation of 4D sequence volumes using Sequence Registration

**Topic ID**: 20567
**Date**: 2021-11-10
**URL**: https://discourse.slicer.org/t/segmentation-of-4d-sequence-volumes-using-sequence-registration/20567

---

## Post #1 by @Shambhavi_Malik (2021-11-10 15:08 UTC)

<p>I am trying to segment the CT Cardio Volume Sequence (from the Slicer sample data). I have followed all the steps as mentioned in <a href="https://discourse.slicer.org/t/load-multiple-cardiac-phases-for-segmentation-virtual-reality/5214">Load multiple cardiac phases for segmentation/virtual reality</a> question that was posted earlier on the forum, but I can’t get the required results.</p>
<ul>
<li>
<p>My input volume sequence is the CTCardioSeq</p>
</li>
<li>
<p>I have created a new output volume sequence (OutputVolumes)</p>
</li>
<li>
<p>For output transform sequence I have chosen the Segmentation.</p>
</li>
</ul>
<p>I had segmented frame 4 of the volume sequence and wanted to modify that segmentation to fit all other frames. Instead of modifying the segmentation to fit all the frames, Slicer is modifying the rest of the frames to fit the segmentation. I am not able to figure out where I am going wrong and how should I go about this issue. I am using Slicer 4.11.20210226.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2022-03-12 04:09 UTC)

<p>For output transform sequence you need to choose a transform sequence (not segmentation).<br>
Transform direction should be “fixed frame to moving frames”.</p>
<p>If you segment the fixed frame and then apply the transform sequence’s proxy node (the transform that is changing in time as you replay the sequence) then you’ll see the segmentation is warped to each image frame.</p>
<p>If you want to edit the automatically warped transform then you need to create a segmentation sequence, enable “Save changes” for the segmentation sequence in “Synchronized nodes” section in Sequences module, and replay it once so that the segmentation is saved for each time point. You can then apply the warping transform manually for each time point and fix up the segmentation if you have found inaccuracies in the automatic warping.</p>

---

## Post #3 by @Yiling_Fan (2022-06-07 15:17 UTC)

<p>Hi Lasso,<br>
I tried to use this method on a (2D+time) dataset and it through me an error:<br>
“Error: Command ‘elastix’ returned non-zero exit status 1.”</p>
<p>Could this function work with 2D cine data?</p>
<p>Thanks for the help!</p>

---

## Post #4 by @lassoan (2022-06-19 03:05 UTC)

<p>Probably you need to adjust the settings to register 2D+t data. You can ask help from the <a href="https://groups.google.com/g/elastix-imageregistration">Elastix forum</a>.</p>

---

## Post #5 by @SassanHashemi (2025-11-10 03:12 UTC)

<p>Hi Andras,</p>
<p>Is there a way to segment the anatomy of interest in each time frame and extract a transform sequence based off that?</p>
<p>I need an accurate transform sequence of the airway in a multiphase CT that I have. But the transform sequence that “sequence registration” module creates is not very accurate, So I was curious to know if I can work backwards and go from a series of segmentation to an accurate transform sequence.</p>
<p>Thank you,</p>
<p>Sassan</p>

---

## Post #6 by @lassoan (2025-11-10 15:35 UTC)

<p>You can make registration more accurate by cropping the images to the region of interest, using Crop volume sequence module. You can also tune the registration parameters to make the registration more accurate.</p>
<p>But if you still want to register based on segmentation, you can do that, too. You’ll need to manually (or from Python script) compute a distance map from one or few structures and then use sequence registration on these distance maps. The resulting transform sequence can be then applied to the image sequence.</p>

---
