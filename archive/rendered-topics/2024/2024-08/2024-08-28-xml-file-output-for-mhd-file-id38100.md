# .xml file output for .mhd file

**Topic ID**: 38100
**Date**: 2024-08-28
**URL**: https://discourse.slicer.org/t/xml-file-output-for-mhd-file/38100

---

## Post #1 by @QianyuXie_Julie (2024-08-28 20:42 UTC)

<p>Hi everyone,</p>
<p>I’m working on a Unity project and I need a related <code>.mhd</code> file along with an <code>.xml</code> file. However, when I export the <code>.mhd</code> image from Slicer3D, I only get the <code>.mhd</code> and <code>.raw</code> files.</p>
<p>Does anyone know how I can generate the <code>.xml</code> file that I need? Should this file be generated from the <code>.raw</code> file, or is there another way to create it from the data exported by Slicer3D?</p>
<p>Thanks in advance for your help!</p>

---

## Post #2 by @lassoan (2024-08-28 20:49 UTC)

<p>An image is stored in a single .mha file; or in an .mhd and a .raw file.</p>
<p>There should be no need for any .xml file, because all metadata, including any custom metadata can be stored in the .mha or .mhd file itself.  Maybe you worked with NIFTI file format before, which is so limited that it requries an xml sidecar to store custom metadata.</p>

---

## Post #3 by @QianyuXie_Julie (2024-08-29 21:04 UTC)

<p>Thank you for your response! I actually managed to solve the issue—I found the .xml file I needed, and it turns out it’s a configuration file specific to my project. Your explanation about the .mhd and .mha files was really helpful, though, and I appreciate you taking the time to clarify that!</p>

---
