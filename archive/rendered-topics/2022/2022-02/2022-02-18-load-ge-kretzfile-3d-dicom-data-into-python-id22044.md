---
topic_id: 22044
title: "Load Ge Kretzfile 3D Dicom Data Into Python"
date: 2022-02-18
url: https://discourse.slicer.org/t/22044
---

# Load GE Kretzfile 3D Dicom data into python

**Topic ID**: 22044
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/load-ge-kretzfile-3d-dicom-data-into-python/22044

---

## Post #1 by @leopold-franz (2022-02-18 13:52 UTC)

<p>Hello,<br>
Im currently developing an app to access segment 3D ultrasound images from a Voluson E10 device. The images are currently saved as a DICOMDIR that contain Dicom images in the GE Kretzfile format. I managed to successfully open the files using Slicer with the SlicerHeart extension. This then allows me to save the files in a different format (*.nrrd) and then open them in Python.<br>
As I would like my program to work seemlessly without having to open a different UI (the slicer UI) I am wondering if it is possible to open the DICOM kretzfiles and extract the image data and metadata using  your reversed engineered Kretzloader. Can I load a library or copy some of your code to get a python function that takes the (DICOMDIR) folderpath as an input and returns the data and metadata of the kretzfile.<br>
Could you direct me to which function I should use/what parts I should modify?<br>
Best regards,<br>
Leopold</p>

---

## Post #2 by @lassoan (2022-02-18 16:28 UTC)

<p>These examples in the script repository should help:</p>
<ul>
<li>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder">load in image from DICOM</a> (if you know in advance that you will need to load Kretzfile then you can disable all other plugins, making the loading slightly faster)</li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">save image to file</a></li>
</ul>
<p>Note that Slicer has great 3D ultrasound segmentation tools (manual, semi-automatic, automatic, AI-based, etc.), and many other essential features that you would need to implement to get a basic application. Even if in the long term you want to have a custom application that is independent from Slicer, I would strongly recommend to do your prototyping work using the Slicer platform because then all you need is to hide features that you don’t want users to see, which is magnitudes less work than redeveloping everything from scratch.</p>

---
