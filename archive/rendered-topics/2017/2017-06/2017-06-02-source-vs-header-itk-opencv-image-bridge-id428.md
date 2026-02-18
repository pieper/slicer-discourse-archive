# Source vs. Header: ITK OpenCV Image Bridge

**Topic ID**: 428
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/source-vs-header-itk-opencv-image-bridge/428

---

## Post #1 by @tdiprima (2017-06-02 16:38 UTC)

<p>I have a C++ header file and a source file.  I’m including itkOpenCVImageBridge.h"`.  The include compiles as long as it’s in the source file.  I can’t put it in the header.  We want to put all the source in the header, and delete the source.  But like I said it won’t compile.  The error is:</p>
<blockquote>
<p>fatal error: itkOpenCVImageBridge.h: No such file or directory</p>
</blockquote>
<p>I don’t get it.  Can anyone please point me in the right direction?  I already went in the Google direction… But the advice is to set <code>Module_ITKVideoBridgeOpenCV</code> on when compiling ITK (which is already being pulled in by Slicer).</p>
<p>Help…</p>

---

## Post #2 by @lassoan (2017-06-02 17:26 UTC)

<p>Adding any OpenCV include files into a header file would make other modules directly depend on OpenCV, which would cause build failure. You did right at the beginning: have a clean public interface in the header file and have all private implementation details (with special dependencies) in the cxx file.</p>

---

## Post #3 by @thewtex (2017-06-02 20:15 UTC)

<p>Take a look at SlicerOpenCV, which builds both OpenCV and the ITKVideoBridgeOpenCV module outside of ITK:</p>
<p><a href="https://github.com/SBU-BMI/SlicerOpenCV" rel="nofollow noopener">https://github.com/SBU-BMI/SlicerOpenCV</a></p>

---
