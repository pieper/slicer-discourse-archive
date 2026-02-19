---
topic_id: 3890
title: "Errors Reading Dicom Files From Cirrus Hd Oct"
date: 2018-08-24
url: https://discourse.slicer.org/t/3890
---

# Errors reading Dicom files from CIRRUS HD-OCT

**Topic ID**: 3890
**Date**: 2018-08-24
**URL**: https://discourse.slicer.org/t/errors-reading-dicom-files-from-cirrus-hd-oct/3890

---

## Post #1 by @Ekisolid (2018-08-24 18:26 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.8.1<br>
Expected behavior:loading Dicom files from CIRRUS HD-OCT<br>
Actual behavior: errors in loading process.</p>

---

## Post #2 by @pieper (2018-08-24 21:32 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #3 by @Ekisolid (2018-08-27 10:30 UTC)

<p>Hi,</p>
<p>I’ve patched my DICOM folder with the DICOM patcher and there are some issues in the proces:</p>
<p>DICOM patching started…</p>
<p>Examining .\ZDBDIR2.ibk…</p>
<p>Not DICOM file. Skipped.</p>
<p>Examining .\ZDBDIR2.ib…</p>
<p>Not DICOM file. Skipped.</p>
<p>Examining .\Export2.xml…</p>
<p>Not DICOM file. Skipped.</p>
<p>Examining .\Data64To32Convertor.cmd…</p>
<p>Not DICOM file. Skipped.</p>
<p>Examining DataFiles\E773\5MT7JPM9KQ72AUMGN5LV92BV9NL92IDFS27IOLS4X2ZU.EX.DCM…</p>
<p>Patching…</p>
<p>Writing DICOM…</p>
<p>Unexpected error: Invalid tag (0018, 0088): invalid literal for float(): 0.04724409</p>
<p>Any suggestion?</p>

---

## Post #4 by @lassoan (2018-08-27 11:53 UTC)

<p>Maybe there are space characters before or after the number. That would violate the DICOM standard.</p>

---

## Post #5 by @Mihail_Isakov (2018-08-28 07:21 UTC)

<p>Hi,<br>
BTW, leading or trailing space characters for VR DS don’t violate DICOM standard, it is DICOM standard. And DS is VR of 0018,0088.</p>
<p><a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html" class="onebox" target="_blank" rel="nofollow noopener">http://dicom.nema.org/medical/dicom/current/output/chtml/part05/sect_6.2.html</a><br>
Table 6.2-1. DICOM Value Representations</p>

---

## Post #6 by @lassoan (2018-08-28 13:35 UTC)

<p>Yes, you are right, leading and trailing spaces are allowed. Can you check what exactly do you have in those fields? Probably there are some other non-printing characters that violate the standard - newline, 0x00, …?</p>
<p>It is somewhat odd that these field is found in an OCT image, as this field is <a href="http://dicomlookup.com/lookup.asp?sw=Tnumber&amp;q=(0018,0088)">only referenced in MR IODs</a>. I also had a look at a couple of <a href="https://www.zeiss.com/meditec/int/products/conformance-interoperability/dicom-conformance.html?catalog=dicom-cirrus-hd-oct">DICOM conformance statements of CIRRUS HD OCTs</a> and this field was not listed. Have you added this field manually or modified (anonymized, converted, etc.) these files in any way?</p>

---

## Post #8 by @lassoan (2018-08-28 22:12 UTC)

<p><a class="mention" href="/u/ekisolid">@Ekisolid</a> We would either need a dump of all fields (you can use dcmdump command-line tool or “Metadata” feature of Slicer’s DICOM browser) or a sample data set for further investigation.</p>

---
