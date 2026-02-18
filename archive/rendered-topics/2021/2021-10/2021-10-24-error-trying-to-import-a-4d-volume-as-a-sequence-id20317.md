# Error trying to import a 4D volume as a sequence

**Topic ID**: 20317
**Date**: 2021-10-24
**URL**: https://discourse.slicer.org/t/error-trying-to-import-a-4d-volume-as-a-sequence/20317

---

## Post #1 by @kliron (2021-10-24 08:54 UTC)

<p>I have a list of 3D MRI images (70-step time series of 41 slices each) that I combine into a 4D sequence with the JoinSeriesImageFilter by:</p>
<p><code>img4d = sitk.JoinSeries(series)</code></p>
<p>Everything seems to work, <code>series[0].GetSize()</code> as expected returns <code>(128, 128, 41)</code> and <code>img4d.GetSize()</code> correctly returns <code>(128, 128, 41, 70)</code></p>
<p>I save my image to .nrrd:</p>
<p><code>sitk.WriteImage(img4d, 'img4D.nrrd')</code></p>
<p>The header looks ok to me:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned short
dimension: 4
space dimension: 4
sizes: 128 128 41 70
space directions: (1.71407600550601,-0.068471672259036137,-0.10656753702048134,0) (0.0059831519064795693,1.4881492724538934,-0.85992878035812514,0) (0.29446403003947097,1.9949830942955855,3.4544656850761313,0) (0,0,0,1)
kinds: domain domain domain domain
endian: little
encoding: raw
space origin: (-104.3200603168,-110.66393947156,-2.9187184148237999,0)
</code></pre>
<p>Yet when I try to load it to slicer as a Sequence I get the following error:</p>
<p><code>Error: Loading H:/Dokument/Data/dsc/Derived/img4D.nrrd - Failed to read node img4D (vtkMRMLSequenceNode4) from filename='H:/Dokument/Data/Derived/img4D.nrrd'</code></p>
<p>EDIT: I should also mention that I <em>can</em> load the file as a Volume but then, as expected, only a single 3D volume node is presented.</p>
<p>EDIT2: My Slicer version is 4.11.20210226 and I am on Windows 10 if that is important.</p>

---

## Post #2 by @kliron (2021-10-25 07:13 UTC)

<p>It seems the problem is that my 4D image is missing ‘MultiVolume.FrameIdentifyingDICOMTagName’ and thus cannot be loaded as a MultiVolume. How do I set this attribute when I construct the 4D series?</p>

---
