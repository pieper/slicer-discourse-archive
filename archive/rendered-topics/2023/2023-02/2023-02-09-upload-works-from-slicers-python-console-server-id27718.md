# Upload works from slicer's python console (server)

**Topic ID**: 27718
**Date**: 2023-02-09
**URL**: https://discourse.slicer.org/t/upload-works-from-slicers-python-console-server/27718

---

## Post #1 by @dsa934 (2023-02-09 09:33 UTC)

<p>Operating system: window 11<br>
Slicer version: 5.2.1</p>
<p>I am using a private sftp server to store data.<br>
The data I handle is sensitive to security, so I can’t experiment easily, so I’m asking a question because I want to get a proper answer while searching for data.</p>
<p>Q1. Is it possible to run a command through the 3d slicer’s Python console to transfer the working file to my personal SFTP server?</p>
<p>Q2. What are the limitations or problems when trying to communicate with private sftp through 3d slicer’s python console?</p>
<p>edit :</p>
<p>Am I thinking too hard right now?</p>
<p>Is it possible to create an ftp module using private server and run it in 3d slicer?</p>

---

## Post #2 by @pieper (2023-02-09 13:16 UTC)

<p>It should be no problem to write to a private temporary directory and the invoke sftp commands from Slicer’s python using ssh keys in a secured directory, just like you would from the command line.</p>
<p>If your files are big you might prefer to implement a streaming solution, but this would be more complex.</p>

---
