# Segment editor tools arrangement

**Topic ID**: 16285
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/segment-editor-tools-arrangement/16285

---

## Post #1 by @mohammed_alshakhas (2021-03-01 12:09 UTC)

<p>im newly using the preview version , and one thing i definitely don’t like is the tools arrangement</p>
<p>im so used to the old one , work perfect with keyboard shortcuts and all</p>
<p>now im keeping hitting 1 for paint and getting threshold</p>
<p>id love the old one back please <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60b633b05e9e1163ab84cd962642de55154da395.png" alt="Screen Shot 2021-03-01 at 15.09.17" data-base62-sha1="dNycA9Ok0BClMqOLVNZ10C2mo05" width="617" height="306"></p>

---

## Post #2 by @lassoan (2021-03-01 14:09 UTC)

<p>In most cases, you need to start segmentation with thresholding (to check if global thresholding can give meaningful segmentation results, to choose intensity range for painting, or create a mask segment).</p>
<p>Of course each segmentation workflow is different, so you may want to change defaults. For example, you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_list_of_displayed_Segment_editor_effects">customize order and visibility of Segment editor effects</a> and can even create custom <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_keyboard_shortcut_for_toggling_sphere_brush_for_paint_and_erase_effects">keyboard shortcuts for switching between effects</a> and customize almost anything on the GUI and in the application behavior by a few lines  of Python code. You can place these code snippets in your application startup file to make the changes persistent.</p>

---

## Post #3 by @mohammed_alshakhas (2021-03-01 14:13 UTC)

<p>I’m sure you got great reason for the change , however mostly I use pain /erase / draw</p>
<p>Threshold is first but much less frequent .</p>
<p>I’m programmming illetrate , I’m just a humble Maxillofacial surgeon enjoying slicer too much <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"></p>

---

## Post #4 by @lassoan (2021-03-01 14:22 UTC)

<p>Customizing effect order does not require any programming experience. Hit <kbd>Ctrl</kbd>+<kbd>3</kbd> and copy-paste this into the displayed Python interactor:</p>
<pre><code class="lang-python">segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setEffectNameOrder(['Paint', 'Erase'])
</code></pre>

---

## Post #5 by @mohammed_alshakhas (2021-03-01 14:25 UTC)

<p>thats great , thats too much programming to me<br>
works perfect though</p>

---

## Post #6 by @lassoan (2021-03-01 14:32 UTC)

<p>We could add a graphical user interface for configuring effect order (for example, a text input box in application settings where user can list segment editor effect names in preferred order), but so far we have no heard from too many people that they would need this. Users are either fine with the current order or they are OK with changing it by scripting.</p>

---

## Post #7 by @mohammed_alshakhas (2021-03-01 14:39 UTC)

<p>id love such feature , even the list of favorite module would be great if can be customized .<br>
like if love to have crop volume in my favorite but didn’t figure out how .</p>
<p>one more thing is that if possible to have favorite views . i only use 3d only ,  conventional , four up , two side by side .<br>
the rest are not useful to me . id love to be able to customize the list and remove the ones i never use .</p>
<p>thank you for considering these points</p>

---

## Post #8 by @lassoan (2021-03-01 14:48 UTC)

<p>Favorite modules: You can already customize the favorite modules with a GUI, in application settings - see <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#toolbar">here</a> for details.</p>
<p>Favorite views: We have been planning to add this, I’ve submitted a <a href="https://github.com/Slicer/Slicer/issues/5497">feature request</a> to make sure we consider it for the next release. Until then, you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_keyboard_shortcuts">assign keyboard shortcuts to switch between views</a>, which is probably even faster than using toolbar buttons anyway.</p>

---

## Post #9 by @mohammed_alshakhas (2021-03-02 05:10 UTC)

<p>i didn’t get how can i change my favorite module ,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5368a16320dde313aed780024ecfcfbce2aba1c7.png" data-download-href="/uploads/short-url/bTRNzZvo4TRc3J6Iy3y7gscxThl.png?dl=1" title="Screen Shot 2021-03-02 at 08.07.34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5368a16320dde313aed780024ecfcfbce2aba1c7_2_358x500.png" alt="Screen Shot 2021-03-02 at 08.07.34" data-base62-sha1="bTRNzZvo4TRc3J6Iy3y7gscxThl" width="358" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5368a16320dde313aed780024ecfcfbce2aba1c7_2_358x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5368a16320dde313aed780024ecfcfbce2aba1c7_2_537x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5368a16320dde313aed780024ecfcfbce2aba1c7.png 2x" data-dominant-color="333333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-02 at 08.07.34</span><span class="informations">661×923 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i also love to be able to customize too bar more freely rather than fewer options</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd324981e655ce439f42dcc9cea44d2fa4108e13.png" data-download-href="/uploads/short-url/thfCvEQa8jnyGestWlliguTfEdl.png?dl=1" title="Screen Shot 2021-03-02 at 08.07.56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd324981e655ce439f42dcc9cea44d2fa4108e13_2_690x27.png" alt="Screen Shot 2021-03-02 at 08.07.56" data-base62-sha1="thfCvEQa8jnyGestWlliguTfEdl" width="690" height="27" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd324981e655ce439f42dcc9cea44d2fa4108e13_2_690x27.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd324981e655ce439f42dcc9cea44d2fa4108e13_2_1035x40.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd324981e655ce439f42dcc9cea44d2fa4108e13_2_1380x54.png 2x" data-dominant-color="3B3D49"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-02 at 08.07.56</span><span class="informations">1920×77 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2021-03-02 05:16 UTC)

<p>How to change your list of favorite modules: “The list can be customized using menu: Edit / Application settings / Modules / Favorite Modules. Drag-and-drop modules from the Modules list to the Favorite Modules list to add a module.” Let us know if anything is not clear or any suggestions how to improve these instructions.</p>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="9" data-topic="16285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>i also love to be able to customize too bar more freely rather than fewer options</p>
</blockquote>
</aside>
<p>You are absolutely free to customize the toolbar, add new toolbars, invent new actions, etc. It just requires adding a few lines of Python script to the Slicer startup file. You can cut&amp;paste the script from examples in the script repository, but if you describe what features you would put in the toolbar we can put it together for you.</p>

---

## Post #11 by @muratmaga (2021-03-02 05:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="16285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could add a graphical user interface for configuring effect order (for example, a text input box in application settings where user can list segment editor effect names in preferred order), but so far we have no heard from too many people that they would need this.</p>
</blockquote>
</aside>
<p>Actually it would be great to reorder the effects by dragging and dropping the icons positions (like the top toolbar).</p>

---

## Post #12 by @mohammed_alshakhas (2021-03-02 05:33 UTC)

<p>thats what i would love to have !</p>

---
