---
topic_id: 17595
title: "How To Run Cast Scalar Volume Module From Command Line"
date: 2021-05-12
url: https://discourse.slicer.org/t/17595
---

# How to run cast scalar volume module from command line

**Topic ID**: 17595
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/how-to-run-cast-scalar-volume-module-from-command-line/17595

---

## Post #1 by @shael (2021-05-12 13:39 UTC)

<p>Hi community,</p>
<p>I’m trying to run the Cast Scalar Volume module from the command line to convert a nifti brain mask into a uchar nrrd file format. I can successfully run the command from the Slicer GUI, and when I click on the red X button to see the commands Slicer ran, I get the following:</p>
<pre><code class="lang-auto">
Found CommandLine Module, target is  C:/Users/User/AppData/Local/NA-MIC/Slicer_4.11.20200930/bin/../lib/Slicer-4.11/cli-modules/CastScalarVolume.exe
ModuleType: CommandLineModule
Cast Scalar Volume command line: 

C:/Users/User/AppData/Local/NA-MIC/Slicer_4.11.20200930/bin/../lib/Slicer-4.11/cli-modules/CastScalarVolume.exe --type UnsignedChar C:/Users/User/AppData/Local/Temp/Slicer/BAHDC_vtkMRMLScalarVolumeNodeB.nrrd C:/Users/User/AppData/Local/Temp/Slicer/BAHDC_vtkMRMLScalarVolumeNodeB.nrrd 

Cast Scalar Volume completed without errors

</code></pre>
<p>I’m working on a 64bit Windows 10 machine, and using powershell for the command line. So if my path to the executable is path/to/exectuable/CastScalarVolume.exe, my input file is path/to/input/input.nii, and my desired output uchar file is path/to/output/output.nrrd, what should I run from the command line?</p>
<p>Thanks so much everyone!!</p>

---

## Post #2 by @smrolfe (2021-05-12 20:47 UTC)

<p>Check out this example running <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_call_a_CLI_module_from_command-line.3F" rel="noopener nofollow ugc">CastScalarVolume from the command line</a>. You can also get the parameter names for CLI modules using a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#get-list-of-parameter-names" rel="noopener nofollow ugc">few lines of Python</a> in the Python interactor.</p>

---

## Post #3 by @shael (2021-05-14 18:53 UTC)

<p>Hi Sara,</p>
<p>Worked like a charm! Thanks so much.</p>
<p>Best,<br>
Shael</p>

---
