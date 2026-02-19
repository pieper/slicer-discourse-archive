---
topic_id: 23358
title: "Slicer And Jupyterhub"
date: 2022-05-10
url: https://discourse.slicer.org/t/23358
---

# Slicer and JupyterHub

**Topic ID**: 23358
**Date**: 2022-05-10
**URL**: https://discourse.slicer.org/t/slicer-and-jupyterhub/23358

---

## Post #1 by @SaraPoli22 (2022-05-10 08:56 UTC)

<p>Hi, for my thesis I would need to use Slicer on a server created with JupyterHub, could you tell me how to add the Slicer kernel to allow the use of Slicer without installation?<br>
Thanks for your help.</p>

---

## Post #2 by @lassoan (2022-05-11 16:31 UTC)

<p>You can find the kernelspec install instructions in the Jupyter Kernel module in Slicer.</p>

---

## Post #3 by @SaraPoli22 (2022-05-12 06:40 UTC)

<p>Thanks for the reply.<br>
I still have a question, Slicer must be installed on the pc where the server resides, correct?</p>

---

## Post #4 by @lassoan (2022-05-12 12:25 UTC)

<p>Yes, the Jupyter kernels are installed on the same computer as the Jupyter server.</p>
<p>However, the Jupyter protocol just uses a few sockets to communicate with the kernel, so if you want to run kernels on different computers then it is quite easy to work around this. For example, you can specify a small executable in the kernelspec that just launches the real Jupyter kernel on a remote computer and sets up port forwarding.</p>

---
