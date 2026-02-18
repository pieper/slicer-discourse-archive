# Running CLI modules on a remote server

**Topic ID**: 328
**Date**: 2017-05-16
**URL**: https://discourse.slicer.org/t/running-cli-modules-on-a-remote-server/328

---

## Post #1 by @mirclem (2017-05-16 17:44 UTC)

<p>I developed a tool to get all the CLI modules loaded into a local Slicer, use them as you were used to. But, when you click on apply it generates the command, saves it in a json file and uploads the json file to a database.<br>
Then, a remote Slicer has a connection with the database, it checks if there is a command in the database, runs it remotely and then uploads back the outputs.</p>
<p>Thanks to the nice documentation and people here on Discourse, I have been able to parse CLI node parameters, get their values (nodes) and run some CLIs remotely.<br>
The only exception I have is about colormaps. When I generate the CLI command in the local Slicer, the colormap parameter is empty and so the remote Slicer returns an error with missing parameter.</p>

---

## Post #2 by @lassoan (2017-05-16 18:14 UTC)

<p>Slicer does some processing before running a CLI: export data to files, resolve dependencies (such as colormaps); and after running a CLI (displays results, applies a referenced transform, etc). I would suggest to intercept the CLI execution at a lower level so that you don’t have to reimplement all these pre/post CLI actions.</p>
<p><a href="https://www.na-mic.org/Wiki/index.php/2013_Project_Week:Slicer_Personal_Cloud">Slicer personal cloud</a> did something similar. See more information about it on <a href="https://www.slicer.org/wiki/Developer_Meetings/20130212">this page</a> (<em>regarding remote execution of modules</em>). Probably <a class="mention" href="/u/pieper">@pieper</a> and/or Jim Miller (GE Corporate Research) can give you more details.</p>

---

## Post #3 by @jcfr (2017-05-16 21:18 UTC)

<p>Hi Clement,</p>
<p>If you would like to execute CLI remotely, you could have a look at <a href="https://github.com/girder/slicer_cli_web">https://github.com/girder/slicer_cli_web</a></p>
<p>The easiest would be to ask your questions on <a href="https://gitter.im/girder/girder">https://gitter.im/girder/girder</a></p>
<p>In a nutshell, it provides infrastructure to execute your CLI available in docker containers:</p>
<ul>
<li>Input and results are automatically downloaded/uploaded from a girder instance</li>
<li>API endpoint to allow remote execution are generated for each CLI</li>
<li>WebUI is also generated for you based on the XML description</li>
<li>Both Cpp and Python based CLIs are supported</li>
<li>Execution is distributed to available worker nodes. Note that database, webserver and worker nodes can all “live” on the same server</li>
</ul>

---

## Post #4 by @cdeepakroy (2017-05-16 21:36 UTC)

<p>Adding onto what <a class="mention" href="/u/jcfr">@jcfr</a> said, take a look at this repo – <a href="https://github.com/cdeepakroy/slicer_cli_web_plugin" rel="nofollow noopener">https://github.com/cdeepakroy/slicer_cli_web_plugin</a> – that demonstrates how to package a bunch of slicer CLIs to be accessed over the web through slicer_cli_web.</p>
<p>It contains one python and one c++ sample CLI (see Applications folder). Developers need to write a slicer_cli_list.json (see Applications folder) file listing the CLIs to be exposed and write the <a href="https://github.com/cdeepakroy/slicer_cli_web_plugin/blob/master/Dockerfile" rel="nofollow noopener">Dockerfile</a> with commands to install/build all pre-requisites and libraries needed by the CLIs.</p>
<p>All the functionality within slicer_cli_web is being integrated into the <a href="http://girder.readthedocs.io/en/latest/plugins.html#automatic-configuration-of-item-tasks-via-docker" rel="nofollow noopener">item tasks plugin</a> of girder.</p>

---
