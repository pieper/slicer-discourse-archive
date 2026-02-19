---
topic_id: 28840
title: "Local Dicom Folder Query"
date: 2023-04-11
url: https://discourse.slicer.org/t/28840
---

# Local DICOM folder query

**Topic ID**: 28840
**Date**: 2023-04-11
**URL**: https://discourse.slicer.org/t/local-dicom-folder-query/28840

---

## Post #1 by @docmaniac (2023-04-11 13:55 UTC)

<p>Hi there! Can you tell me if it’s possible to set up the slicer to automatically check a folder for new DICOM files and add them to its database? And, do you know if there are any plugins that can help with this?</p>

---

## Post #2 by @pieper (2023-04-11 14:03 UTC)

<p>If you start the Slicer dicom listener in the dicom module it can receive DIMSE CSTORE from other dicom networking equipment and they will show up in the database directly.  But if the files are coming another way you can use the <code>QFileSystemWatcher</code> to read files as they appear.  Beware that you don’t want to start importing until the file is fully written, and that may be difficult to know for sure.</p>
<p><a href="https://doc.qt.io/qt-5/qfilesystemwatcher.html" class="onebox" target="_blank" rel="noopener">https://doc.qt.io/qt-5/qfilesystemwatcher.html</a></p>

---
