# Modify properties of the segment editor (maximumHeight of ctkExpandableWidget)

**Topic ID**: 7467
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/modify-properties-of-the-segment-editor-maximumheight-of-ctkexpandablewidget/7467

---

## Post #1 by @EricM (2019-07-08 17:23 UTC)

<p>Hello,</p>
<p>I am a beginner at Slicer (1 week today), so I apologize if my question is simple. I am building a small module in which I would like to include the Segment Editor. In particular, I would like to set the maximum height of the ctkExpandableWidget object (i.e., the list of the segmentations) so as not to make it too long.</p>
<p>The following does what I want when executed in the Python console</p>
<pre><code>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.show()
segmentEditorWidget.layout().itemAt(2).widget().setMaximumHeight(100)
</code></pre>
<p><span class="hashtag">#or</span> this<br>
segmentEditorWidget.children()[13].setMaximumHeight(100)</p>
<p>However, when I put the same code in my .py file and insert it into my module, the ctkExpandableWidget object still behaves like the default ctkExpandableWidget (i.e., it can expand much further than this).</p>
<p>There is more code in my .py file (I followed a couple tutorials that also use the Segment Editor Widget in them), namely:</p>
<pre><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
segmentationNode.CreateDefaultDisplayNodes()

segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)

#inserts into a QGroupBox
groupBoxSegmentation = qt.QGroupBox("Segmentation")
segmentationLayout = qt.QVBoxLayout()
segmentationLayout.addWidget(segmentEditorWidget)
groupBoxSegmentation.setLayout(segmentationLayout)
</code></pre>
<p>Perhaps there is code in here that is overwriting the maximumHeight that I am trying to force?</p>
<p>Thank you for your help, and any comments to improve the above code are welcome!<br>
EricM</p>

---

## Post #2 by @jamesobutler (2019-07-08 17:55 UTC)

<p>There’s an open issue related to layout sizing of the segment editor widget which is what you are describing. This work has stalled, but you might want to look into helping pick this back up.</p>
<p>See <a href="https://github.com/Slicer/Slicer/pull/1085" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1085</a></p>

---

## Post #3 by @cpinter (2019-07-08 18:09 UTC)

<p>Also, in general I’d advise against using pixel values for setting sizes because the wide range of DPIs of the current screens. Use ratios, or multiples of the sizeHint that you can get from certain elements.</p>

---

## Post #4 by @lassoan (2019-07-09 04:09 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="7467">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>in general I’d advise against using pixel values for setting sizes because the wide range of DPIs of the current screens. Use ratios, or multiples of the sizeHint that you can get from certain elements.</p>
</blockquote>
</aside>
<p>Qt5 can scale sizes specified in pixels (they are now called “device independent pixels”) - see <a href="https://doc.qt.io/qt-5/highdpi.html" class="inline-onebox">High DPI Displays | Qt 5.15</a>. So, in theory, specifying size simply in pixels may work well on a variety of displays and resolutions.</p>

---

## Post #5 by @cpinter (2019-07-09 14:02 UTC)

<p>Hm. I kind of liked using size hints for sizing because it allowed to be very precise compared to UI elements in whatever style. So you say we can now use pixels again in Slicer core too? I think we moved away from that completely.</p>

---

## Post #6 by @pieper (2019-07-09 17:06 UTC)

<p>I’d also vote for hints and ratios - I think those device independent pixels sound error prone.</p>

---

## Post #7 by @lassoan (2019-07-10 03:36 UTC)

<p>When you use the Qt designer then most sizes and size hints are defined in device-independent pixels. With the automatic pixel scaling, simple layouts often work well enough. I would try to stick to these simple layouts whenever it is possible.</p>
<p>If there are complicated UI mechanisms or fine-tuned layout behavior is needed then of course it makes sense compute sizes from ratios, font sizes, or other metrics.</p>

---

## Post #8 by @EricM (2019-07-12 07:47 UTC)

<p>Thanks for these tips.<br>
<a class="mention" href="/u/jamesobutler">@jamesobutler</a> - I will look at the link you provided from <a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a>.<br>
<a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a> - is the <a href="https://github.com/Slicer/Slicer/files/2814355/SegmentEditorUIFix.zip" rel="nofollow noopener">SegmentEditorUIFix.zip</a> file you provided in this <a href="https://github.com/Slicer/Slicer/pull/1085" rel="nofollow noopener">link</a> after the modifications on Jan 31, or is it from the original post on Jan 30? If it is after the second round of modifications, I can try to see if it fits in my module better.</p>
<p>Thanks again,<br>
Eric</p>

---

## Post #9 by @jcfr (2019-07-12 07:58 UTC)

<p>The archive provided by <a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a> contains small files created on Jan 25 and useful only to test the changes proposed in the associated PR <a href="https://github.com/Slicer/Slicer/pull/1085" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1085</a></p>

---
