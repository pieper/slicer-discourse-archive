# DICOM network retrieval from PACS - automated approach possible?

**Topic ID**: 4780
**Date**: 2018-11-17
**URL**: https://discourse.slicer.org/t/dicom-network-retrieval-from-pacs-automated-approach-possible/4780

---

## Post #1 by @Sandor_Konya (2018-11-17 11:20 UTC)

<p>Hi there,</p>
<p>i’ve managed to set up a PACS server connection in Slicer, image retrieval is w/o problem, listener listens and gets/stores images, they show up in local DICOM storage. So far so good, but i would like to “download” a series of thousands of images (i have patient IDs/ image IDs  in  .CSV file)</p>
<p>A, Is it possible to script the data retrieval with Python, so that i can retrieve without manually entering any data on the DICOM Query dialog interface (<a href="https://www.slicer.org/wiki/File:Form_224.png" rel="noopener nofollow ugc">this</a>)</p>
<p>B, if not, is it possible to add more options to the DICOM Query dialog interface (like more modalities DX,EC etc. is missing)</p>
<p>EDIT:<br>
i found <a href="https://discourse.slicer.org/t/dicom-pacs-does-retrieve-but-series-do-not-show-in-browser/2012/2">this post</a>, based on it, what i need is to call external commands… do i?</p>
<p>thank you in advance,<br>
regards<br>
Sandor</p>

---

## Post #2 by @pieper (2018-11-17 13:31 UTC)

<p>Hi Sandor -</p>
<p>It’s great that this is working via the GUI.  For scripting, it’s probably easiest to just use the <a href="https://dicom.offis.de/dcmtk.php.en">dcmtk command line utilities</a> directly. If you look in the slicer log you will see the command line options used for <code>storescp</code> that runs the listener.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @Sandor_Konya (2018-11-18 18:00 UTC)

<p>Hi Steve,</p>
<p>thank you for the tip, i managed to retrieve the pictures with dcmtk command line utilities (after realizing that the findscu and echoscu executables are not in the Slicer3D install).</p>
<p>In the meanwhile i explored the source code of Slicer3D and i’ll post another, but dev. question you definitely are able to help with.</p>
<p>thank you,<br>
Sandor</p>

---
