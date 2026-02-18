# Inline documentation options

**Topic ID**: 41032
**Date**: 2025-01-10
**URL**: https://discourse.slicer.org/t/inline-documentation-options/41032

---

## Post #1 by @muratmaga (2025-01-10 19:45 UTC)

<p>For SlicerMorph, we maintain a tutorials page as a github repo:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerMorph/Tutorials/">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/37d522cebf531fac1142beb29e490093/SlicerMorph/Tutorials" class="thumbnail">

  <h3><a href="https://github.com/SlicerMorph/Tutorials/" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a></h3>

    <p><span class="github-repo-description">SlicerMorph module tutorials</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I want to have a Tutorials module within SlicerMorph so that people can navigate to this site easily (or be aware of its existence). I can of course simply point this out as a URL in a basic module interface. But given that we have nice <a href="https://github.com/SlicerMorph/Tutorials?tab=readme-ov-file#slicermorph-tutorials" rel="noopener nofollow ugc">README.MD file with links to the tutorials</a>, I am wondering if there is a way to import this dynamically? I.e., I do not want to replicate the contents of the README.MD as part of the module help page (too much duplicated work).</p>
<p>I guess I am looking into something like making a snapshot of this README during module build and rendered with clickable links…</p>
<p>I am still fuzzy on details, so can use suggestions.</p>

---

## Post #2 by @pieper (2025-01-10 20:29 UTC)

<p>Well you could bundle the contents of the tutorials (either just the readme or the full repo contents) when the extension is built or you could assume people will have internet when they use it and fetch dynamically.</p>
<p>Do you want to show the tutorials in a web view that can interact somehow with Slicer or just have them in an independent system browser?</p>

---

## Post #3 by @muratmaga (2025-01-10 21:32 UTC)

<p>This is sort of what I want to, when I choose SlicerMorph-&gt;Tutorials from the module panel, this page shows up like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3e4b3ff0cf32da75e34de6b52c71a341f367cf2.png" data-download-href="/uploads/short-url/pFpsBu9GAJ0pDohZ9bxYnDA2A9A.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3e4b3ff0cf32da75e34de6b52c71a341f367cf2_2_600x500.png" alt="image" data-base62-sha1="pFpsBu9GAJ0pDohZ9bxYnDA2A9A" width="600" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3e4b3ff0cf32da75e34de6b52c71a341f367cf2_2_600x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3e4b3ff0cf32da75e34de6b52c71a341f367cf2_2_900x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3e4b3ff0cf32da75e34de6b52c71a341f367cf2_2_1200x1000.png 2x" data-dominant-color="9596A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1278×1064 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then clicking on a link, opens the tutorial in the system registered web browser.</p>
<p>I am not interested in offline availability or want to use the internal browser.</p>

---

## Post #4 by @pieper (2025-01-10 21:47 UTC)

<p>If you are using the external browser I think it would be much easier just to open the readme page in the external browser.  So you would just open that from a button in Slicer.  Otherwise you’l be messing with getting the rendered markdown into a Slicer widget and handling links, which can be done (most easily with a webwidget) but it doesn’t look like it buys you much.</p>

---

## Post #5 by @muratmaga (2025-01-10 21:50 UTC)

<p>That means you need</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="41032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>open the readme page in the external browser.</p>
</blockquote>
</aside>
<p>true, but that means you know the URL before hand. Point of this is increasing the discoverability of the content.</p>

---

## Post #6 by @muratmaga (2025-01-10 22:00 UTC)

<p>For example. I can have convert the README.MD to html via tool, and dump it in the <code>self.parent.helpText =</code> field, which gives me this. But I want this to be in the module panel, and not the help field which is almost always overlooked.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8469a6f0438116b77355fe4c3bb2a7d9ee12bdd.png" data-download-href="/uploads/short-url/qib7wrc3CoaHiY1GeKKzzOGFOUJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8469a6f0438116b77355fe4c3bb2a7d9ee12bdd_2_266x500.png" alt="image" data-base62-sha1="qib7wrc3CoaHiY1GeKKzzOGFOUJ" width="266" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8469a6f0438116b77355fe4c3bb2a7d9ee12bdd_2_266x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8469a6f0438116b77355fe4c3bb2a7d9ee12bdd_2_399x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8469a6f0438116b77355fe4c3bb2a7d9ee12bdd_2_532x1000.png 2x" data-dominant-color="BCC3D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1314×2466 493 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pieper (2025-01-10 22:03 UTC)

<p>yes, that’s what I was would be the easiest, just to use an html widget in Slicer (could be a full web widget or just a simpler html render) but you need to integrate a markdown to html converter somewhere, either in slicer or in your build process or fetch the html from github when you open the module.</p>

---

## Post #8 by @muratmaga (2025-01-10 22:09 UTC)

<p>Supposedly QT support markdown? <a href="https://doc.qt.io/qt-5/qtextedit.html#markdown-prop" class="inline-onebox" rel="noopener nofollow ugc">QTextEdit Class | Qt Widgets 5.15.18</a></p>

---

## Post #9 by @pieper (2025-01-10 22:21 UTC)

<p>I didn’t know about that and it might work, but remember there are ‘<a href="https://gist.github.com/vimtaai/99f8c89e7d3d02a362117284684baa0f">flavors</a>’ of markdown and that could bite you at some point (looks like Qt supports a basic one).  In any case you can get the contents either at build time or run time.</p>

---

## Post #10 by @muratmaga (2025-01-10 22:30 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="41032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>there are ‘<a href="https://gist.github.com/vimtaai/99f8c89e7d3d02a362117284684baa0f" rel="noopener nofollow ugc">flavors</a>’ of markdown and that could bite you at some point</p>
</blockquote>
</aside>
<p>True. But I think we use a very minimal and fairly standard subset on that Readme.<br>
Mostly heading levels #, ##, ###, emphasis (**), and link.</p>

---

## Post #11 by @muratmaga (2025-01-11 04:12 UTC)

<p>I used Bing Chat to build the module. Seems to work, but can’t quite get it to use the full height of the module panel</p>
<pre><code class="lang-auto">import os
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import mistune
import requests
import webbrowser

class SlicerMorphTutorials(ScriptedLoadableModule):

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "SlicerMorph Tutorials"
        self.parent.categories = ["Examples"]
        self.parent.dependencies = []
        self.parent.contributors = ["Your Name (Your Institution)"]
        self.parent.helpText = """This is an example of a scripted module that displays Markdown text in a QTextBrowser."""
        self.parent.acknowledgementText = """This file was originally developed by Your Name, Your Institution."""

class SlicerMorphTutorialsWidget(ScriptedLoadableModuleWidget):

    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)

        # URL of the Markdown file
        markdown_url = "https://raw.githubusercontent.com/SlicerMorph/Tutorials/main/README.md"

        # Fetch the Markdown content
        response = requests.get(markdown_url)
        markdown_text = response.text

        # Create a Markdown renderer
        renderer = mistune.create_markdown()

        # Convert Markdown to HTML
        html_content = renderer(markdown_text)

        # Add some basic styling for better display
        styled_html_content = f"""
        &lt;html&gt;
        &lt;head&gt;
        &lt;style&gt;
        body {{ font-family: Arial, sans-serif; }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: disc; padding-left: 20px; }}
        li {{ margin: 5px 0; }}
        &lt;/style&gt;
        &lt;/head&gt;
        &lt;body&gt;
        {html_content}
        &lt;/body&gt;
        &lt;/html&gt;
        """

        # Create a QTextBrowser widget
        self.textWidget = qt.QTextBrowser()
        self.textWidget.setReadOnly(True)
        self.textWidget.setOpenExternalLinks(True)  # Ensure external links open in the default web browser

        # Set the styled HTML content in the QTextBrowser widget
        self.textWidget.setHtml(styled_html_content)

        # Create a vertical layout for the widget
        layout = qt.QVBoxLayout()

        # Add the QTextBrowser widget with full stretch factor
        layout.addWidget(self.textWidget)

        # Set the layout for the module
        self.layout.addLayout(layout)

    def cleanup(self):
        pass

class SlicerMorphTutorialsLogic(ScriptedLoadableModuleLogic):
    pass

class SlicerMorphTutorialsTest(ScriptedLoadableModuleTest):
    def runTest(self):
        self.setUp()
        self.test_SlicerMorphTutorials1()

    def test_SlicerMorphTutorials1(self):
        self.delayDisplay("Starting the test")
        self.delayDisplay('Test passed!')


</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f47b1b88726cdc6f54390d4dfde997183c6a55d1.png" data-download-href="/uploads/short-url/ySMg5wgOyxoTQmJj0k7hUHWoceZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f47b1b88726cdc6f54390d4dfde997183c6a55d1_2_252x500.png" alt="image" data-base62-sha1="ySMg5wgOyxoTQmJj0k7hUHWoceZ" width="252" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f47b1b88726cdc6f54390d4dfde997183c6a55d1_2_252x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f47b1b88726cdc6f54390d4dfde997183c6a55d1_2_378x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f47b1b88726cdc6f54390d4dfde997183c6a55d1_2_504x1000.png 2x" data-dominant-color="E5E5F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">706×1398 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @Thibault_Pelletier (2025-01-13 07:55 UTC)

<p>If you want to package the exact version of the tutorial the module was built with, it may be worthwhile to package the sphinx HTML documentation directly with the module during the build / install step in the CI. (it would also be useful for offline usage).</p>
<p>For the height of the widget, maybe changing the size policy to MinimumExpanding could help.</p>

---

## Post #13 by @shai-ikko (2025-01-13 09:14 UTC)

<p>Python stdlib has a module called “webbrowser”. You can do this:</p>
<pre data-code-wrap="python"><code class="lang-python">import webbrowser
webbrowser.open("https://slicer.org")
</code></pre>
<p>and it opens a web page in your external browser. This works from within Slicer (for me on Linux, but I expect elsewhere too), so you could trigger that from a button in your module. The users don’t need to know the URL in advance.</p>
<p>I thought this was what <a class="mention" href="/u/pieper">@pieper</a> meant in the message you replied to.</p>

---
