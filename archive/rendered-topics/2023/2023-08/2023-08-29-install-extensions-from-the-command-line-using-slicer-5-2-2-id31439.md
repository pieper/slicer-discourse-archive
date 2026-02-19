---
topic_id: 31439
title: "Install Extensions From The Command Line Using Slicer 5 2 2"
date: 2023-08-29
url: https://discourse.slicer.org/t/31439
---

# Install extensions from the command line using Slicer 5.2.2

**Topic ID**: 31439
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/install-extensions-from-the-command-line-using-slicer-5-2-2/31439

---

## Post #1 by @jhlegarreta (2023-08-29 21:26 UTC)

<p>Hi,<br>
can Slicer extensions be installed from the command line? If yes, where can I find the related documentation?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-08-29 21:42 UTC)

<p>In the past I’ve used this:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/Dockerfile#L16-L21">
  <header class="source">

      <a href="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/Dockerfile#L16-L21" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/Dockerfile#L16-L21" target="_blank" rel="noopener">pieper/SlicerDockers/blob/master/slicer-plus/Dockerfile#L16-L21</a></h4>



    <pre class="onebox"><code class="lang-">
      <ol class="start lines" start="16" style="counter-reset: li-counter 15 ;">
          <li>for ext in ${SLICER_EXTS} ; \</li>
          <li>do echo "Installing ${ext}" ; \</li>
          <li>  EXTENSION_TO_INSTALL=${ext} \</li>
          <li>    su researcher -c "xvfb-run --auto-servernum \</li>
          <li>      /opt/slicer/Slicer --python-script /tmp/install-slicer-extension.py" ; \</li>
          <li>done</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>to run this script:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py">
  <header class="source">

      <a href="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py" target="_blank" rel="noopener">pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py</a></h4>


      <pre><code class="lang-py">
import os
extensionName = os.environ['EXTENSION_TO_INSTALL']
print(f"installing {extensionName}")
manager = slicer.app.extensionsManagerModel()
if not manager.isExtensionInstalled(extensionName):
  extensionMetaData = manager.retrieveExtensionMetadataByName(extensionName)
  url = f"{manager.serverUrl().toString()}/api/v1/item/{extensionMetaData['_id']}/download"
  extensionPackageFilename = slicer.app.temporaryPath+'/'+extensionMetaData['_id']
  slicer.util.downloadFile(url, extensionPackageFilename)
  manager.installExtension(extensionPackageFilename)
exit()
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But you can also use this newer code:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension</a></p>

---

## Post #3 by @jhlegarreta (2023-08-29 21:57 UTC)

<p>OK, thanks Steve. Will give it a try and report back as time permits.</p>

---

## Post #4 by @jhlegarreta (2023-08-29 23:08 UTC)

<p>So, when launching the shell command (using Slicer 5.2.2 on an Ubuntu 22.04 machine), e.g.</p>
<pre><code class="lang-auto">slicer_ext="CurveMaker"

export EXTENSION_TO_INSTALL=${slicer_ext}

./Slicer \
  --no-splash \
  --no-main-window \
  --python-script "/&lt;my_path&gt;/install_slicer_extension.py"
</code></pre>
<p>where the <code>install_slicer_extension.py</code> script is esentially what you kindly posted in <a href="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py" rel="noopener nofollow ugc">https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py</a>, I get the following error:</p>
<pre><code class="lang-auto">installing CurveMaker
Traceback (most recent call last):
  File "&lt;string&gt;", line 5, in &lt;module&gt;
  File "&lt;string&gt;", line 28, in &lt;module&gt;
  File "&lt;string&gt;", line 17, in main
AttributeError: qSlicerExtensionsManagerModel has no attribute named 'retrieveExtensionMetadataByName'
</code></pre>
<p>the command hangs, and the installation does not take place.</p>
<p>So maybe something changed from the version you used at the time (5.0.2 according to the commit message) and 5.2.2?</p>

---

## Post #5 by @jcfr (2023-08-30 04:53 UTC)

<p>Starting with Slicer 5.4, a dedicated API was introduced to streamline the programmatic installation of extensions.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension</a></p>

---

## Post #6 by @jhlegarreta (2023-08-30 12:48 UTC)

<p>Steve already pointed to that possibility for Slicer 5.4; I’m using 5.2.2, though.</p>

---

## Post #7 by @jcfr (2023-08-30 13:15 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="4" data-topic="31439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>So maybe something changed from the version you used at the time (5.0.2 according to the commit message) and 5.2.2?</p>
</blockquote>
</aside>
<p>See <a href="https://github.com/Slicer/Slicer/commit/537281b6cfeaa3bdf9f35538efb53846a2fe3729#diff-1c3362f027f4595ea24d34d4627256f9d63d418fcddbd325fe8d022829c611ac" class="inline-onebox">BUG: fix/doc DMRIInstall (#6594) · Slicer/Slicer@537281b · GitHub</a></p>

---

## Post #8 by @jhlegarreta (2023-08-30 13:24 UTC)

<p>Hitting the very same error reported earlier even when modifying the script according to it.</p>

---

## Post #9 by @jcfr (2023-08-30 13:33 UTC)

<p>With Slicer &gt;= 5.2, consider using the following script:</p>
<pre><code class="lang-python">import os


extensionName = os.environ['EXTENSION_TO_INSTALL']
em = slicer.app.extensionsManagerModel()
if not em.isExtensionInstalled(extensionName):
    em.interactive = False  # prevent display of popups
    em.updateExtensionsMetadataFromServer(True, True)  # update extension metadata from server now
    installDependencies = True
    if not em.downloadAndInstallExtensionByName(extensionName, installDependencies, True):
        raise ValueError(f"Failed to install {extensionName} extension")
</code></pre>
<p>Assuming you saved it as <code>/tmp/install_slicer_extension.py</code>, you may run it using:</p>
<pre><code class="lang-bash">$ EXTENSION_TO_INSTALL=Sandbox \
~/Downloads/Slicer-5.2.2-linux-amd64/Slicer \
  --exit-after-startup \
  --no-main-window \
  --disable-modules \
  --python-script /tmp/install_slicer_extension.py

Retrieving extension metadata for Sandbox extension
Retrieving Sandbox extension files (extensionId: 63f5ca688939577d9867ba35)
Downloading Sandbox extension (item_id: 63f5ca688939577d9867ba35, file_id: 64c8c82516826926710d5a97)
Installed extension Sandbox (63f5ca688939577d9867ba35) revision e163d61
</code></pre>

---

## Post #10 by @jcfr (2023-08-30 13:42 UTC)

<p>And here is an improved version allowing to install extensions in Slicer 5.2.2 while passing extension names as regular arguments:</p>
<pre><code class="lang-python">import sys


def install_exttension(extensionName, installDependencies=True):
    print(f"\nInstalling extension {extensionName}")
    em = slicer.app.extensionsManagerModel()
    if em.isExtensionInstalled(extensionName):
        print(f"Extension {extensionName} already installed")
        return

    em.interactive = False  # prevent display of popups
    em.updateExtensionsMetadataFromServer(True, True)  # update extension metadata from server now

    if not em.downloadAndInstallExtensionByName(extensionName, installDependencies, True):
        raise ValueError(f"Failed to install {extensionName} extension")


if __name__ == "__main__":
    for extensionName in sys.argv[1:]:
        install_exttension(extensionName)
</code></pre>
<p>For future reference, to install extension in Slicer 5.4, there is a dedicated API to do so. See <a href="https://slicer.readthedocs.io/en/5.4/developer_guide/script_repository.html#download-and-install-extension">here</a></p>
<p>Then, to install extensions:</p>
<pre><code class="lang-bash">$ ads/Slicer-5.2.2-linux-amd64/Slicer \
  --exit-after-startup \
  --no-main-window \
  --disable-modules \
  --python-script /tmp/install_slicer_extension.py \
  Sandbox \
  SlicerHeart \
  SlicerDMRI
</code></pre>
<p>and example of output:</p>
<pre><code class="lang-plaintext">Installing extension Sandbox
Retrieving extension metadata for Sandbox extension
Retrieving Sandbox extension files (extensionId: 63f5ca688939577d9867ba35)
Downloading Sandbox extension (item_id: 63f5ca688939577d9867ba35, file_id: 64c8c82516826926710d5a97)
Installed extension Sandbox (63f5ca688939577d9867ba35) revision e163d61

Installing extension SlicerHeart
Retrieving extension metadata for SlicerHeart extension
Retrieving SlicerHeart extension files (extensionId: 63f5f3f08939577d9867dbc7)
Downloading SlicerHeart extension (item_id: 63f5f3f08939577d9867dbc7, file_id: 64de321206a93d6cff35a4c1)
"The following extensions are required by SlicerHeart extension therefore they will be installed now: SlicerIGT, SlicerIGSIO"
Retrieving extension metadata for SlicerIGT extension
Retrieving SlicerIGT extension files (extensionId: 63f5f2d78939577d9867da34)
Downloading SlicerIGT extension (item_id: 63f5f2d78939577d9867da34, file_id: 64aa9a94b81c954f339bfef6)
Retrieving extension metadata for SlicerIGSIO extension
Retrieving SlicerIGSIO extension files (extensionId: 63f5da488939577d9867c528)
Downloading SlicerIGSIO extension (item_id: 63f5da488939577d9867c528, file_id: 64c0f2c6c0e19dd3b30f7352)
Installed extension SlicerHeart (63f5f3f08939577d9867dbc7) revision 09e440d
Installed extension SlicerIGT (63f5f2d78939577d9867da34) revision 245fa92
Installed extension SlicerIGSIO (63f5da488939577d9867c528) revision b6328fd

Installing extension SlicerDMRI
Retrieving extension metadata for SlicerDMRI extension
Retrieving SlicerDMRI extension files (extensionId: 63fb32ce8939577d9869e2b2)
Downloading SlicerDMRI extension (item_id: 63fb32ce8939577d9869e2b2, file_id: 64ccc3ed16826926710f2500)
"The following extensions are required by SlicerDMRI extension therefore they will be installed now: UKFTractography"
Retrieving extension metadata for UKFTractography extension
Retrieving UKFTractography extension files (extensionId: 63f5eae38939577d9867d2b3)
Downloading UKFTractography extension (item_id: 63f5eae38939577d9867d2b3, file_id: 63f5eae38939577d9867d2ba)
Installed extension SlicerDMRI (63fb32ce8939577d9869e2b2) revision aad4331
Installed extension UKFTractography (63f5eae38939577d9867d2b3) revision fcf83e2

</code></pre>

---

## Post #11 by @jhlegarreta (2023-08-30 14:59 UTC)

<p>OK, after some more work, got it working: looks like I had still carried over the statement to call <code>retrieveExtensionMetadataByName</code> in <a href="https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py#L7C3-L7C77" rel="noopener nofollow ugc">https://github.com/pieper/SlicerDockers/blob/master/slicer-plus/install-slicer-extension.py#L7C3-L7C77</a>, so the instructions in <a href="https://discourse.slicer.org/t/install-extensions-from-the-command-line-using-slicer-5-2-2/31439/10" class="inline-onebox">Install extensions from the command line using Slicer 5.2.2 - #10 by jcfr</a> worked.</p>
<p>Thanks for the effort <a class="mention" href="/u/jcfr">@jcfr</a>.</p>

---
