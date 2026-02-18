# How to package slicer to a zip for publication

**Topic ID**: 43185
**Date**: 2025-06-02
**URL**: https://discourse.slicer.org/t/how-to-package-slicer-to-a-zip-for-publication/43185

---

## Post #1 by @zhaokaien (2025-06-02 03:01 UTC)

<p>Hello, I have successfully built Slicer v5.9 from source code, and Slicer runs normally. I’ve also performed custom development on Slicer, and everything works as expected. Now, I need to <code>INSTALL</code> and <code>PACKAGE</code> Slicer so we can properly distribute it to users for testing. However, when I try to <code>INSTALL</code>, I get an error in Visual Studio. When I try to <code>PACKAGE</code>, there’s no error, and an <code>.exe</code> file is generated normally. When I double-click this <code>.exe</code> file, it prompts me to install it. I’ve found Slicer’s official documentation on this part to be very brief, only providing a single command for how to execute <code>PACKAGE</code>. I’d like to ask, is it normal for <code>INSTALL</code> to fail but <code>PACKAGE</code> to succeed? How can I package Slicer into a ZIP file? Thanks to all the experts in the forum for your guidance! Thank you!</p>

---

## Post #2 by @muratmaga (2025-06-03 15:47 UTC)

<p>I don’t know about packaging in Visual Studio, but if you successfully build your Slicer and everything is working fine, you can simply zip that folder and give it to your users. Slicer is portable. I don’t think you need to build an installer…</p>

---

## Post #3 by @zhaokaien (2025-06-04 10:13 UTC)

<p>Thank you for your replying, I set variables like <strong>CMAKE_INSTALL_PREFIX</strong> and <strong>CPACK_GENERATOR</strong> in the CMake GUI, but after generation, these variables don’t seem to have any effect. Ultimately, an executable file named <strong>Slicer-5.9.0-2025-05-28-win-amd64.exe</strong> and a folder named <strong>Slicer-5.9.0-2025-05-28-win-amd64</strong> are still generated in this directory on my computer: <code>E:\D\SR\Slicer-build\_CPack_Packages\win-amd64\NSIS</code>. The .exe file is an installer, and all the files in the folder are what this installer compresses.</p>
<p>I’m currently trying to zip this folder and distribute it to users. The program runs, but there’s an issue: this zipped folder seems to depend on my <strong>python-install</strong> directory from when I built Slicer. I originally thought the packaged files would include Slicer’s own Python environment, but that’s not the case, which is causing me a lot of trouble. Did I not set things up correctly during the build process, leading to the packaging process not including the necessary files from the <strong>python-install</strong> folder?I don’t know how to package the “python-install” dir into the zip, Could you please guide me again? Thanks!</p>

---
