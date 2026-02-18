# Problem loading segmentation from file (trouble parsing space directions info)

**Topic ID**: 3444
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/problem-loading-segmentation-from-file-trouble-parsing-space-directions-info/3444

---

## Post #1 by @Laura_CM (2018-07-10 13:15 UTC)

<p>Hi everyone.<br>
I am a new user and I apologize for my English, I am trying to do my best to explain.</p>
<p>When I save my work, all files that get created after segmentation, export it, etc. Then I can’t open them and appear the following error message:</p>
<pre><code class="lang-auto">Slicer has caught an internal error.
You may be able to continue from this point, but results are undefined.
Suggested action is to save your work and restart.
If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at http://slicer.org

The message detail is:

Exception thrown in event: D:\D\blablabla:
itk::ERROR: NrrdImageIO(000001E7F3BD21E0): ReadImageInformation: Error reading C:/blabla/Segmentation.seg.nrrd:
[nrrd] nrrdLoad: trouble reading "C:/blabla/Segmentation.seg.nrrd"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: trouble parsing space directions info |(-0,70703125,-0,0) (-0,-0,70703125,-0) (0,0,5)|
[nrrd] _nrrdReadNrrdParse_space_directions: trouble getting space vector 1 of 3
[nrrd] _nrrdSpaceVectorParse: space dimension is 3, but seem to have 4 coefficients
</code></pre>
<p>What I am doing wrong? Is there any way to open or load them?</p>
<p>Thanks you very much in advance!</p>

---

## Post #2 by @lassoan (2018-07-10 14:17 UTC)

<p>It seems that your locale is set so that comma (<code>,</code>) character is used as decimal mark and for some reason the NRRD file writer uses this locale-specific mark, instead of the standard dot (<code>.</code>) mark.</p>
<p>Can you upload the Segmentation.seg.nrrd file that you are trying to read?<br>
What operating system do you use? What language/regional setting is selected in the operating system?<br>
Does it work correctly if you use latest nightly version of Slicer (4.9.x version)?</p>

---

## Post #3 by @Laura_CM (2018-07-11 06:24 UTC)

<p>I am using latest nightly version for Windows 10. But it is already resolved.</p>
<p>What I have done is to change the format of these files .nrrd for .vkt which is compatible. Then, when I load the folder on Slicer, I dont check files .png, .py nor the scene created by the programme. Immediatly, I load the DICOM and import the segmentation which I want to edit, within the module Segmentations. It is already to work!</p>

---

## Post #4 by @samuelholly (2021-01-15 10:02 UTC)

<p>Dear everyone,</p>
<p>I have the same problem, but the above solution by <a class="mention" href="/u/laura_cm">@Laura_CM</a> does not work for me. Could you kindly suggest what could be done here?</p>
<p>I’m running Slicer 4.11.0 2020-05-30 pre-release on a Windows 10 machine.</p>
<p>Thank you in advance.</p>
<p>Samuel</p>

---

## Post #5 by @samuelholly (2021-01-15 14:13 UTC)

<p>Hello again,</p>
<p>I decided to do the segmenting again from scratch. Luckily, I had only few segmentations affected by this issue.</p>
<p>So for me it is solved.</p>
<p>Best regards</p>
<p>Samuel</p>

---
