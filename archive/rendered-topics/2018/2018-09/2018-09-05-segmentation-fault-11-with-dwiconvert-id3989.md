# Segmentation fault: 11 with DWIConvert

**Topic ID**: 3989
**Date**: 2018-09-05
**URL**: https://discourse.slicer.org/t/segmentation-fault-11-with-dwiconvert/3989

---

## Post #1 by @alca (2018-09-05 12:30 UTC)

<p>Dear Slicer experts,</p>
<p>I am trying to use DTIConvert to convert nrrd to nii (–conversionMode NrrdToFSL) on the data  that were previously preprocessed by DTIPrep (before that I successfully converted them from nii to nrrd), but I am receiving the error message “Segmentation fault: 11”. Any idea what went wrong?</p>
<p>Looking forward to your response.</p>
<p>Best</p>
<p>Alena</p>

---

## Post #2 by @alca (2018-09-07 11:30 UTC)

<p>Operating system: Mac Os<br>
Slicer version: 4.8.1</p>
<p>I am trying to use DWIConvert to convert nrrd to nii (–conversionMode NrrdToFSL) on the data that were previously preprocessed by DTIPrep (before that I successfully converted them from nii to nrrd), but I am receiving the error message “Segmentation fault: 11”. Any idea what went wrong?</p>
<p>Best</p>
<p>Alena</p>

---

## Post #3 by @lassoan (2018-09-07 12:40 UTC)

<p>Does DTIConvert in <em>latest nightly version</em> of Slicer work well?</p>

---

## Post #4 by @alca (2018-09-10 07:50 UTC)

<p>Haven’t tried that I only used 4.8.1 and when it did not work the version of DWIConvert from GitHub.</p>

---

## Post #5 by @lassoan (2018-09-10 17:57 UTC)

<p>Could you please try if DTIConvert in <em>latest nightly version</em> of Slicer works as expected?</p>

---

## Post #6 by @ihnorton (2018-10-03 20:28 UTC)

<aside class="quote no-group" data-username="alca" data-post="1" data-topic="3989">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7ab992/48.png" class="avatar"> alca:</div>
<blockquote>
<p>Any idea what went wrong?</p>
</blockquote>
</aside>
<p>You may need to use the <code>--allowLossyConversion</code> option (if your data can be converted safely). Aside from that, it is very hard to say without more information – the command line you used, example data, etc.</p>

---

## Post #7 by @ihnorton (2018-10-03 20:33 UTC)

<p>In case it helps, here is an example command line I wrote in a script earlier:</p>
<pre><code class="lang-auto">DWIConvert --conversionMode NrrdToFSL \
    --inputVolume dwi.nhdr \
    --outputBVectors dwi.bvec \
    --outputBValues dwi.bval \
    --outputNiftiFile dwi.nii
</code></pre>

---

## Post #8 by @Drew (2018-11-15 23:26 UTC)

<p>I’m also experiencing this issue, first with the newest stable version, and also with the latest nightly build. I’m simply trying to convert between nifti format and .nrrd to QC in DTIPrep, but DWIConvert is not working to convert from the .nrrd back to .nii. Any suggestions?</p>

---

## Post #9 by @ljod (2018-11-16 18:33 UTC)

<p>Have you tried the options and suggestions above? Such as the lossy conversion? It is hard to give more advice without more information (see the information Isaiah requests above for a list that can help us). Also please try the example command line, or try using those options in the GUI.</p>

---

## Post #10 by @Drew (2018-11-16 21:03 UTC)

<p>Thanks for the reply.</p>
<p>I originally had this issue runnnng it from the command line, but it happens in the GUI as well.<br>
Without the lossy conversion option, it initially generates an error, “Error: ReadVolume: Unsupported source pixel type”<br>
When I run it with the lossy conversion option, it changes the error to ‘Segmentation fault: 11’<br>
I’ve tried it with the stable build (4.10), the nightly build (4.11) and older versions (4.8).</p>
<p>One issue that could possibly contribute to this is that I’ve started with a 4D DWI file in .nii format, that includes 2 separate acquisitions. I extract those into two separate files, split out the b-vectors and b-values, and then convert the resultant .nii files into .nrrd files before running DTIPrep on each .nrrd files. Then, when I try to convert back to .nii, I get these errors.</p>
<p>Any ideas? What other information would be helpful for you?</p>
<p>Many thanks,<br>
-Drew</p>

---

## Post #11 by @ihnorton (2018-11-20 18:52 UTC)

<p>Unfortunately, DWIConvert has some crash modes which do not produce informative error messages due to exception handling issues. My guess is that something about your files does not correspond to DWIConvert’s expectation, and it crashes. If you can reproduce your workflow on one of these <a href="https://discourse.slicer.org/t/not-working-dwi-component/4793/3?u=ihnorton">public datasets</a>, and then share the resulting nrrd file with me, then I can take a look.</p>

---
