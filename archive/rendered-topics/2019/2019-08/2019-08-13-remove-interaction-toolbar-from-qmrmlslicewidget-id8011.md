# Remove Interaction toolbar from QMRMLSliceWidget

**Topic ID**: 8011
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/remove-interaction-toolbar-from-qmrmlslicewidget/8011

---

## Post #1 by @burnhamd (2019-08-13 18:54 UTC)

<p>I would like to remove the toolbar from the qMRMLSliceWidget for a cleaner UI for a project I am working on.  Is there a way to do this on the widget or should I display the slice by another method.</p>
<p>For reference this is the toolbar I am referring to.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d75dfba000ac634837e3080c484932183afc8c42.png" data-download-href="/uploads/short-url/uJe0QhYn7VkAAws4ig12TDN6UDM.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d75dfba000ac634837e3080c484932183afc8c42.png" alt="Capture" data-base62-sha1="uJe0QhYn7VkAAws4ig12TDN6UDM" width="687" height="500" data-dominant-color="6B6A6A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">963×700 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-08-13 19:28 UTC)

<p>AFAIK there’s no option exposed for that.  It would be a bit of a hack (but not unprecedented) to use <a href="https://doc.qt.io/qt-5/qobject.html#findChild" rel="nofollow noopener">findChild</a> at the qt in python level to remove the pushpin widget so the popup would never appear.</p>

---

## Post #3 by @burnhamd (2019-08-13 20:17 UTC)

<p>Thats a good thought.  I will try that.</p>

---

## Post #4 by @burnhamd (2019-08-13 20:46 UTC)

<p>Having trouble finding documentation on the children of QMRMLSliceWidget.  Is there somewhere that outlines this?  Or a way to get a list of all children?  calling findChildren(’*’) yielded empty result.</p>

---

## Post #5 by @jcfr (2019-08-13 21:05 UTC)

<p>You could also doing something like this:</p>
<pre><code class="lang-python">for viewName in ["Green", "Red", "Yellow"]:
  slicer.app.layoutManager().sliceWidget(viewName).sliceController().setVisible(False)
</code></pre>

---

## Post #6 by @lassoan (2019-08-14 04:13 UTC)

<p>You can also use <code>slicer.util.setViewControllersVisible(False)</code> in recent Preview Releases.</p>
<p>If you want to create a Slicer-based application with a customized look&amp;feel then you’ll probably find this page useful: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---

## Post #7 by @burnhamd (2019-08-14 21:51 UTC)

<p><span class="mention">@Iassoan</span> , I did look into the slicelet templates.  I am following basically this approach, but currently building the UI a different way.  Having everything for my module on the sidebar and having the layout always visible next to it doesnt work for my application.</p>
<p>I am currently building a guided screen which opens several screens that get some user input, then I display a custom display consisting of QMRMLSliceWidgets.</p>

---

## Post #8 by @burnhamd (2019-08-20 21:01 UTC)

<p>Continuing on this track, I want to add my own interaction widgets to the top of the slice view.</p>
<p>Im considering a few paths.</p>
<ol>
<li>I create my own widget in c++ that is similar to the qMRMLSliceWidget<br>
2.I build essentially the same thing in python using qMRMLSliceView - so far I only get a slicer crash when in do a show of a sliceview<br>
3.I hide the toolbar and simply place my buttons above the qMRMLSliceWidget in my layout.</li>
</ol>
<p>Any thoughts on these approaches?  I think 3 is easiest, but doesnt allow me to embed some of the logic in the view itself, but I havent been able to get very far with option 2.</p>

---

## Post #9 by @lassoan (2019-08-21 03:04 UTC)

<p>You can customize widgets in the existing slice controller widgets any way you need: you can hide any built-in widget and add your own, as shown in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_widgets_in_view_controller_bars" rel="nofollow noopener">examples in script repository</a>.</p>

---

## Post #10 by @burnhamd (2019-08-27 14:14 UTC)

<p>Getting a layout issue when I remove the widgets using the method in the script repository.  The slice view becomes very small and the 3D grows to cover most of the space.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1f9ba5ae93db72790eba124cfc5758c22de2e84.png" data-download-href="/uploads/short-url/wf4taF3KPuWS8yzGx4AyLWjqwO8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1f9ba5ae93db72790eba124cfc5758c22de2e84_2_690x297.png" alt="image" data-base62-sha1="wf4taF3KPuWS8yzGx4AyLWjqwO8" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1f9ba5ae93db72790eba124cfc5758c22de2e84_2_690x297.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1f9ba5ae93db72790eba124cfc5758c22de2e84_2_1035x445.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1f9ba5ae93db72790eba124cfc5758c22de2e84_2_1380x594.png 2x" data-dominant-color="595A76"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2245×968 69.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is this expected?</p>

---

## Post #11 by @lassoan (2019-08-27 14:20 UTC)

<p>Yes, it works as expected. You must to set up size policies in your Qt widgets according to what you need. Setting up size policies is not simple but it is standard Qt matter - there is nothing Slicer specific about how Qt widgets are sized in Slicer. See documentation <a href="https://doc.qt.io/qt-5/qsizepolicy.html" rel="nofollow noopener">here</a>.</p>

---
