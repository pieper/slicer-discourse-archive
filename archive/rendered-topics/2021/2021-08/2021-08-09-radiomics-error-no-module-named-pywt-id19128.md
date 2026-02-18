# Radiomics error - No module named ‘pywt’

**Topic ID**: 19128
**Date**: 2021-08-09
**URL**: https://discourse.slicer.org/t/radiomics-error-no-module-named-pywt/19128

---

## Post #1 by @hotsen (2021-08-09 20:08 UTC)

<p>Another question: I am trying to from radiomics import getFeatureClasses, but got the error " No module named ‘pywt’ ". I fixed the problem using the code mentioned here <a href="https://discourse.slicer.org/t/slicer-radiomics-error/14279/3" class="inline-onebox">Slicer Radiomics error  - #3 by fedorov</a> , and <a class="mention" href="/u/fedorov">@fedorov</a> said he has updated this. But both the stable version and preview release of Slicer have this error. Thank you.</p>
<p>Hotsen</p>

---

## Post #2 by @fedorov (2021-08-11 18:11 UTC)

<p>I tried, and I am unable to even install the extension - I do not know what happened and why it says it is incompatible with the nightly slicer. I posted that question separately <a href="https://discourse.slicer.org/t/unable-to-install-extension-incompatible-with-slicer-r30110/19158">here</a>.</p>

---

## Post #3 by @lassoan (2021-08-12 03:52 UTC)

<p>Switch to the new-generation extension server happened just today. You can use a release from a couple of days back on the download page by specifying an offset, for example: <a href="https://download.slicer.org/?offset=-3">https://download.slicer.org/?offset=-3</a> allows you to download the Slicer Preview Release from 3 days ago.</p>

---

## Post #4 by @fedorov (2021-08-12 15:11 UTC)

<p><a class="mention" href="/u/hotsen">@hotsen</a> the pyradiomics self-test works fine for me on mac for the preview release from 3 days ago. What platform are you on?</p>

---

## Post #5 by @hotsen (2021-08-12 15:21 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> I am using stable version 4.11.20210226 and preview release 4.13.0-2021-08-08<br>
Enter “from radiomics import getFeatureClasses” in python interactor, will give you “No module named ‘pywt’ error”</p>

---

## Post #6 by @hotsen (2021-08-12 15:22 UTC)

<p>I am using Windows platform</p>

---

## Post #7 by @fedorov (2021-08-12 15:22 UTC)

<p>Thanks, this works fine for me on mac, and I have not tested on windows. I actually don’t have a windows machine, but will try to figure something out.</p>

---

## Post #8 by @fedorov (2021-08-12 15:43 UTC)

<p><a class="mention" href="/u/hotsen">@hotsen</a> I have Windows 10 running on Mac in Parallels, and for me the self-test completes fine, and <code>from radiomics import getFeatureClasses</code> in the python console does not trigger any errors for the preview release 2021-08-08.</p>

---

## Post #9 by @hotsen (2021-08-12 19:11 UTC)

<p>That’s odd. I just downloaded the new preview release 2021-08-12, no errors anymore. Thank you for testing!</p>

---
