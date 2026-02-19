---
topic_id: 28598
title: "Hanging Protocol For Displaying Pet Ct Images"
date: 2023-03-27
url: https://discourse.slicer.org/t/28598
---

# Hanging protocol for displaying PET/CT images

**Topic ID**: 28598
**Date**: 2023-03-27
**URL**: https://discourse.slicer.org/t/hanging-protocol-for-displaying-pet-ct-images/28598

---

## Post #1 by @nick.reynders (2023-03-27 12:46 UTC)

<p>Is is possible to add on a feature that saves a user’s preferred modality-specific viewing settings.  I view PET/CT images regularly and it would be great to be able to have my view settings saved so I’m always viewing PET with PET-Heat in 0-20SUV, then CT in CT Abdomen Window without having to adjust this every single time I load a new case.  Having custom view settings for a given user where it loads up the same way each time would be great!</p>

---

## Post #2 by @lassoan (2023-03-27 15:09 UTC)

<p>Thanks for the suggestion. A task-specific view setup, so called “hanging protocol” is indeed a useful feature. In Slicer, currently hanging protocols must be specified in Python.</p>
<p>For example, if you copy-paste <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#activate-hanging-protocol-by-keyboard-shortcut">this code snippet</a> into the Pyhon console or into the Slicer startup file (.slicerrc.py) then a PET/CT hanging protocol can be applied by using the Ctrl+9 keyboard shortcut.</p>
<p>Defining hanging protocol in a Python script has the advantage that it is possible to set very sophisticated image display set selection criteria, visualization options, even any kind of pre-processing, registration, etc.</p>
<p>However, <strong>it is not easy to create hanging protocols and distribute them to users</strong>. <strong>It would be also nice to be able to load/save hanging protocols from/to DICOM</strong> (see <a href="https://dicom.innolitics.com/ciods/hanging-protocol">IOD</a> and some <a href="https://dicom.nema.org/dicom/Conf-2005/Day-2_Selected_Papers/B305_Morgan_HangProto_v1.pdf">slides</a>) or some JSON description (see for example <a href="https://v3-docs.ohif.org/platform/extensions/modules/hpModule">OHIF</a>).</p>

---
