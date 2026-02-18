# Conflict vmtk with OpenGL/Mesa in NVIDIA graphics card

**Topic ID**: 8765
**Date**: 2019-10-13
**URL**: https://discourse.slicer.org/t/conflict-vmtk-with-opengl-mesa-in-nvidia-graphics-card/8765

---

## Post #1 by @shahrokh (2019-10-13 07:38 UTC)

<p><strong>Hi Dears 3DSlicer and VMTK Developers and Users</strong></p>
<p>At first I must mention that I stated my problem at <a href="https://groups.google.com/forum/#!forum/vmtk-users" rel="nofollow noopener">vmtk-mailing-list</a> unfortunately I do not get any guidance; Maybe I’m in a hurry. <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"><br>
Anyway I state my problem. I hope that you guide me.</p>
<p>I installed vmtk using Anaconda with the following commands:</p>
<pre><code>sn@sn-P41T-D3P:~$ python --version
Python 2.7.17rc1
sn@sn-P41T-D3P:~$
sn@sn-P41T-D3P:~$ conda install anaconda-client
...
sn@sn-P41T-D3P:~$ conda update conda anaconda-client
...
sn@sn-P41T-D3P:~$ conda config --set restore_free_channel true
...
sn@sn-P41T-D3P:~$ conda create -n myVMTK -c vmtk python=3.6 itk vtk vmtk
...
sn@sn-P41T-D3P:~$ conda activate myVMTK
(myVMTK) sn@sn-P41T-D3P:~$ python --version
Python 3.6.1 :: Continuum Analytics, Inc.
(myVMTK) sn@sn-P41T-D3P:~$
</code></pre>
<p>After doing it, I want to view Aorta_voi.mha file in vmtk-tutorials with the following command:</p>
<pre><code>(myVMTK) sn@sn-P41T-D3P:~$ cd vmtk-tutorials/
(myVMTK) sn@sn-P41T-D3P:~/vmtk-tutorials$ vmtkimagereader -ifile Aorta_voi.mha --pipe vmtkimageviewer
Automatic piping vmtkimagereader
Parsing options vmtkimagereader
    InputFileName = Aorta_voi.mha
Explicit piping vmtkimagereader
Input vmtkimagereader members:
    Id = 0
    Disabled = 0
    Format =
    GuessFormat = 1
    UseITKIO = 1
    Image = 0
    InputFileName = Aorta_voi.mha
    InputFilePrefix =
    InputFilePattern =
    DataExtent = [-1, -1, -1, -1, -1, -1]
    HeaderSize = 0
    DataSpacing = [1.0, 1.0, 1.0]
    DataOrigin = [0.0, 0.0, 0.0]
    DesiredOrientation = native
    DataByteOrder = littleendian
    DataScalarType = float
    FileDimensionality = 3
    Flip = [0, 0, 0]
    AutoOrientDICOMImage = 1
    ImageOutputFileName =
Executing vmtkimagereader ...
Spacing 0.878906 0.878906 1.500090
Origin 156.445000 24.609400 0.000000
Dimensions 157 393 34
Done executing vmtkimagereader.
Output vmtkimagereader members:
    Id = 0
    Image = vtkImageData
    RasToIjkMatrixCoefficients = [1.137778101412438, -0.0, 0.0, -177.99969507546882, -0.0, 1.137778101412438, -0.0, -28.000036408899245, 0.0, -0.0, 0.6666266690665227, -0.0, -0.0, 0.0, -0.0, 1.0]
    XyzToRasMatrixCoefficients = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]

Automatic piping vmtkimageviewer
    Image = vmtkimagereader-0.Image
Parsing options vmtkimageviewer
Explicit piping vmtkimageviewer
Input vmtkimageviewer members:
    Id = 0
    Disabled = 0
    Image = vtkImageData
    ImageInputFileName =
    ArrayName =
    vmtkRenderer = None
    WindowLevel = [0.0, 0.0]
    Display = 1
    Margins = 0
    TextureInterpolation = 1
    ContinuousCursor = 0
    ImageOutputFileName =
Executing vmtkimageviewer ...
ERROR: In ../Rendering/OpenGL2/vtkOpenGLRenderWindow.cxx, line 797
vtkOSOpenGLRenderWindow (0x2138a60): GL version 2.1 with the gpu_shader4 extension is not supported by your graphics driver but is required for the new OpenGL rendering backend. Please update your OpenGL driver. If you are using Mesa please make sure you have version 10.6.5 or later and make sure your driver in Mesa supports OpenGL 3.2.

(myVMTK) sn@sn-P41T-D3P:~/vmtk-tutorials$
</code></pre>
<p>As mentioned above, I get error message about OpenGL and Mesa.</p>
<p>I must mentioned that I have Ubuntu 19.4 (Ubuntu Eoan Ermine).</p>
<pre><code>sn@sn-P41T-D3P:~$ uname --all
Linux sn-P41T-D3P 5.3.0-18-generic #19-Ubuntu SMP Tue Oct 8 20:14:06 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
sn@sn-P41T-D3P:~$
</code></pre>
<p>As mentioned in the following web page, I think that it is occurred due to “Conflict MESA with NVIDIA card”.<br>
Title: How to: Mesa on ubuntu 19.04 - Ask Ubuntu<br>
Address: <a href="https://askubuntu.com/questions/1135653/how-to-mesa-on-ubuntu-19-04" rel="nofollow noopener">https://askubuntu.com/questions/1135653/how-to-mesa-on-ubuntu-19-04</a></p>
<p>As mentioned in this site that:<br>
<strong>"Proprietary graphics drivers (e.g. Nvidia GeForce driver and Catalyst) replace all of Mesa, providing their own implementation of a graphics API."</strong></p>
<p>Then I switch from nvidia to Nouveau as mentioned in the following web page:<br>
Address: How to switch from nvidia to nouveau drivers on ubuntu 18.04 - Ask Ubuntu<br>
Title: <a href="https://askubuntu.com/questions/1032357/how-to-switch-from-nvidia-to-nouveau-drivers-on-ubuntu-18-04" rel="nofollow noopener">https://askubuntu.com/questions/1032357/how-to-switch-from-nvidia-to-nouveau-drivers-on-ubuntu-18-04</a></p>
<p><strong>Befor doing it:</strong></p>
<pre><code>(base) sn@sn-P41T-D3P: ~$ glxinfo | grep "OpenGL version"
OpenGL version string: 3.3.0 NVIDIA 340.107
(base) sn@sn-P41T-D3P: ~$
</code></pre>
<p><strong>After doing it (switching):</strong></p>
<pre><code>(base) sn@sn-P41T-D3P: ~$ glxinfo | grep "OpenGL version"
OpenGL version string: 3.3 (Compatibility Profile) Mesa 19.2.1
(base) sn@sn-P41T-D3P:~$
</code></pre>
<p>However, this error still exists and I get same error.<br>
Please guide me.<br>
Thank a lot.<br>
Shahrokh.</p>

---

## Post #2 by @lassoan (2019-10-13 11:06 UTC)

<p>Does Slicer run correctly on this computer? You can then install VMTK by installing SlicerVMTK extension and do all necessary visualization in Slicer.</p>

---

## Post #3 by @shahrokh (2019-10-13 12:07 UTC)

<p>Thanks a lot for your guidance. Yes I can run 3dslicer without problem but I want to use vmtk commands in the terminal, then I must install vmtk.</p>
<p>I think that my problem is occurred by the version of Anaconda. I installed Anaconda 2019.07  with Python 3.7.</p>
<p>Do you also confirm that this prevents vmtk installation?</p>

---

## Post #4 by @lassoan (2019-10-13 13:49 UTC)

<p>You can use vmtk Python classes from <code>PythonSlicer</code> Python console or Slicer’s built-in Python console. I cannot help with Anaconda build system issues.</p>

---
