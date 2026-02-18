# Python Interactor colors

**Topic ID**: 14053
**Date**: 2020-10-15
**URL**: https://discourse.slicer.org/t/python-interactor-colors/14053

---

## Post #1 by @Niels (2020-10-15 11:51 UTC)

<p>Hello,</p>
<p>I just installed the latest stable version on my MacBook and I noticed that the colors in the interaction are different. The Error messages are printed in white so they are not visible.</p>
<p>MAC<br>
version 4.11.20200930<br>
revision 29402<br>
built 2020-10-02</p>

---

## Post #2 by @hherhold (2020-10-15 11:53 UTC)

<p>I just noticed the exact same thing and was about to post. You can see them in dark mode, so that might be a workaround if you don’t mind dark mode.</p>

---

## Post #3 by @lassoan (2020-10-15 13:16 UTC)

<p>There was a <a href="https://github.com/Slicer/Slicer/commit/ab51796fd3bf42a9f38fd82a40e0ac2ca4781e27">commit that fixed Python console colors</a> after the 20200930 release. Could you please try if colors look good in the latest preview release?</p>

---

## Post #4 by @hherhold (2020-10-15 13:21 UTC)

<p>I have a recent build (couple of days old?) and the colors look fine in that, so presumably the latest preview is okay too.</p>
<p>Thanks!</p>

---

## Post #5 by @lassoan (2020-10-15 13:24 UTC)

<p>Thanks for testing. Currently, we don’t plan to have a patch release for Slicer-4.11 but we’ll see what else comes up and how long does it take to make Slicer-4.13 functional (and release Slicer-5.0).</p>

---

## Post #6 by @hherhold (2020-10-15 13:49 UTC)

<p>As a quick workaround, if you don’t want to switch to dark mode for everything, you could use:</p>
<pre><code>slicer.util.mainWindow().pythonConsole().backgroundColor = qt.QColor(0,0,0)
</code></pre>
<p>to just switch the python console to black.</p>

---
