# Let me know how to set MONAI Label server in MONAI Label module

**Topic ID**: 24177
**Date**: 2022-07-05
**URL**: https://discourse.slicer.org/t/let-me-know-how-to-set-monai-label-server-in-monai-label-module/24177

---

## Post #1 by @platanus (2022-07-05 07:02 UTC)

<p>Hello. All members of 3D-Slicer</p>
<p>I have a question for setting of MONAI Label module in 3D-Slicer.</p>
<p>What should I input in ‘MONAI Label server’ option as following image? (I have no local IP address, I’m using wifi.)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db36417a2dc08093ac5f6801b3859dcf3d1da2c5.png" data-download-href="/uploads/short-url/vheO7NzAllPMLQdP5LIxXnbBJtz.png?dl=1" title="MONAI_setting" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db36417a2dc08093ac5f6801b3859dcf3d1da2c5_2_690x410.png" alt="MONAI_setting" data-base62-sha1="vheO7NzAllPMLQdP5LIxXnbBJtz" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db36417a2dc08093ac5f6801b3859dcf3d1da2c5_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db36417a2dc08093ac5f6801b3859dcf3d1da2c5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db36417a2dc08093ac5f6801b3859dcf3d1da2c5.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MONAI_setting</span><span class="informations">793×472 23.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please, let me know how to input accurate MONAI Label server.</p>

---

## Post #2 by @rbumm (2022-07-05 12:15 UTC)

<p>You will need to install and run MONAI Label itself on your local computer (<a href="https://github.com/Project-MONAI/MONAILabel">see here</a> → Installation) or collaborate with somebody who provides a MONAI Label server and tells you the IP address that you could connect to.</p>
<p>To fetch the active MONAI Label models you would need to press the green button in your above image.</p>

---

## Post #3 by @platanus (2022-07-06 00:58 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>Thank you for answering my question.</p>
<p>When I input ‘<a href="http://localhost:8000/" rel="noopener nofollow ugc">http://localhost:8000/</a>’ in input item of MONAI Label server. It occurs error as following image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ab8abe4bf813bd3d6a99691c4132c64e2f78344.png" data-download-href="/uploads/short-url/65VI3itvcI6tSsu2oXK90dukaFe.png?dl=1" title="MONAI_server_input" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ab8abe4bf813bd3d6a99691c4132c64e2f78344_2_690x405.png" alt="MONAI_server_input" data-base62-sha1="65VI3itvcI6tSsu2oXK90dukaFe" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2ab8abe4bf813bd3d6a99691c4132c64e2f78344_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ab8abe4bf813bd3d6a99691c4132c64e2f78344.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ab8abe4bf813bd3d6a99691c4132c64e2f78344.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MONAI_server_input</span><span class="informations">787×463 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a6fdccb738247415ef2308cccd347007aa18142.png" alt="3d-slicer MONAI_Label Error" data-base62-sha1="fbAh7qbqOZYlEYunCAIy1aML0A2" width="664" height="136"></p>
<p>Is there the solution?</p>

---

## Post #4 by @muratmaga (2022-07-06 03:27 UTC)

<aside class="quote no-group" data-username="platanus" data-post="3" data-topic="24177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecb155/48.png" class="avatar"> platanus:</div>
<blockquote>
<p>Is there the solution?</p>
</blockquote>
</aside>
<p>From your response it is not clear whether you have started MonaiLabel server or not? What happens when you type that address to a web browser?</p>

---

## Post #5 by @platanus (2022-07-06 04:28 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thank you answering my question. When I input my address(<a href="http://localhost:8000" rel="noopener nofollow ugc">http://localhost:8000</a>) in my web browser, It occurs error that couldn’t connect in web browser.</p>

---

## Post #6 by @muratmaga (2022-07-06 04:29 UTC)

<p>looks like you didn’t start the monaiLabel server. Follow the <a href="https://github.com/Project-MONAI/MONAILabel#installation" rel="noopener nofollow ugc">installation instructions</a> as <a class="mention" href="/u/rbumm">@rbumm</a> pointed out.</p>

---

## Post #7 by @platanus (2022-07-06 08:21 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
Yes. I installed MONAI Label plugin as you and others inform installation instruction.</p>
<p>I conducted in 3d-slicer mode as follows.</p>
<h2><a name="p-80459-installing-monailabel-plugin-1" class="anchor" href="#p-80459-installing-monailabel-plugin-1" aria-label="Heading link"></a>Installing MONAILabel Plugin</h2>
<p>Pick one of the following options to install MONAILabel Plugin for 3D Slicer</p>
<h3><a name="p-80459-install-3d-slicer-preview-version-with-in-built-plugin-2" class="anchor" href="#p-80459-install-3d-slicer-preview-version-with-in-built-plugin-2" aria-label="Heading link"></a>Install 3D Slicer Preview Version with in-built Plugin</h3>
<ul>
<li>Download and Install <a href="https://download.slicer.org/" rel="noopener nofollow ugc">3D Slicer</a> <strong>Preview version</strong></li>
<li>Go to <strong>View</strong> → <strong>Extension Manager</strong> → <strong>Active Learning</strong> → <strong>MONAI Label</strong></li>
<li>Install MONAI Label plugin</li>
<li><em><strong>Restart</strong></em> 3D Slicer</li>
</ul>
<blockquote>
<p>To update the plugin to latest version, you have to uninstall existing 3D Slicer version and download + install new preview version of 3D Slicer again.</p>
</blockquote>
<h3><a name="p-80459-install-plugin-in-developer-mode-3" class="anchor" href="#p-80459-install-plugin-in-developer-mode-3" aria-label="Heading link"></a>Install Plugin in Developer Mode</h3>
<ul>
<li><code>git clone git@github.com:Project-MONAI/MONAILabel.git</code></li>
<li>Open 3D Slicer: Go to <strong>Edit</strong> → <strong>Application Settings</strong> → <strong>Modules</strong> → <strong>Additional Module Paths</strong></li>
<li>Add New Module Path: <em>&lt;FULL_PATH&gt;</em>/plugins/slicer/MONAILabel</li>
<li><em><strong>Restart</strong></em> 3D Slicer</li>
</ul>
<h3><a name="p-80459-plugin-settings-4" class="anchor" href="#p-80459-plugin-settings-4" aria-label="Heading link"></a>Plugin Settings</h3>
<p>User can change some default behavior for the plugin. Go to <strong>Edit</strong> → <strong>Application Settings</strong> → <strong>MONAI Label</strong></p>
<p>I was done installation and MONAI Label setting.</p>
<p>When I input sever address that is “<a href="http://localhost:8000" rel="noopener nofollow ugc">http://localhost:8000</a>”, It occurs error as it is same error above.</p>
<p>And I input my address(<a href="http://localhost:8000/" rel="noopener nofollow ugc">http://localhost:8000</a>) in my web browser again, but it also occurs error.</p>
<p>Please, inform me regarding how to set MONAI Label server and check available port number in MONAI server.</p>

---

## Post #8 by @rbumm (2022-07-06 12:13 UTC)

<p>Dear Platanus <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Please understand that it is <strong>not enough to just install the MONAI Label extension</strong>.  You will need a server, either locally - on your computer, or remotely, on the internet.</p>
<p>Option 1 (local) :<br>
You <strong>install</strong> the complete MONAI Label software package and server on your local computer.<br>
Please refer to the MONAI Label GitHub Page <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">or this document</a> on how to do that. The computer needs to have a medium to high-end Nvidia GPU.</p>
<p>Then you would need to <strong>run</strong> the server from the command line, only then start 3D Slicer and use the MONAI Label extension by just pressing the green button mentioned above, without putting anything in the address line.</p>
<p>Option 2 (internet):<br>
You have a coworker who provides a MONAI Label server. Then start 3D Slicer, call the MONAI Label extension, enter the IP address that your coworker tells you, and only then press the green button.</p>

---

## Post #10 by @platanus (2022-07-09 06:27 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>Thank you for answering details.</p>
<p>I conducted process as you had said.</p>
<p>First, I finished setting of IP address in my local pc.<br>
Second, I conducted process regarding setting of MONAI Label sever that you linked above.</p>
<p>After setting IP address in my local PC and installing MONAI Label software package, I tested ‘localhost’ in web browser. But it occurs error message that is “localhost refused to connect.” in web browser. It also occurs error in 3D-Slicer as follow.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77d8f044c6ed4335ebe1423cd147eeee22799255.png" alt="image" data-base62-sha1="h6dBFVEjO22yO80st4PQxS7ZH2B" width="502" height="99"></p>

---

## Post #11 by @rbumm (2022-07-09 08:03 UTC)

<p>In case the installation of MONAI Label outlined above succeeded, you should be able to start the MONAI Label server in a PowerShell (Windows 11) and connect from Slicer 5.1 as follows:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1f95ed1943416c54d6585376803bd57de420276.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1f95ed1943416c54d6585376803bd57de420276.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1f95ed1943416c54d6585376803bd57de420276.mp4</a>
    </source></video>
  </div><p></p>
<p>The procedure is similar on Mac or Linux.</p>

---

## Post #12 by @platanus (2022-07-13 00:32 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>Thank you for answering details to me.</p>
<p>I could solve above problem because of <a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/muratmaga">@muratmaga</a>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/247fabeb24926752604c602bf184051867b662e8.png" data-download-href="/uploads/short-url/5cSISZT457bdg5W4BhtUNio36CQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/247fabeb24926752604c602bf184051867b662e8.png" alt="image" data-base62-sha1="5cSISZT457bdg5W4BhtUNio36CQ" width="690" height="77" data-dominant-color="F4F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×89 2.68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you very much again.</p>

---

## Post #13 by @linda_varghese (2023-06-16 13:56 UTC)

<p>Hi ,<br>
Could you please help me with the Monai server run, as it showing some error even after I use windows Power shell.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f3cd47ae16727adffc0246899bb6585c9994ab.png" data-download-href="/uploads/short-url/5Z7V09WLJfDu5Wb0ufvJvH2uGgj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29f3cd47ae16727adffc0246899bb6585c9994ab_2_690x319.png" alt="image" data-base62-sha1="5Z7V09WLJfDu5Wb0ufvJvH2uGgj" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29f3cd47ae16727adffc0246899bb6585c9994ab_2_690x319.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f3cd47ae16727adffc0246899bb6585c9994ab.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f3cd47ae16727adffc0246899bb6585c9994ab.png 2x" data-dominant-color="D6D4D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">692×320 87.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
