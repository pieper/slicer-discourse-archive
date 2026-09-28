---
topic_id: 48315
title: "Crash rendering very large meshes on macOS: Apple's OpenGL driver fails on glBufferSubData uploads over 2 GB"
date: 2026-09-27
url: https://discourse.slicer.org/t/48315
last_bumped: 2026-09-27T21:24:17.420Z
---

# Crash rendering very large meshes on macOS: Apple's OpenGL driver fails on glBufferSubData uploads over 2 GB

**Topic ID**: 48315
**Date**: 2026-09-27
**URL**: https://discourse.slicer.org/t/crash-rendering-very-large-meshes-on-macos-apples-opengl-driver-fails-on-glbuffersubdata-uploads-over-2-gb/48315

---

## Post #1 by @hherhold (2026-09-27 21:24 UTC)

<p>I ran into an issue with a very complex segmentation on an M5 Max (128GB RAM). A summary from Claude Opus 5.5 (with fix) as follows:</p>
<p>Summary</p>
<p>On Apple Silicon, Slicer crashes (`EXC_BAD_ACCESS` in `_platform_memmove`) when rendering a mesh whose vertex or index buffer is larger than 2 GB. The crash is in Apple’s OpenGL-on-Metal driver, inside `glBufferSubData`. VTK can avoid it by uploading large buffers in chunks.</p>
<p>To repro:</p>
<p>I loaded a full-resolution CT (1164×1393×2206) and a `.seg.nrrd` saved with the Closed surface representation, decimation 0 and smoothing off. The largest segment’s surface is about 234M triangles. `vtkOpenGLIndexBufferObject::CreateTriangleIndexBuffer` builds 701,005,668 indices and uploads them in one 2,804,022,672-byte `glBufferSubData` call:</p>
<pre><code class="lang-auto">frame #0: libsystem_platform.dylib`_platform_memmove + 88
frame #1: AppleMetalOpenGLRenderer`gldBufferSubData + 300
frame #2: GLEngine`glBufferSubData_Exec + 548
frame #3: libvtkOpenGL`vtkOpenGLBufferObject::UploadRangeInternal(..., offset=0, size=2804022672, objectType=ElementArrayBuffer) at vtkOpenGLBufferObject.cxx:263
frame #4: libvtkOpenGL`vtkOpenGLBufferObject::UploadInternal(...)
frame #6: libvtkOpenGL`vtkOpenGLIndexBufferObject::CreateTriangleIndexBuffer(...)
frame #7: libvtkOpenGL`vtkOpenGLPolyDataMapper::BuildIBO(...)

</code></pre>
<p><strong>Isolating the driver bug</strong></p>
<p>A standalone CGL/OpenGL 3.2 core program, with no VTK involved, shows:</p>
<p>- <code>`glBufferData(GL_ARRAY_BUFFER, 2804022672, NULL, GL_STATIC_DRAW)`</code> succeeds. `glGetError()` returns 0 and `GL_BUFFER_SIZE` reports the full 2804022672 bytes.</p>
<p>- A single <code>glBufferSubData</code> of 2³¹ bytes (2147483648) works, but anything larger crashes. I tested 2147487744 and 2804022672.</p>
<p>- Uploading the same 2.8 GB buffer as several `glBufferSubData` calls of ≤1 GB (or ≤2³¹−1 bytes) works. `glGetError()` is clean and reading the buffer back with `glMapBufferRange` matches the source exactly.</p>
<p>This isn’t a real hardware limit: `MTLDevice.maxBufferLength` on this machine is about 86 GB. The driver doesn’t report an error either; it just crashes.</p>
<p>Environment: Apple M5 Max, 128 GB RAM, macOS 26.5 (25F71), Slicer main with the Slicer VTK fork (VTK 9.6.1, `470a7a557a`). I reproduced it in both Debug and RelWithDebInfo builds.</p>
<p>**Proposed fix (VTK)**</p>
<p>Split the upload in <code>vtkOpenGLBufferObject::UploadRangeInternal</code> into chunks. All VBO and IBO uploads from the polydata mapper go through this function:</p>
<pre><code class="lang-auto">diff
--- a/Rendering/OpenGL2/vtkOpenGLBufferObject.cxx
+++ b/Rendering/OpenGL2/vtkOpenGLBufferObject.cxx
@@ -5,6 +5,8 @@
 #include "vtk_glad.h"
+#include &lt;algorithm&gt;
+
@@ -260,8 +262,16 @@ bool vtkOpenGLBufferObject::UploadRangeInternal(
   glBindBuffer(this-&gt;Internal-&gt;Type, this-&gt;Internal-&gt;Handle);
   vtkDebugMacro(&lt;&lt; "glBufferSubData: "
                 &lt;&lt; "(offset: " &lt;&lt; offset &lt;&lt; ", size: " &lt;&lt; size &lt;&lt; ")");
-  glBufferSubData(
-    this-&gt;Internal-&gt;Type, static_cast&lt;GLintptr&gt;(offset), static_cast&lt;GLsizeiptr&gt;(size), buffer);
+  // Upload in chunks: some drivers (e.g. Apple's OpenGL-on-Metal) crash when
+  // a single glBufferSubData call transfers more than 2^31 bytes.
+  constexpr ptrdiff_t maxChunkSize = ptrdiff_t(1) &lt;&lt; 30;
+  const char* data = static_cast&lt;const char*&gt;(buffer);
+  for (ptrdiff_t chunkOffset = 0; chunkOffset &lt; size; chunkOffset += maxChunkSize)
+  {
+    const ptrdiff_t chunkSize = std::min(maxChunkSize, size - chunkOffset);
+    glBufferSubData(this-&gt;Internal-&gt;Type, static_cast&lt;GLintptr&gt;(offset + chunkOffset),
+      static_cast&lt;GLsizeiptr&gt;(chunkSize), data + chunkOffset);
+  }
   this-&gt;Dirty = false;
</code></pre>
<p>With this patch the segmentation loads and renders correctly: four segments, the largest with 233.7M triangles. For buffers under 1 GB the behavior is exactly the same as before (one call), so it should be safe on all platforms.</p>
<p>Would this be better as a merge request to upstream VTK, to the Slicer VTK fork, or both? I’m happy to submit it, let me know the best way to proceed.</p>

---
