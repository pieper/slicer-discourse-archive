# Input option from command line

**Topic ID**: 23991
**Date**: 2022-06-21
**URL**: https://discourse.slicer.org/t/input-option-from-command-line/23991

---

## Post #1 by @bserrano (2022-06-21 16:01 UTC)

<p>Hi,</p>
<p>I am working on a script and I need to ask the user some parameters. I am using the function input:</p>
<pre><code class="lang-auto">def func():
     option1 = input("Bla bla")
     option2 = input("Bla bla")
     option3 = input("Bla bla")
</code></pre>
<p>The first input is working but the following ones don’t. What I am doing wrong?<br>
Same code works outside the function.</p>

---

## Post #2 by @lassoan (2022-06-21 16:41 UTC)

<p>You can use a nice GUI widget to get additional inputs.</p>
<p>For a single input you can do this:</p>
<pre><code class="lang-auto">result = qt.QInputDialog().getText(None, "Some Title","Some description")
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b748cdb00e333ef2f4b58beb532b7da8d2461cf.png" alt="image" data-base62-sha1="mbdImNfWUSkTSrP7bKhbpqOsxTV" width="202" height="106"></p>
<p>If you need multiple inputs then you can put together a dialogbox with a few fields in 10-15 lines of Python code; or create a dialog in Qt Designer (menu: Edit / Application settings / Developer / Qt Designer → launch):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f0a19bcee0f148daee8bbde32edc8785b1089da.png" data-download-href="/uploads/short-url/mGVyBmqDxINjgDNH130Q2rYJD7k.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0a19bcee0f148daee8bbde32edc8785b1089da_2_690x356.png" alt="image" data-base62-sha1="mGVyBmqDxINjgDNH130Q2rYJD7k" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0a19bcee0f148daee8bbde32edc8785b1089da_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0a19bcee0f148daee8bbde32edc8785b1089da_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0a19bcee0f148daee8bbde32edc8785b1089da_2_1380x712.png 2x" data-dominant-color="DADBD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1390×718 69.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can display the dialog and get the entered values like this:</p>
<pre data-code-wrap="python"><code class="lang-python">widget = slicer.util.loadUI(r'c:\D\S4\Base\QTGUI\Resources\UI\qSlicerSettingsUserInformationPanel.ui')
widget.show()
ui = slicer.util.childWidgetVariables(widget)
print(ui.NameLineEdit.text)
</code></pre>
<p>This widget does not have an OK/Cancel button but you can add them in Qt Designer.</p>

---

## Post #3 by @jcfr (2022-06-21 18:24 UTC)

<p>We could also look into overriding the <code>input</code> and <code>raw_input</code> built-in function to display a dialog when running without <code>--testing</code> flag.</p>
<p>That said, to be robust, modules should provide default values and nicely handle the case of being executed as self-test.</p>

---
