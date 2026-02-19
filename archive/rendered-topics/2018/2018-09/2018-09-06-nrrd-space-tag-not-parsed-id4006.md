---
topic_id: 4006
title: "Nrrd Space Tag Not Parsed"
date: 2018-09-06
url: https://discourse.slicer.org/t/4006
---

# NRRD space tag not parsed

**Topic ID**: 4006
**Date**: 2018-09-06
**URL**: https://discourse.slicer.org/t/nrrd-space-tag-not-parsed/4006

---

## Post #1 by @muratmaga (2018-09-06 17:40 UTC)

<p>Is this expected? This is with r27390 on windows 10.</p>
<p>ReadImageInformation: Error reading C:/Users/amaga/Box Sync/PI_Murat/grant_proposals/Nsf_Informatics/data_dropbox/Chris.Percival/dont_work.nhdr:<br>
[nrrd] nrrdLoad: trouble reading “C:/Users/amaga/Box Sync/PI_Murat/grant_proposals/Nsf_Informatics/data_dropbox/Chris.Percival/dont_work.nhdr”<br>
[nrrd] nrrdRead: trouble<br>
[nrrd] _nrrdRead: trouble reading NRRD file<br>
[nrrd] _nrrdFormatNRRD_read: trouble parsing space info |“LPS”|<br>
[nrrd] _nrrdReadNrrdParse_space: couldn’t parse space ““LPS””</p>
<p>This is the header.<br>
NRRD0004<br>
type: short<br>
dimension: 3<br>
sizes: 622 642 1085<br>
byteskip: 3195<br>
data file: ./PERCIVAL_370.AIM<br>
endian: big<br>
encoding: raw<br>
space: “LPS”<br>
space directions: (0.02,0,0) (0,0.02,0) (0,0,0.02)</p>
<p>“LPS” is a valid NRRD tag. If I do something like this, it works fine:</p>
<p>NRRD0004<br>
type: short<br>
dimension: 3<br>
sizes: 622 642 1085<br>
byteskip: 3195<br>
data file: ./PERCIVAL_370.AIM<br>
endian: big<br>
encoding: raw<br>
space dimension: 3<br>
space directions: (-0.02,0,0) (0,-0.02,0) (0,0,0.02)</p>

---

## Post #2 by @lassoan (2018-09-06 18:03 UTC)

<p>Do you actually have LPS in quotation marks: <code>"LPS"</code> instead of <code>LPS</code>?<br>
What software was used to create this file?</p>

---

## Post #3 by @muratmaga (2018-09-06 18:20 UTC)

<p>Yes, LPS was in the quotes. I just used a text-editor (notepad) to generate the header. I removed the quotes and it is working now.</p>

---
