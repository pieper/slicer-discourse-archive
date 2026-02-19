---
topic_id: 35815
title: "How To Make A Portable Slicer With Monai Auto3Dseg Extension"
date: 2024-04-29
url: https://discourse.slicer.org/t/35815
---

# How to make a portable slicer with Monai Auto3Dseg extension

**Topic ID**: 35815
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/how-to-make-a-portable-slicer-with-monai-auto3dseg-extension/35815

---

## Post #1 by @Osson4 (2024-04-29 19:56 UTC)

<p>Using the latest preview of slicer (5.7.0 revision 32834 built 2024-04-28) on a Windows system, I would like to try the new extension on a offline, hospital computer with limited space and writing rights but with good GPU. I’m trying to make a portable version so I can run slicer from a hard-disk, without internet access on the secondary machine and with limited disk writing rights due to admin.<br>
While following this thread for clarity <a href="https://discourse.slicer.org/t/slicer-is-now-fully-portable/15410">adn</a> I would like to share how to correctly make a portable version and also request support in some passages, to see if i’m doing something wrong.</p>
<p>1 - I get that now the Slicer.ini file needs now to be put in<br>
<em>x:\myfolder\Slicer 4.13.0-2021-01-05/slicer.org/Slicer.ini</em><br>
to make slicer effectively detect the new .ini file and change the absolute paths to a relative reference to the main app directory.<br>
I can’t manage to change the DICOM database default main folder for a relative position (I tried under general from the the “customize slicer” settings menu and it does not work). The other default folders (temp, cache, extensions and scene) change immediately in the .ini file when you update the “customize slicer” settings from the GUI.</p>
<p>2 - I then proceed to install the Monai Auto3dseg extension from the store, and that would also automatically install the Pytorch extension (right now the home directory is still managable, around 1 GB of disk space). When using the auto3dseg for the first time, the extension would then automatically download the required dependencies, or you can force install it from advaced mode if you don’t have dicom data.<br>
Even though I have the pytorch extension correctly installed, the monai Auto3dseg would install pytorch and monai dependencies for a total of more than 7gb. I would like to know if this behaviour is correct, or if there’s a way to make a lighter version <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>3 - Monai auto3dseg downloads the pretrained models for inference in a separate cache folder that can be opened via the GUI with the button “opens models cache folder”. That folder in my computer is located in:<br>
“C:\Users&lt;MYNAME&gt;.MONAIAuto3DSeg\models”<br>
that is outside the app home directory. Thus I can’t export the model weights to an offline computer, without having the rights to write in a secondary folder on the offline machine. Is it possibile to change the model cache folder to make slicer with this extension completely portable?</p>
<p>Thanks to whoever can answer these doubts <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2024-04-29 20:44 UTC)

<aside class="quote no-group" data-username="Osson4" data-post="1" data-topic="35815">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/osson4/48/70236_2.png" class="avatar"> Osson4:</div>
<blockquote>
<p>I can’t manage to change the DICOM database default main folder for a relative position</p>
</blockquote>
</aside>
<p>It is actually a relative path if you place it within the Slicer folder. You can see that by inspecting the Slicer.ini file, you’ll see something like this:</p>
<pre><code class="lang-auto">[General]
DatabaseDirectory_X.Y.Z=slicer.org/dicom
</code></pre>
<p>What may confuse you is that by default you link DICOM files, so Slicer will not manage the DICOM files (Slicer will not delete the files when you delete them in the browser, they are expected to remain at the same location if Slicer is moved to a different location, etc.). If you want to Slicer to manage the DICOM files then click the small down-arrow button on the <code>Import DICOM files</code> button and check <code>Copy imported files to DICOM database</code> checkbox - or set this in the Slicer.ini file:</p>
<pre><code class="lang-auto">[DICOM]
ImportDirectoryMode=1
</code></pre>
<aside class="quote no-group" data-username="Osson4" data-post="1" data-topic="35815">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/osson4/48/70236_2.png" class="avatar"> Osson4:</div>
<blockquote>
<p>I then proceed to install the Monai Auto3dseg extension from the store, and that would also automatically install the Pytorch extension (right now the home directory is still managable, around 1 GB of disk space)</p>
</blockquote>
</aside>
<p>Pytorch Slicer extension just responsible for downloading and configuring Pytorch Python package.</p>
<p>Pytorch Python packageis about 5GB, largest part (3.5GB) is for CUDA support. ITK is about 0.7GB. The rest of the packages are small. If you have already installed the packages then they won’t be downloaded and installed again (unless you force).</p>
<p>I don’t think you can easily reduce this, but if you have time then you could search on the web if anybody was able to significantly cut down on the size of pytorch. While I agree that it would be nice to reduce the package size, memory is so cheap and fast (you can get a 32GB fast USB3 memory stick for $10) and Slicer can run directly from the stick, it should not be major issue.</p>
<aside class="quote no-group quote-modified" data-username="Osson4" data-post="1" data-topic="35815">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/osson4/48/70236_2.png" class="avatar"> Osson4:</div>
<blockquote>
<p>Monai auto3dseg downloads the pretrained models for inference in a separate cache folder that can be opened via the GUI with the button “opens models cache folder”. That folder in my computer is located in:<br>
“C:\Users.MONAIAuto3DSeg\models”<br>
that is outside the app home directory.</p>
</blockquote>
</aside>
<p>Yes, sure, it is really easy to change this. All you need to do is to change this single line:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/302495cf504eef3d80831444bbbadb0d5fe8101c/MONAIAuto3DSeg/MONAIAuto3DSeg.py#L639">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/302495cf504eef3d80831444bbbadb0d5fe8101c/MONAIAuto3DSeg/MONAIAuto3DSeg.py#L639" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/302495cf504eef3d80831444bbbadb0d5fe8101c/MONAIAuto3DSeg/MONAIAuto3DSeg.py#L639" target="_blank" rel="noopener">lassoan/SlicerMONAIAuto3DSeg/blob/302495cf504eef3d80831444bbbadb0d5fe8101c/MONAIAuto3DSeg/MONAIAuto3DSeg.py#L639</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="629" style="counter-reset: li-counter 628 ;">
          <li></li>
          <li>def __init__(self):</li>
          <li>    """</li>
          <li>    Called when the logic class is instantiated. Can be used for initializing member variables.</li>
          <li>    """</li>
          <li>    from collections import OrderedDict</li>
          <li></li>
          <li>    ScriptedLoadableModuleLogic.__init__(self)</li>
          <li></li>
          <li>    import pathlib</li>
          <li class="selected">    self.fileCachePath = pathlib.Path.home().joinpath(".MONAIAuto3DSeg")</li>
          <li></li>
          <li>    self.dependenciesInstalled = False  # we don't know yet if dependencies have been installed</li>
          <li></li>
          <li>    self.moduleDir = os.path.dirname(slicer.util.getModule('MONAIAuto3DSeg').path)</li>
          <li></li>
          <li>    self.logCallback = None</li>
          <li>    self.processingCompletedCallback = None</li>
          <li>    self.startResultImportCallback = None</li>
          <li>    self.endResultImportCallback = None</li>
          <li>    self.useStandardSegmentNames = True</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>to something like this:</p>
<pre><code class="lang-auto"># User can create a .MONAIAuto3DSeg folder within the Slicer settings folder
# (same folder as Slicer.ini file) to make the downloaded model files portable with the application.
# If the folder does not exist (this is the default) then the models are cached in the user profile folder,
# so that not just Slicer but other tools can find and use it.
portableFileCachePath = 
pathlib.Path(slicer.app.slicerUserSettingsFilePath).parent.joinpath(".MONAIAuto3DSeg")
self.fileCachePath = portableFileCachePath if portableFileCachePath.exists() else pathlib.Path.home().joinpath(".MONAIAuto3DSeg")
</code></pre>
<p>Please test and send a pull request if works well for you.</p>

---
