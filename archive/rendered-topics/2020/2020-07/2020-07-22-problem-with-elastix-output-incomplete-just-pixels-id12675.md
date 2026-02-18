# Problem with Elastix: Output incomplete (just pixels)

**Topic ID**: 12675
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/problem-with-elastix-output-incomplete-just-pixels/12675

---

## Post #1 by @KatS (2020-07-22 12:01 UTC)

<p>Dear Slicer community,</p>
<p>I have a problem with Slicer Elastix extension. I’m using Slicer 4.10.2 on Windows 10 and downloaded the Slicer Elastix Extension using the Extension manager.<br>
It usually works fine with my data (preclinical Bruker and clinical Siemens data).<br>
I now have an issue when trying to register scans from a specific dataset, which was acquired 4 years ago on a 9.4 T Bruker scanner (longitudinal brain 3D T2w and 3D T2*w sequences):<br>
I tried to register the T2w scans from follow-up to the baseline scan with Elastix preset generic (all). It runs without error message, but the output file (I created a new file with “Create new output volume as”) consists only of a few pixels delineating the ventricles and parts of the eyes, while the rest of the brain is missing. This is not an issue associated to window level (I tried it in “Volumes”).<br>
The transform generated with this seems to be fine. If I apply it to the inital scan, I get a reasonable result.<br>
I’m able to reproduce this with original DICOMs from this old dataset, with niftys and .nrrd files and with different combinations of sequences.</p>
<p>I tried to register data from this dataset with “GeneralRegistration (BRAINS)” and obtain normal output files.</p>
<p>When doing the same Elastix registration with other datasets acquired recently on the same scanner, the output volume is normal.</p>
<p>Do you have any idea why the output volumes of my old data are corrupted?</p>
<p>I could work around the issue by just creating the transform in Elastix and applying it in a second step or use GeneralRegistration BRAINS instead, but would like to know, if there is an explanation for this problem.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @pieper (2020-07-22 14:19 UTC)

<p>Hi -</p>
<p>No particular reason comes to mind, but if you share a way to reproduce the issue either with your own data or on public sample data perhaps someone can give concrete suggestions.</p>

---

## Post #3 by @lassoan (2020-07-22 14:22 UTC)

<p>Maybe there is something wrong with the image geometry. Could you save the input volumes as nhdr files (image header is then saved as a separate file from voxels) and copy-paste here the content of the nhdr files?</p>

---

## Post #4 by @KatS (2020-07-23 07:03 UTC)

<p>Sure!<br>
Here is the content of the nhdr files of the input volumes and the output:</p>
<p>Scan 1 (3D T2w, fixed volume):<br>
type: double<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 100 200 120<br>
space directions: (0,0,-0.10000000149011608) (0,0.10000000149011608,0) (-0.099999904632568345,0,0)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: raw<br>
space origin: (5.9499943256378174,-9.9500001482665521,4.950000073760747)<br>
data file: Elastix-issue_scan1.raw</p>
<p>Scan 2 (T2*w 3D, moving volume):</p>
<p>type: double<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 188 400 100<br>
space directions: (0.079787231981754303,0,0) (0,0.079999998211860643,0) (0,0,-0.07999992370605466)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: raw<br>
space origin: (-9.5792102813720685,-17.481479644775384,5.8411898612976065)<br>
data file: Elastix-issue_scan2.raw</p>
<p>Output from Elastix:</p>
<p>type: short<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 100 200 120<br>
space directions: (0,0,-0.10000000149999999) (0,0.10000000149999999,0) (-0.099999904600000009,0,0)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: gzip<br>
space origin: (5.9499943255999996,-9.9500001483000009,4.9500000738000001)<br>
data file: Elastix-issue_output.raw.gz</p>
<p>When I apply the output transform to the T2*w scan (= my moving volume) (Data Module --&gt; Transform hierarchy: put scan on transform and harden transform), the scan is registered well to the T2w scan (= my fixed volume). So the transform itself seems to be fine.<br>
This is the nhdr from the result I get when applying the transform in Data Module:</p>
<p>type: double<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 194 388 112<br>
space directions: (0.079787231981754303,0,0) (0,0.079999998211860643,0) (0,0,-0.07999992370605466)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: raw<br>
space origin: (-7.7820387508446265,-14.82506917528052,5.6760153794068611)<br>
data file: scan2-to-scan1_ElastixOutput-transform-applied.raw</p>

---

## Post #5 by @lassoan (2020-07-23 13:55 UTC)

<p>Probably the issue is that you use <code>double</code> scalar type. Medical images usually use <code>short</code> scalar type and you may run into issues at various places if you deviate from this.</p>
<p>The problem here may be that in Elastix parameter sets, the output pixel type is hardcoded:</p>
<pre><code>(ResultImagePixelType "short")
</code></pre>
<p>Changing the parameter set or casting your input data (and maybe also rescaling it) may solve the issue.</p>

---
