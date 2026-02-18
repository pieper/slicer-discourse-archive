# Install python library with extension

**Topic ID**: 10110
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/install-python-library-with-extension/10110

---

## Post #1 by @PaoloZaffino (2020-02-04 17:55 UTC)

<p>Hi all,<br>
the extension I’m developing needs an external python library.<br>
I can install it by using pip_install in the python shell but, of course I need to embed this into the installation process.<br>
How can I do this?<br>
Thanks a lot.</p>
<p>Paolo</p>

---

## Post #2 by @markasselin (2020-02-04 18:41 UTC)

<p>Hi Paolo,</p>
<p>You can use the following structure to do this right in the module. The first time the module is loaded the library will be automatically installed, and every successive time the import in the try block will succeed and the catch will not be executed.</p>
<pre><code>try:
    import library_name
except:
    slicer.util.pip_install('library_name')
    import library_name
</code></pre>
<p>Of course you can use other forms of the Python import lines as well, like<br>
<code>from library_name import module_name</code></p>

---

## Post #3 by @PaoloZaffino (2020-02-04 18:44 UTC)

<p>Thanks <a class="mention" href="/u/markasselin">@markasselin</a>!<br>
Yes, this is a possible solution, but I was looking for a way to do this in the <em>real</em> installation step (maybe you install the extension and the first time you run the extension you have no internet access).</p>
<p>Thanks again</p>

---

## Post #4 by @pieper (2020-02-04 19:11 UTC)

<p>Hi Paulo -</p>
<p>Since the user needs internet to download the extension you are probably safe with the approach Mark suggested.  If you want to be one step safer, you could include that code in a method called by when the <code>startupCompleted</code> signal is triggered.  If you set this up in the module class it will be triggered every time Slicer starts up with your extension installed.  Since they need to restart after installing the extension it’s pretty likely to happen while they are on the internet.</p>
<p>Something like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/6302522681e6a0bdcdb9f112634f94f3eb4f0097/Modules/Scripted/SampleData/SampleData.py#L87-L109" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6302522681e6a0bdcdb9f112634f94f3eb4f0097/Modules/Scripted/SampleData/SampleData.py#L87-L109" target="_blank">Slicer/Slicer/blob/6302522681e6a0bdcdb9f112634f94f3eb4f0097/Modules/Scripted/SampleData/SampleData.py#L87-L109</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="87" style="counter-reset: li-counter 86 ;">
<li>  # Trigger the menu to be added when application has started up</li>
<li>  if not slicer.app.commandOptions().noMainWindow :</li>
<li>    slicer.app.connect("startupCompleted()", self.addMenu)</li>
<li>
</li>
<li>  # allow other modules to register sample data sources by appending</li>
<li>  # instances or subclasses SampleDataSource objects on this list</li>
<li>  try:</li>
<li>    slicer.modules.sampleDataSources</li>
<li>  except AttributeError:</li>
<li>    slicer.modules.sampleDataSources = {}</li>
<li>
</li>
<li>
</li>
<li>def addMenu(self):</li>
<li>  actionIcon = self.parent.icon</li>
<li>  a = qt.QAction(actionIcon, 'Download Sample Data', slicer.util.mainWindow())</li>
<li>  a.setToolTip('Go to the SampleData module to download data from the network')</li>
<li>  a.connect('triggered()', self.select)</li>
<li>
</li>
<li>  fileMenu = slicer.util.lookupTopLevelWidget('FileMenu')</li>
<li>  if fileMenu:</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/6302522681e6a0bdcdb9f112634f94f3eb4f0097/Modules/Scripted/SampleData/SampleData.py#L87-L109" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2020-02-04 19:40 UTC)

<p>The installation steps that <a class="mention" href="/u/markasselin">@markasselin</a> and <a class="mention" href="/u/pieper">@pieper</a> described are correct.</p>
<p>You cannot install required Python packages during extension installation time, because extensions are shared between all Slicer instances of a specific version, while extension packages are not shared (but installed separately for each Slicer instance).</p>

---

## Post #6 by @adamrankin (2020-02-04 21:08 UTC)

<p>Tagging for when I forget how to do this.</p>

---

## Post #7 by @PaoloZaffino (2020-02-05 00:05 UTC)

<p>Thanks a lot!<br>
I used the strategy proposed by <a class="mention" href="/u/markasselin">@markasselin</a>, it is much more confortable!</p>
<p>Thanks again!<br>
Paolo</p>

---

## Post #8 by @Davide_Punzo (2020-02-05 08:59 UTC)

<p>Ciao <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a>, if your extension is in the extension manager, you can actually do it directly in the cmake (so they will be packed at compilation time on the kitware factory machines):</p>
<ol>
<li>
<p>add  python requirements in the superbuild:<br>
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild.cmake#L28" rel="nofollow noopener">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild.cmake#L28</a><br>
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/slicerastro-requirements.txt" rel="nofollow noopener">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/slicerastro-requirements.txt</a><br>
<a href="https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/External_python-slicerastro-requirements.cmake" rel="nofollow noopener">https://github.com/Punzo/SlicerAstro/blob/master/SuperBuild/External_python-slicerastro-requirements.cmake</a></p>
</li>
<li>
<p>ensure the packing directly in Slicer build:<br>
<a href="https://github.com/Punzo/SlicerAstro/blob/master/CMakeLists.txt#L169-L176" rel="nofollow noopener">https://github.com/Punzo/SlicerAstro/blob/master/CMakeLists.txt#L169-L176</a></p>
<p>(this will not pollute the Slicer build. They will be installed only when you install the extension)</p>
</li>
</ol>
<p>I tested this recently and it works. However, I tested only on linux.</p>
<p>P.S.: If you don’t have a SuperBuild, I advise to add it if you want to use this approach.</p>

---
