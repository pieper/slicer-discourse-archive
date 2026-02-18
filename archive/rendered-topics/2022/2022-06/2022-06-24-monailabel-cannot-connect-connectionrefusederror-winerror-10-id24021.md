# MONAILabel cannot connect: ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

**Topic ID**: 24021
**Date**: 2022-06-24
**URL**: https://discourse.slicer.org/t/monailabel-cannot-connect-connectionrefusederror-winerror-10061-no-connection-could-be-made-because-the-target-machine-actively-refused-it/24021

---

## Post #1 by @hourglassnam (2022-06-24 10:20 UTC)

<p>Hello,<br>
I have tried running the MONAILabel module but keep getting a connection refused error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/173435b73aa4fff6ab598708d88fb539197bf3f5.png" data-download-href="/uploads/short-url/3jgQ8gfg5t5esRS02Sp8iWM45fv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173435b73aa4fff6ab598708d88fb539197bf3f5_2_690x257.png" alt="image" data-base62-sha1="3jgQ8gfg5t5esRS02Sp8iWM45fv" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173435b73aa4fff6ab598708d88fb539197bf3f5_2_690x257.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173435b73aa4fff6ab598708d88fb539197bf3f5_2_1035x385.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/173435b73aa4fff6ab598708d88fb539197bf3f5_2_1380x514.png 2x" data-dominant-color="F6F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1901×710 67.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At first, I suspected the firewall to be the reason and allowed the slicer.exe app through the window firewall on the control panel.</p>
<p>However, it still did not work.</p>
<p>So next thing I checked was the port number.</p>
<p>I found out that the default server was serving at <a href="http://127.0.0.1:8000/" rel="noopener nofollow ugc">http://127.0.0.1:8000/</a>.</p>
<p>When I checked my computer with the command below, port number 8000 did not exist.</p>
<blockquote>
<p>netstat -an|findstr 8000</p>
</blockquote>
<p>So I am wondering not having the port can be the reason for this error and how to solve it.</p>
<p>Thank you always for your help.</p>

---

## Post #2 by @lassoan (2022-06-24 12:35 UTC)

<p>When I start MONAILabel server I see something like this:</p>
<pre><code class="lang-bash">root@perklabseg:/opt/monai# monailabel start_server --app /opt/monai/MONAILabel/apps/radiology --studies /opt/monai/MONAILabel/datasets/Task09_Spleen/imagesTr --conf models deepedit --port 9005 --host 127.0.0.1
Using PYTHONPATH=/opt:
[2022-06-24 12:29:09,732] [387] [MainThread] [INFO] (__main__:292) - USING:: app = /opt/monai/MONAILabel/apps/radiology
[2022-06-24 12:29:09,732] [387] [MainThread] [INFO] (__main__:292) - USING:: studies = /opt/monai/MONAILabel/datasets/Task09_Spleen/imagesTr
[2022-06-24 12:29:09,732] [387] [MainThread] [INFO] (__main__:292) - USING:: verbose = INFO
[2022-06-24 12:29:09,732] [387] [MainThread] [INFO] (__main__:292) - USING:: conf = [['models', 'deepedit']]
[2022-06-24 12:29:09,732] [387] [MainThread] [INFO] (__main__:292) - USING:: host = 127.0.0.1
[2022-06-24 12:29:09,732] [387] [MainThread] [INFO] (__main__:292) - USING:: port = 9005
[2022-06-24 12:29:09,732] [387] [MainThread] [INFO] (__main__:292) - USING:: uvicorn_app = monailabel.app:app
...
[2022-06-24 12:29:10,649] [387] [MainThread] [INFO] (uvicorn.error:59) - Application startup complete.
[2022-06-24 12:29:10,649] [387] [MainThread] [INFO] (uvicorn.error:206) - Uvicorn running on http://127.0.0.1:9005 (Press CTRL+C to quit)
</code></pre>
<p>After this, if I open the server URL in a web browser, I see this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/506e1371792607b7cb120f167a1924ed87942940.png" data-download-href="/uploads/short-url/btw27JSxV7ySEcQ0tPngpj7N4qs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506e1371792607b7cb120f167a1924ed87942940_2_690x419.png" alt="image" data-base62-sha1="btw27JSxV7ySEcQ0tPngpj7N4qs" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506e1371792607b7cb120f167a1924ed87942940_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506e1371792607b7cb120f167a1924ed87942940_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506e1371792607b7cb120f167a1924ed87942940_2_1380x838.png 2x" data-dominant-color="EAEEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2099×1276 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you see something similar on your computer?</p>

---

## Post #3 by @hourglassnam (2022-06-24 13:24 UTC)

<p>Thank you, Lassoan, for your response!<br>
Sadly, I do not see any message on my python interactor after loading the MONAILabel module.</p>
<p>Confirming the server URL for the TOMAAT also gives an error message as below, and I wonder if this is due to the same reason.</p>
<blockquote>
<p>USING HOST IN DIRECT CONNECTION PANE<br>
Execute GET by global HTTPS CERT system<br>
Starting new HTTPS connection (1): localhost<br>
Execute GET UNSAFE<br>
Starting new HTTPS connection (1): localhost<br>
Host is not reachable! (<a href="https://localhost:9000/interface" rel="noopener nofollow ugc">https://localhost:9000/interface</a>)</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b89295c3669ca0e87401f7019058ec30dcf42663.png" data-download-href="/uploads/short-url/qkNUvOYja9yVVvnn43FFyAVfylJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b89295c3669ca0e87401f7019058ec30dcf42663_2_651x500.png" alt="image" data-base62-sha1="qkNUvOYja9yVVvnn43FFyAVfylJ" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b89295c3669ca0e87401f7019058ec30dcf42663_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b89295c3669ca0e87401f7019058ec30dcf42663_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b89295c3669ca0e87401f7019058ec30dcf42663_2_1302x1000.png 2x" data-dominant-color="F7F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1952×1497 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-06-24 16:44 UTC)

<aside class="quote no-group" data-username="hourglassnam" data-post="3" data-topic="24021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>Sadly, I do not see any message on my python interactor after loading the MONAILabel module.</p>
</blockquote>
</aside>
<p>Installing MONAILabel module is not sufficient. You also need to configure and start a MONAILabel server (outside Slicer).</p>

---

## Post #5 by @hourglassnam (2022-06-27 10:12 UTC)

<p>Thank you Lassoan for your reply!<br>
After your feedback,  I went to <a href="https://github.com/Project-MONAI/MONAILabel" rel="noopener nofollow ugc">GitHub link</a> and tried to install the monailabel on my computer using window cmd.<br>
I was able to install the monailabel-weekly outside the slicer. However, an error message pops up when I try to move to the next step.<br>
Following is the script I tried to run and the error message I get.<br>
Sorry for bothering you again, but could you please give me some advice?<br>
Thank you always for your help.</p>
<blockquote>
<p>monailabel --help<br>
monailabel apps --download --name radiology --output apps<br>
monailabel datasets --download --name Task09_Spleen --output datasets</p>
<p><span class="hashtag-raw">#returned</span> error message<br>
‘monailabel’ is not recognized as an internal or external command, operable program or batch file</p>
</blockquote>

---

## Post #6 by @muratmaga (2022-06-27 15:22 UTC)

<p>You</p>
<aside class="quote no-group" data-username="hourglassnam" data-post="5" data-topic="24021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hourglassnam/48/11796_2.png" class="avatar"> hourglassnam:</div>
<blockquote>
<p>‘monailabel’ is not recognized as an internal or external command, operable program or batch file</p>
</blockquote>
</aside>
<p>This means monailabel has not been installed (or at least not correctly installed and executable is not on the path).</p>
<p>Did you follow <a href="https://docs.monai.io/projects/label/en/latest/installation.html">the instructions to install MonaiLabel</a>? Which method did you use?</p>

---

## Post #8 by @hourglassnam (2022-06-28 08:37 UTC)

<p>Hello, <a href="https://discourse.slicer.org/u/muratmaga">@muratmaga</a>!</p>
<p>Thank you for your reply.</p>
<p>Yes, I have followed the instruction you linked.</p>
<p>Here are my steps:</p>
<ol>
<li>opened Window cmd</li>
<li>Install the following Python libraries</li>
<li>used command “pip install monailabel-weekly”</li>
<li>checked if the installed package “pip list”
<ul>
<li>monai and monailabel-weekly(0.4.dev2226) were on the list</li>
</ul>
</li>
</ol>
<p>I uninstalled the package and tried it again on the Anaconda Powershell Powershell Prompt (Anaconda3) but it gives me following message.</p>
<blockquote>
<p>(base) PS C:\Windows\system32&gt; monailabel --help</p>
<p>Using PYTHONPATH=C:\ProgramData;</p>
<p>OMP: Error <span class="hashtag-raw">#15:</span> Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.</p>
<p>OMP: Hint This means that multiple copies of the OpenMP runtime have been linked into the program. That is dangerous, since it can degrade performance or cause incorrect results. The best thing to do is to ensure that only a single OpenMP runtime is linked into the process, e.g. by avoiding static linking of the OpenMP runtime in any library. As an unsafe, unsupported, undocumented workaround you can set the environment variable KMP_DUPLICATE_LIB_OK=TRUE to allow the program to continue to execute, but that may cause crashes or silently produce incorrect results. For more information, please see <a href="http://www.intel.com/software/products/support/" rel="noopener nofollow ugc">http://www.intel.com/software/products/support/</a>.</p>
</blockquote>

---

## Post #9 by @hourglassnam (2022-06-28 13:18 UTC)

<p>Here is the validation of the monai installation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/901033cd5b8cb93019b3787379981b00a3df8104.png" data-download-href="/uploads/short-url/kyrt5js0fQL9BTnhagLCaIlH38g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/901033cd5b8cb93019b3787379981b00a3df8104_2_690x407.png" alt="image" data-base62-sha1="kyrt5js0fQL9BTnhagLCaIlH38g" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/901033cd5b8cb93019b3787379981b00a3df8104_2_690x407.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/901033cd5b8cb93019b3787379981b00a3df8104_2_1035x610.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/901033cd5b8cb93019b3787379981b00a3df8104_2_1380x814.png 2x" data-dominant-color="141414"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1895×1120 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @muratmaga (2022-06-28 17:50 UTC)

<p>I don’t have experience running MonaiLabel through the python environment, I only used it through docker which simplified things quite a bit.</p>
<p>Perhaps you can take a look at <a class="mention" href="/u/rbumm">@rbumm</a> <a href="https://discourse.slicer.org/t/how-to-start-with-monailabel-for-new-models/21063/88">explanations here:</a></p>

---

## Post #11 by @rbumm (2022-06-28 20:12 UTC)

<p>Hi,</p>
<p>Maybe this <a href="https://docs.google.com/document/d/1azFpJutBVJEW9W_riYZlXzrXac58ToCEzNTAwkzNf2c/edit?usp=sharing">Google doc</a> helps.<br>
Was not use Anaconda at all during recent installation processes.</p>

---

## Post #12 by @lassoan (2022-06-29 04:39 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> would you mind uploading these instructions to your <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/">project page</a>? Google docs are not indexed by web search services, cannot be found by searching in the ProjectWeeks repository, etc.</p>

---

## Post #13 by @hourglassnam (2022-06-29 08:21 UTC)

<p>Thank you guys for all the help!!</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a>, I was able to make the monailabel work with the Google doc you provided! I can’t even express how grateful I am for your help!<br>
I think the problem was that I was at my system32 directory, not the user directory.</p>
<p>Also, I tried running the monailabel with docker, which was much more straightforward, just like <a class="mention" href="/u/muratmaga">@muratmaga</a> have mentioned! Thank you!</p>

---

## Post #14 by @rbumm (2022-06-29 09:48 UTC)

<p>Absolutely,  <a class="mention" href="/u/lassoan">@lassoan</a><br>
The information <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">is now here</a> and linked from the MONAI Label lung project page. The Google doc received a ‘move page’ notice.</p>

---

## Post #15 by @lassoan (2022-06-29 14:32 UTC)

<p>Perfect, thank you very much!</p>

---

## Post #16 by @diazandr3s (2022-07-04 11:29 UTC)

<p>Many thanks for the support, <a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a>  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #17 by @rbumm (2022-07-04 16:27 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> could you maybe add a few points about how you installed MONAI Label through docker exactly? Thank you.<br>
ping <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>

---

## Post #18 by @diazandr3s (2022-07-04 20:49 UTC)

<p>This is a good point.</p>
<p>I’ve mostly used Docker on Linux, but it should also work on Windows.</p>
<p>The first step is to make sure <a href="https://docs.nvidia.com/ai-enterprise/deployment-guide/dg-docker.html" rel="noopener nofollow ugc">nvidia docker is installed on the computer</a>. Then, by running this command you should be able to start the docker container with MONAI Label installed:</p>
<p><code>docker run --gpus all --rm -ti --ipc=host --net=host projectmonai/monailabel:latest bash</code></p>
<p>Here I show the ways of installing MONAI Label: <a href="https://www.youtube.com/watch?v=8y1OBQs2wis" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label Installation - PyPi, Docker, and GitHub - YouTube</a></p>

---

## Post #19 by @muratmaga (2022-07-05 15:56 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="17" data-topic="24021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> could you maybe add a few points about how you installed MONAI Label through docker exactly? Thank you.</p>
</blockquote>
</aside>
<p>Happy to, but can I edit that link?</p>

---

## Post #20 by @rbumm (2022-07-05 16:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> could you maybe enable <a class="mention" href="/u/muratmaga">@muratmaga</a> for editing the <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.md">37th Project Week MONAIL Label installation  GitHub</a> document?  Thank you<br>
<a class="mention" href="/u/muratmaga">@muratmaga</a> feel free to add your name at the top <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #21 by @lassoan (2022-07-06 18:32 UTC)

<p>Everyone can edit the Project Week pages. If you don’t have direct write access then GitHub will offer you to create a pull request for you - just accept that.</p>

---

## Post #22 by @Dexter_Luth (2023-07-21 20:46 UTC)

<p>For anyone in the future who would still like to download monailabel through anaconda, this error (OMP: Error <span class="hashtag-raw">#15:</span> Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.) is essentially caused by multiple libiomp5md.dll files. The simplest solution that I found was to delete the older libiomp5md.dll file in the anaconda directory. After that everything should run smoothly. Path to the file is C:\Users\username\Anaconda3\Library\bin or C:\Users\username\Anaconda3\envs\your_env_name\Library\bin\ if you are in an env.<br>
Others solutions are discussed <a href="https://stackoverflow.com/questions/20554074/sklearn-omp-error-15-initializing-libiomp5md-dll-but-found-mk2iomp5md-dll-a" rel="noopener nofollow ugc">here</a> if you would like to try them instead</p>

---
