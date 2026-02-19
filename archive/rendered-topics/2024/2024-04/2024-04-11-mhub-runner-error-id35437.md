---
topic_id: 35437
title: "Mhub Runner Error"
date: 2024-04-11
url: https://discourse.slicer.org/t/35437
---

# mHUB runner error

**Topic ID**: 35437
**Date**: 2024-04-11
**URL**: https://discourse.slicer.org/t/mhub-runner-error/35437

---

## Post #1 by @dr_deem (2024-04-11 15:16 UTC)

<p>SlicerMrunner error.                                                                                                 Python 3.9.10 (main, Apr  5 2024, 01:02:26) [MSC v.1938 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Qt] Designer: Reading properties of the type 0 is not supported yet.<br>
Collecting pyyaml<br>
Using cached PyYAML-6.0.1-cp39-cp39-win_amd64.whl.metadata (2.1 kB)<br>
Using cached PyYAML-6.0.1-cp39-cp39-win_amd64.whl (152 kB)<br>
Installing collected packages: pyyaml<br>
Successfully installed pyyaml-6.0.1<br>
Collecting pandas<br>
Using cached pandas-2.2.2-cp39-cp39-win_amd64.whl.metadata (19 kB)<br>
Requirement already satisfied: numpy&gt;=1.22.4 in c:\users\monster\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (from pandas) (1.26.1)<br>
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\monster\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (from pandas) (2.8.2)<br>
Collecting pytz&gt;=2020.1 (from pandas)<br>
Using cached pytz-2024.1-py2.py3-none-any.whl.metadata (22 kB)<br>
Collecting tzdata&gt;=2022.7 (from pandas)<br>
Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)<br>
Requirement already satisfied: six&gt;=1.5 in c:\users\monster\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;pandas) (1.16.0)<br>
Using cached pandas-2.2.2-cp39-cp39-win_amd64.whl (11.6 MB)<br>
Using cached pytz-2024.1-py2.py3-none-any.whl (505 kB)<br>
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)<br>
Installing collected packages: pytz, tzdata, pandas<br>
Successfully installed pandas-2.2.2 pytz-2024.1 tzdata-2024.1<br>
Collecting git+https://github.com/MHubAI/SegDB.git<br>
Cloning <a href="https://github.com/MHubAI/SegDB.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MHubAI/SegDB: Database and tools for standardized segmentation codes.</a> to c:\users\monster\appdata\local\temp\pip-req-build-1j91bj8x<br>
Running command git clone --filter=blob:none --quiet <a href="https://github.com/MHubAI/SegDB.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MHubAI/SegDB: Database and tools for standardized segmentation codes.</a> ‘C:\Users\monster\AppData\Local\Temp\pip-req-build-1j91bj8x’<br>
Resolved <a href="https://github.com/MHubAI/SegDB.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MHubAI/SegDB: Database and tools for standardized segmentation codes.</a> to commit 79add4b3176b3676673edef4fad32a18e9770d39<br>
Preparing metadata (setup.py): started<br>
Preparing metadata (setup.py): finished with status ‘done’<br>
Building wheels for collected packages: segdb<br>
Building wheel for segdb (setup.py): started<br>
Building wheel for segdb (setup.py): finished with status ‘done’<br>
Created wheel for segdb: filename=segdb-0.0.1-py3-none-any.whl size=16321 sha256=90c9e10e753c6c2352dd8e7b8d289f6590d4a3cb4070335366c719a570e8bf72<br>
Stored in directory: C:\Users\monster\AppData\Local\Temp\pip-ephem-wheel-cache-2_qizwmb\wheels\cd\e3\2b\bcc842045c9e3e9228c56d15e666f91fdb02e9ebd8097bb720<br>
Successfully built segdb<br>
Installing collected packages: segdb<br>
Successfully installed segdb-0.0.1<br>
Traceback (most recent call last):<br>
File “C:/Users/monster/SlicerMRunner/MRunner/MRunner.py”, line 110, in setup<br>
self.onUpdateRepoButtonClick(reinstallSegDB=False)<br>
File “C:/Users/monster/SlicerMRunner/MRunner/MRunner.py”, line 452, in onUpdateRepoButtonClick<br>
self.models = Models.Repository(self.resourcePath(‘MHub/models.json’))<br>
File “C:\Users\monster\SlicerMRunner\MRunner\Utils\Models.py”, line 27, in <strong>init</strong><br>
self.data = json.load(f)<br>
File “C:\Users\monster\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json_<em>init</em>_.py”, line 293, in load<br>
return loads(fp.read(),<br>
File “C:\Users\monster\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json_<em>init</em>_.py”, line 346, in loads<br>
return _default_decoder.decode(s)<br>
File “C:\Users\monster\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py”, line 337, in decode<br>
obj, end = self.raw_decode(s, idx=_w(s, 0).end())<br>
File “C:\Users\monster\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py”, line 355, in raw_decode<br>
raise JSONDecodeError(“Expecting value”, s, err.value) from None<br>
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)<br>
 → updateGUIFromParameterNode</p>

---
