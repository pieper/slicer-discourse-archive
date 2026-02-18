# Error after building 

**Topic ID**: 17445
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/error-after-building/17445

---

## Post #1 by @MarioGQ (2021-05-04 14:47 UTC)

<p>Hi everyone. I keep receiving this error when i try to open Slicer environmenr after building it</p>
<p>QWindowsEGLContext: ANGLE only partially supports OpenGL ES &gt; 3.0<br>
QWindowsEGLContext: Failed to create context, eglError: 3005, this: 0x1d151cf5e60</p>
<p>Have enyine got the same? What have you done to resolve it?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-05-21 18:36 UTC)

<p>It seems that you don’t have proper OpenGL support on your computer. Does the code run in some virtual/headless environment?</p>

---
