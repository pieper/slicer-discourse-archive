---
topic_id: 20541
title: "Is There A Way To View Just One Slice With One 3D View"
date: 2021-11-09
url: https://discourse.slicer.org/t/20541
---

# Is there a way to view just one slice with one 3D view?

**Topic ID**: 20541
**Date**: 2021-11-09
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-view-just-one-slice-with-one-3d-view/20541

---

## Post #1 by @DIV (2021-11-09 13:21 UTC)

<p>I see that the viewing options already include <em>Side by side</em>, but that only allows each viewport to show a (2D) slice, not a 3D view.<br>
I feel that it would sometimes be useful to view just one slice and one 3D view, which displays each with more space than in the <em>Four-Up</em> view.</p>
<p>Three options I can think of to achieve this:</p>
<ul>
<li>
<p>Provide “3D view” as one of the options in the drop-down menu at the top of a viewport (removing distinction between slice viewport and 3D viewport).  <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/305dcfb18c66c26175c478bdbc721cbc0c83e45a.png" alt="image" data-base62-sha1="6TRUjMgNS2KtXMbS3xn3qCrDZDY" width="407" height="31"></p>
</li>
<li>
<p>Provide a new viewing configuration choice in the list of viewing options.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f59b3f45bdf3e72d25949244fe2928894f6da03.png" data-download-href="/uploads/short-url/mJG6xsMGdCnJcm8aqJntI4OqdmH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f59b3f45bdf3e72d25949244fe2928894f6da03.png" alt="image" data-base62-sha1="mJG6xsMGdCnJcm8aqJntI4OqdmH" width="214" height="500" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">256×598 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Allow the ‘struts’ (~<a href="https://www.diydoctor.org.uk/projects/parts-of-window.htm" rel="noopener nofollow ugc">transoms/mullions</a>) separating each viewport to be draggable, so that the individual viewports are resizeable.  [This would be a kind of workaround, as it might be applied to a <em>Four-Up</em> view, with two of the Slice viewports shrunk to a small size, making more room available for the other two.]</p>
</li>
</ul>
<p>Or maybe there’s already some (convenient) way to do it that I just haven’t noticed?</p>
<p>—DIV</p>

---

## Post #2 by @lassoan (2021-11-09 23:42 UTC)

<p>We provide a handful of layouts, but you can specify custom layouts (including a side-by-side 3D+slice view) by an XML string. This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">example in the script repository</a> does almost exactly what you describe. You can change <code>vertical</code> to <code>horizontal</code> to have side-by-side instead of over-under.</p>
<p>The idea of making layout customization easier for clinicians or make layouts more dynamic comes up time-to-time (see the issues below) but overall there is not too many upvotes for these features:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/issues/5497" class="inline-onebox">Allow user to specify favorite views · Issue #5497 · Slicer/Slicer · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/issues/2384" class="inline-onebox">arbitrary screen layout grids · Issue #2384 · Slicer/Slicer · GitHub</a></li>
<li><a href="https://github.com/Slicer/Slicer/issues/1359" class="inline-onebox">layout modification for better editing · Issue #1359 · Slicer/Slicer · GitHub</a></li>
</ul>
<p>You can upvote the issues that you find the most relevant. You may also find other feature request that are closer to what you want to achieve, or you can add a new feature request if you feel that none of them describe what you want.</p>

---

## Post #3 by @DIV (2021-11-12 01:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20541">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout" rel="noopener nofollow ugc">example in the script repository</a> does almost exactly what you describe. You can change <code>vertical</code> to <code>horizontal</code> to have side-by-side instead of over-under.</p>
</blockquote>
</aside>
<p>This seems to work well.  (One quirk: I had to toggle the crosshairs off and then back on again to be able to see them in the 3D viewport.)</p>
<p>I also tried the script for adding a button to the layout selector toolbar, which also works OK once <code>layoutSwitchAction.setData(layoutId)</code> is adjusted to <code>layoutSwitchAction.setData(customLayoutId)</code> to match the custom layout definition script.<br>
Thanks.</p>
<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20541">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Allow the ‘struts’ (~<a href="https://www.diydoctor.org.uk/projects/parts-of-window.htm" rel="noopener nofollow ugc">transoms/mullions</a>) separating each viewport to be draggable, so that the individual viewports are resizeable.</p>
</blockquote>
</aside>
<p>Funnily enough this functionality is available already in the custom layout defined through the abovementioned script!  Not sure why that happens, when I haven’t seen such (potentially useful) functionality in any of the other built-in layouts.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d72628776d6d29d6cc8541584967689160caa1.png" data-download-href="/uploads/short-url/3xKpFtoXXhRWMvZGpW2pegfDmPT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18d72628776d6d29d6cc8541584967689160caa1_2_690x363.png" alt="image" data-base62-sha1="3xKpFtoXXhRWMvZGpW2pegfDmPT" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18d72628776d6d29d6cc8541584967689160caa1_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d72628776d6d29d6cc8541584967689160caa1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d72628776d6d29d6cc8541584967689160caa1.png 2x" data-dominant-color="393640"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">835×440 18.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-11-12 05:34 UTC)

<p>You can enable/disable the splitter (“struts”) by the <code>split</code> attribute. Slicer has lots of features that are not fully exposed to the users to keep things a bit simpler. I think that’s the main reason why the splitter is not used in every view layout.</p>

---

## Post #5 by @DIV (2021-11-18 04:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20541">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can enable/disable the splitter (“struts”) by the <code>split</code> attribute.</p>
</blockquote>
</aside>
<p>Ah, yes.  I see now that it is <em>occasionally</em> used in some built-in layouts too.<br>
For example, the <code>Conventional</code> layout is the first on the list, and the properties can be viewed with</p>
<pre><code class="lang-auto">&gt;&gt;&gt; layoutManager = slicer.app.layoutManager()
&gt;&gt;&gt; layoutManager.layoutLogic().GetLayoutNode().GetLayoutDescription(1)
</code></pre>
<p>With a little reformatting the output is</p>
<pre><code class="lang-auto">&lt;layout type="vertical" split="true" &gt;
 &lt;item splitSize="500"&gt;  &lt;view class="vtkMRMLViewNode" singletontag="1" verticalStretch="0"&gt;    &lt;property name="viewlabel" action="default"&gt;1&lt;/property&gt;  &lt;/view&gt; &lt;/item&gt;
 &lt;item splitSize="500"&gt;
  &lt;layout type="horizontal"&gt;
   &lt;item&gt;    &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;     &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;     &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;     &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;    &lt;/view&gt;   &lt;/item&gt;
   &lt;item&gt;    &lt;view class="vtkMRMLSliceNode" singletontag="Green"&gt;     &lt;property name="orientation" action="default"&gt;Coronal&lt;/property&gt;     &lt;property name="viewlabel" action="default"&gt;G&lt;/property&gt;     &lt;property name="viewcolor" action="default"&gt;#6EB04B&lt;/property&gt;    &lt;/view&gt;   &lt;/item&gt;
   &lt;item&gt;    &lt;view class="vtkMRMLSliceNode" singletontag="Yellow"&gt;     &lt;property name="orientation" action="default"&gt;Sagittal&lt;/property&gt;     &lt;property name="viewlabel" action="default"&gt;Y&lt;/property&gt;     &lt;property name="viewcolor" action="default"&gt;#EDD54C&lt;/property&gt;    &lt;/view&gt;   &lt;/item&gt;
  &lt;/layout&gt;
 &lt;/item&gt;
&lt;/layout&gt;
</code></pre>
<p><code>layout type="vertical"</code> creates vertically stacked panes separated by horizontal dividers.  In the above case, for the horizontal divider the split is (explicitly) enabled, so it is draggable.</p>
<p><code>layout type="horizontal"</code> creates horizontally stacked panes separated by vertical dividers.  In the above case, for the vertical dividers the splits are (implicitly) disabled, so they are not draggable.</p>
<p>—DIV</p>

---

## Post #6 by @DIV (2022-03-24 13:29 UTC)

<p>In case others want to be able to conveniently define the <em>three distinct</em> <strong>two-up views</strong> comprising 3D+Red, 3D+Yellow and 3D+Green, I have extended the existing code as follows.<br>
It can be run (per session) from the “Python Interactor” (button on toolbar).</p>
<pre><code class="lang-auto"># https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout
# https://discourse.slicer.org/t/is-there-a-way-to-view-just-one-slice-with-one-3d-view/20541/2

# Adapted/extended by D.I.V.
# 2021 to 2022.
# CC-BY


### Initialise

tagTuple = ("Red", "Yellow", "Green")
orientationTuple = ("Axial", "Sagittal", "Coronal")
labelTuple = tuple( [x[0] for x in tagTuple] )
colourTuple = ("#F34A33", "#E9D14B", "#6CAD4A")

# Show a custom layout of a 3D view on top of the (yet-to-be) specified slice view
customLayoutTemplate = """
&lt;layout type="horizontal" split="true"&gt;
  &lt;item&gt;
  &lt;view class="vtkMRMLViewNode" singletontag="1"&gt;
    &lt;property name="viewlabel" action="default"&gt;1&lt;/property&gt;
  &lt;/view&gt;
  &lt;/item&gt;
  &lt;item&gt;
  &lt;view class="vtkMRMLSliceNode" singletontag="{tag}"&gt;
    &lt;property name="orientation" action="default"&gt;{ori}&lt;/property&gt;
    &lt;property name="viewlabel" action="default"&gt;{lab}&lt;/property&gt;
    &lt;property name="viewcolor" action="default"&gt;{col}&lt;/property&gt;
  &lt;/view&gt;
  &lt;/item&gt;
&lt;/layout&gt;
"""

# Built-in layout IDs are all below 100, so you can choose any large random number
# for your custom layout ID.
customLayoutIdBase = 500

layoutManager = slicer.app.layoutManager()

### Iterate over new views

for i, (t, o, l, c) in enumerate(zip(tagTuple, orientationTuple, labelTuple, colourTuple), start=1):
    # Define new views
    customLayoutId = customLayoutIdBase + i
    customLayout = customLayoutTemplate.format(tag=t, ori=o, lab=l, col=c)
    layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)
    # Add button to layout selector toolbar for this custom layout
    viewToolBar = mainWindow().findChild("QToolBar", "ViewToolBar")
    layoutMenu = viewToolBar.widgetForAction(viewToolBar.actions()[0]).menu()
    layoutSwitchActionParent = layoutMenu  # use `layoutMenu` to add inside layout list, use `viewToolBar` to add next the standard layout list
    layoutSwitchAction = layoutSwitchActionParent.addAction("Two-up (3D and " + t + ")") # add inside layout list
    layoutSwitchAction.setData(customLayoutId)
    layoutSwitchAction.setIcon(qt.QIcon(":Icons/Go.png"))
    layoutSwitchAction.setToolTip("3D and " + o + " slice view")


### Switch to the last new custom layout
layoutManager.setLayout(customLayoutId)
</code></pre>

---

## Post #7 by @lassoan (2022-03-25 14:41 UTC)

<p>Thanks for sharing the script. Alternatively, you could add just one new layout, containing a “tabbed slice view” and “3D view” side by side. Something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce0e652a5240b636454d81c8a8d16d38d05b2a40.jpeg" data-download-href="/uploads/short-url/toRcqtKY2zmKaEiQBcuKCp4f4gE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce0e652a5240b636454d81c8a8d16d38d05b2a40_2_689x315.jpeg" alt="image" data-base62-sha1="toRcqtKY2zmKaEiQBcuKCp4f4gE" width="689" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce0e652a5240b636454d81c8a8d16d38d05b2a40_2_689x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce0e652a5240b636454d81c8a8d16d38d05b2a40_2_1033x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce0e652a5240b636454d81c8a8d16d38d05b2a40.jpeg 2x" data-dominant-color="67687E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1181×540 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @DIV (2022-03-26 07:26 UTC)

<p>That’s good too. (Although I’m not sure how to make the tabs — never even saw/noticed them before on any other view.)</p>
<hr>
<p>Actually, another way is to just make the one basic (untabbed) two-up view and then manually adjust the orientation from the drop-down menu.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e5facc9a62aa1f1aae291d6428b9a7c1f133ca8.png" alt="image" data-base62-sha1="8TMAjQcv7iJbXMrLmVmD4b4EzNu" width="217" height="130"></p>
<p>That workflow is almost as efficient as defining three distinct two-up views:  hover or click to display menu bar, click to display drop-down list, click to choose VERSUS click to display list of views, click to choose.<br>
However, it breaks the correspondence between slice colour and slice orientation.</p>
<hr>
<p>On reflection, the tabbed view maintains slice colour–orientation correspondence, and <em>potentially</em> has the most efficient workflow (fewest clicks) — depending on how the user likes to work.  For instance, if the user were mostly using one of the two-up combinations, then just clicking the tab is a one-click process.  Conversely, if the user were regularly swapping between (say) four-up and two-up views, then the tabbed set-up might actually add an extra click:  e.g. select four-up; [do work]; select two-up (defaulting to Red slice), then click tab to get Green slice; [do work]; return to four-up; [do work]; select two-up (defaulting to Red or Green* slice), then click tab to get Yellow slice; [do work]; <em>etc.</em>.</p>
<p>—DIV</p>
<p>*Presumably there could be a way of either setting one tab as a constant default, or else to display the most recently displayed tab (within a session, at least).</p>

---

## Post #9 by @lassoan (2022-11-17 20:23 UTC)

<p>A post was split to a new topic: <a href="/t/display-two-sagittal-views/26292">Display two sagittal views</a></p>

---
