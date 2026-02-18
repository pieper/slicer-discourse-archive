# VMTK generated centerline curves missing structure hierarchy

**Topic ID**: 36586
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/vmtk-generated-centerline-curves-missing-structure-hierarchy/36586

---

## Post #1 by @RomanStriker (2024-06-04 12:11 UTC)

<p>Hi,</p>
<p>I am using the Extract Centerline module of VMTK extension to generate network and centerline curves for the network and centerline models. The problem is that the network curve generated is missing the hierarchical structure, while the centerline cuve only consists of a single curve. What could be causing this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c55f76b46fdae9614c9b23fc3348686ef0fad0ec.jpeg" data-download-href="/uploads/short-url/sa2AGsUPtndqNH7sNQQPSGtpNqk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55f76b46fdae9614c9b23fc3348686ef0fad0ec_2_690x359.jpeg" alt="image" data-base62-sha1="sa2AGsUPtndqNH7sNQQPSGtpNqk" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55f76b46fdae9614c9b23fc3348686ef0fad0ec_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55f76b46fdae9614c9b23fc3348686ef0fad0ec_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c55f76b46fdae9614c9b23fc3348686ef0fad0ec_2_1380x718.jpeg 2x" data-dominant-color="B7BCD6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×999 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c05cbb4058c08dfa54e70f45b2b9ad6c5b9338ef.jpeg" data-download-href="/uploads/short-url/rrIlJuaVbLGfZ0yq8TKHDsLa8uH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c05cbb4058c08dfa54e70f45b2b9ad6c5b9338ef_2_690x376.jpeg" alt="image" data-base62-sha1="rrIlJuaVbLGfZ0yq8TKHDsLa8uH" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c05cbb4058c08dfa54e70f45b2b9ad6c5b9338ef_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c05cbb4058c08dfa54e70f45b2b9ad6c5b9338ef_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c05cbb4058c08dfa54e70f45b2b9ad6c5b9338ef_2_1380x752.jpeg 2x" data-dominant-color="BDBFDA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1047 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-04 16:01 UTC)

<aside class="quote no-group" data-username="RomanStriker" data-post="1" data-topic="36586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c37758/48.png" class="avatar"> RomanStriker:</div>
<blockquote>
<p>The problem is that the network curve generated is missing the hierarchical structure</p>
</blockquote>
</aside>
<p>Network does not have a hierarchical structure. It is an arbitrary graph structure. You can traverse the lines and determine branching points by finding points that are used in multiple lines.</p>
<aside class="quote no-group" data-username="RomanStriker" data-post="1" data-topic="36586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c37758/48.png" class="avatar"> RomanStriker:</div>
<blockquote>
<p>he centerline cuve only consists of a single curve</p>
</blockquote>
</aside>
<p>Centerline curve is not a single curve. It is a single model (polydata) that contains lots of polylines. It is a hierarchical structure (it is a “forest” topology) and you can use VMTK filters to identify branches (see for example how the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/e9aa8e7e532299c10cfae5746e9c7ef06a4314b1/ExtractCenterline/ExtractCenterline.py#L833">Slicer module creates a curve from each branch</a>).</p>

---

## Post #3 by @RomanStriker (2024-06-04 18:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="36586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Centerline curve is not a single curve. It is a single model (polydata) that contains lots of polylines.</p>
</blockquote>
</aside>
<p>I have a <code>Centerline model</code> shown in the subject hierarchy tab above, which is a polydata object with multiple lines, which is fine and is drawn in the 3d view in green in the first image. The problem is with the <code>Centerline curve (0)</code> which is obtained from the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/e9aa8e7e532299c10cfae5746e9c7ef06a4314b1/ExtractCenterline/ExtractCenterline.py#L833" rel="noopener nofollow ugc">createCurveTreeFromCenterline</a> function (it should be called when I add a new curve in the ‘Centerline curve’ field as shown in the image below in the Extract Centerline module) and it should be heirarchical structure with tree topology.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74fab95b6b6252b3ff360821587e09896ae380e8.jpeg" data-download-href="/uploads/short-url/gGQyK4TWIVxxkaYFPTzJy0wqKgw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74fab95b6b6252b3ff360821587e09896ae380e8_2_690x498.jpeg" alt="image" data-base62-sha1="gGQyK4TWIVxxkaYFPTzJy0wqKgw" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74fab95b6b6252b3ff360821587e09896ae380e8_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74fab95b6b6252b3ff360821587e09896ae380e8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74fab95b6b6252b3ff360821587e09896ae380e8.jpeg 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">936×676 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have tried this on a different vessel tree centerline and this approach gives me the hierarchical structure but for this lung airway which is clearly a tree structure it fails and I only get a single curve <code>Centerline curve (0)</code> shown in the second image in my original post. The result on a different tree is shown in the image below, and you can see in the Subject hierarchy tab that the <code>Centerline curve (0)</code> has a tree topology with children nodes.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dacece2de3d0af1a73130f5ccfb96f43e231af0c.jpeg" data-download-href="/uploads/short-url/vdFamavLWdlZbQtgLjQjuqA6sEs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacece2de3d0af1a73130f5ccfb96f43e231af0c_2_690x198.jpeg" alt="image" data-base62-sha1="vdFamavLWdlZbQtgLjQjuqA6sEs" width="690" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacece2de3d0af1a73130f5ccfb96f43e231af0c_2_690x198.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacece2de3d0af1a73130f5ccfb96f43e231af0c_2_1035x297.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dacece2de3d0af1a73130f5ccfb96f43e231af0c_2_1380x396.jpeg 2x" data-dominant-color="B9BCD8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×553 84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know I can write a custom function to find where the centerline model branches and create a tree myself, but I was wondering why this function does not work for this airway tree.</p>

---

## Post #4 by @lassoan (2024-06-04 18:51 UTC)

<p>In the second image of the top post (where there is only a single short curve) the centerline extraction seems to have failed in some unexpected way. You may see in the application log some hints of what happened. If you share the input segmentation then I can have a look.</p>

---

## Post #5 by @RomanStriker (2024-06-04 19:27 UTC)

<p>I get the following warnings when running the Extract Centerline Module.</p>
<pre><code class="lang-auto">[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 240
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Degenerate descent detected. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
</code></pre>
<p>There are also some other errors that I always get during startup, but they don’t seem to affect the centerline extraction normally. The whole output is as following.</p>
<pre><code class="lang-auto">Python 3.9.10 (main, Apr  5 2024, 04:28:47) 
[GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux2
&gt;&gt;&gt; 
Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython
Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython
[Qt]   Error(s):
[Qt]     CLI executable: /home/roman/Slicer-5.6.2/slicer.org/Extensions-32448/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules/vtkvmtk.py
[Qt]     The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.
[Qt] Fail to instantiate module  "vtkvmtk"
[Qt] The following modules failed to be instantiated:
[Qt]    vtkvmtk
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 240
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Degenerate descent detected. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
[VTK] Warning: In vtkvmtkSteepestDescentLineTracer.cxx, line 213
[VTK] vtkvmtkSteepestDescentLineTracer (0x192f00d0): Can't find a steepest descent edge. Target not reached.
</code></pre>
<p>It seems to fail at the first bifurcation point.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f17484b36b88672064bb9c48650d8fbd374787d.jpeg" data-download-href="/uploads/short-url/i8iwiVKKAxIR6yNl4S5O8WfpFc9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f17484b36b88672064bb9c48650d8fbd374787d.jpeg" alt="image" data-base62-sha1="i8iwiVKKAxIR6yNl4S5O8WfpFc9" width="690" height="409" data-dominant-color="8F96BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×679 44.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb6f249bdb692bb31d3af3cec89552375eaab1a4.jpeg" data-download-href="/uploads/short-url/zShY0uf8rSRcCK1TbgsaAN39vKY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb6f249bdb692bb31d3af3cec89552375eaab1a4_2_690x390.jpeg" alt="image" data-base62-sha1="zShY0uf8rSRcCK1TbgsaAN39vKY" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb6f249bdb692bb31d3af3cec89552375eaab1a4_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb6f249bdb692bb31d3af3cec89552375eaab1a4_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb6f249bdb692bb31d3af3cec89552375eaab1a4.jpeg 2x" data-dominant-color="8F95BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1182×669 98.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a36daa8c55fda7aba112268369ab5ffea5de3daf.png" data-download-href="/uploads/short-url/njKML4ZsSUu4dsLxOxwE5pUmxSD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36daa8c55fda7aba112268369ab5ffea5de3daf_2_690x369.png" alt="image" data-base62-sha1="njKML4ZsSUu4dsLxOxwE5pUmxSD" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36daa8c55fda7aba112268369ab5ffea5de3daf_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a36daa8c55fda7aba112268369ab5ffea5de3daf_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a36daa8c55fda7aba112268369ab5ffea5de3daf.png 2x" data-dominant-color="9B9DD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1189×637 41.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @RomanStriker (2024-06-05 10:16 UTC)

<p>I get the full centerline curve after grow the segmentation mask.</p>

---

## Post #7 by @bobcieri (2025-04-29 07:59 UTC)

<p>Can you be more specific? I am having a similar issue here. Do you mean that you made the surface mesh larger, with grow or similar?</p>

---
