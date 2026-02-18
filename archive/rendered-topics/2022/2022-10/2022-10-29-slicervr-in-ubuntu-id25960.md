# SlicerVR in Ubuntu

**Topic ID**: 25960
**Date**: 2022-10-29
**URL**: https://discourse.slicer.org/t/slicervr-in-ubuntu/25960

---

## Post #1 by @Mauricio_Cespedes (2022-10-29 04:17 UTC)

<p>Operating system: Ubuntu 20.04<br>
Slicer version: 5.1<br>
Expected behavior: SlicerVR module is loaded properly<br>
Actual behavior: I can’t load SlicerVR</p>
<p>Hi,<br>
I’m currently trying to build and load SlicerVR from source code in Ubuntu. The commands that I followed were the following:</p>
<ol>
<li>Cloned the repo in a source directory: <code>git clone https://github.com/KitwareMedical/SlicerVirtualReality.git .</code>
</li>
<li>Created a build directory and configure the cmake file:<code> cmake -DSlicer_DIR:PATH=/opt/D/Slicer-superbuild/Slicer-build ../source/</code>
</li>
<li>Build SlicerVR: <code>make -j8</code>
</li>
</ol>
<p>Then I added the folder <code>/opt/D/SlicerVR/build/inner-build/lib/Slicer-5.1/qt-loadable-modules/</code> to Additional Paths through the GUI. It was not working at this point; therefore, I was trying to do something similar as what is recommended for Windows here <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerVirtualReality/DeveloperGuide.md at master · KitwareMedical/SlicerVirtualReality · GitHub</a> (which is copy the dll files to the <code>qt-loadable-modules\</code> folder). As it’s Linux, I was trying to look for *.so equivalent files. I did find an equivalent to the file <code>(SlicerVirtualReality-binary)\OpenVR\bin\win64\openvr_api.dll</code> but there’s no <code>bin</code> folder in the build directory so I haven’t been able to find an equivalent to <code>(SlicerVirtualReality-binary)\bin\Release\vtkRenderingOpenVR-9.0.dll</code>.<br>
Therefore, I haven’t been able to add the module library. Any advice?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2022-10-30 12:33 UTC)

<p>I don’t know anyone who has ever tried to use OpenVR on Linux. If you cannot find this library on Linux then probably it does not exist.</p>
<p>We are slowly moving to OpenXR. There is funding and the development is already in progress (maybe <a class="mention" href="/u/adamrankin">@adamrankin</a> can provide more details). If you find that OpenXR is supported on Linux then you may be able to try that soon.</p>

---
