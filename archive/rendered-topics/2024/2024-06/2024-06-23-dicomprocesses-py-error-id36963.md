# DICOMProcesses.py error

**Topic ID**: 36963
**Date**: 2024-06-23
**URL**: https://discourse.slicer.org/t/dicomprocesses-py-error/36963

---

## Post #1 by @Jennieyy (2024-06-23 06:48 UTC)

<p>Operating system:Windows11<br>
Slicer version:5.6<br>
Expected behavior: run a python script using 3D slicer<br>
Actual behavior: the 3D slicer source code give me a error</p>
<p>I run a python script that creates a valid dataset from the source data found on TCIA using 3D Slicer. <a href="https://github.com/KCL-BMEIS/VS_Seg/blob/master/preprocessing/data_conversion.py" class="inline-onebox" rel="noopener nofollow ugc">VS_Seg/preprocessing/data_conversion.py at master · KCL-BMEIS/VS_Seg · GitHub</a><br>
but raise an error:<br>
AttributeError: module ‘qt’ has no attribute ‘QProcess’</p>
<p>in Slicer_5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\DICOMProcesses.py</p>

---

## Post #2 by @pieper (2024-06-23 17:00 UTC)

<p>Please provide the exact steps that lead to the issue you are having.  Ideally, describe how to reproduce the issue with publicly available data.</p>

---

## Post #3 by @Jennieyy (2024-06-24 02:51 UTC)

<p>Firstly, I open the python script as a Pycharm Project, and I change the Python Interpreter (System Interpreter) to the D:/Slicer5.6.2/bin/PythonSlicer.exe, the path in 3D Slicer archive.<br>
Secondly, I run the python script aforementioned.<br>
Then, I encounter the error</p>
<pre><code class="lang-auto">"D:\Slicer 5.6.2\bin\PythonSlicer.exe" D:\Dataset_preprocess\TCIA_VS_SEG\data_conversion.py -i D:/Dataset/VS_SEG/ -o D:/Dataset/VS_SEG1/ 
No module named 'logic'
Traceback (most recent call last):
  File "D:\Dataset_preprocess\TCIA_VS_SEG\data_conversion.py", line 48, in &lt;module&gt;
    from DICOMLib import DICOMUtils
  File "D:\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "D:\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\DICOMProcesses.py", line 38, in &lt;module&gt;
    class DICOMProcess:
  File "D:\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\DICOMLib\DICOMProcesses.py", line 84, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
AttributeError: module 'qt' has no attribute 'QProcess'

Process finished with exit code 1

</code></pre>

---

## Post #4 by @Jennieyy (2024-06-24 03:15 UTC)

<p>I use the public dataset from TCIA. The raw data includes<br>
every patient’s <strong>T1 and T2 DICOM files</strong>,<br>
<strong>RT_Structure.dcm</strong> <strong>RT_Dose.dcm</strong> <strong>RT_Plan.dcm</strong> and <strong>metadata.csv</strong><br>
and tumor segmentation label <strong>contour.json</strong><br>
and T1toT2 and T2toT1 registration matrices <strong>inv_T1_LPS_to_T2_LPS.tfm</strong> or <strong>inv_T2_LPS_to_T1_LPS.tfm</strong><br>
In proprecessing raw data, Firstly, <strong>TCIA_data_convert_into_convenient_folder_structure.py</strong> makes the raw data to a convenient folder structure which puts the every patient’s T1 folder and T2 folder<br>
Secondly, <strong>data_conversion.py</strong> converts the DICOM images and contour.json to  NIFTI using the 3D Slicer. The error happens in this step.</p>

---

## Post #5 by @pieper (2024-06-24 12:42 UTC)

<p>PythonSlicer doesn’t have the application context needed to run all the DICOM options.  See the warning here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#what-is-the-pythonslicer-executable" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#what-is-the-pythonslicer-executable</a></p>
<p>You probably can just run the regular Slicer application instead.</p>

---

## Post #6 by @Jennieyy (2024-06-24 14:04 UTC)

<p>Thanks a lot!! I run the data_conversion.py in the Python Console 3D Slicer application. It works!! Thanks again.</p>

---
