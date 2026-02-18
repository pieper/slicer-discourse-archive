# Customized application launchers

**Topic ID**: 564
**Date**: 2017-06-23
**URL**: https://discourse.slicer.org/t/customized-application-launchers/564

---

## Post #1 by @fedorov (2017-06-23 19:01 UTC)

<p>What <a class="mention" href="/u/che85">@che85</a> and I considered in the past (and I think we discussed this with <a class="mention" href="/u/lassoan">@lassoan</a>) is to include “launchers” (for the lack of a better word) that would provide access to the application/community-specific slicelet.</p>
<p>The user would still install the full Slicer application downloaded from the same central location, but (perhaps as an option at install time) they would get a separate icon for a focused functionality that would launch specific slicelet, which would not expose the full application with all the bells and whistles.</p>
<p>I am still a bit lost about what is SlicerVerse, and what defines “a SlicerDistribution” or “something that is customized enough to meet the needs of a certain biomedical community” - I think the guidelines are fuzzy or non-existing. But what I suggest would provide access to the very focused application UI developed for a specific need, distributed as part of Slicer. I think if the main goal is to hide the complexities of Slicer that are irrelevant to a given task, it might be enough to achieve that goal.</p>

---

## Post #2 by @ihnorton (2017-06-23 20:39 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/communities-slicerverse/40">Communities / “SlicerVerse”</a></p>

---

## Post #4 by @che85 (2017-06-23 19:24 UTC)

<p>I absolutely agree. There are often situations where users are overwhelmed by the Slicer user interface and developers decide to create their own slicelets.</p>
<p>I think it would be a great feature to have shortcuts within one’s Application directory (regarding MacOS) that allow starting an extension slicelet for hiding the complexity of Slicer.</p>
<p>Another <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=5" title=":thumbsup:" class="emoji" alt=":thumbsup:"> for extensions that provide a slicelet would be to have a checkbox within the ExtensionManager which says “Add slicelet shortcut to my applications” or something similar.</p>
<p>The structure for the ExtensionIndex might need to be extended then I guess.</p>

---

## Post #5 by @lassoan (2017-06-23 20:57 UTC)

<p>Good point, this is a nice approach, too. Based on this, I update the list of existing customization options:</p>
<ol>
<li>User downloads standard Slicer installer and installs extensions manually.</li>
<li>Custom installers (have custom application name, some additional extensions are bundled, some modules are excluded) - this can be built without modifying anything in Slicer source code, just by tuning CMake options (except resources). No extension manager access.</li>
<li>CustomSlicerGenerator: It works but it has two serious limitations (no installer is available, just a zip file; resources, such as any icons and bitmaps shown in the application are not customizable - except application icon and splash screen).</li>
<li>Custom launcher: Shortcut in the Start menu (Windows) or Application directory (MaxOSX) that starts Slicer, jumping right into a slicelet (module with a simplified user interface). It uses standard Slicer installation.</li>
</ol>
<p>All these options have some merits. I guess we just need to decide if we want to promote one of these methods to be an officially supported, widely advertised solution for distributing customized Slicer versions.</p>

---

## Post #6 by @pieper (2017-06-24 16:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>CustomSlicerGenerator: It works but it has two serious limitations (no installer is available, just a zip file; resources, such as any icons and bitmaps shown in the application are not customizable - except application icon and splash screen).</p>
</blockquote>
</aside>
<p>First let me comment on these issues:</p>
<ul>
<li>
<p>it would be trivial to add a windows installer to the CustomSlicerGenerator.  The current cpack method used for Slicer is NSIS and has been unchanged for well over a decade and it basically just starts from a redistributable directory of the app.  (Of course, as <a class="mention" href="/u/bpaniagua">@bpaniagua</a> has confirmed a zip file containing an executable is completely usable even by clinical users)</p>
</li>
<li>
<p>I believe all the Slicer resources can be overridden from python; if not that is probably a limitation to be fixed in any case.  However I also suspect that any slicelet or other customized app is going to create a whole new interface that remixes the slicer widgets so the application side of that would have its own resources anyway.  (<a class="mention" href="/u/lassoan">@lassoan</a> can you give a specific example you’d like to change but cannot currently?)</p>
</li>
</ul>
<p>I also think we need to weigh these issues against the benefits of the CustomSlicerGenerator:</p>
<ul>
<li>
<p>Custom app maintainers don’t need to have cmake or compilers or even have access to all the build platforms</p>
</li>
<li>
<p>customized versions can be built using the standard slicer packages and extensions from using any platform  (e.g. linux script can generate linux, mac, and windows custom versions)</p>
</li>
<li>
<p>re-uses the existing factory and extension resources rather than duplicating them</p>
</li>
<li>
<p>leverages the python customization features of the Slicer core, so any improvements there will have side benefits for other extensions</p>
</li>
<li>
<p>As <a class="mention" href="/u/bpaniagua">@bpaniagua</a> says, specific versions multiple extensions can be pulled together in a bundle version which simplifies support</p>
</li>
</ul>

---

## Post #7 by @lassoan (2017-06-24 18:21 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>confirmed a zip file containing an executable is completely usable even by clinical users</p>
</blockquote>
</aside>
<p>I can very easily find any number of users who has no clue what to do with a zip file but can easily install using an installation package. You would not have start menu shortcuts, uninstaller, etc. either. So, I would not even consider this as a viable option.</p>
<p>It’s certainly possible to create/edit an NSIS project file (project.nsi) manually but it requires some work. For example, you need to list explicitly list in the .nsi file all files that need to be uninstalled. If you add some files to the distribution you need to edit the .nsi file and add an uninstall command for each.</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I believe all the Slicer resources can be overridden from python</p>
</blockquote>
</aside>
<p>I don’t think it is possible to override resources that are built into the application. It is possible to dynamically load/unload complete resource files, but then you need to compile a resource file using Qt’s resource compiler for creating a custom package.<br>
If we know in advance what images we allow to replace (for example the large Slicer logo at the top of the module panel) then we can change the implementation to load those from individual external files instead of a resource package.</p>
<p>There a number of other things that can be nicely configured at build time but not dynamically - see the long list of options <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Customizing_application_build">here</a>. These were all specifically added because customers needed to change it.</p>
<p>I agree that having a way of customizing a Slicer package without setting up a compiler would be really, really good. All benefits that you listed are valid and I could add a few more. The only issue is that it would be so much work to implement (and maintain) all the necessary hooks and additional mechanisms that would make this solution feasible. in contrast, we have an almost complete solution by simply building Slicer core, customized through CMake options.</p>
<p>If we decide to go that way, I would be ready to help with improving the custom slicer generator, but it would require a lot of efforts from others, too.</p>

---

## Post #8 by @lassoan (2017-06-24 20:19 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>can you give a specific example you’d like to change but cannot currently?</p>
</blockquote>
</aside>
<p>Currently we customize these in our custom application packages:</p>
<ul>
<li>All application options defined <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Customizing_application_build">here</a>.</li>
<li>These resource files:
<ul>
<li>Applications\SlicerApp\Resources\Icons\Large(appname)-DesktopIcon.png</li>
<li>Applications\SlicerApp\Resources\Icons\Medium(appname)-DesktopIcon.png</li>
<li>Applications\SlicerApp\Resources\Icons\Small(appname)-DesktopIcon.png</li>
<li>Applications\SlicerApp\Resources\Icons\XLarge(appname)-DesktopIcon.png</li>
<li>Applications\SlicerApp\Resources\Icons\XXLarge(appname)-DesktopIcon.png</li>
<li>Applications\SlicerApp\Resources\Images(appname)-Logo.png</li>
<li>Applications\SlicerApp\Resources\Images(appname)-ModulePanelLogo.png</li>
<li>Applications\SlicerApp\Resources\Images(appname)-SplashScreen.png</li>
<li>Applications\SlicerApp\Resources(appname).icns</li>
<li>Applications\SlicerApp\Resources(appname).ico</li>
</ul>
</li>
</ul>
<p>If these remain customizable and an installer can be generated on all platforms, then using custom slicer generator will be an acceptable option for us.</p>

---

## Post #9 by @pieper (2017-06-25 12:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I can very easily find any number of users who has no clue what to do with a zip file but can easily install using an installation package. You would not have start menu shortcuts, uninstaller, etc. either. So, I would not even consider this as a viable option.</p>
</blockquote>
</aside>
<p>Yes, for windows users an installer can be helpful so we should add an option to create one.  I haven’t looked in a <em>very</em> long time but it should be easy to just recursively list all the files in the custom slicer directory and tell NSIS to install them.</p>
<p>Of course there’s also the issue that some PCs will let you run executables from zip files, but won’t let you install without admin accounts so people may still want the zip option in some cases.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>All application options defined here.</p>
</blockquote>
</aside>
<p>Other than Slicer_USE_PYTHONQT_WITH_OPENSSL (which I doubt you want to change) it looks like those all just turn modules on or off or set things in the Settings file.  These are easy to customize already.</p>
<p>The rest of the options you list should be editable with <a href="https://github.com/jcfr/ResEdit/blob/master/README.md">ctkResEdit</a> or an existing platform specific variant.</p>
<p>Of course, people <em>will always</em> have the option of working from the CMake level to create their own amazing project, but as we all know that is <em>not easy at all!</em></p>

---

## Post #10 by @lassoan (2017-06-25 16:55 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>there’s also the issue that some PCs will let you run executables from zip files, but won’t let you install without admin accounts</p>
</blockquote>
</aside>
<p>That’s just a simple setting if the installer should ask for elevated access. It is usually set for elevated access so that you can install in Program Files folder. If the installer does not request for elevated access then any user can run it and then typically you set the install folder to be in the user’s profile (this is for example how <a href="http://www.plustoolkit.org">Plus applications installer</a> is configured).</p>
<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>it should be easy to just recursively list all the files</p>
</blockquote>
</aside>
<p>Not very simple, but it can be certainly implemented in Python (some directory walking and text file generation based on a template). This is already implemented in CMake but if we don’t want to depend on CMake then it has to be reimplemented from scratch.</p>
<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>set things in the Settings file</p>
</blockquote>
</aside>
<p>Default settings are now hardcoded in the application. If a key is missing then the application creates it and initializes it with the default value. Of course the setting can be changed in Python but you don’t know if a particular setting is a default value set by the application (can be updated) or set by the user (must not be changed). If we don’t implement some sophisticated mechanism then some user settings will be lost on application install.</p>
<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>just turn modules on or off</p>
</blockquote>
</aside>
<p>There is also disclaimer text. There are many solutions for this, just have to implement one of them.</p>
<p>Overall, no blocking issues, just many small things and a few larger mechanisms would need to be implemented.</p>

---

## Post #11 by @Tesla2678 (2021-12-01 06:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>tuning CMake options (except resources)</p>
</blockquote>
</aside>
<p>Hello lassoan,</p>
<p>Would you tell me how to implement “tuning CMake options (except resources)”.</p>
<p>Thank you!</p>

---

## Post #12 by @jcfr (2021-12-01 07:20 UTC)

<blockquote>
<p>Would you tell me how to implement “tuning CMake options (except resources)”.</p>
</blockquote>
<p><code>just by tuning CMake options</code> originally referenced by <a class="mention" href="/u/lassoan">@lassoan</a>  means you can simply toggle CMake options during the configuration step described in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html" class="inline-onebox">Build Instructions — 3D Slicer documentation</a></p>
<p>To provide the full context, I quoted below the original answer where this was mentioned.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ul>
<li>User downloads standard Slicer installer and installs extensions manually.</li>
<li>Custom installers (have custom application name, some additional extensions are bundled, some modules are excluded) - this can be built without modifying anything in Slicer source code, just by tuning CMake options (except resources). No extension manager access.</li>
<li>CustomSlicerGenerator: It works but it has two serious limitations (no installer is available, just a zip file; resources, such as any icons and bitmaps shown in the application are not customizable - except application icon and splash screen).</li>
<li>Custom launcher: Shortcut in the Start menu (Windows) or Application directory (MaxOSX) that starts Slicer, jumping right into a slicelet (module with a simplified user interface). It uses standard Slicer installation.</li>
</ul>
</blockquote>
</aside>

---

## Post #13 by @lassoan (2021-12-01 14:53 UTC)

<p>There are different options now, most importantly the <a href="https://github.com/KitwareMedical/SlicerCAT">Slicer custom application template</a>.</p>

---

## Post #14 by @Tesla2678 (2021-12-03 10:52 UTC)

<p>Hello jcfr,<br>
Thank you for your reply,<br>
I still can’t find the configuration when creating the installer package.<br>
I have built already, I added a new module, and then want to create a new installer package containing the new modules.</p>
<blockquote>
<h2>Package Slicer (create installer package)<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#package-slicer-create-installer-package" rel="noopener nofollow ugc">¶</a></h2>
<ul>
<li>Start Visual Studio with the launcher:</li>
</ul>
<p>Slicer.exe --VisualStudioProject</p>
<ul>
<li>Select <code>Release</code> build configuration.</li>
<li>In the “Solution Explorer”, right click on <code>PACKAGE</code> project (in the CMakePredefinedTargets folder) and then select <code>Build</code> .</li>
</ul>
</blockquote>

---

## Post #15 by @lassoan (2021-12-14 14:31 UTC)

<p>The settings are here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1de2a2a58d9cca56dca196e1bbc950f1fa2dd48b.png" data-download-href="/uploads/short-url/4gnpsprN2Gz2tAfqI0UZGLv80A3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1de2a2a58d9cca56dca196e1bbc950f1fa2dd48b_2_690x216.png" alt="image" data-base62-sha1="4gnpsprN2Gz2tAfqI0UZGLv80A3" width="690" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1de2a2a58d9cca56dca196e1bbc950f1fa2dd48b_2_690x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1de2a2a58d9cca56dca196e1bbc950f1fa2dd48b_2_1035x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1de2a2a58d9cca56dca196e1bbc950f1fa2dd48b_2_1380x432.png 2x" data-dominant-color="252524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1746×547 38.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
