# DTIPrep, Nrrd to Nifti conversion, and header info

**Topic ID**: 2396
**Date**: 2018-03-22
**URL**: https://discourse.slicer.org/t/dtiprep-nrrd-to-nifti-conversion-and-header-info/2396

---

## Post #1 by @micaceous (2018-03-22 03:35 UTC)

<p>I’ve been using Ubuntu 16.04 on Bash on Windows (but this problem has occurred within regular linux/ubuntu as well).</p>
<p>After running DTIPrep (through their own tool, not through Slicer module), cannot convert .nrrd to .nii.gz due to “unsupported source pixel type” / “unsigned_short” (as has been discussed)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a39529dc1420e506035a255b00d2e4b1b818c2e.png" data-download-href="/uploads/short-url/aAC93Thf2rNfxEOUM6lDT2IjH1s.png?dl=1" title="Slicer_dwiconvert_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a39529dc1420e506035a255b00d2e4b1b818c2e.png" alt="Slicer_dwiconvert_error" data-base62-sha1="aAC93Thf2rNfxEOUM6lDT2IjH1s" width="602" height="500" data-dominant-color="0C0D0E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_dwiconvert_error</span><span class="informations">874×725 37.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know that this error can be fixed with the -allowLossyConversion option, but another problem is that this slicer conversion output has wrong header info (flipped on anterior/posterior axis). In the past, I’ve fixed this by following the FSL instructions <a href="https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Orientation%20Explained" rel="noopener nofollow ugc">here</a>, with the example code below:</p>
<p>fslorient -deleteorient filename.nii.gz<br>
[which is output from DWIConvert]<br>
fslorient -setsformcode 1 filename.nii.gz</p>
<p>However, this fixed header file causes problems for registrations of this diffusion data to T1 weighted data.</p>
<p>I’m wondering:</p>
<ol>
<li>
<p>can this “unsupported source pixel type” be avoided in the DTIPrep output by running DTIPrep as a Slicer module? (in other words, does DTIPrep as a Slicer module create output that is already “short”?)</p>
</li>
<li>
<p>Is there any other option other than -allowLossyConversion to move from unsigned_short to short?</p>
</li>
<li>
<p>or, is there a better way to fix the header of the output after Lossy conversion from nrrd to nifti?</p>
</li>
</ol>
<p>Thanks so much!<br>
Micah</p>

---
