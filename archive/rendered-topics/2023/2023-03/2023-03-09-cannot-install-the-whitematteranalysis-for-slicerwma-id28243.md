---
topic_id: 28243
title: "Cannot Install The Whitematteranalysis For Slicerwma"
date: 2023-03-09
url: https://discourse.slicer.org/t/28243
---

# Cannot install the whitematteranalysis for SlicerWMA

**Topic ID**: 28243
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/cannot-install-the-whitematteranalysis-for-slicerwma/28243

---

## Post #1 by @Fumi (2023-03-09 00:52 UTC)

<p>Hi all,<br>
I am having a problem in installing whitematteranalysis with pip as follows;</p>
<p>(base) C:\Users\kidokoro_win&gt;  pip install git+https://github.com/SlicerDMRI/whitematteranalysis.git<br>
Collecting git+https://github.com/SlicerDMRI/whitematteranalysis.git<br>
Cloning <a href="https://github.com/SlicerDMRI/whitematteranalysis.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerDMRI/whitematteranalysis: White matter tractography clustering and more...</a> to c:\users\kidokoro_win\appdata\local\temp\pip-req-build-w2zcv6au<br>
Running command git clone --filter=blob:none --quiet <a href="https://github.com/SlicerDMRI/whitematteranalysis.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerDMRI/whitematteranalysis: White matter tractography clustering and more...</a> ‘C:\Users\kidokoro_win\AppData\Local\Temp\pip-req-build-w2zcv6au’<br>
Resolved <a href="https://github.com/SlicerDMRI/whitematteranalysis.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerDMRI/whitematteranalysis: White matter tractography clustering and more...</a> to commit 5bbe6a17fc37e68530fb578476339943e5cc57c4<br>
Preparing metadata (setup.py) … done<br>
Collecting cython<br>
Using cached Cython-0.29.33-py2.py3-none-any.whl (987 kB)<br>
Requirement already satisfied: numpy in c:\users\kidokoro_win\miniconda3\lib\site-packages (from WhiteMatterAnalysis==0.3.0) (1.23.5)<br>
Requirement already satisfied: setuptools in c:\users\kidokoro_win\miniconda3\lib\site-packages (from WhiteMatterAnalysis==0.3.0) (65.6.3)<br>
Collecting scipy<br>
Downloading scipy-1.10.1-cp310-cp310-win_amd64.whl (42.5 MB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.5/42.5 MB 10.4 MB/s eta 0:00:00<br>
Collecting vtk<br>
Downloading vtk-9.2.6-cp310-cp310-win_amd64.whl (48.8 MB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.8/48.8 MB 10.7 MB/s eta 0:00:00<br>
Requirement already satisfied: joblib in c:\users\kidokoro_win\miniconda3\lib\site-packages (from WhiteMatterAnalysis==0.3.0) (1.2.0)<br>
Collecting statsmodels<br>
Downloading statsmodels-0.13.5-cp310-cp310-win_amd64.whl (9.1 MB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.1/9.1 MB 11.5 MB/s eta 0:00:00<br>
Collecting xlrd<br>
Downloading xlrd-2.0.1-py2.py3-none-any.whl (96 kB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.5/96.5 kB 5.8 MB/s eta 0:00:00<br>
Collecting matplotlib<br>
Downloading matplotlib-3.7.1-cp310-cp310-win_amd64.whl (7.6 MB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.6/7.6 MB 11.6 MB/s eta 0:00:00<br>
Collecting nibabel<br>
Downloading nibabel-5.0.1-py3-none-any.whl (3.3 MB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 11.0 MB/s eta 0:00:00<br>
Requirement already satisfied: packaging&gt;=20.0 in c:\users\kidokoro_win\miniconda3\lib\site-packages (from matplotlib-&gt;WhiteMatterAnalysis==0.3.0) (22.0)<br>
Requirement already satisfied: python-dateutil&gt;=2.7 in c:\users\kidokoro_win\miniconda3\lib\site-packages (from matplotlib-&gt;WhiteMatterAnalysis==0.3.0) (2.8.2)<br>
Requirement already satisfied: pillow&gt;=6.2.0 in c:\users\kidokoro_win\miniconda3\lib\site-packages (from matplotlib-&gt;WhiteMatterAnalysis==0.3.0) (9.4.0)<br>
Collecting fonttools&gt;=4.22.0<br>
Downloading fonttools-4.39.0-py3-none-any.whl (1.0 MB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 8.0 MB/s eta 0:00:00<br>
Collecting contourpy&gt;=1.0.1<br>
Downloading contourpy-1.0.7-cp310-cp310-win_amd64.whl (162 kB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.0/163.0 kB 10.2 MB/s eta 0:00:00<br>
Collecting kiwisolver&gt;=1.0.1<br>
Downloading kiwisolver-1.4.4-cp310-cp310-win_amd64.whl (55 kB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.3/55.3 kB ? eta 0:00:00<br>
Collecting pyparsing&gt;=2.3.1<br>
Downloading pyparsing-3.0.9-py3-none-any.whl (98 kB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 98.3/98.3 kB 5.5 MB/s eta 0:00:00<br>
Collecting cycler&gt;=0.10<br>
Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)<br>
Collecting patsy&gt;=0.5.2<br>
Downloading patsy-0.5.3-py2.py3-none-any.whl (233 kB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 233.8/233.8 kB 14.9 MB/s eta 0:00:00<br>
Collecting pandas&gt;=0.25<br>
Downloading pandas-1.5.3-cp310-cp310-win_amd64.whl (10.4 MB)<br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.4/10.4 MB 11.5 MB/s eta 0:00:00<br>
Requirement already satisfied: pytz&gt;=2020.1 in c:\users\kidokoro_win\miniconda3\lib\site-packages (from pandas&gt;=0.25-&gt;statsmodels-&gt;WhiteMatterAnalysis==0.3.0) (2022.7)<br>
Requirement already satisfied: six in c:\users\kidokoro_win\miniconda3\lib\site-packages (from patsy&gt;=0.5.2-&gt;statsmodels-&gt;WhiteMatterAnalysis==0.3.0) (1.16.0)<br>
Building wheels for collected packages: WhiteMatterAnalysis<br>
Building wheel for WhiteMatterAnalysis (setup.py) … error<br>
error: subprocess-exited-with-error</p>
<p>× python setup.py bdist_wheel did not run successfully.<br>
│ exit code: 1<br>
╰─&gt; [38 lines of output]<br>
C:\Users\kidokoro_win\miniconda3\lib\site-packages\setuptools\installer.py:27: SetuptoolsDeprecationWarning: setuptools.installer is deprecated. Requirements should be satisfied by a PEP 517 installer.<br>
warnings.warn(<br>
running bdist_wheel<br>
running build<br>
running build_py<br>
creating build<br>
creating build\lib.win-amd64-cpython-310<br>
creating build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\cluster.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\congeal_multisubject.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\congeal_to_atlas.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\fibers.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\filter.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\io.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\laterality.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\mrml.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register_two_subjects.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register_two_subjects_nonrigid.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register_two_subjects_nonrigid_bsplines.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\relative_distance.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\render.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\similarity.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\tract_measurement.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis_<em>init</em>_.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
running build_ext<br>
cythoning whitematteranalysis/fibers.pyx to whitematteranalysis\fibers.c<br>
c:\users\kidokoro_win\appdata\local\temp\pip-req-build-w2zcv6au.eggs\cython-0.29.33-py3.10.egg\Cython\Compiler\Main.py:369: FutureWarning: Cython directive ‘language_level’ not set, using 2 for now (Py2). This will change in a later release! File: C:\Users\kidokoro_win\AppData\Local\Temp\pip-req-build-w2zcv6au\whitematteranalysis\fibers.pyx<br>
tree = Parsing.p_module(s, pxd, full_module_name)<br>
cythoning whitematteranalysis/similarity.pyx to whitematteranalysis\similarity.c<br>
c:\users\kidokoro_win\appdata\local\temp\pip-req-build-w2zcv6au.eggs\cython-0.29.33-py3.10.egg\Cython\Compiler\Main.py:369: FutureWarning: Cython directive ‘language_level’ not set, using 2 for now (Py2). This will change in a later release! File: C:\Users\kidokoro_win\AppData\Local\Temp\pip-req-build-w2zcv6au\whitematteranalysis\similarity.pyx<br>
tree = Parsing.p_module(s, pxd, full_module_name)<br>
building ‘whitematteranalysis.fibers’ extension<br>
creating build\temp.win-amd64-cpython-310<br>
creating build\temp.win-amd64-cpython-310\Release<br>
creating build\temp.win-amd64-cpython-310\Release\whitematteranalysis<br>
cl.exe /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\kidokoro_win\miniconda3\lib\site-packages\numpy\core\include -IC:\Users\kidokoro_win\miniconda3\include -IC:\Users\kidokoro_win\miniconda3\Include /Tcwhitematteranalysis\fibers.c /Fobuild\temp.win-amd64-cpython-310\Release\whitematteranalysis\fibers.obj<br>
error: command ‘cl.exe’ failed: None<br>
[end of output]</p>
<p>note: This error originates from a subprocess, and is likely not a problem with pip.<br>
ERROR: Failed building wheel for WhiteMatterAnalysis<br>
Running setup.py clean for WhiteMatterAnalysis<br>
Failed to build WhiteMatterAnalysis<br>
Installing collected packages: xlrd, scipy, pyparsing, patsy, nibabel, kiwisolver, fonttools, cython, cycler, contourpy, pandas, matplotlib, vtk, statsmodels, WhiteMatterAnalysis<br>
Running setup.py install for WhiteMatterAnalysis … error<br>
error: subprocess-exited-with-error</p>
<p>× Running setup.py install for WhiteMatterAnalysis did not run successfully.<br>
│ exit code: 1<br>
╰─&gt; [34 lines of output]<br>
running install<br>
C:\Users\kidokoro_win\miniconda3\lib\site-packages\setuptools\command\install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.<br>
warnings.warn(<br>
running build<br>
running build_py<br>
creating build<br>
creating build\lib.win-amd64-cpython-310<br>
creating build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\cluster.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\congeal_multisubject.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\congeal_to_atlas.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\fibers.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\filter.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\io.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\laterality.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\mrml.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register_two_subjects.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register_two_subjects_nonrigid.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\register_two_subjects_nonrigid_bsplines.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\relative_distance.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\render.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\similarity.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis\tract_measurement.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
copying whitematteranalysis_<em>init</em>_.py → build\lib.win-amd64-cpython-310\whitematteranalysis<br>
running build_ext<br>
skipping ‘whitematteranalysis\fibers.c’ Cython extension (up-to-date)<br>
skipping ‘whitematteranalysis\similarity.c’ Cython extension (up-to-date)<br>
building ‘whitematteranalysis.fibers’ extension<br>
creating build\temp.win-amd64-cpython-310<br>
creating build\temp.win-amd64-cpython-310\Release<br>
creating build\temp.win-amd64-cpython-310\Release\whitematteranalysis<br>
cl.exe /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\kidokoro_win\miniconda3\lib\site-packages\numpy\core\include -IC:\Users\kidokoro_win\miniconda3\include -IC:\Users\kidokoro_win\miniconda3\Include /Tcwhitematteranalysis\fibers.c /Fobuild\temp.win-amd64-cpython-310\Release\whitematteranalysis\fibers.obj<br>
error: command ‘cl.exe’ failed: None<br>
[end of output]</p>
<p>note: This error originates from a subprocess, and is likely not a problem with pip.<br>
error: legacy-install-failure</p>
<p>× Encountered error while trying to install package.<br>
╰─&gt; WhiteMatterAnalysis</p>
<p>note: This is an issue with the package mentioned above, not pip.<br>
hint: See above for output from the failure.</p>
<p>Could anyone tell me how to solve this?<br>
I tried Python 3.7 and 3.8 as well, but the result was the same. Because I am a begginer user for Python, I might make a easy mistake at the first step.<br>
And I am going to use SlicerWMA for white matter analysis.</p>
<p>Any advice would be appreciated.</p>
<p>Fumi</p>

---

## Post #2 by @pieper (2023-03-09 15:06 UTC)

<p>I don’t know for sure, but I suspect this has <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md#3-prepare-terminal-environment-to-run-related-commands">never been used on windows</a>.  I know the original developers used macs and linux, so I’d suggest using one of those platforms.  Installing <a href="https://learn.microsoft.com/en-us/windows/wsl/install">WSL</a> is probably easiest.  Alternatively you might be able to use the <a href="https://github.com/SlicerDMRI/SlicerWMA">SlicerWMA extension</a> to install the needed python packages and then use Slicer’s python.  If you get one of those paths working please post back for the benefit of future users who may have the same question.</p>

---

## Post #3 by @Fumi (2023-03-15 03:51 UTC)

<p>Thank you for replying, Steve. I tried WNAinstalling again in my Linux PC, then succeeded!!</p>

---
