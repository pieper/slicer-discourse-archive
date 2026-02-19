---
topic_id: 45079
title: "How To Detect Mri File Being Loaded"
date: 2025-11-14
url: https://discourse.slicer.org/t/45079
---

# How to detect MRI file being loaded?

**Topic ID**: 45079
**Date**: 2025-11-14
**URL**: https://discourse.slicer.org/t/how-to-detect-mri-file-being-loaded/45079

---

## Post #1 by @Victor_Wayne (2025-11-14 10:31 UTC)

<p>Hello,</p>
<p>I need to log the header of the MRI file. How can I detect if an MRI file is loaded in slicer?</p>
<p>Thanks for your help.</p>

---

## Post #2 by @ebrahim (2025-11-14 16:34 UTC)

<p>If you need to do something whenever a node is added, you can listen for the <code>slicer.vtkMRMLScene.NodeAddedEvent</code>. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded" rel="noopener nofollow ugc">Example</a></p>
<p>What kind of information is in the header depends on the file format, so you would need to figure out how your file format indicates whether the modality is MRI. Not all formats indicate this information in any standard way.</p>

---

## Post #3 by @cpinter (2025-11-17 10:27 UTC)

<p>It is also possible to add a callback for DICOM image having been loaded. Let me know if that’s what you want instead.</p>

---

## Post #4 by @Victor_Wayne (2025-11-18 04:31 UTC)

<p>The user will be working only with .nii files. (Most of the times atleast)</p>

---

## Post #5 by @Victor_Wayne (2025-11-18 04:33 UTC)

<p>Can you please elaborate on that?</p>

---

## Post #6 by @cpinter (2025-11-18 11:30 UTC)

<p>You can add this in <code>.slicerrc.py</code> or if you have a custom module then to its initialization:</p>
<pre><code class="lang-auto">    dicomWidget = slicer.modules.dicom.widgetRepresentation()
    dicomWidgetSelf = dicomWidget.self()
    # Override onLoadingFinished to use customized function
    dicomWidgetSelf.browserWidget.onLoadingFinished = self.onDicomLoadingFinished
</code></pre>
<p>Then you can implement <code>onDicomLoadingFinished</code> as you desire. You can check the modality of the DICOM, and it it’s an MRI, then you can do what you need with that (you provided very little information on what you want to do).</p>

---

## Post #7 by @Victor_Wayne (2025-11-21 05:21 UTC)

<p>Thanks for your help.<br>
I have only one more question.<br>
Is there any way to find out if the vtkMRMLScalarVolumeNode came from a nifty file or a dicom file?</p>

---

## Post #8 by @cpinter (2025-11-21 09:33 UTC)

<p>Yes. If loaded from DICOM, the volume node and its subject hierarchy item has all kinds of attributes</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb5a4ad4caa373699c50f0ff93c8ac2002682e57.png" data-download-href="/uploads/short-url/xA1EFpZutd80ApMdt9DC00ITcph.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb5a4ad4caa373699c50f0ff93c8ac2002682e57.png" alt="image" data-base62-sha1="xA1EFpZutd80ApMdt9DC00ITcph" width="373" height="500" data-dominant-color="ECEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">561×752 22.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If loaded from file, the volume node’s storage node has the file name.</p>

---

## Post #9 by @Victor_Wayne (2025-11-21 09:40 UTC)

<p>Thank you so much for your help.</p>

---
