# Errors when converting DICOM to NRRD with DWIConvert

**Topic ID**: 1756
**Date**: 2018-01-02
**URL**: https://discourse.slicer.org/t/errors-when-converting-dicom-to-nrrd-with-dwiconvert/1756

---

## Post #1 by @atbauman (2018-01-02 19:59 UTC)

<p>I am having difficulty converting DICOM files to nrrd using the DWIConvert module.</p>
<p>The following command gives the output below:</p>
<p><code>DWIConvert --inputDicomDirectory /path/to/dicom/files --outputVolume output.nrrd</code></p>
<pre><code>======= DWI Convert Public Lib Ctest =========
Exception creating converter
itk::ExceptionObject (0x2f769d0)
Location: "unknown"
File: /home/kitware/Dashboards/Nightly/Slicer-0-build/BRAINSTools/DWIConvert/GenericDWIConverter.cxx
Line: 13
Description: itk::ERROR:  LoadFromDisk not relevant</code></pre>

---

## Post #2 by @ihnorton (2018-01-02 20:23 UTC)

<p>Please add <code>--conversionMode DicomToNrrd</code> to the command line.</p>
<p>(not sure if Andras was helping you, but, x-ref <a href="https://discourse.slicer.org/t/dwi-loading-from-dicom/1746/3">DWI loading from DICOM</a> which I’m looking at right now)</p>

---

## Post #3 by @atbauman (2018-01-02 20:39 UTC)

<p>I have the same error after <code>--conversionMode DicomToNrrd</code> was added. I assumed DicomToNrrd was the default so I left it out the first time.</p>
<p>I have also just run DWIConvert through the GUI and receive the same error.</p>

---

## Post #4 by @ihnorton (2018-01-02 21:25 UTC)

<p>Is the data in <a href="https://discourse.slicer.org/t/dwi-loading-from-dicom/1746/3">this question</a> yours? I just evaluated the sample data <a class="mention" href="/u/lassoan">@lassoan</a> shared there, for a similar error. If so, then we should consolidate the threads and figure out next steps. See:</p>
<aside class="quote quote-modified" data-post="5" data-topic="1746">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dwi-loading-from-dicom/1746/5">DWI loading from DICOM</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for sharing the data. The DWI sequence is 1866: 
BWH003265:1861 inorton$ for f in *; do echo $f; dcmdump $f/$(ls $f | head -n 1) | grep Description; done
1863
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [localizer]                              #  10, 1 SeriesDescription
1864
(0008,1030) LO [NEURO HEAD^BRAIN]                       #  16, 1 StudyDescription
(0008,103e) LO [SAG TSE T1]                             #  10, 1 SeriesDescriptio…
  </blockquote>
</aside>


---

## Post #5 by @atbauman (2018-01-02 21:59 UTC)

<p>No I am using different data than Andras. I am using data exported from a Bruker scanner (7T biospec). I am getting the same error on all the Bruker data I have tried (Diffusion and non-diffusion data).</p>
<p>Though I wonder if this is the wrong approach for what I am trying to do. I am hoping to automatically convert all DICOM files to Nrrd as data is acquired. What I have been doing is using the DICOM module to import data into slicer and then just saving as nrrd within the GUI. I thought the DWIConvert command line interface might be able to help me automate this.</p>

---

## Post #6 by @ihnorton (2018-01-02 22:18 UTC)

<p>I haven’t used DWIConvert with Bruker data, diffusion or otherwise, and the error message is not very helpful, unfortunately. But I do know there is currently no support for Bruker diffusion specifically in DWIConvert (this is a small animal magnet, correct?). If the non-diffusion volumes are “relatively sane” it probably could/should work but may require a bug report with sample data.</p>
<p>If the Slicer DICOM module interface works well, most steps should be accessible via a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting">script in Python</a>, as an alternative automation approach.</p>

---

## Post #7 by @atbauman (2018-01-03 00:27 UTC)

<p>Yes it is a small animal magnet. Just scripting it with python does seem like it is probably the way to go. Thanks!</p>

---

## Post #8 by @zjx1805 (2018-04-10 15:29 UTC)

<p>Hi atbauman,</p>
<p>I am having the same issue as you. However, I could not figure out how you solved it from the selected solution. Would you mind elaborate a little bit? Thanks!</p>

---

## Post #9 by @atbauman (2018-04-11 19:20 UTC)

<p>Hi <a class="mention" href="/u/zjx1805">@zjx1805</a> ,</p>
<p>I suppose calling this solved is not entirely accurate. I solved my issue of converting DICOM files to NRRD, though I ended up doing this without using the DWIConvert module. Instead I wrote a python script using Slicer’s python interpreter instead. The script basically uses the DICOM browser module to import dicom files, and then the Save module to convert them to NRRD. I was able to suppress all the graphical windows so the script can be run without actually opening the Slicer GUI.</p>

---

## Post #10 by @zjx1805 (2018-04-11 19:45 UTC)

<p>Thank you for the clarification!</p>

---
