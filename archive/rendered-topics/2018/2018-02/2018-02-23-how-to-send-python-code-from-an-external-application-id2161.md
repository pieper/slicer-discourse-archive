---
topic_id: 2161
title: "How To Send Python Code From An External Application"
date: 2018-02-23
url: https://discourse.slicer.org/t/2161
---

# How to send python code from an external application?

**Topic ID**: 2161
**Date**: 2018-02-23
**URL**: https://discourse.slicer.org/t/how-to-send-python-code-from-an-external-application/2161

---

## Post #1 by @Ahmed_Soufane (2018-02-23 20:20 UTC)

<p>Hi,<br>
I was wondering how to send python code from an external application ?</p>

---

## Post #2 by @pieper (2018-02-23 21:36 UTC)

<p>There’s not a standard way to send arbitrary python commands to slicer (and it might be considered unsafe in general).  You could set up a socket to listen for strings and then execute them as python code.  I have done experiments with embedding a web server in slicer and it can work.</p>

---

## Post #3 by @jcfr (2018-02-23 22:14 UTC)

<p>We have been experimenting with using “Slicer” (or more generally application that are qt+pythonqt+ctk based as a jupyter/ipython kernel).</p>
<p>See <a href="https://github.com/commontk/QEmbedIPython">https://github.com/commontk/QEmbedIPython</a>  and <a href="http://jupyter.org/">http://jupyter.org/</a></p>
<p>That said, there is nothing like this readily available in 3D Slicer.</p>
<p>Here what I envision:</p>
<ul>
<li>install a jupyter extension (e.g <code>pip install slicer-jupyter-bridge</code>)  in the jupyter interface.</li>
<li>install an extension in 3D Slicer using the extension manager</li>
<li>and optionally you could even install something like <a href="https://github.com/InsightSoftwareConsortium/itk-jupyter-widgets">itk-jupyter-widgets</a> to visualize images directly in jupyter</li>
</ul>
<p>Let us know if you have any questions</p>
<p>Cc: <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #4 by @lassoan (2018-02-25 23:19 UTC)

<p>It would be awesome to have all these. Can QEmbedIPython be already used with Slicer or there are still some unresolved issues?</p>

---
