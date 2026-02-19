---
topic_id: 18118
title: "Create A Mrml Viewer"
date: 2021-06-14
url: https://discourse.slicer.org/t/18118
---

# Create a MRML Viewer

**Topic ID**: 18118
**Date**: 2021-06-14
**URL**: https://discourse.slicer.org/t/create-a-mrml-viewer/18118

---

## Post #1 by @bhandarys (2021-06-14 15:21 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.13.0</p>
<p>Hi All,</p>
<p>I am new to Slicer and have been playing with it for a month or so. My requirement is to create a MRML viewer for users (doctors) with associated threshold controls. I intend to create registration prior to the users using it. I have gone through SlicerCAT template, Slicer IGT and Slicelets. I am still not clear about how best to approach this problem. Can anyone guide and point to a good step by step article / tutorial / resource on net?</p>

---

## Post #2 by @lassoan (2021-06-14 18:50 UTC)

<p>The easiest to get started is to implement a slicelet: a custom module that has all the user interface that your users need (so that they don’t need to switch between modules) and hides all other user interface elements (so that they are not confused by the lots of options that they don’t need. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">QuickSegment</a> example and let us know if you have any specific question.</p>
<p>If you are ready to develop a custom application (so that you have full control over branding, have a custom installer, etc.) then you can use SlicerCAT or use or contribute to an existing trimmed-down custom version of Slicer, such as <a href="https://github.com/KitwareMedical/SlicerQReads">SlicerQReads</a>, which is a Slicer-based simple DICOM viewer developed for clinicians at Mayo Clinic (developed by <a class="mention" href="/u/spycolyf">@spycolyf</a> and <a class="mention" href="/u/jcfr">@jcfr</a>).</p>

---

## Post #3 by @bhandarys (2021-06-15 13:15 UTC)

<p>Hi Andras,</p>
<p>Thanks a lot for your response. Based on your inputs, SlicerCAT is the way to go for me.</p>
<p>However, I am finding it very time consuming with this trial and error approach. I make changes to the CMAKE files, then configure, build, verify, repeat. Am I doing something wrong?</p>

---

## Post #4 by @lassoan (2021-06-15 14:48 UTC)

<p>You only need to build the top-level project once. Then, you only need to build Slicer.sln in the Slicer-build subdirectory. Build at that level takes less than 30 seconds.</p>

---

## Post #5 by @bhandarys (2021-06-17 12:48 UTC)

<p>Thanks a lot for your guidance. I tried Build/Slicer.sln. But I was getting “access is denied” error. After fiddling around a bit, I realized that the startup project was pointing to ALL_BUILD. So I changed it to SlicerQReadsApp (Is this right?).</p>
<p>The build is working fine and I am getting the exe and it executes also. But when I try to debug, I get “DLL not found” errors with the following DLLs.<br>
CTKWidgets.dll<br>
qt5widgets.dll<br>
qt5guid.dll<br>
qt5cored.dll</p>
<p>Based on your answer here (<a href="https://discourse.slicer.org/t/nightly-build-does-not-run/6774/2" class="inline-onebox">Nightly build does not run - #2 by lassoan</a>) I tried building the whole application again. I still get the same problem. I fail to understand how the build was successful if the dlls were not found. Seeking your help once again.</p>
<p>Thanks a lot for your time. Really appreciate.</p>

---

## Post #6 by @lassoan (2021-06-17 13:08 UTC)

<p>It is all good. You just need to start Visual Studio using the Slicer launcher as described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#run-slicer">build instructions</a>.</p>

---

## Post #7 by @bhandarys (2021-06-19 10:11 UTC)

<p>Hi Andras,</p>
<p>Yes, that worked. I now need to read up on why they are different.</p>
<p>I am using the SlicerCAT template and trying to make the landing module to be “Volumes”. So I modifed the following lines.</p>
<pre><code class="lang-auto">set(Slicer_DEFAULT_HOME_MODULE "Volumes")
set(Slicer_DEFAULT_FAVORITE_MODULES "Home, Data, Models, Transforms, Markups, SegmentEditor")
</code></pre>
<p>I even got the following lines during the compilation.</p>
<pre><code class="lang-auto">1&gt;-- Configuring Sudhirs default home module [Volumes]
1&gt;-- Configuring Sudhirs default favorite modules [Homes, Data, Models, Transforms, Markups, SegmentEditor]
</code></pre>
<p>However when the application opens of the default module is still “Home”. I tried deleting the .ini file based on this <a href="https://discourse.slicer.org/t/custom-application-does-not-open-module-at-startup/4913/15" class="inline-onebox">Custom application does not open module at startup - #15 by lassoan</a>. But that has not changed anything. Can you please guide on what I should look for now.</p>
<p>Thanks a lot for your suggestions and guidance. Really appreciate it.</p>

---

## Post #8 by @lassoan (2021-06-19 12:36 UTC)

<p><code>Slicer_DEFAULT_HOME_MODULE</code> is used for generating the default application settings (<code>(applicationname).ini</code>) file. It has no effect if the file already exists. You need to delete the existing application settings file.</p>

---

## Post #9 by @bhandarys (2021-06-23 13:33 UTC)

<p>Hi Andras,</p>
<p>I did delete the ini file. Unfortunately I had deleted slicer’s ini file. Your answer pointed me to the right ini file. Now the application starts with Volumes module (Which is exactly what I wanted).</p>
<p>However the open data and open DCIM button has disappeared. Is the application bar dependent on the module selected? I was of the opinion that only the left pane is dependent on the loaded module. Kindly correct me if I am wrong.</p>

---

## Post #10 by @lassoan (2021-06-23 13:50 UTC)

<p>Only a toolbar’s overall visibility and position is stored in application settings, not the list or visibility of individual buttons. If some of the “Load/Save” toolbar buttons are not visible then your application customizations explicitly made them hidden. Since Qt allows introspection of all objects, it is impossible to list all the possible places where these toolbar actions got hidden, but it should be somewhere in your code.</p>

---

## Post #11 by @Saima (2022-03-24 04:33 UTC)

<p>Hi Andras,<br>
I wanted to have a slicelet with only segment editor module and save and load and windows all windows for viewing the medical images.</p>
<p>From within the segment editor module I only wanted few of the already available functionality like paint, eraser, grow from seed.</p>
<p>What is the best way to start to make a slicelet with only essential functionality and hiding all the details?</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #12 by @Saima (2022-03-24 04:44 UTC)

<p>Hi andras,<br>
Regarding the quicksegment. the axial coronal and sagital window is showing just one slice. How can it be extended to show all the slices like in the slicer.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #13 by @lassoan (2022-03-28 11:28 UTC)

<p>The view layout defines what views are displayed. See how to customize and select a layout in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">script repository</a>.</p>

---
