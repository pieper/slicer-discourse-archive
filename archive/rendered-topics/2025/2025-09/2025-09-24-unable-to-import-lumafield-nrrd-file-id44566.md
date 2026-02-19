---
topic_id: 44566
title: "Unable To Import Lumafield Nrrd File"
date: 2025-09-24
url: https://discourse.slicer.org/t/44566
---

# Unable to Import Lumafield NRRD file

**Topic ID**: 44566
**Date**: 2025-09-24
**URL**: https://discourse.slicer.org/t/unable-to-import-lumafield-nrrd-file/44566

---

## Post #1 by @mchon (2025-09-24 02:11 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.8.1<br>
Expected behavior: Load NRRD file as volume<br>
Actual behavior: Error loading data. Does not recognize NRRD file.</p>
<p>We use a X-Ray CT from a local startup called Lumafield. We lease a CT machine from them and their web-based software automates the reconstruction for us, along with other analysis features. One of their features is the ability to export scans as NRRD files. However, I am u nable to load any of the NRRD files into Slicer (~85MB).</p>
<p>I’ve attached the error log and the header info from the NRRD file below:</p>
<p>==== Error Log ======</p>
<p>CanReadFile failed: [nrrd] nrrdLoad: trouble reading “C:/Users/MichaelChon/Downloads/2dee31ef-f170-4b82-ac12-e58663efae71.nrrd”</p>
<p>[nrrd] nrrdRead: trouble</p>
<p>[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read: trouble parsing space directions info |(0,0,1) (0,1,0) (1,0,0)|</p>
<p>[nrrd] _nrrdReadNrrdParse_space_directions: don’t yet have a valid space dimension</p>
<p>CanReadFile failed: [nrrd] nrrdLoad: trouble reading “C:/Users/MichaelChon/Downloads/2dee31ef-f170-4b82-ac12-e58663efae71.nrrd”</p>
<p>[nrrd] nrrdRead: trouble</p>
<p>[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read: trouble parsing space directions info |(0,0,1) (0,1,0) (1,0,0)|</p>
<p>[nrrd] _nrrdReadNrrdParse_space_directions: don’t yet have a valid space dimension</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/MichaelChon/Downloads/2dee31ef-f170-4b82-ac12-e58663efae71.nrrd. ITK exception info: error in unknown: Could not create IO object for reading file C:/Users/MichaelChon/Downloads/2dee31ef-f170-4b82-ac12-e58663efae71.nrrd</p>
<p>Tried to create one of the following:</p>
<p>BMPImageIO</p>
<p>BioRadImageIO</p>
<p>DCMTKImageIO</p>
<p>GDCMImageIO</p>
<p>GiplImageIO</p>
<p>JPEGImageIO</p>
<p>LSMImageIO</p>
<p>MGHImageIO</p>
<p>MINCImageIO</p>
<p>MRCImageIO</p>
<p>MetaImageIO</p>
<p>NiftiImageIO</p>
<p>NrrdImageIO</p>
<p>PNGImageIO</p>
<p>ScancoImageIO</p>
<p>StimulateImageIO</p>
<p>TIFFImageIO</p>
<p>VTKImageIO</p>
<p>MRMLIDImageIO</p>
<p>You probably failed to set a file suffix, or</p>
<p>set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile (000001C338AB2030) returned failure for request: vtkInformation (000001C347E2E8B0)</p>
<p>Debug: Off</p>
<p>Modified Time: 218680</p>
<p>Reference Count: 1</p>
<p>Registered Events: (none)</p>
<p>Request: REQUEST_INFORMATION</p>
<p>FORWARD_DIRECTION: 0</p>
<p>ALGORITHM_AFTER_FORWARD: 1</p>
<p>CanReadFile failed: [nrrd] nrrdLoad: trouble reading “C:/Users/MichaelChon/Downloads/2dee31ef-f170-4b82-ac12-e58663efae71.nrrd”</p>
<p>[nrrd] nrrdRead: trouble</p>
<p>[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read: trouble parsing space directions info |(0,0,1) (0,1,0) (1,0,0)|</p>
<p>[nrrd] _nrrdReadNrrdParse_space_directions: don’t yet have a valid space dimension</p>
<p>===== NRRD Header ======</p>
<p>NRRD0005<br>
type: uint8<br>
dimension: 3<br>
sizes: 367 355 764<br>
endian: little<br>
encoding: gzip<br>
space directions: (0,0,1) (0,1,0) (1,0,0)<br>
space origin: (0,0,0)<br>
old min: 0.0<br>
old max: 0.09155961871147156</p>

---

## Post #2 by @lassoan (2025-09-24 02:15 UTC)

<p>It seems that the Lumafield software creates a file that does not follow the NRRD standard. It should be a very easy fix for Lumafield, just report the issue to them. They can ask any questions or help here if something is unclear.</p>

---

## Post #3 by @mchon (2025-09-24 18:53 UTC)

<p>Thanks Andras. I think that helps narrow down the problem.</p>
<p>I read through the NRRD specifications and think I have a hotfix for the time being. Section 4 (Space and Orientation Information) requires either a “space” or “space orientation” field and neither were in the header of the Lumafield NRRD file. I edited the header to include “space: left-anterior-superior” (arbitary) under “dimension” and that was sufficient to load the data!</p>

---

## Post #4 by @mikebind (2025-09-26 16:53 UTC)

<p>Just make sure that the loaded image is correct!  If the space orientation is incorrect the image loaded may be the mirror image of the correct image.  Since people are roughly bilaterally symmetric, it is not necessarily obvious when an image has been mirrored. Check an image with an identifiable feature and ensure that the orientation you chose has not mirrored it.  Other orientation errors may amount to rotations, which are usually obvious and not really a problem, but mirroring can be subtle and possible to miss.</p>

---

## Post #5 by @lassoan (2025-09-26 19:23 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="44566">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Just make sure that the loaded image is correct</p>
</blockquote>
</aside>
<p>Agreed,</p>
<p><a class="mention" href="/u/mchon">@mchon</a> I would recommend to let Lumafield about the problem and your workaround. They should be able to figure out how to fix this in their software and test it. If they have any question they can ask it here.</p>

---

## Post #6 by @mchon (2025-09-30 18:01 UTC)

<p>Thanks. I reached out to Lumafield and they will incorporate a fix in the next update.</p>
<p>In re: symmetry, I did trial the three orientations and compared to the original recon and found one that worked for me. Another approach is to set “space dimension” to 3 and edit the space directions to have the same orientation as the original model.</p>
<p>Thanks all for your input. It was especially helpful to know where to pinpoint the issue.</p>
<p>Michael</p>

---
