# Handling Slicer Close Event During MorphoSourceImport Module Download

**Topic ID**: 33474
**Date**: 2023-12-20
**URL**: https://discourse.slicer.org/t/handling-slicer-close-event-during-morphosourceimport-module-download/33474

---

## Post #1 by @oothomas (2023-12-20 20:36 UTC)

<p>Hello,</p>
<p>I’m currently working with the MorphoSourceImport module in SlicerMorph, which utilizes a separate QProcess to download data. I’ve encountered a scenario where a user might try to close 3D Slicer while a download is still ongoing. I’m looking for advice on the best approach to intercept this close event.</p>
<p>Specifically, I want to prompt the user with a notification about the active download and give them the option to either proceed with closing Slicer or keep it open until the download completes. Any insights or suggestions on how to effectively implement this functionality would be greatly appreciated.</p>
<p>Thank you in advance for your help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7927d8e3ceb0e5394e398b478a70c96f2d637dad.png" data-download-href="/uploads/short-url/hhN942weLMtSxfdunoYGNR7ZFN3.png?dl=1" title="InProgress Download" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7927d8e3ceb0e5394e398b478a70c96f2d637dad_2_377x500.png" alt="InProgress Download" data-base62-sha1="hhN942weLMtSxfdunoYGNR7ZFN3" width="377" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7927d8e3ceb0e5394e398b478a70c96f2d637dad_2_377x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/7927d8e3ceb0e5394e398b478a70c96f2d637dad_2_565x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7927d8e3ceb0e5394e398b478a70c96f2d637dad.png 2x" data-dominant-color="E6E6E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">InProgress Download</span><span class="informations">619×820 97.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-12-21 17:39 UTC)

<p>You can customize the behavior of application closing as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#override-application-close-behavior">this example in the script repository</a>.</p>

---

## Post #3 by @oothomas (2023-12-21 18:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="33474">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>this example in the script repository</p>
</blockquote>
</aside>
<p>Thank you! This helps a lot!</p>

---

## Post #4 by @oothomas (2023-12-22 00:25 UTC)

<p>Here’s my event filter class:</p>
<pre><code class="lang-auto">class CloseApplicationEventFilter(qt.QWidget):
    def __init__(self, morphoSourceImportWidget, parent=None):
        super(CloseApplicationEventFilter, self).__init__(parent)
        self.morphoSourceImportWidget = morphoSourceImportWidget

    def eventFilter(self, object, event):
        if event.type() == qt.QEvent.Close:
            if self.morphoSourceImportWidget.downloadInProgress:
                userChoice = qt.QMessageBox.question(
                    self, "Download in Progress",
                    "A download is currently in progress. Would you like to stop the download and close the application?",
                    qt.QMessageBox.Yes | qt.QMessageBox.No, qt.QMessageBox.No
                )
                if userChoice == qt.QMessageBox.Yes:
                    self.morphoSourceImportWidget.terminateDownload()
                    event.accept()
                    return True
                else:
                    event.ignore()
                    return True
            else:
                event.accept()
                return True
        return False
</code></pre>
<p>I then add this to the setup method of my widget:</p>
<blockquote>
<p>morphoSourceImportWidget = self<br>
event_filter = CloseApplicationEventFilter(morphoSourceImportWidget)<br>
slicer.util.mainWindow().installEventFilter(event_filter)</p>
</blockquote>
<p>This doesn’t seem to work so far. Am I implementing this correctly?</p>

---

## Post #5 by @lassoan (2023-12-22 03:34 UTC)

<p>It seems that you create the event filter object and store it in a local variable of the <code>setup</code> method. As soon as the <code>setup</code> method returns, all local variables, including your event filter gets deleted. Probably storing the event filter object in a member variable (<code>self.eventFilter = CloseApplicationEventFilter(...)</code>) will make it work.</p>

---

## Post #6 by @oothomas (2023-12-22 03:47 UTC)

<p>Ah. Rookie mistake, lol. Thank you. Worked like a charm!</p>

---
