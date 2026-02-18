# Patient Identifiers in Scans

**Topic ID**: 14716
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/patient-identifiers-in-scans/14716

---

## Post #1 by @atbeksac (2020-11-20 19:21 UTC)

<p>Hello,</p>
<p>I want  to  use  slicer to extract radiomic data from CT scans. Unfortunately I wasn’t able to get deidentified images. My  question is whether it is safe to use images with patient identifiers. I want to do my research the right way and I don’t want to jeopardize any identified patient data.</p>
<p>Thanks</p>

---

## Post #2 by @manjula (2020-11-20 21:01 UTC)

<p>Hi,</p>
<p>I think for most practical purposes you can save the data in nrrd format which will remove the patient information from the standard tags.</p>
<p>But I think I have people really going the extra mile and describing things like changing image origins and axes like that. And i understand it to be a very complex topic.</p>

---

## Post #3 by @pieper (2020-11-20 22:05 UTC)

<p>Most institutions will have guidelines about what is considered safe practices for using identified data for research.  Saving to nrrd without using real names or ids as filenames is a common practice for de-identifying and will work fine for radiomics research.  There are probably still institutional rules you will need to follow to safeguard the data even if it’s been de-identified in this way.</p>

---
