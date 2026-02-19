---
topic_id: 28560
title: "Couldnt Register Customized Displayablemanager To Extension"
date: 2023-03-24
url: https://discourse.slicer.org/t/28560
---

# Couldn't Register customized DisplayableManager to extension module

**Topic ID**: 28560
**Date**: 2023-03-24
**URL**: https://discourse.slicer.org/t/couldnt-register-customized-displayablemanager-to-extension-module/28560

---

## Post #1 by @RuoyanMeng (2023-03-24 17:20 UTC)

<p>Hi, I tried to customize a slice DisplayableManager and register it to vtkMRMLSliceViewDisplayableManagerFactory. But after successfully compiling our extension, When starting the 3D slicer, it will report  <em><strong>“/Slicer/Slicer-SuperBuild-Debug/VTK/Common/Core/vtkDebugLeaks.cxx, line 272, Deleting unknown object: vtkMRMLLiverResectionsDisplayableManager”</strong></em><br>
And the following error is <em><strong>“/Slicer/Libs/MRML/DisplayableManager/vtkMRMLDisplayableManagerFactory.cxx, line 136, vtkMRMLSliceViewDisplayableManagerFactory (0x555584f96130): RegisterDisplayableManager - vtkMRMLLiverResectionsDisplayableManager is not a displayable manager. Failed to register”</strong></em></p>
<p>For creating customized DisplayableManager I referenced slicer markups’ <a href="https://github.com/Slicer/Slicer/tree/fbc2ede79060e2e2c653ddb2f0b7d2bba9fab16b/Modules/Loadable/Markups/MRMLDM" rel="noopener nofollow ugc">MRMLDM</a></p>
<p>Could you share your thoughts on possible reasons lead this error? Thank you so much.</p>

---

## Post #2 by @lassoan (2023-03-26 04:32 UTC)

<p>If you want to create custom markups then you don’t need to implement a custom displayable manager. See complete example <a href="https://github.com/chir-set/SlicerExtraMarkups">in ExtraMarkups extension</a>.</p>
<p>Also check out the Liver extension’s <a href="https://github.com/ALive-research/Slicer-Liver">advanced liver resection planning and visualization tools</a> already exist in Slicer. Maybe it is a better starting point.</p>

---

## Post #3 by @Mik (2023-03-27 09:39 UTC)

<p>Did you <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Colors/qSlicerColorsModule.cxx#L51-L53" rel="noopener nofollow ugc">initiate</a> and <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Colors/qSlicerColorsModule.cxx#L98-L102" rel="noopener nofollow ugc">register</a> your displayable manager in a module source file?</p>

---

## Post #4 by @RuoyanMeng (2023-03-27 09:40 UTC)

<p>Hi, Thank you for your input! Actually, I am one of the Slicer-Liver extension developers, I would like to add a new feature for visualizing the cutting lines between the resection surface and 3D Slicer slice views. I thought it might be easier to do it within DisplayableManager.</p>

---

## Post #5 by @RuoyanMeng (2023-03-27 09:47 UTC)

<p>Thank you so much for pointing this out, I did ignore the initiating process! Now everything works fine!</p>

---
