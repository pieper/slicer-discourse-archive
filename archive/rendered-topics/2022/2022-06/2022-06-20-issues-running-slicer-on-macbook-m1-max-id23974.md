# Issues running Slicer on macbook m1 max

**Topic ID**: 23974
**Date**: 2022-06-20
**URL**: https://discourse.slicer.org/t/issues-running-slicer-on-macbook-m1-max/23974

---

## Post #1 by @sannpeterson (2022-06-20 23:57 UTC)

<p>I’m trying to use Slicer on the macbook m1 max but I’m having a lot of performance issues. I’m mostly trying to segment brain vessels but the program crashes constantly while I’m in segment editor. I haven’t been able to use it longer than 5 min without crashing. Using scissor tool to erase large pieces also takes much longer than on my old machine and it’s usually during this step where Slicer crashes. I’ve tried the preview and stable releases but it doesn’t make a difference. Is there any way to make Slicer run better?</p>

---

## Post #2 by @lassoan (2022-06-21 01:31 UTC)

<p>What you describe sounds like you are running out of memory. How much physical RAM does your computer have? How much is the free disk space? (macOS uses disk space when it runs out of memory)</p>
<p>What is the size of the image that you are processing (Volumes module → Volume information → Dimensions, Scalar Type)?</p>
<p>What model was your old machine that worked better?</p>
<p>Which Slicer version are you using?</p>
<p>Do you get any error messages in Slicer? Can you provide us a crash report (that the operating system can generate when an application crashes)?</p>

---

## Post #3 by @sannpeterson (2022-06-21 20:36 UTC)

<p>Physical RAM: 32 GB<br>
Free disk space: 919 GB<br>
Model of old PC: Dell XPS 9560<br>
Slicer version: 5.1.0</p>
<p>Error message just says the app quit unexpectedly.<br>
<a href="https://gist.github.com/sannpeterson/1a21ba5136aa54b22daa8a0c579a88b6" rel="noopener nofollow ugc">Crash report here</a></p>
<p>Volume information:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/505c322c3dfb9df514c2fcd8e3740058791225cd.png" alt="image" data-base62-sha1="bsTJ39SfluHP6OsAb3AYLcRfhyR" width="590" height="436"></p>

---

## Post #4 by @lassoan (2022-06-22 01:21 UTC)

<p>Performance of an M1 Max should as fast as a latest Intel systems, so it should be definitely faster than a Dell XPS 9560 (that was released about 5 years ago). The Intel compatibility layer may slow things down a bit, but not that much. So, there is something unusual about your data, what operations are performed on the data, or your system.</p>
<p>Could you provide a .mrb scene file and instructions for reproducing the crash for you on your M1?<br>
(no need to share your data but create a scene based on any of the Slicer sample data sets)</p>

---

## Post #5 by @sannpeterson (2022-06-22 20:10 UTC)

<p><a href="https://github.com/sannpeterson/slicermrb2" rel="noopener nofollow ugc">mrb file here</a></p>
<p>Used the scissor tool to cut a large quadrant from the top right corner.</p>
<p>Slicer crashed after about 10-15 min of trying to process this step.</p>
<p>Even scissoring out a small portion of the segmentation takes a long time though, even if it doesn’t crash.</p>

---

## Post #6 by @lassoan (2022-06-25 05:15 UTC)

<p>I can use the Scissors effect on this scene very conveniently, on my 3-year-old laptop. It cuts away pieces in a fraction of a second. I don’t know what’s wrong with your system. We’ll keep an eye out on these M1 macs to see if others have problem with them, too.</p>
<p>Note that you clean up this image much more easily, fully automatically, by using Islands effect. Just use the default option (Keep largest island) and click Apply. If you want to keep some disconnected branches then you can use “Grow from seeds” effect, with the current segment selected as Masking → Editable area, and then painting scribbles into the pieces that you want to keep.</p>

---

## Post #7 by @lassoan (2022-06-28 14:41 UTC)

<p>2 posts were split to a new topic: <a href="/t/segmentation-of-thin-vessels/24082">Segmentation of thin vessels</a></p>

---

## Post #8 by @lassoan (2022-08-04 05:45 UTC)

<p>Well continue discussing this issue at this topic:</p>
<aside class="quote" data-post="5" data-topic="22564">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sannpeterson/48/10892_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/performance-issues-on-mac-m1/22564/5">Performance issues on Mac M1?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I also posted about this same issue. Performance on my brand new Macbook Pro M1 is very unreliable. I’ve tried working with smaller areas but it doesn’t seem to matter much. Sometimes it runs smoothly but most of the time it’s painfully slow. I switched back over to windows just to use Slicer.
  </blockquote>
</aside>


---
