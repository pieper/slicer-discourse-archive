# Changing all paths in Slicer

**Topic ID**: 19916
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/changing-all-paths-in-slicer/19916

---

## Post #1 by @muratmaga (2021-09-29 17:47 UTC)

<p>We are using Slicer in a docker environment. There is a persistent storage mounted under /home/docker/mydata so that individual settings/files are saved there and when the container is stop that they are retained.</p>
<p>I have been manually configuring default paths (like download, cache, default location), in Slicer.ini that we build the docker image with. But it turns out I am missing other things (like DICOM cache folder), and probably there are other path settings that I am not aware of .</p>
<p>So, what would be the most robust way that all default path variables are prefixed by /home/docker/mydata/Slicer or something along those lines?</p>

---

## Post #2 by @lassoan (2021-09-29 18:17 UTC)

<p>All settings are saved in Slicer.ini and Slicer-NNN.ini, so it is enough set the content of those two files correctly. Modules do not (should not) invent their own root paths but should derive their <a href="https://github.com/Slicer/Slicer/blob/047571414481cada211db12f13eb7c5148a1c3fd/Base/QTCore/qSlicerCoreApplication.h#L72-L82">paths from those provided by the application</a>.</p>
<p>In Slicer core, the only module that use a custom root path is the DICOM module, as it places the DICOM database in <a href="https://doc.qt.io/qt-5/qstandardpaths.html">QStandardPaths::DocumentsLocation</a>. It should point to a good location by default, but if this is not the case in your special configuration, then all you need to set (in addition to the qSlicerCoreApplication-managed paths) in your Slicer.ini is the DICOM database.</p>

---
