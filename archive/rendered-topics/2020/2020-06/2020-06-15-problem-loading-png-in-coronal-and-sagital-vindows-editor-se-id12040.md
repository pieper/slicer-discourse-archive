# Problem loading png. in coronal and sagital vindows + Editor segmentation diabeled 

**Topic ID**: 12040
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/problem-loading-png-in-coronal-and-sagital-vindows-editor-segmentation-diabeled/12040

---

## Post #1 by @hpok (2020-06-15 17:57 UTC)

<p>Hello,</p>
<p>I have encountered a few problems when loading png data and subsequently segmenting them.<br>
I aim to segment a hippocampus from a set of png. images. When I load it into Slicer, the axial view port is all right but the sagital and coronal views are squished. I thought I need to adjust the z- distance, however that made no change. I therefore decided to only use the axial view to draw on in Editor using paint effect tool), however I cannot chose Input data and the Editor options are grayed out.<br>
I am attaching screenshots of both issues.</p>
<p>Has anyone encountered similar problems and knows how to solve them?</p>
<p>Thank you!![squished_coronal and saggital view.PNG|690x475]<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb3f75c7ae42436f093e3ab873b3ea2be215d71d.png" alt="Grey_editor" data-base62-sha1="t00T7FoTykHHeVqoLNcSLNlwsnH" width="498" height="301"></p>

---

## Post #2 by @pieper (2020-06-15 19:32 UTC)

<p>Hi -</p>
<p>You can adjust the image spacing in the Volumes Module and then convert with the Vector to Scalar Volume module to get a single (not RGB) volume for use with the Editor.  If you use those keywords as search terms you’ll find a lot more discussion about this (including discussions of why png is not a good format for medical imaging).</p>

---
