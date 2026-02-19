---
topic_id: 8805
title: "Calling Aetitle And Storage Aetitle"
date: 2019-10-16
url: https://discourse.slicer.org/t/8805
---

# Calling AETITLE and storage AETITLE

**Topic ID**: 8805
**Date**: 2019-10-16
**URL**: https://discourse.slicer.org/t/calling-aetitle-and-storage-aetitle/8805

---

## Post #1 by @NormandRobert (2019-10-16 21:16 UTC)

<p>Operating system: All<br>
Slicer version: All<br>
Can someone clarify why some medical image viewers make a distinction between a calling AETITLE and a storage AETITLE?  I never really understood why. Is it to send back images on a different port than is used to query?</p>

---

## Post #2 by @lassoan (2019-10-17 03:09 UTC)

<p>The reason is that the protocol is defined like this in the DICOM standard. Maybe they added this string because usually DICOM services do not use any other kind of user identification.</p>

---

## Post #3 by @pieper (2019-10-17 20:12 UTC)

<p>I try not to remember the details of DIMSE (too much DIMSE can lead to mental health issues), but I’ve always understood the idea to be that both ends, the provider and the user, can be configured to restrict which AETITLEs they will talk to.  This becomes a kind of minimal form of security.  DICOMweb is much more logical in the sense that you can put it inside standard web security frameworks.</p>

---
