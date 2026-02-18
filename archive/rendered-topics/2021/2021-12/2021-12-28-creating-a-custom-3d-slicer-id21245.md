# Creating a custom 3D Slicer

**Topic ID**: 21245
**Date**: 2021-12-28
**URL**: https://discourse.slicer.org/t/creating-a-custom-3d-slicer/21245

---

## Post #1 by @Karthik (2021-12-28 07:19 UTC)

<p>Hi.<br>
I wish to create a custom Slicer. Something like <a href="http://salt.slicer.org/" rel="noopener nofollow ugc">http://salt.slicer.org/</a><br>
I have build Slicer v4.11.20210226 on my machine (ubuntu 20.04) before.<br>
Now, I wish to customize the application. Change the name, logo, looks, modules, etc.<br>
I have been able to change logos quiet easily. Just change the logos and build Slicer, I got it to work. But, I’m still unclear on how to make other changes.</p>
<p>I found a custom app template <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/tree/master/%7B%7Bcookiecutter.project_name%7D%7D" class="inline-onebox" rel="noopener nofollow ugc">SlicerCustomAppTemplate/{{cookiecutter.project_name}} at master · KitwareMedical/SlicerCustomAppTemplate · GitHub</a><br>
I tried to use this and ended up with many errors. This page hadn’t been updated in a couple of years.</p>
<p>Please guide me to other resources/instructions to create a customized 3D Slicer v4.11.20210226 with changes in style, logo, name, etc.</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2021-12-28 13:55 UTC)

<p>The custom app template you linked works well. It is actually live and maintained; it was updated last month. <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" class="inline-onebox">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom 3D Slicer application</a></p>

---

## Post #3 by @Karthik (2021-12-29 17:27 UTC)

<p>Hi. So, I’ve tried using the SlicerCustomAppTemplate again. I was getting some errors but maybe its because I’m doing something wrong.</p>
<p>First, I used ‘cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate’ to create the template.<br>
Then, I followed the steps given in <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> to change any settings if necessary.</p>
<p>Finally, I build it using instructions from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" class="inline-onebox" rel="noopener nofollow ugc">Build Instructions — 3D Slicer documentation</a>.</p>
<p>It runs for a couple of hours and build fails. These are the errors that I am getting</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d489dad03d1d5495a71fda25b595f3baf4fe0bc0.jpeg" data-download-href="/uploads/short-url/ukczIJuKYNVmd3Nw36cQp0AQZc4.jpeg?dl=1" title="build_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d489dad03d1d5495a71fda25b595f3baf4fe0bc0_2_690x127.jpeg" alt="build_error" data-base62-sha1="ukczIJuKYNVmd3Nw36cQp0AQZc4" width="690" height="127" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d489dad03d1d5495a71fda25b595f3baf4fe0bc0_2_690x127.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d489dad03d1d5495a71fda25b595f3baf4fe0bc0_2_1035x190.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d489dad03d1d5495a71fda25b595f3baf4fe0bc0_2_1380x254.jpeg 2x" data-dominant-color="3F1C34"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">build_error</span><span class="informations">1857×343 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In order to make sure that my logos are not the cause of the problem, I have not changed anything. Just let the default logos be. In fact, the only change I made is the Slicer tag to v4.11.20210226 in the CMakeLists.txt file and started the build process.</p>
<p>I don’t understand what caused this error. Please help me decode this. It will be very helpful for my build.</p>

---

## Post #4 by @Karthik (2021-12-29 17:41 UTC)

<p>I have checked qMRMLWidget class and found the following.<br>
qMRMLWidget Class in 4.13 has a Static Public Member Function called pixmapFromIcon as seen here <a href="https://apidocs.slicer.org/master/classqMRMLWidget.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: qMRMLWidget Class Reference</a>.</p>
<p>But, I want to build Slicer 4.11.20210226. It doesn’t seem to have pixmapFromIcon as seen here <a href="https://apidocs.slicer.org/v4.11/classqMRMLWidget.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: qMRMLWidget Class Reference</a></p>
<p>Is my analysis correct?<br>
What steps can I take to get this working?</p>

---

## Post #5 by @jcfr (2021-12-29 18:43 UTC)

<p>After running the following:</p>
<pre><code class="lang-auto">pip install cookiecutter jinja2-github
cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate
</code></pre>
<p>the Slicer SHA injected in the top-level <code>CMakeLists.txt</code> will correspond to the latest one and you should keep it as such.</p>
<p>The template is maintained up-to-date so that it builds against the latest version of Slicer.</p>
<p>The <code>Step 2: Customize Slicer using CMake options</code> of the blog provides some general information and is not intended to prescribe a specific SHA.</p>
<p>Could you indicate the value used in the top level of you your <code>CMakeLists.txt</code> ?</p>

---

## Post #6 by @pieper (2021-12-29 18:45 UTC)

<p>Creating a custom app is a pretty advanced topic, meaning that you do it when you need total control of the build process, dependency libraries, and app behavior.  With this much control it means there are a million options to consider and these need to be kept up to date with changes at various levels, so only the latest code versions are maintained and most likely to work so you should always start there before trying to customize.</p>

---

## Post #7 by @jcfr (2021-12-29 18:46 UTC)

<blockquote>
<p>I want to build Slicer 4.11.20210226</p>
</blockquote>
<p>Considering we will soon release Slicer 5.0 (see milestone <a href="https://github.com/Slicer/Slicer/milestone/1">here</a>), I suggest you build your application using the latest version (basically the one injected by default in the <code>CMakeLists.txt</code>)</p>
<p>Is there a specific reason for using the “older” version ?</p>
<p>Ultimately, if you would like to create a custom app based on an older version of Slicer, you would have to revert changes added to the template that were introduced to support the latest one.</p>

---

## Post #8 by @Karthik (2021-12-30 08:28 UTC)

<p>So, I have tried to build it again. This time, I didn’t want to change anything. Hence, I used the default git tag in the top level CMakeLists.txt which was the latest commit in Slicer git repository. I have made no other changes to the file. In fact, I just did ‘cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate’ with the name as SSLIP. Then, I created another directory named SSLIP-rel. I performed cmake. Then, make.</p>
<p>However, even without making any changes to the SlicerCustomAppTemplate, I am still unable to complete the build.<br>
This is the latest error that I got.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28f046820d9d6a62b9ad2bfe0dc070fa7e7bac6c.png" data-download-href="/uploads/short-url/5Q9SXQbOnJLw6uSmaMF0fdV3FBW.png?dl=1" title="attempt11_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28f046820d9d6a62b9ad2bfe0dc070fa7e7bac6c_2_690x388.png" alt="attempt11_error" data-base62-sha1="5Q9SXQbOnJLw6uSmaMF0fdV3FBW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28f046820d9d6a62b9ad2bfe0dc070fa7e7bac6c_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28f046820d9d6a62b9ad2bfe0dc070fa7e7bac6c_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28f046820d9d6a62b9ad2bfe0dc070fa7e7bac6c_2_1380x776.png 2x" data-dominant-color="37152C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">attempt11_error</span><span class="informations">1920×1080 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It says that Slicer_MAIN_PROJECT_WC_REVISION is mandatory. What am I doing wrong?</p>

---

## Post #9 by @Karthik (2021-12-30 08:30 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="21245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Is there a specific reason for using the “older” version ?</p>
</blockquote>
</aside>
<p>I wanted to build custom Slicer based on v4.11.20210226 because it is currently the stable version. v4.13 is in preview release. It is not essential that I build using this version only.<br>
After reading your comments, I have tried to build the latest one, but still got some build errors. I posted a photo of those in this forum.</p>

---

## Post #10 by @Karthik (2021-12-30 08:38 UTC)

<p>I am writing in detail the steps that I followed to build custom Slicer. Please correct me if I am wrong.<br>
Step1: <strong>cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate</strong>. Then I get prompt in terminal to fill in application name, project name etc. which I have filled in accordingly. The name of the directory that is created is called SSLIP.<br>
At this step I would normally make changes to CMakeLists.txt, logos, etc. But to make sure that I am not changing anything important, I have not touched any file and proceeded to the next step.</p>
<p>Step2: created another directory at the same level of SSLIP called SSLIP-rel.</p>
<p>Step3: Inside SSLIP-rel, I opened a terminal and entered the following command.<br>
<strong>cmake -DCMAKE_BUILD_TYPE:STRING=Release …/SSLIP</strong></p>
<p>Step4: Then I did <strong>make</strong>.<br>
The exact command I used is <strong>make 2&gt;&amp;1 &gt;attempt11_output.log</strong>. This is to redirect the output to the log file.</p>
<p>The build runs for a couple of hours and then crashes with errors.</p>

---

## Post #11 by @Dwij_Mistry (2021-12-30 13:47 UTC)

<aside class="quote no-group" data-username="Karthik" data-post="10" data-topic="21245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9fc348/48.png" class="avatar"> Karthik:</div>
<blockquote>
<p>The build runs for a couple of hours and then crashes with errors.</p>
</blockquote>
</aside>
<p>Can you please share errors.</p>
<p>Mostly we get error because of long file path.<br>
If you got error because of long file path then try to have only one character named folder.</p>

---

## Post #12 by @Karthik (2021-12-30 14:45 UTC)

<p>I shared the error above in this forum. I took a screenshot and the image is called attempt11_error.</p>
<p>It shows CMake Error: Slicer_MAIN_PROJECT_WC_REVISION is mandatory</p>

---

## Post #13 by @jcfr (2021-12-30 23:41 UTC)

<p>It turns out the root cause is outlined earlier in the error message:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a4e9615468731b247b4f293c4fd189ac3edb1de.png" alt="image" data-base62-sha1="hrYCxKUYtB2aVQH1cTZob0oSpJ4" width="597" height="54"></p>
<p>Nitpick: In the future, make sure to copy/paste the text of the error. It makes copy/pasting possible and speedup the process of trying to understand the problem.</p>
<h3><a name="p-71921-solution-1" class="anchor" href="#p-71921-solution-1" aria-label="Heading link"></a>Solution</h3>
<p>Consider running <code>git init</code> in the <code>SSLIP</code> source tree and adding at least one commit.</p>
<h3><a name="p-71921-background-2" class="anchor" href="#p-71921-background-2" aria-label="Heading link"></a>Background</h3>
<p>Error is report by the module <code>SlicerConfigureVersionHeaderTarget</code> expecting a revision to be set.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/CMake/SlicerConfigureVersionHeaderTarget.cmake#L129-L151">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/CMake/SlicerConfigureVersionHeaderTarget.cmake#L129-L151" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/CMake/SlicerConfigureVersionHeaderTarget.cmake#L129-L151" target="_blank" rel="noopener">CMake/SlicerConfigureVersionHeaderTarget.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/CMake/SlicerConfigureVersionHeaderTarget.cmake#L129-L151" rel="noopener"><code>3de75b9c4</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="129" style="counter-reset: li-counter 128 ;">
          <li># Variables expected to be set by 'SlicerVersion' module.</li>
          <li>set(expected_defined_vars</li>
          <li>  Slicer_BUILDDATE</li>
          <li>  Slicer_VERSION</li>
          <li>  Slicer_VERSION_FULL</li>
          <li>  Slicer_REVISION</li>
          <li>  Slicer_WC_REVISION</li>
          <li>  Slicer_WC_REVISION_HASH</li>
          <li>  Slicer_WC_URL</li>
          <li></li>
          <li>  Slicer_MAIN_PROJECT_BUILDDATE</li>
          <li>  Slicer_MAIN_PROJECT_VERSION</li>
          <li>  Slicer_MAIN_PROJECT_VERSION_FULL</li>
          <li>  Slicer_MAIN_PROJECT_REVISION</li>
          <li>  Slicer_MAIN_PROJECT_WC_REVISION</li>
          <li>  Slicer_MAIN_PROJECT_WC_REVISION_HASH</li>
          <li>  Slicer_MAIN_PROJECT_WC_URL</li>
          <li>  )</li>
          <li>foreach(var ${expected_defined_vars})</li>
          <li>  if(NOT DEFINED ${var})</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/CMake/SlicerConfigureVersionHeaderTarget.cmake#L129-L151" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Original issue and possible discussion have been summarized here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6096">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6096" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6096" target="_blank" rel="noopener">Support configuring Slicer from a source archive</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-12-30" data-time="23:38:31" data-timezone="UTC">11:38PM - 30 Dec 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: Low
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

Attempting <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">to build Slicer from an archive of the source (instead of git repository) will fail with the following error:

```
CMake Error: Slicer_MAIN_PROJECT_WC_REVISION is mandatory
```

reported by checks implemented in https://github.com/Slicer/Slicer/blob/3de75b9c4c6f3ee9a1e5da17059b9f11517e16ab/CMake/SlicerConfigureVersionHeaderTarget.cmake#L129-L151

Error was originally discussed in https://discourse.slicer.org/t/creating-a-custom-3d-slicer/21245 after trying to build a custom application using [KitwareMedical/SlicerCustomAppTemplate](https://github.com/KitwareMedical/SlicerCustomAppTemplate) but without first creating a git repository.

## Describe the solution you'd like

Configuring from a directory not managed by version control should not fail.

Archive created from a source tree managed by version control should include hard-coded revision metadata.

## Describe alternatives you've considered

Only support configuring from a source tree managed by version control.

## Additional context

NA</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #14 by @Karthik (2022-01-01 03:02 UTC)

<p>Thank you for the advice. I ran <code>git init</code> and added a commit. I was successfully able to build Slicer.</p>
<p>However, I came into some problems.<br>
<strong>Problem1:</strong> I turned <strong>Slicer_BUILD_EXTENSIONMANAGER_SUPPORT</strong> ON in the top level CMakeLists.txt in the SlicerCustomAppTemplate as I wanted to download some extensions.<br>
The built Slicer has the Extension Manager. But no matter which extension I try to install, it doesn’t work.</p>
<p>For example, I have tried to install the SlicerVMTK extension. I even get a pop-up at the top right of the screen saying ‘Installed Extension SlicerVMTK’. But, the restart button at the bottom right corner of the screen doesn’t get activated. When I close and reopen Slicer, I cannot find the extension anywhere.</p>
<p>This is what I see in terminal when I try to install the SlicerVMTK extension.</p>
<blockquote>
<p>libpng warning: iCCP: known incorrect sRGB profile<br>
Retrieving extension metadata [ extensionId: 61cc101f342a877cb3f28a6a]<br>
Retrieving extension files [ extensionId: 61cc101f342a877cb3f28a6a ]<br>
Downloading extension [ item_id: 61cc101f342a877cb3f28a6a, file_id: 61ceb486342a877cb3f3dc34]<br>
Installed extension SlicerVMTK (61cc101f342a877cb3f28a6a) revision 8e3fdf6<br>
QPixmap::scaled: Pixmap is a null pixmap<br>
“” 1 “JQuery not loaded - Failed to trigger webkitvisibilitychange”</p>
</blockquote>
<p>But, the files are downloaded to the extensions folder. The same thing is happening with all the extensions.</p>
<p><strong>Problem2:</strong> I have written some Effects in Segment Editor which also don’t seem to be working in the customized Slicer, but were working for me before. Note: I have written and used the effects in Slicer v4.11.20210226 but the custom built Slicer is the latest commit (v4.13). Could this be the reason?</p>

---

## Post #15 by @Karthik (2022-01-02 15:37 UTC)

<p><strong>Problem3:</strong>  In my laptop (where the custom Slicer was built), I am able to launch the application successfully. It leads to the Slicer application home screen.</p>
<p>Then, I packaged the application (using <code>make package</code>). I am still able to launch the application. However, when I share the custom built Slicer application with someone else, they are unable to launch the application.<br>
Errors related to ‘libqt5’ are showing up.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa825d2c5023cfb944f6cce4bcfc1044e257db4d.jpeg" alt="libqt5_error1" data-base62-sha1="zK6FBIBKZnclEySBZd9uqHT1CBT" width="493" height="139"></p>
<p>Thinking that there might have been some problem with the build, I tried building Slicer again. This time I got the following error.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90adfddd3b9df1b815d0f0644002d1641a9023fb.jpeg" alt="libqt5_error2" data-base62-sha1="kDTwVK34ABwTBTwelyvaGjwskif" width="496" height="136"></p>
<p>In the directory where I have built Slicer, I searched for these shared object libraries, but I could not find them. However, the application still launches on my computer.<br>
Is there anything wrong with my build process?<br>
What changes do I need to make to solve this problem?</p>

---

## Post #16 by @Karthik (2022-01-03 04:08 UTC)

<aside class="quote no-group" data-username="Karthik" data-post="15" data-topic="21245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9fc348/48.png" class="avatar"> Karthik:</div>
<blockquote>
<p>However, when I share the custom built Slicer application with someone else, they are unable to launch the application.</p>
</blockquote>
</aside>
<p>I figured out that the new laptop on which Slicer is expected to run on also needs to have the support libraries installed as it does not come as part of superbuild as explained in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" class="inline-onebox" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a>.</p>
<p>Once I installed these using the following commands, Slicer successfully launched.</p>
<pre><code class="lang-auto">sudo apt update &amp;&amp; sudo apt install git subversion build-essential cmake cmake-curses-gui cmake-qt-gui \
  qt5-default qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev qtwebengine5-dev qtscript5-dev \
  qtbase5-private-dev libqt5x11extras5-dev libxt-dev
</code></pre>
<p>However, is it possible to get rid of these requirements and get them with the superbuild itself? When I download Slicer from the website, I don’t need these support libraries to run the application. Everything comes neatly packaged. Is it possible for me to do the same for custom Slicer build?</p>

---

## Post #17 by @Karthik (2022-01-03 04:30 UTC)

<aside class="quote no-group" data-username="Karthik" data-post="14" data-topic="21245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9fc348/48.png" class="avatar"> Karthik:</div>
<blockquote>
<p><strong>Problem1:</strong> I turned <strong>Slicer_BUILD_EXTENSIONMANAGER_SUPPORT</strong> ON in the top level CMakeLists.txt in the SlicerCustomAppTemplate as I wanted to download some extensions.<br>
The built Slicer has the Extension Manager. But no matter which extension I try to install, it doesn’t work.</p>
</blockquote>
</aside>
<p><strong>Solution:</strong> I now understand that if I build Slicer, then I have to build the extensions myself. I cannot install them through the extension manager due to ABI compatibility issues. Using the instructions from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions-build-system" class="inline-onebox" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a>, I was able to successfully build a custom Slicer application with vmtk extension as shown in the figure below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc5fcab101e0b24a6016e9f6459d3eb4962ad946.png" data-download-href="/uploads/short-url/qSqZPOFMxXUmHiFBMRkk6VWwbJQ.png?dl=1" title="slicervmtk_innerbuild" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc5fcab101e0b24a6016e9f6459d3eb4962ad946_2_690x148.png" alt="slicervmtk_innerbuild" data-base62-sha1="qSqZPOFMxXUmHiFBMRkk6VWwbJQ" width="690" height="148" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc5fcab101e0b24a6016e9f6459d3eb4962ad946_2_690x148.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc5fcab101e0b24a6016e9f6459d3eb4962ad946_2_1035x222.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc5fcab101e0b24a6016e9f6459d3eb4962ad946_2_1380x296.png 2x" data-dominant-color="DBDADA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicervmtk_innerbuild</span><span class="informations">1664×359 48.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This creates an executable named ‘SlicerWithSlicerVMTK’ which I am able to run.<br>
However, I now want to package this just like I would package Slicer using <code>make package</code>.  This is what I want to achieve.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/832daf496b290cd41dac591b586431b7ee83717e.png" data-download-href="/uploads/short-url/iIsqvZsid6Lwq6rbpU0rlk6uQFg.png?dl=1" title="slicersalt_package" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832daf496b290cd41dac591b586431b7ee83717e_2_690x73.png" alt="slicersalt_package" data-base62-sha1="iIsqvZsid6Lwq6rbpU0rlk6uQFg" width="690" height="73" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832daf496b290cd41dac591b586431b7ee83717e_2_690x73.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832daf496b290cd41dac591b586431b7ee83717e_2_1035x109.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832daf496b290cd41dac591b586431b7ee83717e_2_1380x146.png 2x" data-dominant-color="C6C4C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicersalt_package</span><span class="informations">1662×177 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To achieve this, I would normally to go the superbuild directory and run the command <code>make package</code>.</p>
<p>But, how do I package this now that I have an executable with SlicerVMTK?</p>
<p>Also, why has the name of the executable changed to ‘SlicerWithSlicerVMTK’. I want the name to be SSLIP. This is what I used in the customApplicationTemplate to build custom SLicer.</p>
<p>Thanks</p>

---

## Post #18 by @jcfr (2022-01-03 23:03 UTC)

<aside class="quote no-group" data-username="Karthik" data-post="17" data-topic="21245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/9fc348/48.png" class="avatar"> Karthik:</div>
<blockquote>
<p>But, how do I package this now that I have an executable with SlicerVMTK?</p>
</blockquote>
</aside>
<p>You could do the following:</p>
<ol>
<li>Create a custom application leveraging <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate#readme">KitwareMedical/SlicerCustomAppTemplate</a></li>
<li>Bundle the extension looking at the example in the top-level <code>CMakeLists.txt</code> of the custom application.</li>
</ol>
<blockquote>
<p>when I share the custom built Slicer application with someone else, they are unable to launch the application.</p>
</blockquote>
<p>Consider using the latest docker image described at <a href="https://github.com/Slicer/SlicerBuildEnvironment" class="inline-onebox">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a></p>

---

## Post #19 by @Karthik (2022-01-03 23:24 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="18" data-topic="21245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Bundle the extension looking at the example in the top-level <code>CMakeLists.txt</code> of the custom application.</p>
</blockquote>
</aside>
<p>I have tried to do the same. I just uncommented the lines for bundling the extension in the top-level CMakeLists.txt of the custom application and I got the following error.</p>
<p></p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2660a683d5644712b259425835d2c269c3dce19.png" data-download-href="/uploads/short-url/psbBS265AgbzPh1Ol4O0RuhyaH7.png?dl=1" title="list_error_extension" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2660a683d5644712b259425835d2c269c3dce19_2_690x222.png" alt="list_error_extension" data-base62-sha1="psbBS265AgbzPh1Ol4O0RuhyaH7" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2660a683d5644712b259425835d2c269c3dce19_2_690x222.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2660a683d5644712b259425835d2c269c3dce19_2_1035x333.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2660a683d5644712b259425835d2c269c3dce19.png 2x" data-dominant-color="38142D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">list_error_extension</span><span class="informations">1355×437 69.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><p></p>
<p><strong>CMake Error: list sub-command insert requires at least three arguments.</strong></p>
<p>This is what I have in the top-level CMakeLists.txt file.</p>
<pre><code class="lang-auto"># Enable/Disable Slicer custom modules: To create a new module, use the SlicerExtensionWizard.
set(Slicer_EXTENSION_SOURCE_DIRS
  #${CTFFR_SOURCE_DIR}/Modules/CLI/MyCLIModule
  #${CTFFR_SOURCE_DIR}/Modules/Loadable/MyLoadableModule
  ${CTFFR_SOURCE_DIR}/Modules/Scripted/Home
  )

# Add remote extension source directories

# SlicerOpenIGTLink
set(extension_name "SlicerOpenIGTLink")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/openigtlink/SlicerOpenIGTLink.git
  GIT_TAG        2b92f7b1ffe02403109b671f28424e8770e902a0
  GIT_PROGRESS   1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})

# Add Slicer sources
add_subdirectory(${slicersources_SOURCE_DIR} ${slicersources_BINARY_DIR})
</code></pre>
<p>I haven’t changed any other part of the file.<br>
Please suggest what changes I need to make to get this working.</p>

---

## Post #20 by @zhiyuan (2022-05-04 01:14 UTC)

<p>Hi Karthik, can you tell me how you run slicercustomapptemplate? I also need to customize a template, but I don’t know how to start the first step. Do I need to download QT or cmake before running</p>

---

## Post #21 by @cpinter (2022-05-04 09:38 UTC)

<p>You build the custom app template exactly as you build Slicer, see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" class="inline-onebox">Build Instructions — 3D Slicer documentation</a></p>

---

## Post #22 by @zhiyuan (2022-05-04 10:06 UTC)

<p>So is the ultimate goal the same as the link you sent me? I don’t know how to do this first step,<a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">this</a></p>

---

## Post #23 by @Karthik (2022-05-09 04:33 UTC)

<p>First, make sure you have all the pre-requisites installed. Follow these instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#pre-requisites" class="inline-onebox" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a></p>
<p>Then, follow the steps in <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step1" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step1</a> to create your own custom application based on 3D Slicer</p>

---

## Post #24 by @Karthik (2022-05-09 04:40 UTC)

<p>The first step is pretty simple. Just follow the instructions given in step 1. The commands will first clone the latest SlicerCustomAppTemplate from GitHub repo and allow you to customise basic information such as application name, organization name, etc.</p>
<p>Then, you need to set your preferences for the application build such as what version of 3D Slicer you wish to build. All these modifications can be made in the top level CMakeLists.txt in the SlicerCustomAppTemplate. (Note: By default it points to the latest commit in the 3D Slicer github repo. If you want to build a previous version of Slicer such as 4.11, then you must not only make this change in the top level CMakeLists.txt, but you also might need to checkout to a previous commit of SlicerCustomAppTemplate itself. )</p>

---

## Post #25 by @Karthik (2022-05-09 06:19 UTC)

<p>When I create the custom 3D Slicer, the top of the application window shows 0000-00-00. Normally, when I download 3D Slicer from the website, it shows the date on which Slicer was built. How can I get this to work in the custom app template? I want the date on which custom Slicer was built to be visibile instead of 0000-00-00</p>

---

## Post #26 by @lassoan (2022-05-12 02:51 UTC)

<p>Do you store your source files in a git repository? The date is probably not the build date but the date of the last modification, which is determined from the version history. Maybe git is not found or maybe you use an unusual date format on your computer and that’s why the date cannot be determined.</p>

---

## Post #27 by @Karthik (2022-05-12 04:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="21245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you store your source files in a git repository?</p>
</blockquote>
</aside>
<p>Which source files do you mean? I clone the custom app template from github every time I want to build. Currently, I just clone the custom app template and start the build process. Should I add a commit to this to make sure the date is updated?</p>
<p>By date of last modification, are you refering to modifying the custom app template or something else?</p>

---

## Post #28 by @lassoan (2022-06-29 02:20 UTC)

<p>Normally the date is retrieved from the git repository. If you get <code>0000-00-00</code> it means that either git cannot determine a date or the returned date cannot be parsed. You can get more information by printing out CMake variable values by adding <code>MESSAGE()</code> commands in <code>CMakeLists.txt</code> and <code>*.cmake</code> files.</p>

---
