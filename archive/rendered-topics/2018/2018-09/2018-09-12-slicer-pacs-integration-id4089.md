---
topic_id: 4089
title: "Slicer Pacs Integration"
date: 2018-09-12
url: https://discourse.slicer.org/t/4089
---

# Slicer PACS integration

**Topic ID**: 4089
**Date**: 2018-09-12
**URL**: https://discourse.slicer.org/t/slicer-pacs-integration/4089

---

## Post #1 by @muratmaga (2018-09-12 18:13 UTC)

<p>We are looking into how feasible it is to pull patients from the clinical PACS system into Slicer for research purposes. Do we use DICOM browser for this, is it as simple as putting in the IP address of the server into the browser?</p>
<p>I appreciate any feedback, documentation as I will pass this to our radiology system admins for them to evaluate.</p>

---

## Post #2 by @pieper (2018-09-13 16:54 UTC)

<p>Hi Murat -</p>
<p>DICOM networking (technically DIMSE) is supported by Slicer for query and retrieve using CGET or CFIND/CMOVE if you set up the IP address, port, and AETITLE correctly on both the Slicer and PACS side.  This usually means to you need to get the blessing and help of the radiology network administrators, and access policies vary from site to site.  Some people may be reluctant to allow research software on their network or they worry about bogging down the network or servers.</p>
<p>I typically suggest debugging first with dcmtk command line tools and then just copying the settings into Slicer and everything should just work because we use dcmtk under the hood.</p>
<p>Sending to PACS (CSTORE) is not enabled in Slicer in part because most sites prohibit research data in the clinical pacs.  For people who need to push it’s a single command line (storescu in dcmtk).  It sounds like you don’t need that.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @muratmaga (2018-09-13 17:30 UTC)

<p>Thanks Steve. That’s all I needed.</p>

---

## Post #4 by @timeanddoctor (2018-09-13 23:55 UTC)

<p>If you have done it successfully, can you share it here?</p>

---

## Post #5 by @Robert_Leo (2019-08-23 13:20 UTC)

<p>So, is it complete now? If yes, then please send it here…I’m still confused about it.</p>

---

## Post #6 by @pieper (2019-08-23 13:37 UTC)

<p>Slicer works as described above.  DICOM networking is a complex topic, but well described (for example <a href="https://www.amazon.com/Digital-Imaging-Communications-Medicine-DICOM/dp/3642108490" rel="nofollow noopener">in this book</a>).  Once you know the concepts they can be applied in the slicer environment.</p>

---

## Post #7 by @muratmaga (2019-08-23 18:21 UTC)

<p><a class="mention" href="/u/robert_leo">@Robert_Leo</a> <a class="mention" href="/u/timeanddoctor">@timeanddoctor</a></p>
<p>Just to clarify, we needed those information to check with our clinical radiology IT department. In the end, we couldn’t do it due to audit trail requirements and a lot of compliance issues. For us, it is logistically easier to get clinical imaging core extract the data in bulk after IRB approval, and we take it from there.</p>

---
