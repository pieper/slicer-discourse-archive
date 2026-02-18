# Minimal draw tube effect

**Topic ID**: 32511
**Date**: 2023-10-31
**URL**: https://discourse.slicer.org/t/minimal-draw-tube-effect/32511

---

## Post #1 by @mau_igna_06 (2023-10-31 18:23 UTC)

<p>Hi</p>
<p>I have a side panel with two widgets laid out vertically: first one is a groupbox to execute simplified segmentation actions by using the second widget, a qMRMLSegmentEditorWidget, that’s hidden.</p>
<p>I have to use the drawTubeEffect from the 2nd widget (only the buttons inside red marks):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2487721cdd2e42a07c7d33686566863b3ebdede9.jpeg" data-download-href="/uploads/short-url/5d9nzc471R9npg0SC9Lv2q6n5e9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2487721cdd2e42a07c7d33686566863b3ebdede9_2_690x365.jpeg" alt="image" data-base62-sha1="5d9nzc471R9npg0SC9Lv2q6n5e9" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2487721cdd2e42a07c7d33686566863b3ebdede9_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2487721cdd2e42a07c7d33686566863b3ebdede9_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2487721cdd2e42a07c7d33686566863b3ebdede9_2_1380x730.jpeg 2x" data-dominant-color="636368"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1016 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’d like to move the widgets in red to my firstly mentioned widget to keep all connections/logic working.</p>
<p>And I’d like to avoid duplicating the GUI of the segment editor widget inside the first widget to achieve that (but I’ll do it if there is not a simpler way to get it working)</p>
<p>Could you advice? Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2023-10-31 19:47 UTC)

<p>Widgets are not guaranteed to work if they are extracted from the widget that is managing them. Developers of all the reusable high-level widgets assume that the internal widgets are only accessed and displayed through the public API that the widgets provides, otherwise they would never know what they can change in their implementation.</p>
<p>I would recommend to add whatever widgets you need to your own module. Code duplication should be minimal, because you only need to add a markup place widget and a push-button. If you find that you need to add more than a couple of lines of code then you can suggest changes to refactor the Draw Tube effect that avoids any need for substantial code duplication.</p>

---

## Post #3 by @chir.set (2023-10-31 20:23 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="32511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>move the widgets in red</p>
</blockquote>
</aside>
<p>This concerns the default segment editor widget as a suggestion, yours is hidden, but it is the same widget class.</p>
<p>The ‘place fiducial’ widget may be obtained thus:</p>
<pre><code class="lang-auto">sew = slicer.modules.SegmentEditorWidget.editor
sew.setActiveEffectByName("Draw tube")
dt = sew.activeEffect()
fpt = dt.self().fiducialPlacementToggle
</code></pre>
<p>On a quick try, it seems to work more or less when reparented:</p>
<p><code>fpt.setParent(MyContainerWidget)</code></p>
<p>If the segment editor is  next shown and the ‘Draw tube’ effect is activated with the mouse, then the scene of the re-parented point placement widget needs to be set again. But yours is private and hidden.</p>
<p>All this may just worth a try, may be it’s too much of an ugly hack as <a class="mention" href="/u/lassoan">@lassoan</a> advised.</p>
<p>Regards.</p>

---

## Post #4 by @mau_igna_06 (2023-10-31 20:59 UTC)

<p>Thanks for your answer</p>

---

## Post #5 by @mau_igna_06 (2023-10-31 21:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="32511">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Code duplication should be minimal, because you only need to add a markup place widget and a push-button.</p>
</blockquote>
</aside>
<p>A problem arise from otherwise straightforward solution:</p>
<ul>
<li>cannot access all internal widgets of the above markupsPlaceWidget to disconnect the default established signals and proxy (i.e. connect) them to the effect’s markupsPlaceWidget slots (i.e. both default and draw-tube-logic ones)</li>
</ul>
<p>Don’t you agree?</p>

---

## Post #6 by @lassoan (2023-10-31 21:09 UTC)

<p>All the widgets are synchronized via MRML nodes. You should not need to do such low level things like connect/disconnect signals. Let me know if you run into any specific problem.</p>

---

## Post #7 by @mau_igna_06 (2023-10-31 21:59 UTC)

<p>Right <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=12" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20"></p>
<p>My example:</p>
<pre><code class="lang-auto">import SampleData
# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadCTChest()
# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("test")

slicer.util.selectModule("SegmentEditor")

segmentEditorWidget = mainWindow().findChildren('qMRMLSegmentEditorWidget')[0]
segmentEditorWidget.setActiveEffectByName('Draw tube')
drawTubeEffect = segmentEditorWidget.activeEffect()
drawTubeEffect.self().logic.radius=15
drawTubeEffect.self().updateModelFromSegmentMarkupNode()
</code></pre>
<p>Then, I expected just adding points like this would not work, <em><strong>but it does:</strong></em></p>
<pre><code class="lang-auto">drawTubeEffect.self().segmentMarkupNode.AddControlPoint([0,0,0])
drawTubeEffect.self().segmentMarkupNode.AddControlPoint([100,0,0])
drawTubeEffect.self().segmentMarkupNode.AddControlPoint([0,200,0])
drawTubeEffect.self().segmentMarkupNode.AddControlPoint([0,0,-300])
drawTubeEffect.self().segmentMarkupNode.AddControlPoint([0,-400,0])
</code></pre>
<p>Thanks!</p>

---
