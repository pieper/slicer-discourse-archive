---
topic_id: 17926
title: "Using Native File Dialog For Selecting Files And Folders"
date: 2021-06-01
url: https://discourse.slicer.org/t/17926
---

# Using native file dialog for selecting files and folders

**Topic ID**: 17926
**Date**: 2021-06-01
**URL**: https://discourse.slicer.org/t/using-native-file-dialog-for-selecting-files-and-folders/17926

---

## Post #1 by @tbillah (2021-06-01 20:58 UTC)

<p>In <code>fsleyes</code> I can load data from the terminal:</p>
<blockquote>
<p>fsleyes img1.nii.gz img2.nii.gz</p>
</blockquote>
<p>Can I do a similar thing with Slicer? I am asking because it is a little difficult to navigate to my required directory from within the GUI.</p>

---

## Post #2 by @lassoan (2021-06-02 13:35 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/loading-data-in-slicer-from-terminal/17912/5">Loading data in Slicer from terminal</a></p>

---

## Post #3 by @jamesobutler (2021-06-02 12:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="17912">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/loading-data-in-slicer-from-terminal/17912/6">Loading data in Slicer from terminal</a></div>
<blockquote>
<p>I usually drag-and-drop data into the application window and hit Enter to open it.</p>
</blockquote>
</aside>
<p>Users from my group almost exclusively do this because they hate using the standard QFileDialog to navigate to directories. They much prefer using the native file explorer to find the files they want to load. <a class="mention" href="/u/lassoan">@lassoan</a> I’m assuming this behavior of using drag-and-drop is also a result of this similar preference to the native file dialog over the QFileDialog?</p>
<p>Could we change to the following which uses native file explorer?</p>
<pre><code class="lang-auto">qfiledialog = qt.QFileDialog()
tuple_file_paths = qfiledialog.getOpenFileNames()  # Select file(s)
directory = qfiledialog.getExistingDirectory()  # Select directory
</code></pre>

---

## Post #4 by @lassoan (2021-06-02 13:39 UTC)

<p>I agree that Qt’s own (non-native) QFileDialog is not nice. It still the same as 10 years ago, while native file dialogs have improved substantially.</p>
<p>In the past, there were concerns in the past about limitations of the native dialog (e.g., on Mac filtered out files are shown as gray instead of being hidden), but I think those have been fixed since then, and the native file dialogs have more advantages anyway. Qt internal file dialogs also allow adding custom widgets inside, such as “Copy” checkbox in DICOM import file selector, but I think these cases should be possible to address using alternative designs.</p>
<p>I’m in favor of replacing Qt internal file dialogs by native ones (either by using the static methods you mentioned above <code>qt.QFileDialog.getOpenFileNames()</code> or by removing the <code>QFileDialog::DontUseNativeDialog</code> flag), but we should do it consistently, switching to native dialogs everywhere.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> could you review QFileDialog usages in Slicer and CTK and send a pull request that switches them to use native dialogs?</p>

---

## Post #5 by @jamesobutler (2021-06-04 15:42 UTC)

<p>Proposed usage of native dialogs instead of the Qt widget-based dialog has been posted at:<br>
<a href="https://github.com/Slicer/Slicer/pull/5674" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve directory and file selection by using native dialogs by jamesobutler · Pull Request #5674 · Slicer/Slicer · GitHub</a>.</p>

---
