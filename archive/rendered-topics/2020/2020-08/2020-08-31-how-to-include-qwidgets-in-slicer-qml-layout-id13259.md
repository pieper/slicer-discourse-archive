# How to include qwidgets in slicer qml layout

**Topic ID**: 13259
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/how-to-include-qwidgets-in-slicer-qml-layout/13259

---

## Post #1 by @Chintha_Siva_Prasad (2020-08-31 17:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1f529b28bb6704c4a028c83d6fe0527fe63f585.png" data-download-href="/uploads/short-url/weUGLYzhzlGx3xKu7C0mvkqnnNz.png?dl=1" title="Screenshot from 2020-08-31 23-09-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1f529b28bb6704c4a028c83d6fe0527fe63f585_2_690x354.png" alt="Screenshot from 2020-08-31 23-09-42" data-base62-sha1="weUGLYzhzlGx3xKu7C0mvkqnnNz" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1f529b28bb6704c4a028c83d6fe0527fe63f585_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1f529b28bb6704c4a028c83d6fe0527fe63f585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1f529b28bb6704c4a028c83d6fe0527fe63f585.png 2x" data-dominant-color="F4FBF4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-31 23-09-42</span><span class="informations">967×497 57.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am using this layout. I want to insert a toolbar on top of first viewNode only.<br>
That means at grid(0,0) position I want a layout which contains both toolbar and viewNode1.<br>
How can I do this?</p>

---

## Post #2 by @lassoan (2020-08-31 17:52 UTC)

<p>You can only add view widgets in the view layout. You can customize what Qt widgets are shown in the view control and add custom widgets, as shown in this example in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_widgets_in_view_controller_bars">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_widgets_in_view_controller_bars</a></p>

---
