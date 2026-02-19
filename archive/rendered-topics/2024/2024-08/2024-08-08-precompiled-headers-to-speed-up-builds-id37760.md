---
topic_id: 37760
title: "Precompiled Headers To Speed Up Builds"
date: 2024-08-08
url: https://discourse.slicer.org/t/37760
---

# Precompiled headers to speed up builds

**Topic ID**: 37760
**Date**: 2024-08-08
**URL**: https://discourse.slicer.org/t/precompiled-headers-to-speed-up-builds/37760

---

## Post #1 by @aymeric.chataigner (2024-08-08 07:03 UTC)

<p>Hi,</p>
<p>I would like to precompile Qt, Vtk and Itk headers to speed up the build in the Slicer-build directory.</p>
<p>I created some empty libraries in Libs directory to precompile the most common headers (QString, QObject, VtkObject.h…)<br>
PrecompileItkHeaders<br>
PrecompileVtkHeaders<br>
PrecompileQtCoreHeaders<br>
PrecompileQtWidgetsHeaders</p>
<p>I tried to add some target_precompile_headers cmake commands in slicer CMakeLists.txt but most of the time it does not work: this gcc warning appears:<br>
cmake_pch.hxx.gch: not used because `PrecompileVtkHeaders_EXPORTS’ not defined [-Winvalid-pch]</p>
<p>If I use add_executable rather than add_library in my Precompile*** projects then these warnings disappear… But I still have similar warnings if I try to use precompiled headers in loadable modules.</p>
<p>Do you have any experience / guidelines with precompiled headers ?<br>
Is it in the 3D Slicer roadmap ?</p>
<p>The results are very interesting (Libs/MRML/Widgets build in 20 seconds rather than 2 minutes if I use QtCore and QtWidgets precompiled headers)</p>
<p>Regards</p>

---
