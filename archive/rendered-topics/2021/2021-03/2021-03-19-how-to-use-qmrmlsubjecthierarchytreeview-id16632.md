# How to use qMRMLSubjectHierarchyTreeView

**Topic ID**: 16632
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/how-to-use-qmrmlsubjecthierarchytreeview/16632

---

## Post #1 by @kejuhn (2021-03-19 08:59 UTC)

<p>I create an extension, and add a loadable module “PluginA”.<br>
In default UI, I add a qMRMLSubjectHierarchyTreeView by Qt Designer.<br>
After build extension in Visual Studio, several errors occurred.<br>
‘qMRMLSubjectHierarchyTreeView.h’: No such file or directory in ui_qSlicerPluginAModuleWidget.h<br>
Are there any settings missing?<br>
How to solve this error, Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a3f638fbfd8ea0a50aeb21d0eade8da5f4f6b7b.png" data-download-href="/uploads/short-url/3KcdUoOv6GLUStziMV1u209Orzl.png?dl=1" title="2021-03-19 16 34 32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a3f638fbfd8ea0a50aeb21d0eade8da5f4f6b7b_2_690x373.png" alt="2021-03-19 16 34 32" data-base62-sha1="3KcdUoOv6GLUStziMV1u209Orzl" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a3f638fbfd8ea0a50aeb21d0eade8da5f4f6b7b_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a3f638fbfd8ea0a50aeb21d0eade8da5f4f6b7b_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a3f638fbfd8ea0a50aeb21d0eade8da5f4f6b7b_2_1380x746.png 2x" data-dominant-color="C6C6C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-03-19 16 34 32</span><span class="informations">1920×1040 59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cf34bf9dcb6f26812dc5495819a985b8c1fc116.png" data-download-href="/uploads/short-url/k6U6CAuOIRlGzzwdkNcLN1vLJSS.png?dl=1" title="2021-03-19 16 34 16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cf34bf9dcb6f26812dc5495819a985b8c1fc116_2_690x375.png" alt="2021-03-19 16 34 16" data-base62-sha1="k6U6CAuOIRlGzzwdkNcLN1vLJSS" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cf34bf9dcb6f26812dc5495819a985b8c1fc116_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cf34bf9dcb6f26812dc5495819a985b8c1fc116_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cf34bf9dcb6f26812dc5495819a985b8c1fc116_2_1380x750.png 2x" data-dominant-color="282B2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-03-19 16 34 16</span><span class="informations">1912×1040 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2021-03-19 09:33 UTC)

<p>The error is probably due to the fact that the necessary include directories are not added in the <code>CMakeLists.txt</code> file. See examples in the Slicer source code, for example:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Data/CMakeLists.txt#L20">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Data/CMakeLists.txt#L20" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Data/CMakeLists.txt#L20" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Loadable/Data/CMakeLists.txt#L20</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="10" style="counter-reset: li-counter 9 ;">
          <li>#-----------------------------------------------------------------------------</li>
          <li>set(MODULE_EXPORT_DIRECTIVE "Q_SLICER_QTMODULES_${MODULE_NAME_UPPER}_EXPORT")</li>
          <li></li>
          <li># Additional includes - Current_{source,binary} and Slicer_{Libs,Base} already included</li>
          <li>set(MODULE_INCLUDE_DIRECTORIES</li>
          <li>  ${CMAKE_CURRENT_SOURCE_DIR}/Logic</li>
          <li>  ${CMAKE_CURRENT_BINARY_DIR}/Logic</li>
          <li>  ${vtkSlicerCamerasModuleLogic_SOURCE_DIR}</li>
          <li>  ${vtkSlicerCamerasModuleLogic_BINARY_DIR}</li>
          <li>  ${qSlicerSubjectHierarchyModuleWidgets_INCLUDE_DIRS}</li>
          <li class="selected">  ${qMRMLWidgets_INCLUDE_DIRS}</li>
          <li>  )</li>
          <li></li>
          <li>set(MODULE_SRCS</li>
          <li>  qSlicer${MODULE_NAME}Module.cxx</li>
          <li>  qSlicer${MODULE_NAME}Module.h</li>
          <li>  qSlicer${MODULE_NAME}ModuleWidget.cxx</li>
          <li>  qSlicer${MODULE_NAME}ModuleWidget.h</li>
          <li>  qSlicerSceneIOOptionsWidget.cxx</li>
          <li>  qSlicerSceneIOOptionsWidget.h</li>
          <li>  qSlicerSceneReader.cxx</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also just to prevent further surprises any MRML object, including the SH tree view, needs to be connected in Designer to the mrmlSceneChanged event, like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a13afed7bc68d00b8abb6e3e58f3c50aae1e264.png" data-download-href="/uploads/short-url/1r8XaBTzDmpuNwxzONdhrOBb69C.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a13afed7bc68d00b8abb6e3e58f3c50aae1e264_2_690x431.png" alt="image" data-base62-sha1="1r8XaBTzDmpuNwxzONdhrOBb69C" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a13afed7bc68d00b8abb6e3e58f3c50aae1e264_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a13afed7bc68d00b8abb6e3e58f3c50aae1e264_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a13afed7bc68d00b8abb6e3e58f3c50aae1e264_2_1380x862.png 2x" data-dominant-color="DDDAD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1663×1041 93.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(you can get to signal/slot mode by pressing F4)</p>
<p>In general, as suggested by the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Loadable_Modules">guide</a>, it is a good idea to take existing Slicer modules as example when developing a new one.</p>

---

## Post #3 by @cpinter (2022-09-02 10:01 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/qmrmlsubjecthierarchytreeview-vs2022-error-lnk2019/25021/3">qMRMLSubjectHierarchyTreeView vs2022 error LNK2019</a></p>

---
