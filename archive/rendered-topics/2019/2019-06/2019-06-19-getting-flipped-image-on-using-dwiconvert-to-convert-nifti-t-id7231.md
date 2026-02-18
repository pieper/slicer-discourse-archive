# Getting flipped image on using DWIConvert to convert nifti to nhdr/nrrd

**Topic ID**: 7231
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/getting-flipped-image-on-using-dwiconvert-to-convert-nifti-to-nhdr-nrrd/7231

---

## Post #1 by @Ashutosh_Vaish (2019-06-19 09:39 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.10.2<br>
Expected behavior: Orientation of nifti image is same as nhdr/nrrd<br>
Actual behavior: Image is getting rotated and there is shift in dimensions of 4D data volume.</p>
<p>Dear Slicer Experts</p>
<p>I want to convert some Nifti DTI volumes to nhdr/nrrd format using available .bval and .bvec files. Currently, I am using DWIConvert from Slicer modules and have selected FSLtoNrrd conversion option.</p>
<p>Link to data : <a href="http://hardi.epfl.ch/static/events/2013_ISBI/training_data.html#trainingdata" rel="nofollow noopener">http://hardi.epfl.ch/static/events/2013_ISBI/training_data.html#trainingdata</a><br>
I am using 64 directions b=3000 hardi volume of SNR 30 with available bval and bvec files.</p>
<p>Problems I am facing:</p>
<ol>
<li>bvectors are getting negated in nhdr file (I am not sure if some parameter is set in nhdr too compensate for that).</li>
<li>Original data size is as 50x50x50x65. After conversion to Nhdr I am getting a size of 65x50x50x50.<br>
Apart from this visible shift in dimension (65 from dim-4 to dim-1), there is also change in orientation along other three dimensions.</li>
</ol>
<p>I am using python’s nibabel and pynrrd libraries to read nifti and nrrd formats but the two image volumes I am getting are not in same orientation. I need nrrd data to allign with the orientation of original nifti image volume.</p>
<p>I basically want to bypass this reorientation by slicer while loading data. Can you please help me with this?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2019-06-19 21:13 UTC)

<p>Hi <a class="mention" href="/u/ashutosh_vaish">@Ashutosh_Vaish</a> -</p>
<p>It sounds like a good first step would be to try <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage" rel="nofollow noopener">dcm2niix</a>, which is newer than DWIConvert and the most recent versions include nifti to nrrd dwi conversions.  You can get it as a Slicer extension but probably you want the command line version with all the options exposed.  Let us know how that goes.</p>
<p>-Steve</p>

---

## Post #3 by @Ashutosh_Vaish (2019-06-20 07:32 UTC)

<p>Hi Steve</p>
<p>Thank you for your response. I looked at the dcm2niix Git-repo that you redirected me to and in the list of tools that utilize dcm2niix, I found another Git-repo : <a href="https://github.com/pnlbwh/pnlNipype" rel="nofollow noopener">https://github.com/pnlbwh/pnlNipype</a> , specifically for nifti-nhdr conversion. I am able to write an .nhdr for my nifti without any orientation change using this script.</p>
<p>Thank you for your help. I was really struggling for where to look at.</p>

---
