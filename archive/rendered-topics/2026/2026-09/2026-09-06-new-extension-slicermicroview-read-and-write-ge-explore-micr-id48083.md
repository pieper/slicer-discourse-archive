---
topic_id: 48083
title: "New extension: SlicerMicroView – read and write GE eXplore / MicroView VFF micro-CT volumes"
date: 2026-09-06
url: https://discourse.slicer.org/t/48083
last_bumped: 2026-09-06T23:02:52.868Z
---

# New extension: SlicerMicroView – read and write GE eXplore / MicroView VFF micro-CT volumes

**Topic ID**: 48083
**Date**: 2026-09-06
**URL**: https://discourse.slicer.org/t/new-extension-slicermicroview-read-and-write-ge-explore-microview-vff-micro-ct-volumes/48083

---

## Post #1 by @falkwiegmann (2026-09-06 23:02 UTC)

<p>Hi all,</p>
<p>I have submitted a small extension to the ExtensionsIndex and would appreciate a review when someone has a moment: <a href="https://github.com/Slicer/ExtensionsIndex/pull/2390" class="inline-onebox" rel="noopener nofollow ugc">Add SlicerMicroView extension by falkwiegmann · Pull Request #2390 · Slicer/ExtensionsIndex · GitHub</a></p>
<p>What it does</p>
<p>SlicerMicroView adds a reader and writer for VFF files, the native volume format of GE eXplore micro-CT scanners and of the MicroView software. VFF files then open directly through Add Data, and volumes can be exported back to VFF for MicroView.</p>
<p>The existing VFF reader in SlicerRT is written for radiotherapy dose files and does not handle scanner output: it requires header fields GE does not write, reads all voxels as float, and ignores the elementsize field that carries the real voxel size. The new reader follows MicroView’s own conventions, which I checked against the MicroView source: voxel size = spacing × elementsize, origin in voxel units, big-endian 16-bit data, values loaded as stored. Scanner calibration fields (water, air, boneHU) are kept as node attributes and written back on export.</p>
<p>Repository: <a href="https://github.com/UBC-Ford-lab/SlicerMicroView" class="inline-onebox" rel="noopener nofollow ugc">GitHub - UBC-Ford-lab/SlicerMicroView: 3D Slicer extension to read and write GE eXplore / MicroView micro-CT volumes (VFF format). · GitHub</a> (MIT)</p>
<p>screenshot (<a href="https://raw.githubusercontent.com/UBC-Ford-lab/SlicerMicroView/main/Screenshots/1.png" rel="noopener nofollow ugc">https://raw.githubusercontent.com/UBC-Ford-lab/SlicerMicroView/main/Screenshots/1.png</a>)</p>
<p>Testing</p>
<ul>
<li>Python-only scripted module, no build dependencies.</li>
<li>Self-test with synthetic files covers the GE header, minimal headers, endianness, writer round trips and the loading options.</li>
<li>Tested on macOS with Slicer 5.12.3 on 1.4 GB and 2.1 GB GE eXplore CT 120 reconstructions and on scanner-side output; read-write-read round trips are byte-identical.</li>
</ul>
<p>Happy to make any changes the reviewers would like.</p>
<p>Falk Wiegmann<br>
Ford Lab, University of British Columbia</p>

---
