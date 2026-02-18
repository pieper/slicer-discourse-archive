# mCT fossil tooth segmentation

**Topic ID**: 44992
**Date**: 2025-11-07
**URL**: https://discourse.slicer.org/t/mct-fossil-tooth-segmentation/44992

---

## Post #1 by @ThomasVanParys (2025-11-07 17:38 UTC)

<p>Hello:</p>
<p>I am asking for advice about the best way to segment a tooth from a fossil mandibular fragment. This is from a mCT scan of 1,554 slices. I want to segment enamel, dentine, pulp, and roots etc… but densities are extremely similar!</p>
<p>Thank you!</p>
<p>Tom</p>

---

## Post #2 by @muratmaga (2025-11-07 18:20 UTC)

<p>There is really no magical formulas to separate enamal, dentine pulp and roots if the intensities are very similar. Normally enamel should be easy, but you said this is a fossil so diagenesis would change that. You can try the NNInteractive, AI-based interactive segmentation, but you will probably first reduce the resolution of your dataset (probably by factor of 2).</p>

---

## Post #3 by @ThomasVanParys (2025-11-10 13:10 UTC)

<p>Thank you. I am running on a Windows device with NVIDIA GPU, Quadro RTX 4000.</p>
<p>The setup instructions don’t seem to be working in Windows PowerShell:</p>
<pre><code class="lang-auto">PS C:\Users\Imaging Lab&gt; cd /d %localappdata%
Set-Location : A positional parameter cannot be found that accepts argument '%localappdata%'.
At line:1 char:1
+ cd /d %localappdata%
+ ~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-Location], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

PS C:\Users\Imaging Lab&gt; mkdir nninteractive-server
mkdir : An item with the specified name C:\Users\Imaging Lab\nninteractive-server already exists.
At line:1 char:1
+ mkdir nninteractive-server
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceExists: (C:\Users\Imagin...eractive-server:String) [New-Item], IOException
    + FullyQualifiedErrorId : DirectoryExist,Microsoft.PowerShell.Commands.NewItemCommand

PS C:\Users\Imaging Lab&gt; cd nninteractive-server
PS C:\Users\Imaging Lab\nninteractive-server&gt; pixi init .
Error:   x pixi.toml already exists

PS C:\Users\Imaging Lab\nninteractive-server&gt; pixi add python=3.12 pip
Added python=3.12
Added pip &gt;=25.2,&lt;26
PS C:\Users\Imaging Lab\nninteractive-server&gt; cd .pixi\envs\default\Scripts
PS C:\Users\Imaging Lab\nninteractive-server\.pixi\envs\default\Scripts&gt; pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 : The term 'pip3' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ pip3 install torch torchvision torchaudio --index-url https://downloa ...
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (pip3:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command pip3 was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\pip3". See "get-help about_Command_Precedence" for more details.
PS C:\Users\Imaging Lab\nninteractive-server\.pixi\envs\default\Scripts&gt; cd /d %localappdata%\nninteractive-server\.pixi\envs\default\Scripts
Set-Location : A positional parameter cannot be found that accepts argument
'%localappdata%\nninteractive-server\.pixi\envs\default\Scripts'.
At line:1 char:1
+ cd /d %localappdata%\nninteractive-server\.pixi\envs\default\Scripts
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-Location], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

PS C:\Users\Imaging Lab\nninteractive-server\.pixi\envs\default\Scripts&gt; pip install nninteractive-slicer-server
pip : The term 'pip' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ pip install nninteractive-slicer-server
+ ~~~
    + CategoryInfo          : ObjectNotFound: (pip:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command pip was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\pip". See "get-help about_Command_Precedence" for more details.
PS C:\Users\Imaging Lab\nninteractive-server\.pixi\envs\default\Scripts&gt; nninteractive-slicer-server --host 0.0.0.0 --port 1527
nninteractive-slicer-server : The term 'nninteractive-slicer-server' is not recognized as the name of a cmdlet,
function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the
path is correct and try again.
At line:1 char:1
+ nninteractive-slicer-server --host 0.0.0.0 --port 1527
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (nninteractive-slicer-server:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command nninteractive-slicer-server was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\nninteractive-slicer-server". See "get-help about_Command_Precedence" for more details.
PS C:\Users\Imaging Lab\nninteractive-server\.pixi\envs\default\Scripts&gt;
</code></pre>

---

## Post #4 by @muratmaga (2025-11-10 15:25 UTC)

<p>You need to execute these instructions in the Terminal (command) window, not in PowerShell;</p>

---

## Post #5 by @ThomasVanParys (2025-11-10 16:38 UTC)

<p>Thank you. This has worked until the last moment:</p>
<pre><code class="lang-auto">RuntimeError: Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False. If you are running on a CPU-only machine, please use torch.load with map_location=torch.device('cpu') to map your storages to the CPU.

C:\Users\Imaging Lab\AppData\Local\nninteractive-server\.pixi\envs\default\Scripts&gt;
</code></pre>
<p>Does this mean my installed model checkpoint was trained for GPU (CUDA), but my current PyTorch install is CPU-only?</p>
<p>EDIT: I have forced a CUDA version in Terminal which now seems to have linked the server with the Slicer plug-in. Thank you!</p>

---

## Post #6 by @muratmaga (2025-11-10 17:31 UTC)

<p>Yes, somehow it is not finding CUDA. Did you install cuda?</p>

---

## Post #7 by @ThomasVanParys (2025-11-11 09:42 UTC)

<p>Yes, it has now worked in the Terminal and linked to the Slicer URL:</p>
<pre><code class="lang-auto">C:\Users\Imaging Lab\AppData\Local\nninteractive-server\.pixi\envs\default\Scripts&gt;python -m pip install torch torchvision torchaudio --index-url 

C:\Users\Imaging Lab\AppData\Local\nninteractive-server\.pixi\envs\default\Scripts&gt;python -c "import torch; print(torch.__version__); print(torch.version.cuda); print('CUDA available:', torch.cuda.is_available())"
2.9.0+cu126
12.6
CUDA available: True
</code></pre>
<p>One further issue, however, is the file size. I have cropped the volume to just one tooth on the mandible, I did not apply ResampleScalarVolume, as I was hesitant to reduce resolution too much. NNInteractive has failed at some stage:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f2926d1c815318650a458a2eace071fc1934239.jpeg" data-download-href="/uploads/short-url/kqsrByhvmpkFIDEuq1kl6AL6siJ.jpeg?dl=1" title="Screenshot 2025-11-11 094038" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f2926d1c815318650a458a2eace071fc1934239_2_690x375.jpeg" alt="Screenshot 2025-11-11 094038" data-base62-sha1="kqsrByhvmpkFIDEuq1kl6AL6siJ" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f2926d1c815318650a458a2eace071fc1934239_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f2926d1c815318650a458a2eace071fc1934239_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f2926d1c815318650a458a2eace071fc1934239_2_1380x750.jpeg 2x" data-dominant-color="AEAEBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-11-11 094038</span><span class="informations">1920×1044 316 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Error:</p>
<pre><code class="lang-auto">[VTK] There is more than one file, use the vtkITKArchetypeImageSeriesReader instead
[Qt] ctkRangeWidget::setSingleStep( 100 ) is outside valid bounds
[Python] Segmentation failed.
[Python] Something has gone wrong with your request (Status code 500).
[VTK] vtkMRMLMarkupsNode::GetNthControlPointPositionStatus failed: control point 1 does not exist
Traceback (most recent call last):
  File "C:/Users/Imaging Lab/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/NNInteractive/lib/Slicer-5.8/qt-scripted-modules/SlicerNNInteractive.py", line 642, in on_point_placed
    self.point_prompt(xyz=xyz, positive_click=self.is_positive)
  File "C:/Users/Imaging Lab/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/NNInteractive/lib/Slicer-5.8/qt-scripted-modules/SlicerNNInteractive.py", line 69, in inner
    return func(self, *args, **kwargs)
  File "C:/Users/Imaging Lab/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/NNInteractive/lib/Slicer-5.8/qt-scripted-modules/SlicerNNInteractive.py", line 651, in point_prompt
    seg_response = self.request_to_server(
  File "C:/Users/Imaging Lab/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/NNInteractive/lib/Slicer-5.8/qt-scripted-modules/SlicerNNInteractive.py", line 1144, in request_to_server
    raise RuntimeError(f"Something has gone wrong with your request (Status code {status_code}).")
RuntimeError: Something has gone wrong with your request (Status code 500).
[Python] Segmentation failed.
[Python] Something has gone wrong with your request (Status code 500).
[VTK] Warning: In vtkSlicerCLIModuleLogic.cxx, line 2377
[VTK] vtkSlicerCLIModuleLogic (000001ECA648A420): Unable to delete temporary file C:/Users/Imaging Lab/AppData/Local/Temp/Slicer/BCJAAE_vtkMRMLScalarVolumeNodeD.nrrd
[Python] Segmentation failed.
[Python] Something has gone wrong with your request (Status code 500).
</code></pre>
<p>Thank you for the help!</p>

---

## Post #8 by @ThomasVanParys (2025-11-11 12:25 UTC)

<p>UPDATE: I have re-activated the server and URL and this has now worked, with some post-processing model cleaning. Unfortunately, as you mentioned, enamel and dentine densitites are too similar, but it has segmented from matrix rather well.<br>
Best,<br>
Tom</p>

---
