# Setting widget variable from --python-code on Slicer.exe start

**Topic ID**: 23908
**Date**: 2022-06-17
**URL**: https://discourse.slicer.org/t/setting-widget-variable-from-python-code-on-slicer-exe-start/23908

---

## Post #1 by @talmazov (2022-06-17 02:33 UTC)

<p>Hey all,<br>
I am launching 3d slicer via python script using subprocess as such</p>
<blockquote>
<p>Slicer.exe --python-code slicer.util.getModule(‘BlenderMonitor’).widgetRepresentation().self().test = ‘TESTING’</p>
</blockquote>
<p>in the python widget I have</p>
<pre><code class="lang-auto">class BlenderMonitorWidget:
    def __init__(self, parent = None):
        if not parent:
            self.parent = slicer.qMRMLWidget()
            self.parent.setLayout(qt.QVBoxLayout())
            self.parent.setMRMLScene(slicer.mrmlScene)
        else:
            self.parent = parent
        self.layout = self.parent.layout()
        if not parent:
            self.setup()
            self.parent.show()
        self.watching = True #False before but now we are automating things
        self.sock = None
        self.sliceSock = None
        self.host_address = asyncsock.address[0]
        self.host_port = asyncsock.address[1]
        self.SlicerSelectedModelsList = []
        #self.toSync = []
        #slice list
        self.sliceViewCache = {}
        #self.workingVolume = None
        self.test = None
</code></pre>
<p>for some reason when I try to set self.test on launch, once 3d slicer starts I check the variable and it is still None.<br>
how can i set self.test automatically as 3D slicer is loading? I’ve tried it with other variables and it doesn’t seem to work. Thoughts?</p>
<p>Best,<br>
Georgi</p>

---

## Post #2 by @mau_igna_06 (2022-06-17 08:11 UTC)

<p>Hi Georgi</p>
<p>Did you add your module to the additional-paths ?</p>

---

## Post #3 by @talmazov (2022-06-17 12:19 UTC)

<p>here?<br>
I added it before, module loads.<br>
If i do</p>
<pre><code class="lang-auto">slicer.util.getModule(‘BlenderMonitor’).widgetRepresentation().self().test = ‘TESTING’
</code></pre>
<p>in the python CLI console once 3d slicer is launched it works. its only on startup via --python-code</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b1581be23b5ddd1fbb241583ef5d69fa01ae168.png" data-download-href="/uploads/short-url/1A3ktFalAjQxqWqN9naJ2oqSIME.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b1581be23b5ddd1fbb241583ef5d69fa01ae168_2_690x458.png" alt="image" data-base62-sha1="1A3ktFalAjQxqWqN9naJ2oqSIME" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b1581be23b5ddd1fbb241583ef5d69fa01ae168_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b1581be23b5ddd1fbb241583ef5d69fa01ae168.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b1581be23b5ddd1fbb241583ef5d69fa01ae168.png 2x" data-dominant-color="F8F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">961×639 40.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mau_igna_06 (2022-06-17 12:45 UTC)

<p>Try adding it in the same line of code</p>
<p>When you are opening the app I mean</p>

---

## Post #5 by @talmazov (2022-06-17 13:14 UTC)

<p>hey,<br>
apologies but i am not following.<br>
Do you mean adding the module path via code?<br>
I found this but the links are broken: <a href="https://discourse.slicer.org/t/can-i-add-an-additional-module-path-with-python-code/6189" class="inline-onebox">Can I add an "additional module path" with python code</a></p>
<p>~Georgi</p>

---

## Post #6 by @lassoan (2022-06-17 18:20 UTC)

<p>If a command-line argument contains spaces then you must put the argument between quotes (<code>"</code>). If this is cumbersome then you can write your custom startup code into a .py file and run it by using the <code>--python-script</code> argument.</p>
<p>Widget representation of a module may not be created or fully initialized until you actually open the module, so you may want to first call <code>slicer.util.selectedModule('BlenderMonitor')</code> and then get the module widget.</p>

---

## Post #7 by @talmazov (2022-06-17 21:55 UTC)

<p>Hey,<br>
Thank you for the suggestion. Let me provide some more code context.<br>
Below is my test script I launch from Python IDLE</p>
<pre><code class="lang-auto">import subprocess

slicer_startup_parameters = ''.join((
  "slicer.util.selectModule('BlenderMonitor')\n",
  "slicer.util.getModule('BlenderMonitor').widgetRepresentation().self().connect_to_blender(55)"))
subprocess.Popen(["C:\\ProgramData\\NA-MIC\\Slicer 4.11.20210226\\Slicer.exe", "--python-code", slicer_startup_parameters])
</code></pre>
<p>below is part of the code from my 3d slicer widget i am trying to work with.</p>
<pre><code class="lang-auto">class BlenderMonitorWidget:
    def __init__(self, parent = None):
        if not parent:
            self.parent = slicer.qMRMLWidget()
            self.parent.setLayout(qt.QVBoxLayout())
            self.parent.setMRMLScene(slicer.mrmlScene)
        else:
            self.parent = parent
        self.layout = self.parent.layout()
        if not parent:
            self.setup()
            self.parent.show()
        self.host_address = asyncsock.address[0]
        self.host_port = 5959

    def setup(self):
        # Instantiate and connect widgets ...
        
    def connect_to_blender(self, port):
        self.host_port = port
        print(self.host_port)
</code></pre>
<p>I created a separate function <code>connect_to_blender(self,port)</code> that takes int port value when 3D slicer is launched with <code>--python-code</code></p>
<p>the first paramater, <code>selectModule</code>, works well and slicer switches to the widget on startup. when <code>connect_to_blender</code> is called after, i do not see the print statement in the console when slicer is finished startup and <code>--python-code</code> has been fully executed<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d26710a6896361d89409d8a50d1512b054639e18.png" alt="image" data-base62-sha1="u1j5fiSCf46t0Q0T7DX4j16IFMQ" width="571" height="259"></p>
<p>and when I try to access <code>host_port</code> via the console, the value of the variable has not changed. in <code>--python-code</code> i pass int 55, the hard-coded value is 5959<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b06728acc6a7f628e4f0d5c9023baad9eeec0ac0.png" alt="image" data-base62-sha1="pax3cI3Qmrfwt67pwAhsoun3eAU" width="571" height="271"></p>

---

## Post #8 by @lassoan (2022-06-18 13:12 UTC)

<p>I’m not sure if newline character is acceptable in command-line arguments. If you need to run multiple commands, pass multiple arguments, etc. then it is safer to use <code>--python-script</code> argument, see a complete example here: <a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" class="inline-onebox">SlicerRT/BatchProcessing at master · SlicerRt/SlicerRT · GitHub</a></p>

---

## Post #9 by @talmazov (2022-06-18 14:03 UTC)

<p>hey,<br>
multiline arguments work with --python-code<br>
The code below, for example, works just fine for me using \t and \n</p>
<blockquote>
<pre><code>            slicer_startup_parameters = ''.join((
                "dicomDataDir = '%s'\n"%os.path.dirname(context.scene.DICOM_dir).replace(os.sep, '/'),
                "loadedNodeIDs = []\n",
                "from DICOMLib import DICOMUtils\n",
                "with DICOMUtils.TemporaryDICOMDatabase() as db:\n",
                "\tDICOMUtils.importDicom(dicomDataDir, db)\n",
                "\tpatientUIDs = db.patients()\n",
                "\tfor patientUID in patientUIDs:\n",
                "\t\tloadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))\n",
                "slicer.util.selectModule('BlenderMonitor')\n",
                "slicer.util.setSliceViewerLayers(background=slicer.util.getNode(loadedNodeIDs[0]))\n",
                "slicer.util.getModule('BlenderMonitor').widgetRepresentation().self().workingVolume = slicer.util.getNode(loadedNodeIDs[0])"
            ))
</code></pre>
</blockquote>
<p>its just that you cannot set variables on startup. I have some ideas how to work around that via configuration file. I just wanted to check if there was a solution to this as it is easier to pass data directly</p>
<p>best,<br>
Georgi</p>

---

## Post #10 by @lassoan (2022-06-18 14:26 UTC)

<p>Could you provide a complete, minimal example that reproduces the problem? (your <code>BlenderMonitorWidget</code> example was not a complete script file that I could use for testing)</p>
<p>Passing of parameters via <code>--python-code</code> works welll for example in SlicerJupyter:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerJupyter/blob/master/JupyterKernel/Resources/kernel-template.json.in">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerJupyter/blob/master/JupyterKernel/Resources/kernel-template.json.in" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/master/JupyterKernel/Resources/kernel-template.json.in" target="_blank" rel="noopener">Slicer/SlicerJupyter/blob/master/JupyterKernel/Resources/kernel-template.json.in</a></h4>


      <pre><code class="lang-in">{
    "display_name": "{slicer_application_name} {slicer_version_major}.{slicer_version_minor}",
    "language" : "python",
    "argv": [
        "{slicer_launcher_executable}",
        "--no-splash",
        "--python-code",
        "connection_file=r'{connection_file}';print('JupyterConnectionFile:['+connection_file+']');slicer.modules.jupyterkernel.startKernel(connection_file);slicer.util.mainWindow().showMinimized()"
    ]
}
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @talmazov (2022-06-19 16:09 UTC)

<p>Hey,<br>
I have provided working examples that you should be able to use to reproduce the problem.<br>
I am just trying to set the variable self.host_port on start-up via —python-code</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/talmazov/b294c11c0a6a25fe3c8889cc57419b3a">
  <header class="source">

      <a href="https://gist.github.com/talmazov/b294c11c0a6a25fe3c8889cc57419b3a" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/talmazov/b294c11c0a6a25fe3c8889cc57419b3a" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/talmazov/b294c11c0a6a25fe3c8889cc57419b3a</a></h4>

  <h5>BlenderTest.py</h5>
  <pre><code class="Python">"""
@author: Patrick R. Moore, Georgi Talmazov

"""

from __main__ import vtk, qt, ctk, slicer

class BlenderTest:
    def __init__(self, parent):
        parent.title = "blender_test"</code></pre>
    This file has been truncated. <a href="https://gist.github.com/talmazov/b294c11c0a6a25fe3c8889cc57419b3a" target="_blank" rel="noopener nofollow ugc">show original</a>
  <h5>start_slicer.py</h5>
  <pre><code class="Python">import subprocess

slicer_startup_parameters = ''.join(("slicer.util.selectModule('BlenderTest')\n",
                                     "slicer.util.getModule('BlenderTest').widgetRepresentation().self().connect_to_blender(55)"))

subprocess.Popen(["C:\\ProgramData\\NA-MIC\\Slicer 5.0.2\\Slicer.exe", "--python-code", slicer_startup_parameters])</code></pre>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>BlenderTest.py is the add-on module, please add via additional modules path</p>
<p>start_slicer.py is the startup code. Please set your 3D slicer install directory.</p>
<p>Keep me posted.</p>
<p>Best,<br>
Georgi</p>

---

## Post #12 by @lassoan (2022-06-20 01:24 UTC)

<p>Maybe newline character can be passed through inside command-line arguments in certain situations, but I would not even attempt that. Especially because it is not necessary. You can separate commands by semicolon instead. For example, this works well for me:</p>
<pre><code class="lang-auto">import subprocess

slicer_startup_parameters = """print('Connecting to Blender...')
slicer.util.selectModule('BlenderTest')
slicer.util.getModuleWidget('BlenderTest').connect_to_blender(55)
""".replace('\n', ';')

subprocess.Popen([r"c:\Users\andra\AppData\Local\NA-MIC\Slicer 5.0.2\Slicer.exe", "--python-code", slicer_startup_parameters])
</code></pre>
<p>Note that on Windows, the Slicer installer registers <code>Slicer.exe</code> with the last installed instance, so you can start the application without knowing the full path, like this:</p>
<pre><code class="lang-auto">subprocess.Popen(["Slicer.exe", "--python-code", slicer_startup_parameters])
</code></pre>

---

## Post #13 by @talmazov (2022-06-28 16:50 UTC)

<p>Hey,<br>
Apologies it took me a while to respond, thank you so much for your help.<br>
For future reference to those who stumble on this post I would like to elaborate on the solution.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> thank you for the suggestion of improving on the string formatting. Use of</p>
<blockquote>
<p>“\n” and “\t”</p>
</blockquote>
<p>within the string was not a problem. Although for future reference it is good to know that I can separate commands inline with semicolon “;”<br>
The real problem was that I was trying to set</p>
<blockquote>
<p>self.host_port</p>
</blockquote>
<p>by accessing</p>
<blockquote>
<p>slicer.util.getModule(‘BlenderMonitor’).widgetRepresentation().self().[widget init var]</p>
</blockquote>
<p>Reviewing <a class="mention" href="/u/lassoan">@lassoan</a> suggestion, widget class functions are more appropriately accessed by the</p>
<blockquote>
<p>slicer.util.getModuleWidget().[widget class method] ()</p>
</blockquote>
<p>method. When I switched to getModuleWidget() and wrapped self.host_port variable in the self.connect_to_blender() method I was able to pass and set self.host_port on widget startup.</p>
<p>TL;DR <a class="mention" href="/u/lassoan">@lassoan</a> code suggestions worked well, use of semicolon was not necessary and use of \n and \t in string formatting is acceptable when --python-code</p>

---
