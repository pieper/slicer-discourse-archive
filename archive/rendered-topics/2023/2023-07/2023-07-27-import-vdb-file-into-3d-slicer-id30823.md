---
topic_id: 30823
title: "Import Vdb File Into 3D Slicer"
date: 2023-07-27
url: https://discourse.slicer.org/t/30823
---

# Import VDB File into 3D Slicer

**Topic ID**: 30823
**Date**: 2023-07-27
**URL**: https://discourse.slicer.org/t/import-vdb-file-into-3d-slicer/30823

---

## Post #1 by @domdow (2023-07-27 00:19 UTC)

<p>Hello,</p>
<p>I am looking to import a .VDB file into 3D Slicer. When I try importing I receive a error notification:</p>
<p>" Error occurred while loading the selected files. Click ‘Show details’ button and check the application log for more information."</p>
<p>The error log:<br>
Loading /user/desktop/test_01.vdb - load failed</p>
<p>Can you please help me understand how load a VDB into 3D Slicer?</p>
<p>Thank you,</p>
<p>Dom</p>

---

## Post #2 by @tsehrhardt (2023-07-27 13:38 UTC)

<p>You can load a vdb into Paraview or Blender.</p>

---

## Post #3 by @lassoan (2023-07-30 12:05 UTC)

<p>OpenVDB reader/writer is available in VTK, so we could expose it in Slicer with not too much work. Or, we could wait for ITK to support and then we could enable support for it by modifying only 1-2 liines (as we already use ITK for reading/writing most image types).</p>
<p>Integration will happen faster if there is confirmed interest in this by the community (or somebody contributes with development work or specific funding) . I’ll change the category of this topic to “feature request” to allow people to vote on it.</p>
<p>As <a class="mention" href="/u/tsehrhardt">@tsehrhardt</a> wrote above, ParaView can already read vdb files, so until Slicer has direct support, you can read the vdb file for n ParaView and save as vti, mha, nrrd image file that Slicer can read.</p>

---

## Post #4 by @domdow (2023-08-01 01:27 UTC)

<p>Thanks Andras,</p>
<p>What would it take to add it to 3D Slicer?</p>
<p>You mentioned VTK are you referring to the <a href="http://GitHub.com/Slicer/vtkAddon" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/vtkAddon: General-purpose features that may be integrated into VTK library in the future.</a> you created? Or another piece of software?</p>
<p>And what is ITK I am not familiar?</p>

---

## Post #5 by @lassoan (2023-08-01 02:52 UTC)

<p>I was referring to the VDB reader and writer in VTK:</p>
<ul>
<li><a href="https://vtk.org/doc/nightly/html/classvtkOpenVDBReader.html">https://vtk.org/doc/nightly/html/classvtkOpenVDBReader.html</a></li>
<li><a href="https://vtk.org/doc/nightly/html/classvtkOpenVDBWriter.html" class="inline-onebox">VTK: vtkOpenVDBWriter Class Reference</a></li>
</ul>
<p>It is not enabled by default (and not enabled in Slicer build of VTK either) because it requires the <a href="https://github.com/AcademySoftwareFoundation/openvdb">OpenVDB library</a>. OpenVDB uses permissive license, so integrating it should not be an issue.</p>
<blockquote>
<p>What would it take to add it to 3D Slicer?</p>
</blockquote>
<ul>
<li>Add a VDB CMake option to Slicer (<code>Slicer_BUILD_VDB_SUPPORT</code> or something similar)</li>
<li>Add OpenVDB as a dependency to the Slicer build (similarly to rapidjson, teem, zlib, sqlite, …), enabled when <code>Slicer_BUILD_VDB_SUPPORT</code> is enabled</li>
<li>Update Slicer’s VTK build to enable <code>VTK_MODULE_ENABLE_VTK_IOOpenVDB</code> when <code>Slicer_BUILD_VDB_SUPPORT</code> is enabled</li>
<li>Add VTK’s VDB reader/writer to <code>vtkMRMLVolumeArchetypeStorageNode</code>, similarly to <code>vtkTeemReader</code></li>
</ul>

---

## Post #6 by @domdow (2023-08-14 04:34 UTC)

<p>Hi Andras,</p>
<p>As I am industrial designer adding an OpenVBD library into Slicer seems a little out of my depth.</p>
<p>Would you know how I could go about this? Or someone I could work with to add this feature?</p>
<p>Thanks,</p>
<p>Dom</p>

---

## Post #7 by @lassoan (2023-08-14 06:41 UTC)

<p>If it is urgent for you then you can ask a friend (who has some C++ programming experience) or  hire Kitware or other Slicer commercial partner company, or just wait for someone else to implement it. In the meantime, you can convert manually to nifti or nrrd format in ParaView  or other software.</p>

---

## Post #8 by @tsehrhardt (2023-08-29 13:37 UTC)

<p>Would Blender or Paraview not have functions you can use for now to work with the VDB?</p>

---
