# PSA for Linux users: work-around for Linux-nightly extension manager error

**Topic ID**: 2755
**Date**: 2018-05-03
**URL**: https://discourse.slicer.org/t/psa-for-linux-users-work-around-for-linux-nightly-extension-manager-error/2755

---

## Post #1 by @ihnorton (2018-05-03 17:47 UTC)

<p>Here is a temporary work-around for the following bug, which prevents using the extension manager in nightly builds on Linux:</p>
<p><a href="https://issues.slicer.org/view.php?id=4544" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=4544</a></p>
<p>in the expanded Slicer directory, copy the contents of resources/ to libexec. Then restart Slicer.</p>
<pre><code class="lang-auto">root@kali:~/Downloads/Slicer-4.9.0-2018-05-02-linux-amd64# cp resources/* libexec/
root@kali:~/Downloads/Slicer-4.9.0-2018-05-02-linux-amd64# ./Slicer
</code></pre>

---

## Post #2 by @Sam_Horvath (2018-06-13 23:14 UTC)

<p>This should be permanently addressed (updating linux builds to 5.11) in the next nightly build (fingers crossed).</p>

---
