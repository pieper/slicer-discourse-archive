# XML style for custom layout

**Topic ID**: 5831
**Date**: 2019-02-19
**URL**: https://discourse.slicer.org/t/xml-style-for-custom-layout/5831

---

## Post #1 by @ghnguyen (2019-02-19 16:10 UTC)

<p>Hi,</p>
<p>I want to make a custom layout and right now I just have a long XML string. Can I specify an XML stylesheet or is there any easier way to change the background color (for the space between the items or the layouts)? Using style=“background-color:<span class="hashtag">#000000</span>” directly in the item does not work. Right now it’s <span class="hashtag">#EEEEEE</span> I believe and I’d like to make it black. Thanks!</p>

---

## Post #2 by @jamesobutler (2019-02-19 23:19 UTC)

<p>For regular Qt layouts, you change change background color of a widget using xml or python</p>
<pre><code class="lang-xml">&lt;property name="styleSheet"&gt;
 &lt;string&gt;background-color:#000000&lt;/string&gt;
&lt;/property&gt;
</code></pre>
<pre><code class="lang-python">widget=qt.QWidget()
widget.setStyleSheet("background-color:#000000")   # background set to black
</code></pre>
<p>I generally use Qt Designer to generate UI files which is the XML code. That application is actually bundled in Slicer 4.10.1 which you can access by going to …/Slicer 4.10.1/bin/SlicerDesigner.exe or you can use it if you download Qt5 from the web.</p>
<p>Slicer does technically have a “Dark Mode” if you are attempting to set layouts to some dark color. You can switch to it by going to Edit-&gt;Application Settings-&gt;Appearance-&gt;Style-&gt;Dark Slicer</p>

---

## Post #3 by @ghnguyen (2019-03-06 17:10 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/xml-style-for-custom-layout/5831/2">XML style for custom layout</a>:</p>
<p>Hi James, thanks for the suggestion. I think there is a misunderstanding here, I can set the styleSheet of the regular Qt layouts like you mentioned. What I am looking for is how to change that of the layoutnode. Specifically the one that handles all viewports when you call slicer.app.layoutManager().layoutLogic().GetLayoutNode(). I can set the custom XML layout for this, but when screen size changes, there would be gaps between my XML items and those gaps are currently gray. I’m adding 2 screenshots for easier comparison.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cae9c07ffcb119c6cac5b2accdb330aba365c9e7.png" data-download-href="/uploads/short-url/sX3g8w2NC53pEnsIcHh3fgDEaub.png?dl=1" title="normal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cae9c07ffcb119c6cac5b2accdb330aba365c9e7_2_483x500.png" alt="normal" data-base62-sha1="sX3g8w2NC53pEnsIcHh3fgDEaub" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cae9c07ffcb119c6cac5b2accdb330aba365c9e7_2_483x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cae9c07ffcb119c6cac5b2accdb330aba365c9e7_2_724x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cae9c07ffcb119c6cac5b2accdb330aba365c9e7_2_966x1000.png 2x" data-dominant-color="4E4D5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">normal</span><span class="informations">1012×1047 14.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2019-03-06 19:50 UTC)

<p>Instead of addressing the issue of making the grey color black, I think you actually need to be addressing why the slice widgets don’t have the correct horizontal size policy. If you are changing window size and the objects are not changing size, then you have incorrect size policy set for the widgets.</p>
<p>I don’t think I’ve ever had to set size policy when customizing layouts.  See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout</a> as an example for customizing layouts. Otherwise you might need to explicitly state another property for sizepolicy.</p>

---

## Post #5 by @ghnguyen (2019-03-06 20:10 UTC)

<p>Good point, I did in fact fix the maximum height/width of the slice widgets to match with the size of some images that I need to do mapping on. I was just wondering if I could change the background as well.</p>

---

## Post #6 by @jamesobutler (2019-03-06 20:39 UTC)

<aside class="quote no-group" data-username="ghnguyen" data-post="5" data-topic="5831">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/c6cbf5/48.png" class="avatar"> ghnguyen:</div>
<blockquote>
<p>fix the maximum height/width of the slice widgets to match with the size of some images that I need to do mapping on</p>
</blockquote>
</aside>
<p>This is quite unusual. I would suggest updating the field of view of the slice window instead. Then the black color from inside the slice viewers will be used.<br>
Look into slice logic for doing things like:</p>
<pre data-code-wrap="python"><code class="lang-python">width = 10 # mm 
slice_logic = slicer.app.layoutManager().sliceWidget("Green").sliceLogic()
slice_logic.FitFOVToBackground(width))
</code></pre>
<p>or the basic centering:</p>
<pre data-code-wrap="python"><code class="lang-python">layout_manager = slicer.app.layoutManager()
for slice_name in layout_manager.sliceViewNames():
  layout_manager.sliceWidget(slice_name).sliceLogic().FitSliceToAll()
</code></pre>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Reset_field_of_view_to_show_background_volume_maximized" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Reset_field_of_view_to_show_background_volume_maximized</a></p>

---
