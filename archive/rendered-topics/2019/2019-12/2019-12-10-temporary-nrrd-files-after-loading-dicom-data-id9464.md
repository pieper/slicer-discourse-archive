---
topic_id: 9464
title: "Temporary Nrrd Files After Loading Dicom Data"
date: 2019-12-10
url: https://discourse.slicer.org/t/9464
---

# Temporary .nrrd files after loading DICOM data

**Topic ID**: 9464
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/temporary-nrrd-files-after-loading-dicom-data/9464

---

## Post #1 by @giovform (2019-12-10 16:20 UTC)

<p>Hello there! I am using the DICOMScalarVolumePlugin to programmatically load a series of dicom data inside a user specified directory. It works well, but I noticed that sometimes it leaves large .nrrd files inside the Slicer temporary directory (JHCI_vtkMRMLScalarVolumeNodeBD.nrrd for example). What could I do to avoid this behavior? Is there a better DICOM loader alternative/example script?</p>

---

## Post #2 by @pieper (2019-12-10 20:04 UTC)

<p>Hi -</p>
<p>Hmm, the scalar volume plugin shouldn’t be creating nrrd files - are you sure it’s not one of the other dicom plugin classes?  The filename indicates it’s the result of running a Command Line Interface (CLI) module.  For example the diffusion plugin does that to estimate tesors.  If you have an example to reproduce the behavior that would be helpful.</p>

---

## Post #3 by @lassoan (2019-12-10 20:11 UTC)

<p>When “Developer mode” is enabled in application settings, CLI module input and output files are not removed (to make debugging easier). You can clean up your temp folder time to time, disable “developer mode”, or disable “prefer executable CLIs” (in application settings / Modules; this make images transfer within memory instead of via files).</p>

---

## Post #4 by @giovform (2019-12-11 13:21 UTC)

<p>Oh, nice, I made a test here and indeed disabling the developer mode does not keep those .nrrd files. Thanks.</p>

---

## Post #5 by @giovform (2019-12-11 13:21 UTC)

<p>Hello, I am using a code I found in another module, here is the snippet:</p>
<pre><code>    plugin = slicer.modules.dicomPlugins['DICOMScalarVolumePlugin']()
    loadables = plugin.examine([files])</code></pre>

---
