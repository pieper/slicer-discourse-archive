---
topic_id: 45114
title: "Download Sample Data Not Working"
date: 2025-11-17
url: https://discourse.slicer.org/t/45114
---

# Download sample data not working

**Topic ID**: 45114
**Date**: 2025-11-17
**URL**: https://discourse.slicer.org/t/download-sample-data-not-working/45114

---

## Post #1 by @PaoloZaffino (2025-11-17 12:21 UTC)

<p>Hi all,<br>
I tried to download some sample data by using the dedicated extension but it keeps downloading and no data is loaded.</p>
<p>Paolo</p>

---

## Post #2 by @Andinet_Enquobahrie (2025-11-17 19:33 UTC)

<p>Could you please let us know which Slicer version you are using and which operating system?</p>

---

## Post #3 by @PaoloZaffino (2025-11-17 22:44 UTC)

<p>Stable version (5.10.0) on Linux.</p>
<p>I get these messages in the python console</p>
<blockquote>
<p>[VTK] vtkMRMLModelStorageNode::ReadDataInternal: Failed to load model: unrecognized file extension ‘.gipl.gz’ of file ‘/home/p4ol0/.cache/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz’.</p>
<p>[VTK] vtkMRMLStorageNode::ReadData: Failed to read node (null) ((null)) from filename=‘/home/p4ol0/.cache/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz’</p>
<p>[VTK] Couldn’t read file, returning null fiberBundle node: /home/p4ol0/.cache/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz</p>
<p>[Python] Load failed!</p>
<p>[Python] Load failed (attempt 1 of 3)…</p>
</blockquote>
<p>I think the same happens for the preview.</p>

---

## Post #4 by @muratmaga (2025-11-17 22:55 UTC)

<p>Is this your custom build or the installer? I can’t replicate this is on Linux using standard package from <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>.</p>
<pre><code class="lang-auto">Requesting download PreDentalSurgery.gipl.gz from https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/7bfa16945629c319a439f414cfb7edddd2a97ba97753e12eede3b56a0eb09968 ...
Downloaded 2.4 MB (10% of 23.6 MB)...
Downloaded 4.7 MB (20% of 23.6 MB)...
Downloaded 7.1 MB (30% of 23.6 MB)...
Downloaded 9.5 MB (40% of 23.6 MB)...
Downloaded 11.8 MB (50% of 23.6 MB)...
Downloaded 14.2 MB (60% of 23.6 MB)...
Downloaded 16.5 MB (70% of 23.6 MB)...
Downloaded 18.9 MB (80% of 23.6 MB)...
Downloaded 21.3 MB (90% of 23.6 MB)...
Downloaded 23.6 MB (100% of 23.6 MB)...
Download finished
Verifying checksum
Checksum OK
Requesting load PreDentalSurgery from /home/exouser/.cache/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz ...
"Volume" Reader has successfully read the file "/home/exouser/.cache/slicer.org/Slicer/SlicerIO/PreDentalSurgery.gipl.gz" "[0.28s]"
Load finished

Requesting download PostDentalSurgery.gipl.gz from https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/4cdc3dc35519bb57daeef4e5df89c00849750e778809e94971d3876f95cc7bbd ...
Downloaded 3.4 MB (10% of 33.8 MB)...
Downloaded 6.8 MB (20% of 33.8 MB)...
Downloaded 10.1 MB (30% of 33.8 MB)...
Downloaded 13.5 MB (40% of 33.8 MB)...
Downloaded 16.9 MB (50% of 33.8 MB)...
Downloaded 20.3 MB (60% of 33.8 MB)...
Downloaded 23.6 MB (70% of 33.8 MB)...
Downloaded 27.0 MB (80% of 33.8 MB)...
Downloaded 30.4 MB (90% of 33.8 MB)...
Downloaded 33.8 MB (100% of 33.8 MB)...
Download finished
Verifying checksum
Checksum OK
Requesting load PostDentalSurgery from /home/exouser/.cache/slicer.org/Slicer/SlicerIO/PostDentalSurgery.gipl.gz ...
"Volume" Reader has successfully read the file "/home/exouser/.cache/slicer.org/Slicer/SlicerIO/PostDentalSurgery.gipl.gz" "[0.29s]"
Load finished

</code></pre>
<p>If you are custom building, did you any chance turn off gipl support off in ITK?</p>

---

## Post #5 by @PaoloZaffino (2025-11-17 23:07 UTC)

<p>I’m using the build available on the website.</p>
<p>I’m on Arch Linux</p>

---

## Post #6 by @lassoan (2025-11-17 23:26 UTC)

<p>Can tou load other data sets that are not in gipl.gz file format?</p>
<p>Have you installed any extensions or Python packages? (maybe your ITK IO classes have been overwritten)</p>

---

## Post #7 by @PaoloZaffino (2026-01-05 16:42 UTC)

<p>Sorry for the huge delay.</p>
<p>I noticed I have problems only with the CBCTDentalSurgery dataset.</p>
<p>Paolo</p>

---

## Post #8 by @lassoan (2026-01-05 22:36 UTC)

<p>CBCTDentalSurgery uses the very rare .gipl.gz file format, so your ITK might not have been built without support it. Which Slicer version is this? Have you built it yourself?</p>

---

## Post #9 by @PaoloZaffino (2026-01-06 22:46 UTC)

<p>I am using the binaries downloaded from website (Linux OS).</p>
<p>I just noticed that if I use fresh-new slicer it works, so now I’m trying to figure out if it is something related to the installation of some extension (and if so wich one)</p>

---

## Post #10 by @lassoan (2026-01-12 17:41 UTC)

<p>Does the image reading break if you <code>pip_install('SimpleITK')</code>?</p>

---

## Post #11 by @PaoloZaffino (2026-01-18 14:45 UTC)

<p>No, if I force to reinstall SimpleITK it works.</p>
<p>If I install TotalSegmentator and DentalSegmentator it got the problem.</p>
<p>If I install TotalSegmentator or DentalSegmentator, the sample data works well.</p>

---
