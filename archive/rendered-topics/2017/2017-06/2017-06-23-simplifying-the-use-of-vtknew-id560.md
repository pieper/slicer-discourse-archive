# Simplifying the use of vtkNew

**Topic ID**: 560
**Date**: 2017-06-23
**URL**: https://discourse.slicer.org/t/simplifying-the-use-of-vtknew/560

---

## Post #1 by @lassoan (2017-06-23 15:44 UTC)

<p>For C++ developers only. We had a discussion on the VTK mailing list arguing that vtkNew should be as simple to use as vtkSmartPointer or not. Currently, when an object is created by vtkNew, you need to call .GetPointer() to get the raw pointer.</p>
<p>Current usage:</p>
<pre><code>someFilter-&gt;SetInputData(imageData.GetPointer());
</code></pre>
<p>I recommended to add an implicit converter to raw pointer, so that we can simply write:</p>
<pre><code>someFilter-&gt;SetInputData(imageData);
</code></pre>
<p>If you agree that it would be better to simplify the syntax, <strong><a href="https://docs.google.com/forms/d/e/1FAIpQLScTeGsjR925mL7KyNeTHB3-tvmYxaJF0_72ZnQgX1ihbJuX4A/viewform">please mark your preference in this poll - takes two clicks</a></strong>. If you think that requiring adding .GetPointer() is safer, fill the form accordingly, too.</p>

---

## Post #2 by @pieper (2017-06-23 16:40 UTC)

<p>It that the main use case?  Maybe the vtkSetObjectMacro should be polymorphic and apply GetPointer when needed.</p>

---

## Post #3 by @lassoan (2017-06-23 18:21 UTC)

<p>I think we could add implicit conversion for existing classes at Slicer level, but that would mean that VTK code that works in Slicer may not work (or work slightly differently) in a plain VTK environment. So far 75% of poll respondents support this simplification, so hopefully this can be changed in VTK.</p>

---

## Post #4 by @pieper (2018-12-13 15:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I thought we were getting rid of GetPointer, but it’s still needed, at least on my gcc 7.3 ubuntu 18.04 builds.  I have been <a href="https://github.com/Slicer/Slicer/commit/8f47ce8cb596de776a70ef3731fc4244be909a93" rel="nofollow noopener">just fixing them</a> but they keep popping up.  Can we come up with some way to get rid of them all or if not can we explicitly always use them.</p>
<pre><code class="lang-auto">[ 11%] Building CXX object Libs/MRML/Core/CMakeFiles/MRMLCore.dir/vtkMRMLSegmentationNode.cxx.o
/home/pieper/slicer4/latest/Slicer/Libs/MRML/Core/vtkMRMLSegmentationNode.cxx: In member function ‘virtual bool vtkMRMLSegmentationNode::GenerateEditMask(vtkOrientedImageData*, int, vtkOrientedImageData*, std::__cxx11::string, std::__cxx11::string, vtkOrientedImageData*, double*, vtkMRMLSegmentationDisplayNode*)’:
/home/pieper/slicer4/latest/Slicer/Libs/MRML/Core/vtkMRMLSegmentationNode.cxx:782:63: error: no matching function for call to ‘vtkOrientedImageData::SetImageToWorldMatrix(vtkNew&lt;vtkMatrix4x4&gt;&amp;)’
   maskImage-&gt;SetImageToWorldMatrix(referenceImageToWorldMatrix);
</code></pre>

---

## Post #5 by @jcfr (2018-12-13 16:02 UTC)

<p>After the next patch release, we should be able to remove the explicit use of <code>GeTPointer()</code></p>
<blockquote>
<p>at least on my gcc 7.3 ubuntu 18.04 builds</p>
</blockquote>
<p>Could you confirm that the build is done with VTK8 and c++11 ?</p>

---

## Post #6 by @lassoan (2018-12-13 16:49 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I don’t know about any other developer using qt4/vtk7, so it would be great if you could keep fixing these. I try to pay attention to adding those GetPointer() calls but since the compiler does not complain, it us easy to miss them. After releasing 4.10.1, qt4/vtk7 will not be supported, so this will not be problem anymore.</p>

---

## Post #7 by @pieper (2018-12-15 00:31 UTC)

<p>I added the extra GetPointer calls and also version check ifdef on one vtk method that was added after vtk7.</p>
<p>This was actually a vtk7/Qt5.8 build.  I’ve stopped doing Qt4 builds and have no reason to keep a vtk7 build (it just happened that I updated an old build tree).  So if we can’t be sure these work we should explicitly stop supporting them.</p>

---

## Post #8 by @lassoan (2018-12-15 05:57 UTC)

<p>We’ll explicitly stop supporting it in Slicer-5, which I think should be now or within a few days.</p>

---
