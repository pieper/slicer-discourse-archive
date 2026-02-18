# pkModelling 4D fitted data output 

**Topic ID**: 2387
**Date**: 2018-03-21
**URL**: https://discourse.slicer.org/t/pkmodelling-4d-fitted-data-output/2387

---

## Post #1 by @deepsky (2018-03-21 15:54 UTC)

<p>Hi experts,</p>
<p>is there a way to convert pkModelling 4D data fits (.nhdr/.raw.gz) to nii.gz? I tried a) saving data as .nrrd and applying pynrrd which resulted in corrupted spatial information, and b) exporting data as DICOM files resulting in complete loss of 4D information. Got stuck at this point.</p>
<p>Any ideas?</p>
<p>Any help is very much appreciated!</p>
<p>All the best<br>
Billy</p>

---

## Post #2 by @fedorov (2018-03-21 20:13 UTC)

<p>No, we don’t provide such capability. May I ask what is the reason you prefer NIFTI?</p>

---

## Post #3 by @deepsky (2018-03-22 07:17 UTC)

<p>One reason is, that DCE data are part of a multiparametric brain data set. Morphometric analyses were performed using freesurfer/fsl. So all morphometric segmentations are nifti (there are a lot), and I need to apply a conjoint analysis of all different signals per structure (in batch mode).<br>
The other reason is, that pkModelling yields plausible ktrans values (longitudinal measures before and after intervention) but strange r-squared values. At visual inspection data fits seem to be not that bad (however there are indeed drawbacks of that study, e.g. no T1 map). So I’d like to analyse these fits a little more by generating a mean data fit for every morphometric segmentation and comparing them. Ideally I would do this for varying initial assumptions (population AIF vs. AIF mask, T1 tissue values for white and gray matter, etc) to better understand data, model fit and error.</p>
<p>Best<br>
Billy</p>

---

## Post #4 by @fedorov (2018-03-22 14:46 UTC)

<p>Thanks for the details, this makes sense.</p>
<p>I have not tried it myself, but I heard that the latest SimpleITK release supports 4d data (see this post <a href="https://discourse.itk.org/t/simpleitk-1-1-release-candidate-1/664">https://discourse.itk.org/t/simpleitk-1-1-release-candidate-1/664</a>). You might want to try that to use nrrd output. If you absolutely need nifti, it should be doable - recently <a class="mention" href="/u/pieper">@pieper</a> added support for reading 4d nifti input in MultiVolumeExplorer (see <a href="https://github.com/fedorov/MultiVolumeImporter/pull/30">https://github.com/fedorov/MultiVolumeImporter/pull/30</a>) - maybe you could follow that example to add the capability to export? It sounds like you are technically savvy to work on this. Your contribution would be most welcomed, as I can’t make time to work on this feature myself at the moment.</p>
<p>Let us know what you think.</p>

---

## Post #5 by @deepsky (2018-03-25 09:59 UTC)

<p>I’m afraid I’m a newbie to slicer and just about to understand it (in part). So, I’m barely skimming the surface: for example, I’d like to get rid of the gui based approach and run pkmodelling via command line. Is there a bash „slicer based“ command? Or is pkmodelling.py the way to go?</p>

---

## Post #6 by @fedorov (2018-03-25 21:00 UTC)

<p>PkModeling is a CLI module. You can invoke it from command line as any other CLI module, as described in the FAQ entry here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_call_a_CLI_module_from_command-line.3F">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_call_a_CLI_module_from_command-line.3F</a></p>

---
