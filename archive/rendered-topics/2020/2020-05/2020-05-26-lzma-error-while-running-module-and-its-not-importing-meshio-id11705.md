# Lzma error while running module and its not importing meshio

**Topic ID**: 11705
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/lzma-error-while-running-module-and-its-not-importing-meshio/11705

---

## Post #1 by @Saima (2020-05-26 07:46 UTC)

<p>Hi Andras,<br>
I am getting the following error. Could you please help how can I resolve it in slicer 4.11.0-2020-02-25.</p>
<p>Traceback (most recent call last):<br>
File “/home/saima/slicer/Slicer-4.11.0-2019-09-17-linux-amd64/ImageAsaModel/MeshNodesToFiducials/MeshNodesToFiducials.py”, line 210, in onVMeshButton<br>
logic.createVolumeMesh(sMesh, meshAlgo, int(cMin), int(cMax), int(optimize), int(meshQuality), int(lFactor))<br>
File “/home/saima/slicer/Slicer-4.11.0-2019-09-17-linux-amd64/ImageAsaModel/MeshNodesToFiducials/MeshNodesToFiducials.py”, line 367, in createVolumeMesh<br>
import meshio<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/<strong>init</strong>.py”, line 1, in <br>
from . import (<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/_cli/<strong>init</strong>.py”, line 1, in <br>
from ._ascii import ascii<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/_cli/_ascii.py”, line 5, in <br>
from … import ansys, flac3d, gmsh, mdpa, ply, stl, vtk, vtu, xdmf<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/vtu/<strong>init</strong>.py”, line 1, in <br>
from ._vtu import read, write<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/site-packages/meshio/vtu/_vtu.py”, line 8, in <br>
import lzma<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/lib/Python/lib/python3.6/lzma.py”, line 27, in <br>
from _lzma import *<br>
ModuleNotFoundError: No module named ‘_lzma’</p>

---

## Post #2 by @jamesobutler (2020-05-26 12:11 UTC)

<p>Lzma is typically a built in module in Python, but the Python that Slicer is using does not currently include it. You can follow <a href="https://github.com/Slicer/Slicer/issues/4920" rel="nofollow noopener">https://github.com/Slicer/Slicer/issues/4920</a> to track the progress of starting to include it. It really only becomes an issue if the specific methods in that Python package are using it. If you are importing the entire package but don’t actually need it then you can ignore it.</p>

---
