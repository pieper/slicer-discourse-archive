# Reload data via UI

**Topic ID**: 26204
**Date**: 2022-11-11
**URL**: https://discourse.slicer.org/t/reload-data-via-ui/26204

---

## Post #1 by @Karl_Hahn (2022-11-11 20:14 UTC)

<p>Hello,</p>
<p>Is there already a way to reload data from disk?</p>
<p>Example use case would be to load a scene in slicer containing (say) a model, run some external tool that modifies that mesh, and reload and inspect the result in slicer.</p>

---

## Post #2 by @gcsharp (2022-11-11 20:22 UTC)

<p>Not that I know of.  I think you’d need to use python.</p>
<p>Personally I think this would be super useful.  For example a “reload” context menu item on the Data module.</p>

---

## Post #3 by @Karl_Hahn (2022-11-11 20:24 UTC)

<blockquote>
<p>For example a “reload” context menu item on the Data module.</p>
</blockquote>
<p>Exactly. Agreed that it would be invaluable to have this functionality out of the box.</p>

---

## Post #4 by @lassoan (2022-11-11 20:42 UTC)

<p>Using CLI module infrastructure for launching external tools is much more versatile and user-friendly (you may just need to write a wrapper Python script that launches the tool -  see example <a href="https://github.com/lassoan/SlicerPythonCLIExample/blob/master/BlurImage/BlurImage.py">here</a>).</p>
<p>You can also make Slicer to update/load data using the Web Server API from any Python script <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html#usage-via-slicerio-python-package">using the slicerio Python package</a>. For example, you can run this Python command in your external tool to load the result image into Slicer:</p>
<pre><code class="lang-python"># Prerequisite: pip install slicerio
import slicerio.server
slicerio.server.file_load("c:/tmp/MRHead.nrrd")
</code></pre>
<p>Then you don’t need to switch to Slicer, find the data node in the tree that you want to update, right-click on it, and choose Refresh, but it would be all automatic.</p>
<p>We could add a command for updating a node from a file, something like <code>slicerio.server.file_load("c:/tmp/MRHead.nrrd", "MyVolumeNode")</code> could update the node named “MyVlumeNode” with the content of the provided file.</p>

---

## Post #5 by @Karl_Hahn (2022-11-11 21:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the example. <code>slicerio</code> seems like it could indeed facilitate the use case described. Unfortunately, I’m unable to get it working.</p>
<p>Running below gives following results:</p>
<pre><code class="lang-auto">slicerio.server.file_load(r"...\mesh.ply", slicer_executable=r"...\path\to\Slicer.exe")
</code></pre>
<ul>
<li>5.0.3: application starts, but nothing loaded; eventually receive <code>requests.exceptions.ConnectTimeout: Timeout while waiting for application to start</code></li>
<li>5.1.0 nightly: <code>AttributeError: 'WebServerLogic' object has no attribute 'enableCORS'</code></li>
</ul>
<blockquote>
<p>We could add a command for updating a node from a file</p>
</blockquote>
<p>I think that would be helpful, indeed.</p>
<p>Edit:<br>
Just saw in <code>slicerio.server.start_server</code> that version 5.2 is required…</p>

---

## Post #6 by @pieper (2022-11-11 21:54 UTC)

<p><a class="mention" href="/u/karl_hahn">@Karl_Hahn</a> Are you able to start the web server manually with the GUI for either version?  The server is working for me with both 5.0.3 and my local build of the main github branch.</p>

---

## Post #7 by @Karl_Hahn (2022-11-11 22:08 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, I seem to be able to do so.</p>
<p>In 5.0.3, via the <code>Web Server</code> module, choosing “Start server”:</p>
<pre><code class="lang-auto">Server stopped.
Starting server on port 2016
docroot: b'C:/ProgramData/NA-MIC/Slicer 5.0.3/bin/../lib/Slicer-5.0/qt-scripted-modules/Resources/docroot'
started httpserver...
listening on 3928...
</code></pre>
<p>After doing this, I then naively attempted to run the following in an external script:</p>
<pre><code class="lang-auto">slicerio.server.file_load(
    file_path=r"...\path\to\mesh.ply",
    file_type='ModelFile',
    properties=dict(name='mesh')
)
</code></pre>
<p>Nothing seems to load in the UI. I do, however, see that the HTTP server received a request and processed it without reporting an error.</p>
<p>Is this a valid use case?</p>
<p>Edit:<br>
Running instead:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicerio.server.is_server_running()
False
</code></pre>

---

## Post #8 by @Karl_Hahn (2022-11-11 22:20 UTC)

<p>Happily, repeating the above in a 5.1.0 nightly produces the expected result.</p>
<p>In this case, manually starting the web server prompted for a windows firewall exception to be created. This same thing did not happen for 5.0.3.</p>
<p>Edit:<br>
After manually removing all firewall entries for slicer, I restarted 5.0.3 and received the prompt for firewall exception. Unfortunately, <code>slicerio.server.file_load</code> still has no effect despite the server apparently processing the request.</p>

---

## Post #9 by @Karl_Hahn (2022-11-11 22:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Ran into an issue, but perhaps it’s better discussed in a GitHub <a href="https://github.com/lassoan/slicerio/issues/3" rel="noopener nofollow ugc">issue</a>. Thanks for your help!</p>

---

## Post #10 by @lassoan (2022-11-11 23:07 UTC)

<p>This all requires recent Slicer Preview Release (or the new stable release 5.2 that will be out in a few days). I don’t think Slicer 5.0.3 supports the necessary commands.</p>

---

## Post #11 by @lassoan (2022-11-12 03:36 UTC)

<p>I’ve fixed the CORS error message and the node deletion issue that was reported in GitHub.</p>
<p>I’ve also added a function to slicerio (0.1.8) to reload an already loaded node (in case the file is changed on disk):</p>
<pre><code class="lang-python">nodeID = slicerio.server.file_load("path/to/Segmentation.seg.nrrd", "SegmentationFile")
# ... some changes are made in the file, make Slicer reload the node from the modified file
slicerio.server.node_reload(id=nodeID)
</code></pre>

---

## Post #12 by @Karl_Hahn (2022-11-12 07:44 UTC)

<p>Awesome, looking forward to checking it out. Thanks for your help!</p>

---
