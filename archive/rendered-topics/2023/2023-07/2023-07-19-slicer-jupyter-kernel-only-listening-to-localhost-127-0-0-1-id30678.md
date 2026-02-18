# Slicer Jupyter Kernel only listening to localhost(127.0.0.1)

**Topic ID**: 30678
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/slicer-jupyter-kernel-only-listening-to-localhost-127-0-0-1/30678

---

## Post #1 by @Reshma (2023-07-19 15:51 UTC)

<p>I am using fedora linux and I have a 3D Slicer v5.2.2 installed. I am using the JupyterKernel extension and everything works fine locally. When I try to access the same outside from WAN, I am not able to access the jupyter notebook. I have made necessary settings in my router(port forwarding). I figured out that when I press the “Start Jupyter Server” button, it starts the server for localhost(127.0.0.1) usage only. I want to change the visibility from “127.0.0.1” to “0.0.0.0” so that it can listen to any IP. How can I start the server in a way that it listens to custom specified IP and port numbers. Can anyone give me some directions? I plan to use Slicer for remote visualization.</p>

---

## Post #2 by @lassoan (2023-07-21 04:38 UTC)

<p>You can configure jupyter notebook settings as usual: <a href="https://jupyter-notebook.readthedocs.io/en/stable/configuring/config_overview.html">generate a config file</a> and then edit the server address (and many other authentication options). Probably there is just one thing that is not trivial - if you want to run the Jupyter server in Slicer’s Python environment then (instead of <code>jupyter notebook --generate-config</code>), you can run:</p>
<pre><code>PythonSlicer -m jupyter notebook --generate-config
</code></pre>

---

## Post #3 by @Reshma (2023-07-24 09:13 UTC)

<p>Thank you Andras! It works! Do you know if I can install SlicerJupyter in a headless server (no GUI) and still have the same remote slicer notebook work?</p>

---

## Post #4 by @lassoan (2023-07-24 11:11 UTC)

<p>Yes you can run <a href="https://xpra.org/trac/wiki/Xdummy">xdummy</a> or similar software to allow running Slicer on a headless node.</p>

---
