---
topic_id: 16178
title: "Showing A Qmrrmlwidget Instead Of The View Layout"
date: 2021-02-24
url: https://discourse.slicer.org/t/16178
---

# Showing a qMRRMLWidget instead of the view layout

**Topic ID**: 16178
**Date**: 2021-02-24
**URL**: https://discourse.slicer.org/t/showing-a-qmrrmlwidget-instead-of-the-view-layout/16178

---

## Post #1 by @pll_llq (2021-02-24 13:17 UTC)

<p>Hi <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20"></p>
<p>I want to display a widget that will takes the space used by the view layout.<br>
As I understand after reading <a href="https://discourse.slicer.org/t/how-to-include-qwidgets-in-slicer-qml-layout/13259">reply to this post</a> I can’t have a QMRMLWidget as a part of a custom layout.</p>
<p>I tried to manually set my widget to be the <code>centralWidget</code> of the <code>mainWindow</code> with</p>
<pre><code class="lang-python">mainWindow = slicer.util.mainWindow()
mainWindow.setCentralWidget(mywidget)
</code></pre>
<p>and I see the result, but the existing layout manager get’s destroyed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/313fe76ec4bbc9b16b809ee98859d2a407846e9a.png" data-download-href="/uploads/short-url/71GjcVbe30guIjAUyjwk1hORPpE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/313fe76ec4bbc9b16b809ee98859d2a407846e9a_2_690x492.png" alt="image" data-base62-sha1="71GjcVbe30guIjAUyjwk1hORPpE" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/313fe76ec4bbc9b16b809ee98859d2a407846e9a_2_690x492.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/313fe76ec4bbc9b16b809ee98859d2a407846e9a_2_1035x738.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/313fe76ec4bbc9b16b809ee98859d2a407846e9a_2_1380x984.png 2x" data-dominant-color="F1F1F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1684×1202 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So when I try to revert to a view layout I am met with an error:</p>
<pre data-code-wrap="log"><code class="lang-plaintext">ValueError: Trying to call 'setLayout' on a destroyed qSlicerLayoutManager object
</code></pre>
<p><a href="https://gist.github.com/piiq/62df9c295d4467c2712760dc0ab0747e" rel="noopener nofollow ugc">Here’s the sample code</a>. Copy-paste into Slicer python interpreter works.</p>
<p>I guess that setting the centralWidget like that is not a good idea. Can anyone advice how to correctly show my widget in the middle of the main window?</p>

---

## Post #2 by @lassoan (2021-02-24 13:37 UTC)

<p>Custom widgets are placed inside the view layout. The simplest way is to use <code>qSlicerSingletonViewFactory</code> as it is done in the DICOM module.</p>

---

## Post #3 by @pll_llq (2021-02-24 13:39 UTC)

<p>Thanks, this something that I wanted to try.</p>

---

## Post #4 by @pll_llq (2021-02-24 16:24 UTC)

<p>Thanks, it worked.</p>
<p>I’ve added</p>
<pre><code class="lang-auto">viewFactory = slicer.qSlicerSingletonViewFactory()
viewFactory.setWidget(mywidget)
viewFactory.setTagName("helloLayout")
layoutManager.registerViewFactory(viewFactory)

layout = (
    "&lt;layout type=\"horizontal\"&gt;"
    " &lt;item&gt;"
    "  &lt;helloLayout&gt;&lt;/helloLayout&gt;"
    " &lt;/item&gt;"
    "&lt;/layout&gt;"
)

customLayoutId = 42

layoutNode = slicer.app.layoutManager().layoutLogic().GetLayoutNode()
layoutNode.AddLayoutDescription(customLayoutId, layout)

layoutManager.setLayout(customLayoutId)
</code></pre>
<p>instead of manipulating the centralWidget and got a nice layout with my widget.</p>

---
