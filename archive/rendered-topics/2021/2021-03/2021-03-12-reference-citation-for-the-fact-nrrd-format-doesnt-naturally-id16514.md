---
topic_id: 16514
title: "Reference Citation For The Fact Nrrd Format Doesnt Naturally"
date: 2021-03-12
url: https://discourse.slicer.org/t/16514
---

# Reference/citation for the fact NRRD format doesn't naturally hold patient data

**Topic ID**: 16514
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/reference-citation-for-the-fact-nrrd-format-doesnt-naturally-hold-patient-data/16514

---

## Post #1 by @John_Moore (2021-03-12 22:15 UTC)

<p>Are there any papers or web pages that explicitly state the NRRD file format does not contain any (textual) patient identifiers?  I’d like to include this in an ethics application.</p>

---

## Post #2 by @lassoan (2021-03-13 14:05 UTC)

<p>The file format can store arbitrary custom fields, so it is possible to store patient health information in nrrd files. However, we can show that a particular export or conversion workflow strips all patient data. What is your processing workflow, what modules and features do you use for creating the nrrd?</p>
<p>Alternatively, you might add a step to your workflow that the data processing person opens the nrrd file and checks the file header with a text file viewer, as all custom fields are listed in the beginning of the file.</p>

---

## Post #3 by @John_Moore (2021-03-15 14:05 UTC)

<p>We are using Philips TEE systems, so the workflow is:</p>
<p>from QLab, export to Cartesian DICOM<br>
in Slicer, open as 4D sequence<br>
save image data as a NRRD file, using filename with no correlation to patient information</p>
<p>For our REB application, I would like to include a reference/citation to indicate the file format, in its default form, does not keep any patient identifiers beyond the image data itself. Even a wiki page reference would suffice.</p>
<p>thanks</p>

---

## Post #4 by @muratmaga (2021-03-15 15:10 UTC)

<p>If you import your DICOM data, and save it as NRRD using Slicer (or DCM2NIIX), patient information will not be saved into NRRD. But as <a class="mention" href="/u/lassoan">@lassoan</a> explained above, NRRD keeps a text header, and by mistake (or veyr unlikely with malicious intent) people can include any arbitrary information in the header. As such I don’t think you can find a reference for what you want to include.</p>
<p>If this is IRB and particularly challenging, you can say something like “prior to conversion of data, a fake dataset with PHI fields will be converted to NRRD using the proposed pipeline, and an independent observer will review the contents of the NRRD after the conversion” (or something that is better worded).</p>

---
