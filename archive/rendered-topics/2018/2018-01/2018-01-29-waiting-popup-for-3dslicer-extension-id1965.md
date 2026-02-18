# Waiting popup (for 3dslicer extension)

**Topic ID**: 1965
**Date**: 2018-01-29
**URL**: https://discourse.slicer.org/t/waiting-popup-for-3dslicer-extension/1965

---

## Post #1 by @Frederic (2018-01-29 11:00 UTC)

<p>Hi all,</p>
<p>I am creating 3dslicer module. It’s why I would know if you already have developed a “waiting popup”  to indicate that calculating is occurring?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @leochan2009 (2018-01-29 13:22 UTC)

<p>Hi Frederic,</p>
<p>Try use this function: slicer.util.createProgressDialog()</p>
<p>Best,<br>
Longquan</p>

---

## Post #3 by @Frederic (2018-01-29 14:10 UTC)

<p>Thanks a lot <a class="mention" href="/u/leochan2009">@leochan2009</a> !<br>
Do you have an example of how this function works please?<br>
It’s displayed after the calculating to me.</p>

---

## Post #4 by @leochan2009 (2018-01-29 14:35 UTC)

<p>Hi,<br>
progressBar=slicer.util.createProgressDialog()<br>
progressBar.labelText = 'Calculating step 1’<br>
slicer.app.processEvents()</p>
<h1>Some algorithm calculation 1</h1>
<p>progressBar.value = 25<br>
progressBar.labelText = 'Calculating step 2’<br>
slicer.app.processEvents()</p>
<h1>Some algorithm calculation 2</h1>
<p>for some cli module, you should be able to get the current progress and update the progress bar value.<br>
but for loadable modules, i am not sure the proper way to get the progress…</p>

---

## Post #5 by @Frederic (2018-01-29 15:02 UTC)

<p>Perfect,<br>
Thanks a lot!</p>

---
