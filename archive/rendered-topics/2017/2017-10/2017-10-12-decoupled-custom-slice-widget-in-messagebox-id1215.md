---
topic_id: 1215
title: "Decoupled Custom Slice Widget In Messagebox"
date: 2017-10-12
url: https://discourse.slicer.org/t/1215
---

# Decoupled (custom) slice widget in messagebox

**Topic ID**: 1215
**Date**: 2017-10-12
**URL**: https://discourse.slicer.org/t/decoupled-custom-slice-widget-in-messagebox/1215

---

## Post #1 by @che85 (2017-10-12 21:28 UTC)

<p>Hi Developers,</p>
<p>I am curious if it would be possible for have a message box showing a slice widget. I somewhat “hacked” that but I am not happy with it and I would like to know if there is a clean way to do it.</p>
<p>I am asking because prior to doing prostate biopsy our module receives pre-procedural images. The operator has to confirm if an endo-rectal coil was used during pre-procedural acquisition.</p>
<p>The following screenshot displays, what I ‘hacked’ so far.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a5634fd7cfa74cd10e1a8bc7493a1e16673c6fc.png" data-download-href="/uploads/short-url/3KZ6VZToMMMzbfHIKwgEl6KKKyo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5634fd7cfa74cd10e1a8bc7493a1e16673c6fc_2_578x500.png" alt="image" data-base62-sha1="3KZ6VZToMMMzbfHIKwgEl6KKKyo" width="578" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5634fd7cfa74cd10e1a8bc7493a1e16673c6fc_2_578x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5634fd7cfa74cd10e1a8bc7493a1e16673c6fc_2_867x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5634fd7cfa74cd10e1a8bc7493a1e16673c6fc_2_1156x1000.png 2x" data-dominant-color="787878"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1518×1312 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code>class ...
  def __init__(self, widgetName, text="", parent=None, **kwargs):
    qt.QMessageBox.__init__(self, parent if parent else slicer.util.mainWindow())
    self.widgetName = widgetName
    self.text = text
    for key, value in kwargs.iteritems():
      if hasattr(self, key):
        setattr(self, key, value)
    self.setup()

  def setup(self):
    widget = self.layoutManager.sliceWidget(self.widgetName)
    if not widget:
      raise AttributeError("Slice widget with name %s not found" %self.widgetName)
    sliceNode = widget.sliceLogic().GetSliceNode()

    self.sliceWidget = slicer.qMRMLSliceWidget()
    self.sliceWidget.setMRMLScene(widget.mrmlScene())
    self.sliceWidget.setMRMLSliceNode(sliceNode)

    self.layout().addWidget(self.sliceWidget, 0, 1)
    self.layout().addWidget(qt.QLabel(self.text), 1 ,1)
    self.layout().addWidget(self.createHLayout(self.buttons()), 2, 1)

  def exec_(self):
      widget = self.layoutManager.sliceWidget(self.widgetName)
      self.sliceWidget.setFixedSize(widget.size)
      return qt.QMessageBox.exec_(self)
</code></pre>
<p>Thanks for any help.</p>

---

## Post #2 by @lassoan (2017-10-12 21:44 UTC)

<p>You should be able to just show the slice widget directly, without a layout manager. Have you tried that?</p>

---

## Post #3 by @che85 (2017-10-13 13:21 UTC)

<p>Hi Andras,</p>
<p>I tried the following. For any reason it displays the red slice widget, but I didn’t even specify the name…</p>
<pre><code>sliceWidget = slicer.qMRMLSliceWidget()
sliceWidget.setMRMLScene(slicer.mrmlScene)
sliceWidget.show()
</code></pre>
<p>I would like to specify my own slice widget name, so I tried the following code which crashes Slicer:</p>
<pre><code>sliceWidget = slicer.qMRMLSliceWidget()
sliceNode = slicer.vtkMRMLSliceNode()
sliceNode.SetLayoutName(“Black”)
slicer.mrmlScene.AddNode(sliceNode) # crashes here
sliceWidget.setMRMLSliceNode(sliceNode)
</code></pre>
<p>Did I miss something?</p>

---

## Post #4 by @lassoan (2017-10-13 19:45 UTC)

<p>You need to create nodes in a certain order. I needed this some time ago and remember that Slicer crashed when that strict order was not followed bit otherwise worked. I’m not sure I can find that code, but you should be able to replicate what the layout manager does by inspecting its source code. Let me know if you have trouble finding it.</p>

---

## Post #5 by @che85 (2017-12-07 18:19 UTC)

<aside class="quote no-group" data-username="che85" data-post="3" data-topic="1215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/che85/48/636_2.png" class="avatar"> che85:</div>
<blockquote>
<p>sliceWidget = slicer.qMRMLSliceWidget()<br>
sliceNode = slicer.vtkMRMLSliceNode()<br>
sliceNode.SetLayoutName(“Black”)<br>
slicer.mrmlScene.AddNode(sliceNode) # crashes here<br>
sliceWidget.setMRMLSliceNode(sliceNode)</p>
</blockquote>
</aside>
<p>Andras I found this code <a href="https://github.com/Slicer/Slicer/blob/dddd78bbf570644825caed947d42def104bfbc4c/Libs/MRML/Widgets/qMRMLLayoutManager.cxx#L296-L329" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/dddd78bbf570644825caed947d42def104bfbc4c/Libs/MRML/Widgets/qMRMLLayoutManager.cxx#L296-L329</a></p>
<p>The following code partially works partially. Unfortunately the method calls, that are commented out, are not accessible from Python.</p>
<pre><code>sliceLogic = slicer.vtkMRMLSliceLayerLogic()
sliceLogic.SetMRMLScene(slicer.mrmlScene)
sliceNode = slicer.vtkMRMLSliceNode()
sliceNode.SetLayoutName("Black")
slicer.mrmlScene.AddNode(sliceNode)
sliceLogic.SetSliceNode(sliceNode)

lm = slicer.app.layoutManager()
sliceLayoutColor = qt.QColor.fromRgbF(sliceNode.GetLayoutColor()[0], sliceNode.GetLayoutColor()[1], sliceNode.GetLayoutColor()[2])
sliceWidget = slicer.qMRMLSliceWidget(lm.viewport())
#sliceWidget.setSliceViewName("test") # not accessible from python
sliceWidget.setObjectName("qMRMLSliceWidget" + sliceNode.GetLayoutName())
#sliceWidget.setSliceViewLabel(sliceViewLabel) # not accessible from python
#sliceWidget.setSliceViewColor(sliceLayoutColor) # not accessible from python
sliceWidget.setMRMLScene(slicer.mrmlScene)
sliceWidget.setMRMLSliceNode(sliceNode) # crashes here again


widget = qt.QWidget()
widget.setLayout(qt.QGridLayout())
widget.layout().addWidget(sliceWidget)
sliceWidget.show()

widget.show()
</code></pre>
<p>When hovering with the mouse on that sliceWidget, I am not getting the following errors:</p>
<pre><code>Traceback (most recent call last):

 File "/Applications/Slicer.app/Contents/lib/Slicer-4.9/qt-scripted-modules/DataProbe.py", line 265, in processEvent

sliceView = slicer.app.layoutManager().sliceWidget(sliceNode.GetLayoutName()).sliceView()

AttributeError: 'NoneType' object has no attribute 'sliceView'
</code></pre>
<p>Seems like I need to register the newly created sliceWidget in the layoutManager?</p>

---

## Post #6 by @pieper (2017-12-07 18:48 UTC)

<p>These should be made Q_INVOKABLE:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/61b366ef5bf0dc3c198d0bba2e509851e856cbac/Libs/MRML/Widgets/qMRMLSliceWidget.h#L82-L104" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/61b366ef5bf0dc3c198d0bba2e509851e856cbac/Libs/MRML/Widgets/qMRMLSliceWidget.h#L82-L104" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/61b366ef5bf0dc3c198d0bba2e509851e856cbac/Libs/MRML/Widgets/qMRMLSliceWidget.h#L82-L104</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="82" style="counter-reset: li-counter 81 ;">
<li>/// \sa qMRMLSliceControllerWidget::sliceViewName()</li>
<li>/// \sa setSliceViewName()</li>
<li>QString sliceViewName()const;</li>
<li>
</li>
<li>/// \sa qMRMLSliceControllerWidget::sliceViewName()</li>
<li>/// \sa sliceViewName()</li>
<li>void setSliceViewName(const QString&amp; newSliceViewName);</li>
<li>
</li>
<li>/// \sa qMRMLSliceControllerWidget::sliceViewLabel()</li>
<li>/// \sa setSliceViewLabel()</li>
<li>QString sliceViewLabel()const;</li>
<li>
</li>
<li>/// \sa qMRMLSliceControllerWidget::sliceViewLabel()</li>
<li>/// \sa sliceViewLabel()</li>
<li>void setSliceViewLabel(const QString&amp; newSliceViewLabel);</li>
<li>
</li>
<li>/// \sa qMRMLSliceControllerWidget::sliceViewColor()</li>
<li>/// \sa setSliceViewColor()</li>
<li>QColor sliceViewColor()const;</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/61b366ef5bf0dc3c198d0bba2e509851e856cbac/Libs/MRML/Widgets/qMRMLSliceWidget.h#L82-L104" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/che85">@che85</a> can you try adding that to see if it fixes the python example?</p>

---

## Post #7 by @jcfr (2017-12-07 18:54 UTC)

<p>Considering Q_PROPERTY similar to<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/61b366ef5bf0dc3c198d0bba2e509851e856cbac/Libs/MRML/Widgets/qMRMLSliceWidget.h#L52" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/61b366ef5bf0dc3c198d0bba2e509851e856cbac/Libs/MRML/Widgets/qMRMLSliceWidget.h#L52" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/61b366ef5bf0dc3c198d0bba2e509851e856cbac/Libs/MRML/Widgets/qMRMLSliceWidget.h#L52</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="42" style="counter-reset: li-counter 41 ;">
<li>
</li>
<li>class vtkAlgorithmOutput;</li>
<li>class vtkImageData;</li>
<li>class vtkInteractorObserver;</li>
<li>class vtkCornerAnnotation;</li>
<li>class vtkCollection;</li>
<li>
</li>
<li>class QMRML_WIDGETS_EXPORT qMRMLSliceWidget : public qMRMLWidget</li>
<li>{</li>
<li>Q_OBJECT</li>
<li class="selected">Q_PROPERTY(QString sliceOrientation READ sliceOrientation WRITE setSliceOrientation)</li>
<li>public:</li>
<li>/// Superclass typedef</li>
<li>typedef qMRMLWidget Superclass;</li>
<li>
</li>
<li>/// Constructors</li>
<li>explicit qMRMLSliceWidget(QWidget* parent = 0);</li>
<li>virtual ~qMRMLSliceWidget();</li>
<li>
</li>
<li>/// Get slice controller</li>
<li>Q_INVOKABLE qMRMLSliceControllerWidget* sliceController()const;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #8 by @lassoan (2017-12-07 20:54 UTC)

<p>This works for me on latest nightly build:</p>
<pre><code>import SampleData
volumeNode = SampleData.SampleDataLogic().downloadMRHead()

sliceWidget = slicer.qMRMLSliceWidget()
sliceWidget.setMRMLScene(slicer.mrmlScene)
sliceNode = slicer.vtkMRMLSliceNode()
sliceNode.SetName("MySlice")
sliceNode.SetLayoutName("Black")
slicer.mrmlScene.AddNode(sliceNode)
sliceWidget.setMRMLSliceNode(sliceNode)

sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
sliceLogic.GetSliceCompositeNode().SetBackgroundVolumeID(volumeNode.GetID())

sliceWidget.show()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/393eb3ad441f250e466bf5eded9eb4c90c67e838.jpeg" data-download-href="/uploads/short-url/8apylkBxDHhCa7VDD1FYWhomPGg.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/393eb3ad441f250e466bf5eded9eb4c90c67e838_2_690x373.jpg" alt="image" data-base62-sha1="8apylkBxDHhCa7VDD1FYWhomPGg" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/393eb3ad441f250e466bf5eded9eb4c90c67e838_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/393eb3ad441f250e466bf5eded9eb4c90c67e838_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/393eb3ad441f250e466bf5eded9eb4c90c67e838_2_1380x746.jpg 2x" data-dominant-color="6B6B71"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 365 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @che85 (2017-12-07 21:40 UTC)

<p>I am getting a bunch of errors. I assume that the additional slice widget needs to be registered somehow, right?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1f54edefaf1c19085effb94b95f8221c6418c73.png" data-download-href="/uploads/short-url/poi56QWTEc8lgln9m8D1gTuWnmj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b1f54edefaf1c19085effb94b95f8221c6418c73_2_690x399.png" alt="image" data-base62-sha1="poi56QWTEc8lgln9m8D1gTuWnmj" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b1f54edefaf1c19085effb94b95f8221c6418c73_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b1f54edefaf1c19085effb94b95f8221c6418c73_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/b1f54edefaf1c19085effb94b95f8221c6418c73_2_1380x798.png 2x" data-dominant-color="9B969B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2226 1.48 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2017-12-07 22:02 UTC)

<p>That’s fine, those are only reported by data probe, as it uses the layout manager to look up slice view node. I’ll fix that today. No need to register anything.</p>

---

## Post #11 by @che85 (2017-12-07 22:07 UTC)

<p>Another thing is, that only “Reformat” is available in the slice orientation drop down</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fb1840b03a0e116ed6e681921970150573c4d64.png" data-download-href="/uploads/short-url/bn02QOCUSLyWzrTRb6vao8yiXAM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fb1840b03a0e116ed6e681921970150573c4d64_2_558x500.png" alt="image" data-base62-sha1="bn02QOCUSLyWzrTRb6vao8yiXAM" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fb1840b03a0e116ed6e681921970150573c4d64_2_558x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fb1840b03a0e116ed6e681921970150573c4d64_2_837x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fb1840b03a0e116ed6e681921970150573c4d64_2_1116x1000.png 2x" data-dominant-color="535353"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1234×1104 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2017-12-08 03:17 UTC)

<p>I’ve checked this again and found that the layout manager automatically creates a widget for all slice nodes that are added to the scene. The simplest is to use this widget, as there are no side effects.</p>
<pre><code># Load some data into the scene
import SampleData
volumeNode = SampleData.SampleDataLogic().downloadMRHead()

# Create slice node (this automatically creates a slice widget)
sliceNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLSliceNode')
sliceNode.SetName("Black")
sliceNode.SetLayoutName("Black")
sliceNode.SetLayoutLabel("BL")
sliceNode.SetOrientation("Sagittal")
sliceNode = slicer.mrmlScene.AddNode(sliceNode)

# Select background volume
sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
sliceLogic.GetSliceCompositeNode().SetBackgroundVolumeID(volumeNode.GetID())

# Get the automatically created slice widget
lm=slicer.app.layoutManager()
sliceWidget=lm.viewWidget(sliceNode)

# Move slice widget to a different layout
# (it can be added to any other layout)
sliceWidget.setParent(None)
# Show slice widget
sliceNode.SetMappedInLayout(1)
</code></pre>
<p>Note: when you switch layouts, the widget gets hidden, so you have to call sliceNode.SetMappedInLayout(1) again.</p>

---

## Post #13 by @che85 (2017-12-08 03:41 UTC)

<p>Great! That’s working. Thanks a lot!</p>

---

## Post #14 by @talmazov (2019-06-28 05:14 UTC)

<p>This is awesome, thanks for sharing!<br>
Is there a way to instead of decoupling the slice widget, have it appear to the left of the current preset layout as part of the currently loaded layout template?</p>
<p>Do I use the sliceWidget.setParent() feature? If so, how do I obtain an instance of the currently used layout?</p>

---

## Post #15 by @lassoan (2019-06-28 15:52 UTC)

<p>If you want to add views to the layout then you can customize viewer layout as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout" rel="nofollow noopener">here</a>.</p>
<p>Views are grouped based on <code>viewgroup</code> property. To get an “independent” view, set its <code>viewgroup</code> property to a unique value.</p>

---

## Post #16 by @talmazov (2019-06-28 16:38 UTC)

<p>Ok, but i’m unsure how the syntax would be. Can you please give me an example of Slicer’s preset layout named “Conventional Widescreen” where the slice nodes are grouped on the right and the 3d view on the left. I should be able to play around with that to get what I am looking for. Thanks!</p>

---

## Post #17 by @lassoan (2019-06-28 22:26 UTC)

<p>Go to the script repository link that I posted above. XML description of all the built-in view presets are linked from there.</p>

---
