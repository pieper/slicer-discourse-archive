---
topic_id: 16849
title: "Add Directories To Path Env When Launching Slicercat"
date: 2021-03-30
url: https://discourse.slicer.org/t/16849
---

# Add directories to PATH env when launching SlicerCAT

**Topic ID**: 16849
**Date**: 2021-03-30
**URL**: https://discourse.slicer.org/t/add-directories-to-path-env-when-launching-slicercat/16849

---

## Post #1 by @keri (2021-03-30 13:50 UTC)

<p>Hi,</p>
<p>My custom app have .dll dependency. To launch app I need to set PATH env to these .dll (on windows).<br>
Where can I see how this is done in slicer?</p>

---

## Post #2 by @lassoan (2021-04-14 05:48 UTC)

<p>You would normally build (or at least install) these DLLs as part of the custom application package. If you don’t do that then you can simply copy the DLLs into the bin folder of Slicer, or add the external path to the <code>Paths</code> section of your <code>Slicer-NNNN.ini</code> file.</p>

---

## Post #3 by @keri (2021-04-14 12:12 UTC)

<p>Thank you,</p>
<p>I think I’ve found how this is done in Slicer. By adding lines in external project :</p>
<pre><code class="lang-auto"># library paths
set(${proj}_LIBRARY_PATHS_LAUNCHER_INSTALLED 
  ${GDAL_ROOT}
  ${GDAL_ROOT}/data/proj    # path that needs to be added to PATH env
  )
mark_as_superbuild(
  VARS ${proj}_LIBRARY_PATHS_LAUNCHER_INSTALLED
  LABELS "LIBRARY_PATHS_LAUNCHER_INSTALLED"
  )
</code></pre>
<p>path is automatically added to <code>Slicer-NNNN.ini</code> file. In this example I used it in <code>INSTALL</code> mode, but it also can be used in <code>BUILD</code> mode in similar way (examples can be found in slicer’s external package like python or VTK).</p>

---
