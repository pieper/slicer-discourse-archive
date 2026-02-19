---
topic_id: 35142
title: "Amasss Error With Cbct Segmentation"
date: 2024-03-27
url: https://discourse.slicer.org/t/35142
---

# AMASSS error with cbct segmentation

**Topic ID**: 35142
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/amasss-error-with-cbct-segmentation/35142

---

## Post #1 by @ARtur_Zhumabekov (2024-03-27 22:36 UTC)

<p>Hello<br>
I have got a problem with AMASSS extension</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging\requirements.py”, line 35, in <strong>init</strong><br>
parsed = _parse_requirement(requirement_string)<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging_parser.py”, line 64, in parse_requirement<br>
return _parse_requirement(Tokenizer(source, rules=DEFAULT_RULES))<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging_parser.py”, line 82, in _parse_requirement<br>
url, specifier, marker = _parse_requirement_details(tokenizer)<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging_parser.py”, line 126, in _parse_requirement_details<br>
marker = _parse_requirement_marker(<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging_parser.py”, line 147, in _parse_requirement_marker<br>
tokenizer.raise_syntax_error(<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging_tokenizer.py”, line 165, in raise_syntax_error<br>
raise ParserSyntaxError(<br>
pkg_resources.extern.packaging._tokenizer.ParserSyntaxError: Expected end or semicolon (after name and no valid version specifier)<br>
torch, torchvision, torchaudio<br>
^</p>
<p>The above exception was the direct cause of the following exception:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/zhuma/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/SlicerAutomatedDentalTools/lib/Slicer-5.6/qt-scripted-modules/AMASSS.py”, line 704, in onPredictButton<br>
libs_installation = install_function(list_libs,platform.system())<br>
File “C:/Users/zhuma/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/SlicerAutomatedDentalTools/lib/Slicer-5.6/qt-scripted-modules/AMASSS.py”, line 51, in install_function<br>
if not check_lib_installed(lib, version):<br>
File “C:/Users/zhuma/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/SlicerAutomatedDentalTools/lib/Slicer-5.6/qt-scripted-modules/AMASSS.py”, line 31, in check_lib_installed<br>
installed_version = pkg_resources.get_distribution(lib_name).version<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_<em>init</em>_.py”, line 526, in get_distribution<br>
dist = Requirement.parse(dist)<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_<em>init</em>_.py”, line 3215, in parse<br>
(req,) = parse_requirements(s)<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_<em>init</em>_.py”, line 3174, in <strong>init</strong><br>
super(Requirement, self).<strong>init</strong>(requirement_string)<br>
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging\requirements.py”, line 37, in <strong>init</strong><br>
raise InvalidRequirement(str(e)) from e<br>
pkg_resources.extern.packaging.requirements.InvalidRequirement: Expected end or semicolon (after name and no valid version specifier)<br>
torch, torchvision, torchaudio</p>
<p>I tried to update conda and python, used NRRD cbct scan but still when i press Run Prediction on AMASSS extension there is no action</p>

---
