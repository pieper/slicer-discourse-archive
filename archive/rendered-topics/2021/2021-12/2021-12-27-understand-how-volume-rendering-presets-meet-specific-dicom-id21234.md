# Understand how volume rendering presets meet specific dicom viewer usage

**Topic ID**: 21234
**Date**: 2021-12-27
**URL**: https://discourse.slicer.org/t/understand-how-volume-rendering-presets-meet-specific-dicom-viewer-usage/21234

---

## Post #1 by @rambery (2021-12-27 11:47 UTC)

<p>Hi. I’m currently working on a medical web application using OHIF - vtkjs stack and trying to understand the volume rendering part here. The default presets from open source that I could find is pretty much the same with: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/Resources/presets.xml" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/VolumeRendering/Resources/presets.xml</a>. To further tailor my volume rendering feature, I want to understand how each property in these presets contribute to the rendering pipeline, and how it tailor to medical usage. For example, how the attributes of CT-Chest-Vessels preset relates to the specific viewing of chest vessels, and so on (this requires some domain knowledge I suppose). So I’ll be very glad if someone can give me a lead onto this domain of technical - medical expertise. A general explanation, published papers (if comprehensible for outsiders like me), a medical-imaging-for-dummy articles, (or anything related really), would be really helpful.<br>
Thanks in advance !</p>

---

## Post #2 by @pieper (2021-12-29 00:01 UTC)

<p>Will your OHIF based volume rendering be open source?  If so, it would be great if you could start by writing documentation of what you have so far, how it relates to techniques used in Slicer.  A lot of work has been going on in the OHIF and VTKjs teams to build up the infrastructure so if your work builds on and contributes back to those efforts then I’m sure people here will be glad to help.</p>

---
