# Launch multiple instances of Slicer in Mac

**Topic ID**: 29630
**Date**: 2023-05-24
**URL**: https://discourse.slicer.org/t/launch-multiple-instances-of-slicer-in-mac/29630

---

## Post #1 by @muratmaga (2023-05-24 13:42 UTC)

<p>Is there a way to launch multiple Slicer application in Mac? I can do that in windows and linux just fine by clicking the icon, but in mac that simply changes the focus to main Slicer window. CMD, option or other key combinations doesn’t seem to have an effect either.</p>
<p>Launching from command terminal is possible, but if possible I would like to do it through the UI.</p>

---

## Post #2 by @pieper (2023-05-24 13:45 UTC)

<p>I always use the terminal to do this.  But probably you could write a small program that would launch slicer and put the icon on your desktop.</p>

---

## Post #3 by @hherhold (2023-05-24 13:46 UTC)

<p>I’ve wondered about this too, and always wound up running multiple instanced from the command line. I wonder if you could use Automator to do this as a clickable icon (like <a class="mention" href="/u/pieper">@pieper</a> suggested).</p>

---

## Post #4 by @muratmaga (2023-05-24 13:47 UTC)

<p>I’m fine with the terminal window, it was an inquiry mostly for other people.</p>

---

## Post #5 by @hherhold (2023-05-24 13:51 UTC)

<p>I just wrote a quick shell script (<code>runSlicerScript</code>) containing:</p>
<pre><code class="lang-auto">#!/bin/zsh
/Applications/Slicer.app/Contents/MacOS/Slicer
</code></pre>
<p>Run a quick <code>chmod +x runSlicerScript</code> and you can double click it from the finder to run Slicer.</p>

---
