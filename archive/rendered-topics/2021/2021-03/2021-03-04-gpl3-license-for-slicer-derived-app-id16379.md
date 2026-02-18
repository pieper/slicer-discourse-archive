# GPL3 license for Slicer derived app

**Topic ID**: 16379
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/gpl3-license-for-slicer-derived-app/16379

---

## Post #1 by @keri (2021-03-04 21:18 UTC)

<p>I’m starting to develop Slicer based application that is supposed to be used in geoscience field and will be distributed on github under GPL3 license. It will have its own name, mainwindow will be changed, some modules will be disabled by default, some modules will be added and I would like to have access to extension manager and have the possibility to write custom modules as it is done in Slicer.<br>
It is up to me to support this app.</p>
<p>The question is about how to license an app on github.<br>
Lets suppose I’m starting developping application. I plan to use Circle CI or Travis from the very beginning. Thus I create new ropository <code>MyApp</code>, make some small changes to Slicer mainwindow and make some changes in CMakeLists, try to build it with Travis or Circle CI. What license file should my repository have: BSD or GPL3?</p>
<p>Also from the beginning I plan not to use <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#license" rel="noopener nofollow ugc">SlicerCat (SlicerCustomAppTemplate)</a> (or to use it to only change the name of an app) as I need to more detailly get aquainted with Slicer.Thus in the very beginning I’m going to upload “Slicer” under different name with very small changes in mainwindow (like adding few more QDockWidgets, tree views and removing logo)</p>

---

## Post #2 by @pieper (2021-03-04 21:30 UTC)

<p>As long as you comply with the terms of <a href="https://github.com/Slicer/Slicer/blob/master/License.txt">the Slicer license</a> you are free to distribute your modifications under the license of your choice.  For example, it can be <a href="https://discourse.slicer.org/t/slicer-usage-in-the-closed-commercial-product/14180">in a closed source application</a>.</p>
<p>We would encourage you not to use GPL, for <a href="https://discourse.slicer.org/t/rpy2-pip-installation-fails/4883/15">reasons outlined here</a>, but that’s up to you.</p>

---

## Post #3 by @Sam_Horvath (2021-03-04 21:58 UTC)

<p>Can you elaborate more on why you don’t want to use the SlicerCustomAppTemplate?  Directly forking Slicer and adding additional commits will make it difficult to upgrade your app to pull in changes (features and more importantly bugfixes) that are added to Slicer after you create your fork.</p>

---

## Post #4 by @lassoan (2021-03-04 22:39 UTC)

<p>It is great to hear that you plan to use Slicer as a basis for your project. I fully support suggestions of <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>.</p>
<p>GPL practically means that you will be left alone with all development and maintenance tasks. Very few people can afford to support or contribute to a GPL project.</p>
<p>The custom app template allows you to benefit from all the efforts that the Slicer team invests into improving the code base. If you don’t isolate Slicer core changes from your own changes then it will be practically impossible for you to to keep up with all the Slicer core changes.</p>

---

## Post #5 by @keri (2021-03-04 22:39 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> thank you for clarifying. As I understood Slicer’s community don’t like GPL3 license as Slicer want to stay free for both commercial and non commercial use case.<br>
I don’t have experience in such licensing but I’m thinking to make a platform where geoscientists are able to create their extension and may upload them under GPL3 license to prevent commercial use or earn some money for their effort. Thus scientists could work on algorithms and companies should pay to GPL3 extension’s owner.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> what you said is my goal. Actually I can’t find the easiest way to keep integrating Slicer updates with my custom application.<br>
Lets suppose I make some changes to mainwindow and CMake files (CMakeLists.txt, external packages and some other). Then I pull new Slicer commit and it should overwrite my changes to mainwindow and cmake files.<br>
Or I miss something? As I didn’t find the most efficient way to support app I planned to make all changes to a Slicer fork and probably then experimenting with SlicerCAT (pull this fork when customizing SlicerCAT). If you have experience I would appreciate if you give me recommendation.</p>

---

## Post #6 by @lassoan (2021-03-04 22:50 UTC)

<p>GPL can make sense for algorithms, but not for infrastructure, such as an application platform. I would recommend to keep the permissive license for the application platform changes and only apply GPL or other commercial license to specific modules or algorithms that you develop.</p>
<p>The custom application template will help you with very clearly separating the stock Slicer core (that the superbuild pulls in), your customizations (Applications folder of CAT), and custom modules (Modules folder of CAT). If you want to save time on maintenance then you can push back some of your customizations/enhancements into the Slicer core.</p>

---

## Post #7 by @Sam_Horvath (2021-03-04 23:00 UTC)

<p>So, if you are making changes on a fork of Slicer, to update the underlying Slicer, you would rebase your branch on top of the updated Slicer, essentially adding the new Slicer changes into the history before your work.  Issues occur when the Slicer changes affect the same areas of code and you have to resolve conflicts to make sure all changes are integrated correctly.</p>
<p>When working on custom apps, we generally keep all of the custom specific code in the template layer.  We sometimes fork Slicer to use as the base for the custom app, as you noted, but that is usually only done when there is a core change needed by the app, and our goal is to get that core change integrated into Slicer so we can go back to using the official repo.</p>
<p>An important thing to note is that you can make very aggressive changes to the main window from within custom modules when writing in the Python layer.  When designing custom apps, I usually include a Home module (scripted) which takes responsibility for modifying the main window.  Here is an example from a currently in development project:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://gitlab.kitware.com/aeva/aevaslicer/-/blob/master/Modules/Scripted/Home/Home.py#L158" target="_blank" rel="noopener nofollow ugc">GitLab</a>
  </header>
  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/5058/aeva.ico" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://gitlab.kitware.com/aeva/aevaslicer/-/blob/master/Modules/Scripted/Home/Home.py#L158" target="_blank" rel="noopener nofollow ugc">Modules/Scripted/Home/Home.py · master · aeva / aevaSlicer</a></h3>

<p>GitLab Community Edition</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>This code adds another dock widget which contains a “data and properties” view based on built in Slicer widgets.</p>

---

## Post #8 by @keri (2021-03-04 23:13 UTC)

<p>Now I see how to work with CAT. I’ve built Slicer yesterday using CAT and didn’t see that my folder contains other files like <code>main.cxx</code> etc.</p>
<p>Then I will start from the Slicer default license and during few moth I will try to collect my thoughts to understand this lcensing staff. Probably I will look for sponsors.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> thank you for clarification. I didn’t know before that we have such a broad control over mainwindow via python. I will keep in mind the line <code>slicer.util.mainWindow()</code> for the future</p>

---

## Post #9 by @pieper (2021-03-05 00:57 UTC)

<p>Sounds great, let us know how it goes with your geoscience colleagues.  You’ve probably seen SlicerAstro and SlicerMorph, which may give you some ideas.</p>

---

## Post #10 by @fbordignon (2022-01-12 14:03 UTC)

<p>Hey <a class="mention" href="/u/keri">@keri</a> I work with LTrace developing GeoSlicer. We’ve built it with SlicerCAT and implemented various scripted modules. We are currently using a closed source format for GeoSlicer, at least for now, due to the funding contract requirements. We are developing it in partnership with Petrobras, the Brazilian oil major.<br>
Although it is intended for petroleum geosciences, there are some overlap with mining. Take a look and see if you can benefit from the software or form a partnership: ltrace.com.br/geoslicer<br>
My email is fernando -at- ltrace.com.br</p>

---
