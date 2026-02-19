---
topic_id: 4574
title: "Highlighted Vtk Changes Associated With Slicer 4 10 Virtual"
date: 2018-10-29
url: https://discourse.slicer.org/t/4574
---

# Highlighted VTK changes associated with Slicer 4.10: Virtual Reality, Rendering, Volume Rendering, Python Wraping, OpenGL performance and threading management

**Topic ID**: 4574
**Date**: 2018-10-29
**URL**: https://discourse.slicer.org/t/highlighted-vtk-changes-associated-with-slicer-4-10-virtual-reality-rendering-volume-rendering-python-wraping-opengl-performance-and-threading-management/4574

---

## Post #1 by @jcfr (2018-10-29 18:43 UTC)

<p>This post highlights some of the recent VTK changes included in Slicer 4.10</p>
<ul>
<li><a href="#heading--blogs">Blogs</a></li>
<li><a href="#heading--build">Build</a></li>
<li><a href="#heading--chart">Chart</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--openvr">OpenVR</a></li>
<li><a href="#heading--performance">Performance</a></li>
<li><a href="#heading--python-wrapping">Python Wrapping</a></li>
<li><a href="#heading--qvtkopenglwidget">QVTKOpenGLWidget</a></li>
<li><a href="#heading--rendering">Rendering:</a></li>
<li><a href="#heading--volume-rendering-fixes">Volume Rendering Fixes</a></li>
<li><a href="#heading--widgets">Widgets</a></li>
</ul>
<h2>Blogs</h2>
<ul>
<li>Rendering translucent geometry intermixed with volumes: <a href="https://blog.kitware.com/rendering-translucent-geometry-intermixed-with-volumes/">https://blog.kitware.com/rendering-translucent-geometry-intermixed-with-volumes/</a>
</li>
<li>VTK 8.0.0: <a href="https://blog.kitware.com/vtk-8-0-0/">https://blog.kitware.com/vtk-8-0-0/</a>
</li>
<li>New OpenGL Rendering in VTK: <a href="https://blog.kitware.com/new-opengl-rendering-in-vtk/">https://blog.kitware.com/new-opengl-rendering-in-vtk/</a>
</li>
</ul>
<h2>Build</h2>
<ul>
<li>
<p><strong>BUG: Common naming of <span class="hashtag">#define</span> conflicts with ITK</strong><br>
<a href="https://github.com/Kitware/VTK/commit/10873ec">kitware/vtk@10873ec</a> (from <code>Hans Johnson &lt;hans-johnson[at]uiowa.edu&gt;</code>)</p>
<p>When VTK and ITK are used together, the<br>
<span class="hashtag">#define</span> ThreadInfoStruct vtkMultiThreader::ThreadInfo<br>
from VTK/Common/Core/vtkMultiThreader.h</p>
<p>would clobber the ThreadInfoStruct definition from<br>
ITK/Modules/Core/Common/include/itkMultiThreaderBase.h</p>
<p>See <a href="https://discourse.itk.org/t/vtk9-and-itk5-conflicts/802">https://discourse.itk.org/t/vtk9-and-itk5-conflicts/802</a></p>
<p>Slicer: Ensure that future build of Slicer against ITK 5.0 and VTK succeed.</p>
</li>
</ul>
<h2>Chart</h2>
<ul>
<li>
<p><strong>Add single click selection in chartXY</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4531/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4531/commits</a> (from <code>Davide Punzo &lt;punzodavide[at]hotmail.it&gt;</code>)</p>
</li>
<li>
<p><strong>Fixed control points clamp function to handle NaN value</strong><br>
<a href="https://github.com/Kitware/VTK/commit/bc627d8">kitware/VTK@bc627d8</a> (from <code>Csaba Pinter &lt;csaba.pinter[at]queensu.ca&gt;</code>)</p>
<p>If the user clicks in a plot that has an invalid (0,0) range, then in vtkContextScene::ProcessItem that<br>
is called after mouse events, the mapped mouse position becomes NaN, due to invalid matrix in the ContextScene’s<br>
transform. This NaN position is then added to the function as a control point with an invalid NaN value. This fix<br>
makes sure this does not happen, by clamping the NaN values to minimum bounds on x axis, and 0 on y axis (any<br>
value comparison returns false if an operand is NaN, so need to check explicitly).</p>
<p>Slicer: Fix <a href="https://issues.slicer.org/view.php?id=4518#c15573">issue 4518</a>: Slicer crashes when clicking on Transforms color widget</p>
</li>
</ul>
<h2>IO</h2>
<ul>
<li>
<p><strong>ENH: Improve scene exporters and STL, OBJ, and PLY file IO</strong><br>
<a href="https://github.com/Kitware/VTK/commit/3b814e9">kitware/VTK@3b814e9</a> (from <code>Andras Lasso &lt;lasso[at]queensu.ca&gt;</code>)</p>
<ul>
<li>Allow reading/writing custom comments in STL, PLY, and OBJ files. This allows<br>
storing metadata, such as coordinate system, unit, or color in the files.</li>
<li>Allow reading/writing binary comments (that can contain 0 character) for STL<br>
files. This allows reading/writing color information in Mimics-style (Mimics<br>
software writes RGBA color as 4 bytes in STL file binary header).</li>
<li>Allow specifying renderer for exporting: Some exporters rejected to export<br>
a scene when more renderers were associated with a render window. This was an<br>
issue because it prevented scene export when additional renderers were used for<br>
displaying various annotations on the render window. Instead of hardcoding using<br>
the first renderer, added a ActiveRenderer member, which defines which renderer<br>
content should be exported. If not set then the first renderer is used, so the<br>
behavior is backward-compatible.</li>
<li>Fixed writing of of .mtl file path in .obj file (full path of .mtl file was<br>
written into the .obj file).</li>
</ul>
<p>Slicer: Used in Segmentation and SegmentEditor modules</p>
</li>
<li>
<p><strong>Add support for writing larger unstructured grids</strong><br>
<a href="https://github.com/Kitware/VTK/commit/a7988f5">kitware/VTK@a7988f5</a> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>)</p>
<p>Patch from gitlab Constantine <span class="mention">@Butakoff</span></p>
<p>Slicer: used in vtkMRMLModelStorageNode and ProbeVolumeWithModel</p>
</li>
</ul>
<h2>OpenVR</h2>
<ul>
<li>
<p><strong>remove openvr factory</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4540/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4540/commits</a> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>)</p>
</li>
<li>
<p><strong>fix an issue with flying controller labels</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4447/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4447/commits</a> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>)</p>
<p>Labels would flyu off the controller while<br>
flying through VR due to position calc being done<br>
prior to the world translation.</p>
</li>
<li>
<p><strong>better code for handling panel rotations</strong>. See <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4480/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4480/commits</a></p>
</li>
<li>
<p><strong>Fix an issue with moving to the next saved pose.</strong> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>) .See <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4767">https://gitlab.kitware.com/vtk/vtk/merge_requests/4767</a></p>
</li>
</ul>
<h2>Performance</h2>
<ul>
<li>
<p><strong>Resolve "Multithreader creates many unnecessary threads"</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4175/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4175/commits</a> (from <code>David Gobbi &lt;David Gobbi &lt;david.gobbi[at]gmail.com&gt;</code>)</p>
<p>Creating threads is expensive, so creating threads that do nothing should be avoided.</p>
<ul>
<li>Limit number of threads in vtkImageHistogram</li>
<li>Remove redundant UpdateExtent calculation.</li>
<li>Use vector to allocate arrays instead of new</li>
<li>17279: Limit num threads to num pieces.</li>
</ul>
</li>
<li>
<p><strong>hardware picking code: improve picking performance and memory footprint</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4175/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4175/commits</a> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>)</p>
<p>Significant rework of the hardware picking code.</p>
<p>Previously each mapper had to make sure that the rendered<br>
colors were correct for point/cell etc ID during hardware picking<br>
and this required large datastructures and texture uploads<br>
to the GPU on each pick.</p>
<p>Now it collects the color buffers and gives the mappers a chance to<br>
update them. This allows us to use gl_VertexId and gl_PrimitiveId<br>
directly in the shader and then if picked, allow the mapper to<br>
adjust the color buffer as needed. This allows us to avoid<br>
rebuilding the VBO and textures each time and avoids the memory<br>
footprint related to that.</p>
</li>
<li>
<p><strong>Fix issue where picking happened with a bad context</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4616/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4616/commits</a> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>)</p>
<p>Make sure our OpenGL context is current when hardware picking</p>
</li>
<li>
<p><strong>VolumeRendering: update volume rendering to share jitter and depth textures</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4416/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4416/commits</a> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>)</p>
</li>
<li>
<p><strong>some opengl performance fixes</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4389/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4389/commits</a> (from <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code>)</p>
<p>mostly cache a few items to avoid glGet* invocations</p>
<p>remove an unused ivar form the image slice mapper</p>
<p>make it so that the image slice mapper does not force<br>
an IBO rebuild every frame as typically it is not needed<br>
and a waste of CPU-GPU</p>
</li>
<li>
<p><strong>Improve vtkAppendFilter efficiency</strong><br>
<a href="https://github.com/Kitware/VTK/commit/d36b129">kitware/VTK@d36b129</a> (from <code>Andrew Bauer &lt;andy.bauer[at]kitware.com&gt;</code>)</p>
<p>If there’s a single unstructured grid in the composite dataset we<br>
now just do a shallow copy of that to the output.</p>
<p>Slicer: used in vtkSlicerTransformLogic, vtkSlicerSegmentationsModuleLogic,<br>
vtkOrientedImageDataResample, vtkMRMLVolumeNode, MergeModels CLI,<br>
and ScriptedSegmentEditor templates</p>
</li>
</ul>
<h2>Python Wrapping</h2>
<ul>
<li>
<p><strong>Wrap std::vector for basic vector types</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4545/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4545/commits</a> (from David Gobbi)</p>
<p>Wraps std::vector arguments for Python where the value type is std::string or a fundamental<br>
numeric type (excluding ‘char’ due to its ambiguity)</p>
</li>
</ul>
<h2>QVTKOpenGLWidget</h2>
<ul>
<li>
<p><strong>Add Qt gestures events to QVTKOpenGLWidget</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4398/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4398/commits</a> (from <code>Kyle Sunderland &lt;sunderlandkyl[at]gmail.com&gt;</code>)</p>
<p>Qt gestures in QVTKOpenGLWidget are handled by QVTKInteractorAdapter, which will update the<br>
interactor and invoke corresponding events</p>
</li>
<li>
<p><strong>Correct QVTKOpenGLWidget double click management, Correct MakeCurrent behavior</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4400/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4400/commits</a> (from <code>Mathieu Westphal &lt;mathieu.westphal[at]kitware.com&gt;</code>)</p>
</li>
<li>
<p><strong>Add stero support</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4317/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4317/commits</a> (from <code>Mathieu Westphal &lt;mathieu.westphal[at]kitware.com&gt;</code>)</p>
<ul>
<li>Improve QVTKOpenGLWidget and add QVTKOpenGLWindow class based on QOpenGLWindow</li>
<li>Fix viewport size before FXAA pass on OSX</li>
<li>Invoke WindowResizeEvent on vtkWindow::SetSize() call</li>
<li>Fix memory exception with checkerboard stereo</li>
<li>Add WindowStereoTypeChangedEvent fired by vtkRenderWindow</li>
</ul>
</li>
<li>
<p><strong>Rename QVTKOpenGLSimpleWidget to QVTKOpenGLNativeWidget</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4642/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4642/commits</a> (from <code>Jean-Christophe Fillion-Robin &lt;jcfr[at]kitware.com</code>&gt;)</p>
<p>Improve QVTKOpenGLWidget docstring</p>
</li>
<li>
<p><strong>vtkRenderer::PickProp: Fix crash handling empty selection</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4608/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4608/commits</a> (from <code>Jean-Christophe Fillion-Robin &lt;jcfr[at]kitware.com&gt;</code>)</p>
</li>
</ul>
<h2>Rendering:</h2>
<ul>
<li>
<p><strong>Add support for defining custom uniform variables</strong>. See <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4621">https://gitlab.kitware.com/vtk/vtk/merge_requests/4621</a><br>
Thanks: <code>Simon Drouin &lt;drouin.simon[at]gmail.com&gt;</code></p>
</li>
<li>
<p><strong>Fix issues with order independent translucency_fixes</strong> See <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4757">https://gitlab.kitware.com/vtk/vtk/merge_requests/4757</a><br>
Thanks: <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code></p>
</li>
<li>
<p><strong>Add ability to share data between render windows</strong><br>
<a href="https://github.com/Kitware/VTK/commit/363d99b">kitware/VTK@363d99b</a></p>
<p>This topic adds a capability to share some data between<br>
render windows. Basically it is implemented shared context<br>
data in OpenGL such as with wglShareLists or the similar<br>
functionality on glX or Cocoa. Right now only the VBO<br>
cache makes use of the shared space but in the future shader<br>
programs, textures, etc could also be shared.</p>
</li>
<li>
<p><strong>vtkOpenGLPolyDataMapper:limit timing calls to reasonable sized renders</strong><br>
<a href="https://github.com/Kitware/VTK/commit/f128754">kitware/VTK@f128754</a></p>
<p>The timing calls require a round trip to the driver<br>
which for many actors can be a significant cost. This<br>
change makes it so that for small datasets the timers<br>
are called less frequently but still at least once<br>
per hundred renders.</p>
</li>
<li>
<p><strong>vtkOpenGLRenderWindow: Improve error message reported when OpenGL is not supported.</strong><br>
<a href="https://github.com/Kitware/VTK/commit/51e0dc9">kitware/VTK@51e0dc9</a></p>
<p>Unable to find a valid OpenGL 3.2 or later implementation.<br>
Please update your video card driver to the latest version.<br>
If you are using Mesa please make sure you have version 11.2 or<br>
later and make sure your driver in Mesa supports OpenGL 3.2 such<br>
as llvmpipe or openswr. If you are on windows and using Microsoft<br>
remote desktop note that it only supports OpenGL 3.2 with nvidia<br>
quadro cards. You can use other remoting software such as nomachine<br>
to avoid this issue.</p>
<p>See <a href="https://issues.slicer.org/view.php?id=4252">https://issues.slicer.org/view.php?id=4252</a></p>
</li>
<li>
<p><strong>Add centralized lighting uniforms and benchmark</strong><br>
<a href="https://github.com/Kitware/VTK/commit/84e87cf">kitware/VTK@84e87cf</a></p>
<p>profiling has shown that a lot of time is spent in the<br>
mapper setting the lighting uniforms when there are a<br>
large number of mappers. In a more traidiotnal program<br>
this is handled by a UBO or similar set once per program.<br>
This topic addds in capability to the shader program<br>
to store an mtime associated with a group of uniforms.<br>
It also makes use of that capability by having the renderer<br>
generate shader code for the lights, and update the unifoms<br>
when requested and needed. The result is a significant reduction<br>
in the time spect updating the lights when faced with many mappers.</p>
<p>This topic also includes a new benchmark to test the performance<br>
of many actors.</p>
<p>This topic also includes a performance fix to short circuit<br>
the mtime check for RenderPasses in the mapper. The most common<br>
case is none and yet that case was taking significant time.</p>
</li>
<li>
<p><strong>OpenGL2: Check that context exists before trying to pop context.</strong><br>
<a href="https://github.com/Kitware/VTK/commit/a7988f5">kitware/VTK@a7988f5</a></p>
<p>On some linux drivers (such as nvidia version 384.111 and 387.34) setting the<br>
context to zero causes a segfault so check before setting in cases where the<br>
destruction may be trying to pop to a zero context.</p>
</li>
</ul>
<h2>Volume Rendering Fixes</h2>
<ul>
<li>
<p><strong>Fix volume clip bug and add regression test.</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4338/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4338/commits</a> (from <code>Allison Vacanti &lt;allison.vacanti[at]kitware.com&gt;</code>)</p>
<p>When clipping a volume using in-shader clipping planes, it was possible for the starting point of the ray cast to<br>
lie beyond the data volume. The raycast code is written such that the first sample is always taken before testing<br>
termination criteria, and in these cases we would always take a single sample outside of the volume, leading to<br>
artifacts.</p>
<p>Fixed this behavior by checking that the starting position calculated by AdjustSampleRangeForClipping is indeed<br>
inside of the volume bounds and aborting the raycast if it is not.</p>
<p>The existing TestGPURayCastClipping test would have caught this, except that the vase.vti volume used for testing<br>
has all 0’s at the boundaries, so the rendering was correct even with the edge-clamp repetition outside of the volume<br>
(the faulty samples always computed RGBA=vec4(0)). I replaced the vase.vti of this test with a wavelet with finite<br>
boundary values that will catch this problem if there’s a regression.</p>
</li>
<li>
<p><strong>Fix box widget face highlighting.</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4573/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4573/commits</a> (from <code>Allison Vacanti &lt;allison.vacanti[at]kitware.com&gt;</code>)</p>
<p>The actual data was updated correctly in the BoxWidget<br>
code, but the wrong object was being marked as modified.</p>
<p>The rendering code got smarter at some point and now<br>
only rebuilds VBOs when the corresponding cell array<br>
has been modified. Marking the entire polydata as modified<br>
is no longer sufficient to update the on-device<br>
representation of the highlighted face.</p>
<p>This patch fixes the BoxWidget so that the active face is<br>
used for highlighting instead of getting “stuck” on an<br>
arbitrary face.</p>
</li>
<li>
<p><strong>Volume peel widget flicker</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4568">https://gitlab.kitware.com/vtk/vtk/merge_requests/4568</a> (from <code>Allison Vacanti &lt;allison.vacanti[at]kitware.com&gt;</code>)</p>
<p>Correctly apply jittering in ClampToSampleLocation. We were reapplying it inconsistently in the DDP. This<br>
pass was updated also.</p>
<p>Rearrange cast initialization code in DDP. The start point was adjusted for clipping <em>after</em> clamping<br>
to a sample position. This would move the effective sample positions to an inconsistent locations if clipping planes<br>
were present.</p>
</li>
<li>
<p><strong>Introduce volume API to specify intensity for clipped voxels</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4627">https://gitlab.kitware.com/vtk/vtk/merge_requests/4627</a> (from <code>Sankhesh Jhaveri &lt;sankhesh.jhaveri[at]kitware.com&gt;</code>)</p>
<p>See <a href="https://issues.slicer.org/view.php?id=4513">Slicer issue 4513</a></p>
<p>Specifying a fixed intensity value for voxels in clipped space provides<br>
the ability to change lighting computations at the clipped face.</p>
</li>
<li>
<p><strong>VolumeMapper: Invoke update shader event each frame</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4614">https://gitlab.kitware.com/vtk/vtk/merge_requests/4614</a> (from <code>Sankhesh Jhaveri &lt;sankhesh.jhaveri[at]kitware.com&gt;</code>)</p>
<p>This allows applications to modify uniforms on the dynamically created and compiled shader program.</p>
</li>
<li>
<p><strong>Fix volume clip bug and add regression test.</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4338/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4338/commits</a> (from <code>Allison Vacanti &lt;allison.vacanti[at]kitware.com&gt;</code>)</p>
<p>When clipping a volume using in-shader clipping planes, it was possible for the starting point of the ray cast to<br>
lie beyond the data volume. The raycast code is written such that the first sample is always taken before testing<br>
termination criteria, and in these cases we would always take a single sample outside of the volume, leading to<br>
artifacts.</p>
<p>Fixed this behavior by checking that the starting position calculated by AdjustSampleRangeForClipping is indeed<br>
inside of the volume bounds and aborting the raycast if it is not.</p>
<p>The existing TestGPURayCastClipping test would have caught this, except that the vase.vti volume used for testing<br>
has all 0’s at the boundaries, so the rendering was correct even with the edge-clamp repetition outside of the volume<br>
(the faulty samples always computed RGBA=vec4(0)). I replaced the vase.vti of this test with a wavelet with finite<br>
boundary values that will catch this problem if there’s a regression.</p>
</li>
<li>
<p><strong>Fix box widget face highlighting.</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4573/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4573/commits</a> (from <code>Allison Vacanti &lt;allison.vacanti[at]kitware.com&gt;</code>)</p>
<p>The actual data was updated correctly in the BoxWidget<br>
code, but the wrong object was being marked as modified.</p>
<p>The rendering code got smarter at some point and now<br>
only rebuilds VBOs when the corresponding cell array<br>
has been modified. Marking the entire polydata as modified<br>
is no longer sufficient to update the on-device<br>
representation of the highlighted face.</p>
<p>This patch fixes the BoxWidget so that the active face is<br>
used for highlighting instead of getting “stuck” on an<br>
arbitrary face.</p>
</li>
<li>
<p><strong>Refactor in-shader volume clipping to be depth-peeling-friendly.</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4071/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4071/commits</a> (from <code>Allison Vacanti &lt;allison.vacanti[at]kitware.com&gt;</code>)</p>
<p>Refactor the volume clipping code so that it is compatible with the volume peeling<br>
implementation in vtkDualDepthPeelingPass. At a high level, the new version adjusts<br>
the sampling ray so that it won’t sample clipped areas, rather than check for clipping<br>
at each sample location.</p>
<p>This should give better performance (less work during casting) and allows the clip<br>
calculations to be aware of the depth-peeling sample range.</p>
<p><a href="https://github.com/Kitware/VTK/commit/11c0ccc">kitware/vtk@11c0ccc</a> (Fix early termination criteria in volume peeler)<br>
<a href="https://github.com/Kitware/VTK/commit/410f979">kitware/vtk@410f979</a> (Ensure that the dual depth peeling algorithm samples consistently)<br>
<a href="https://github.com/Kitware/VTK/commit/f144205">kitware/vtk@f144205</a> (Refactor in-shader volume clipping to be depth-peeling-friendly)</p>
<p>Slicer: Fix <a href="https://issues.slicer.org/view.php?id=4510">issue 4510</a>: VTK OpenGL2 Backend: Cropping is broken with GPU Volume rendering<br>
if depth peeling is enabled.<br>
See <a href="https://issues.slicer.org/view.php?id=4510">https://issues.slicer.org/view.php?id=4510</a></p>
</li>
</ul>
<h2>Widgets</h2>
<ul>
<li>
<p><strong>Invoke DeletePointEvent before deleting vtkSeedWidget seed</strong><br>
<a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4493/commits">https://gitlab.kitware.com/vtk/vtk/merge_requests/4493/commits</a> (from <code>Sankhesh Jhaveri &lt;sankhesh.jhaveri[at]kitware.com&gt;</code>)</p>
</li>
<li>
<p><strong>Fix picking through a disabled widget with picking manager on</strong><br>
<a href="https://github.com/Kitware/VTK/commit/8e4f2f7">kitware/VTK@8e4f2f7</a> (from <code>Johan Andruejol &lt;johan.andruejol[at]kitware.com&gt;</code>)</p>
<p>With picking manager on, it was impossible to pick a widget if a disabled<br>
widget was in front of it.<br>
To fix this, we have:<br>
- In the old style widgets (derived only from vtkInteractorObserver), we<br>
went through all the implementation and added the unregistration/registration<br>
of the pickers in the SetEnabled() method.</p>
<ul>
<li>In new style widgets (derived from vtkAbstractWidget and<br>
vtkWidgetRepresentation) the method RegisterPickers and UnRegisterPickers<br>
have been moved into the representation public API to be able to be called<br>
by the widget’s SetEnabled() method. This allows the widget to register and<br>
unregisters the pickers as necessary when enabled and disabled.</li>
</ul>
<p>In both cases we also implemented the SetPickingManaged method as previously<br>
the PickingManaged property was never used anywhere in the code base.<br>
Similarly, the PickersModified() method was removed as its purpose seemed<br>
redundant to SetPickingManaged().</p>
<p>The test TestPickingManagerSeedWidget2 was added to demonstrate/test the<br>
picking behind a disabled widget.</p>
<p>For more background information, see <a href="https://issues.slicer.org/view.php?id=3808">https://issues.slicer.org/view.php?id=3808</a></p>
<p>Co-Authored-by: <code>Ken Martin &lt;ken.martin[at]kitware.com&gt;</code><br>
Co-Authored-by: <code>Jean-Christophe Fillion-Robin &lt;jchris.fillionr[at]kitware.com&gt;</code><br>
Thanks: <code>Steve Pieper &lt;pieper[at]bwh.harvard.edu&gt;</code></p>
<p>Slicer: Allow to remove workaround and Slicer/VTK specific patch associated with <a href="https://issues.slicer.org/view.php?id=3808">Slicer issue #3808</a></p>
</li>
<li>
<p><strong>BUG: Uniformize RegisterPickers() method</strong><br>
<a href="https://github.com/Kitware/VTK/commit/fc043da5b">kitware/vtk@fc043da5b</a> (from <code>Johan Andruejol &lt;johan.andruejol[at]kitware.com&gt;</code>)</p>
<p>Uniformize the RegisterPickers() method across all the widgets to make sure<br>
to check for the validity of the picking manager.<br>
This completes the work started in 8e4f2f7c.</p>
<p>Slicer: Follow up of <a href="https://issues.slicer.org/view.php?id=3808">issue #3808</a><br>
See <a href="https://issues.slicer.org/view.php?id=3808">https://issues.slicer.org/view.php?id=3808</a></p>
</li>
</ul>

---
