# Cannot find SlicerIGT in extensions library

**Topic ID**: 2112
**Date**: 2018-02-19
**URL**: https://discourse.slicer.org/t/cannot-find-slicerigt-in-extensions-library/2112

---

## Post #1 by @Prashant_Pandey (2018-02-19 01:44 UTC)

<p>I’m using Slicer 4.9.0 2018-01-24, and wanted to install the SlicerIGT module, but I can’t find it in the extensions manager. I remember that it was available for older versions of Slicer.</p>

---

## Post #2 by @lassoan (2018-02-19 02:05 UTC)

<p>Use 4.8.1 or the latest nightly version.</p>

---

## Post #3 by @Prashant_Pandey (2018-02-19 19:47 UTC)

<p>Thanks, using 4.8.1 worked.</p>
<p>As an aside I also found that MatlabBridge does not work with the nightly version, it gives the error that cli-modules/MatlabCommander.exe does not exist.</p>

---

## Post #4 by @lassoan (2018-02-19 23:08 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="3" data-topic="2112">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>it gives the error that cli-modules/MatlabCommander.exe does not exist.</p>
</blockquote>
</aside>
<p>Could you please copy-paste here the application log? (menu: Help / Report a bug)</p>

---

## Post #5 by @Prashant_Pandey (2018-02-21 16:45 UTC)

<p>Unfortunately I uninstalled nightly Slicer so I cannot go back and look at the error logs, but essentially the problem was that the MatlabBridge/cli-modules sub-folder did not exist.</p>

---

## Post #6 by @lassoan (2018-02-21 16:56 UTC)

<p>I was able to reproduce the problem and I expect to fix it today.</p>

---

## Post #7 by @lassoan (2018-02-21 17:15 UTC)

<p>I’ve fixed the issue (the extension needs OpenIGTLink and this library was moved out from the Slicer core to the SlicerOpenIGTLink extension). Everything should work correctly again in nightly builds that you download tomorrow or later.</p>

---
