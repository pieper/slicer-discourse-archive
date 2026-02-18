# DWIToDTIEstimation: Error reading Mask file, wrong coordinate space

**Topic ID**: 3847
**Date**: 2018-08-20
**URL**: https://discourse.slicer.org/t/dwitodtiestimation-error-reading-mask-file-wrong-coordinate-space/3847

---

## Post #1 by @Saba_Shahab (2018-08-20 13:23 UTC)

<p>Operating system:<br>
NAME=“Ubuntu”<br>
VERSION=“16.04.3 LTS (Xenial Xerus)”<br>
ID=ubuntu<br>
ID_LIKE=debian<br>
PRETTY_NAME=“Ubuntu 16.04.3 LTS”<br>
VERSION_ID=“16.04”</p>
<p>Slicer version:<br>
slicer/4.4.0 and slicer/4.8.1 (I got an error using both versions)</p>
<p>Generally, when running the WMA pipeline, I run DTIPrep &gt; DWIToDTIEstimation &gt; DiffusionWeightedVolumeMasking &gt; TractographyLabelMapSeeding. I wanted to create the mask before the tensor estimation step and use the mask to limit the area where the tensor is being calculated. I switched the two steps around and added the mask as an argument in the DWIToDTIEstimation code and got the following error: DWIToDTIEstimation: Error reading Mask file, wrong coordinate space</p>
<p>I looked for a solution online and found this: <a href="http://massmail.spl.harvard.edu/public-archives/slicer-users/2013/006314.html" rel="nofollow noopener">http://massmail.spl.harvard.edu/public-archives/slicer-users/2013/006314.html</a></p>
<p>As suggested in this link, I ran the estimation once without a mask and then used the baseline volume to regenerate the mask and tried re-running DWIToDTIEstimation with this mask but got the same error.</p>
<p>Please let me know if you need any more information to debug this issue.</p>
<p>Best,<br>
Saba Shahab</p>

---

## Post #2 by @lassoan (2018-08-20 14:08 UTC)

<p>Could you please try if latest Slicer nightly version works well?</p>

---

## Post #3 by @Saba_Shahab (2018-08-20 20:01 UTC)

<p>I used the latest Slicer nightly version (updated as of 2018-08-20) and got this error message:</p>
<p>DWIToDTIEstimation: Error reading Mask file, wrong coordinate space<br>
vtkDebugLeaks has found no leaks.</p>
<p>Here is the code I am running: <a href="https://github.com/sabashahab/STOPPD_DTI/blob/master/SlicerTractography_edit.sh" rel="nofollow noopener">https://github.com/sabashahab/STOPPD_DTI/blob/master/SlicerTractography_edit.sh</a></p>

---

## Post #4 by @ihnorton (2018-08-20 21:18 UTC)

<p>I believe the following is happening:</p>
<ul>
<li>
<p>The output DWI from DTIPrep is probably in ITK’s native LPS.</p>
</li>
<li>
<p>Slicer’s NRRD reader (used by DWVolumeMasking) “reorients” the volume while loading, such that the transformation matrix is relative to Slicer’s native RAS. This is technically an identity operation, but when the mask volume is saved, the resulting transform is different than the input DWI.</p>
</li>
<li>
<p>Then DWToDTIEstimation checks that the mask and DWI transforms are equal, but only looks at the transformation matrices, and does not account for the fact that the image is (technically) the same (relative to the embedding NRRD space-directions).</p>
</li>
</ul>
<p>So, in light of that, in the short term I think the quickest solution is to use the <a href="https://www.slicer.org/wiki/Documentation/4.0/Modules/OrientScalarVolume">OrientScalarVolume</a> module to change the mask image back to the same “space directions” as found in the DTIPrep output.</p>
<p>Assuming the DTIPrep output is indeed LPS (check the NRRD header “space directions” field), then you could try adding a step to your script – something like this:</p>
<pre><code class="lang-auto">OrientImage -o LPS  ${outputfolder}/${stem}_MASK.nrrd ${outputfolder}/${stem}_MASK_lps.nrrd
</code></pre>
<p>(and the input mask file for DWIToDTIEstim step would correspondingly change to<br>
<code>$outputfolder/${stem}_MASK_lps.nrrd</code>)</p>

---

## Post #5 by @Saba_Shahab (2018-08-24 13:51 UTC)

<p>Hi Isaiah,</p>
<p>Thanks for your response. I tried OrientScalarVolume (OrientImage didn’t show up as a module) and it didn’t fix the problem.</p>
<p>But the following worked:</p>
<p><code>ResampleScalarVectorDWIVolume -R ${outputfolder}/${stem}_QCed.nrrd ${outputfolder}/${stem}_MASK.nrrd ${outputfolder}/${stem}_MASK_oriented.nrrd</code></p>

---
