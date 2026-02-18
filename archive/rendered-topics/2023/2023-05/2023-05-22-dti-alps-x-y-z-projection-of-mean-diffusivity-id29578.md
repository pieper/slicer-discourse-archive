# DTI_ALPS x,y,z-projection of mean diffusivity

**Topic ID**: 29578
**Date**: 2023-05-22
**URL**: https://discourse.slicer.org/t/dti-alps-x-y-z-projection-of-mean-diffusivity/29578

---

## Post #1 by @JSteinJ (2023-05-22 13:36 UTC)

<p>terribly sorry me again,<br>
I forgot that I need x,y,z projections of MeanDiffusivity to.<br>
How can I calculate it from the maps in DiffusionTensorScalarMeasurement provided…?<br>
thank you,<br>
jürgen</p>

---

## Post #2 by @pieper (2023-05-22 14:43 UTC)

<p>You’ll need to figure out the details of the calculations yourself, but you can get the individual tensors in python: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-values-in-a-dti-tensor-volume" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #3 by @JSteinJ (2023-05-25 05:07 UTC)

<p>thank you for your help…<br>
is that ok that the script works more than 47h now??<br>
its a 2040 pics dti on a Intel® Core™ i7-4790 CPU @ 3.60GHz × 8 machine…<br>
ok I know Slicer uses just 1 core…</p>

---

## Post #4 by @pieper (2023-05-25 13:35 UTC)

<p>Processing tensor volumes voxel by voxel in python is likely to be slow, but that does seem like a long time.  Usually it’s good to try small experiments to confirm that you are getting the results you expect and then you can use the timing of small examples to estimate how long it should take to process a full volume.  It depends on your priorities but writing in C++ is an option to speed things up.</p>

---

## Post #5 by @JSteinJ (2023-05-31 10:21 UTC)

<p>Seems to be a never ending story… ;((<br>
I mean now I got a result but I can´t evalue it.</p>
<p>I have the tensor in a 4D “.nii.gz” file. in the order of Dxx, Dxy, Dxz, Dyy, Dyz &amp; Dzz<br>
I can load it into 3D Slicer using the MultiVolumeImporter.<br>
I would like to place some ROIs and measure the values for Dxx Dyy and Dzz<br>
How is that possible?</p>
<p>Moving the mouse over the frame in the MultiVolumeExplorer gives koordinates but no values?<br>
So does Segmentation &amp; Segment Statistics…</p>
<p>Is there a possibility to export the multiframe in single frames?</p>
<p>thanks jürgen</p>

---

## Post #6 by @pieper (2023-05-31 14:00 UTC)

<p>See the MultiVolumeExplorer to extract individual scalar volumes that are compatible with the DataProbe and SegmentStatistics.</p>

---

## Post #7 by @JSteinJ (2023-06-20 09:55 UTC)

<p>Me again…<br>
sorry your tip with the script repository doesn’t work…<br>
tried on different Slicer versions, and on different data… (just to let you know…)</p>
<p>in older slicer versions (4.0…) there are different kind of maps (Diffusion Tensor Scalar Measurement) available. Is there a way to calculate this maps also in the recent versions (5…)?</p>
<p>And can you tell me whats RAIMaxEigenvecX,Y,Z??? the links to the documentation are no longer up to date, can’t find any explanation…</p>

---

## Post #8 by @pieper (2023-06-20 13:00 UTC)

<p>Be sure to read the documentation and study the code: <a href="http://dmri.slicer.org/">http://dmri.slicer.org/</a></p>
<p>If you see broken links please report specifically so they can be fixed.  If there are scripts that don’t work for you please report the steps you took and what didn’t work.</p>

---

## Post #9 by @zhangfanmark (2023-07-06 05:43 UTC)

<p>Hi!</p>
<p>“RAIMaxEigenvecX,Y,Z” are likely the eigenvectors computed the diffusion tensors. I don’t think these are provided even in older Slicer versions. Perhaps in the code used as intermediate functions.</p>
<p>Yes, in the new release of Slicer, Diffusion Tensor Scalar Measurement module is available. You would need to install SlicerDMRI to use this module: <a href="http://dmri.slicer.org/download/" class="inline-onebox" rel="noopener nofollow ugc">Download</a></p>
<p>Btw, above you mentioned “x,y,z projections” are needed. I am not sure if you meant to analyze the Dxx, Dyy, Dzz from the diffusion tenor, or lamda 1, 2, 3 corresponding to the eigenvalues. If the later, you can directly obtain them in the Diffusion Tensor Scalar Measurement module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5abe47d807433a15cc9029e0a12463178582a3d7.png" alt="image" data-base62-sha1="cWKE62fDSAERLgAMS1MpQU4aZa7" width="566" height="324"></p>
<p>Regards,<br>
Fan</p>

---

## Post #10 by @JSteinJ (2023-07-07 06:43 UTC)

<p>HI Fan,</p>
<p>thank you for this useful message:<br>
“RAIMaxEigenvecX,Y,Z”  whatever it is, is provided in Slicer versions around 4.0 - 4.4… +/-… in “Diffusion Tensor Scalar Measurement module”<br>
In this versions you also get the x,y,z projection of MaxEigenValue… This feature is useful<br>
for the ALPS index… but no longer provided in the new versions. In the meantime I have solved my problems, and I am able to calculate DTI -ALPS index using 3D Slicer and some other software…<br>
I wonder that the “Diffusion Tensor Scalar Measurement module” does not provide calculation of ADC maps from DTI scans… as this is a very basic often used information. but ok…<br>
So thank you for your help, I have found a solution.</p>

---

## Post #11 by @djl (2024-03-04 15:02 UTC)

<p>Hi！<br>
Can you tell me how you solved your problem please. can I calculate ALPS just by 3d slicer.Does “Max Eight Value” in diffusion tensor scalar maps mean Dxx?<br>
thank you</p>

---
