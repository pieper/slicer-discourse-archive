---
topic_id: 33977
title: "Add Vtkvectortext Programmatically"
date: 2024-01-25
url: https://discourse.slicer.org/t/33977
---

# Add vtkVectorText programmatically

**Topic ID**: 33977
**Date**: 2024-01-25
**URL**: https://discourse.slicer.org/t/add-vtkvectortext-programmatically/33977

---

## Post #1 by @Jeff_Zeyl (2024-01-25 18:29 UTC)

<p>I would like to engrave many text models onto a skin model, programmatically, based on a set of markup control point coordinates.</p>
<p>My current approach is to generate vtk.vtkVectorText models, set their location, and subtract the text and skin models. I have successfully loaded vtk model, but vtk.vtkVectorText doesn’t have a set center method (like some other vtk model types types) but rather position is set by a vtkActor. If I understand correctly, in Slicer vtkPolyDataActor and vtkPolyDataMapper are tied into Displayable Managers (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DisplayableManagers" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/DisplayableManagers - Slicer Wiki</a>) but don’t see relevant methods to set position.</p>
<p>How can i set the position of a model vtkVectorText inside slicer, which would otherwise be controlled by vtkActor outside of the Slicer environment?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/889a4bafe4c1734a296ce66d632b677b1af07959.png" data-download-href="/uploads/short-url/jurvNyBerSEMiCmN7a8ySd0aSF3.png?dl=1" title="vectortext" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/889a4bafe4c1734a296ce66d632b677b1af07959_2_690x369.png" alt="vectortext" data-base62-sha1="jurvNyBerSEMiCmN7a8ySd0aSF3" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/889a4bafe4c1734a296ce66d632b677b1af07959_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/889a4bafe4c1734a296ce66d632b677b1af07959_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/889a4bafe4c1734a296ce66d632b677b1af07959.png 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vectortext</span><span class="informations">1366×731 57.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-01-25 18:31 UTC)

<p>Did you look at this? <a href="https://discourse.slicer.org/t/new-text-engrave-emboss-effect-in-segment-editor/12013" class="inline-onebox">New text engrave/emboss effect in Segment Editor</a></p>

---

## Post #3 by @Jeff_Zeyl (2024-01-25 18:54 UTC)

<p>I have tried the effect but encountered the unclear text issue noted on the same discussion thread (I have not yet followed through with changing volume spacing to make the text clearer).</p>
<p>In terms of programmatic placement of position, the lines in the link below could then potentially be modified?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngrave.py#L99-L122">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngrave.py#L99-L122" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngrave.py#L99-L122" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngrave.py#L99-L122</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="99" style="counter-reset: li-counter 98 ;">
          <li># effect.self().fiducialPlacementToggle.placeButton().click()</li>
          <li></li>
          <li># points =[[2.589283578714074, 44.60536690073953, 27.299999999999997], [8.515228351086698, 35.22262101114956, 27.299999999999997],</li>
          <li>#          [13.700430026912741, 25.099132025013006, 27.299999999999997], [5.799170330415919, 19.17318725264039, 27.299999999999997],</li>
          <li>#          [2.589283578714074, 9.296612632019361, 27.299999999999997], [-10.250263428093263, 12.25958501820567, 27.299999999999997],</li>
          <li>#          [-16.17620820046588, 18.185529790578286, 27.299999999999997], [-20.373752414229813, 27.568275680168263, 27.299999999999997],</li>
          <li>#          [-15.929293834950343, 38.679422128366916, 27.299999999999997], [-11.484835255670887, 44.11153816970849, 27.299999999999997],</li>
          <li>#          [6.539913426962492, 33.49422045254088, 31.499999999999993], [1.354711751136449, 42.383137611099805, 31.499999999999993],</li>
          <li>#          [-8.768777235000101, 44.35845253522401, 31.499999999999993], [-14.200893276341674, 36.70410720424271, 31.499999999999993],</li>
          <li>#          [-18.398437490105607, 27.07444694913721, 31.499999999999993], [-12.719407083248512, 16.704043597485132, 31.499999999999993],</li>
          <li>#          [-7.534205407422476, 11.765756287174618, 31.499999999999993], [0.12013992355882408, 12.25958501820567, 31.499999999999993],</li>
          <li>#          [5.799170330415919, 16.21021486645408, 31.499999999999993], [8.268313985571176, 21.642330907795646, 31.499999999999993],</li>
          <li>#          [13.947344392428263, 26.827532583621682, 31.499999999999993], [-3.0897468281430065, 32.50656299047878, 45.49999999999998],</li>
          <li>#          [2.589283578714074, 27.32136131465274, 45.49999999999998], [-5.3119761177827485, 21.642330907795646, 45.49999999999998],</li>
          <li>#          [-8.02803413845352, 27.32136131465274, 45.49999999999998], [-14.694722007372718, 30.778162431870093, 38.499999999999986],</li>
          <li>#          [-8.02803413845352, 12.01267065269014, 38.499999999999986], [-3.583575559174065, 39.66707959042902, 11.900000000000007],</li>
          <li>#          [3.576941040776184, 31.765819893932196, 11.900000000000007], [0.12013992355882408, 20.901587811249065, 11.900000000000007],</li>
          <li>#          [-9.26260596603116, 28.555933142230366, 11.900000000000007], [6.046084695931441, 38.432507762851394, 17.500000000000007],</li>
          <li>#          [-17.163865662527982, 33.7411348180564, 17.500000000000007], [-14.200893276341674, 21.889245273311168, 17.500000000000007]]</li>
          <li></li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngrave.py#L99-L122" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @pieper (2024-01-25 19:20 UTC)

<p>You could have a look at how the effect is implemented using VTK:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngraveLib/SegmentEditorEffect.py#L537">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngraveLib/SegmentEditorEffect.py#L537" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngraveLib/SegmentEditorEffect.py#L537" target="_blank" rel="noopener">lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngraveLib/SegmentEditorEffect.py#L537</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="527" style="counter-reset: li-counter 526 ;">
          <li>
</li>
          <li>  # Need to pause render, to prevent rendering pipeline updates during DeepCopy.
</li>
          <li>  # (Details: During deepcopy, Modified() is called before the copy is fully completed,
</li>
          <li>  # which can trigger a rendering pipeline update. During that update, the
</li>
          <li>  # polydata that is still in inconsistent state is used, which can cause
</li>
          <li>  # application crash.)
</li>
          <li>  slicer.app.pauseRender()
</li>
          <li>  outputModel.GetPolyData().DeepCopy(self.extrusion.GetOutput())
</li>
          <li>  slicer.app.resumeRender()
</li>
          <li>
</li>
          <li class="selected">def apply(self, segmentMarkupNode, segmentModel, text, textDepth, mode):
</li>
          <li>
</li>
          <li>  self.updateModel(segmentMarkupNode, segmentModel, text, textDepth)
</li>
          <li>
</li>
          <li>  import vtkSegmentationCore
</li>
          <li>
</li>
          <li>  if not segmentMarkupNode:
</li>
          <li>    raise AttributeError(f"{self.__class__.__name__}: segment markup node not set.")
</li>
          <li>  if not segmentModel:
</li>
          <li>    raise AttributeError(f"{self.__class__.__name__}: segment model not set.")
</li>
          <li>
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Jeff_Zeyl (2024-05-08 19:48 UTC)

<p>Thank you. I was able to reproduce the segmentation effect so that my text labels can engrave or emboss at specific coordinates. However, when plugging in the arguments into the apply function, the letters engrave upside down relative to the default ‘Test’ text in the GUI, even if I apply a transform to the associated segment model, flipping it 180 degrees. Any idea where this transform is getting applied?</p>
<p>here?: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/f43df35af66a0b60000b008e0fa061d53319dc78/SegmentEditorEngrave/SegmentEditorEngraveLib/SegmentEditorEffect.py#L511" class="inline-onebox" rel="noopener nofollow ugc">SlicerSegmentEditorExtraEffects/SegmentEditorEngrave/SegmentEditorEngraveLib/SegmentEditorEffect.py at f43df35af66a0b60000b008e0fa061d53319dc78 · lassoan/SlicerSegmentEditorExtraEffects · GitHub</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2e1088f75df237a46817889fbee4fb19bd60353.png" data-download-href="/uploads/short-url/u5woQlkD9H6pvNVnNyk2tiZxppp.png?dl=1" title="inversion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2e1088f75df237a46817889fbee4fb19bd60353_2_690x312.png" alt="inversion" data-base62-sha1="u5woQlkD9H6pvNVnNyk2tiZxppp" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2e1088f75df237a46817889fbee4fb19bd60353_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2e1088f75df237a46817889fbee4fb19bd60353_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2e1088f75df237a46817889fbee4fb19bd60353.png 2x" data-dominant-color="55684F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">inversion</span><span class="informations">1276×578 93.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
