# No module named vtkmodules.vtkCommonCore

**Topic ID**: 21854
**Date**: 2022-02-08
**URL**: https://discourse.slicer.org/t/no-module-named-vtkmodules-vtkcommoncore/21854

---

## Post #1 by @n_h (2022-02-08 16:40 UTC)

<p>Hey,</p>
<p>I have recently got in touch with vmtk but I have still some issues making it work from python scripts. I would like to used it to implement an automatic segmentation and meshing workflow.</p>
<p>I have set up an Ubuntu 20.04 Dockerimage and build vmtk following the instructions on the <code>http://www.vmtk.org/download/</code> page to install the development version.</p>
<p>It is possible to run simple commands from the terminal like “vmtk vmtkimagereader -ifile ct_scan.nii.” If I want to execute the <code>myscript.py</code>example after running chmod u+x myscript.py i get the following traceback:</p>
<pre><code class="lang-auto">File "./myscript.py", line 4, in &lt;module&gt; from vmtk import vmtkscripts       
File "/build/vmtk/vmtk-build/Install/lib/python3.9/site-packages/vmtk/vmtkscripts.py", line 158, in &lt;module&gt;   exec('from '+item+' import *')   
File "&lt;string&gt;", line 1, in &lt;module&gt; File "/build/vmtk/vmtk-build/Install/lib/python3.9/site-packages/vmtk/vmtkactivetubes.py", line 19, in &lt;module&gt; import vtk                                                                                                          File "/build/vmtk/vmtk-build/Install/lib/python3.9/site-packages/vtk.py", line 31, in &lt;module&gt;                          all_m = importlib.import_module('vtkmodules.all')
File "/root/miniconda3/envs/vmtk/lib/python3.6/importlib/__init__.py", line 126, in import_module  
        return _bootstrap._gcd_import(name[level:], package, level)                                                         
File "/build/vmtk/vmtk-build/Install/lib/python3.9/site-packages/vtkmodules/all.py", line 7, in &lt;module&gt;                
from .vtkCommonCore import *      
       ModuleNotFoundError: No module named 'vtkmodules.vtkCommonCore' 
</code></pre>
<p>I would really appreciate some hints on how to get that working.</p>
<p>Thank you very much,<br>
Nils</p>

---

## Post #2 by @ramtingh (2022-02-09 09:36 UTC)

<p>Might be that your script is getting executed by a different python installation? I can’t think of a scenario where the command line pype scripts can find vtk, but the python script version can’t.</p>

---

## Post #3 by @n_h (2022-02-09 10:45 UTC)

<p>Thank you very much for your thoughts and the quick reply.</p>
<p>I had a similar idea earlier and was playing around with different python versions 3.9 or even python2.7 (which should both be supported by vmtk) and got the same error but I think that you are referring to a vmtk python version, right?<br>
Should I set the python version to something like: <code>/build/vmtk/vmtk-build/Install/lib/python3.9/</code> or what are you suggesting?</p>

---

## Post #4 by @ramtingh (2022-02-09 10:54 UTC)

<p>I was wondering if there are multiple python installations (e.g. default system python and one you have installed), because if “vmtk vmtkimagereader -ifile ct_scan.nii.” from the terminal works I would be very confused about it not being able to find vtk. <code>vmtkimagereader</code> definitely needs vtk.</p>
<p>I haven’t exactly tried python 2.7, but I’m pretty sure the current vmtk master branch is not going to be compatible with python 2.7. The instructions at <code>http://www.vmtk.org/download</code> were written about three years ago and aren’t necessarily accurate at this point, although the builds scripts are reasonably up to date.</p>
<p>How exactly are you building vmtk (superbuild?) and which versions of VTK and ITK are you using?</p>

---

## Post #5 by @n_h (2022-02-09 11:13 UTC)

<p>Yes, in fact there are two versions 2.7 and 3.9.5 but the default during build and execution is 3.9 which comes from anaconda and not the system itself as i just figured out.</p>
<p>I am strictly following the build instructions form the download page:</p>
<pre><code class="lang-auto">mkdir vmktk-build 

cd vmktk-build 

cmake .. \

make
</code></pre>
<p>The versions are: itk 5.2 and vtk9.1<br>
Are here any issues that are not obvious to me?<br>
If not I would try to build it again ensuring that I use the system’s python as 3.9.</p>

---

## Post #6 by @ramtingh (2022-02-09 11:17 UTC)

<p>If you’re already using anaconda, you could install it from the conda-forge channel with</p>
<pre><code class="lang-auto">conda config --add channels conda-forge
conda install vmtk 

</code></pre>
<p>Do you actually need it to be built from source?</p>

---

## Post #7 by @n_h (2022-02-09 11:36 UTC)

<p>Yes and no,</p>
<p>I have tried to use an anaconda installation as you suggested above first but the <code>conda install vmtk</code> had some issues when using the python API that are already fixed when building from the current master.</p>
<p>Since I want to embed vmtk in a larger python-workflow in a dockerimage I was hoping to circumvent those issues by building it directly but this turns out to be trickier than expected xD</p>

---

## Post #8 by @ramtingh (2022-02-09 11:43 UTC)

<p>The conda-forge version is up to date with the current master branch. You can try installing specifically the new version with <code>conda install vmtk=1.5</code> .</p>
<p>Otherwise you can have a look at the cmake setup for Slicer’s builds which incorporate vmtk (<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/SuperBuild/External_VMTK.cmake" rel="noopener nofollow ugc">https://github.com/vmtk/SlicerExtension-VMTK/blob/master/SuperBuild/External_VMTK.cmake</a>) or the anaconda packaging builds (<a href="https://github.com/vmtk/vmtk/blob/master/distribution/build.sh" rel="noopener nofollow ugc">https://github.com/vmtk/vmtk/blob/master/distribution/build.sh</a>), presumably something has gone wrong during the cmake configuration</p>

---
