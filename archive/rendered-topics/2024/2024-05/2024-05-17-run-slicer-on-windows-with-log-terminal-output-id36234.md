---
topic_id: 36234
title: "Run Slicer On Windows With Log Terminal Output"
date: 2024-05-17
url: https://discourse.slicer.org/t/36234
---

# Run slicer on windows with log / terminal output?

**Topic ID**: 36234
**Date**: 2024-05-17
**URL**: https://discourse.slicer.org/t/run-slicer-on-windows-with-log-terminal-output/36234

---

## Post #1 by @dangerweenie (2024-05-17 17:18 UTC)

<p>Hi there!</p>
<p>New to slicer here, excited to dig in.</p>
<p>I’m trying to run the HDBrainExtraction module and it seems to hang (30 minutes or more) when initialzing / installing pytorch.</p>
<p>Not sure if slicer uses a .venv, i have lots of Torch installs from AI apps, though I am keen to have it use its own install of course.</p>
<p>Regardless, I’d like to see what is going on when it hangs - is there any way to launch slicer.exe with some kind of terminal output so I can see what is going on?  There doesn’t seem to be a terminal window in slicer.  I just want to see the install / build progress so I can troubleshoot.</p>
<p>I’m not an expert by any measure, so I tried:</p>
<pre><code class="lang-auto">slicer.exe -l
slicer.exe | cat
</code></pre>
<p>but no dice.</p>
<p>Any advice on how to expose what is going on?</p>

---
