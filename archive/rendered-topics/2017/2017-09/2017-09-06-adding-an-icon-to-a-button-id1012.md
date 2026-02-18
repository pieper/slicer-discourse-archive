# Adding an icon to a button

**Topic ID**: 1012
**Date**: 2017-09-06
**URL**: https://discourse.slicer.org/t/adding-an-icon-to-a-button/1012

---

## Post #1 by @mschumaker (2017-09-06 14:56 UTC)

<p>I’ve tried a number of things to add a resource and use an icon with a button. I’ve noticed I can access Slicer resources, but not ones in the Resources folder of my module. I’d like to do the following, hopefully with a relative path as opposed to absolute, with the icon file in the Resources/Icons directory of my module:</p>
<pre><code>    loadSSFPIcon = qt.QIcon(":/Icons/SSFPicon.png")
    self.LoadSSFPButton = qt.QPushButton("Load SSFP Image Series")
    self.LoadSSFPButton.setIcon(loadSSFPIcon)
    self.layout.addWidget(self.LoadSSFPButton)
</code></pre>
<p>How do I accomplish this?</p>

---

## Post #2 by @cpinter (2017-09-06 15:08 UTC)

<p>You can do this:</p>
<p>iconPath = os.path.join(os.path.dirname(self.parent.path), ‘Resources/Icons’, ‘SSFPicon.png’)<br>
icon = qt.QIcon(iconPath)</p>

---

## Post #3 by @lassoan (2017-09-06 15:55 UTC)

<p>2 posts were split to a new topic: <a href="/t/landmark-registration-for-registering-models/1013">Landmark registration for registering models</a></p>

---

## Post #4 by @mschumaker (2017-09-06 16:19 UTC)

<p>Thanks, I can see where you’re going with this, though when I tried it, self.parent.path was not recognized. What am I missing?</p>

---

## Post #5 by @mschumaker (2017-09-06 16:38 UTC)

<p>I think part of the problem is that I’m trying to use it from the Widget class. I’m looking at <a href="http://ScriptedLoadableModule.py" rel="nofollow noopener">ScriptedLoadableModule.py</a> and I see that self.parent.path works from the module class.</p>

---

## Post #6 by @mschumaker (2017-09-06 17:10 UTC)

<p>I’m currently trying the following, but the image still does not show in the button:</p>
<pre><code>    moduleDir = os.path.dirname(slicer.util.modulePath(self.__module__))
    iconPath = os.path.join(moduleDir, 'Resources/Icons', 'SSFPicon.png')
    icon = qt.QIcon(iconPath)
</code></pre>
<p>Is there something else missing?<br>
Thanks.</p>

---

## Post #7 by @cpinter (2017-09-06 18:16 UTC)

<p>Did you verify that the path actually points to the image? For example you need to install the image file to the build directory as well. A working example:<br>
<a href="https://app.assembla.com/spaces/slicerrt/subversion/source/HEAD/trunk/GelDosimetryAnalysis/src/GelDosimetryAnalysis/GelDosimetryAnalysis.py#ln2322" class="onebox" target="_blank">https://app.assembla.com/spaces/slicerrt/subversion/source/HEAD/trunk/GelDosimetryAnalysis/src/GelDosimetryAnalysis/GelDosimetryAnalysis.py#ln2322</a><br>
with the relevant CMake line<br>
<a href="https://app.assembla.com/spaces/slicerrt/subversion/source/HEAD/trunk/GelDosimetryAnalysis/src/GelDosimetryAnalysis/CMakeLists.txt#ln19" class="onebox" target="_blank">https://app.assembla.com/spaces/slicerrt/subversion/source/HEAD/trunk/GelDosimetryAnalysis/src/GelDosimetryAnalysis/CMakeLists.txt#ln19</a></p>

---

## Post #8 by @mschumaker (2017-09-06 19:52 UTC)

<p>I’ve checked the value of iconPath, and it points to the image. What build directory do you mean?<br>
I’ve looked at the code you referenced, and what I have is consistent. A possible difference may be that I’m using an additional image, rather than the one that was defined when the module was created. Do I need a .qrc file, or something else to add new files?</p>

---

## Post #9 by @cpinter (2017-09-06 20:09 UTC)

<p>I said all I know. Please try to work with this example and see what is in it that is not present in your module. One of those differences will be what causes your image not to show up. The qrc file is a good starting point.</p>

---

## Post #10 by @mschumaker (2017-09-06 20:39 UTC)

<p>Ok. Thanks for trying. If you think of anything else, let me know.</p>

---

## Post #11 by @lassoan (2017-09-06 22:35 UTC)

<p>There are many examples for using custom icons in widget classes. For example: <a href="https://github.com/SlicerIGT/SlicerIGT/blob/b05132759b32ae3a2d3e52e9897dd28f7a39677d/PlusRemote/PlusRemote.py#L55">https://github.com/SlicerIGT/SlicerIGT/blob/b05132759b32ae3a2d3e52e9897dd28f7a39677d/PlusRemote/PlusRemote.py#L55</a></p>
<p>Using qrc file is a bit more complicated, because you need to compile resources and for that probably you need to build Slicer and your module.</p>

---

## Post #12 by @cpinter (2017-09-06 22:49 UTC)

<p>Yes, this is basically the same method. What you’ll need to make sure is that the icon file is properly deployed with your module.</p>

---

## Post #13 by @lassoan (2017-09-06 22:51 UTC)

<p>Yes, there are just slight differences in how to retrieve resource directory path from various classes.</p>

---

## Post #14 by @jcfr (2017-09-07 15:00 UTC)

<p>From scripted module, there is also support for handling <code>qrc</code> files:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/adf9e547646d38f2bf93e6d456bc715974e467cf/Modules/Scripted/ExtensionWizard/CMakeLists.txt#L18-L27" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/adf9e547646d38f2bf93e6d456bc715974e467cf/Modules/Scripted/ExtensionWizard/CMakeLists.txt#L18-L27" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/adf9e547646d38f2bf93e6d456bc715974e467cf/Modules/Scripted/ExtensionWizard/CMakeLists.txt#L18-L27</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="18" style="counter-reset: li-counter 17 ;">
<li>slicerFunctionAddPythonQtResources(MODULE_PYTHON_RESOURCES</li>
<li>${MODULE_NAME}Lib/${MODULE_NAME}.qrc</li>
<li>)</li>
<li>
</li>
<li>#-----------------------------------------------------------------------------</li>
<li>slicerMacroBuildScriptedModule(</li>
<li>NAME ${MODULE_NAME}</li>
<li>SCRIPTS ${MODULE_PYTHON_SCRIPTS} ${MODULE_PYTHON_RESOURCES}</li>
<li>WITH_GENERIC_TESTS</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This will generate a <code>&lt;NameOfFile&gt;Resources</code> python module that can be imported:</p>
<pre><code class="lang-auto">from . import ExtensionWizardResources as Resources
</code></pre>
<p>See <a href="https://github.com/Slicer/Slicer/blob/adf9e547646d38f2bf93e6d456bc715974e467cf/Modules/Scripted/ExtensionWizard/ExtensionWizardLib/__init__.py#L1">here</a> for more details</p>
<p>Then, the corresponding resources can be used as usual:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/adf9e547646d38f2bf93e6d456bc715974e467cf/Modules/Scripted/ExtensionWizard/ExtensionWizard.py#L33-L34" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/adf9e547646d38f2bf93e6d456bc715974e467cf/Modules/Scripted/ExtensionWizard/ExtensionWizard.py#L33-L34" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/adf9e547646d38f2bf93e6d456bc715974e467cf/Modules/Scripted/ExtensionWizard/ExtensionWizard.py#L33-L34</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="33" style="counter-reset: li-counter 32 ;">
<li>parent.title = "Extension Wizard"</li>
<li>parent.icon = qt.QIcon(":/Icons/Medium/ExtensionWizard.png")</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #15 by @mschumaker (2017-09-07 16:59 UTC)

<p>Thanks very much everyone. I currently have it working with this in the CMakeLists.txt:</p>
<pre><code>set(MODULE_PYTHON_RESOURCES
  Resources/Icons/${MODULE_NAME}.png
  Resources/Icons/SSFPIcon.png
  )
</code></pre>
<p>And this in my module Widget class:</p>
<pre><code>    moduleDir = os.path.dirname(slicer.util.modulePath(self.__module__))
    SSFPIconPath = os.path.join(moduleDir, 'Resources/Icons', 'SSFPIcon.png')
    loadSSFPIcon = qt.QIcon(SSFPIconPath)
    self.LoadSSFPButton = qt.QPushButton(" Load SSFP Image Series")
    self.LoadSSFPButton.setIcon(loadSSFPIcon)
    self.layout.addWidget(self.LoadSSFPButton)</code></pre>

---

## Post #16 by @mschumaker (2017-09-07 17:03 UTC)

<p>Thanks, Jean Christophe. I tried to follow this, but ran in to difficulty. Possibly with the qrc file prefix, or location. Since I was able to get it working the other way, I’ll carry on with it for now.<br>
Thanks again.</p>

---

## Post #17 by @lassoan (2017-09-07 17:19 UTC)

<p>The complexity with using qrc files is that you need to compile resources into a qrc file. That requires building of Slicer (or manual compilation).</p>

---

## Post #18 by @che85 (2018-02-15 20:19 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I tried handling qrc in my own project, but I am failing when bulding the project.</p>
<p>Out of curiosity I copied the ExtensionWizard to my local project and added that subdirectory to my CMakeLists.txt.</p>
<pre><code class="lang-auto">christian@christians-mbp ~/D/S4R&gt; gcc --version
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 9.0.0 (clang-900.0.39.2)
Target: x86_64-apple-darwin17.4.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
</code></pre>
<p>The output that I am getting looks as follows:</p>
<pre><code class="lang-auto">[  5%] Built target ConfigureAdditionalLauncherSettings
[ 11%] Copying python Script: ExtensionWizard.py
[ 16%] Copying python Script: ExtensionWizardLib/__init__.py
[ 22%] Copying python Script: ExtensionWizardLib/CreateComponentDialog.py
[ 27%] Copying python Script: ExtensionWizardLib/DirectoryListWidget.py
[ 33%] Copying python Script: ExtensionWizardLib/EditableTreeWidget.py
[ 38%] Copying python Script: ExtensionWizardLib/EditExtensionMetadataDialog.py
[ 44%] Copying python Script: ExtensionWizardLib/LoadModulesDialog.py
[ 50%] Copying python Script: ExtensionWizardLib/ModuleInfo.py
[ 55%] Copying python Script: ExtensionWizardLib/SettingsPanel.py
[ 61%] Copying python Script: ExtensionWizardLib/TemplatePathUtilities.py
make[2]: *** No rule to make target `/Utilities/Scripts/qrcc.py', needed by `ExtensionWizard/ExtensionWizardLib/ExtensionWizardResources.py'.  Stop.
make[1]: *** [ExtensionWizard/CMakeFiles/CopyExtensionWizardPythonScriptFiles.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>with running <code>make -d</code> <a href="https://gist.github.com/che85/1bff5a003b53e477a7ef403c7c3f7991" rel="nofollow noopener">https://gist.github.com/che85/1bff5a003b53e477a7ef403c7c3f7991</a></p>
<p>By any chance, do you have an idea what why that doesn’t work locally?</p>
<p>Thanks<br>
Christian</p>

---
