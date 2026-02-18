# Can't open a local file on web UI?

**Topic ID**: 44255
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/cant-open-a-local-file-on-web-ui/44255

---

## Post #1 by @Rod_Whiteley (2025-08-29 14:38 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.03<br>
Expected behavior: Upload a nrrd file to analyse<br>
Actual behavior: can’t access local files (Downloads folder) from</p>

---

## Post #2 by @lassoan (2025-08-29 14:38 UTC)

<p>Do you run Slicer in a docker container?</p>

---

## Post #3 by @Rod_Whiteley (2025-08-29 16:03 UTC)

<p>On this machine I was trying to run it in a Jupytper window as the local installation said I couldn’t run OpenGL (despite Open GL 1.1.0; Radeon RX560X; Intel UHD Graphics 63C are the display adapters, 12-core Intel i7CPU).</p>
<p>I have installed on a different machine where it’s running locally, and it works a treat. Perhaps the web/Jupyter version doesn’t allow opening local files?</p>

---

## Post #4 by @lassoan (2025-08-29 17:26 UTC)

<p>Applications that are running inside a container are isolated from the host, you can only access those folders that you choose to expose in the container. If you are running Slicer on a remote host then you need to upload/download your files. You can use the Jupyter GUI to transfer files between your local computer and the remote Jupyter server.</p>

---
