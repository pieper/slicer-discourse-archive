---
topic_id: 9064
title: "Librarynotfounderror Slicerdmri"
date: 2019-11-07
url: https://discourse.slicer.org/t/9064
---

# [LibraryNotFoundError] [SlicerDMRI]

**Topic ID**: 9064
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/librarynotfounderror-slicerdmri/9064

---

## Post #1 by @tbillah (2019-11-07 16:25 UTC)

<p>When I try to launch <code>DWIToDTIEstimation</code> from GUI or from CLI:</p>
<blockquote>
<p>Slicer-4.10.2-linux-amd64/Slicer --launch /path/to/.config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules/DWIToDTIEstimation --help</p>
</blockquote>
<p>I run into the following error:</p>
<pre><code class="lang-auto">.config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules/DWIToDTIEstimation: error while loading shared libraries: libvtkDMRI.so: cannot open shared object file: No such file or directory
</code></pre>
<p>However, when I explicitly define <code>LD_LIBRARY_PATH</code> before, there is no error:</p>
<blockquote>
<p>LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/.config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/qt-loadable-modules Slicer-4.10.2-linux-amd64/Slicer --launch /path/to/.config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules/DWIToDTIEstimation --help</p>
</blockquote>
<p>The <code>LibraryPaths</code> section in my <code>Extensions-28257.ini</code> is following:</p>
<pre><code class="lang-auto">[LibraryPaths]
/path/to/.config/NA-MIC/Extensions-28257/UKFTractography/lib/Slicer-4.10
/path/to/.config/NA-MIC/Extensions-28257/UKFTractography/lib/Slicer-4.10/cli-modules
/path/to/.config/NA-MIC/Extensions-28257/UKFTractography/lib/Slicer-4.10/qt-loadable-modules
/path/to/.config/NA-MIC/Extensions-28257/DiffusionQC/lib/Slicer-4.10
/path/to/.config/NA-MIC/Extensions-28257/DiffusionQC/lib/Slicer-4.10/cli-modules
/path/to/.config/NA-MIC/Extensions-28257/DiffusionQC/lib/Slicer-4.10/qt-loadable-modules
/path/to/.config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10
/path/to/.config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/cli-modules
/path/to/.config/NA-MIC/Extensions-28257/SlicerDMRI/lib/Slicer-4.10/qt-loadable-modules
/path/to/.config/NA-MIC/Extensions-28257/MarkupsToModel/lib/Slicer-4.10
/path/to/.config/NA-MIC/Extensions-28257/MarkupsToModel/lib/Slicer-4.10/cli-modules
/path/to/.config/NA-MIC/Extensions-28257/MarkupsToModel/lib/Slicer-4.10/qt-loadable-modules
/path/to/.config/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10
/path/to/.config/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/cli-modules
/path/to/.config/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules
/path/to/.config/NA-MIC/Extensions-28257/DiffusionQC/lib/python2.7/site-packages
size=16

</code></pre>
<p>which evidently includes the directory of <code>libvtkDMRI.so</code> that I defined manually.</p>
<p>Anyone got a fix for this?</p>

---

## Post #2 by @tbillah (2019-11-11 20:17 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, can you look at the <code>.ini</code> file? It might be a minor issue related to how LD_LIBRARY_PATH is set up.</p>

---
