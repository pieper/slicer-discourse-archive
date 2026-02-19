---
topic_id: 24401
title: "Modulewizard Script Problems"
date: 2022-07-20
url: https://discourse.slicer.org/t/24401
---

# ModuleWizard script problems

**Topic ID**: 24401
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/modulewizard-script-problems/24401

---

## Post #1 by @torquil (2022-07-20 05:33 UTC)

<p>Hi! I’m going to create a new module. I followed a tutorial which told med to download the source code and run the following:</p>
<p>python3 ./Utilities/Scripts/ModuleWizard.py --template ./Extensions/Testing/ScriptedLoadableExtensionTemplate --target …/ModuleName ModuleName</p>
<p>There are two problems. First, it didn’t work with python3:</p>
<p>Will copy<br>
{template}<br>
to<br>
{target}<br>
replacing “{templateKey}” with “{moduleName}”</p>
<p>[‘CMakeLists.txt’, ‘ScriptedLoadableExtensionTemplate.png’, ‘ScriptedLoadableModuleTemplate/CMakeLists.txt’, ‘ScriptedLoadableModuleTemplate/ScriptedLoadableModuleTemplate.py’, ‘ScriptedLoadableModuleTemplate/Resources/Icons/ScriptedLoadableModuleTemplate.png’, ‘ScriptedLoadableModuleTemplate/Testing/CMakeLists.txt’, ‘ScriptedLoadableModuleTemplate/Testing/Python/CMakeLists.txt’]<br>
creating …/TorquilTools/CMakeLists.txt<br>
creating …/TorquilTools/TorquilTools.png<br>
Traceback (most recent call last):<br>
File “/home/torquil/Slicer/./Utilities/Scripts/ModuleWizard.py”, line 123, in <br>
main(sys.argv[1:])<br>
File “/home/torquil/Slicer/./Utilities/Scripts/ModuleWizard.py”, line 117, in main<br>
copyAndReplace(file, template, target, templateKey, moduleName)<br>
File “/home/torquil/Slicer/./Utilities/Scripts/ModuleWizard.py”, line 39, in copyAndReplace<br>
contents = fp.read()<br>
File “/usr/lib/python3.10/codecs.py”, line 322, in decode<br>
(result, consumed) = self._buffer_decode(data, self.errors, final)<br>
UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0x89 in position 0: invalid start byte</p>
<p>So I ran this:</p>
<p>python2.7 ./Utilities/Scripts/ModuleWizard.py --template ./Extensions/Testing/ScriptedLoadableExtensionTemplate --target …/ModuleName ModuleName</p>
<p>but this gave the following error:</p>
<p>File “./Utilities/Scripts/ModuleWizard.py”, line 112<br>
print(f"\nWill copy \n\t{template} \nto \n\t{target} \nreplacing "{templateKey}" with "{moduleName}"\n")<br>
^<br>
SyntaxError: invalid syntax</p>
<p>Removing an “f” at the beginning of the print() argument seemed to solve the problem. Is that  bug?</p>
<p>Will the script also be updated to work with python3?</p>
<p>Best regards,<br>
Torquil Sørensen, Norway</p>

---
