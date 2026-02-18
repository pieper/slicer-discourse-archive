# MultiVolumeImporter problem in DSCMRIAnalysis module

**Topic ID**: 3591
**Date**: 2018-07-27
**URL**: https://discourse.slicer.org/t/multivolumeimporter-problem-in-dscmrianalysis-module/3591

---

## Post #1 by @Kyu_Sung_Choi (2018-07-27 05:20 UTC)

<p>Dear Dr.Fedorov,</p>
<p><em>I’ve found another missing attribute in MultiVolumeImporter for input of DSCMRIAnalysis module.</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6e15dac60f67c99ed8ec764aef6362cab6afb5b.png" data-download-href="/uploads/short-url/snnnLJZ2NoI8EC8DE3qrlN4nMin.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6e15dac60f67c99ed8ec764aef6362cab6afb5b.png" alt="image" data-base62-sha1="snnnLJZ2NoI8EC8DE3qrlN4nMin" width="690" height="90" data-dominant-color="090909"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1412×185 8.02 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I’ll send you the DSC dicom files via Email, because I cannot upload .dcm files here.<br>
<strong>Could you please update this attribute?</strong><br>
Always thank you and look forward to your fabulous work!</p>
<p>All the best,<br>
Kyu Sung</p>

---

## Post #2 by @fedorov (2018-07-27 14:38 UTC)

<p>In this example (based on the dataset you shared with me in a separate communication), the issue is not in missing attributes, but that the series is not recognized as a multivolume at all. This could be due to various issues.</p>
<p>I’ve just tried to convert this dataset using <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a>, and that also failed with this message:</p>
<pre><code class="lang-nohighlight">Slice positions repeated, but number of slices (319) not 
  divisible by number of repeats (65): missing images?
</code></pre>
<p>It could be that you did not download the complete series from TCIA, or it could also be the TCIA has an incomplete dataset.</p>
<p>From what collection on TCIA did you download that dataset?</p>

---

## Post #3 by @Kyu_Sung_Choi (2018-07-29 10:13 UTC)

<p>Oh I didn’t notice it.<br>
I’ve got the same error msg on my workstation, too.<br>
Maybe I’d better exclude the data.<br>
Thanks!</p>

---
