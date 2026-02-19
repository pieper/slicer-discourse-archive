---
topic_id: 31074
title: "Save Nrrd Files To Portable Drive"
date: 2023-08-09
url: https://discourse.slicer.org/t/31074
---

# Save nrrd files to portable drive

**Topic ID**: 31074
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/save-nrrd-files-to-portable-drive/31074

---

## Post #1 by @Robert_Spaans (2023-08-09 17:47 UTC)

<p>I work on a macbook and want to save my data on a samsung T7 portable drive.<br>
I can load all datatypes and save all datatypes except nrrd files. (which I can load, but not save)<br>
I am able to save everything directly on the internal storage and on a windows machine I am able to save all the files correctly on the drive. So only when I want to save an nrrd file on a macbook to the portable drive, I get an error.</p>
<p>error message: " Error renaming file to PATH/._5 Thorax Insp 2.0 B70f.nrrd,renameReturn = -1"<br>
Error message: “Cannot write data file: PATH/ 5 Thorax Insp 2.0 B70f.nrrd.”</p>
<p>Does anyone know what causes this and how I can resolve it?</p>

---

## Post #2 by @Robert_Spaans (2023-08-09 18:12 UTC)

<p>Also tried it with the CT chest sample data, but I get the same errors.</p>

---

## Post #3 by @lassoan (2023-08-09 19:31 UTC)

<p>You need to remove the space character from the beginning of the filename. To avoid this problem in the future, remove the space from the beginning of the volume node name. The space character may come from the series description or you might have left it there when you edited the node name.</p>

---

## Post #4 by @Robert_Spaans (2023-08-09 19:36 UTC)

<p>Thanks,</p>
<p>But in there is no space at the beginning of the volume node name in the data tree.<br>
I think it is because the portable hard drive has an ExFAT file system which creates extended attributes starting with “._” which causes the problem. As far as I know, In the APFS file system, these extende attributes are saved differently.</p>
<p>I reformatted the drive to a MacOS extended filesystem which solved the error, but leaves me unable to use the drive with a Windows Machine.</p>
<p>Do you know if it could be that 3DSlicer does not support files with “._” before the filename?</p>

---
