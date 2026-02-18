# dMRI Scalar Maps & Meausrements

**Topic ID**: 11933
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/dmri-scalar-maps-meausrements/11933

---

## Post #1 by @LearningSlicerYay (2020-06-08 20:27 UTC)

<p>Hi everyone,</p>
<p>I could not find this info when going through the documentation, but I was wondering if there were definitions or more info about how the following are calculated using dMRI:<br>
-Relative Anisotropy<br>
-Determinant</p>
<p>Also, when generating the measurements:</p>
<ol>
<li>How come some are excluded? (Num_Clamp_Excluded)?</li>
<li>What do the ones that have the “NAN” suffix mean?</li>
</ol>
<p>Thank you!</p>

---

## Post #2 by @zhangfanmark (2020-06-09 14:57 UTC)

<p>Hi <a class="mention" href="/u/learningsliceryay">@LearningSlicerYay</a> ,</p>
<p>Relative Anisotropy is defined as the ratio of the anisotropic part of the diffusion tensor to the isotropic part (Basser, 1994). The implementation is here: <a href="https://github.com/zhangfanmark/Slicer/blob/69c4b90c62ab400f9f7862bdbfd96fc02998f45d/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx#L1006" rel="nofollow noopener">https://github.com/zhangfanmark/Slicer/blob/69c4b90c62ab400f9f7862bdbfd96fc02998f45d/Libs/vtkTeem/vtkDiffusionTensorMathematics.cxx#L1006</a> Different to FA, the denominator is trace, instead of norm.</p>
<p>Determinant is just the determinant of the tensor matrix. You can find the math definition here: <a href="https://www.chilimath.com/lessons/advanced-algebra/determinant-3x3-matrix/" rel="nofollow noopener">https://www.chilimath.com/lessons/advanced-algebra/determinant-3x3-matrix/</a></p>
<p>Regarding Num_Clamp_Excluded, there are some computed values out of the expected range for some reason. E.g, FA value may be negative due to noisy signal values. These values are excluded when computing the tract statistics. Num_Clamp_Excluded is used to record the number of such voxels.</p>
<p>Regarding NAN, this means not-a-number, and it should happen when the input tract vtk file is empty, i.e. not fibers.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @LearningSlicerYay (2020-06-09 15:55 UTC)

<p>Hi Fan,</p>
<p>Thanks very much for your reply, that was very helpful.<br>
Some follow-up questions:</p>
<ol>
<li>Are the statistics generated based on “Num_Points” then? Does this represent the number of voxels ?</li>
<li>Regarding the NAN - I am slightly confused - is this also when voxels are excluded for specific analyses? I am not sure how to interpret this in light of Num_Clamp_Excluded. For example, I have a result where:<br>
-Num_Points = 420<br>
-Num_Fibers = 5<br>
-Num_Clamp_Excluded = 37<br>
-Results for FA, RA, MD etc are still generated<br>
-And a variable number in different NAN measurements (i.e., FA.NAN is 14; Max Eigenvalue.NAN is 0; Trace.NAN is 90)</li>
</ol>
<p>In this scenario, how would I interpret what was included to generate the (for example) FA results?</p>
<p>Thanks again</p>

---

## Post #4 by @zhangfanmark (2020-06-09 16:33 UTC)

<p>Hi <a class="mention" href="/u/learningsliceryay">@LearningSlicerYay</a></p>
<p>Yes, the Num_Clamp_Excluded is point-wise. Sorry for the confusion. Regarding the NAN, I thought you meant the NAN values in the computed statistics. In fact, Num_Clamp_Excluded is different from NAN. In the code, we are checking several major diffusion scalars: <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/59297e6212f4cefce9d644164584b5f4df934625/Modules/CLI/FiberTractMeasurements/FiberTractMeasurements.cxx#L898" rel="nofollow noopener">https://github.com/SlicerDMRI/SlicerDMRI/blob/59297e6212f4cefce9d644164584b5f4df934625/Modules/CLI/FiberTractMeasurements/FiberTractMeasurements.cxx#L898</a> So, Num_Clamp_Excluded means the points that have values outside the defined range. The XX.NAN (e.g. FA.NAN) gives the number of points that have nan values in this computed scalar. There should be no direct connection between  Num_Clamp_Excluded and XX.NAN.</p>
<p>For your case, I think it should be interpreted as follows. There are 5 fibers with a total of 420 points. There are 37 points with values outside the defined ranges for the major diffusion scalars. When you are looking specifically at the FA, there are 14 points with nan values, which should have been excluded when computing the mean statistics.</p>
<p>Regards,<br>
Fan</p>

---

## Post #5 by @LearningSlicerYay (2020-06-09 16:53 UTC)

<p>Thanks for your very detailed responses Fan - really appreciate it and now I think understand how to properly interpret it properly <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:">!</p>

---
