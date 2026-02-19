---
topic_id: 24072
title: "3D Object Rotates When We Are Perform 3D Center Code In Cpp"
date: 2022-06-28
url: https://discourse.slicer.org/t/24072
---

# 3D object rotates when we are perform 3D center code in CPP

**Topic ID**: 24072
**Date**: 2022-06-28
**URL**: https://discourse.slicer.org/t/3d-object-rotates-when-we-are-perform-3d-center-code-in-cpp/24072

---

## Post #1 by @Prasun_Parmar (2022-06-28 06:07 UTC)

<p>Actually I want to have 3D view by default in center.</p>
<h1><a name="p-80124-try1-python-1" class="anchor" href="#p-80124-try1-python-1" aria-label="Heading link"></a>TRY:1 Python</h1>
<p>in the Script repository we are having this code.</p>
<pre><code class="lang-auto"># Center the 3D view on the scene¶
layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()
</code></pre>
<p>But this is rotating 3D object when we are clicking (Eye button) visible - invisible from segment table.</p>
<h1><a name="p-80124-try2-python-2" class="anchor" href="#p-80124-try2-python-2" aria-label="Heading link"></a>TRY:2 Python</h1>
<p>by pressing center 3D button programmatically.</p>
<pre><code class="lang-auto"># Center 3D View
slicer.app.layoutManager().threeDWidget(0).threeDController().BarWidget.CenterButton_Header.click()

</code></pre>
<h4><a name="p-80124-this-code-by-pressing-center-3d-button-has-solved-the-issue-of-rotation-in-python-files-3" class="anchor" href="#p-80124-this-code-by-pressing-center-3d-button-has-solved-the-issue-of-rotation-in-python-files-3" aria-label="Heading link"></a>This code by pressing center 3D button has solved the issue of rotation in python files.</h4>
<hr>
<hr>
<h1><a name="p-80124-try1-cpp-4" class="anchor" href="#p-80124-try1-cpp-4" aria-label="Heading link"></a>TRY:1 Cpp</h1>
<p>As we know segment table’s show 3D eye code is in the Cpp for that I have done.</p>
<pre><code class="lang-auto">//Center 3D View
      PythonQt::init();
      PythonQtObjectPtr openBrowserContext = PythonQt::self()-&gt;getMainModule();
      openBrowserContext.evalScript(QString(
        "from slicer.util import * \n"
        "mainWindow = slicer.util.mainWindow()\n"
        "print('Segment table visible button')\n"
        "slicer.app.layoutManager().threeDWidget(0).threeDController().BarWidget.CenterButton_Header.click()\n"));
</code></pre>
<p>This code makes 3D object in the center but when we are frequently pressing segment table’s eye button it rotates the 3D object in CW.</p>
<h2><a name="p-80124-can-you-please-share-any-better-approach-for-this-issue-5" class="anchor" href="#p-80124-can-you-please-share-any-better-approach-for-this-issue-5" aria-label="Heading link"></a>Can you please share any better approach for this issue.</h2>
<h1><a name="p-80124-reason-6" class="anchor" href="#p-80124-reason-6" aria-label="Heading link"></a>Reason:</h1>
<ul>
<li>its very annoying to press center 3D button all the time. So that’s way when I am loading or showing 3D object it should come to center.</li>
</ul>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2022-06-28 13:20 UTC)

<p>Thanks for the code snippets. They specify what code you have problem with, but it is not clear for me why you keep clicking the eye icons, why would you like to change the camera’s focal point, and why it causes problems for you.</p>
<p>Normaly you set the camera focal point to the center of the volume you have segmented and don’t change if after that programmatically.</p>
<p>Can you describe your workflow in a bit more detail? Is there anything special about it that makes it necessary to change the focal point frequently or you think that in general Slicer does not do a good job in setting the focal point?</p>

---
