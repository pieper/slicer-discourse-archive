---
topic_id: 13284
title: "Way To Create Permanent Slice Intersection"
date: 2020-09-01
url: https://discourse.slicer.org/t/13284
---

# Way to create permanent slice intersection

**Topic ID**: 13284
**Date**: 2020-09-01
**URL**: https://discourse.slicer.org/t/way-to-create-permanent-slice-intersection/13284

---

## Post #1 by @Jakew (2020-09-01 21:02 UTC)

<p>when slice intersection is enabled, the user can see a line that indicates where the slice they are currently viewing is relative to the other views. I was wondering if there was a way to create a static line for a certain slice (i.e. create a line in the sagittal and coronal views indicating where the a specific axial slice is located, so it doesn’t change no matter what slice is currently in the axial view).</p>

---

## Post #2 by @lassoan (2020-09-01 23:20 UTC)

<p>You can create a markups plane node (or a model node with a plane in it) at the desired position and enable 2D display to show its intersection line in slice views.</p>
<p>There are many other ways to do this, depending on what you would like to achieve. Can you write a bit more about your application?</p>

---

## Post #3 by @Jakew (2020-09-01 23:26 UTC)

<p>This goal of this feature is basically so if the user has an axial and sagittal view open, the user can click a button with a specific slice open on the axial view and it would be “marked” on the sagittal view, i.e. if the user scrolls away from the that slice, they can tell exactly where the marked scan is by scrolling back to that line in the sagittal view.</p>

---

## Post #4 by @lassoan (2020-09-01 23:35 UTC)

<p>To mark a point, you can also use markup fiducial points. It not just remembers a slice but a 3D position. You can jumpy to slice by clicking on the fiducial in the control point list (in Markups module) or in any views (you need to enable 2D projection to make the point show up in all slices).</p>
<p>Alternatively, you can choose view layouts with a couple of extra views (if you want to keep showing the reference planes to the user).</p>

---

## Post #5 by @Jakew (2020-09-02 21:39 UTC)

<p>Is it possible to call functions in the vtkSlicerMarkupsLogic and vtkMRMLMarkupsLineNode classes in a different module? I’m not sure if my implementation is incorrect or something else is going wrong.</p>

---

## Post #6 by @lassoan (2020-09-02 22:53 UTC)

<p>Yes, you can call methods of MRML nodes and module logic classes from any modules. If you write us the error messages that you get then we can tell what is missing.</p>

---

## Post #7 by @Jakew (2020-09-02 23:04 UTC)

<p>Right now my issue is that despite including the vtkSlicerMarkupsLogic.h file in an <span class="hashtag">#include</span> line, I’m getting an “undefined reference to [function]” error whenever I try to use any of the functions in the class.</p>

---

## Post #8 by @lassoan (2020-09-03 00:03 UTC)

<p>Please provide the entire error message.</p>

---

## Post #9 by @Jakew (2020-09-03 00:26 UTC)

<p>This is what I’ve done:</p>
<pre><code>vtkSlicerMarkupsLogic* markupLogic = vtkSlicerMarkupsLogic::SafeDownCast(qSlicerApplication::application()-&gt;applicationLogic());
vtkMRMLNode *markupsNode = qSlicerApplication::application()-&gt;mrmlScene()-&gt;AddNewNodeByClass("vtkMRMLMarkupsLineNode");
markupLogic-&gt;AddNewDisplayNodeForMarkupsNode(markupsNode);
</code></pre>
<p>The error I got was: “undefined reference to `vtkSlicerMarkupsLogic::AddNewDisplayNodeForMarkupsNode [abi:cxx11] (vtkMRMLNode*) '”</p>

---

## Post #10 by @lassoan (2020-09-03 02:40 UTC)

<p>Adding <code>#include "vtkSlicerMarkupsLogic.h"</code> fixes undefined reference to <code>vtkSlicerMarkupsLogic::AddNewDisplayNodeForMarkupsNode</code>. If not, then most likely your compiler threw an error before that it could not find <code>vtkSlicerMarkupsLogic.h</code>. You always need to fix the very first error the compiler reports because subsequent errors may be result of previous ones.</p>
<p>There are several examples of using markups from C++ modules, for example in <a href="https://github.com/SlicerIGT/SlicerIGT/">SlicerIGT extension</a>.</p>

---

## Post #11 by @Jakew (2020-09-03 17:08 UTC)

<p>That’s the strange part, I have the <span class="hashtag">#include</span> line and this error is the only error the compiler throws. I’ll keep investigating then, thanks!</p>

---

## Post #12 by @lassoan (2020-09-03 17:52 UTC)

<p>If you send a link to your source code repository then I can take a look.</p>

---

## Post #13 by @Suhaim (2025-07-16 06:08 UTC)

<p>Hi <a class="mention" href="/u/jakew">@Jakew</a> , were you able to solve this issue?</p>

---

## Post #14 by @Suhaim (2025-07-16 07:04 UTC)

<p>For me the error arised in the linking stage, the linker was not able to find the source code even though compilation worked due to the headers being found. I modified the CMakeLists.txt of the component that was looking for the logic component of the module in use(Markups in your case).</p>
<p>My module’s logic component needed vtkSlicerReformatModuleLogic, so adding it to the components to be linked(TARGET_LIBRARIES) worked. Hope this helps, thanks!</p>
<pre><code class="lang-auto">project(vtkSlicer${MODULE_NAME}ModuleLogic)

set(KIT ${PROJECT_NAME})

set(${KIT}_EXPORT_DIRECTIVE "VTK_SLICER_${MODULE_NAME_UPPER}_MODULE_LOGIC_EXPORT")

set(${KIT}_INCLUDE_DIRECTORIES
  )

set(${KIT}_SRCS
  vtkSlicer${MODULE_NAME}Logic.cxx
  vtkSlicer${MODULE_NAME}Logic.h
  )

set(${KIT}_TARGET_LIBRARIES
  ${ITK_LIBRARIES}
  vtkSlicerReformatModuleLogic
)

#-----------------------------------------------------------------------------
SlicerMacroBuildModuleLogic(
  NAME ${KIT}
  EXPORT_DIRECTIVE ${${KIT}_EXPORT_DIRECTIVE}
  INCLUDE_DIRECTORIES ${${KIT}_INCLUDE_DIRECTORIES}
  SRCS ${${KIT}_SRCS}
  TARGET_LIBRARIES ${${KIT}_TARGET_LIBRARIES}
  )

</code></pre>

---
