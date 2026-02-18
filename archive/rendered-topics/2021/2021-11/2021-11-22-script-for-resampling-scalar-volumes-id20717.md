# Script for resampling scalar volumes

**Topic ID**: 20717
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/script-for-resampling-scalar-volumes/20717

---

## Post #1 by @nthach17 (2021-11-22 00:01 UTC)

<p>Hello,</p>
<p>I’m new to the developer aspect of 3D Slicer and would like to compile a Python script for resampling batch of scalar volumes. While looking at the documentation for the ResampleVolume module, <a href="https://www.slicer.org/wiki/Modules:ResampleVolume-Documentation-3.6" class="inline-onebox" rel="noopener nofollow ugc">Modules:ResampleVolume-Documentation-3.6 - Slicer Wiki</a>, I noticed that it was written in C++ and its module type is CLI. So my question is: How can I have access to this module from my Python script? Or probably a more suitable question: How should I compile script for CLI modules in general?</p>
<p>Best regards</p>

---

## Post #2 by @Alex_Vergara (2021-11-22 09:52 UTC)

<p>You can do something similar to what I do in my module. See <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/OpenDose3D/Logic/OpenDose3DLogic.py#L571" class="inline-onebox" rel="noopener nofollow ugc">OpenDose3D/Logic/OpenDose3DLogic.py · develop · OpenDose / SlicerOpenDose3D · GitLab</a></p>

---
