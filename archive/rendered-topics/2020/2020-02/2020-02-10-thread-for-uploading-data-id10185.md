# Thread for uploading data

**Topic ID**: 10185
**Date**: 2020-02-10
**URL**: https://discourse.slicer.org/t/thread-for-uploading-data/10185

---

## Post #1 by @tbuikr (2020-02-10 15:30 UTC)

<p>Thanks for great SDK and python support.</p>
<p>I am using python and Slicer to upload dicom file to my server using <code>requests.post</code>. My dicom size about 20MB and it takes 1 mins to upload it to server.</p>
<p>During uploading process, the application only runs one thread, so I cannot do other tasks (GUI blocked). Could we create another thread for data uploading and run it on other thread, instead of main thread (GUI)? Do we have any example for the task? Thanks</p>

---

## Post #2 by @pieper (2020-02-10 15:48 UTC)

<p>Probably the easiest is to save the data to a file and then use <code>subprocess.run</code> or <code>QProcess</code> to execute a little script that does the upload (you can execute it with <code>PythonSlicer</code> which will be in your path and can run the same python scripts (non-gui) as you would inside slicer).</p>
<p>Are you connecting to a dicomweb server using dicomweb_client or directly via requests?</p>

---

## Post #3 by @tbuikr (2020-02-10 16:00 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="10185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>subprocess.run</p>
</blockquote>
</aside>
<p>I just directly use request function in python. My data is dump to file and write to buffer to send to a web-service.</p>
<p>My function such as</p>
<pre><code class="lang-auto">def send_data():
   with open(path_to_dcm, 'rb') as file:
        file_read = file.read()
        base64_encode = base64.encodebytes(file_read)         
        multipart_form_data = {
              'file': (path_to_dcm, base64_encode, 'dicom')
          }
        try:
            json_results = requests.post(my_url,
                                    files=multipart_form_data)
            return json_results.json()
        except:
            pass
</code></pre>
<p>The <code>send_data </code> is called when I click the <code>Send</code> button such as</p>
<pre><code class="lang-auto">       self.sendButton = qt.QPushButton("Send")
       self.sendButton.connect("clicked()", self.onSend)

def onSend(self):
    send_data()

</code></pre>
<p>Could you give an example how to do <code>subprocess.run</code> or <code>QProcess</code>?</p>

---

## Post #4 by @pieper (2020-02-10 19:48 UTC)

<p>Here’s an example with subprocess to run a job:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/91acb6167cdda31bfdc18bd752a85c6420462885/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1281" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/91acb6167cdda31bfdc18bd752a85c6420462885/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1281" target="_blank">Slicer/Slicer/blob/91acb6167cdda31bfdc18bd752a85c6420462885/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1281</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="1271" style="counter-reset: li-counter 1270 ;">
<li>                  "-y", # overwrite without asking</li>
<li>                  "-r", str(frameRate),</li>
<li>                  "-start_number", "0",</li>
<li>                  "-i", str(filePathPattern)]</li>
<li>  ffmpegParams += [_f for _f in extraOptions.split(' ') if _f]</li>
<li>  ffmpegParams.append(outputVideoFilePath)</li>
<li>
</li>
<li>  self.addLog("Start ffmpeg:\n"+' '.join(ffmpegParams))</li>
<li>
</li>
<li>  import subprocess</li>
<li class="selected">  p = subprocess.Popen(ffmpegParams, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=outputDir)</li>
<li>  stdout, stderr = p.communicate()</li>
<li>  if p.returncode != 0:</li>
<li>    self.addLog("ffmpeg error output: " + stderr.decode())</li>
<li>    raise ValueError("ffmpeg returned with error")</li>
<li>  else:</li>
<li>    self.addLog("Video export succeeded to file: "+outputVideoFilePath)</li>
<li>    logging.debug("ffmpeg standard output: " + stdout.decode())</li>
<li>    logging.debug("ffmpeg error output: " + stderr.decode())</li>
<li>
</li>
<li>def deleteTemporaryFiles(self, outputDir, imageFileNamePattern, numberOfImages):</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Also, coincidentally, I’m working on another example for the SlicerMorph project that maybe be closer to your use case.  I hope to publish it soon.</p>

---

## Post #5 by @pieper (2020-02-10 20:38 UTC)

<p>Here’s a more elaborate set of code for doing this sort of thing (new, so use with care).  It you look at the self test you can see what the interface looks like.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/pieper/SlicerProcesses" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/126077?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/pieper/SlicerProcesses" target="_blank">pieper/SlicerProcesses</a></h3>

<p>Slicer modules for running subprocesses to operate on data in parallel - pieper/SlicerProcesses</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Manh_Nguyen (2020-03-22 12:25 UTC)

<p>Hi Steven, I’ve been looking into your project and have some questions:</p>
<p>How can a process modify the GUI written in ScriptedLoadableModuleWidget inherited class ?<br>
If I put a time.sleep(4) in your processing Input code, the GUI is freeze and unable to access or click.</p>
<p>In case I want to use multi-threading to handle the send to server, I got unexpected issue like when I click in the button and the send to server thread does not working at all. Is there any modules with multi-threading code that I can learn from ?</p>
<p>Thanks you very much</p>

---

## Post #7 by @lassoan (2020-03-22 13:43 UTC)

<p>If you want to give a chance for GUI updates while you are doing processing then you need to call slicer.app.processEvents(), not just a sleep.</p>
<p>As you probably know, due to the global interpreter lock, there is no parallel execution of Python code within one interpreter, even if you start multiple threads. For IO operations, asynchronous IO might help, but I don’t know if anyone has figured out how to use that in Slicer.</p>
<p>A simpler solution is to start a separate process for background operations. Fortunately, Slicer already has a very simple solution for this: scripted CLI modules, which are Python scripts that are executed in the background, in a new Python interpreter. If you have a Python script that uploads an input image to a server then all you need to run it in the background in Slicer is to create a simple XML file that describes inputs and outputs of your script - see a complete example <a href="https://github.com/lassoan/SlicerPythonCLIExample">here</a>. The XML file allows Slicer to recognize the script as a CLI module, and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">CLI modules are run in the background by default</a>.</p>
<p>If you start multiple CLI modules in parallel then Slicer puts them in a queue and runs them one after the other.</p>

---

## Post #8 by @Manh_Nguyen (2020-03-22 13:52 UTC)

<p>Thanks you very much for your answers.<br>
The example link you provided above seems not working to me<br>
Anyway, I found some useful reference in this github <a href="https://github.com/Radiomics/SlicerRadiomics/tree/master/SlicerRadiomicsCLI" rel="noopener nofollow ugc">link</a></p>
<p>However, how can I add this CLI modules to my Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3b3f9e2d461d0c2173b360a11677f30ebf61078.png" data-download-href="/uploads/short-url/ucOlhIgRM1ZFZ9ezwygo4S2XG1a.png?dl=1" title="Screenshot from 2020-03-22 20-50-39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3b3f9e2d461d0c2173b360a11677f30ebf61078_2_629x500.png" alt="Screenshot from 2020-03-22 20-50-39" data-base62-sha1="ucOlhIgRM1ZFZ9ezwygo4S2XG1a" width="629" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3b3f9e2d461d0c2173b360a11677f30ebf61078_2_629x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3b3f9e2d461d0c2173b360a11677f30ebf61078.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3b3f9e2d461d0c2173b360a11677f30ebf61078.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-03-22 20-50-39</span><span class="informations">814×647 99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec6557b24fc1c61d01909ff0dabaa39ada5e89a7.png" alt="Screenshot from 2020-03-22 20-50-45" data-base62-sha1="xJfO7KQqLeeHj8ZQNFZogsYkJdJ" width="639" height="131"><br>
This seems not working at all ? Seems like I missed some steps ? Can you show me some instruction into this ?<br>
Again, thank you very much for your help.</p>

---

## Post #9 by @lassoan (2020-03-22 14:04 UTC)

<p>I confirm that the module that I linked works well with recent Slicer-4.11 versions. If you have any problems running it then describe what steps you performed, what you expected to happen, and what happened instead.</p>

---

## Post #10 by @Manh_Nguyen (2020-03-22 14:25 UTC)

<p>So these are steps that I followed:</p>
<ul>
<li>Clone the git project from <a href="https://github.com/Radiomics/SlicerRadiomics" rel="noopener nofollow ugc">here</a></li>
<li>Add the modules inside Slicer: Application Settings → Modules → Add → <strong>SlicerRadiomicsCLI</strong></li>
<li>Run some experiment code:</li>
</ul>
<blockquote>
<p>parameters = {}<br>
res = slicer.cli.runSync(slicer.modules.SlicerRadiomicsCLI, None, parameters)<br>
print(res)<br>
pass</p>
</blockquote>
<p>So are there anything need to be additionally performed ? The version I used is Slicer 4.11 (I think my Slicer is not nightly version since I downloaded the binary in the main page)</p>
<p>The way I want it to work is I’m able to access slicer.modules.SlicerRadiomicsCLI CLI from the scripted code python that I wrote.</p>

---

## Post #11 by @lassoan (2020-03-22 15:58 UTC)

<p>OK, what you do will work, just use the example that I provided above: <a href="https://github.com/lassoan/SlicerPythonCLIExample">https://github.com/lassoan/SlicerPythonCLIExample</a></p>

---

## Post #12 by @Manh_Nguyen (2020-03-27 09:10 UTC)

<p>Sorry for the late response. Do I need to runSync CLI modules in separated file ? The BlurImage CLI seems still frozen GUI when I add time.sleep(5) into BlurImage.py</p>
<p>Btw, the SlicerProcesses works pretty well. However, is there any way to monitor the progress of the process run in background ?</p>
<p>Many thanks for yours support</p>

---

## Post #13 by @lassoan (2020-03-27 12:08 UTC)

<p>RunSync blocks the main thread until the execution completes, so don’t use it of you want to process in the background.</p>

---

## Post #14 by @pieper (2020-03-27 12:35 UTC)

<aside class="quote no-group" data-username="Manh_Nguyen" data-post="12" data-topic="10185">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/manh_nguyen/48/6327_2.png" class="avatar"> Manh_Nguyen:</div>
<blockquote>
<p>Btw, the SlicerProcesses works pretty well. However, is there any way to monitor the progress of the process run in background ?</p>
</blockquote>
</aside>
<p>The current SlicerProcesses code isn’t set up for progress reporting.  There could be lots of ways to do it,  Slicer CLI modules use a convention of embedding xml snippets in the output that triggers automatic progress updates in the GUI.  Another option would be to set up a connection like OpenIGTLink to pass data.  Or one could create a custom network protocol.</p>

---
