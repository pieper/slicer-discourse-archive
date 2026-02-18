# Unable to access/import slicer's cli module from python script

**Topic ID**: 1845
**Date**: 2018-01-15
**URL**: https://discourse.slicer.org/t/unable-to-access-import-slicers-cli-module-from-python-script/1845

---

## Post #1 by @Milogav (2018-01-15 14:05 UTC)

<p>Operating system: Ubuntu 16.04.3 LTS<br>
Slicer version: 4.8.1</p>
<p>Hi everyone!</p>
<p>I’m trying to create a scripted python module and I need to perform bias correction over an MRI volume as the first step in the processing pipeline. For this purpose, I intended to call the n4itkbiascorrection CLI module from within the python script. After looking the tutorials in the slicer web page, I understand I should be using ‘slicer.module’ to import the n4itkbiasfieldcorrection module.</p>
<p>I am able to do so from the Python Interactor console via the following code line:</p>
<p><em>from slicer.modules import n4itkbiasfieldcorrection</em></p>
<p>However, when using the same code line in the script, the module won’t load and Slicer throws the following error in the python console:</p>
<p><em>Traceback (most recent call last):</em><br>
_  File “”, line 1, in _<br>
_  File “/home/miguel/Documentos/Extensiones_3DSlicer/SPAL/SPAL/SPAL.py”, line 12, in _<br>
_    from slicer.modules import n4itkbiasfieldcorrection_<br>
<em>ImportError: cannot import name n4itkbiasfieldcorrection</em></p>
<p>I tried checking the importable modules via the command:</p>
<p><em>print(dir(slicer.modules))</em></p>
<p>When I call this line from the console, the n4itkbiasfieldcorrection module appears in the list printed but it does not appear (along with other many modules) when calling the line from the script.</p>
<p>I am quite new in developing slicer extensions so I am probably missing something here. Any clues on solving this issue??</p>
<p>Thanks in advance for the help!</p>
<p>Miguel</p>

---

## Post #2 by @lassoan (2018-01-15 14:32 UTC)

<p>There is no need to import the module (in addition to the imports that are in the default module template). See description how to run a CLI module from Python in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">developer documentation</a> and here is an example in a module:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Tables/Testing/Python/TablesSelfTest.py#L246-L253" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Tables/Testing/Python/TablesSelfTest.py#L246-L253" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Loadable/Tables/Testing/Python/TablesSelfTest.py#L246-L253</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="246" style="counter-reset: li-counter 245 ;">
<li>parameters = {}</li>
<li>parameters["arg0"] = self.createDummyVolume().GetID()</li>
<li>parameters["arg1"] = self.createDummyVolume().GetID()</li>
<li>parameters["transform1"] = self.createDummyTransform().GetID()</li>
<li>parameters["transform2"] = self.createDummyTransform().GetID()</li>
<li>parameters["inputDT"] = inputTableNode.GetID()</li>
<li>parameters["outputDT"] = outputTableNode.GetID()</li>
<li>slicer.cli.run(slicer.modules.executionmodeltour, None, parameters, wait_for_completion=True)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Milogav (2018-01-15 15:13 UTC)

<p>You are right, don’t know why I assumed I had to import the module. I should have paid more attention to the docs. As you state, if the module is called directly without any importing, it seems to work perfectly.</p>
<p>Anyway, thanks for your quick response!</p>

---

## Post #4 by @Saima (2021-08-25 23:11 UTC)

<p>Hi Andras,<br>
Can I get the link to function that gives parameter information for a cli module?</p>
<p>For your own created python scripted modules if you want to access the parameters how can we access them. Also if there are two apply buttons can these be run from a single module.</p>
<p>for example please see screnn shot for the scripted loadable python module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43f408b3c769c70e5e7a5fb7dc4efd49cebd120d.png" data-download-href="/uploads/short-url/9H8Pw859Gpg2DcJuOV6raEzNcpD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43f408b3c769c70e5e7a5fb7dc4efd49cebd120d.png" alt="image" data-base62-sha1="9H8Pw859Gpg2DcJuOV6raEzNcpD" width="515" height="500" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">522×506 30.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regards,<br>
Saima Safdar</p>

---
