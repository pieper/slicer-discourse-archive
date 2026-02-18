# Loading data in Slicer from terminal

**Topic ID**: 17912
**Date**: 2021-06-01
**URL**: https://discourse.slicer.org/t/loading-data-in-slicer-from-terminal/17912

---

## Post #1 by @tbillah (2021-06-01 20:58 UTC)

<p>In <code>fsleyes</code> I can load data from the terminal:</p>
<blockquote>
<p>fsleyes img1.nii.gz img2.nii.gz</p>
</blockquote>
<p>Can I do a similar thing with Slicer? I am asking because it is a little difficult to navigate to my required directory from within the GUI.</p>

---

## Post #2 by @lassoan (2021-06-02 13:33 UTC)

<p>3 posts were split to a new topic: <a href="/t/using-native-file-dialog-for-selecting-files-and-folders/17926">Using native file dialog for selecting files and folders</a></p>

---

## Post #4 by @lassoan (2021-06-02 13:36 UTC)

<p>A post was merged into an existing topic: <a href="/t/using-native-file-dialog-for-selecting-files-and-folders/17926/3">Using native file dialog for selecting files and folders</a></p>

---

## Post #5 by @Andinet_Enquobahrie (2021-06-02 10:18 UTC)

<p>Dear  <a class="mention" href="/u/tbillah">@tbillah</a></p>
<p>When you run your Slicer executable you can pass a python code to load the data during start time. something like the following</p>
<pre><code class="lang-auto">Slicer.exe --python-code "slicer.util.loadVolume('/full/path/to/img1.nii.gz')
</code></pre>
<p>or</p>
<pre><code class="lang-auto">Slicer.exe /full/path/to/img1.nii.gz
</code></pre>
<p>Also, you can do something similar from within the Slicer application using the python terminal</p>
<p>You might want to refer the Script repository for more information</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a></p>
<p>HTH<br>
Andinet</p>

---

## Post #6 by @lassoan (2021-06-02 11:10 UTC)

<p>I usually drag-and-drop data into the application window and hit Enter to open it. Do you have any suggestion how to make opening a file easier?</p>

---

## Post #7 by @tbillah (2021-06-02 15:21 UTC)

<p>Andient, this is amazing. I have been able to load multiple images from the terminal even with relative paths.</p>

---

## Post #8 by @tbillah (2021-06-02 15:22 UTC)

<p>Thanks, I forgot the drag and drop feature. Andinet’s command line suggestion is the best for me. I don’t have anymore suggestion.</p>

---
