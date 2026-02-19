---
topic_id: 19544
title: "Does Webwidgets Printtopdf Work On Mac"
date: 2021-09-07
url: https://discourse.slicer.org/t/19544
---

# Does WebWidget's printToPdf work on Mac?

**Topic ID**: 19544
**Date**: 2021-09-07
**URL**: https://discourse.slicer.org/t/does-webwidgets-printtopdf-work-on-mac/19544

---

## Post #1 by @mau_igna_06 (2021-09-07 13:37 UTC)

<p>Hi. I would like to know if this script to create a pdfReport with a webwidget works on Mac (it does work on Windows):</p>
<pre><code class="lang-auto">#get/create directories/paths
import os

desktopPath = os.path.join(os.path.expanduser("~"), "Desktop")
reportFolderPath = os.path.join(desktopPath, "ReportFolder")

if not os.path.exists(reportFolderPath):
    os.makedirs(reportFolderPath)

reportPath = os.path.join(
    reportFolderPath, "PDFReport.pdf"
)

import tempfile
tempFolderPath = tempfile.mkdtemp()

pdfReportPicturePath = os.path.join(
    tempFolderPath, "pdfReportPicture.png"
)

#load CT
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
ct = sampleDataLogic.downloadCTChest()

#take report picture
import ScreenCapture

redSliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")

screenCaptureLogic = ScreenCapture.ScreenCaptureLogic()
view = screenCaptureLogic.viewFromNode(redSliceNode)
screenCaptureLogic.captureImageFromView(view, pdfReportPicturePath)

#create html code
_html = f"""
        &lt;html&gt;
        &lt;body&gt;
        &lt;h1&gt;Test PDF Report&lt;/h1&gt;
        &lt;img src="{pdfReportPicturePath}" alt="" border=3 width=300&gt;&lt;/img&gt;
        &lt;br&gt;
        &lt;/body&gt;
        &lt;/html&gt;
        """

#create html file
htmlPath = os.path.join(tempFolderPath, "pdfReport.html")
file = qt.QFile(htmlPath)
file.open(qt.QIODevice.WriteOnly | qt.QIODevice.Text)
file.write(_html)
file.close()

#page layout for the pdf
pageLayout = qt.QPageLayout(
    qt.QPageSize(qt.QPageSize.A4),
    qt.QPageLayout.Portrait,
    qt.QMarginsF(15, 15, 0, 15),
    qt.QPageLayout.Millimeter,
)

#create webwidget, load html page, print pdf and open it
webWidget = slicer.qSlicerWebWidget()

def onWebWidgetLoadFinished(result):
    webWidget.loadFinished.disconnect(onWebWidgetLoadFinished)
    webWidget.pdfPrintingFinished.connect(onWebWidgetPDFPrintingFinished)
    webWidget.printToPdf(reportPath, pageLayout)

def onWebWidgetPDFPrintingFinished(filePath, result):
    webWidget.pdfPrintingFinished.disconnect(
        onWebWidgetPDFPrintingFinished
    )
    #
    from shutil import rmtree
    #
    rmtree(tempFolderPath, ignore_errors=True)
    #
    # Open in PDF viewer
    print("Starting '" + reportPath + "' ...")
    # slash/backlash replacements because of active directory
    import subprocess
    #
    subprocess.Popen([reportPath], shell=True)

webWidget.loadFinished.connect(onWebWidgetLoadFinished)
webWidget.setUrl(htmlPath.replace("\\", "/"))
</code></pre>
<p>If it doesn’t work on Mac, do you know any workaround to make it work?</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @pieper (2021-09-07 14:03 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="19544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>If it doesn’t work on Mac, do you know any workaround to make it work?</p>
</blockquote>
</aside>
<p>With today’s nightly it runs but the webWidget and the pdf are blank.</p>
<p>Changing the last line to this works:</p>
<pre><code class="lang-auto">webWidget.url = "file://" + htmlPath.replace("\\", "/")
</code></pre>

---

## Post #3 by @mau_igna_06 (2021-09-07 14:13 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>Is there any function I can call to check in what OS Slicer is running on?</p>

---

## Post #4 by @mau_igna_06 (2021-09-07 14:20 UTC)

<blockquote>
<p>Is there any function I can call to check in what OS Slicer is running on?</p>
</blockquote>
<p><code>slicer.app.os</code></p>

---

## Post #5 by @pieper (2021-09-07 14:29 UTC)

<p>You don’t need to do anything different based on the os - the <code>file://</code> should also work on windows.</p>

---

## Post #6 by @mau_igna_06 (2021-09-07 14:49 UTC)

<p>In my PC it doesn’t work with that change. Here is the <a href="https://gofile.io/d/aUUz0j" rel="noopener nofollow ugc">result</a>.</p>
<p>What is the return of this function <code>slicer.app.os</code> on mac?</p>

---

## Post #7 by @pieper (2021-09-07 14:57 UTC)

<p>Looks like <code>file:///</code> is the right thing - it works on mac and should also work on windows.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="6" data-topic="19544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>What is the return of this function <code>slicer.app.os</code> on mac?</p>
</blockquote>
</aside>
<p>But if you really need it:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.app.os
'macosx'
</code></pre>

---

## Post #8 by @lassoan (2021-09-08 03:03 UTC)

<p>There is no need to implement such low-level logic. You can simply use the <code>QUrl</code> class to get URL from local file path:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; qt.QUrl.fromLocalFile(r"c:\tmp").toString()
'file:///c:/tmp'
</code></pre>

---
