# Custom Python QDialog crash

**Topic ID**: 9899
**Date**: 2020-01-21
**URL**: https://discourse.slicer.org/t/custom-python-qdialog-crash/9899

---

## Post #1 by @Johan_Andruejol (2020-01-21 20:22 UTC)

<p>Hi everyone !</p>
<p>I am trying to create a custom QDialog in Python. Whenever you add a custom signal/slot connection, the application crashes on exit.</p>
<p>Here is the minimal example you can reproduce the crash with, following the steps:</p>
<ul>
<li>Open Slicer</li>
<li>Run the python code below:</li>
</ul>
<blockquote>
<pre><code>class CustomDialog(qt.QDialog):
    def __init__(self, parent = None):
        qt.QDialog.__init__(self, parent)
        self.connect('accepted()', self.myCustomSlot)
    def myCustomSlot(self):
        print("Doesn't matter")

w = CustomDialog()
w.open()
</code></pre>
</blockquote>
<ul>
<li>Exit Slicer<br>
 → <strong>CRASH</strong> <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></li>
</ul>
<p>Has someone else encountered something like this ? I managed to reproduce it in the nightly and in an older windows build (2019-08-20 hash: 499d10b035181586489f5e3d60ff486a136a12bb).</p>
<p>Thanks !</p>
<p>P.S.: Here is an example of the call-stack after the crash: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72277666d7953d90b3b34e6d8a668dd964833154.png" data-download-href="/uploads/short-url/ghQYJOSlVQ6vEREoL5nVUz085P6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72277666d7953d90b3b34e6d8a668dd964833154_2_690x259.png" alt="image" data-base62-sha1="ghQYJOSlVQ6vEREoL5nVUz085P6" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72277666d7953d90b3b34e6d8a668dd964833154_2_690x259.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72277666d7953d90b3b34e6d8a668dd964833154_2_1035x388.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72277666d7953d90b3b34e6d8a668dd964833154_2_1380x518.png 2x" data-dominant-color="F2F2EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1631×613 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2020-01-21 20:39 UTC)

<p>I’m currently unable to replicate the crash using today’s Slicer nightly (28737) built by the factory machine on Windows 10.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input: class CustomDialog(qt.QDialog):
[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input:     def __init__(self, parent = None):
[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input:         qt.QDialog.__init__(self, parent)
[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input:         self.connect('accepted()', self.myCustomSlot)
[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input:     def myCustomSlot(self):
[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input:         print("Doesn't matter")
[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input: w = CustomDialog()
[DEBUG][Qt] 21.01.2020 15:37:22 [] (unknown:0) - Python console user input: w.open()
[DEBUG][Qt] 21.01.2020 15:37:34 [] (unknown:0) - Python console user input: w.accept()
[INFO][Stream] 21.01.2020 15:37:34 [] (unknown:0) - Doesn't matter
[DEBUG][Qt] 21.01.2020 15:38:17 [] (unknown:0) - Python console user input: slicer.app.repositoryRevision
[INFO][Stream] 21.01.2020 15:38:17 [] (unknown:0) - '28737'
</code></pre>

---

## Post #3 by @lassoan (2020-01-22 00:55 UTC)

<p>You need to disconnect all signals and delete all widget instances before application shutdown (while the widget that you created in the above example is kept alive forever by the global Python variable).</p>
<p>The <a href="https://github.com/Slicer/Slicer/blob/4db181a73e03b3a2c8044ffd4e4174d873b267c3/Base/Python/slicer/ScriptedLoadableModule.py#L99-L106">module widget’s cleanup method</a> is added exactly for performing this kind of cleanup.</p>

---

## Post #4 by @Johan_Andruejol (2020-01-22 20:13 UTC)

<p>Following your suggestion, I realized that my mistake came from having the QDialog un-parented. Here is what I ended up doing:</p>
<pre><code>class CustomDialog(qt.QDialog):
    def __init__(self, parent = None):
        qt.QDialog.__init__(self, parent)
        self.connect('accepted()', self.myCustomSlot)
    def myCustomSlot(self):
        pass

w = CustomDialog(slicer.util.mainWindow()) # Parent could be your module GUI
w.show()
</code></pre>
<p>No more crash, the dialog is properly deleted when the application exits, also no need to worry about the dialog life-cycle.</p>
<p>Thanks a lot for your help !</p>

---

## Post #5 by @lassoan (2020-01-22 20:37 UTC)

<p>Parent widget deletes all child widgets in its destructor. Probably that’s why you don’t need to delete your widget manually when you set the main window as parent.</p>

---
