# Custom mouse interaction with model node

**Topic ID**: 33264
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/custom-mouse-interaction-with-model-node/33264

---

## Post #1 by @drouin-simon (2023-12-06 20:13 UTC)

<p>I’m trying to implement a custom mouse-based interaction mechanism to move/rotate a model node in the 3D view (scripted module). I want a different interaction than the one provided by the transform node widget. For example, I would like the user to be able to press the left mouse button to “pick” a model and then rotate the model around the picked point by moving the mouse.</p>
<p>Is there a simple way to override the interactor style of the 3D view without breaking anything else? I see many posts suggesting to create temporary markups to do similar things, but it seems overkill and I’m thinking there must be a simpler way.</p>

---

## Post #2 by @jcfr (2023-12-06 20:31 UTC)

<p>For context, the interactions associated with widget like the “CameraWidget” ones are currently hard-coded in the associated constructor<sup class="footnote-ref"><a href="#footnote-104349-1" id="footnote-ref-104349-1">[1]</a></sup> by mapping event to specific actions with calls to functions like:</p>
<ul>
<li><code>SetKeyboardEventTranslation</code></li>
<li><code>SetEventTranslationClickAndDrag</code></li>
</ul>
<p>This concept is applied to all the other widgets<sup class="footnote-ref"><a href="#footnote-104349-2" id="footnote-ref-104349-2">[2]</a></sup> used to update properties of various object.</p>
<blockquote>
<p>to override the interactor style of the 3D view without breaking anything else?</p>
</blockquote>
<p>To override the mapping describe above, we would need to redefine the mapping. This could be done either globally (or an a per-context basis).</p>
<p>For reference, the segment editor is handling this in a ad-hoc way through the <code>qMRMLSegmentEditorWidget::setupViewObservations</code><sup class="footnote-ref"><a href="#footnote-104349-3" id="footnote-ref-104349-3">[3]</a></sup></p>
<p>Waiting we further improve the framework, addressing what you are describing by relying on existing capabilities (e.g markups) is sensible.</p>
<p>The <a href="https://github.com/KitwareMedical/SlicerMarkupConstraints">SlicerMarkupConstraints</a> may also provide some useful concept we could integrate into Slicer core.</p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/allemangd">@allemangd</a></p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-104349-1" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/d3698410865fe2dba7235703aff08748fcf94410/Libs/MRML/DisplayableManager/vtkMRMLCameraWidget.cxx#L113-L133">https://github.com/Slicer/Slicer/blob/d3698410865fe2dba7235703aff08748fcf94410/Libs/MRML/DisplayableManager/vtkMRMLCameraWidget.cxx#L113-L133</a> <a href="#footnote-ref-104349-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-104349-2" class="footnote-item"><p><a href="https://github.com/search?type=code&amp;q=repo%3ASlicer%2FSlicer+-%3ESetEventTranslationClickAndDrag">https://github.com/search?type=code&amp;q=repo%3ASlicer%2FSlicer+-&gt;SetEventTranslationClickAndDrag</a> <a href="#footnote-ref-104349-2" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-104349-3" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/d3698410865fe2dba7235703aff08748fcf94410/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L2620">https://github.com/Slicer/Slicer/blob/d3698410865fe2dba7235703aff08748fcf94410/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L2620</a> <a href="#footnote-ref-104349-3" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #3 by @lassoan (2023-12-06 21:25 UTC)

<p>Default translation from interaction even to widget action is defined in each widget, but you are free to remove those and/or add new translations, as shown in examples in the script repository.</p>
<p>The current transformation widget is very limited and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is working on a much better widget that will replace it, which works in both 3D and slice views, has adjustable center of rotation, allows translation/rotation around a single axis, supports non-linear transform hiearchies, etc. At the project week Kyle could work with you to refine the widget in a way that it fulfills your requirements. He also has a prototype on node focus: allow picking a node (such as a model) in 3D/slice views or in subject hierarchy widgets by clicking on it and then interact with it (e.g., show interaction handles to translate/rotate).</p>
<aside class="quote no-group" data-username="drouin-simon" data-post="1" data-topic="33264">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drouin-simon/48/258_2.png" class="avatar"> drouin-simon:</div>
<blockquote>
<p>Is there a simple way to override the interactor style of the 3D view without breaking anything else? I see many posts suggesting to create temporary markups to do similar things, but it seems overkill and I’m thinking there must be a simpler way.</p>
</blockquote>
</aside>
<p>You can of course override the entire event translation infrastructure, as it is done in the Segment Editor, but I would not recommend it, as it can have many unintended side-effects (e.g., interactive slice intersections are not compatible with Segment Editor). At some point the Segment Editor will be fixed to use the proper event translation mechanism.</p>

---

## Post #4 by @jcfr (2023-12-06 21:41 UTC)

<blockquote>
<p>[…] are free to remove those and/or add new translations, as shown in examples in the script repository</p>
</blockquote>
<p>For reference, see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-mouse-gestures-in-viewers">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-mouse-gestures-in-viewers</a></p>
<p>In the script repository linked here, you can see that reference to widgets like the ones mentioned above are retrieved and then calls to <code>SetKeyboardEventTranslation</code> and <code>SetEventTranslationClickAndDrag</code> are done to customize the behavior.</p>

---
