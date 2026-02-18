# Extension manager icons look faded

**Topic ID**: 14077
**Date**: 2020-10-16
**URL**: https://discourse.slicer.org/t/extension-manager-icons-look-faded/14077

---

## Post #1 by @Gaston (2020-10-16 12:36 UTC)

<p>When I open the extension manager the icons look washed out</p>
<p>Mac osx catalina</p>

---

## Post #2 by @lassoan (2020-10-16 14:32 UTC)

<p>Thank you for reporting this. So far we have only heard about one user having the same issue (see <a href="https://github.com/Slicer/Slicer/issues/5118">here</a>) and many others had no problems with this.</p>
<p>Can you check if you can reproduce it without the extensions manager window by copy-pasting this into the Python console?</p>
<pre><code class="lang-python">webWidget = slicer.qSlicerWebWidget()
webWidget.url = "https://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=29431&amp;layout=layout"
webWidget.show()
</code></pre>
<p>Can you check if the new extension manager frontend is rendered correctly?</p>
<pre><code class="lang-python">webWidget.url = "https://extensions-slicer-org.netlify.app/catalog/All/29431/win"; webWidget.raise_()
</code></pre>
<p>Do other websites look good? (execute these lines one by one)</p>
<pre><code class="lang-python">webWidget.url = "https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4b515ae1d8c75dfc70b53a"; webWidget.raise_()

webWidget.url = "https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager"; webWidget.raise_()

webWidget.url = "https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/"; webWidget.raise_()

webWidget.url = "https://github.com/girder/slicer_package_manager#readme"; webWidget.raise_()

webWidget.url = "https://www.google.com/"; webWidget.raise_()
</code></pre>
<p>Are these pages rendered correctly in Google Chrome (outside Slicer)?</p>
<p>What hardware do you use? Have you configured any custom theme, color management, etc.?</p>
<p>What processor and graphics your computer has?</p>

---

## Post #3 by @Gaston (2020-11-02 22:15 UTC)

<p>Hello Andras, I have done everything you have suggested and the letters and icons are washed out.<br>
I have not configured any custom theme.<br>
This is my configuration.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eabbca35b6b7f1f9f039599b21ec677b8d3deb9.png" alt="image" data-base62-sha1="4nkgEI6UiIsyiaZjiHVFxK8kcnn" width="288" height="188"></p>

---

## Post #4 by @fedorov (2020-11-03 14:16 UTC)

<p><a class="mention" href="/u/gaston">@Gaston</a> do you see something similar to what was reported in this comment: <a href="https://github.com/Radiomics/SlicerRadiomics/issues/62#issuecomment-719427367">https://github.com/Radiomics/SlicerRadiomics/issues/62#issuecomment-719427367</a>  ?</p>

---

## Post #5 by @lassoan (2020-11-03 14:25 UTC)

<p><a class="mention" href="/u/gaston">@gaston</a> it would help a lot if you could answer all the questions above (Can you check if you can reproduce it without the extensions manager window by copy-pasting this into the Python console? Can you check if the new extension manager frontend is rendered correctly? Do other websites look good? Are these pages rendered correctly in Google Chrome (outside Slicer)?)</p>

---

## Post #6 by @Gaston (2020-11-03 14:41 UTC)

<p>Hello Andras, I have done what you have suggested.<br>
When I run the python commands, the extension manager looks washed out. When I run the links in chrome the page looks perfectly fine.</p>

---

## Post #7 by @lassoan (2020-11-03 14:44 UTC)

<p>Does the new extension manager appear washed-out, too?<br>
Do all other websites appear washed out when you open them in the web widget in Slicer?</p>

---

## Post #8 by @Gaston (2020-11-03 15:21 UTC)

<p>New extension manager an old extension manager</p>
<blockquote>
<p>Do all other websites appear washed out when you open them in the web widget in Slicer?</p>
</blockquote>
<p>yes all</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31c456c5801dcd901dc9bd4c82d0349a31176c3.png" alt="Attachment-1.png" data-base62-sha1="ngWoHvOmkyJLfPc8JAFih2aMWA3" width="320" height="245"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21b0e820202b023bd061c50e95bd64584d07d16b.png" alt="Attachment-2.png" data-base62-sha1="4O2McAjuStga6EA9XqWYDs54OOn" width="320" height="245"></p>

---

## Post #9 by @Gaston (2020-11-09 23:16 UTC)

<p>Hi Andras<br>
I have tried to change the system to dark mode and now the icons are ok</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/230dc70c6246eac75d5517d0204455ead4a2e1b3.png" alt="Attachment.png" data-base62-sha1="506eeWn7Qv3VXHtj8HfBfX0ZoT9" width="320" height="261"></p>

---

## Post #10 by @lassoan (2020-11-10 04:02 UTC)

<p>Thanks for the update, this is an interesting piece of information that may prove to be helpful in figuring out what’s happening.</p>

---
