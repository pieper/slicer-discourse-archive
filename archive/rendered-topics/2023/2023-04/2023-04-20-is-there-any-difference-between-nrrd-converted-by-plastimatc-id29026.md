---
topic_id: 29026
title: "Is There Any Difference Between Nrrd Converted By Plastimatc"
date: 2023-04-20
url: https://discourse.slicer.org/t/29026
---

# Is there any difference between nrrd converted by plastimatch and slicer? What algorithm is used by slicer to convert to nrrd

**Topic ID**: 29026
**Date**: 2023-04-20
**URL**: https://discourse.slicer.org/t/is-there-any-difference-between-nrrd-converted-by-plastimatch-and-slicer-what-algorithm-is-used-by-slicer-to-convert-to-nrrd/29026

---

## Post #1 by @b_s_umesh_sherkhane (2023-04-20 11:31 UTC)

<p>Hi ,<br>
I am trying to extract radiomics from PET dicom. I converted the dicom to nrrd using two methods.</p>
<ol>
<li>using slicer i saved the image and mask to nrrd</li>
<li>Using plastimatch i converted the dicom to nrrd.<br>
When i run pyradiomics on the nrrds from slicer it works fine. but if i run pyradiomics on the plastimatch converted nrrds then radiomics extraction is going forever and hung.<br>
Any idea if there is any difference between the plstimatch and slicer nrrds? Can you also describe how slicer converts to nrrd, what algorithm is used ?</li>
</ol>
<p>Thanks and regards</p>

---

## Post #2 by @gcsharp (2023-04-20 15:58 UTC)

<p>Hmm.  Not sure why that would be.  Plastimatch nrrds are created using ITK and are always compressed.   Maybe pyradiomics needs an uncompressed nrrd?</p>
<p>Anyway, if you open the nrrd files with a text editor, you can look at the ASCII header.  This might help you to debug.  Or if you post both headers here I can take a look.</p>

---

## Post #3 by @lassoan (2023-04-20 16:41 UTC)

<p>ITK’s DICOM reader only works for simple Cartesian images (all slices are parallel, slice spacing is uniform, gantry is not tilted, etc.) and you may need to move all DICOM files into a different folder that do not belong to the series that you want to read.</p>

---

## Post #4 by @gcsharp (2023-04-20 17:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes, interesting idea.  It might be related to import rather than export.  Plastimatch does not use ITK for DICOM import.</p>

---

## Post #5 by @b_s_umesh_sherkhane (2023-04-24 06:42 UTC)

<p>Hi Greg,</p>
<p>Thanks for the reply. here are the headers of the nrrd files</p>
<p><strong>1. slicer nrrd</strong></p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: double
dimension: 3
space: left-posterior-superior
sizes: 128 128 90
space directions: (2,0,0) (0,2,0) (0,0,2)
kinds: domain domain domain
endian: little
encoding: gzip
space origin: (-127.585938,-57.585937999999999,-358.5)
</code></pre>
<ol start="2">
<li>plastimatch nrrd</li>
</ol>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: float
dimension: 3
space: left-posterior-superior
sizes: 128 128 90
space directions: (2,0,0) (0,2,0) (0,0,2)
kinds: domain domain domain
endian: little
encoding: gzip
space origin: (-127.5859375,-57.5859375,-358.5)
</code></pre>

---

## Post #6 by @b_s_umesh_sherkhane (2023-04-24 06:48 UTC)

<p>which package does plastimatch use to import the dicoms ?</p>

---

## Post #7 by @gcsharp (2023-05-08 14:26 UTC)

<p>Plastimatch uses dcmtk.</p>
<p>The only difference appears to be the type, and a bit of rounding in the origin.  Can you try converting to double type?</p>
<p><code>plastimatch convert --output-type double ...</code></p>

---
