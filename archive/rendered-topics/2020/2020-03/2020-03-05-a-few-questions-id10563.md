# A few questions

**Topic ID**: 10563
**Date**: 2020-03-05
**URL**: https://discourse.slicer.org/t/a-few-questions/10563

---

## Post #1 by @LearningSlicerYay (2020-03-05 18:49 UTC)

<p>Hi all,</p>
<p>Working with Slicer 4.10.1 and have a few questions:</p>
<ol>
<li>
<p>Is there a way to adjust for eddy current in this (or 4.10.2) version? I have read <a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ#Is_there_a_way_to_perform_an_Eddy_current_correction_on_DWI_in_Slicer" rel="noopener nofollow ugc">the FAQ</a> but cannot find the “GTRACT” extension that they mention.</p>
</li>
<li>
<p>What is the difference between the following tractography modules:</p>
</li>
</ol>
<ul>
<li>Diffusion → Tratography → Tractography Seeding; vs</li>
<li>Diffusion → Tractography → Region-based → Tractography ROI Seeding; vs</li>
<li>Diffusion → Tractography → Region-based → Tractography ROI Selection</li>
</ul>
<ol start="3">
<li>Lastly, I have been running DWIconvert fine but for one of my cases DWIConvert either 1) crashes when I use a windows computer; or 2) gives me the following error on the Mac:</li>
</ol>
<blockquote>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
E: DcmElement: CommandField (0000,0100) larger (828667202) than remaining bytes in file</p>
</blockquote>
<p>I have not encountered this error before and am not sure how to fix it. Any help would be greatly appreciated.</p>
<p>Many thanks!!</p>

---

## Post #2 by @zhangfanmark (2020-03-05 19:18 UTC)

<p>Hi!</p>
<p>Regarding your questions:</p>
<ol>
<li>
<p>I am not sure if the GTRACT extension is still available. Other options for eddy correction include DTIprep (<a href="https://www.nitrc.org/projects/dtiprep" rel="nofollow noopener">https://www.nitrc.org/projects/dtiprep</a>), which takes NRRD file as input.</p>
</li>
<li>
<p>In brief, Tractography Seeding enables multiple options to seed tractography, e.g. from a fiducial. Also, it allows interactive tractography, which means when you move the seeding fiducial, the tractography can be updated interactively.</p>
</li>
</ol>
<p>Tractography ROI Seeding enables only seeding within a predefined mask, usually using a brain mask for whole brain tractography.</p>
<p>Tractography ROI Selection is used for fiber selection using ROIs (a labelmap as defined in Slicer) after you have computed tractography.</p>
<p>Please refer to the Slicer DTI tutorial on the SlicerDMRI documentation page for more information. <a href="http://dmri.slicer.org/docs" rel="nofollow noopener">http://dmri.slicer.org/docs</a></p>
<ol start="3">
<li>It’s hard to tell from the error message. I would suggest trying to use the new DCMtNiixGUI module for data conversion, and see if there are still similar problems.</li>
</ol>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @LearningSlicerYay (2020-03-05 20:53 UTC)

<p>Hi Fan,</p>
<p>Thanks for your response, especially for questions 1 and 2. I will look into DTIprep.</p>
<p>Regarding <span class="hashtag">#3</span>, I tried coverting using dcm2niix v1.0.20190902 - no issues, but when I import this file into Slicer I can’t seem to change the DWI component, etc. I am not sure all the components are there. Do you know if there is a way to check?</p>
<p>Many thanks,<br>
AC</p>

---

## Post #4 by @LearningSlicerYay (2020-03-06 14:20 UTC)

<p>Not sure why I can’t edit my post from yesterday anymore - but exporting the files as .nrrd using dcm2niix seems to have fixed the issue above and I can proceed with my pipeline again.</p>

---

## Post #5 by @zhangfanmark (2020-03-06 14:32 UTC)

<p>Thanks for letting us know!</p>
<p>Regards,<br>
Fan</p>

---
