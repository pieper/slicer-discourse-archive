# can't import volume from dicom files from philips HD11 ultrasound 

**Topic ID**: 2135
**Date**: 2018-02-21
**URL**: https://discourse.slicer.org/t/cant-import-volume-from-dicom-files-from-philips-hd11-ultrasound/2135

---

## Post #1 by @Rafael_Bezerra_Dalla (2018-02-21 01:30 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.9<br>
Expected behavior:<br>
Actual behavior: when importing volume data from the philips HD11 it loads all 3 perspectives into a single window, the red one , and when I select the volume and click to show Slicer crashes.<br>
When I open files from Philips Affiniti 50G it works great.<br>
I’m trying to 3d print baby faces from 4D ultrasound.</p>

---

## Post #2 by @lassoan (2018-02-21 04:30 UTC)

<p>Based on what you described, it seems that 3D image data is stored in private fields and what Slicer can see in standard DICOM fields is just secondary capture. If you can load your data set to Philips QLab and export it as a Cartesian image then Slicer can load it using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerHeart">SlicerHeart extension</a>.</p>

---

## Post #3 by @Rafael_Bezerra_Dalla (2018-02-22 02:19 UTC)

<p>I downloaded qlab from this link - <a href="http://www.crf.org/files/meetings/echo/2017/QLAB%2010.7%20Link_%20Instructions_%20Help%20Desk%20-%20ECHO%202017%20UPDATED.pdf" rel="nofollow noopener">http://www.crf.org/files/meetings/echo/2017/QLAB%2010.7%20Link_%20Instructions_%20Help%20Desk%20-%20ECHO%202017%20UPDATED.pdf</a> -<br>
and I can’t see the 3d image, just the static image although the file is larger the the standard jpg.<br>
could you try to transform it to open in slicer that tell me the steps to do it?<br>
I’ll upload the file to dropbox<br>
<a href="https://www.dropbox.com/s/0tp0byc71aubixq/GEISSY0Q?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/0tp0byc71aubixq/GEISSY0Q?dl=0</a><br>
thanks</p>

---

## Post #4 by @GLORIA_MAGA (2021-10-02 06:09 UTC)

<p>Hi Rafael, I´m trying print 3D ultrasound from the Philips Affiniti 50, could you tell me which file type need, File that is generated saving MPR? or volume?, I open this files on slicer but baby doesnt see. Pleasse helpme</p>

---
