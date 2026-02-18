# How does 3dslicer read external marker coordinates

**Topic ID**: 17192
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/how-does-3dslicer-read-external-marker-coordinates/17192

---

## Post #1 by @wujie (2021-04-20 03:30 UTC)

<p>How does 3dslicer read external marker coordinates</p>

---

## Post #2 by @ungi (2021-04-20 22:33 UTC)

<p>Slicer communicates with position trackers through the OpenIGTLink communication protocol. You need to install the SlicerOpenIGTLink extension for that. I also recommend installing SlicerIGT extension, if you use real time trackers. There are some useful tutorials on this page: <a href="http://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a><br>
Some of them are a bit outdated, but still useful.<br>
PLUS is a great tool to read any tracker and translate the real time information to OpenIGTLink and send in real time to Slicer: <a href="https://plustoolkit.github.io/" rel="noopener nofollow ugc">https://plustoolkit.github.io/</a></p>

---

## Post #3 by @wujie (2021-04-21 07:45 UTC)

<p>Thanks your reply, I have installed the OpenIGTLink and communication protocol and PLUS,could you please tell me the examples of read external marker coordinates?</p>

---

## Post #4 by @ungi (2021-04-21 14:22 UTC)

<p>You need to specify which tracker device you are using. Here is a list of devices already supported by PLUS: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Device set configuration</a><br>
Can you find your device in the list?</p>

---
