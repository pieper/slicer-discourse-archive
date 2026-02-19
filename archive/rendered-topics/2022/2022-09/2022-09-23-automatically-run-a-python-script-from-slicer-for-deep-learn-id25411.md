---
topic_id: 25411
title: "Automatically Run A Python Script From Slicer For Deep Learn"
date: 2022-09-23
url: https://discourse.slicer.org/t/25411
---

# Automatically run a python script from slicer for deep learning inference purpose

**Topic ID**: 25411
**Date**: 2022-09-23
**URL**: https://discourse.slicer.org/t/automatically-run-a-python-script-from-slicer-for-deep-learning-inference-purpose/25411

---

## Post #1 by @AMK (2022-09-23 09:44 UTC)

<p>Hi,</p>
<p>I am trying to automatically run a deep learning inference from the slicer.</p>
<p>The link of the model is: (<a href="https://github.com/AMK-AQ/CTPelvic1K" class="inline-onebox" rel="noopener nofollow ugc">GitHub - AMK-AQ/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models”.</a>)</p>
<p>I have been able to automate the whole process. I have to just place the concerned CT data in a folder (which I am able to do from Slicer) and then run the script runs.py from the command window. The segmented volume is stored in another folder, which again I am able to import back into Slicer. I wanted to know how can I run this runs.py from Slicer.</p>
<p>Or is there any better alternatives.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2022-09-23 12:05 UTC)

<p>You can run external processes using this utility:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html?highlight=launchconsoleprocess#slicer.util.launchConsoleProcess" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html?highlight=launchconsoleprocess#slicer.util.launchConsoleProcess</a></p>

---

## Post #3 by @AMK (2022-09-23 13:26 UTC)

<p>I tried the following code</p>
<p>proc = slicer.util.launchConsoleProcess(r"python runs.py", useStartupEnvironment=True)<br>
slicer.util.logProcessOutput(proc)</p>
<p>But it outputs the following error:<br>
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings &gt; Manage App Execution Aliases.<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\ProgramData\NA-MIC\Slicer 5.0.3\bin\Python\slicer\util.py”, line 3459, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘python runs.py’ returned non-zero exit status 9009.</p>
<p>Thanks</p>

---

## Post #4 by @pieper (2022-09-23 15:50 UTC)

<p>The <code>useStartupEnvironment</code> will be the one that was used to launch Slicer.  If you launch from the Start menu you may get a vanilla empty environment.  If you launch Slicer.exe from the same console where you can run your python script then the command should work.</p>

---

## Post #5 by @AMK (2022-09-26 08:40 UTC)

<p>I have updated the code:</p>
<pre><code>def onRunAIButton(self):

    import os
    import sys

    pythonSlicerExecutablePath = os.path.dirname(sys.executable)+"/PythonSlicer"

    module = "runs"
    commandLine = [pythonSlicerExecutablePath, "-m", module]

    #proc = slicer.util.launchConsoleProcess(commandLine, useStartupEnvironment=True)
    proc = slicer.util.launchConsoleProcess(commandLine)
    slicer.util.logProcessOutput(proc)

    print('done')
</code></pre>
<p>The good thing is that now the slicer is able to print the things written in the python file. But its not able to run the commands in the file.</p>
<p>I am recieving the following output:</p>
<p>Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings &gt; Manage App Execution Aliases.<br>
Please cite the following paper when using CTPelvic1K dataset:</p>
<p>Pengbo, Liu, et al. “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models.” arXiv preprint arXiv: (2021).</p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/ICT-MIRACLE-lab/CTPelvic1K" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIRACLE-Center/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models”.</a><br>
C:\Users\akh\Downloads\all_data_2</p>
<p>python inference/predict_simple.py -i C:\Users\akh\Downloads\all_data_2\nnUNet\rawdata\ipcai2021_ALL_Test -o C:\Users\akh\Downloads\all_data_2\nnUNet\rawdata\ipcai2021_ALL_Test/Task22_ipcai2021__CTPelvic1K__fold0_2d_pred -t Task22_ipcai2021 -tr nnUNetTrainer -m 2d -f 0 --num_threads_preprocessing 8 --num_threads_nifti_save 4 --gpu 0</p>
<p>I tried to find the reason for the error. Apparently it says that the Python is not in the path. But i am not sure if this is correct as I am able to run all the other Python commands.</p>
<p>Am I getting something wrong here.</p>
<p>Thanks</p>

---

## Post #6 by @AMK (2022-09-26 09:35 UTC)

<p>I tried to implement the suggestion given by the above error message.</p>
<p>It now gives another error</p>
<p>Please cite the following paper when using CTPelvic1K dataset:</p>
<p>Pengbo, Liu, et al. “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models.” arXiv preprint arXiv: (2021).</p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/ICT-MIRACLE-lab/CTPelvic1K" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIRACLE-Center/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models”.</a><br>
Traceback (most recent call last):<br>
File “C:\ProgramData\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\numpy\core_<em>init</em>_.py”, line 23, in <br>
from . import multiarray<br>
File “C:\ProgramData\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\numpy\core\multiarray.py”, line 10, in <br>
from . import overrides<br>
File “C:\ProgramData\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\numpy\core\overrides.py”, line 6, in <br>
from numpy.core._multiarray_umath import (<br>
ModuleNotFoundError: No module named ‘numpy.core._multiarray_umath’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “C:\dev\CTPelvic1K\nnunet\inference\predict_simple.py”, line 8, in <br>
from nnunet.inference.predict import predict_from_folder<br>
File “C:\dev\CTPelvic1K\nnunet\inference\predict.py”, line 4, in <br>
import numpy as np<br>
File “C:\ProgramData\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\numpy_<em>init</em>_.py”, line 144, in <br>
from . import core<br>
File “C:\ProgramData\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\numpy\core_<em>init</em>_.py”, line 49, in <br>
raise ImportError(msg)<br>
ImportError:</p>
<p>IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!</p>
<p>Importing the numpy C-extensions failed. This error can happen for<br>
many reasons, often due to issues with your setup or how NumPy was<br>
installed.</p>
<p>We have compiled some common reasons and troubleshooting tips at:</p>
<pre><code>https://numpy.org/devdocs/user/troubleshooting-importerror.html
</code></pre>
<p>Please note and check the following:</p>
<ul>
<li>The Python version is: Python3.10 from “C:\Users\akh\AppData\Local\Programs\Python\Python310\python.exe”</li>
<li>The NumPy version is: “1.22.1”</li>
</ul>
<p>and make sure that they are the versions you expect.<br>
Please carefully study the documentation linked above for further help.</p>
<p>Original error was: No module named ‘numpy.core._multiarray_umath’</p>
<p>Please cite the following paper when using CTPelvic1K dataset:</p>
<p>Pengbo, Liu, et al. “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models.” arXiv preprint arXiv: (2021).</p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/ICT-MIRACLE-lab/CTPelvic1K" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIRACLE-Center/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models”.</a><br>
C:\Users\akh\Downloads\all_data_2</p>
<p>python inference/predict_simple.py -i C:\Users\akh\Downloads\all_data_2\nnUNet\rawdata\ipcai2021_ALL_Test -o C:\Users\akh\Downloads\all_data_2\nnUNet\rawdata\ipcai2021_ALL_Test/Task22_ipcai2021__CTPelvic1K__fold0_2d_pred -t Task22_ipcai2021 -tr nnUNetTrainer -m 2d -f 0 --num_threads_preprocessing 8 --num_threads_nifti_save 4 --gpu 0</p>

---

## Post #7 by @pieper (2022-09-26 16:52 UTC)

<p>You are running Slicer’s python environment, which is not the same as the one you get in a console.  To run the console version you’ll need to set an environment that matches the console’s so the correct python environment is used.</p>

---

## Post #8 by @rbumm (2022-09-27 07:08 UTC)

<p>Maybe you should set up a batch file first that exactly does what you expect - just for testing and outside Slicer.</p>
<p>For example, create a file “runai.bat” in your Windows home directory with the following content (adjust the path to the Python script directory and put your file “runs.py” there) :</p>
<pre><code class="lang-auto">cd "C:\Users\YourName\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts"
python runs.py
pause
</code></pre>
<p>Double-click runai.bat.</p>
<p>Is this working? If yes we could provide the next steps.</p>

---

## Post #9 by @AMK (2022-09-27 09:40 UTC)

<p>The batch file is working. I had to do some more scripting there, but it’s working really nice.</p>
<p>Thanks.</p>

---

## Post #10 by @rbumm (2022-09-27 09:53 UTC)

<p>Very good.</p>
<p>So you could copy your “runs.py” script into the Slicer Python script directory and do the following from within Slicer or a Slicer extension now:</p>
<pre><code class="lang-auto"># get current directory 
beforeDir = os.getcwd()

# get Slicer home bin folder
slicerHomeBinDir = slicer.app.slicerHome
slicerHomeDir = slicerHomeBinDir.removesuffix('/bin/..')

# change to Slicer script directory
os.chdir(slicerHomeDir + r"/lib/Python/Scripts")
                
# run your script from Slicer script directory
proc = slicer.util.launchConsoleProcess(r"python ./runs.py")
slicer.util.logProcessOutput(proc)

# change to before directory
os.chdir(beforeDir)

</code></pre>
<p>The Python script directory for Slicer 5.0.3 in Windows would be at</p>
<pre><code class="lang-auto">C:\Users\Yourname\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Python\Scripts
</code></pre>

---

## Post #11 by @AMK (2022-09-27 11:51 UTC)

<p>Thanks for the script. I tried to implement this in Slicer. It starts the process perfectly, but after sometime the whole system crashes and the system restarts. I didn’t faced this problem when working from the anaconda prompt or from the bash file etc. Do you have any suggestion what might be the cause?</p>

---

## Post #12 by @rbumm (2022-09-27 12:05 UTC)

<p>Not really, try to debug this by using a very basic Python script “runs.py” initially with a <code>print("Hello")</code> and make this more complex later, see where it fails …</p>
<p>Are you working with the latest stable version of 3D Slicer?</p>

---

## Post #13 by @AMK (2022-09-27 12:25 UTC)

<p>Yes, I am using the latest stable version of Slicer (5.0.3).</p>
<p>I ran the code in Slicer 4.11.20210226 and it worked perfectly with this version.</p>

---

## Post #14 by @AMK (2022-09-30 08:31 UTC)

<p>So my code works with old version of Slicer. But it crashes with Slicer 5.0.3 and restarts the computer. Is there any way I can make it work with the latest version also?</p>
<p>Thanks.</p>

---

## Post #15 by @rbumm (2022-09-30 09:18 UTC)

<p>We’ve recently been integrating a call to a complex deep learning tool (<a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator</a>)  in our Lung CT Segmenter extension without crashing 5.0.3 stable.</p>
<p>See the <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/LungCTSegmenter/LungCTSegmenter.py#L1532:~:text=elif%20self.,Segmentation%20done.%22">code segment here</a>. You could even <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Step-2-Using-Lung-CT-Segmenter-with-experimental-AI">test the extension yourself</a>.</p>
<p>As you probably do not want to publish your code yet, I fear you would need to debug the code step by step and identify the part that crashes Slicer.</p>
<p>If your code is available online please provide a link.</p>

---
