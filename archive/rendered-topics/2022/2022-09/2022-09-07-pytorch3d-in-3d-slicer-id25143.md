---
topic_id: 25143
title: "Pytorch3D In 3D Slicer"
date: 2022-09-07
url: https://discourse.slicer.org/t/25143
---

# PyTorch3D in 3D Slicer

**Topic ID**: 25143
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/pytorch3d-in-3d-slicer/25143

---

## Post #1 by @Connor-Bowley (2022-09-07 17:17 UTC)

<p>As part of SlicerSALT, the <a href="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg" rel="noopener nofollow ugc">SlicerDentalModelSeg</a> extension used <a href="https://github.com/facebookresearch/pytorch3d" rel="noopener nofollow ugc">PyTorch3D</a> to run segment and number teeth from a <code>vtkMRMLModelNode</code> of an intraoral scan. There was some difficulty in getting PyTorch3D to install in Slicer, and it currently only works on Linux.</p>
<p>Given that there may be more projects in the future that could benefit from PyTorch3D, and it would be good if SlicerDentalModelSeg could run on Windows and Mac as well as Linux, I am wondering if an extension can be made that will take care of the install. I know that <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">SlicerPyTorch</a> exists to ease the use of PyTorch in 3D Slicer, which leads to few couple questions:</p>
<ol>
<li>Would it make sense to create a SlicerPyTorch3D extension that handled the install? If so, what is the relation to SlicerPyTorch?</li>
<li>Would it instead make sense to have SlicerPyTorch (optionally) install PyTorch3D?</li>
<li>Has anyone already installed PyTorch3D in Slicer such that it works for all platforms, or even some of them?</li>
</ol>

---

## Post #2 by @pieper (2022-09-07 20:54 UTC)

<p>Agreed, PyTorch3D sounds like something we’d want to have available as widely as possible, although I have not tried it myself…  I think the idea of adding it to SlicerPyTorch makes sense since PyTorch is a core dependency of PyTorch3D.</p>

---

## Post #3 by @Nathan_Hutin (2023-07-12 20:03 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a><br>
I am working to deploy a Slicer extension or intraoral scans that uses PyTorch3D. It is working properly, but I was able to install it only in Slicer on Linux. I tried <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">SlicerPyTorch</a> but it does not install PyTorch3D in Slicer on Windows.<br>
Back in Sep 2022, Steve had suggested that it made sense to add PyTorch3D to SlicerPyTorch. Can one of you please guide me how to install PyTorch3D in Slicer on Windows? If code development needs to be done, I am willing to work on contributing to the code, but I would really appreciate your guidance on what I need to do. Thank you.</p>

---

## Post #4 by @Nathan_Hutin (2023-07-12 20:05 UTC)

<p><a class="mention" href="/u/allemangd">@allemangd</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
I am a new user and I was not able to tag David and Andras in my previous message  ( it said there was a limit of reply to  only two users) so I am resending to you.<br>
I am working to deploy a Slicer extension or intraoral scans that uses PyTorch3D. It is working properly, but I was able to install it only in Slicer on Linux. I tried <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">SlicerPyTorch</a> but it does not install PyTorch3D in Slicer on Windows.<br>
Back in Sep 2022, Steve had suggested that it made sense to add PyTorch3D to SlicerPyTorch. Can one of you please guide me how to install PyTorch3D in Slicer on Windows? If code development needs to be done, I am willing to work on contributing to the code, but I would really appreciate your guidance on what I need to do. Thank you.</p>

---

## Post #5 by @lassoan (2023-07-12 20:30 UTC)

<p>PyTorch Slicer extension is only needed because PyTorch Python package is over the maximum size limit of PyPI and therefore it requires special mechanisms to download and install. For all other Python packages, you should be able to use <code>slicer.util.pip_install()</code>.</p>
<p>The problem with <code>PyTorch3D</code> is that <a href="https://pypi.org/project/pytorch3d/#files">it does not have binary packages on PyPI</a>. Many people complain about this - see the <a href="https://github.com/facebookresearch/pytorch3d/issues?q=is%3Aissue+is%3Aopen+install">40 open issues about installation in their tracker</a>. Considering that having packages on PyPI is such a basic requirement and PyTorch3D developers don’t care about it, the only recommendation I can make is avoid using PyTorch3D.</p>

---

## Post #6 by @Nathan_Hutin (2023-07-12 20:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Thank you. Can you please suggest another framework that can replace PyTorch3D?</p>

---

## Post #7 by @lassoan (2023-07-12 20:56 UTC)

<p>Sorry, I don’t have any suggestion. Others might.<br>
If you find alternatives then please report it back here.</p>

---

## Post #8 by @Nathan_Hutin (2023-07-12 21:15 UTC)

<p>I am planning to investigate issues with Slicer on Windows installation using  as possible alternative frameworks, Kaolin, Tensorflow3D, Tensorflow graphics and Unity Barracuda.</p>
<p>If you have any indication on which one to start with,  I appreciate any guidance.</p>

---

## Post #9 by @pieper (2023-07-13 15:40 UTC)

<p>The field is evolving very quickly, so it’s hard to know which will work best for your research.  As a general approach tough, I’d suggest using an external python environment with miniconda to isolate a package with all the pytorch3d dependencies and then communicate with Slicer through files or network connections.</p>

---

## Post #10 by @Nathan_Hutin (2023-07-13 15:50 UTC)

<p>Thank your for your answer <a class="mention" href="/u/pieper">@pieper</a>.<br>
I am going to try your suggestion.</p>

---

## Post #11 by @Nathan_Hutin (2023-07-20 21:09 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a><br>
I investigated some technics to find a solution.</p>
<p>First, I tried to use docker in Python with the <a href="https://docker-py.readthedocs.io/en/stable/containers.html" rel="noopener nofollow ugc">docker library</a>. The docker library is an API that uses docker on the desktop. It is a problem because that means the users have to install docker, this idea is not an option.</p>
<p>The error I got is below.</p>
<blockquote>
<p>client = docker.from_env()<br>
client.containers.run(‘hunath/pythontest’,volumes=[‘path/TestDocker:/app/’] )<br>
raise DockerException(docker.errors.DockerException: Error while fetching server API version:(‘Connection aborted.’, FileNotFoundError(2, ‘No such file or directory’))</p>
</blockquote>
<p>The error was obtained on Windows without docker installed.</p>
<p>The second test was to use the <a href="https://docs.python.org/3/library/subprocess.html" rel="noopener nofollow ugc">subprocess library</a> with Python environment create by miniconda or the venv library.<br>
The different difficulties I meet were:</p>
<ul>
<li>using subprocesses on Windows because python couldn’t open my python file</li>
</ul>
<blockquote>
<p>command_line =[os.path.normpath(‘C:/Users/…/Python/Python36/python’),os.path.normpath(‘C:/Users/…/testpython.py’)]<br>
subprocess.run(command_line,env=slicer.util.startupEnvironment())</p>
<p>CompletedProcess(args=[‘C:\Users\…\Python\Python36\python’, ‘C:\Users\…\testpython.py’], returncode=2)<br>
[FD] C:\Users.…\Python\Python36\python: can’t open file ‘C:\Users.…\testpython.py’: [Errno 2] No such file or directory</p>
</blockquote>
<ul>
<li>I don’t know how to install packages in a specific environment with pip. I suppose I should use the argument target of pip but I don’t know which folder I should target.</li>
<li>For miniconda, I tried to use the <a href="https://docs.conda.io/projects/conda/en/stable/api/python_api.html" rel="noopener nofollow ugc">conda.cli.python_ali library</a>, but it was impossible to import in Slicer. I suppose it’s the same problem as docker because this library it’s also an API.</li>
</ul>
<p>If you have an idea how to solve any of these problems, that would be very helpful. If you have links or Python libraries that might be interesting to investigate, I would be interested.</p>

---

## Post #12 by @lassoan (2023-07-20 22:26 UTC)

<p>Many Slicer extensions use PyTorch, for example <a href="https://github.com/lassoan/SlicerTotalSegmentator">TotalSegmentator</a> and <a href="https://github.com/lassoan/SlicerHDBrainExtraction">HDBrainExtraction</a>. You can use them as examples for installing and using PyTorch in an extension.</p>

---

## Post #13 by @luciacev (2023-07-25 20:04 UTC)

<p>Thanks so much Andras! Our issue is that at least 3  Slicer extensions that our group developed, DentalModelSeg, ALIIOS and ARegIOS use Pytorch 3D. <a class="mention" href="/u/juanprietob">@juanprietob</a> suggested using Docker which Nathan has not been able to install in Windows. Can someone please provide guidance on how to install Docker in Windows?<br>
<a class="mention" href="/u/pieper">@pieper</a>  suggested using an external python environment with miniconda to isolate a package with all the pytorch3d dependencies and then communicate with Slicer through files or network connections.<br>
Can one of you please suggest how to connect miniconda with Slicer through files or network connections?</p>

---

## Post #14 by @pieper (2023-07-27 17:35 UTC)

<aside class="quote no-group" data-username="luciacev" data-post="13" data-topic="25143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luciacev/48/66975_2.png" class="avatar"> luciacev:</div>
<blockquote>
<p>Can one of you please suggest how to connect miniconda with Slicer through files or network connections?</p>
</blockquote>
</aside>
<p>If you want to control the Pytorch3D process from Slicer, then using QProcess is a good option.  You can send commands and data to the miniconda instance using stdin and get results via stdout, like what’s done <a href="https://github.com/pieper/SlicerParallelProcessing">in the Processes</a> module of the ParallelProcessing extension.  In addition to stdin/stdout, if the processes share a filesystem they can read and write files to exchange data.</p>
<p>Another option is to create a server, like in MONAI Label, or use OpenIGTLink.</p>

---

## Post #15 by @jcfr (2023-07-27 18:20 UTC)

<blockquote>
<p>suggested using an external python environment with miniconda to isolate</p>
</blockquote>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-external-process-in-startup-environment">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-external-process-in-startup-environment</a></p>
<p>And if using the <code>subprocess.check_output</code> referenced above is not enough … you could achieve similar outcome leveraging <code>QProcess</code>.</p>
<pre data-code-wrap="python"><code class="lang-python">process = qt.QProcess()
process.setProcessChannelMode(qt.QProcess.ForwardedChannels)

processEnv = qt.QProcessEnvironment()
for var_name, var_value in slicer.util.startupEnvironment().items():
    processEnv.insert(var_name, var_value)

process.setProcessEnvironment(processEnv)

process.setProgram("python3.11")
process.setArguments(["-c", "import sys; print(sys.version)"])

process.start()
process.waitForStarted()
</code></pre>
<blockquote>
<p>communicate with Slicer through files</p>
</blockquote>
<p>When invoking the external process, you would indicate what should be the input/output files/directories.</p>
<blockquote>
<p>communicate with Slicer through […] network connections</p>
</blockquote>
<p>I suggest to first looking into a file based integration</p>

---

## Post #17 by @Gaelle_Leroux (2023-11-02 19:20 UTC)

<p>Hello !</p>
<p>Just an update, I managed to run some code using pytorch3d on windows.<br>
To do this I used WSL. I installed miniconda on it and in a new environment I was able to download pytorch3d and all the other libraries needed for my code. The code is then able to run correctly using pytorch3d.<br>
I’m still trying to automate the wsl installation to simplify it. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #18 by @7738censhy (2023-11-15 20:46 UTC)

<p>Hi<br>
I have problem in install pytorch</p>
<p>the totalsegmentor need to download pytorch and after download it  , it erroer in installion</p>

---

## Post #19 by @rbumm (2023-11-16 09:14 UTC)

<p>Download and install the PyTorch extension, then install PyTorch from there.</p>

---

## Post #20 by @lassoan (2023-11-23 12:48 UTC)

<p>If you have a failed Pytorch install attempt (you have run out of disk space or there was network instability during installation) then you may need to uninstall Pytorch first (using the extension), restart Slicer, and then install Pytorch again. Note that you may need 20GB free disk space during installation (the final amount of used disk space will be less, but you need a lot of space during installation).</p>

---
