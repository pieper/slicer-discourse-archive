# No extensions in extension manager

**Topic ID**: 4117
**Date**: 2018-09-14
**URL**: https://discourse.slicer.org/t/no-extensions-in-extension-manager/4117

---

## Post #1 by @vincitytaymodaimo (2018-09-14 12:23 UTC)

<p>Hi! After installing Slicer 4.9.0 2018-08-07, there are no extensions listed in the extension manager.</p>
<p>In the extensions manager, I get the message: “No extensions found for win:64-bit, revision: ‘27339’. Please try a different combination”.</p>
<p>This is the whole Slicer error log:</p>
<p>“Session start time …: 2018-08-08 13:37:45<br>
Slicer version …: 4.9.0-2018-08-07 (revision 27339) win-amd64 - installed release<br>
Operating system …: Windows / Professional / (Build 9200) - 64-bit<br>
Memory …: 16262 MB physical, 16262 MB virtual<br>
CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
VTK configuration …: OpenGL2 rendering, TBB threading<br>
Developer mode enabled …: no<br>
Prefer executable CLI …: yes<br>
Additional module paths …: (none)<br>
Popen([‘git’, ‘version’], cwd=C:\Program Files\Slicer 4.9.0-2018-08-07, universal_newlines=False, shell=None)<br>
Popen([‘git’, ‘version’], cwd=C:\Program Files\Slicer 4.9.0-2018-08-07, universal_newlines=False, shell=None)<br>
Scripted subject hierarchy plugin registered: Annotations<br>
Scripted subject hierarchy plugin registered: SegmentEditor<br>
Scripted subject hierarchy plugin registered: SegmentStatistics<br>
Switch to module: “Welcome”<br>
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.”</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #2 by @lassoan (2018-09-14 13:14 UTC)

<p>Thanks for reporting this. See explanation and temporary download link here:</p>
<aside class="quote" data-post="2" data-topic="4097">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/2018-09-13-only-nightly-slicer-packages-do-not-expect-extensions-this-morning/4097/2">2018.09.13: Only nightly Slicer packages - do not expect extensions this morning</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Until the build infrastructure is restored, Slicer nightly version (with extensions) can be downloaded from here: <a href="https://download.slicer.org/?date=2018-09-10">https://download.slicer.org/?date=2018-09-10</a>.
  </blockquote>
</aside>


---
