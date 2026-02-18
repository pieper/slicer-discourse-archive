# Problems with the SPHARM-PDM on Slicer-4.8.0-linux-amd64 (Command-Line Tool, the step GenParaMesh)

**Topic ID**: 15877
**Date**: 2021-02-07
**URL**: https://discourse.slicer.org/t/problems-with-the-spharm-pdm-on-slicer-4-8-0-linux-amd64-command-line-tool-the-step-genparamesh/15877

---

## Post #1 by @Daisy_Xiong (2021-02-07 04:31 UTC)

<p>Hello, everyone,</p>
<p>I tried to utilize the software Slicer(Slicer-4.8.0-linux-amd64) and the method SPHARM-PDM to get the some SPHARM Mesh ( such as the output files *para.vtk and *SPHARM_Ellalign.vtk).</p>
<p>If I use the main window, and select the module through click ’ Modules – Shape Analysis Module’, and then select the input and output directories, I can run the SPDM analysis successfully.<br>
Finally, I can obtain the 3 output folders (Step1_SegPostProcess , Step2_GenMeshPara, Step3_ParaToSPHARMMesh).</p>
<p>But if I try to use the SPHARM-PDM Command-Line Tool on Linux: ./Slicer --no-main-window --python-script share/Slicer-4.8/CommandLineTool/SPHARM-PDM.py share/Slicer-4.8/CommandLineTool/SPHARM-PDM-parameters.ini<br>
) for the same dataset as before, I will get some errors in the step GenParaMesh like the following content:</p>
<p><em>GenParaMesh standard output:</em></p>
<p><em>itk::ExceptionObject (0x7ffddee49b80)</em><br>
*Location: “Unknown” *<br>
<em>File: /home/kitware/Dashboards/Nightly/S-480-E-b/SPHARM-PDM/Libraries/Shape/Algorithms/BinaryMask3DEqualAreaParametricMeshSource.txx</em><br>
<em>Line: 97</em><br>
<em>Description: BinaryMask3DEqualAreaParametricMeshSource : Image empty</em></p>
<p><em>GenParaMesh completed with errors</em></p>
<p>I tried to fix this error but failed. Could you kindly guide me to solve this problem? Thank you very much！</p>
<p>I would appreciate any help, thanks in advance.</p>
<p>Daisy</p>

---
