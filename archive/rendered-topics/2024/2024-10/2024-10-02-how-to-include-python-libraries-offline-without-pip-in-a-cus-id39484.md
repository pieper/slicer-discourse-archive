---
topic_id: 39484
title: "How To Include Python Libraries Offline Without Pip In A Cus"
date: 2024-10-02
url: https://discourse.slicer.org/t/39484
---

# How to Include Python Libraries Offline (without pip) in a Custom Slicer Application?

**Topic ID**: 39484
**Date**: 2024-10-02
**URL**: https://discourse.slicer.org/t/how-to-include-python-libraries-offline-without-pip-in-a-custom-slicer-application/39484

---

## Post #1 by @park (2024-10-02 04:02 UTC)

<p>Hi all,</p>
<p>I’m currently developing a custom application using Slicer. At the moment, I’m installing the necessary Python libraries via <code>pip</code> (using <code>slicer.util.pip_install('library')</code>).</p>
<p>However, I’m looking for a way to include these Python libraries in the custom application package for offline use. Does anyone have suggestions or methods to package these libraries for offline integration?</p>
<p>Any advice would be greatly appreciated!</p>

---

## Post #2 by @lassoan (2024-10-02 12:40 UTC)

<p>You can bundle Python packages in your extension package (as it is done for example in <a href="https://github.com/Slicer/SlicerJupyter/blob/master/SuperBuild/External_python-packages.cmake">SlicerJupyter extension</a>) or in your custom Slicer application (<a href="https://github.com/Slicer/Slicer/blob/9c0754c6741e8127c38691895d452d389ee3cd03/SuperBuild/External_python-dicom-requirements.cmake">as it is done in Slicer core</a>).</p>

---
