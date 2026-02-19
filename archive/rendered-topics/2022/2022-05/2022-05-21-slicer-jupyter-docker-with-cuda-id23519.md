---
topic_id: 23519
title: "Slicer Jupyter Docker With Cuda"
date: 2022-05-21
url: https://discourse.slicer.org/t/23519
---

# Slicer Jupyter docker with CUDA

**Topic ID**: 23519
**Date**: 2022-05-21
**URL**: https://discourse.slicer.org/t/slicer-jupyter-docker-with-cuda/23519

---

## Post #1 by @Jakub_Mitura (2022-05-21 18:08 UTC)

<p>Hello I try to customize official slicer docker for jupyter, and integrate it with vs code development in a container.</p>
<p>I managed already to Install and test CUDA - which seem to works ok (pytorch detects it)</p>
<p>Now I have some problems, first I want to ask is it possible to use slicer extensions from the jupyter - primarly but not exclusively I am interested in installing SlicerRadiomics extension and use it from jupyter.</p>
<p>Secondly I try to install extension by modyfing install.sh<br>
and adding after SlicerJupyter is installed</p>
<pre><code class="lang-auto">
echo "Install extensions"
$slicer_executable -c '
em = slicer.app.extensionsManagerModel()
extensionMetaData = em.retrieveExtensionMetadataByName("SlicerRadiomics")
if slicer.app.majorVersion*100+slicer.app.minorVersion &lt; 413:
    # Slicer-4.11
    itemId = extensionMetaData["item_id"]
    url = f"{em.serverUrl().toString()}/download?items={itemId}"
    extensionPackageFilename = f"{slicer.app.temporaryPath}/{itemId}"
    slicer.util.downloadFile(url, extensionPackageFilename)
else:
    # Slicer-4.13
    itemId = extensionMetaData["_id"]
    url = f"{em.serverUrl().toString()}/api/v1/item/{itemId}/download"
    extensionPackageFilename = f"{slicer.app.temporaryPath}/{itemId}"
    slicer.util.downloadFile(url, extensionPackageFilename)
    # Prevent showing popups for installing dependencies
    # (this is not needed right now for SlicerJupyter, but we still add this line here
    # because this docker image may be used by other projects as a starting point)
    em.interactive = False
em.installExtension(extensionPackageFilename)
'
</code></pre>
<p>Yet It gives error</p>
<pre><code class="lang-auto">[2022-05-21T18:07:13.536Z] Install extensions
[2022-05-21T18:07:15.830Z] Traceback (most recent call last):
[2022-05-21T18:07:15.830Z]   File "&lt;string&gt;", line 12, in &lt;module&gt;
[2022-05-21T18:07:15.831Z] KeyError: '_id'
[2022-05-21T18:07:16.363Z] The command '/bin/sh -c ./install.sh ${HOME}/Slicer/Slicer &amp;&amp;     rm ${HOME}/install.sh' returned a non-zero code: 1
[2022-05-21T18:07:16.366Z] Stop (15155 ms): Run: docker build -f /home/jakub/projects/slicerModifB/.devcontainer/Dockerfile -t vsc-slicermodifb-cec2d2e6cdb09b3c149f8f6bee02d187 /home/jakub/projects/slicerModifB/.devcontainer
[2022-05-21T18:07:16.367Z] Error: Command failed: docker build -f /home/jakub/projects/slicerModifB/.devcontainer/Dockerfile -t vsc-slicermodifb-cec2d2e6cdb09b3c149f8f6bee02d187 /home/jakub/projects/slicerModifB/.devcontainer
[2022-05-21T18:07:16.367Z]     at Tu (/home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js:221:3219)
[2022-05-21T18:07:16.367Z]     at processTicksAndRejections (node:internal/process/task_queues:96:5)
[2022-05-21T18:07:16.367Z]     at async LR (/home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js:221:1567)
[2022-05-21T18:07:16.367Z]     at async zy (/home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js:221:594)
[2022-05-21T18:07:16.367Z]     at async $R (/home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js:226:2007)
[2022-05-21T18:07:16.367Z]     at async Zy (/home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js:226:3112)
[2022-05-21T18:07:16.367Z]     at async BR (/home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js:226:12448)
[2022-05-21T18:07:16.367Z]     at async qR (/home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js:226:12204)
[2022-05-21T18:07:16.370Z] Stop (15293 ms): Run: /snap/code/97/usr/share/code/code /home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js up --user-data-folder /home/jakub/.config/Code/User/globalStorage/ms-vscode-remote.remote-containers/data --container-data-folder .vscode-server/data/Machine --container-system-data-folder /var/vscode-server --workspace-folder /home/jakub/projects/slicerModifB --workspace-mount-consistency cached --id-label vsch.local.folder=/home/jakub/projects/slicerModifB --id-label vsch.quality=stable --log-level debug --log-format json --config /home/jakub/projects/slicerModifB/.devcontainer/devcontainer.json --default-user-env-probe loginInteractiveShell --mount type=volume,source=vscode,target=/vscode,external=true --skip-post-create --update-remote-user-uid-default on --mount-workspace-git-root true
[2022-05-21T18:07:16.370Z] Exit code 1
[2022-05-21T18:07:16.372Z] Command failed: /snap/code/97/usr/share/code/code /home/jakub/.vscode/extensions/ms-vscode-remote.remote-containers-0.234.0/dist/spec-node/devContainersSpecCLI.js up --user-data-folder /home/jakub/.config/Code/User/globalStorage/ms-vscode-remote.remote-containers/data --container-data-folder .vscode-server/data/Machine --container-system-data-folder /var/vscode-server --workspace-folder /home/jakub/projects/slicerModifB --workspace-mount-consistency cached --id-label vsch.local.folder=/home/jakub/projects/slicerModifB --id-label vsch.quality=stable --log-level debug --log-format json --config /home/jakub/projects/slicerModifB/.devcontainer/devcontainer.json --default-user-env-probe loginInteractiveShell --mount type=volume,source=vscode,target=/vscode,external=true --skip-post-create --update-remote-user-uid-default on --mount-workspace-git-root true
[2022-05-21T18:07:16.373Z] Exit code 1
</code></pre>
<p>My docker project</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/jakubMitura14/slicerModifB/tree/master">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/jakubMitura14/slicerModifB/tree/master" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/jakubMitura14/slicerModifB/tree/master" target="_blank" rel="noopener nofollow ugc">GitHub - jakubMitura14/slicerModifB</a></h3>

  <p><a href="https://github.com/jakubMitura14/slicerModifB/tree/master" target="_blank" rel="noopener nofollow ugc">master</a></p>

  <p><span class="label1">Contribute to jakubMitura14/slicerModifB development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2022-05-22 13:38 UTC)

<p>This sounds great and it seems that you are making good progress.</p>
<aside class="quote no-group" data-username="Jakub_Mitura" data-post="1" data-topic="23519">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jakub_mitura/48/8858_2.png" class="avatar"> Jakub_Mitura:</div>
<blockquote>
<p>is it possible to use slicer extensions from the jupyter - primarly but not exclusively I am interested in installing SlicerRadiomics extension and use it from jupyter</p>
</blockquote>
</aside>
<p>Yes, this should be no problem at all. You can install other extensions the same way as SlicerJupyter. You can use any modules in any extensions from Jupyter the same way as from the Python console or any Python module. You can find more information in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html">Python FAQ</a>.</p>
<aside class="quote no-group" data-username="Jakub_Mitura" data-post="1" data-topic="23519">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jakub_mitura/48/8858_2.png" class="avatar"> Jakub_Mitura:</div>
<blockquote>
<p>I try to install extension by modyfing install.sh<br>
and adding after SlicerJupyter is installed</p>
</blockquote>
</aside>
<p>If <code>_id</code> key is missing from the extension description then it means that the extension is not available for that Slicer version. I would recommend to use the latest Slicer Stable version now (Slicer 5.0.x). You can see the list of extensions available for this version here:</p>
<p><a href="https://extensions.slicer.org/catalog/All/30822/linux" class="onebox" target="_blank" rel="noopener">https://extensions.slicer.org/catalog/All/30822/linux</a></p>

---

## Post #3 by @Jakub_Mitura (2022-05-22 15:50 UTC)

<p>Fantastic, yes now it works as I got newer version - when I open python console in the container .Hovewer How to get a token inside the container</p>
<p>as I need <a href="http://127.0.0.1:8888/?token" rel="noopener nofollow ugc">http://127.0.0.1:8888/?token</a> to open jupyter notebook server connection  - I know that I can do it by building in a normal way docker image from command line but from VS code inside the container it is less obvious for me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2022-05-23 03:20 UTC)

<p>You can print the token to the output and capture it from there; or write the token to a file in a mapped folder and read it from that file.</p>
<p>Alternatively, you can <a href="https://stackoverflow.com/questions/47492150/how-do-i-set-a-custom-token-for-a-jupyter-notebook">specify a custom token for the Jupyter server</a>, for example by passing it as a command-line argument to the docker container or via an environment variable.</p>

---

## Post #5 by @Jakub_Mitura (2022-06-02 09:10 UTC)

<p>ok It is working now thanks <a class="mention" href="/u/lassoan">@lassoan</a>  !, If you consider it worth it You may use it as an example for others (<a href="https://github.com/jakubMitura14/SlicerNotebookCUDA" rel="noopener nofollow ugc">if yes here is the  link to repository</a>)</p>
<p>However both dataspell and vs code do not support interactive widgets - that simply works in browser, Is there any IDE that supports it?</p>

---

## Post #6 by @lassoan (2022-06-27 19:10 UTC)

<p>Thanks for sharing your results. What were the main changes that you had to do?</p>
<p>VS Code has lots of assumptions about your Jupyter server and kernel which are often not valid. For example, in Slicer’s Python environment the Python interpreter has a special name, we use xeus-python kernel and not the default native Python kernel - which VS Code may not be prepared for.</p>

---

## Post #7 by @Jakub_Mitura (2022-06-28 06:22 UTC)

<p>changed base to nvidia/cuda:11.3.1-base-ubuntu20.04</p>
<p>added some basic libraries like manpages-dev</p>
<p>installed CUDA 11.3</p>
<p>Changed version of the Slicer to newer</p>
<p>installed  some python packages mainly pytorch and monai with most of its dependencies<br>
for convenience<br>
created some additional folders, added jupyterlab_github</p>

---
