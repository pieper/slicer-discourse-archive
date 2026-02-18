# How can I write a python CLI code using slicer internal module

**Topic ID**: 18023
**Date**: 2021-06-08
**URL**: https://discourse.slicer.org/t/how-can-i-write-a-python-cli-code-using-slicer-internal-module/18023

---

## Post #1 by @bywbilly (2021-06-08 20:10 UTC)

<p>Hi,</p>
<p>I am new to slice and working on incorporating our own 3D segmentation model with slicer. And we would like to assume the slicer user does not know anything about code, so intend to write a python CLI code to do everything. I am wondering is it possible? If not, can you provide me some lights that what should I do?</p>
<ol>
<li>
<p>The user specifies the input volume path, output volume path, and some other parameters, then our python code computes the segmentation. This can be done as shown here: <a href="https://github.com/lassoan/SlicerPythonCLIExample/blob/master/BlurImage/BlurImage.py" class="inline-onebox" rel="noopener nofollow ugc">SlicerPythonCLIExample/BlurImage.py at master · lassoan/SlicerPythonCLIExample · GitHub</a></p>
</li>
<li>
<p>But I would like to use this external python code (note not the interpreter provided in slicer) to render /plot/show the segmentation mask in slicer, is it possible? I know how to do this with the interpreter provided in slicer but not sure whether I can do this with totally external python code?</p>
</li>
</ol>
<p>Thanks!</p>

---

## Post #2 by @bywbilly (2021-06-08 23:29 UTC)

<p>I don’t know how to edit the original post so I reply here.</p>
<p>After more search, I think CLI is designed to not interact with slicer core. I find an alternative way to do it.<br>
I only want the computed label map to be received by Slicer, currently, I did this by return the label map as a grayscale volume and convert it manually through the volume module. Is there a way to explicitly denote the returned object as a label map in Slicer Execution Model?</p>
<p>Thanks!</p>

---

## Post #3 by @lassoan (2021-06-09 04:56 UTC)

<p>CLI modules are Python scripts or command-line applications that do not rely on Slicer. They can be executed within Slicer’s environment or without Slicer. What Slicer offers is displaying automatically-generated GUI, writing all inputs to file, executing the application, continuous progress reporting, and in the end reading back all outputs into the scene.</p>
<p>The automatically generated GUI is typically convenient enough for development, testing, and research/engineering use. For clinical use, often a Python scripted loadable module is developed as a front-end, which provides a more sophisticated GUI and calls the CLI module in the background.</p>
<p>To designate an output image as labelmap, specify <code>type="label"</code>, as it is done for example in ModelToLabelMap module:</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/e6971c540b030f7e83f949918a433cf58bee4c3b/Modules/CLI/ModelToLabelMap/ModelToLabelMap.xml#L45" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e6971c540b030f7e83f949918a433cf58bee4c3b/Modules/CLI/ModelToLabelMap/ModelToLabelMap.xml#L45" target="_blank" rel="noopener">Slicer/Slicer/blob/e6971c540b030f7e83f949918a433cf58bee4c3b/Modules/CLI/ModelToLabelMap/ModelToLabelMap.xml#L45</a></h4>



  <pre class="onebox">    <code class="lang-xml">
      <ol class="start lines" start="35" style="counter-reset: li-counter 34 ;">
          <li>      &lt;index&gt;0&lt;/index&gt;</li>
          <li>      &lt;description&gt;&lt;![CDATA[Output volume will have the same origin, spacing, axis directions, and extent as this volume.]]&gt;&lt;/description&gt;</li>
          <li>    &lt;/image&gt;</li>
          <li>    &lt;geometry type="model"&gt;</li>
          <li>      &lt;name&gt;surface&lt;/name&gt;</li>
          <li>      &lt;label&gt;Model&lt;/label&gt;</li>
          <li>      &lt;channel&gt;input&lt;/channel&gt;</li>
          <li>      &lt;index&gt;1&lt;/index&gt;</li>
          <li>      &lt;description&gt;&lt;![CDATA[Input model]]&gt;&lt;/description&gt;</li>
          <li>    &lt;/geometry&gt;</li>
          <li class="selected">    &lt;image type="label" reference="surface"&gt;</li>
          <li>      &lt;name&gt;OutputVolume&lt;/name&gt;</li>
          <li>      &lt;label&gt;Output Volume&lt;/label&gt;</li>
          <li>      &lt;channel&gt;output&lt;/channel&gt;</li>
          <li>      &lt;index&gt;2&lt;/index&gt;</li>
          <li>      &lt;description&gt;&lt;![CDATA[Unsigned char label map volume]]&gt;&lt;/description&gt;</li>
          <li>    &lt;/image&gt;</li>
          <li>  &lt;/parameters&gt;</li>
          <li>&lt;/executable&gt;</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @bywbilly (2021-06-09 16:54 UTC)

<p>Hi Andras, Thanks for pointing out the XML file. It helps a lot!</p>
<p>I have another question, how could I run the CLI algorithm using my own python environments instead of slicer internal python environments?</p>
<p>Thanks!</p>

---

## Post #5 by @bywbilly (2021-06-09 17:10 UTC)

<p>Another possible way is to install the packages I required in slicer internal environment? What is the correct way for doing this? Thanks!</p>

---

## Post #6 by @bywbilly (2021-06-09 17:16 UTC)

<p>BTW, on MAC, I cannot install packages through the python interaction by “pip.main([…])”</p>
<p>AttributeError: ‘PythonQtStdInRedirect’ object has no attribute ‘isatty’ this error occurs and it seems to have something to do with the mac python framework.</p>

---

## Post #7 by @jamesobutler (2021-06-09 18:50 UTC)

<p>When using Slicer 4.11 and newer you can use the following method to install python packages into Slicer’s environment.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package</a></p>

---

## Post #8 by @lassoan (2021-06-09 20:16 UTC)

<aside class="quote no-group" data-username="bywbilly" data-post="6" data-topic="18023" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/7bcc69/48.png" class="avatar"> bywbilly:</div>
<blockquote>
<p>BTW, on MAC, I cannot install packages through the python interaction by “pip.main([…])”</p>
<p>AttributeError: ‘PythonQtStdInRedirect’ object has no attribute ‘isatty’ this error occurs and it seems to have something to do with the mac python framework.</p>
</blockquote>
</aside>
<p>You need to activate Slicer’s Python environment before you can run any Python executables (this is required in any other Python or Conda virtual environments, too). You can activate the Slicer Python environment for an executable by launching it using the <code>PythonSlicer</code> launcher (it sets up the Python enrivonment and starts the executable).</p>
<p>However, most Python executables just call <code>python -m ModuleName ...</code>, so instead of using that executable, it is simply to directly run <code>PythonSlicer -m ModuleName ...</code>. This is what the <code>slicer.util.pip_install</code> convenience function calls internally:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/6666a5b5f2d50080e2c7f8800bfe0fb6beb721fc/Base/Python/slicer/util.py#L2846">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/6666a5b5f2d50080e2c7f8800bfe0fb6beb721fc/Base/Python/slicer/util.py#L2846" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6666a5b5f2d50080e2c7f8800bfe0fb6beb721fc/Base/Python/slicer/util.py#L2846" target="_blank" rel="noopener">Slicer/Slicer/blob/6666a5b5f2d50080e2c7f8800bfe0fb6beb721fc/Base/Python/slicer/util.py#L2846</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="2836" style="counter-reset: li-counter 2835 ;">
          <li>    if not pythonSlicerExecutablePath:</li>
          <li>      raise RuntimeError("PythonSlicer executable not found")</li>
          <li>  except ImportError:</li>
          <li>    # Running from console</li>
          <li>    import os</li>
          <li>    import sys</li>
          <li>    pythonSlicerExecutablePath = os.path.dirname(sys.executable)+"/PythonSlicer"</li>
          <li>    if os.name == 'nt':</li>
          <li>      pythonSlicerExecutablePath += ".exe"</li>
          <li></li>
          <li class="selected">  commandLine = [pythonSlicerExecutablePath, "-m", module, *args]</li>
          <li>  proc = launchConsoleProcess(commandLine, useStartupEnvironment=False)</li>
          <li>  logProcessOutput(proc)</li>
          <li></li>
          <li>def pip_install(requirements):</li>
          <li>  """Install python packages.</li>
          <li></li>
          <li>  Currently, the method simply calls ``python -m pip install`` but in the future further checks, optimizations,</li>
          <li>  user confirmation may be implemented, therefore it is recommended to use this method call instead of a plain</li>
          <li>  pip install.</li>
          <li>  :param requirements: requirement specifier, same format as used by pip (https://docs.python.org/3/installing/index.html)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="bywbilly" data-post="4" data-topic="18023">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/7bcc69/48.png" class="avatar"> bywbilly:</div>
<blockquote>
<p>I have another question, how could I run the CLI algorithm using my own python environments instead of slicer internal python environments?</p>
</blockquote>
</aside>
<p>Installing the required Python packages is easier, because you don’t need to ask your users to set up a new Python environment.</p>

---
