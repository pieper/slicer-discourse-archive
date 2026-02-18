# OpenCV extension build fails since June ITK upgrade

**Topic ID**: 38158
**Date**: 2024-09-02
**URL**: https://discourse.slicer.org/t/opencv-extension-build-fails-since-june-itk-upgrade/38158

---

## Post #1 by @cpinter (2024-09-02 14:33 UTC)

<p>Hi all,</p>
<p>The OpenCV extension build fails on all three platform since June 4, most probably due to the ITK upgrade: <a href="https://github.com/Slicer/Slicer/commit/acf3dd47940665869765584564b38439f73ff1d5" class="inline-onebox">ENH: Update ITK to 5.4.0 · Slicer/Slicer@acf3dd4 · GitHub</a></p>
<p>This is the first failure on the dashboard:<br>
<a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2024-06-04&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=opencv" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2024-06-04&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=opencv</a></p>
<p>The relevant error seems to be:</p>
<pre><code class="lang-auto">"ITK_FIND_REQUIRED_ITKVideoBridgeOpenCV" "OR" "M" "IN_LIST" "ITK_MODULES_ENABLED"

  Unknown arguments specified
Call Stack (most recent call first):
  SlicerOpenCV/Logic/CMakeLists.txt:6 (find_package)
</code></pre>
<p>Does anyone know off the bat what this unknown argument is and how to fix it? Thanks a lot!</p>

---

## Post #2 by @cpinter (2024-09-06 09:11 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/adamrankin">@adamrankin</a> Have you seen this? The extension is down for three months. If it is not needed anymore, that would also be useful to know. Thanks!</p>

---

## Post #3 by @adamrankin (2024-09-06 11:05 UTC)

<p>Yes, probably time to kill it. If someone needs it, it can be brought back</p>

---

## Post #4 by @cpinter (2024-09-06 11:07 UTC)

<p>I need it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Or importing OpenCV is now trivial via pip?</p>

---

## Post #5 by @adamrankin (2024-09-06 11:46 UTC)

<p>Yes, extension only has value for downstream c++ extensions</p>
<p>Python is solved by pip</p>

---

## Post #6 by @cpinter (2024-09-06 11:59 UTC)

<p>Thanks Adam, you just saved me some time. I assumed the extension it was still needed for some reason.</p>

---
