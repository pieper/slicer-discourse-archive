# Philips EPIQ 7 vol files to dicom or tiff files

**Topic ID**: 9602
**Date**: 2019-12-24
**URL**: https://discourse.slicer.org/t/philips-epiq-7-vol-files-to-dicom-or-tiff-files/9602

---

## Post #1 by @deepz (2019-12-24 07:16 UTC)

<p>Hello Everyone,<br>
I am trying to convert 3d/4d volume files of cardiac slices( from philips epiq7) to dicom or tiff files. In the converter option , the format is not recognized itself. Kindly share your input.</p>

---

## Post #2 by @lassoan (2019-12-24 14:02 UTC)

<p>What converter option you are referring to? How do you plan to use a 4D volume in tiff format?</p>

---

## Post #3 by @deepz (2019-12-30 06:26 UTC)

<p>Hello,<br>
The <strong>Create DICOM Series</strong> option found in Converters/Slicer3D.</p>
<p>The idea is to use the obtained tiff files and convert them to a Unity Asset file. Normally 3D .vol files are visualized using existing Unity Pluginslike that.</p>
<p>Initially, the idea is to create a DICOM Series from the .vol format obtained from Philips epiq 7. But the format is not even recognized in the Converters option. Would it be recognized if the same files are exported in a format called “Cartesian DICOM format” from QLab (Philips software) ?.</p>
<p>Kindly share any documentation related to visualization and conversion 4D .vol files obtained from the Philips machine.</p>

---

## Post #4 by @lassoan (2019-12-30 15:11 UTC)

<p>You can use SlicerHeart extension to load 4D volumes from Philips ultrasound systems. See <a href="https://github.com/SlicerHeart/SlicerHeart#import-philips-4d-cardiac-images">detailed instructions here</a>.</p>
<p>For your information, Slicer can directly display 4D ultrasound using volume rendering and surface rendering in all OpenVR-compatible VR and AR headsets directly, without all the limitations of Unity. So, if the motivation for Unity is AR/VR then I would recommend to use Slicer instead.</p>
<p>For deployment non-OpenVR-compatible headsets, Unity is still a valid option. We already have Slicer-Unity bridge (via OpenIGTLink) and we are going to review and improve it during the <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/">next project week in Spain in January 20-24</a>. You would be very welcome to join us.</p>

---
