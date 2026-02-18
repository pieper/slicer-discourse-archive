# Checksum for retrieved DICOM

**Topic ID**: 13922
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/checksum-for-retrieved-dicom/13922

---

## Post #1 by @xriobe (2020-10-07 14:45 UTC)

<p>Hi,</p>
<p>we are using the DICOM browser module in our application, and i am looking for a way to check the integrity of the data retrieved from a PACS.<br>
Does anybody know if there is an available mechanism to do that (in Slicer or with DICOM management in general), like a checksum to verify that there has been no alteration of the files?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-10-07 14:46 UTC)

<p>It would be a good idea, but I’m not aware of anything like that.  One alternative could be to retrieve twice and compare the results.</p>

---

## Post #3 by @lassoan (2020-10-07 15:15 UTC)

<p>In general, it is not possible to compute checksum for a DICOM data set before/after network transfer, as the sender and receiver may use different file format, SOP class, encoding, endianness, value representation, etc. or may not even store data in DICOM files at all. The server may dynamically transform data before sending it, depending on results of the association negotiation with the client.</p>
<p>However, I don’t hear people complaining about DICOM data getting corrupted during network transfer, so I assume there are checks built into the protocol to preserve data integrity.</p>
<p>It may be possible that not all instances are transferred successfully (e.g., due to network disconnect). There are higher-level DICOM mechanisms for detecting this, such as “storage commitment” service.</p>
<p>Currently, Slicer can act as C-Store SCP&amp;SCU and Query/Retrieve SCU, and it does not support storage commitment. Since DICOM DIMSE services do not work well with modern web services, we do not plan to invest much time into improving them, but we plan to greatly improve DICOMweb support in Slicer in the future.</p>

---

## Post #4 by @xriobe (2020-10-07 15:15 UTC)

<p>If the data was small it could have been a solution, but retrieving some volumes once is already too long…</p>
<p>I found that the DICOM standard provides Digital Signatures (supported by dcmtk) that can be used for that, but apparently the vendors don’t implement it, so not really usefull for now.</p>

---

## Post #5 by @xriobe (2020-10-07 15:22 UTC)

<p>Ok… Thanks both of you for the quick answers anyway !</p>

---
