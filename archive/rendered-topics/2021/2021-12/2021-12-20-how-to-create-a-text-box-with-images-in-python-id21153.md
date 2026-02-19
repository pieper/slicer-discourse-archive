---
topic_id: 21153
title: "How To Create A Text Box With Images In Python"
date: 2021-12-20
url: https://discourse.slicer.org/t/21153
---

# How to create a text box with images in python

**Topic ID**: 21153
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/how-to-create-a-text-box-with-images-in-python/21153

---

## Post #1 by @tsims (2021-12-20 19:15 UTC)

<p>Hi everyone,</p>
<p>as part of a slicer extension I am working on I was hoping to create a section where I could place demonstration images and text to serve as sort of tutorial to people using the modules, something like the “Acknowledgement” section, but wasn’t sure which QT widget I should be using to achieve that result? Any advice would be appreciated!</p>
<p>The effect that I want is similar to this image:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e88ece51b9e187dd69d4a410de4eb442ac8ff9c.png" alt="SlicerAcknowledgement" data-base62-sha1="8VcXNeMc7kISZRK1KptzF8tDy32" width="593" height="225"></p>

---

## Post #2 by @lassoan (2021-12-21 15:01 UTC)

<p>The simplest is to use QTextEdit:</p>
<pre data-code-wrap="python"><code class="lang-python">html="""
&lt;p&gt;This is an image:&lt;/p&gt;
&lt;p&gt;&lt;img src="file:Markups-copy-paste.png" width="100"&gt;&lt;/p&gt;
&lt;p&gt;Another image:&lt;/p&gt;
&lt;p&gt;&lt;img src="file:ClippingFanMask.png" width="100"&gt;&lt;/p&gt;
&lt;p&gt;And some more text.&lt;/p&gt;
"""

resourceFolder = "c:/tmp/20211221/"

resourceFiles = [
    "Markups-copy-paste.png",
    "ClippingFanMask.png"
]

textEdit = qt.QTextEdit()
textEdit.readOnly=True
textEdit.setHtml(html)
textDocument = textEdit.document
for resourceFile in resourceFiles:
    resourceFilePath = resourceFolder+resourceFile
    uri = qt.QUrl().fromLocalFile(resourceFile)
    image = qt.QImage()
    image.load(resourceFilePath)
    textDocument.addResource(qt.QTextDocument.ImageResource, uri, image)

textEdit.show()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/017b5f77dd53a22df0fa8de39d633d268946c1c6.png" data-download-href="/uploads/short-url/d6NLJ1Jfmj5txZ93OsBolI2jJ4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/017b5f77dd53a22df0fa8de39d633d268946c1c6.png" alt="image" data-base62-sha1="d6NLJ1Jfmj5txZ93OsBolI2jJ4" width="308" height="500" data-dominant-color="56585B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">430×697 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For rendering complex tables, videos, using dynamic content (Javascript), etc. you can use the heavyweight <a href="https://apidocs.slicer.org/master/classqSlicerWebWidget.html"><code>slicer.qSlicerWebWidget()</code></a>, which is a thin wrapper over QWebEngineView.</p>

---
