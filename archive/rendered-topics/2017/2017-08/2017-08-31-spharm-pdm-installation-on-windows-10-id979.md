---
topic_id: 979
title: "Spharm Pdm Installation On Windows 10"
date: 2017-08-31
url: https://discourse.slicer.org/t/979
---

# SPHARM-PDM installation on Windows 10

**Topic ID**: 979
**Date**: 2017-08-31
**URL**: https://discourse.slicer.org/t/spharm-pdm-installation-on-windows-10/979

---

## Post #1 by @laurapascal (2017-08-31 15:45 UTC)

<p>Catharina De Rosa wrote on Wed, August 30, 2017:</p>
<hr>
<p><em>I download extension to use Spharm-pdm on 3D Slicer for Windows 10.</em><br>
<em>As I tried to use the tools, it also pop up mensages that the program has stopped working.</em><br>
<em>Messages were “GenParaMeshCLP.exe stopped working” and “ShapeAnalysisModule.exe stopped working”.</em><br>
<em>I had download an tutorial but could understand it much.</em><br>
<em>I have DICOM images to work with.</em></p>
<hr>
<p>Hello Catharina,</p>
<p>I tried to reproduce your error by downloading SPHARM-PDM as an extension on 3D Slicer for Windows 10. But it seems to work on my machine.<br>
Those are the steps that I followed:</p>
<ul>
<li>Download the <a href="http://download.slicer.org/" rel="nofollow noopener">nightly window version of 3DSlicer</a>
</li>
<li>On 3DSlicer, Open the ‘<a href="https://www.slicer.org/wiki/File:ExtensionsManager-4.1-Install_0_ExtensionsManagerMenu.jpg" rel="nofollow noopener">Extension Manager</a>’ and install ShapeAnalysisModule (category SPHARM) in the tab ‘<a href="https://www.slicer.org/wiki/File:Extension_Manager.png" rel="nofollow noopener">Install Extensions</a>’.</li>
<li>Restart 3D Slicer</li>
<li>Open the module ShapeAnalysisModule (category SPHARM)</li>
</ul>
<p>To use SPHARM-PDM tool with less installation steps, you can also just install <a href="http://salt.slicer.org/" rel="nofollow noopener">SlicerSALT</a> by <a href="http://salt.slicer.org/download/" rel="nofollow noopener">downloading it</a>. SPHARM-PDM will be already installed and ready to use.</p>
<p>All the installation steps are explained (with explanatory visuals) in the actual <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf" rel="nofollow noopener">SPHARM-PDM tutorial</a> in the installation section.</p>
<p>If you need any more help, I will be happy to help you!</p>

---

## Post #2 by @stevenagl12 (2017-09-21 18:23 UTC)

<p>Are there any good tutorials on using SPHARM-PDM with nightly for a novice?</p>

---

## Post #3 by @bpaniagua (2017-09-25 13:57 UTC)

<p>Hi Steve,</p>
<p>There are! Here is the SPHARM-PDM updated tutorial: <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf">https://github.com/NIRALUser/SPHARM-PDM/blob/master/Doc/SPHARM-PDM-Tutorial.pdf</a></p>
<p>HTH<br>
Bea</p>

---
