# Making landmark-based warping transformation faster

**Topic ID**: 5247
**Date**: 2019-01-02
**URL**: https://discourse.slicer.org/t/making-landmark-based-warping-transformation-faster/5247

---

## Post #1 by @Abdelkhalek (2019-01-02 18:26 UTC)

<p>Hi, what is the Python library which I can use in order to speed up a 3D Slicer script?<br>
Many thanks in advance.</p>

---

## Post #2 by @lassoan (2019-01-02 18:56 UTC)

<p>Optimization is always very application-specific. What would you like to do?</p>

---

## Post #3 by @Abdelkhalek (2019-01-02 19:02 UTC)

<p>Hi Andras. Thank you for your reply.<br>
I created a new function on the script in order to update the transformation of the surface mesh <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebc32ab9eeec4ea6c46ea634ab150db3d1e16e1d.png" alt="Markups_Trans0" data-base62-sha1="xDElCreKN3bkKHaAWgNDv0TU38N" width="449" height="441">  based on the deformation of the 3D Markups as below:</p>
<pre><code>

 def updateTpsTransform(caller, eventid):
            numPerEdge = self.fromFids.GetNumberOfFiducials()
            if numPerEdge != self.toFids.GetNumberOfFiducials():
                print
                'Error: Fiducial numbers are not equal!'
                return

            fp = vtk.vtkPoints()
            tp = vtk.vtkPoints()
            f = [0, 0, 0]
            t = [0, 0, 0]

            for i in range(numPerEdge):
                self.fromFids.GetNthFiducialPosition(i, f)
                self.toFids.GetNthFiducialPosition(i, t)
                fp.InsertNextPoint(f)
                tp.InsertNextPoint(t)

            tps = vtk.vtkThinPlateSplineTransform()
            tps.SetSourceLandmarks(fp)
            tps.SetTargetLandmarks(tp)
            tps.SetBasisToR()
            self.tNode.SetAndObserveTransformToParent(tps)

        self.toFids.AddObserver(vtk.vtkCommand.ModifiedEvent, updateTpsTransform)
</code>
</pre> 
<p>However, the manual transformation is very slow.</p>

---

## Post #4 by @lassoan (2019-01-02 19:14 UTC)

<p>You would need to use profiling to determine where the perfomance bottleneck is then improve that.</p>
<p>If you don’t know how to do profiling then you can try a few trivial things blindly:</p>
<p>1/ Use Fiducial registration wizard module (in SlicerIGT extension), to compute the transform. It does the same as your code snippet but implemented in C++, so it may be faster (especially the conversion from markups to vtk points).</p>
<ol start="2">
<li>
<p>You should also decimate the transformed model using Surface toolbox module as much as possible. Usually you can reduce the number of points by 80-90% without visible difference.</p>
</li>
<li>
<p>If you transform models then, set transform <strong>from</strong> parent (and swap source/target landmarks), since that is the forward direction when transforming models or points (transform <em>to</em> parent is the forward direction when transforming images, since image warping requires resampling transform).</p>
</li>
<li>
<p>Simplify visualization as much as possible. For example, if you showing model/slice intersection is not essential then hide that.</p>
</li>
</ol>

---

## Post #5 by @ungi (2019-01-03 02:14 UTC)

<p>If you run the original code from the SlicerIGT website, that transforms a 3D grid, does it run fast?</p>
<p>If no, then your computer should probably be upgraded. That code runs fast on average computers.</p>
<p>If yes, then your surface model is too large for the Slicer MRML event system. I had such a problem ealier and the solution was to keep the surface model in a vtkPolyData (not in a vtkMRMLModelNode). Transform the vtkPolyData with the TPS transform you compute at each update, using only VTK functions. Then set this transformed vtkPolyData as the polydata of a vtkMRMLModelNode. Essentially, you prevent Slicer from doing the model transformation for you, because you provide an already transformed model for the MRML system. I could achieve 10x faster rendering this way, but I had several large models, so may experience less improvement if you only have one model.</p>

---

## Post #6 by @Abdelkhalek (2019-01-08 08:41 UTC)

<p>Thank you for the help. Could I use Cython in my script?<br>
Is there any way for 3D Slicer to accept pyx file extensions as modules?</p>
<p>Thank you in advance.</p>

---

## Post #7 by @jcfr (2019-01-08 13:12 UTC)

<aside class="quote no-group" data-username="Abdelkhalek" data-post="6" data-topic="5247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a6a055/48.png" class="avatar"> Abdelkhalek:</div>
<blockquote>
<p>Is there any way for 3D Slicer to accept pyx file extensions as modules</p>
</blockquote>
</aside>
<p>Considering that (1) a <code>.pyx</code> file is compiled by Cython to a <code>.c</code> file, containing the code of a Python extension module and that (2) the <code>.c</code> file is compiled by a C compiler to a <code>.so</code> file (or <code>.pyd</code> on Windows) which can be <code>import</code> -ed directly into a Python session, Slicer has no way to directly import <code>pyx</code> files. This would require the user to have a compiler available.</p>
<p>While there are way to make this happen, it would not be straightforward across all platforms. That said, after we transition to python 3. This will be easier as the official compiler for Slicer distribution will match the one of Python official distribution.</p>
<p>After trying the suggestion of <a class="mention" href="/u/ungi">@ungi</a>,  I suggest you (1) identify the bottleneck, (2) look for equivalent optimized functions or (if there are none), write the function in a module logic in c++ and expose it to python.</p>

---

## Post #8 by @lassoan (2019-01-08 13:31 UTC)

<aside class="quote no-group" data-username="Abdelkhalek" data-post="6" data-topic="5247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a6a055/48.png" class="avatar"> Abdelkhalek:</div>
<blockquote>
<p>Could I use Cython in my script?</p>
</blockquote>
</aside>
<p>You don’t need to use Cython, you can directly implement any part of your module in C++. Either as a loadable module (for real-time interactions and custom GUI) or as a CLI module - see more information <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules">here</a>.</p>

---

## Post #9 by @Abdelkhalek (2019-01-14 10:23 UTC)

<p>Thank you for your detailed explanation. Would it be possible to use Boost lib in order to write the function in a module logic in C++ and to expose it to Python?<br>
Could you please show any example of a function which was written and exposed to Python and adopted in a 3D Slicer ?<br>
Thank you in advance.</p>

---

## Post #10 by @lassoan (2019-01-15 04:15 UTC)

<aside class="quote no-group" data-username="Abdelkhalek" data-post="9" data-topic="5247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a6a055/48.png" class="avatar"> Abdelkhalek:</div>
<blockquote>
<p>Would it be possible to use Boost lib</p>
</blockquote>
</aside>
<p>Yes, sure you can use any C++ library. Boost is library is huge, so probably the simplest is to just copy what you need using <a href="https://www.boost.org/doc/libs/1_69_0/tools/bcp/doc/html/index.html">bcp</a> into your module’s Logic.</p>
<aside class="quote no-group" data-username="Abdelkhalek" data-post="9" data-topic="5247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a6a055/48.png" class="avatar"> Abdelkhalek:</div>
<blockquote>
<p>Could you please show any example of a function which was written and exposed to Python and adopted in a 3D Slicer ?</p>
</blockquote>
</aside>
<p>All module logic, widget, and MRML classes are Python-wrapped, so you can use any of them as example (you can see that in the example module that Extension Wizard generates). You can get the module logic from Python by calling <code>logic()</code> method of the module object, for example to get Volume Rendering module’s logic: <code>volRenLogic = slicer.modules.volumerendering.logic()</code>.</p>

---
