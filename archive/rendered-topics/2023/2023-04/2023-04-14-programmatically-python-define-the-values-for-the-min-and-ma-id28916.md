# Programmatically (python) define the values for the min and max of the slider in the volume widget (not the min-max of the window/level)

**Topic ID**: 28916
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/programmatically-python-define-the-values-for-the-min-and-max-of-the-slider-in-the-volume-widget-not-the-min-max-of-the-window-level/28916

---

## Post #1 by @RonJones (2023-04-14 12:44 UTC)

<p>I am trying to define the minimum and maximum values of the slides in the volume widget (see screenshot - it is the widgets circled in red).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5a371261f67791f151a5a32b7f84ce2ec2795da.png" data-download-href="/uploads/short-url/utVSbQyt0JYWsXvCj52a1thhGgG.png?dl=1" title="WindowLevel slider - min-max" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5a371261f67791f151a5a32b7f84ce2ec2795da_2_690x451.png" alt="WindowLevel slider - min-max" data-base62-sha1="utVSbQyt0JYWsXvCj52a1thhGgG" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5a371261f67791f151a5a32b7f84ce2ec2795da_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5a371261f67791f151a5a32b7f84ce2ec2795da_2_1035x676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5a371261f67791f151a5a32b7f84ce2ec2795da_2_1380x902.png 2x" data-dominant-color="94918F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WindowLevel slider - min-max</span><span class="informations">1707×1116 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For clarity this is not the min-max of the WindowLevel.</p>
<p>Which widget do these elements belong to and how what is the most appropriate way to read/write them?</p>
<p>thanks</p>

---

## Post #2 by @jamesobutler (2023-04-14 17:47 UTC)

<p>Once you have a qMRMLWindowLevelWidget object, you can use the <code>setMinMaxBounds</code> method.</p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
volume_node = SampleData.SampleDataLogic().downloadMRHead()
window_level_widget = slicer.qMRMLWindowLevelWidget()  # creates a new window/level widget object
window_level_widget.setMRMLVolumeNode(volume_node)
window_level_widget.setMinMaxBounds(0,100)
window_level_widget.show()
</code></pre>
<p>You can also see discussion linked below about why you might use Window/Level values that are outside of the scalar range and why the values of -600 to 600 are chosen in the image you show.</p>
<aside class="quote quote-modified" data-post="2" data-topic="17821">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/improving-qmrmlvolumewidget-range-bounds/17821/2">Improving qMRMLVolumeWidget range bounds</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I have only used these widgets a few times in my life. Maybe partly because they are inconvenient, but mainly because I always set window/level visually (using the window/level mouse mode). Can you describe why and how do you use these widgets? Is there any workflow when you rely on setting these values numerically instead of visually? 

The popup makes sense in theory (it saves space and clicks), but I think the widget is quite confusing. 
slicer.qMRMLRangeWidget() solves the same task in a mu…
  </blockquote>
</aside>


---

## Post #3 by @RonJones (2023-04-17 02:04 UTC)

<p>Thanks. That works!</p>
<p>The other part I am having trouble working out is how to identify and access the existing WindowLevelWidget that is associated with PET Scalar volume.</p>

---

## Post #4 by @RonJones (2023-04-26 04:11 UTC)

<p>For reference below is how I worked out to access the existing window level widget.</p>
<p>Very interested to hear if there a better / cleaner approach. thanks.</p>
<pre><code class="lang-auto">ui = slicer.util.getModuleWidget("Volumes")
ui_children = slicer.util.childWidgetVariables(ui)
windowLevelWidget = ui_children.MRMLWindowLevelWidget
windowLevelWidget.setMinMaxBounds(0, 20)
</code></pre>

---
