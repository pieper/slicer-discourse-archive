# Slicer custom application deployment to many computers

**Topic ID**: 18019
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/slicer-custom-application-deployment-to-many-computers/18019

---

## Post #1 by @spycolyf (2021-02-11 15:59 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/superlib">@superlib</a></p>
<p>Good Morning. I’m starting to think about how to deploy SlicerQR to 25,000 PCs across the Mayo Enterprise. After building the package, it consists of over 7000 files at a total size of over 700MB. It would be seriously frowned-upon to propose deploying it to 25,000 PCs. So, my question is: Would there be any disadvantages to placing the installation in 1 place on a file share and have the users execute SlicerQR from a folder there? Would there be conflicts with sharing? Once the app is loaded into local memory, what are potential problems with a common launch path?</p>

---

## Post #2 by @spycolyf (2021-02-11 16:18 UTC)

<p>Hello <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/superlib">@superlib</a></p>
<p>Could you grant <a class="mention" href="/u/liqin">@Liqin</a> access to the SlicerQR repository? She is the technical specialist for this project and will need to begin reading through and understanding the code ASAP. Thank you.</p>

---

## Post #3 by @lassoan (2021-02-11 17:15 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="1" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>After building the package, it consists of over 7000 files at a total size of over 700MB. It would be seriously frowned-upon to propose deploying it to 25,000 PCs.</p>
</blockquote>
</aside>
<p>Probably this could be reduced to about half size by removing parts that are not needed, but I guess it would not change things significantly.</p>
<p>Running Slicer from a shared network drive would have many advantages (for example, it would be much easier to handle automatic updates), but it would be very bad if users would need to download the viewer from scratch for viewing data.</p>
<p>A good solution could be to install just a launcher on each computer, which would be responsible for automatically copying of Slicer files from the shared folder to a local cache and launch it  when needed (no installation is needed, Slicer can run from any writeable folder). The launcher would be a small standalone application (if built with static Qt then it would be a few MB, if built with dynamically-linked Qt then it would be a few ten MB). If someone does not need the 3D viewer then the full Slicer would never be copied to the computer. The launcher could show download progress, handle automatic updates (check if the locally cached version is the same as in the shared folder and offer to upgrade), custom URLs (so that Slicer could be launched from a werb browser) and file associations (e.g., Slicer could be launched when the user wants to open a .dcm, .nrrd, … file).</p>

---

## Post #4 by @spycolyf (2021-02-11 17:44 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I’m a bit confused. Please allow me to clarify.</p>
<p>Currently, I can run the SlicerQR slicelet from a fileserver. I copied the folder tree to a folder on the file server and mapped it to drive S:. When I, launch SlicerQR like this…</p>
<pre><code class="lang-auto">S:
cd SlicerQREADS
SlicerQReads.exe --python-code "folder='S:\SlicerQREADS\TestImages'; import os; slicer.util.loadVolume(folder + '/' + os.listdir(folder)[0], {'singleFile': False})"
</code></pre>
<p>This works fine without copying the files locally.</p>
<p>Will this be OK for 25000 potential users? Actually, probably about 5000 simultaneous users max.</p>

---

## Post #5 by @lassoan (2021-02-11 17:52 UTC)

<p>Simply running from a read-only shared location has these disadvantages:</p>
<ul>
<li>Launching Slicer can take much longer if the files have to be fetched each time from a remote server</li>
<li>Users cannot install extensions that dynamically download and install additional Python packages</li>
</ul>
<p>If you don’t allow your users to install extensions and startup time is not critical (or your network is very fast and/or local file caching works very efficiently) then these limitations might not be a problem for you.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="4" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Will this be OK for 25000 potential users? Actually, probably about 5000 simultaneous users max.</p>
</blockquote>
</aside>
<p>Size of the Slicer installation is comparable with size of a patient image, so if your servers can already handle image download requests from 5000 users then I would assume that they can handle Slicer downloads as well. However, this download is clearly a burden that could be avoided by setting up local caching. If you don’t want to create a custom launcher/downloader then you can check what caching is available at the operating system level. It may be possible to set up local caching of a shared network folder (maybe even persistent cache, which is kept when the computer is restarted) or you may leverage other file sharing services (sharepoint, onedrive, etc.) that your organization already uses.</p>

---

## Post #6 by @spycolyf (2021-02-11 18:10 UTC)

<p>Cool! Thanks <a class="mention" href="/u/lassoan">@lassoan</a> ! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @jcfr (2021-02-12 19:36 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="1" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>After building the package, it consists of over 7000 files at a total size of over 700MB</p>
</blockquote>
</aside>
<p>Here are few approach we could evaluate:</p>
<ul>
<li>statically link loadable module into the application</li>
<li>statically integrate <code>PythonQt</code> module that are currently dynamically loaded</li>
<li>statically link against external dependency like ITK, VTK, DCMTK, …</li>
<li>harden the current python integrate into C++ and remove the use of python</li>
</ul>
<p>That said, before investing resources to support this, we should consider:</p>
<ul>
<li><a class="mention" href="/u/lassoan">@lassoan</a> comment regarding size of images vs size of the application</li>
<li>performing additional bench-marking for startup time and define which target time we aim (Initial profiling by <a class="mention" href="/u/pieper">@pieper</a> concluded that shared library loading was at fault)</li>
</ul>

---

## Post #8 by @pieper (2021-02-13 16:02 UTC)

<p>This is turning into a very interesting topic, since it’s not unusual for custom apps to be concerned about the size of the distribution, startup time, and “time to first image”, so Doug’s project will have extra side benefits.</p>
<p>I wouldn’t suggest this for every computer, but for heavy users who want instant display one could leave the app running so it could respond instantly.  It could even auto-start at login (to be used with care, since this kind of auto-run can really bog down the login process).</p>
<p><a class="mention" href="/u/spycolyf">@spycolyf</a> can you give us any benchmarks about other apps that are distributed to the 25,000 Mayo computers?  How big are the installations?  How fast do they start up?</p>

---

## Post #9 by @spycolyf (2021-02-17 18:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>Sorry for the delay, I had to meet with Mayo legal about its involvement in opensource software. Bottom line, to indicate on the repository GitHub page and documentation that it’s a Mayo collaboration and that “Mayo is a contributor” to any opensource project is totally fine and the use of the QREADS brand is approved as well.</p>
<p>Anyway, about the startup times, are you asking about benchmarks for imaging apps in particular? The main QREADS competitor image viewers are Visage and ResMD. MPR is embedded into those apps. My goal with QREADS is to make SlicerQREADS seem as if is a part of QREADS. When the user right-mouse clicks on a CT scan image for example, a menu pops up and then they select SlicerQREADS. My goal is to make the user experience a seamless transition from QREADS to SlicerQREADS as though SlicerQREADS is a popup from the QREADS menu item selection. If we can get it to come up in 10 seconds, that would be within the range of acceptability.</p>

---

## Post #10 by @pieper (2021-02-17 19:20 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="9" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>If we can get it to come up in 10 seconds, that would be within the range of acceptability.</p>
</blockquote>
</aside>
<p>That’s very helpful as a target. Some of the things Jc mentioned can certainly help towards this.  It may also be possible to start scrolling the axials as they arrive and then snap to MPR once the volume is complete (or something similar so the user doesn’t just see a blank screen and get bored).</p>
<p>Also glad you cleared with legal.  Mayo has a great tradition of contributions to open source but it’s always good to confirm.</p>

---

## Post #11 by @lassoan (2021-02-17 20:11 UTC)

<p>Warm start (starting Slicer if it was launched recently) takes about 10 seconds on my computer but cold startup can take 2-3x more. We may be able to reduce the cold startup time to around 10 seconds, but it would be probably more comfortable to keep Slicer open after it is started because the user would still need to wait for DICOM loading.</p>
<p>The wait time for the user might be also reduced if Slicer startup overlaps with the network transfer of the images.</p>

---

## Post #12 by @spycolyf (2021-02-17 22:06 UTC)

<p>Images will be stored locally by the time the user selects the SlicerQREADS menu item on the image menu. And of course it depends on the size of the series. So, I’d like to pursue keeping slicer up after the first use. So, how would the user experience work? Would it minimize after pushing the close button and restore when the QREADS menu item is selected again? If so, how would QREADS communicate with SlicerQREADS while it’s stays open? Some type of inter-process communication?</p>

---

## Post #13 by @pieper (2021-02-17 22:44 UTC)

<p>Yes, Slicer could just close its windows and go into background mode with a port open so that it could get awaked by, say, an http request with parameters about where to load the data and optionally what view to display.  Then it would open its windows back up.  For heavy users Slicer could be started at login so even their first request is serviced quickly.</p>

---

## Post #14 by @spycolyf (2021-02-18 15:54 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Sounds wonderful Steve! Is this a current Slicer feature? I’d like to try it before my presentation to the Apps Oversight Committee on March 4th if possible.</p>
<p>Thanks</p>

---

## Post #15 by @pieper (2021-02-18 17:39 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="14" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Is this a current Slicer feature?</p>
</blockquote>
</aside>
<p>It’s “sort of” a current feature in the sense that there are existing prototypes and everything needed can be accomplished with a minimal amount python to customize behavior.  There are several options and you’d want to decide what would work best.</p>
<p>A working example is demoed in <a href="https://www.youtube.com/watch?v=vTGQMDIqL9k">this video</a>.  There’s some preamble about how the teamplay system works where the study is selected, etc.  Then when the Slicer button is pressed, the teamplay app creates a json file with the information about the study to load together with the security tokens and it posts it to a url.  This triggers a slicer instance to read and display the corresponding study.</p>
<p>If you are working on the user’s local machine, where you can have direct access to the URL and the data, you could use <a href="https://github.com/pieper/SlicerWeb">SlicerWeb</a> with the repl (read-eval-print-loop) endpoint, which allows arbitrary code execution.</p>
<p>For example:</p>
<p><code>curl -X POST localhost:2016/slicer/repl --data "import SampleData; SampleData.SampleDataLogic().downloadMRHead(); slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpYellowSliceView)"</code></p>
<p>Makes this image appear:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1944a874f02c87439c7be155d1a6e083d6de210d.jpeg" data-download-href="/uploads/short-url/3Bx2e54j2T9ydLKOxMxxESZb7Mp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1944a874f02c87439c7be155d1a6e083d6de210d_2_345x155.jpeg" alt="image" data-base62-sha1="3Bx2e54j2T9ydLKOxMxxESZb7Mp" width="345" height="155" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1944a874f02c87439c7be155d1a6e083d6de210d_2_345x155.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1944a874f02c87439c7be155d1a6e083d6de210d_2_517x232.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1944a874f02c87439c7be155d1a6e083d6de210d_2_690x310.jpeg 2x" data-dominant-color="262624"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">864×389 46.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can post any slicer python commands, e.g. to show/hide the main window, load or unload data, switch layout or modules, etc. (obviously don’t expose this port to the internet!)</p>

---

## Post #16 by @spycolyf (2021-02-18 23:10 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thanks Steve, So could you help me with getting SlicerQREADS to do this, or help me to understand that example? It’s very cryptic to me. How can I get SlicerQREADS to do this?</p>

---

## Post #17 by @pieper (2021-02-19 00:45 UTC)

<p>It shouldn’t be too hard to get this approach going, but I don’t know about the QREADS side of the equation.  What language is it written in?  The example uses a linux command line utility but any http package could be used, so my assumption would be you can add a button that sends an http request.  Do you know if/how it can do that?</p>
<p>On the Slicer side you just need to define the operations you want, like show/hide main window, set layout, load and display dicom data, close scene and hide window.  Then it’s just a matter of sending those python commands via the http request.</p>

---

## Post #18 by @lassoan (2021-02-19 03:48 UTC)

<p>While controlling Slicer via web requests would be certainly an elegant and flexible solution, if it is not easy to integrate a http library into QREADS or hospital IT policies does not let an application to open a listening port then there are other options.</p>
<p>A very simple solution is to use files to communicate. QREADS could ask Slicer to load an image by creating a json file in a designated folder. Slicer can set up a QFileSystemWatcher (or use a timer and check for folder changes manually once in every few seconds) and if there is a new file there then read and process it.</p>

---

## Post #19 by @spycolyf (2021-02-19 16:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> Well that’s just it. I don’t know if the web request method is the way to go or not. I am a user experience guy with little web experience, and that’s all that matters to me in the end. I should get one of my experts in this conversation. I do know that QREADS is written in JAVA and is heavily client-server architected and the client communicates with the server via http and https. So, web requests are in. But would this be as fast as local installation, and could Slicer reside on the QREADS server? I will need to get my QRERADS server experts involved.</p>

---

## Post #20 by @lassoan (2021-02-19 17:20 UTC)

<p>Calling web requests should not be an issue then. It should be possible to create a listening socket in Slicer that only accept local connections and that will not require firewall exceptions. So, QREADS sending commands to Slicer view web requests should work well.</p>

---

## Post #21 by @pieper (2021-02-19 18:31 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="22" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"><a href="https://discourse.slicer.org/t/slicerqr-development/15954/22">SlicerQR Development</a></div>
<blockquote>
<p>Question: Do any of you know my friend, Hunter Downs?</p>
</blockquote>
</aside>
<p>Don’t believe I do, no.</p>
<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A very simple solution is to use files to communicate. QREADS could ask Slicer to load an image by creating a json file in a designated folder.</p>
</blockquote>
</aside>
<p>This could also work fine for the local environment, for about the same amount of work.</p>
<aside class="quote no-group quote-post-not-found" data-username="spycolyf" data-post="20" data-topic="15954">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"><a href="https://discourse.slicer.org/t/slicerqr-development/15954/20">SlicerQR Development</a></div>
<blockquote>
<p>Slicer reside on the QREADS server?</p>
</blockquote>
</aside>
<p>No, we were thinking it would still run on the client machine, but controlled by QREADS via an agreed communication protocol.  Running on the server adds more trouble than it’s worth I think.</p>
<p>Either with the web or file based approach <a class="mention" href="/u/spycolyf">@spycolyf</a> you’ll need to map out the interactions you want Slicer to be able to support and come up with a small python script to implement them.</p>

---

## Post #22 by @spycolyf (2021-02-19 19:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A very simple solution is to use files to communicate. QREADS could ask Slicer to load an image by creating a json file in a designated folder.</p>
</blockquote>
</aside>
<p>The best way to do this I think would be via web request. I do have a little experience in that area. Other’s on the team have more, so not a problem. No problem with QREADS sending local web requests. This way, QREADS will be able to continue to run simultaneously with QREADS slicer. However, we will have to manage patient context. We can’t have images displayed in SlicerQREADS that does not belong to the current patient in QREADS. That could cause a sentinel event.</p>
<p>So, that begs the question, which way is safest for the patient?</p>
<p>Ok, so I feel that I’m establishing a clearer direction in which to focus my energies. In either case, would you agree that I will have to study Slicer development? And where should I start my focus? Is this a Python level effort, C++ level, or both?</p>
<p>FYI: here is the command to run SlicerQREADS:</p>
<p>SlicerQReads.exe --python-code “folder=‘S:\SlicerQREADS\TestImageVolumes\TestICTHead_Compressed’; import os; slicer.util.loadVolume(folder + ‘/’ + os.listdir(folder)[0], {‘singleFile’: False})”</p>

---

## Post #23 by @spycolyf (2021-02-22 16:04 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Good morning all, and thank you for your help with everything so far. The Mayo Clinic will definitely benefit from your amazing service and we in the 3D image software development community are fortunate to have you as a resource and to be able to contribute to the community as well.</p>
<p>This morning, I’ve been given my march orders: Get the Slicer installation size down significantly so that QREADS installation will not increase by more than 250%. Currently, the size of a QREADS installation is about 25 to 30MB. Slicer’s size adds another 700+ MB. What is the best way to approach this issue? Should I use the process of elimination by excluding libraries 1 by 1 until it breaks, or is there a more efficient and methodical way to accomplish size reduction? Maybe there’s a way to accurately determine slicelet dependencies. And hopefully, by reducing the size, this along with other methods, will also help reduce Slicer launch times. Thanks.</p>

---

## Post #24 by @spycolyf (2021-02-22 17:50 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>According to this Slicer documentation, the footprint size and launch time can be drastically reduced as described at the bottom of that page. Do you think we could achieve a reasonably small size and launch time with the method described? …</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets#Slicelet_examples" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets#Slicelet_examples</a></p>

---

## Post #25 by @spycolyf (2021-02-22 18:01 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Here are few approach we could evaluate:</p>
<ul>
<li>statically link loadable module into the application</li>
<li>statically integrate <code>PythonQt</code> module that are currently dynamically loaded</li>
<li>statically link against external dependency like ITK, VTK, DCMTK, …</li>
<li>harden the current python integrate into C++ and remove the use of python</li>
</ul>
<p>That said, before investing resources to support this, we should consider:</p>
<ul>
<li><a class="mention" href="/u/lassoan">@lassoan</a> comment regarding size of images vs size of the application</li>
<li>performing additional bench-marking for startup time and define which target time we aim (Initial profiling by <a class="mention" href="/u/pieper">@pieper</a> concluded that shared library loading was at fault)</li>
</ul>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>In the above response, you mentioned “investing resources.” Are you suggesting that the process would be very expensive and time consuming? And <a class="mention" href="/u/jcfr">@jcfr</a>, I think you said that you had done some size reduction already. If so, how much more reduction do you think could be done to SlicerQREADS?</p>
<p>Thanks</p>

---

## Post #26 by @lassoan (2021-02-22 18:17 UTC)

<p>As far as I remember, you told QREADS is a Java application, so it cannot be only 30MB, because the <a href="https://www.oracle.com/java/technologies/javase-jre8-downloads.html">Java runtime itself is between 70-90MB</a>. So, the actual install size is 100-120MB. Anyway, if you are only allowed to add a few ten MB to the install package then probably the best is to only add a launcher to QREADS. The launcher would download the application from a server to a cache folder (so that it does not have to be re-downloaded at each launch). The launcher could also manage automatic updates, keeping Slicer running in the background, etc. The launcher functionality can be either built into the QREADS application or be a small standalone application.</p>
<p>The application package size could be probably brought down to about 400MB (removing QWebEngine, SimpleITK, all unneeded modules) without reengineering. By removing Python, it could be possible to get the install package size to about 200-300MB, but most DICOM readers are implemented in Python, so that would require porting DICOM plugins to Python (or restricting yourself to only basic 2D and 3D read images from DICOM - no DICOM RT information objects, transforms, 4D volumes, etc.). Static linking could probably reduce the package size by an additional 50-100MB, but that would again require some engineering work. Since you download hundreds of megabytes from the image server anyway, I don’t think that it is worth the effort to remove Python. Static linking might be considered, because it not just decreases package size but may also reduce startup time a lot.</p>

---

## Post #27 by @spycolyf (2021-02-22 20:06 UTC)

<p>Thank you for your response Andras. OK, when we install QREADS on the many PCs, the Java runtime is already installed because it’s part of the standard initial Mayo configuration of all PCs. Therefore, for a QREADS deployment, all that is needed is to copy the QREADS jar files and some dlls. It’s about 27 MB when when do a QREADS deployment. And yes, we do use a launcher that manages automatic QREADS updates, so SlicerQREADS would be also included in those updates. My team lead wants to minimize the time the user experiences to start up QREADS when there is a new deployment. But I understand, I think since we probably won’t be updating SlicerQREADS as often as QREADS, we should have separate launcher code for SlicerQREADS that detects new versions and updates.</p>
<p>With that in mind, maybe there’s a way to perform incremental SlicerQREADS updates after the first install. The initial installation could include Python, and many of the needed libraries, but when a modification is made to SlicerQREADS, only the modified files are copied.</p>
<p>Let’s keep this discussion going. I need to give the team a final statement on this Thursday afternoon.</p>

---

## Post #28 by @lassoan (2021-02-22 22:56 UTC)

<p>A good workflow could be to only install/update SlicerQREADS on request, when the user launches a feature that requires it. If Slicer is downloaded then it would be kept in a cache or temporary folder, so next time it would be already there.</p>
<p>Partial updates: Some granularity is already built in, as Slicer core is one big package, and each extension is a small separate package. You can install/uninstall/update extensions without touching Slicer core. If there are specific features that are changing quickly then they could be developed as extensions and can be updated very quickly. However, I would expect that at the beginning we’ll often need Slicer core updates, because we’ll need to improve core features.</p>

---

## Post #29 by @pieper (2021-02-23 00:10 UTC)

<p><a class="mention" href="/u/spycolyf">@spycolyf</a> can you list the core functional requirements for SlicerQREADS?  This will help identify how much code is actually strictly needed out of the Slicer install.</p>

---

## Post #30 by @spycolyf (2021-02-23 17:38 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>OK, JC can be of great help here. He is very familiar with all of the functionality as he was a major contributor to the current project and knows the low level dependencies. Also, I would be willing to cut back on some of the nice features that JC included if it reduces the size significantly. In the meantime, I will get you the functional requirements ASAP.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, could you chime in here?</p>
<p>Thanks.</p>

---

## Post #31 by @pieper (2021-02-23 18:19 UTC)

<p>Some of us chatted about this during the developer hangout earlier today.  Some of the most valuable parts of Slicer are also pretty demanding in terms of disk space.  Even with a lot of trimming and it’s unlikely Slicer will get down below a few hundred megabytes.  If that’s not viable for the Mayo software distribution model you may need to rethink things.</p>
<p>What about the model <a class="mention" href="/u/lassoan">@lassoan</a> suggested where Slicer is optionally installed on-demand to users who need it.  This would mean having an installer as part of QREADS that would download a few hundred megabytes of Slicer binary into a cache that could be re-used quickly after the first install.</p>

---

## Post #32 by @spycolyf (2021-02-23 21:08 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Yes, <a class="mention" href="/u/lassoan">@lassoan</a> suggestion has been a consideration in the past. The size issue will only make a difference in whether we distribute it to all 25,000 PCs or we give the user the option to install or not. If the size were small enough, every user would see the menu choice in QREADS to view the MPR interface. This would be great for discovery. Sorry if I’m too pushy about things; I was just told to pursue the possibility by my team lead and I need as much info as possible for the big Oversight Committee meeting next Thursday Mar 4th. Anyway, we will get the size down as much as possible and we will decide how we will deal with it.</p>
<p>I am currently studying the code to make the last needed changes that I will be demonstrating to the committee. It’s slow, but I think I’m getting through it.</p>
<p>I’m currently in the QREADS.py code. So, wish me luck. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> .</p>

---

## Post #33 by @lassoan (2021-02-23 21:17 UTC)

<p>You can add the shortcut to all workstations. When users start the feature, the launcher shows a progress window, asking users to wait for a few minutes, and that’s it. I would not mind waiting a few minutes for some software to install or self-update time-to-time, especially if it does not block me from working something else in the meantime.</p>

---

## Post #34 by @spycolyf (2021-02-23 22:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>The feature is started from a java DOS shell process command issued from QREADS when the user selects the “3D MPR” menu item in the right mouse button menu of the displayed image. QREADS passes the DICOM folder path and then SlicerQREADS pops up with the selected images loaded. To the user, SlicerQREADS is a modal or nonmodal pop-up window and feels like a part of QREADS. The menu item won’t be enabled is SlicerQREADS is not installed. If we are able to get the size down enough, all users will be able to experience SlicerQREADS with out having to install it. That would be nice, but maybe not possible.</p>

---

## Post #35 by @pieper (2021-02-23 22:46 UTC)

<p>Just for reference, Acrobat Reader on my windows machine takes over 380MB and all it does is documents.  A few hundred more meg to get a 3D medical image system seems more than fair <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=9" title=":laughing:" class="emoji" alt=":laughing:"></p>

---

## Post #36 by @lassoan (2021-02-23 22:55 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="34" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>The feature is started from a java DOS shell process command issued from QREADS when the user selects the “3D MPR” menu item in the right mouse button menu of the displayed image. QREADS passes the DICOM folder path and then SlicerQREADS pops up with the selected images loaded.</p>
</blockquote>
</aside>
<p>This can all work beautifully then, for all users, without preinstalling anything large on the users computer.</p>
<p>We just need to create a “launcher”, which would either be a new class in QREADS implemented in Java, or a 5-10MB statically-built Qt application (that is bundled with QREADS package). This component performs the followings:</p>
<ul>
<li>display a progress bar immediately when SlicerQREADS start is requested</li>
<li>download/update the 400-500MB SlicerQREADS package (show progress bar, maybe ask the user if he wants to install/update now)</li>
<li>launch Slicer executable and pass information about what data set to load; if there is a Slicer instance already running then don’t start a new Slicer instance but use files or web requests to ask for loading of a data set</li>
<li>shutdown Slicer executable on QREADS shutdown</li>
</ul>
<p>Let’s not block QREADS while SlicerQREADS is running (make it a non-modal popup) to make sure we never force the user to wait.</p>

---

## Post #37 by @spycolyf (2021-02-23 23:14 UTC)

<p>OK great. The Arizona Medical school has been using my modifieds version of Sankhesh’s 2018 FourPanesViewer to teach for the past 2 years and have requested a non-modal launch so that they could contiue to do other things in QREADS. So they will be happy. I will need to work out cases where the user happens to change patients while SlicerQREADS is launching a with a series from the previous patient. There can never be a time when SlicerQREADS and the QREADS host are displaying images from different patients. That another sentinel event potential.</p>
<p>Thanks everyone and good evening.</p>

---

## Post #38 by @spycolyf (2021-02-24 17:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Good morning all,</p>
<p>I hate to keep beating on a dead horse, but I have a totally hypothetical scientific question. Theoretically, if I were crazy enough and had a million years to go through all of the SlicerQREADS files and eliminate 1 at a time and then test the app for failure, using the process of dependent file elimination, might I be able to get the size down significantly smaller than 300MB? Sankhesh’s 2018 FourPanesViewer app was has a total size of 60MB and had similar functionality. It was a quick install.</p>

---

## Post #39 by @pieper (2021-06-08 19:24 UTC)

<p>The typical path is to build an installer like we do for <a href="http://download.slicer.org">download.slicer.org</a> that is basically a single-file archive that also sets OS configurations.  But Slicer doesn’t strictly require an installer, and you could just make a zip file of the installation directory that can be unzipped on the machine for use.</p>
<p>Putting the installation directory on a fileshare can also work, but there will be tradeoffs since a lot of the files will be accessed over the network at startup and performance may suffer (you could test how bad this is).</p>
<p>Probably not all 25,000 PCs need 3D visualization, so probably it’s best to keep the installer on the shared drive and only install the app once on each PC that needs it.  So you would have the download/install cost once for that machine, but then more rapid startups after that.</p>

---

## Post #40 by @spycolyf (2021-06-09 21:37 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and</p>
<p>We appreciate your patience and willingness to work with us. The QREADS team will discuss our options and other experts on the team may chime in with technical questions beyond my experience and expertise.</p>
<p>Doug</p>

---

## Post #41 by @spycolyf (2021-06-14 21:33 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Here are few approach we could evaluate:</p>
<ul>
<li>statically link loadable module into the application</li>
<li>statically integrate <code>PythonQt</code> module that are currently dynamically loaded</li>
<li>statically link against external dependency like ITK, VTK, DCMTK, …</li>
<li>harden the current python integrate into C++ and remove the use of python</li>
</ul>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Question to you posed by my team most interested in JC’s proposed solutions:</p>
<p>Can the Python used by a Slicer module be replaced by a runtime version and thereby replacing the Python libraries in the build?</p>
<p>Thanks</p>

---

## Post #42 by @jcfr (2021-06-14 22:06 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="41" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Can the Python used by a Slicer module be replaced by a runtime version and thereby replacing the Python libraries in the build?</p>
</blockquote>
</aside>
<p>yes but …</p>
<p>… since current packaging rules assumes Slicer built its own python, and expect to package it and find it as as such. Some work would be needed to improve Slicer to accommodate this use-case.</p>

---

## Post #44 by @spycolyf (2021-06-16 15:47 UTC)

<p><span class="mention">@lasson</span>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, <a class="mention" href="/u/pieper">@pieper</a></p>
<p>We are now starting the long cyclical process of elimination and testing to reduce the installation footprint.  PLEASE, if you see potential dangers here, let me know. I’d appreciate it!<br>
So far we’ve eliminated</p>
<pre><code>Qt5WebEngineCore.dll: 92 MB
SciPy folder: So far things are still working, but would eliminate another 100 MB
</code></pre>
<p>Question: What are the “test” folders for? My lead thought because they were called “test”, eliminating them would have no effect. Surprise! They are needed…</p>

---

## Post #45 by @jamesobutler (2021-06-16 17:04 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="44" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>PLEASE, if you see potential dangers here, let me know. I’d appreciate it!</p>
</blockquote>
</aside>
<p>You will likely be in uncharted territory if you are just deleting files in an install package and hoping things continue to work so I would suggest not to start here first.</p>
<p>Have you already deactivated Slicer build options that you don’t need? For example, if you don’t want Scipy, then you would turn off the “Slicer_USE_SCIPY” option. If you don’t need SimpleITK, turn off the “Slicer_USE_SimpleITK”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a44563491efca694c7e180133bef385bf18cc75.png" data-download-href="/uploads/short-url/hrCF3r34MmV0AO4wT1ZDHhaxXfL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a44563491efca694c7e180133bef385bf18cc75.png" alt="image" data-base62-sha1="hrCF3r34MmV0AO4wT1ZDHhaxXfL" width="425" height="500" data-dominant-color="F1B2B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">715×840 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #46 by @spycolyf (2021-06-16 17:28 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, does the SlicerQREADS module need SimpleITK. I vaguely remember ITK was used for some DICOM or database issue.</p>
<p>Also, I am implementing volume cropping and the 3D volume rendering presets on my end that is not on GitHub. <a class="mention" href="/u/jcfr">@jcfr</a>, can you suggest other CMAKE options we might need to deactivate, or have you done that already?</p>
<p>Thanks</p>

---

## Post #47 by @jamesobutler (2021-06-16 17:40 UTC)

<p>Here are your currently defined build options. SimpleITK is already set to off. Here is where you would turn off Scipy if you do not need it.</p><aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L85-L107" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L85-L107" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L85-L107</a></h4>



  <pre class="onebox">    <code class="lang-txt">
      <ol class="start lines" start="85" style="counter-reset: li-counter 84 ;">
          <li># Slicer options</li>
          <li>option(BUILD_TESTING                            "Build application test suite"                        ON)</li>
          <li>option(Slicer_BUILD_DOCUMENTATION               "Build documentation (Doxygen, sphinx, ...)"          OFF)</li>
          <li>if(WIN32)</li>
          <li>  option(Slicer_BUILD_WIN32_CONSOLE             "Build application executable as a console app"       OFF)</li>
          <li>endif()</li>
          <li>
          </li>
<li>option(Slicer_BUILD_DICOM_SUPPORT               "Build application with DICOM support"                ON)</li>
          <li>option(Slicer_BUILD_DIFFUSION_SUPPORT           "Build application with Diffusion support"            OFF)</li>
          <li>option(Slicer_BUILD_EXTENSIONMANAGER_SUPPORT    "Build application with ExtensionManager support"     OFF)</li>
          <li>option(Slicer_BUILD_MULTIVOLUME_SUPPORT         "Build application with MultiVolume support"          OFF)</li>
          <li>option(Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT "Build application with parameter serializer support" OFF)</li>
          <li>option(Slicer_USE_PYTHONQT                      "Build application with Python support"               ON)</li>
          <li>option(Slicer_USE_QtTesting                     "Build application with QtTesting support"            OFF)</li>
          <li>option(Slicer_USE_SimpleITK                     "Build application with SimpleITK support"            OFF)</li>
          <li>
          </li>
<li>option(Slicer_BUILD_BRAINSTOOLS                 "Build application with BRAINSTools module"           OFF)</li>
          <li>option(Slicer_BUILD_DataStore                   "Build application with DataStore module"             OFF)</li>
          <li>option(Slicer_BUILD_CompareVolumes              "Build application with CompareVolumes module"        OFF)</li>
          <li>option(Slicer_BUILD_LandmarkRegistration        "Build application with LandmarkRegistration module"  OFF)</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L85-L107" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #48 by @spycolyf (2021-06-16 17:47 UTC)

<p>Hey <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, my team is just curious. What are all of the test subfolders in many pf the paths used for? I notice that the BUILD_TESTING option is on. Do we need that?</p>
<p>Thanks</p>

---

## Post #49 by @jamesobutler (2021-06-16 17:51 UTC)

<p>What are some examples of the full paths to the “test” directories that you are referring to?</p>
<p>From looking at your application the “BUILD_TESTING” option is enabled which may bring in items into the installed package.</p>

---

## Post #50 by @spycolyf (2021-06-16 17:58 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> - Oh, sorry,  you responded when I modified my previous message.</p>

---

## Post #51 by @spycolyf (2021-06-16 18:08 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
I know that I request a lot of your time and I really try to limit the time that you spend helping me. I just want you to know that we apprecaite it.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="49" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>What are some examples of the full paths to the “test” directories that you are referring to?</p>
</blockquote>
</aside>
<p>Here’s an example of the “test” folders. There are many in other folder paths…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36e69b0b6f89b4e2f213d4006abd0273934af289.png" data-download-href="/uploads/short-url/7PFQVGuv22Nowh2ZZeyuu2ueLcR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36e69b0b6f89b4e2f213d4006abd0273934af289.png" alt="image" data-base62-sha1="7PFQVGuv22Nowh2ZZeyuu2ueLcR" width="555" height="500" data-dominant-color="F4F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">715×644 38.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #52 by @jcfr (2021-06-16 18:21 UTC)

<blockquote>
<p>re: skipping install of test files provided in python packages</p>
</blockquote>
<h3><a name="p-61368-excluding-libdistutilstests-1" class="anchor" href="#p-61368-excluding-libdistutilstests-1" aria-label="Heading link"></a>Excluding  <code>Lib/distutils/tests</code></h3>
<p>To address this specific use case, we should update this list of regex:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8d4bab41dffb2dbf070c481ef4e075537ba36386/CMake/SlicerBlockInstallPython.cmake#L41-L45">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8d4bab41dffb2dbf070c481ef4e075537ba36386/CMake/SlicerBlockInstallPython.cmake#L41-L45" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8d4bab41dffb2dbf070c481ef4e075537ba36386/CMake/SlicerBlockInstallPython.cmake#L41-L45" target="_blank" rel="noopener">CMake/SlicerBlockInstallPython.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/8d4bab41dffb2dbf070c481ef4e075537ba36386/CMake/SlicerBlockInstallPython.cmake#L41-L45" rel="noopener"><code>8d4bab41d</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="41" style="counter-reset: li-counter 40 ;">
          <li>REGEX "lib2to3/tests/" EXCLUDE</li>
          <li>REGEX "lib[-]old/" EXCLUDE</li>
          <li>REGEX "plat[-].*" EXCLUDE</li>
          <li>REGEX "/test/" EXCLUDE</li>
          <li>${extra_exclude_pattern}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h3><a name="p-61368-general-solution-2" class="anchor" href="#p-61368-general-solution-2" aria-label="Heading link"></a>General solution</h3>
<p>Update the relevant <code>SuperBuild/External_python-&lt;packageName&gt;.cmake</code> file to do one of the following:</p>
<p>(1) List directory to include from installation and append the list to the regex listed referenced above.</p>
<p>(2) Update the <code>INSTALL_COMMAND</code> in each external project to explicitly delete the unwanted folder after installation.</p>

---

## Post #53 by @spycolyf (2021-06-16 18:43 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> ,</p>
<p>Just to be sure, when I go through and delete them manually, SlicerQREADS does not work properly. Will following your instructions behave better? I’m assuming SlicerQREADS will no longer expect the existence of test folders if we do your suggestion.</p>

---

## Post #54 by @jcfr (2021-06-16 18:52 UTC)

<p>Assuming the changes I suggested are contributed to Slicer, they will  be tested and validated.</p>
<p>Once this is done, the version of Slicer used SlicerQReads custom application may be updated and at that stage, I indeed expect SlicerQREADS to work properly.</p>
<p>To move forward with excluding <code>Lib/distutils/tests</code>, I suggest you submit a pull request to Slicer. Once this is done, it could be backported to the fork of Slicer used in SlicerQReads.</p>

---

## Post #55 by @spycolyf (2021-06-17 14:32 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="52" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<h3>Excluding <code>Lib/distutils/tests</code></h3>
<p>To address this specific use case, we should update this list of regex:</p>
</blockquote>
</aside>
<p>I see this list in my SlicerBlockInstallPython.cmake. The list specifies “REGEX “/test/” EXCLUDE”. One would think this to mean that test folders would be excluded. But they are included in my installation packages. So, I don’t get it. What am I supposed to do with this information? Update to what? How?</p>
<p>Thanks!</p>

---

## Post #56 by @lassoan (2021-06-17 14:43 UTC)

<p>The regex exclude <code>/test/</code>, which means that it will not exclude <code>Lib/distutils/tests</code>. To exclude that folder, you would need to add <code>/tests</code> to the regexp.</p>

---

## Post #57 by @spycolyf (2021-06-17 23:05 UTC)

<p>Hello <a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, I’m trying to determine if my module (SlicerQREADS) needs Qt5WebEngine files such as Qt5WebEngineCore.dll, etc? Does SlicerQREADS need Qt5WebEngine as a dependency? It won’t launch when Qt5WebEngineCore.dll is deleted from the install package bin folder. Immediately, an error is displayed indicating Qt5WebEngineCore.dll is missing. This is confusing because, eliminating Qt5WebEngineCore.dll worked on my teammate’s system earlier this week. That why we were sure we could reduce the size by 100MB.</p>
<p>So again, is Qt5WebEngineCore.dll really a dependency?</p>
<p>Thanks</p>

---

## Post #58 by @lassoan (2021-06-17 23:15 UTC)

<p>QWebEngine is needed for the extensions manager, data store, or for web-based authentication. Probably none of them are needed for you, so you can turn off WebEngine option when you build your custom application.</p>

---

## Post #59 by @spycolyf (2021-06-17 23:50 UTC)

<p>Do I turn it off in the CMakeList.text in my source folder?</p>
<pre><code class="lang-auto">option(Slicer_BUILD_DICOM_SUPPORT               "Build application with DICOM support"                ON)
option(Slicer_BUILD_DIFFUSION_SUPPORT           "Build application with Diffusion support"            OFF)
option(Slicer_BUILD_EXTENSIONMANAGER_SUPPORT    "Build application with ExtensionManager support"     OFF)
option(Slicer_BUILD_MULTIVOLUME_SUPPORT         "Build application with MultiVolume support"          OFF)
option(Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT "Build application with parameter serializer support" OFF)
option(Slicer_USE_PYTHONQT                      "Build application with Python support"               ON)
option(Slicer_USE_QtTesting                     "Build application with QtTesting support"            OFF)
option(Slicer_USE_SimpleITK                     "Build application with SimpleITK support"            OFF)

option(Slicer_BUILD_BRAINSTOOLS                 "Build application with BRAINSTools module"           OFF)
option(Slicer_BUILD_DataStore                   "Build application with DataStore module"             OFF)
option(Slicer_BUILD_CompareVolumes              "Build application with CompareVolumes module"        OFF)
option(Slicer_BUILD_LandmarkRegistration        "Build application with LandmarkRegistration module"  OFF)
option(Slicer_BUILD_SurfaceToolbox              "Build application with SurfaceToolbo
</code></pre>
<p>x module"        OFF)</p>
<p><strong>Do you know the syntax. What is the best way to find the correct syntax for switching on or off options.</strong><br>
<strong>I’d like to turn off webengine and scipy, but don’t know the syntax and where to insert them.</strong></p>
<p>Thanks</p>

---

## Post #60 by @spycolyf (2021-06-18 00:28 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="47" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Here are your currently defined build options. SimpleITK is already set to off. Here is where you would turn off Scipy if you do not need it.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p>How does someone learn the syntax? There is a cmakelist.txt file in my source folder. Looks like I will make the changes there. I guess I can guess the syntax, but not sure.</p>
<pre><code class="lang-auto">option(Slicer_USE_SciPy                     "Build application with SciPy support"            OFF)
option(Slicer_USE_WEBEngine                 "Build application with WebEngine support"        OFF)
</code></pre>
<p>How’s that? Is there a manual for Slicer CMake options?</p>
<p>Thanks</p>

---

## Post #61 by @jamesobutler (2021-06-18 01:24 UTC)

<p>There isn’t a manual for Slicer CMake options but it is always best to use examples of things that do similar things. You are correct to modify those type entries in your CMakeLists.txt that I had linked above.</p>
<p>You’re on the right track with the example you provided. Just make sure the first item in the parenthesis is the correct build name option. This should match the items in the “Name” column in the screenshot I posted earlier of the CMake GUI.</p>
<p>You will see there is an option with WebEngine in the name which is the one you want. There is also a name entry for Scipy.</p>

---

## Post #62 by @spycolyf (2021-06-18 02:56 UTC)

<p>Ok, I see. I can find the names of options by looking at the Slicer CMakeList or the CMake GUI. Thanks.</p>

---

## Post #63 by @spycolyf (2021-06-21 16:57 UTC)

<p>Good Morning <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I was able to reduce the size of my install package by 200MB via CMake. We just want to thank you all for your help on this as we will continue to look for ways to reduce the size. If you can think of any other functions we might try to eliminate vis CMake, please do not hesitate to inform us. The smaller we can get this, the more accepting our Windows Workstation team would be willing to pre-install SlicerQREADS on all 50,000 plus systems (25,000 simultaneous users) enterprise-wide.</p>
<p>Thank you so much!</p>

---

## Post #64 by @pieper (2021-06-21 17:17 UTC)

<p>If you use a tool like <a href="https://www.jam-software.com/treesize_free">treesize</a> you can figure out what’s taking up space and we can tell you which parts might be optional for you depending on your needs.</p>

---

## Post #65 by @spycolyf (2021-06-30 17:55 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It may also be possible to start scrolling the axials as they arrive and then snap to MPR once the volume is complete (or something similar so the user doesn’t just see a blank screen and get bored).</p>
</blockquote>
</aside>
<p>Hello <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Is "scrolling the axials as they arrive " currently a functionality that I can enable?</p>
<p>Thanks</p>

---

## Post #66 by @pieper (2021-06-30 18:02 UTC)

<p>No, this is a new feature that would need to be enabled.</p>

---

## Post #67 by @spycolyf (2021-06-30 20:32 UTC)

<p>A great feature for users indeed. I know it’s just smoke and mirrors, but many (if not, most) vendors are doing it.</p>
<p>Thanks.</p>

---

## Post #68 by @pieper (2021-06-30 22:59 UTC)

<p>Coincidentally I stated experimenting with this the other day.  As you can see in the linked video it’s super fast to read and display the images if you just read them from disk and display them so we could look at offering this preview mode while the 3D/4D inspection and processing is going on in the background.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/CTK/pull/979">
  <header class="source">

      <a href="https://github.com/commontk/CTK/pull/979" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/pull/979" target="_blank" rel="noopener">WIP: add thumbnails to dicom browser</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>pieper:browser-thumbnails</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-29" data-time="00:34:10" data-timezone="UTC">12:34AM - 29 Jun 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 4 files with 42 additions and 6 deletions">
        <a href="https://github.com/commontk/CTK/pull/979/files" target="_blank" rel="noopener">
          <span class="added">+42</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Based on ProjectWeek discussion:
https://projectweek.na-mic.org/PW35_2021_Virtu<span class="show-more-container"><a href="https://github.com/commontk/CTK/pull/979" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">al/Projects/mpReview/</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #69 by @spycolyf (2021-07-01 15:06 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Do you mean a kind of fancy progress bar that would automatically scroll through the images? That’s cool. In our situation, they’ve already previewed it in the host QREADS app that launched SlicerQREADS, so the previewing again might feel redundant.</p>
<p>I know what I’m about to say sounds ridiculous, but if I were to imaging the ideal UI, the axials would scroll while the coronal and sagittal slices would update to show the cross sections so far. The user would be able to see the image loading advancement in the orthogonal slices as they progress from top to bottom, and they would know that the axial series loading is complete when the cross section slices are visually full. The orthogonal slices act as progress bars if you will.</p>
<p>By the way, is there way to use just a regular progress bar for this. Anything to keep the user from wondering is SlicerQREADS has crashed.</p>
<p>Thanks</p>

---

## Post #70 by @pieper (2021-07-01 17:29 UTC)

<p>In OHIF we do the incremental fill, but not in Slicer.  Yes there’s a lot of room for improving the dicom experience in Slicer, ideally optimizing for the most common cases.  There are a lot of non-trivial special cases being handled by all the plugins and other mechanisms that add time to the loading.</p>

---

## Post #71 by @spycolyf (2021-07-01 17:56 UTC)

<p>Hold on!!! Are you guys are affiliated with OHIF?</p>

---

## Post #72 by @pieper (2021-07-01 18:25 UTC)

<p>Yes, we work very closely with the OHIF team and have for years.  One of our goals is to have smooth interoperability between web and desktop applications.</p>

---

## Post #73 by @spycolyf (2021-07-01 18:43 UTC)

<p>Great! I’m so glad you guys are helping organizations like OHIF. Hopefully relationships like that is helping to sustain you existentially.</p>
<p>Thanks</p>

---

## Post #74 by @spycolyf (2021-07-01 20:38 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a></p>
<p>How can I use a progress bar that appears when the images are loading and terminates when image loading is done?.</p>
<p>Thanks.</p>

---

## Post #75 by @pieper (2021-07-01 21:03 UTC)

<p>You can check out this discussion for options:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5716">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5716" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5716" target="_blank" rel="noopener">ENH: Add context managers to show while waiting</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>fepegar:add-some-utils</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-07-01" data-time="10:33:25" data-timezone="UTC">10:33AM - 01 Jul 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/fepegar" target="_blank" rel="noopener">
          <img alt="fepegar" src="https://avatars.githubusercontent.com/u/12688084?v=4" class="onebox-avatar-inline" width="20" height="20">
          fepegar
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 133 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5716/files" target="_blank" rel="noopener">
          <span class="added">+133</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">These are some potentially useful utils coming from https://github.com/fepegar/S<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5716" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">licerParcellation/blob/master/lib/GeneralUtils.py.

@lassoan's comments were:

&gt; There is indeed some repeating code pattern with the waitcursor and printing of exception messages which would be nice to simplify. Please send a pull request to Slicer core with the content of GeneralUtils.py to start a discussion. Initial comment: the overridecursor has to be restored when an exception occurs ("finally" is too late because the popup window is displayed in "except" and it is not nice if the waitcursor is still shown when the user gets the error popup). messageContextManager: It seems that it is intended for progress reporting, but for thatyou can already use the statusbar or delaydisplay. A context manager for error messages could be more useful: it would take a general error message (that it would display if there is an exception) and would offer to show the exception text if user clicks "Details" button. Something like this: https://github.com/Slicer/Slicer/blob/aaa9f918a4ee4f35bf09e05c5d7e53d083b2e4e3/Modules/Scripted/DICOMLib/DICOMSendDialog.py#L91-L99

My replies:

&gt; the overridecursor has to be restored when an exception occurs ("finally" is too late because the popup window is displayed in "except" and it is not nice if the waitcursor is still shown when the user gets the error popup)

I'm not sure which popup window you mean. Something created by the user? `showWaitCursor` doesn't show a popup window.

&gt; messageContextManager: It seems that it is intended for progress reporting, but for that you can already use the statusbar or delaydisplay.

The status bar might not be very obvious. This is how I've used this in a module (0:35, here being played at x2): https://youtu.be/Gg02F9DGDc4?t=35. Not sure how I would use delayDisplay with the context manager. I wouldn't like buttons in the window.

&gt; A context manager for error messages could be more useful: it would take a general error message (that it would display if there is an exception) and would offer to show the exception text if user clicks "Details" button. 

Thanks. I have added a `tryWithErrorDisplay` context manager.

Comments:

1. Maybe the names can be improved
1. The goal of these is two remove a bit of verbosity from users' code.
1. I imported `contextmanager` to be able to use the decorator. This seems forbidden in `slicer.util`, though. Another option is to use the class syntax for context managers. Why are all the imports inside the functions? Why are many of them in one line, this is against [PEP8](https://www.python.org/dev/peps/pep-0008/#imports).
1. Why is the file so long? Why not splitting it into different submodules and importing everything here if necessary?

Here are some snippets to try these:

```python
import time
import random

def work():
  time.sleep(random.randrange(1, 3))

def fail():
  work()
  int('Szia')

showThings = True

#
with showWaitCursor(show=showThings):
  work()

#
with showWaitCursor(show=showThings):
  fail()

#
with messageContextManager('¡Hola!', show=showThings):
  work()

#
with messageContextManager('¡Hola!', show=showThings):
  fail()

#
with tryWithErrorDisplay(show=showThings):
  work()

#
with tryWithErrorDisplay(show=showThings):
  fail()

#
getPythonConsoleWidget().show()
with peakPythonConsole(show=showThings):
  print('This should just wait a bit')
  slicer.app.processEvents()
  work()

# This one needs to be pasted with a blank line at the end so it runs
getPythonConsoleWidget().hide()
slicer.app.processEvents()
time.sleep(2)
with peakPythonConsole(show=showThings):
  print('I will close soon!')
  slicer.app.processEvents()
  work()


```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #76 by @spycolyf (2021-07-02 14:55 UTC)

<p>OK, is this available to use right now and is it possible to somehow sync it up with the image load process? Yet another rabbit hole? <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=9" title=":expressionless:" class="emoji" alt=":expressionless:"></p>
<p>Thanks <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #77 by @pieper (2021-07-02 17:20 UTC)

<p>I don’t think it’s a rabbit hole, but it’s just a work in progress.  Right now that PR just implements the ability to look at the images as part of the metadata preview.  It’s probably useful as-is but it also demonstrates that it should be possible to do something much faster in terms of presenting the images to the user.  As usual it’s a SMOP*  to make it happen.</p>
<p>* SMOP == “simple matter of programming”</p>

---

## Post #78 by @spycolyf (2021-07-02 18:20 UTC)

<p>Oh, my apologies <a class="mention" href="/u/pieper">@pieper</a>, I didn’t mean that as an offense to you guys, but to mainly my own inexperience and incompetence. It seems to takes me weeks sometimes to accomplish very simple tasks. I’ll get there eventually. Just feels like rabbit holes from my current inadequate Slicer-programming skills and lack of experience. I’m sure eventually, it will get better. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #79 by @pieper (2021-07-02 18:25 UTC)

<p>No offense taken at all!  Just wanted to set expectations with respect to that particular feature.  I’m sure we’ve all spent time in “rabbitholes” or even worse chasing after bugs and otherwise spinning our wheels in unfamiliar environments.</p>

---

## Post #80 by @spycolyf (2021-07-02 18:54 UTC)

<p>So, to answer my question. Is this feature currently available? I would like to use the wait cursor to show progress while loading images. It would need to know how many images to expect and the current number of images loaded so far. Or is this a future feature?</p>
<p>Thanks</p>

---

## Post #81 by @lassoan (2021-07-13 03:16 UTC)

<p>Progressive loading is not available yet.</p>
<p>Pre-allocation of volume and progressive loading of slices on a few threads would make a huge difference when loading the images from a remote server. However, if the images are already on the local file system (and recently accessed by QREADS) then I’m not sure ​it would help much.</p>
<p>For example, I did a quick test and importing and loading of a CT images series of 512x512x681 voxels took 8 seconds in total. 2-3 seconds were spent with importing (parse the header of 681 files and store the results in the DICOM database) and 5-6 was to load the series.</p>
<p>Do you use the DICOM module for loading images?<br>
How long does DICOM import take (populating Slicer’s DICOM database with files of the selected study)?<br>
How long does DICOM loading take (loading an image series into the scene)?</p>

---

## Post #82 by @jcfr (2021-07-13 16:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="81" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you use the DICOM module for loading images?</p>
</blockquote>
</aside>
<p>Indeed, see</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L723-L744">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L723-L744" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L723-L744" target="_blank" rel="noopener">KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L723-L744</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="723" style="counter-reset: li-counter 722 ;">
          <li>def loadDICOMDataDirectory(dicomDataDir):</li>
          <li>  from DICOMLib import DICOMUtils</li>
          <li></li>
          <li>  loadedNodeIDs = []  # this list will contain the list of all loaded node IDs</li>
          <li></li>
          <li>  with DICOMUtils.TemporaryDICOMDatabase() as db:</li>
          <li>    DICOMUtils.importDicom(dicomDataDir, db)</li>
          <li>    patientUIDs = db.patients()</li>
          <li>    for patientUID in patientUIDs:</li>
          <li>      for nodeID in DICOMUtils.loadPatientByUID(patientUID):</li>
          <li></li>
          <li>        # Retrieve tag values associated with first instance UID</li>
          <li>        node = slicer.mrmlScene.GetNodeByID(nodeID)</li>
          <li>        instanceUID = node.GetAttribute('DICOM.instanceUIDs').split()[0]</li>
          <li>        filename = db.fileForInstance(instanceUID)</li>
          <li>        QReadsLogic.DICOM_TAG_VALUES[instanceUID] = {</li>
          <li>          tag: db.fileValue(filename, tag) for tag in QReadsLogic.DICOM_TAGS</li>
          <li>        }</li>
          <li></li>
          <li>        loadedNodeIDs.append(nodeID)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/Modules/Scripted/QReads/QReads.py#L723-L744" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #83 by @spycolyf (2021-07-28 03:06 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.13<br>
Expected behavior: Equal Image load times<br>
Actual behavior: 1 series takes 30 seconds, the other takes 10 minutes.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I’m trying to create DCMs from memory for my Slicer module to load and display. It was too slow for me to get the original files from the server for my module to use, so I decided to create the files from images already in memory. The saved files are identical to the original files (according to the DICOM Validator Compare utility) and all DCMs are the same size. Yet, 1 series takes 30 seconds, the other takes 10 minutes to load into Slicer.</p>
<p>The first series here was created as a result of saving DICOM files from images in memory:<br>
<a>https://www.dropbox.com/s/op4jaeqynhu8u42/FromHeap.zip?dl=0</a><br>
It takes Slicer 10 to 20 times longer to load into Slicer than than the original files…<br>
<a>https://www.dropbox.com/s/pcdxdbpr2jiv4jy/FromStackFile.zip?dl=0</a></p>
<p>How does this happen? This is interesting to say the least.</p>
<p>Thanks</p>

---

## Post #84 by @lassoan (2021-07-28 04:30 UTC)

<p>I could not reproduce the slow loading using the latest Slicer Preview Release. Using DCMTK, GDCM, and the archetype reader, import+loading time was between 48 and 75 seconds (sometimes one, sometimes the other was slightly faster).</p>
<pre><code class="lang-python">&gt;&gt;&gt; def loadDICOM(dicomDataDir):
...     loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
...     import time
...     from DICOMLib import DICOMUtils
...     with DICOMUtils.TemporaryDICOMDatabase() as db:
...         DICOMUtils.importDicom(dicomDataDir, db)
...         patientUIDs = db.patients()
...         for patientUID in patientUIDs:
...             loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
...     return loadedNodeIDs
... 
&gt;&gt;&gt; 
&gt;&gt;&gt; 
&gt;&gt;&gt; 
&gt;&gt;&gt; startTime = time.time()
&gt;&gt;&gt; loadDICOM(r"c:\tmp\20210727-dicom-slow-load\UNZ\heap")
Switching to temporary DICOM database: C:/Users/andra/AppData/Local/Temp/Slicer/20210728_040253_TempDICOMDatabase
Loading with imageIOName: DCMTK
['vtkMRMLScalarVolumeNode1']
&gt;&gt;&gt; print(f"Elapsed: {time.time()-startTime}")
Elapsed: 75.61358332633972
&gt;&gt;&gt; 
&gt;&gt;&gt; startTime = time.time()
&gt;&gt;&gt; loadDICOM(r"c:\tmp\20210727-dicom-slow-load\UNZ\stack")
Switching to temporary DICOM database: C:/Users/andra/AppData/Local/Temp/Slicer/20210728_040408_TempDICOMDatabase
Loading with imageIOName: DCMTK
['vtkMRMLScalarVolumeNode2']
&gt;&gt;&gt; print(f"Elapsed: {time.time()-startTime}")
Elapsed: 66.1774833202362
&gt;&gt;&gt; 
&gt;&gt;&gt; 
&gt;&gt;&gt; 
&gt;&gt;&gt; startTime = time.time()
&gt;&gt;&gt; loadDICOM(r"c:\tmp\20210727-dicom-slow-load\UNZ\heap")
Switching to temporary DICOM database: C:/Users/andra/AppData/Local/Temp/Slicer/20210728_040550_TempDICOMDatabase
Loading with imageIOName: GDCM
['vtkMRMLScalarVolumeNode3']
&gt;&gt;&gt; print(f"Elapsed: {time.time()-startTime}")
Elapsed: 52.05962634086609
&gt;&gt;&gt; 
&gt;&gt;&gt; startTime = time.time()
&gt;&gt;&gt; loadDICOM(r"c:\tmp\20210727-dicom-slow-load\UNZ\stack")
Switching to temporary DICOM database: C:/Users/andra/AppData/Local/Temp/Slicer/20210728_040642_TempDICOMDatabase
Loading with imageIOName: GDCM
['vtkMRMLScalarVolumeNode4']
&gt;&gt;&gt; print(f"Elapsed: {time.time()-startTime}")
Elapsed: 55.64105939865112
&gt;&gt;&gt; 
&gt;&gt;&gt; 
&gt;&gt;&gt; 
&gt;&gt;&gt; startTime = time.time()
&gt;&gt;&gt; loadDICOM(r"c:\tmp\20210727-dicom-slow-load\UNZ\heap")
Switching to temporary DICOM database: C:/Users/andra/AppData/Local/Temp/Slicer/20210728_041449_TempDICOMDatabase
['vtkMRMLScalarVolumeNode5']
&gt;&gt;&gt; print(f"Elapsed: {time.time()-startTime}")
Elapsed: 48.70469260215759
&gt;&gt;&gt; 
&gt;&gt;&gt; startTime = time.time()
&gt;&gt;&gt; loadDICOM(r"c:\tmp\20210727-dicom-slow-load\UNZ\stack")
Switching to temporary DICOM database: C:/Users/andra/AppData/Local/Temp/Slicer/20210728_041538_TempDICOMDatabase
['vtkMRMLScalarVolumeNode6']
&gt;&gt;&gt; print(f"Elapsed: {time.time()-startTime}")
Elapsed: 55.29209494590759
&gt;&gt;&gt; 
&gt;&gt;&gt; 
</code></pre>

---

## Post #85 by @spycolyf (2021-07-28 14:23 UTC)

<p>I’ll check this out. Could it be in the way I’m launching my module? Here’s the command I’m using …</p>
<pre><code class="lang-auto">dicomDataDir = "C:/Stack-vs-HeapMPRLoadingTimes/Stack"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
  
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>Thanks</p>

---

## Post #86 by @spycolyf (2021-07-28 15:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Here’s my timings. I’m using the 4.13 May 15th Slicer version.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0279c74494af5db1ccaa57d94ef774dd852c98d6.png" data-download-href="/uploads/short-url/lTRyYLnU7mWUgEdFXW7h527sKW.png?dl=1" title="StackVsHeap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0279c74494af5db1ccaa57d94ef774dd852c98d6.png" alt="StackVsHeap" data-base62-sha1="lTRyYLnU7mWUgEdFXW7h527sKW" width="690" height="437" data-dominant-color="F6F5FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">StackVsHeap</span><span class="informations">996×631 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #87 by @jamesobutler (2021-07-28 15:36 UTC)

<p>If you use the latest Slicer preview and run that code in the python interactor, do the results change?</p>
<p>Could be a change between your Slicer May 15th version and the latest Slicer preview. Download the slicer preview from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a></p>

---

## Post #88 by @spycolyf (2021-07-28 15:38 UTC)

<p>ok, thanks I will do that.</p>

---

## Post #89 by @spycolyf (2021-07-28 16:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>But isn’t it strange? There has to be something different about the Heap-generated files. I don’t know if it would be to the Slicer community’s advantage to know what causes this phenomenon, but I am perplexed by it.</p>
<p>Thanks</p>

---

## Post #90 by @spycolyf (2021-07-28 16:20 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="87" data-topic="18019" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If you use the latest Slicer preview and run that code in the python interactor, do the results change?</p>
<p>Could be a change between your Slicer May 15th version and the latest Slicer preview. Download the slicer preview from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a></p>
</blockquote>
</aside>
<p>Same results <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=12" title=":expressionless:" class="emoji" alt=":expressionless:" loading="lazy" width="20" height="20"></p>

---

## Post #91 by @lassoan (2021-07-28 17:05 UTC)

<p>Attach VerySleepy (a free profiler) and see what the most time Slicer spends with in both cases.</p>
<p>Also, try DCMTK, GDCM, and the archetype DICOM reader methods.</p>

---

## Post #92 by @jamesobutler (2021-07-28 17:13 UTC)

<p>I used Slicer 4.13.0-2021-07-27 and using the same profiling code that <a class="mention" href="/u/lassoan">@lassoan</a> posted about earlier and I had the following results similar to him:</p>
<p>Each time the load code was run I started Slicer fresh.</p>
<p>FromStackFile: Elapsed: 39.98049068450928<br>
FromHeap: Elapsed: 34.227794885635376</p>
<p>I did observe about 27000 log messages during loading of each I would suspect if sometime took longer to load it would be due to logging more messages. Review the log in Help-&gt;Report A Bug</p>

---

## Post #93 by @pieper (2021-07-28 17:26 UTC)

<p>Good idea about the log messages <a class="mention" href="/u/jamesobutler">@jamesobutler</a>.  I’ve seen slowdowns when the log gets long, so <a class="mention" href="/u/spycolyf">@spycolyf</a>  try comparing a fresh restart of slicer when generating the timings.  If the log is a bottleneck we can definitely address that.</p>

---

## Post #94 by @spycolyf (2021-07-28 18:57 UTC)

<p>So, yes I think you hit the nail right on the head,  929 pairs of these in the Stack log file…</p>
<pre><code class="lang-auto">[CRITICAL][Stream] 27.07.2021 18:23:44 [] (unknown:0) - W: DcmMetaInfo: No Group Length available in Meta Information Header
[CRITICAL][Stream] 27.07.2021 18:23:44 [] (unknown:0) - W: DcmItem: Length of element (7fe0,0010) is not a multiple of 2 (VR=OW)
</code></pre>
<p>… and 929 of these in the Heap log file…</p>
<pre><code class="lang-auto">[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmMetaInfo: No Group Length available in Meta Information Header
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,0015)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,0050)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,0060)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,0090)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1000)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1020)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1030)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1100)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1110)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1111)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1120)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1130)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1140)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1150)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1151)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1152)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1160)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1170)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1190)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1200)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1201)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,1210)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0018,5100)
[CRITICAL][Stream] 27.07.2021 18:10:32 [] (unknown:0) - W: DcmItem: Length of element (7fe0,0010) is not a multiple of 2 (VR=OW)
</code></pre>
<p>So we need to correct things on our end.</p>
<p>Question: Is the bulk of the time spent writing to the log file? Or is the time spent in detecting and analyzing the issues? In other words, if there are no problems detected, would this reduce the load times for both the stack and the heap versions significantly?</p>
<p>Thanks</p>

---

## Post #95 by @pieper (2021-07-28 19:02 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="94" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Question: Is the bulk of the time spent writing to the log file? Or is the time spent in detecting and analyzing the issues?</p>
</blockquote>
</aside>
<p>I’m pretty sure it’s the log file and the log display dialog.  There is code to make it thread safe and I’ve noticed that sometimes output text is significantly delayed for some reason.</p>
<p>I think you are correct though that fixing the dicoms to generate fewer messages is the best path in any case.</p>

---

## Post #96 by @spycolyf (2021-07-28 19:29 UTC)

<p>Here are the links</p>
<aside class="quote no-group" data-username="pieper" data-post="95" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m pretty sure it’s the log file and the log display dialog. There is code to make it thread safe and I’ve noticed that sometimes output text is significantly delayed for some reason.</p>
</blockquote>
</aside>
<p>I’m in a meeting now about this issue and they want to know …</p>
<ol>
<li>
<p>if there is a way to have a rolling log? Or should we manage that ourselves so that we don’t run out of disk space on any of our 50K+ systems?</p>
</li>
<li>
<p>Is there a way to turn logging off so that it’s bypassed completely?</p>
</li>
<li>
<p>When producing the DCMs, would it be OK to exclude the Sequences?</p>
</li>
</ol>
<p>Thanks.</p>

---

## Post #97 by @pieper (2021-07-28 20:55 UTC)

<p>A rolling log sounds like a good solution.  I don’t think you want to turn off messages completely.  Probably you should manage that on your side or propose a fix to the slicer core.  It sounds like an isolated feature that wouldn’t require a lot of changes to the internals of the program.</p>
<p>Best would be to fix the dicom so that not many messages are printed.</p>

---

## Post #98 by @spycolyf (2021-07-28 21:02 UTC)

<aside class="quote no-group" data-username="pieper" data-post="97" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I don’t think you want to turn off messages completely.</p>
</blockquote>
</aside>
<p>Yes, but is  there a Python way to turn off logging? We can always turn it back on when we are troubleshooting. Also, I would like to see what the timing differences would be.</p>
<p>Thanks</p>

---

## Post #99 by @pieper (2021-07-28 21:11 UTC)

<p>That’s an idea, but I don’t know if it’s possible.</p>

---

## Post #100 by @spycolyf (2021-07-28 22:00 UTC)

<aside class="quote no-group" data-username="pieper" data-post="97" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Best would be to fix the dicom so that not many messages are printed.</p>
</blockquote>
</aside>
<p>OK, We will try to eliminate the messages. We are currently looking into the Out Of Order tags. The question is which message can we eliminate in the stack file logs (common to both heap and stack actually)? So, does Slicer normally generate the following log info for all Encapsulated format Pixel Data?</p>
<pre><code class="lang-auto">[CRITICAL][Stream] 27.07.2021 18:23:44 [] (unknown:0) - W: DcmMetaInfo: No Group Length available in Meta Information Header
[CRITICAL][Stream] 27.07.2021 18:23:44 [] (unknown:0) - W: DcmItem: Length of element (7fe0,0010) is not a multiple of 2 (VR=OW)
</code></pre>
<p>Here is our [7FE0, 0010] pixel data tags for Implicit VR Little Endian encapsulated pixel data…</p>
<pre><code class="lang-auto">00008a66 (   35430)	(7FE0,0010) - Pixel Data                          [OW][UNDEFN][  1]: 
00008a72 (   35442)		(FFFE,E000) - Item                                [][     4][  1]: 
00008a7e (   35454)		(FFFE,E000) - Item                                [][183848][  0]: 
000358ae (  219310)	|---&gt;(FFFE,E0DD) - Sequence Delimitation Item          [][     0][  0]:
</code></pre>
<p>Is the “UNDEFN” the problem?</p>

---

## Post #101 by @pieper (2021-07-28 22:44 UTC)

<p>It’s hard for me to say exactly how to fix these, but those messages give you some ideas where to look.  You can compare the structure of your data with samples that don’t generate these messages.</p>
<p>Also this tool can help flag non-conformities:</p>
<p><a href="https://www.dclunie.com/dicom3tools/dciodvfy.html" class="onebox" target="_blank" rel="noopener">https://www.dclunie.com/dicom3tools/dciodvfy.html</a></p>

---

## Post #102 by @spycolyf (2021-07-29 14:33 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="101" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Also this tool can help flag non-conformities:</p>
<p><a href="https://www.dclunie.com/dicom3tools/dciodvfy.html" class="inline-onebox" rel="noopener nofollow ugc">DICOM Validator - dciodvfy</a></p>
</blockquote>
</aside>
<p>Do you like this tool better than DVTk? (DICOM Validation Toolkit - <a>www.dvtk.org</a>)</p>
<p>Also, do you know where I can find valid DICOM file containing Encapsulated format Pixel Data? Is there a site where we can access standard DICOM data with which we can compare our data?</p>
<p>Thanks</p>

---

## Post #103 by @pieper (2021-07-29 14:48 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="102" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Do you like this tool better than DVTk? (DICOM Validation Toolkit - <a href="http://www.dvtk.org">www.dvtk.org</a>)</p>
</blockquote>
</aside>
<p>I’ve never used dvtk, thanks for pointing it out.</p>
<p>dciodvfy is written by David Clunie, editor of the dicom standard, so it’s usually a pretty rigorous and informative test.  In the end if your goal is to make things interoperable you probably want to use anything and everything you can get your hands on to make sure the data you are generating is as standards compliant as possible.  This is usually the best way to avoid surprises down the line.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="102" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Also, do you know where I can find valid DICOM file containing Encapsulated format Pixel Data? Is there a site where we can access standard DICOM data with which we can compare our data?</p>
</blockquote>
</aside>
<p>I wish there were a definitive collection of valid example dicom objects demonstrating the full range of legal variants, but I’ve never found such a collection.  Best I can suggest is <a href="https://www.cancerimagingarchive.net/">the TCIA collections</a> (or the subset hosted through <a href="https://imaging.datacommons.cancer.gov/">IDC</a>).</p>

---

## Post #104 by @spycolyf (2021-07-29 14:59 UTC)

<p>Good Morning,</p>
<p>I’m confused about how to interpret the log files. Here’s an example of the heap logs…</p>
<p>[DEBUG][Qt] 28.07.2021 16:12:06 [] (unknown:0) - “DICOM indexer has successfully inserted 929 files [0.56s]”<br>
[DEBUG][Qt] 28.07.2021 16:12:06 [] (unknown:0) - “DICOM indexer has successfully processed 929 files [2.71s]”</p>
<pre><code class="lang-auto">[DEBUG][Qt] 28.07.2021 16:12:06 [] (unknown:0) - "DICOM indexer has updated display fields for 929 files [0.22s]"
[INFO][Python] 28.07.2021 16:15:17 [Python] (C:/Program Files/Mayo Foundation/QREADS_3D_MPR/bin/../lib/SlicerQReads-4.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:384) - Loading with imageIOName: GDCM
[INFO][Stream] 28.07.2021 16:15:17 [] (unknown:0) - Loading with imageIOName: GDCM
[INFO][Stream] 28.07.2021 16:15:42 [] (unknown:0) - default Window / level = 1673.0 / -187.5
</code></pre>
<p>You can see a 3 minute difference between the 1st and 2nd lines. There are 23,000 lines in this log file and during the whole three minutes we can see the log file growing, and when it stops at around 3000KB, the app displays the images. Yet in the smaller Stack logs the time between the 1st and second lines in about 25 seconds. Is all of that time spent writing out the log file?</p>
<p>Thanks</p>

---

## Post #105 by @pieper (2021-07-29 17:33 UTC)

<p>Yes, if you are really getting 23,000 lines of output then the logging system is likely to get choked.  It would be good if slicer’s logging was faster, but it’s still better to fix the dicom instead.</p>

---

## Post #106 by @spycolyf (2021-07-29 23:31 UTC)

<p>Corrected the main cause that produced the most log lines. But now it’s putting out thousands of these…</p>
<pre><code class="lang-auto">[CRITICAL][Stream] 29.07.2021 17:40:48 [] (unknown:0) - W: DcmMetaInfo: No Group Length available in Meta Information Header
[CRITICAL][Stream] 29.07.2021 17:40:48 [] (unknown:0) - W: DcmItem: Length of element (7fe0,0010) is not a multiple of 2 (VR=OW)
</code></pre>
<ol>
<li>Why is it generating the “No Group Length available in Meta Information Header” lines? Is it a mandatory element?</li>
<li>A “-1” in the element (7fe0,0010) length is valid DICOM meaning “Undefined”. It’s OK for Encapsulated Pixel Data. So why generate log output.</li>
</ol>
<p>I really wish there was a way to turn of logging or control the severity. It’s really affecting my load times. Minutes to load 925 images. The Docs will just stop using 3D MPR.</p>
<p>Are you sure there’s no way to turn it off? Should I be able to find the code to shut it off? I know you don’t recommend it, but is the less of the 2 evils because tomorrow is my dev cutoff day.</p>
<p>Thanks!</p>

---

## Post #107 by @pieper (2021-07-29 23:45 UTC)

<p>Since you are building from source, you have the option to change dcmtk’s behavior here.  If you can’t find a way to change the logging, you can search for the substrings of the error message and comment out the messages you don’t want (again, it’s not what I’d recommend, but it would be a workaround).</p>

---

## Post #108 by @spycolyf (2021-07-29 23:50 UTC)

<p>OK, these files have no “0002,0000) - File Meta Information Group Length” elements. I’ll try to insert it. That may get rid of the “No Group Length available in Meta Information Header” warning.</p>
<p>But, do you allow the length of the Pixel data to be -1 or Undefined as listed here?..</p>
<p>Here is our [7FE0, 0010] pixel data tags for Implicit VR Little Endian encapsulated pixel data…</p>
<pre><code class="lang-auto">00008a66 (   35430)	(7FE0,0010) - Pixel Data                          [OW][UNDEFN][  1]: 
00008a72 (   35442)		(FFFE,E000) - Item                                [][     4][  1]: 
00008a7e (   35454)		(FFFE,E000) - Item                                [][183848][  0]: 
000358ae (  219310)	|---&gt;(FFFE,E0DD) - Sequence Delimitation Item          [][     0][  0]:
</code></pre>
<p>Is the “UNDEFN” is actually -1 which is not a multiple of 2 and it’s legal DICOM I believe. Is this why the “Length of element (7fe0,0010) is not a multiple of 2” problem? Do you think it’s a Slicer bug?</p>
<p>Thanks</p>

---

## Post #109 by @jamesobutler (2021-07-29 23:58 UTC)

<p>I believe all those warnings originate from DCMTK so it’s really not Slicer that is in control of determining the logic. Slicer is just reporting the warnings of DCMTK.</p>

---

## Post #110 by @spycolyf (2021-07-30 00:44 UTC)

<p>OK thanks a lot. I wonder if there is a way to configure DCMTK to control logging. I’ll look into it. Thanks for all of your help.</p>

---

## Post #111 by @spycolyf (2021-07-30 14:18 UTC)

<p>I will look for the code that generates the logs. Any hints would be greatly appreciated. Thanks. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #112 by @pieper (2021-07-30 14:32 UTC)

<p>I believe you are using a SlicerCustomApplicationTemplate, which I haven’t used myself fir this but you should have a way to access the superbuild cmake script for DCMTK corresponding to <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_DCMTK.cmake">this one</a> for Slicer itself.  DCMTK uses log4cpp and probably the configuration variables for that are exposed in CMake, but you’ll need to do some research to figure out what options there are for turning off warning messages.  HTH.</p>

---

## Post #113 by @spycolyf (2021-07-31 16:28 UTC)

<aside class="quote no-group" data-username="pieper" data-post="112" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>CMake, but you’ll need to do some research to figure out what options there are for turning off warning messages. HTH.</p>
</blockquote>
</aside>
<p>I see absolutely nothing in there that gives the slightest hint of controlling error or warning messages.</p>
<p>Are the logs written out by ITK? I found C:.…\TK\Modules\IO\DCMTK\src\itkDCMTKFileReader.cxx that seems to deal with the reading of DCMs, But I can’t find where it’s actually writing to the log files. Are you familiar enough in this space to know what Slicer Code Repository search string I can use to find the code that writes to the log files?</p>
<p>Thank you.</p>

---

## Post #114 by @pieper (2021-07-31 17:58 UTC)

<p>Most of the messages you copied here come from dcmtk. For Slicer builds we use this fork of dcmtk:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/commontk/DCMTK/tree/patched-DCMTK-3.6.6_20210115">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/commontk/DCMTK/tree/patched-DCMTK-3.6.6_20210115" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/commontk/DCMTK/tree/patched-DCMTK-3.6.6_20210115" target="_blank" rel="noopener">GitHub - commontk/DCMTK at patched-DCMTK-3.6.6_20210115</a></h3>

  <p><a href="https://github.com/commontk/DCMTK/tree/patched-DCMTK-3.6.6_20210115" target="_blank" rel="noopener">patched-DCMTK-3.6.6_20210115</a></p>

  <p><span class="label1">WARNING: This is NOT the official upstream DCMTK git repository.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can search for the warning messages from the log file and see what code is generating the messages.</p>
<p>But again, from what I can see these indicate errors in the format of the data.  It sounds from your messages that you have control over the way these files are written and that is the correct place to fix them.  Do you not agree?</p>

---

## Post #115 by @lassoan (2021-07-31 19:35 UTC)

<p>You can control log level in DCMTK, in CTK, and in Slicer and we could add some convenient and easier-to-discover API for changing log levels at runtime.</p>
<p>However, these are invalid DICOM files, so suppressing logs does not sound like a good idea. You want to be able to see warnings and report the issues to developers of the software that created the invalid files (in more severe cases, even report to users to make them aware that the data may be corrupted).</p>
<p>What DICOM toolkit do you use that create pixel data with undefined length? That’s a major issue, because many DICOM toolkit may simply refuse to load such data sets.</p>
<p>As a corrective action, I would recommend fixing the DICOM files. As a preventive action, we could try to improve speed of logging in Slicer.</p>
<p>Log files are already rotated. The number of log files preserved is set to 15 or so, and you can configure the number in the Slicer application configuration file. Cutting off a log file in the middle of a session makes it harder to collect complete log files from customers and make it harder for developers to analyze the logs, so I would not recommend doing it.</p>

---

## Post #116 by @spycolyf (2021-08-01 00:15 UTC)

<p>OK, yes. I think you’re right.</p>
<p>After further review …</p>
<ol>
<li>
<p>Maybe, <code>(7FE0,0010) - Pixel Data [OW][UNDEFN][  1]</code> should be of type OB rather than OW, and maybe that’s why it’s flagged as not being a multiple of 2 bytes.</p>
</li>
<li>
<p>And yes, GEL (0002, 0000) is type 1.</p>
</li>
</ol>
<p>We should try to fix this first.</p>
<p>Thanks!</p>

---

## Post #117 by @spycolyf (2021-08-01 00:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a>\</p>
<p>Hi. Please forgive me for so many questions, but we are preparing for this major release of QREADS with the SlicerQREADS extension. For controlling the number of log files and the temporary database folders, we will use our QREADS launcher code to delete older files.</p>
<p>The question was asked by my lead of whether there is a way to set the path of logging folder different from C:\Users\userID\AppData\Local\Temp\SlicerQReads.</p>
<p>Thanks</p>

---

## Post #118 by @spycolyf (2021-08-01 02:46 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="116" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Maybe, <code>(7FE0,0010) - Pixel Data [OW][UNDEFN][  1]</code> should be of type OB rather than OW, and maybe that’s why it’s flagged as not being a multiple of 2 bytes.</p>
</blockquote>
</aside>
<p>Changing the type to OB fixed that error.</p>

---

## Post #119 by @spycolyf (2021-08-01 02:48 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="116" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>And yes, GEL (0002, 0000) is type 1.</p>
</blockquote>
</aside>
<p>Now trying to figure out how to insert the mandatory (0002, 0000) into the header, and that should fix that error.</p>

---

## Post #120 by @lassoan (2021-08-01 02:49 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="117" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>For controlling the number of log files and the temporary database folders, we will use our QREADS launcher code to delete older files.</p>
</blockquote>
</aside>
<p>There is no need to manage the log files externally. You can set the number of log files to 1 if you only want to keep the log file of the last session.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="117" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>The question was asked by my lead of whether there is a way to set the path of logging folder different from C:\Users\userID\AppData\Local\Temp\SlicerQReads.</p>
</blockquote>
</aside>
<p>The log file location is <a href="https://github.com/Slicer/Slicer/blob/b44b89f2c94b6a44ab5362352fa2ee1b01ff3730/Base/QTGUI/qSlicerApplication.cxx#L863-L870">in the temporary folder specified by <code>TemporaryPath</code> in Slicer.ini</a>. If needed, it would be easy to add an optional settings value to specify a custom location.</p>

---

## Post #121 by @spycolyf (2021-08-01 02:53 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="117" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>For controlling the number of log files and the temporary database folders, we will use our QREADS launcher code to delete older files.</p>
</blockquote>
</aside>
<p>Thanks, how about the Temporary database folders? They are not so temporary. They don’t seem to be ever deleted.</p>
<p>Thanks</p>

---

## Post #122 by @spycolyf (2021-08-01 18:05 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="119" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Now trying to figure out how to insert the mandatory (0002, 0000) into the header, and that should fix that error.</p>
</blockquote>
</aside>
<p>Done, no more errors in the log files. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #123 by @spycolyf (2021-08-01 18:07 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="121" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Thanks, how about the Temporary database folders? They are not so temporary. They don’t seem to be ever deleted.</p>
</blockquote>
</aside>
<p>Do we need to manage those Temporary Database folders?</p>
<p>Thanks</p>

---

## Post #124 by @spycolyf (2021-08-01 19:06 UTC)

<p>Strange, I thought I fixed the logger problem because it worked earlier. But then I tried it on a large series I used on Friday, and got 1000s of lines indicating …</p>
<pre><code class="lang-auto">
[CRITICAL][Stream] 01.08.2021 13:35:48 [] (unknown:0) - W: DcmMetaInfo: No Group Length available in Meta Information Header
[CRITICAL][Stream] 01.08.2021 13:35:48 [] (unknown:0) - W: DcmItem: Length of element (7fe0,0010) is not a multiple of 2 (VR=OW)
[CRITICAL][Stream] 01.08.2021 13:35:48 [] (unknown:0) - W: DcmItem: Non-standard VR '  ' (00\00) encountered while parsing element (0000,0000), assuming 2 byte length field
[CRITICAL][Stream] 01.08.2021 13:35:48 [] (unknown:0) - W: DcmItem: Dataset not in ascending tag order, at element (0000,0000)
[CRITICAL][Stream] 01.08.2021 13:35:48 [] (unknown:0) - W: DcmItem: Non-standard VR '  ' (00\00) encountered while parsing element (0000,0000), assuming 2 byte length field
</code></pre>
<p>… which continued for 1000s of lines. I then observed the DICOM headers. 7FE0 was set to OB, not OW as the logs indicated. And 0002, 0000 was indeed present contrary to what the logs indicated. I tried many times; no luck.</p>
<p>However, after I deleted all of the Temporary Databases and tried again, it worked. Therefore, the Temporary databases need to be deleted immediately after every launch. But I’m assuming this needs to be done very carefully as it may cause issues with multiple instances of the app.</p>
<p>Thanks</p>

---

## Post #125 by @lassoan (2021-08-02 17:22 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="124" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I then observed the DICOM headers. 7FE0 was set to OB, not OW as the logs indicated. And 0002, 0000 was indeed present contrary to what the logs indicated. I tried many times; no luck.</p>
</blockquote>
</aside>
<p>DICOM files are not mutable. SOP instance UID of a DICOM files fully identifies the content of the file. Therefore, if you change a DICOM file you must always generate a new SOP instance UID (and usually series instance UID as well).</p>
<p>Maybe what happened is that when you patched the DICOM files you did not update the SOP instance UID and you still had the old files in the database. During DICOM import, Slicer detected that the files have been already imported (based on the SOP instance UID match) and therefore it did not import the files again.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="124" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>However, after I deleted all of the Temporary Databases and tried again, it worked.</p>
</blockquote>
</aside>
<p>Currently, TemporaryDatabase context manager just <a href="https://github.com/Slicer/Slicer/blob/3b37852a1605a111d26708ece1195c2cc05e297d/Modules/Scripted/DICOMLib/DICOMUtils.py#L287-L293">resets the database but does not delete the files</a>. I’m not sure what the reason is, but probably it is not valid anymore, so we’ll just restore the original behavior of deleting the temporary files:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5764">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5764" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/5764" target="_blank" rel="noopener">BUG: Remove temporary database files when the database is closed</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:remove-temp-dicom-db</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-02" data-time="17:14:47" data-timezone="UTC">05:14PM - 02 Aug 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="4 commits changed 4 files with 22 additions and 29 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/5764/files" target="_blank" rel="noopener">
            <span class="added">+22</span>
            <span class="removed">-29</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The code to delete the database was commented out several years ago (before the <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5764" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">large DICOM database refactoring). The temporary database files can now be deleted properly.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #126 by @jcfr (2021-08-02 17:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="125" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>TemporaryDatabase context manager just <a href="https://github.com/Slicer/Slicer/blob/3b37852a1605a111d26708ece1195c2cc05e297d/Modules/Scripted/DICOMLib/DICOMUtils.py#L287-L293">resets the database but does not delete the files</a>. I’m not sure what the reason is, but probably it is not valid anymore, so we’ll just restore the original behavior of deleting the temporary files:</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/spycolyf">@spycolyf</a>  After you test the changes proposed by <a class="mention" href="/u/lassoan">@lassoan</a>  locally, let us know. Then, we will integrate the changes in Slicer and also backport it into the branch used to build SlicerQReads. See <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L15-L16">here</a> and <a href="https://github.com/KitwareMedical/Slicer/commits/SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6">here</a></p>

---

## Post #127 by @spycolyf (2021-08-03 19:31 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="126" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>After you test the changes proposed by <a class="mention" href="/u/lassoan">@lassoan</a> locally, let us know. Then, we will integrate the changes in Slicer and also backport it into the branch used to build SlicerQReads. See <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L15-L16" rel="noopener nofollow ugc">here </a> and <a href="https://github.com/KitwareMedical/Slicer/commits/SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6" rel="noopener nofollow ugc">here </a></p>
</blockquote>
</aside>
<p>You guys are so great!</p>
<p>So to be clear there are 4 files to change:</p>
<p>Those files are here: <a>https://github.com/Slicer/Slicer/pull/5764/files/9ac1329084af7e1e8250aad57ca6d670a4408aa6</a></p>
<ul>
<li>qMRMLCheckableNodeComboBox.cxx</li>
<li>qMRMLPlotViewControllerWidget.cxx</li>
<li>qSlicerSubjectHierarchySegmentationsPlugin.cxx</li>
<li>DICOMUtils.py</li>
</ul>
<p>I will make the changes my build (delete the red lines and insert the green lines) and rebuild. Is that a full rebuild with: “cmake --build . --config Release --target – /maxcpucount:8” ?</p>

---

## Post #128 by @lassoan (2021-08-03 20:34 UTC)

<p>Merging this commit is sufficient:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5764/commits/16072c7cf399f12adebda275d1489eb14b4c881a">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5764/commits/16072c7cf399f12adebda275d1489eb14b4c881a" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5764" target="_blank" rel="noopener">BUG: Remove temporary database files when the database is closed</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:remove-temp-dicom-db</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-02" data-time="17:14:47" data-timezone="UTC">05:14PM - 02 Aug 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="4 commits changed 4 files with 22 additions and 29 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5764/files" target="_blank" rel="noopener">
          <span class="added">+22</span>
          <span class="removed">-29</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The code to delete the database was commented out several years ago (before the <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5764" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">large DICOM database refactoring). The temporary database files can now be deleted properly.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>That’s a single file. It is a Python file, so you only need to “build” to copy the .py file from the source folder to the appropriate Python module folder.</p>

---

## Post #129 by @spycolyf (2021-08-03 22:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="128" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>That’s a single file. It is a Python file, so you only need to “build” to copy the .py file from the source folder to the appropriate Python module folder.</p>
</blockquote>
</aside>
<p>OK, I was confused by this [<a href="https://github.com/Slicer/Slicer/pull/5764/files/9ac1329084af7e1e8250aad57ca6d670a4408aa6" rel="noopener nofollow ugc">link</a>] which shows the changes for “BUG: Remove temporary database files when the database is closed <span class="hashtag-raw">#5764</span>.” I assumed I had to make all of those changes and I did. Should I undo the changes to the following files?</p>
<ul>
<li>qMRMLCheckableNodeComboBox.cxx</li>
<li>qMRMLPlotViewControllerWidget.cxx</li>
<li>qSlicerSubjectHierarchySegmentationsPlugin.cxx</li>
</ul>

---

## Post #130 by @spycolyf (2021-08-04 00:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="128" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>That’s a single file. It is a Python file, so you only need to “build” to copy the .py file from the source folder to the appropriate Python module folder.</p>
</blockquote>
</aside>
<p>OK, I made the changes to DicomUtils.py. It’s the one located in my final executable package, “…\lib\SlicerQReads-4.13\qt-scripted-modules\DICOMLib” Folder… It doesn’t delete the temp DB files. Shouldn’t this work? Do I need to add a command to my QREADS.py file?</p>
<p><strong>Here is the change I made to DicomUtils.py…</strong></p>
<p><strong>Changed FROM…</strong></p>
<pre><code class="lang-auto">def deleteTemporaryDatabase(dicomDatabase, cleanup=True):
  """ Close temporary DICOM database and remove its directory if requested
  """
  dicomDatabase.closeDatabase()

  if cleanup:
    dicomDatabase.initializeDatabase()
    # TODO: The database files cannot be deleted even if the database is closed.
    #       Not critical, as it will be empty, so will not take measurable disk space.
    # import shutil
    # databaseDir = os.path.split(dicomDatabase.databaseFilename)[0]
    # shutil.rmtree(databaseDir)
    # if os.access(databaseDir, os.F_OK):
      # logging.error('Failed to delete DICOM database ' + databaseDir)

  return True
</code></pre>
<p><strong>TO…</strong></p>
<pre><code class="lang-auto">def deleteTemporaryDatabase(dicomDatabase, cleanup=True):
  """ Close temporary DICOM database and remove its directory if requested
  """
  dicomDatabase.closeDatabase()

  if cleanup:
    import shutil
    databaseDir = os.path.split(dicomDatabase.databaseFilename)[0]
    shutil.rmtree(databaseDir)
    if os.access(databaseDir, os.F_OK):
      logging.error('Failed to delete DICOM database ' + databaseDir)
      # Database is still in use, at least clear its content
      dicomDatabase.initializeDatabase()

  return True
</code></pre>
<p>The files are sill accumulating. What did I do wrong?</p>
<p>When this is done, I’ll be ready to deploy to 30,000 workstations. So, I need to do this somehow.</p>
<p>Thanks</p>

---

## Post #131 by @lassoan (2021-08-04 02:30 UTC)

<p>I’ve tested the code and for me it deleted the temporary folder. You can add a break point and debug the code step by step, or add some log messages to get more information on what is happening exactly.</p>

---

## Post #132 by @spycolyf (2021-08-04 16:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="131" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>’ve tested the code and for me it deleted the temporary folder. You can add a break point and debug the code step by step, or add some log messages to get more information on what is happening exactly.</p>
</blockquote>
</aside>
<p>My problem might be that I did not add the code to the correct file. I added it to the DicomUtlis.py file in my built package. I think I should not have to recompile since it’s Python.  That should work, correct?</p>
<p>Exactly how did you do it?</p>

---

## Post #133 by @lassoan (2021-08-04 17:44 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="132" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I added it to the DicomUtlis.py file in my built package.</p>
</blockquote>
</aside>
<p>That should work. You can attach a Python debugger or at least add a few log messages so that you can verify what code is executed.</p>

---

## Post #134 by @jcfr (2021-08-04 18:19 UTC)

<blockquote>
<p>re: patching SlicerQReads</p>
</blockquote>
<p>For convenience, here is a PR backporting the change. Consider reviewing.<br>
See <a href="https://github.com/KitwareMedical/SlicerQReads/pull/106">https://github.com/KitwareMedical/SlicerQReads/pull/106</a></p>
<blockquote>
<p>I made the changes to DicomUtils.py. It’s the one located in my final executable package …</p>
</blockquote>
<p>Patching a local build or install tree without updating the source code is really discouraged as changes could be lost anytime.</p>

---

## Post #135 by @spycolyf (2021-08-05 23:21 UTC)

<p>Just to be sure, are these changes [<a href="https://github.com/Slicer/Slicer/pull/5764/files/9ac1329084af7e1e8250aad57ca6d670a4408aa6" rel="noopener nofollow ugc">link</a>]  to the following files needed? If not, then no recompile necessary because were making changes only to DicomUtlis.py. Correct?</p>
<ul>
<li>qMRMLCheckableNodeComboBox.cxx</li>
<li>qMRMLPlotViewControllerWidget.cxx</li>
<li>qSlicerSubjectHierarchySegmentationsPlugin.cxx</li>
</ul>
<p>Maybe you already have the changes to those files already.</p>

---

## Post #136 by @spycolyf (2021-08-05 23:30 UTC)

<p>We’re almost ready for primetime. The release is Aug 24th and we are currently in the testing phase. I demoed 3D MPR to the team and my unit head. The image load times are down, the size is down by 200MB, the module will be pre-installed on all 50K of the computers. and everything is running pretty smooth. The only concern expressed was the need for a progress bar while waiting for the images to load; especially for large series. The blank screen with the white background in the 3D view while images are loading leaves the user wondering and worrying if the app crashed. Our docs are stressed out enough <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Are you sure there’s no solutions as of now?</p>
<p>Thanks</p>

---

## Post #137 by @spycolyf (2021-08-05 23:34 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="134" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Patching a local build or install tree without updating the source code is really discouraged as changes could be lost anytime.</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>. Yes I know. I do this only to test things out first and then I make it permanent by copying the changes to the source.</p>
<p>Thanks</p>

---

## Post #138 by @pieper (2021-08-05 23:37 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="136" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>The only concern expressed was the need for a progress bar while waiting for the images to load; especially for large series.</p>
</blockquote>
</aside>
<p>Were you able to have your version of the code open source?  If so send a link to the place where you are loading the series and depending on the method we can probably give advice on how to add a progress bar.</p>

---

## Post #139 by @jamesobutler (2021-08-05 23:42 UTC)

<p>The Slicer custom app code is here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerQReads" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/631b2af89f21cd899397d5297d71f12c30e43dbabff65b75f243faa02b905512/KitwareMedical/SlicerQReads" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerQReads" target="_blank" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerQReads: Slicer-based implementation of QREADS...</a></h3>

  <p>Slicer-based implementation of QREADS medical image viewer used at Mayo Clinic - GitHub - KitwareMedical/SlicerQReads: Slicer-based implementation of QREADS medical image viewer used at Mayo Clinic</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The custom version of Slicer used is here</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/KitwareMedical/Slicer/tree/SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/Slicer/tree/SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/KitwareMedical/Slicer/tree/SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6" target="_blank" rel="noopener nofollow ugc">GitHub - KitwareMedical/Slicer at SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6</a></h3>

  <p><a href="https://github.com/KitwareMedical/Slicer/tree/SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6" target="_blank" rel="noopener nofollow ugc">SlicerQReads-v4.13.0-2021-04-26-d06e71c8a6</a></p>

  <p><span class="label1">Fork for Slicer Custom application. Contribute to KitwareMedical/Slicer development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #140 by @spycolyf (2021-08-06 01:47 UTC)

<p>Hey guys, I fully intend to work on getting it in opensource and I know it’s to my benefit as well as the Slicer community to do so. If it were fully my decision to make, I would have already been in opensource. But I have to go through management and legal to get permission and they are not happy with my taking so long to get this out. I’m hopeful that I will be able to share it in opensource at the appropriate time.</p>
<p>Thanks</p>

---

## Post #141 by @pieper (2021-08-06 11:33 UTC)

<p>Thanks Doug, I didn’t want to put you on the spot, just wanted to say it can be hard sometimes to guess what to suggest without being sure of how the code is working.</p>
<p>Can you describe which code path would benefit from a progress bar?  Are you loading through the dicom module?  The easiest could be to put up a static progress dialog that just says “Working…” and then hide it when the data is loaded.  If you need an actual animated progress bar that accurately predicts how much work is left that can be trickier.</p>

---

## Post #142 by @spycolyf (2021-08-06 19:23 UTC)

<aside class="quote no-group" data-username="pieper" data-post="141" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The easiest could be to put up a static progress dialog that just says “Working…”</p>
</blockquote>
</aside>
<p>Yes, that would work. Can that static progress dialog be done in Python? I don’t have much time. At this point example code would be most helpful. Thanks.</p>

---

## Post #143 by @spycolyf (2021-08-06 20:05 UTC)

<p>Has anyone ever seen this error. Don’t spend much time researching right now please. Just want to know if this rings a bell or have a rough guess. Thanks!</p>
<pre><code class="lang-auto">[ERROR][Python] 06.08.2021 14:04:58 [Python] (...\lib\SlicerQReads-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py:728) - DICOM plugin failed to load '3: MR AXIAL FLAIR' as a 'Image sequence'.
Traceback (most recent call last):
  File "...\lib\SlicerQReads-4.13\qt-scripted-modules\DICOMLib\DICOMUtils.py", line 722, in loadLoadables
    loadSuccess = plugin.load(loadable)
  File "... /bin/../lib/SlicerQReads-4.13/qt-scripted-modules/DICOMImageSequencePlugin.py", line 363, in load
    self.addSequenceBrowserNode(loadable.name, outputSequenceNodes, playbackRateFps, loadable)
  File "... /bin/../lib/SlicerQReads-4.13/qt-scripted-modules/DICOMImageSequencePlugin.py", line 230, in addSequenceBrowserNode
    outputSequenceBrowserNode = slicer.vtkMRMLSequenceBrowserNode()
</code></pre>

---

## Post #144 by @mikebind (2021-08-06 21:15 UTC)

<p>I have occasionally had the DICOM loader erroneously identify a series as a “Sequence” instead of a volume, and then try to load it that way. It looks like that might be what have run into.  Alternatively, it sounds like you have been mucking around in DICOMUtils.py, so perhaps some of the logic there is no longer valid and is leading to this error.</p>

---

## Post #145 by @spycolyf (2021-08-06 21:49 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="144" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Alternatively, it sounds like you have been mucking around in DICOMUtils.py, so perhaps some of the logic there is no longer valid and is leading to this error.</p>
</blockquote>
</aside>
<p>Yes, this occurred only with MR series which I have not done much testing. PET, CT and NM works fine. Also, I undid the DicomUtils changes, so I don’t think it’s that.</p>
<p>Thanks</p>

---

## Post #146 by @pieper (2021-08-06 21:59 UTC)

<p>If you aren’t planning to use Sequences you can also try turning off the Sequences plugin.  Easiest would be to take it out of the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/CMakeLists.txt">CMakeLists.txt</a> so it doesn’t get included in your installation.  (Need to also remove it from the build tree if you are re-building in place).  Be aware though that there can be many MR acquisitions that don’t map cleanly to volumes, so sometimes loading a sequence is correct.  In this case it’s not clear what your MR data is so probably best to just catch any errors and say that the series type is not supported.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="142" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Can that static progress dialog be done in Python? I</p>
</blockquote>
</aside>
<p>Here’s one option.  Replace time.sleep with your call.</p>
<p><code>import time; d = qt.QMessageBox(qt.QMessageBox.Icon(qt.QMessageBox.Information), "SlicerQReads", "Working...", qt.QMessageBox.NoButton); d.setStandardButtons(0); d.show(); slicer.app.processEvents(); time.sleep(2); d.hide()</code></p>

---

## Post #147 by @spycolyf (2021-08-07 21:50 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Do you think it could be programmed in such a way as to show the dialog during the image load time when no images are showing and there is a white background in the 3D view, and then hide when the images are displayed? I’m trying to place the d.show() and d.hide() in various sections of the code to have this effect. Haven’t found it yet tho.</p>
<p>Thanks</p>

---

## Post #148 by @spycolyf (2021-08-09 18:49 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>: I’m assuming that’s a no. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
It seems wherever I put the code, it comes up and immediately disappears. If you blink, you’d miss it.</p>
<p>Thanks</p>

---

## Post #149 by @spycolyf (2021-08-09 18:59 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="146" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>import time; d = qt.QMessageBox(qt.QMessageBox.Icon(qt.QMessageBox.Information), “SlicerQReads”, “Working…”, qt.QMessageBox.NoButton); d.setStandardButtons(0); d.show(); slicer.app.processEvents(); time.sleep(2); d.hide()</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Hello JC, could you tell me where to place the above code to display the dialog box so that it appears when SlicerQREADS’ main window displays and goes away when the images appear?</p>
<p>Thanks</p>

---

## Post #150 by @pieper (2021-08-09 20:22 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="147" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Do you think it could be programmed in such a way as to show the dialog during the image load time when no images are showing and there is a white background in the 3D view, and then hide when the images are displayed?</p>
</blockquote>
</aside>
<p>Hi Doug - that example uses the 2 second delay (the <code>time.sleep(2)</code> part) to emulate calling the load routine.  So if you put the first part, up to <code>slicer.app.processEvents()</code> before your call to load the imags and the <code>d.hide()</code> after the load call returns then the “Working…” dialog should stay up for as long as it takes for the reading process to complete.  Does that make sense to you?</p>

---

## Post #151 by @jcfr (2021-08-09 20:44 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="149" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>could you tell me where to place the above code to display the dialog box so that it appears when SlicerQREADS’ main window displays and goes away when the images appear?</p>
</blockquote>
</aside>
<p>Relevant changes have been implemented in the following pull request:<br>
See <a href="https://github.com/KitwareMedical/SlicerQReads/pull/107">https://github.com/KitwareMedical/SlicerQReads/pull/107</a></p>

---

## Post #152 by @spycolyf (2021-08-11 04:16 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="151" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Relevant changes have been implemented in the following pull request:<br>
See <a href="https://github.com/KitwareMedical/SlicerQReads/pull/107" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerQReads/pull/107 </a></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, that was perfect. I did put it in a try / except block to avoid it hanging up because the DICOM import fails a lot. Otherwise, task manager is the only way to kill it.</p>
<p>Thank y’all so much.</p>

---

## Post #153 by @lassoan (2021-08-11 04:19 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="152" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>to avoid it hanging up because the DICOM import fails a lot</p>
</blockquote>
</aside>
<p>Slicer may need extra plugins for loading exotic information objects, but I don’t find that it fails a lot for commonly occurring data sets. What specific problems did you encounter?</p>

---

## Post #154 by @spycolyf (2021-08-11 05:09 UTC)

<p>Oh probably it’s because some of my DICOM headers are faulty. I have not specifically identified the cause yet. But it seems to be mainly my MR file headers that I need to fix. QREADS itself is very forgiving of DICOM header imperfections. But when it fails, the patient demographics don’t show up in the title bar and the W/L is not set to the header values. Anyway I’ll try to solve that soon.</p>
<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a>, how do I disable or eliminate the main window minimize button. We need to disallow minimizing SlicerQREADS because it behaves as a modal dialog. Probably a QT command. Correct?</p>
<p>Thanks.</p>

---

## Post #155 by @jcfr (2021-08-11 06:57 UTC)

<blockquote>
<p>I did put it in a try / except block to avoid it hanging up because the DICOM import fails a lot. Otherwise, task manager is the only way to kill it.</p>
</blockquote>
<p>Following the coomment of <a class="mention" href="/u/pieper">@pieper</a> , the corresponding PR has been updated with an additional commit introducing the context manager <code>inProgressDialog</code>, this allows to cleanly handle the case when exception are raised without preventing the exception from being caught. See <a href="https://github.com/KitwareMedical/SlicerQReads/pull/107">https://github.com/KitwareMedical/SlicerQReads/pull/107</a></p>
<blockquote>
<p>how do I disable or eliminate the main window minimize button.</p>
</blockquote>
<p>This is implemented in the following PR.<br>
See <a href="https://github.com/KitwareMedical/SlicerQReads/pull/108">https://github.com/KitwareMedical/SlicerQReads/pull/108</a></p>

---

## Post #156 by @spycolyf (2021-08-23 21:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>I think everything is looking good for the release. One thing that could get us a lot of service calls though:</p>
<ul>
<li>Does anyone know how to programmatically detect whether the correct version of OpenGL is installed on the systems for SlicerQREADS to run. Currently, on systems with OpenGL version 1.0, the module displays a dialog indicating insufficient graphics capability, and then does not exit properly, leaving QREADS in a hung state waiting for SlicerQREADS to exit. Maybe there’s somewhere I can place a Try/Catch to avoid this abnormal exit. I believe SlicerQReadsApp-real.exe hangs around in task manager as well.</li>
</ul>
<p>Thanks</p>

---

## Post #157 by @pieper (2021-08-23 21:53 UTC)

<p>The code that checks that is below.  It should be cleaning up nicely, but perhaps for your purposes you want to check the graphics resources earlier and exit right away.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Base/QTApp/qSlicerApplicationHelper.txx#L96-L109">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Base/QTApp/qSlicerApplicationHelper.txx#L96-L109" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Base/QTApp/qSlicerApplicationHelper.txx#L96-L109" target="_blank" rel="noopener">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Base/QTApp/qSlicerApplicationHelper.txx#L96-L109</a></h4>



  <pre class="onebox">    <code class="lang-txx">
      <ol class="start lines" start="96" style="counter-reset: li-counter 95 ;">
          <li>// qSlicerApplicationHelper::checkRenderingCapabilities() seems only work reliably</li>
          <li>// on Windows, therefore we skip it on other platforms.</li>
          <li>// See details at https://issues.slicer.org/view.php?id=4252</li>
          <li>#if defined(_WIN32)</li>
          <li>  if (enableMainWindow &amp;&amp; !app.testAttribute(qSlicerCoreApplication::AA_EnableTesting))</li>
          <li>    {</li>
          <li>    // Warn the user if rendering requirements are not met and offer</li>
          <li>    // exiting from the application.</li>
          <li>    if (!qSlicerApplicationHelper::checkRenderingCapabilities())</li>
          <li>      {</li>
          <li>      return 1;</li>
          <li>      }</li>
          <li>    }</li>
          <li>#endif</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/ae2e56b493138eaa9d9082951f49bb3d693a2a9d/Base/QTApp/qSlicerApplicationHelper.cxx#L240-L300">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/ae2e56b493138eaa9d9082951f49bb3d693a2a9d/Base/QTApp/qSlicerApplicationHelper.cxx#L240-L300" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ae2e56b493138eaa9d9082951f49bb3d693a2a9d/Base/QTApp/qSlicerApplicationHelper.cxx#L240-L300" target="_blank" rel="noopener">Slicer/Slicer/blob/ae2e56b493138eaa9d9082951f49bb3d693a2a9d/Base/QTApp/qSlicerApplicationHelper.cxx#L240-L300</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="240" style="counter-reset: li-counter 239 ;">
          <li>bool qSlicerApplicationHelper::checkRenderingCapabilities()</li>
          <li>{</li>
          <li>  vtkNew&lt;vtkSystemInformation&gt; systemInfo;</li>
          <li>  systemInfo-&gt;RunRenderingCheck();</li>
          <li>  if (systemInfo-&gt;GetRenderingCapabilities() &amp; vtkSystemInformation::OPENGL)</li>
          <li>    {</li>
          <li>    return true;</li>
          <li>    }</li>
          <li>
          </li>
<li>  qWarning("Graphics capability of this computer is not sufficient to run this application");</li>
          <li>
          </li>
<li>  QString message = tr("Graphics capability of this computer is not sufficient to "</li>
          <li>    "run this application. The application most likely will not function properly.");</li>
          <li>
          </li>
<li>  QString details = tr(</li>
          <li>    "See more information and help at:\n{1}/user_guide/get_help.html#slicer-application-does-not-start\n\n"</li>
          <li>    "Graphics capabilities of this computer:\n\n")</li>
          <li>    .arg(qSlicerApplication::application()-&gt;documentationBaseUrl());</li>
          <li>  details += systemInfo-&gt;GetRenderingCapabilitiesDetails().c_str();</li>
          <li>
      </li>
</ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/ae2e56b493138eaa9d9082951f49bb3d693a2a9d/Base/QTApp/qSlicerApplicationHelper.cxx#L240-L300" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #158 by @lassoan (2021-10-12 14:11 UTC)

<p>For computers that don’t have GPU (or not accessible due to using the computer via remote desktop connection) then it is possible to run Slicer using a software renderer. See details <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">here</a>. Switching to a software renderer would require copying about 20 DLLs to the bin folder and set two environment variables, so it would not be hard to automate it.</p>

---

## Post #159 by @spycolyf (2021-10-12 20:58 UTC)

<p>Oh wow! Thanks. I’ll consider that <a class="mention" href="/u/lassoan">@lassoan</a>. Appreciate it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #160 by @spycolyf (2021-10-12 21:04 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>In my 3D view, I’m doing 3D rendering and ROI cropping, and I’m using presets like CT-Cardiac, CT-Xray, CT-Lung, etc. Is there a preset for CT Bone?</p>
<p>Thanks</p>

---

## Post #161 by @lassoan (2021-10-12 21:08 UTC)

<p>Yes, there is a preset called “CT-bone”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea5120d0d9c1c9afae04c9ccba358973d181635.png" data-download-href="/uploads/short-url/rcwnDOxUtjUIYXL79KfUSV6ben3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bea5120d0d9c1c9afae04c9ccba358973d181635_2_564x500.png" alt="image" data-base62-sha1="rcwnDOxUtjUIYXL79KfUSV6ben3" width="564" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bea5120d0d9c1c9afae04c9ccba358973d181635_2_564x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bea5120d0d9c1c9afae04c9ccba358973d181635_2_846x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bea5120d0d9c1c9afae04c9ccba358973d181635_2_1128x1000.png 2x" data-dominant-color="C8C7C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1192×1056 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>These presets are relatively hard to find (the user needs to go to Volumes module and select a volume). Suggestions are welcome for making them more easily accessible. Maybe in the dropdown menu of the window/level mouse mode selector? Or in the right-click menu of a view?</p>

---

## Post #162 by @spycolyf (2021-10-13 14:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="158" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it is possible to run Slicer using a software renderer</p>
</blockquote>
</aside>
<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a>, does Slicer automatically detect the presence of GPU, OpenGL2, CPU and use accordingly? Will it use the software renderer only if no other graphics rendering ability is available? This is probably as great incentive for merging back into the open source community.</p>
<p>Thanks</p>

---

## Post #163 by @rbumm (2021-10-15 07:24 UTC)

<p>Will this thread result in a downsized slicer installation that could be used in a hospital network with approx 3000 windows clients, most of them would probably need software rendering as they have no GPU? We would be interested in that.  Does software rendering really work with volume rendering, which seems to be hardware-intense whenever I use it?</p>

---

## Post #164 by @rbumm (2021-10-15 07:31 UTC)

<p>It would be great to have it in the window/level mouse mode selector.</p>

---

## Post #165 by @lassoan (2021-10-17 21:03 UTC)

<p>It would be great if you could submit a feature request for this at <a href="https://issues.slicer.org">https://issues.slicer.org</a> to keep track of the idea.</p>

---

## Post #166 by @rbumm (2021-11-08 08:36 UTC)

<p>Hi Doug, it would be great if you could give an update on how the deployment to the PCs of the Mayo enterprise actually worked.</p>

---

## Post #167 by @spycolyf (2021-11-23 20:13 UTC)

<p>Oh Wow! I’m just now seeing this. So sorry!</p>
<p>Yes!</p>
<p>QREADS is the imaging app that launches SlicerQREADS via a DOS shell command sending the folder path as the one argument. Upon the user selecting SlicerQREADS in the series right-mouse menu, QREADS first checks whether the SlicerQREADS installation folder exists and contains SlicerQREADS.exe. If not, then the menu item in the right-mouse menu reads “Install 3D MPR?” If the user answers yes to the “Are you sure” dialog,  then a script is executed that creates the module’s installation folder, downloads the SlicerQREADS.zip file from the file share, and unzips it creating the expected SlicerQREADS folder structure. In the zip file, the app name SlicerQREADS.exe is preceded with an underscore, and the very last thing the installation script does is to rename _SlicerQREADS.exe to SlicerQREADS.exe without the underscore. That way QREADS knows that the module is fully installed and the menu item will read simply “3D Multi-Planar Reconstruction,” and the module will launch successfully.</p>
<p>We have about 35,000 potential users of SlicerQREADS. When we first deployed the QREADS version that included the launching of the SlicerQREADS module, we had the Windows Workstation team pre-deploy the SlicerQREADS app to all systems that has QREADS installed. That way, the scenario described about is only performed for new systems and users that come online that do not have SlicerQREADS installed…</p>
<p>Please let me know if I can help any further. Thank you!</p>

---

## Post #168 by @rbumm (2021-11-24 12:49 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="167" data-topic="18019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>SlicerQREADS.exe</p>
</blockquote>
</aside>
<p>This is a clever workflow. Two questions:</p>
<p>(1) is the size-optimized SlicerQREADS windows package (or are the build sources) available somewhere?</p>
<p>(2) Do the Mayo clinic users import their DICOM files on their SlicerQREADS viewers from a PACS solution? How is the loading performance?</p>
<p>Thanks</p>

---

## Post #169 by @spycolyf (2021-12-02 18:49 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a>,</p>
<p>OK, sorry again for the delay.</p>
<p>The SlicerQREADS module is a smaller package separate from the build sources although still about 400 MB in our case. but that zips down to about 150MB and downloads and unzips quickly.</p>
<p>I think the best way to show you the performance is through the following demo which is real-time. As you can see it’s tolerable. Depending on the internet download speeds, the performance will vary. In his video, the downloads were pretty fast. with about 200 DCM files. We maximize the download rate by having the DCMs stacked into 1 file on the QREADS server, downloaded to the client via http, and then de-stacked for the SlicerQREADS module. Anyway, the delays are not bad once the DCMs are present and that’s the real bottleneck. You might use a DICOM receiver in your Slicer app, however. For us, that takes longer since we have our stacked DCMs in a files server ready to be downloaded.</p>
          <div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/vhv0g3unfk7pxql/3D_MPR_Installation.mp4?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/vhv0g3unfk7pxql/3D_MPR_Installation.mp4?dl=0" rel="noopener nofollow ugc">https://dl.dropboxusercontent.com/s/vhv0g3unfk7pxql/3D_MPR_Installation.mp4?dl=0</a>
            </source></video>
          </div>


---

## Post #170 by @lassoan (2021-12-02 18:57 UTC)

<p>Thanks a lot for sharing. It is great to see how it all came together in the end!</p>

---

## Post #171 by @spycolyf (2021-12-02 23:11 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>The only thing that I think could be improved is how I adjust the color and opacity transforms for the 3D renderings. Could you view this video and let me know if this is what’s expected? I really don’t know what I’m doing here. I’m expecting that when I select CT BONE, I only see bone; when I select pulmonary arteries, I see the arteries, etc. And then I think my slider adjustments are all wrong. Do you agree?</p>
          <div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/closarimpzmupak/ColorOpacity.mp4?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/closarimpzmupak/ColorOpacity.mp4?dl=0" rel="noopener nofollow ugc">https://dl.dropboxusercontent.com/s/closarimpzmupak/ColorOpacity.mp4?dl=0</a>
            </source></video>
          </div>

<p>Thanks</p>

---

## Post #172 by @lassoan (2021-12-03 05:28 UTC)

<p>What you do is the simplest way of showing volume rendering and so it makes sense. The preset names describe what the default threshold and color scheme is designed for. Since opacified vessels and bones have the same intensity on CT, they cannot be separated by simply adjusting transfer functions. Therefore if you want to separate them and show only the vessels then you need at least an approximate segmentation.</p>
<p>Creating neural networks that can perform an approximate segmentation of major bones, organs, vasculature, etc. is partly already available (e.g., in NVidia AI-AssistedAnnotation, MONAILabel extensions). However, it would take some effort to extend it to all structures of interest and put together a processing workflow that perform the automatic segmentations and set up the desired visualization.</p>
<p>The processing workflow would be specific to a clinical application (anatomy, disease, treatment approach) and it might not be always fully automatic, so it may be out of scope of a general-purpose image viewer. Exposing more manual segmentation and quantification tools (Segment Editor, Markups, …) could be a more realistic goal, as these manual or semi-automatic tools are applicable to a wide range of clinical applications, but of course they would be more challenging for users to learn.</p>

---

## Post #173 by @spycolyf (2021-12-08 15:43 UTC)

<p>Thanks so much <a class="mention" href="/u/lassoan">@lassoan</a>! You’ve been a great help as has been <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/mikebind">@mikebind</a> <a class="mention" href="/u/pieper">@pieper</a> and others. But a special thanks to <a class="mention" href="/u/jcfr">@jcfr</a> and and <a class="mention" href="/u/superlib">@superlib</a>. They gave me my initial head start.</p>
<p>No word yet on contributing back to open source. I’ll keep pushing from my position. But, even if it does not happen, I know you guys can whip this thing up fast if necessary.</p>
<p>Thanks,</p>
<p>Doug</p>

---

## Post #174 by @spycolyf (2021-12-08 15:44 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>My apologies, I just realized I’m posting this in the wrong thread. Could you move it to the SlicerQREADS thread?</p>
<p>Thanks</p>

---
