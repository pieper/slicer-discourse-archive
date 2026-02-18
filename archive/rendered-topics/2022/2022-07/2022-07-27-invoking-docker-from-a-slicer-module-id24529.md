# Invoking docker from a slicer module

**Topic ID**: 24529
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/invoking-docker-from-a-slicer-module/24529

---

## Post #1 by @Lee_Newberg (2022-07-27 17:26 UTC)

<p>I am modifying <a href="https://github.com/KitwareMedical/lungair-desktop-application" rel="noopener nofollow ugc">LungAIR</a>, a customization of 3D Slicer, and I am going to have the new module call off to a docker image (on the same computer) to perform a calculation.  It would be great if there is a 3D Slicer module out there that already does something similar that I could emulate; anyone know of any?</p>
<p>I suspect that the MONAI Label back end for 3D Slicer could be used, but I don’t think I need all that … or is that the best practice even in a fairly simple case?</p>

---

## Post #2 by @jcfr (2022-07-27 17:55 UTC)

<p>Generally speaking, using the functions <code>slicer.util.launchConsoleProcess</code> and <code>slicer.util.logProcessOutput</code> would allow you to run processes like <code>docker</code> and capture its output.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.util</a></p>
<p>For example:</p>
<pre><code class="lang-python">import shutil
dockerExecutablePath = shutil.which('docker')
commandLine = [dockerExecutablePath, "run", "--rm", "hello-world:latest"]
proc = slicer.util.launchConsoleProcess(commandLine)
slicer.util.logProcessOutput(proc)
</code></pre>

---

## Post #3 by @jcfr (2022-07-27 17:58 UTC)

<p>Depending on how involved the handling of docker containers would be, you may also want to consider looking at <a href="https://docker-py.readthedocs.io/en/stable/">docker-py</a></p>

---

## Post #4 by @Lee_Newberg (2022-08-04 14:32 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a>, this is useful for launching the docker executable.</p>
<p>On a closely related matter, what is the best practice for making a new docker image available via the above <code>slicer.util.launchConsoleProcess(commandLine)</code>?</p>
<ol>
<li>Insert <code>CMakeLists.txt</code> commands so that the docker image is built locally for each user at build time?</li>
<li>Build the docker image myself and upload it to some public repository, so that the above suggested code will automagically find and download the image if it isn’t already available.  If so, which public repository?</li>
<li>Something else?</li>
</ol>
<p>Especially useful would be 3D Slicer code / module that already does the best practice, as a template.</p>

---
