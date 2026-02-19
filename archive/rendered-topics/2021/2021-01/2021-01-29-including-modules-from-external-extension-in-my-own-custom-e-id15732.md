---
topic_id: 15732
title: "Including Modules From External Extension In My Own Custom E"
date: 2021-01-29
url: https://discourse.slicer.org/t/15732
---

# Including modules from external extension in my own custom extension

**Topic ID**: 15732
**Date**: 2021-01-29
**URL**: https://discourse.slicer.org/t/including-modules-from-external-extension-in-my-own-custom-extension/15732

---

## Post #1 by @DhruvKoolRajamani (2021-01-29 04:24 UTC)

<p>I’m working on creating a Slicer Extension that combines various modules available in slicer and the nvidia segmentation tool, all in one extension. I’m not sure how I can include the widgets and logic created by the nvidia AIAA in my own extension as it is an external extension of its own. I’m currently considering using ExternalProject to pull the ai-assisted-annotation repository and link my logic to the segmentation tools in that extension, but I would rather just use the already made slicer extension widgets in my extension.</p>
<p>Module type - loadable module<br>
Language - C++</p>

---

## Post #2 by @lassoan (2021-01-29 04:55 UTC)

<p>You can use the <a href="https://github.com/KitwareMedical/SlicerCAT">Slicer custom application template</a>. You just need specify the extensions you want to include in your application in the top-level CMakeLists.txt file and the build system takes care of everything (download, build, package into your custom application):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/KitwareMedical/SlicerCAT/blob/master/CMakeLists.txt#L131-L142" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerCAT/blob/master/CMakeLists.txt#L131-L142" target="_blank" rel="noopener">KitwareMedical/SlicerCAT/blob/master/CMakeLists.txt#L131-L142</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="131" style="counter-reset: li-counter 130 ;">
<li># Add remote extension source directories</li><li># SlicerIGT</li><li>set(extension_name "SlicerIGT")</li><li>set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")</li><li>FetchContent_Populate(${extension_name}</li><li> SOURCE_DIR     ${${extension_name}_SOURCE_DIR}</li><li> GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/slicerigt/slicerigt.git</li><li> GIT_TAG        origin/master</li><li> GIT_PROGRESS   1</li><li> QUIET</li><li> )</li><li>list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @DhruvKoolRajamani (2021-01-29 13:37 UTC)

<p>Thank you for pointing me to the right location. Is the FetchContent macro also supposed to build the extension before continuing with the next steps? This is the modified code I’m trying out but I don’t see any generated libraries or build configurations.</p>
<pre><code class="lang-auto">include(FetchContent)
set(extension_name "SegmentEditorNvidiaAIAA")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}/slicer-plugin")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/NVIDIA/ai-assisted-annotation-client.git
  GIT_TAG        origin/master
  GIT_PROGRESS   1
  PREFIX         ${CMAKE_BINARY_DIR}/${extension_name}
  BINARY_DIR     ${CMAKE_BINARY_DIR}/${extension_name}-build
  INSTALL_DIR    ${CMAKE_BINARY_DIR}/${extension_name}
  BUILD_ALWAYS   True
  CMAKE_ARGS     -DNvidiaAIAssistedAnnotation_BUILD_SLICER_EXTENSION:BOOL=ON
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})
</code></pre>
<p>Also, do scripted modules also generate include headers and linker targets for C++ code? Or will I need to create a scripted module to include the widgets and logic from a scripted module? I have created a c++ loadable module for my purpose.</p>

---

## Post #4 by @lassoan (2021-01-29 14:42 UTC)

<p>Yes, the extension is downloaded and built automatically.</p>
<p>There is nothing to generate for scripted modules, they are just copied and packaged.</p>
<p>If you think that something is not right then you can print all CMake variables as shown <a href="https://stackoverflow.com/questions/9298278/cmake-print-out-all-accessible-variables-in-a-script">here</a> to see what exactly is going on.</p>

---

## Post #5 by @DhruvKoolRajamani (2021-02-01 03:03 UTC)

<p>Hi Andras, thanks for helping out. While FetchContent didn’t work with the NvidiaAIAA extension, I managed to get it working by adding it as a submodule in my own extension and only building the NvidiaAIAA module via an add_subdirectory command. This is primarily because my own extensions CMAKE variables were overriding the Nvidia ones (since CMAKE was populating my extensions variables first).</p>
<p>I do have a follow up question now - I don’t understand how I can use the NvidiaAIAA modules widget and logic in my C++ loadable extension. With any other module, I can simply include the module widget using the QT designer ui file, and connect it to the widgets logic using the application logic. I then link my module to the respective logic (vtkSlicer{ModuleName}Logic) associated with it. I don’t understand how I can do this with a scripted module. Is the process the same? I add the ui resource and use SlicerApplicationLogic to find the NvidiaAIAA module logic?</p>

---

## Post #6 by @lassoan (2021-02-01 05:46 UTC)

<aside class="quote no-group" data-username="DhruvKoolRajamani" data-post="5" data-topic="15732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dhruvkoolrajamani/48/8799_2.png" class="avatar"> DhruvKoolRajamani:</div>
<blockquote>
<p>I don’t understand how I can use the NvidiaAIAA modules widget and logic in my C++ loadable extension</p>
</blockquote>
</aside>
<p>You can either put a qMRMLSegmentEditorWidget in your module GUI (you can specify in your widget which effects you want to show) or call Python from C++ (search for “pythonmanager” in Slicer source code for examples).</p>

---

## Post #7 by @DhruvKoolRajamani (2021-02-10 05:05 UTC)

<p>Hi Andras,</p>
<p>Thanks for helping out before, I ended up using the low level C++ Nvidia API itself instead of using the python extension. I got the code building and I was able to create a client. However, when I try to create a session, I receive a BAD REQUEST error from the underlying curl command (curlutils.cpp), I even tried using the binary built by the nvidia aiaa tool itself to create a session (nvidiaAIAASession is the binary file) and that returned the same error.</p>
<p>The server I’m using is the perk lab one: <code>http://skull.cs.queensu.ca:8123</code></p>
<p>With it, I’m using a generic image that is saved as a compressed NIftI image (.nii.gz). The image is valid and loads/saves on Slicer.</p>
<pre><code class="lang-auto">23:50:38 [ERROR] [curlutils.cpp:145 - doMethod()] I/O error: Broken pipe
nvidia::aiaa::exception =&gt; nvidia.aiaa.error.101; description: Failed to communicate to AIAA Server
</code></pre>

---

## Post #8 by @lassoan (2021-02-10 14:58 UTC)

<p>In recent Nvidia API they accidentally broke compatibility with v2 servers (see <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/62" class="inline-onebox">Slicer default server needs an upgrade to latest version of AIAA/Clara · Issue #62 · NVIDIA/ai-assisted-annotation-client · GitHub</a>). You either need to downgrade to an earlier version or set up your own Clara v3 server.</p>

---

## Post #9 by @DhruvKoolRajamani (2021-02-11 01:23 UTC)

<p>Thank you! This definitely helps. I would be alright with setting up our own server, however, the requirements to setup a server seem daunting. I was wondering if the inference for the server can be performed on a Nvidia Jetson? Or is it necessary for me to setup a workstation with a dGPU with 8gb of ram for just inference?</p>

---

## Post #10 by @DhruvKoolRajamani (2021-02-11 02:01 UTC)

<p>I also didn’t fully understand what you meant by downgrade to an earlier version. Should I use an earlier version of the ai-annotation-client itself? I tried building against multiple previous commits dating all the way back to Feb 27th 2020. (f0cfc5e). Should I revert to an older commit?</p>

---

## Post #11 by @lassoan (2021-02-11 02:21 UTC)

<aside class="quote no-group" data-username="DhruvKoolRajamani" data-post="9" data-topic="15732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dhruvkoolrajamani/48/8799_2.png" class="avatar"> DhruvKoolRajamani:</div>
<blockquote>
<p>I would be alright with setting up our own server, however, the requirements to setup a server seem daunting.</p>
</blockquote>
</aside>
<p>Setting up the server for anyone who is familiar with linux and docker is probably trivial, but for me it took about a day. I don’t know if it really has to be this complicated, but it is.</p>
<aside class="quote no-group quote-modified" data-username="DhruvKoolRajamani" data-post="9" data-topic="15732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dhruvkoolrajamani/48/8799_2.png" class="avatar"> DhruvKoolRajamani:</div>
<blockquote>
<p>I was wondering if the inference for the server can be performed on a NVidia Jetson? Or is it necessary for me to setup a workstation with a dGPU with 8gb of ram for just inference?</p>
</blockquote>
</aside>
<p>NVidia recommends 16GB GPU RAM. I have set up the Slicer server with a 2080 RTX (8GB RAM) and most models that were shipped with Clara 2 work, but the models come with Clara 3 are keep crashing. People who create models for Clara probably don’t care too much about reducing the memory needs but assume 16GB available.</p>
<aside class="quote no-group" data-username="DhruvKoolRajamani" data-post="10" data-topic="15732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dhruvkoolrajamani/48/8799_2.png" class="avatar"> DhruvKoolRajamani:</div>
<blockquote>
<p>I tried building against multiple previous commits dating all the way back to Feb 27th 2020.</p>
</blockquote>
</aside>
<p>NVidia AIAA client of February 2020 should be OK. You should not need to build anything, it is just a Python API.</p>

---

## Post #12 by @DhruvKoolRajamani (2021-02-11 02:31 UTC)

<p>Thanks again</p>
<blockquote>
<p>NVidia recommends 16GB GPU RAM. I have set up the Slicer server with a 2080 RTX (8GB RAM) and most models that were shipped with Clara 2 work, but the models come with Clara 3 are keep crashing. People who create models for Clara probably don’t care too much about reducing the memory needs but assume 16GB available.</p>
</blockquote>
<p>I see, this is a discussion I would need to bring up with my advisor and have no control over it now unfortunately. It would be really helpful to use the server endpoint available at the PERK Lab to prototype.</p>
<blockquote>
<p>NVidia AIAA client of February 2020 should be OK. You should not need to build anything, it is just a Python API.</p>
</blockquote>
<p>As I mentioned before, I was coming across a lot of issues while trying to integrate the python API. I instead went ahead with integrating the C++ API itself, which was available from the C++ client. Since the task requires me to only use Dext3D, I went ahead with providing the appropriate Markups widget and logic to get that working.</p>
<p>I’m still getting the same error which points to a broken IO Pipe with the Feb 2020 build. I even tried directly using the compiled binary file for NvidiaAIAASession to test if a session is even created with a compressed NIftI image. I’ll try using older commits I guess.</p>
<p>Another option for me would be to not include the AIAA Segmentation in my extension and force the user to navigate to the segmentations module and segment the region, then feed the segmentations node back into my module. While that is a possibility, I wasn’t even able to get the AIAA through the extension wizard with the same PERK Lab server endpoint with the developer build for slicer. Since my module and extension are a loadable C++ module, I’m not sure if I can build my extension against the binary release for slicer to allow the user to use the Nvidia Segmentation tool from the segment editor.</p>

---

## Post #14 by @Saima (2022-03-09 00:20 UTC)

<p>Hi andras,<br>
Is there a way to get widgets and logics of already available python scripted modules in a new extension. I want to combine all my scripted modules under one extension and on one page with different tabs like below. Each tab with a different python scripted modules already in 3 D Slicer.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7313de5eb5a0183ab79d54bfd04cea7797fa8060.png" alt="image" data-base62-sha1="gq1tBjT4iFqPqWHX4Flg7KA6fgQ" width="486" height="96"></p>

---
