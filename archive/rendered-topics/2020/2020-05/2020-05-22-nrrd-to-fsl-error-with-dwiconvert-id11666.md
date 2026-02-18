# NRRD to FSL error with DWIConvert

**Topic ID**: 11666
**Date**: 2020-05-22
**URL**: https://discourse.slicer.org/t/nrrd-to-fsl-error-with-dwiconvert/11666

---

## Post #1 by @amate (2020-05-22 07:24 UTC)

<p>Operating system: MacOS Mojave<br>
3DSlicer v. 4.10.2</p>
<p>Hi everyone,</p>
<p>I have successfully used DWIConvert in Slicer to convert my dicom data to nrrd so I can process it in DTIPrep. However, I am running into problems when trying to convert the DTIPrep QCed nrrd files back into nifti using DWIConvert.</p>
<p>I am getting the following error message:</p>
<pre><code class="lang-auto">======= DWI Convert Tool Program=========
Error: file type of inputVoume is not supported currently
Error: the output file type is not supported currently
illegal input file type, exit
nrrd2nifti_test.sh: line 19: --inputVolume: command not found
</code></pre>
<p>After some time troubleshooting, I am not quite sure what has gone wrong and would greatly appreciate any help. I haven’t found a post on this topic, so my apologies if a similar problem has already been addressed.</p>
<p>This is the code I have used is below if that is helpful at all.</p>
<pre><code class="lang-auto">-----------------------------
### set paths to Slicer
export PATH=$PATH:/Applications/Slicer.app/Contents/lib/Slicer-4.10/cli-modules

#### Finds if path is set correctly
if [ `which DWIConvert | wc -l` -eq 0 ]; then
echo "Cannot find DWIConvert, is it in your PATH?"
exit;
fi

echo "Path found"

for directory in ????? ; do
	cd $directory
	# Convert corrected DWI image data from NRRD to NIFTI
	DWIConvert \
	--conversionMode NrrdToFSL
	--inputVolume ${directory}_QCed.nrrd \
        --outputVolume ${directory}_QCed.nii \
	--outputBValues ${directory}_QCed.bval \
	--outputBVectors ${directory}_QCed.bvec \
	--smallGradientThreshold 0.2 \

	echo $directory
	
	cd ../

done
</code></pre>

---

## Post #2 by @pieper (2020-05-22 13:22 UTC)

<p>We now suggest using dcm2niix, which has nrrd &lt;–&gt; nifti conversion support for diffusion.  You can get it in SlicerDMRI.  Also good to update to the latest preview version of Slicer.</p>

---

## Post #3 by @amate (2020-05-28 17:16 UTC)

<p>Thanks for the tip regarding dcm2niix.</p>
<p>My apologies if I have completely missed something, but it seems that dcm2niix only has an option to go from dicom to NRRD using the following option in the command line.</p>
<p>-e : export as NRRD instead of NIfTI</p>
<p>I haven’t had  success using dcm2niix within slicer (10.11.0) itself. I installed Slicer DMRI with the dcm2niix extension, and tried to run through the extension by adding my directory to “input directory” but no file seems to be created. It opens the data, but it does not seem to convert the NRRD file to nifti.</p>
<p>Let me know if I have just completely missed a step! Any help would be greatly appreciated.</p>

---

## Post #4 by @pieper (2020-05-28 18:24 UTC)

<p>Probably <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> can advise on dcm2niix.</p>
<p>For SlicerDMRI, are you working with the latest nightly preview build?  If not, you should.</p>

---

## Post #5 by @amate (2020-05-28 19:04 UTC)

<p>Hm ok I just gave this a try. I just downloaded the latest preview build of Slicer (4.11.0-2020-05-27). I then re-installed SlicerDMRI and SlicerDcm2niix.</p>
<p>I then go to Modules &gt; Diffusion &gt; Import and Export &gt; DCM2niix(GUI). I get a GUI with the option to enter an input directory. I add my directory with only the DTIprepped files and when I click apply I get the following error message.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c12b515ae4e394827bce1e067359b95a75b95f7a.jpeg" data-download-href="/uploads/short-url/ryQXvf2F2XEozs5VMZMvgrSPGc2.jpeg?dl=1" title="Screen Shot 2020-05-28 at 3.02.28 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12b515ae4e394827bce1e067359b95a75b95f7a_2_690x390.jpeg" alt="Screen Shot 2020-05-28 at 3.02.28 PM" data-base62-sha1="ryQXvf2F2XEozs5VMZMvgrSPGc2" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12b515ae4e394827bce1e067359b95a75b95f7a_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12b515ae4e394827bce1e067359b95a75b95f7a_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c12b515ae4e394827bce1e067359b95a75b95f7a_2_1380x780.jpeg 2x" data-dominant-color="AEADB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-05-28 at 3.02.28 PM</span><span class="informations">2078×1176 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2020-05-28 19:33 UTC)

<p>I agree, that’s cryptic, and the module doesn’t have documentation that I can find.</p>
<p>But I believe the gui works only for directories of dwi dicom files, but there should be a command line option. <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> or <a class="mention" href="/u/tbillah">@tbillah</a> can maybe comment?</p>

---

## Post #7 by @zhangfanmark (2020-05-28 22:49 UTC)

<p>Hi Steve, as far as I know, dcm2niix supports conversion from dicom, but not nrrd to nifti.</p>
<p><a class="mention" href="/u/amate">@amate</a> I think there is an error in your command. It should be --outputNiftiFile, not --outputVolume.</p>
<p>Here is an example:<br>
/Applications/Slicer200421.app/Contents/lib/Slicer-4.11/cli-modules/DWIConvert --conversionMode NrrdToFSL --inputVolume ~/Desktop/DTI.nrrd --outputNiftiFile ~/Desktop/a.nii --outputBValues ~/Desktop/a.bval --outputBVectors ~/Desktop/a.bvec --smallGradientThreshold 0.2  --allowLossyConversion</p>

---

## Post #8 by @pieper (2020-05-28 23:46 UTC)

<aside class="quote no-group" data-username="zhangfanmark" data-post="7" data-topic="11666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhangfanmark/48/4451_2.png" class="avatar"> zhangfanmark:</div>
<blockquote>
<p>Hi Steve, as far as I know, dcm2niix supports conversion from dicom, but not nrrd to nifti.</p>
</blockquote>
</aside>
<p>I know <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> and <a class="mention" href="/u/tbillah">@tbillah</a> were <a href="https://github.com/rordenlab/dcm2niix/search?q=nrrd&amp;type=Commits">working on it</a> and I thought it was done, but maybe it’s not in the release yet.</p>

---

## Post #9 by @tbillah (2020-05-29 13:58 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, we made dcm2niix yield NRRD directly from dicoms apart from its default function of yielding NIFTI. However, conversion of NRRD&lt;–&gt;NIFTI is not the scope of dcm2niix and so it is not there.</p>
<p>Hi <a class="mention" href="/u/amate">@amate</a>, I see two issues you reported here:</p>
<ol>
<li>You are not able to convert NRRD–&gt; NIFTI using DWIConvert:</li>
</ol>
<p>In the community, we are inclined towards eliminating use of this converter. Instead, please use the <a href="https://github.com/pnlbwh/conversion#introduction" rel="nofollow noopener">Python tool</a> I developed for achieving the stated conversion. dcm2niix uses the same tool to yield NRRD directly from dicoms.</p>
<ol start="2">
<li>You are not able to run SlicerDcm2niix:</li>
</ol>
<p>If you click on the red cross button on bottom right corner, you should find an elaborate log. If you can provide the elaborate log, we may be able to help you run that.</p>
<p>Hope this helps. Thanks.</p>

---

## Post #10 by @pieper (2020-05-29 15:43 UTC)

<p>Cool - thanks <a class="mention" href="/u/tbillah">@tbillah</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">  Looks like that is the direction <a class="mention" href="/u/amate">@amate</a> should investigate.</p>

---

## Post #11 by @amate (2020-06-17 21:18 UTC)

<p>Thanks <a class="mention" href="/u/tbillah">@tbillah</a> and <a class="mention" href="/u/pieper">@pieper</a>! The Python tool worked perfectly!!  Thanks for your help!</p>

---

## Post #12 by @smeisler (2020-07-03 23:27 UTC)

<p>I know this is maybe too little too late to be relevant, but in the original code, you need a back slash after the line for conversionMode. That is why it is not recognizing the input volume and also thinks that --inputVolume is its own command.</p>

---
