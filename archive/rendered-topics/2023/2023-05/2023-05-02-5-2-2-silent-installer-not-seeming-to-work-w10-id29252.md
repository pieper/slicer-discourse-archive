# 5.2.2 silent installer not seeming to work w10

**Topic ID**: 29252
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/5-2-2-silent-installer-not-seeming-to-work-w10/29252

---

## Post #1 by @mwfee (2023-05-02 18:35 UTC)

<p>Hi.</p>
<p>MECM environment in a college.</p>
<p>I see this is a NSIS installer but running theexe.exe /S is not firing away on Windows 10.</p>
<p>I had a colleague reproduce this independently.  Updating from 4.2</p>
<p>I see the app is fully portable so I am going to copy the directory and some icons by hand.  It would be pleasant if the silent install function was repaired.</p>
<p>Thank you</p>

---

## Post #2 by @jamesobutler (2023-05-02 18:56 UTC)

<p>On Windows 10, I was able to successfully silently install Slicer 5.2.2. Since it takes several minutes to install, you will see it silently show up after that amount of time.</p>
<pre data-code-wrap="PS"><code class="lang-plaintext">PS C:\Users\james\Downloads&gt; ./Slicer-5.2.2-win-amd64 /S
</code></pre>

---

## Post #3 by @lassoan (2023-05-02 19:21 UTC)

<p>If you want to wait until installation is completed then check out <a href="https://stackoverflow.com/questions/16087674/how-can-i-make-my-nsis-silent-installer-block-until-complete">this page</a>.</p>

---

## Post #4 by @mwfee (2023-05-05 16:39 UTC)

<p>Hi Folks,</p>
<p>Thanks for the reply.  We are a MECM / SCCM shop.</p>
<p>Try simulating a MECM deployment by running the installer as nt system.</p>
<p>pstools from microsoft</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://learn.microsoft.com/en-us/sysinternals/downloads/pstools">
  <header class="source">

      <a href="https://learn.microsoft.com/en-us/sysinternals/downloads/pstools" target="_blank" rel="noopener nofollow ugc">learn.microsoft.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png" class="thumbnail" width="" height="">

<h3><a href="https://learn.microsoft.com/en-us/sysinternals/downloads/pstools" target="_blank" rel="noopener nofollow ugc">PsTools - Sysinternals</a></h3>

  <p>Command-line utilities for listing the processes running on local or remote computers, running processes, rebooting computers, and more.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>elevated command prompt;  psexec64.exe -i -s cmd.exe<br>
that will launch a new window.  whoami will return the system value.  slicerinstallexe /S This is where the error occurs.  Had another engineer try, too.</p>
<p>I can try the install /wait to see what it does.  In the last version the extensions were okay as is.</p>
<p>I also read that this can be a portable app since a current version.  I wrote a PS script that basically up and copies everything.  However when attempting to install an extension, we are getting</p>
<p>“Extensions install directory is expected to be readable/writable/executable: C:/Program Files/Slicer/NA-MIC/Extensions-31382”<br>
And underneath it says “Check that 3D Slicer is properly installed.”</p>
<p>one more update with permission fix - looks like we have to give explicit read write execute permissions on the folder.</p>
<p>I am guessing it is not fully portable.</p>
<p>The last version we had to install was 4.1.1202102.</p>
<p>Thanks - appreciate everyone.</p>

---

## Post #5 by @lassoan (2023-05-05 22:22 UTC)

<p>The application is fully portable, including all data and settings.</p>
<p>However, you need to install in a writable location if you want to allow your users to install extensions (as all the extensions and additional Python packages that they pull in must be all available to all users). It might be possible to remove this requirement (e.g., install additional modules and Python packages in the user’s folder), but it may not be easy to implement this and there has not been very strong demand for it (but you can <a href="https://discourse.slicer.org/c/support/feature-requests/9">submit a feature request</a> and see how much support it gets).</p>
<p>If you want prevent your users from from installing extensions then install Slicer into a read-only folder (e.g., in C:\Program Files). You can disable the extension manager in application settings to prevent the extensions manager from showing up in the application. You can pre-install selected extensions by starting Slicer as administrator. Users that have admin access can also launch Slicer as administrator and then install extensions.</p>
<p>Since each user may want to use different set of extensions and settings, I would generally recommend to install Slicer per user. In some institutions a Slicer shortcut is added that launches a script that downloads and installs Slicer in the user’s folder if Slicer is not installed there already.</p>
<p>How your users are expected to use Slicer? Do they need to install extensions? Are your users generally allowed to install any software (applications, Python packages, etc.) and you just pre-install Slicer for convenience?</p>

---

## Post #6 by @muratmaga (2023-05-06 01:04 UTC)

<aside class="quote no-group" data-username="mwfee" data-post="4" data-topic="29252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e8c25b/48.png" class="avatar"> mwfee:</div>
<blockquote>
<p>“Extensions install directory is expected to be readable/writable/executable: C:/Program Files/Slicer/NA-MIC/Extensions-31382”</p>
</blockquote>
</aside>
<p>Install directly to C:/ (e.g., C:/Slicer-5.2.2), which by default is writable by all users. That was the solution that worked for us.</p><aside class="quote" data-post="6" data-topic="28421">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/install-slicer-for-all-users-on-windows/28421/6">Install Slicer for all users on Windows</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    On a regular windows everything works fine if I install the Slicer directly on C:\ 
Extensions and python packages go in there. 
Default permissions generated by Windows for the C:\Slicer folder includes modify for “Authenticated Users”, which means people logged on the system are allowed to make changes (even install/uninstall extensions, python packages). 
If our company policies allows this, all should be good.
  </blockquote>
</aside>


---
