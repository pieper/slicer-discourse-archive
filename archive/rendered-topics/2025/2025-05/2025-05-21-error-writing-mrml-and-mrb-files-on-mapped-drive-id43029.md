---
topic_id: 43029
title: "Error Writing Mrml And Mrb Files On Mapped Drive"
date: 2025-05-21
url: https://discourse.slicer.org/t/43029
---

# Error writing MRML and MRB files on mapped drive

**Topic ID**: 43029
**Date**: 2025-05-21
**URL**: https://discourse.slicer.org/t/error-writing-mrml-and-mrb-files-on-mapped-drive/43029

---

## Post #1 by @ezgimercan (2025-05-21 21:44 UTC)

<p>I am using latest stable, 5.8.1 on Ubuntu 22.04. I have some research drives mounted with autofs (nfs). Slicer complains that the locations is not writable when I try to save MRB or MRML files. I can save/write/export everything else successfully.<br>
I assume that the writers for these formats are Slicer specific. Any ideas why they fail where others do not?</p>

---

## Post #2 by @muratmaga (2025-05-22 15:54 UTC)

<p>Not sure why that might be the case, but MRB will require a a subfolder to be created within the location you specified (so that it can zip things). Perhaps you have a strange permission that allows you to write files but not create folders?</p>
<p>In general you should avoid creating MRBs over a network connection since it will be slower. I suggest doing locally at a location like /tmp and then moving to your network location where you will like to share/store long term.</p>

---
