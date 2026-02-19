---
topic_id: 35104
title: "Unable To Open Dicom Data"
date: 2024-03-26
url: https://discourse.slicer.org/t/35104
---

# unable to open Dicom data

**Topic ID**: 35104
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/unable-to-open-dicom-data/35104

---

## Post #1 by @DR.DHARAM_SINGH_RATH (2024-03-26 15:20 UTC)

<p>unable to open this type of file ( CT.1.2.840.113704.7.1.1.5160.1421080164.595.dcm) downloaded from the open source database. while uploading msg is popping up –</p>
<p>The following data type is in your database: Structured Report Objects.</p>
<p>The following extension is not installed, but may help you work with this data: QuantitativeReporting.</p>
<p>You can install extensions using the Extensions Manager option from the View menu.</p>
<p>any solution please help.</p>

---

## Post #2 by @pieper (2024-03-26 15:27 UTC)

<p>Structured Reports in DICOM are a complex topic - they may contain text descriptions or measurements or other things (just do a search for the topic).  Installing the Quantitative Reporting extension, as the message suggests, will allow some types of reports to be loaded but generally you need to be very aware of the details to make use of them.</p>

---
