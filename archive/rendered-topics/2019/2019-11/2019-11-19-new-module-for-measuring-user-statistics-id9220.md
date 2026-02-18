# New module for measuring user statistics

**Topic ID**: 9220
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/new-module-for-measuring-user-statistics/9220

---

## Post #1 by @Sunderlandkyl (2019-11-19 17:17 UTC)

<p>In the latest 3D Slicer 4.11.0 releases, the SlicerSandbox extension now includes the “User Statistics” module for measuring how much time is spent using various tools in Slicer. This can be useful for getting quantitative information about efforts needed for manual segmentation or identifying the most time-consuming steps in a processing workflow. Results are saved in a .csv file.</p>
<div class="lazyYT" data-youtube-id="YyO8wi-hnls" data-youtube-title="User Statistics - New module in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>The following statistics are saved in the table:</p>
<ul>
<li>Start time</li>
<li>Operation (Segment editor effect)</li>
<li>Duration</li>
<li>Segment name</li>
<li>Master volume name</li>
<li>Segmentation name</li>
<li>Segment terminology</li>
<li>Active module name</li>
<li>User activity (active, idle, wait)</li>
<li>Computer</li>
<li>Username</li>
<li>Scene</li>
</ul>
<p>Additional information:</p>
<ul>
<li>The module reacts to changes in the current state and measures the length of time that a user spends in each state</li>
<li>User statistics tables from other scenes and can be merged together</li>
<li>Optionally, the module can take screenshots of Slicer when the state is changed</li>
<li>Statistics are recorded every 20 seconds, or whenever a state is changed</li>
</ul>
<p>Suggestions and feedback are welcome.</p>
<p>Development was funded in part by CANARIE’s Research Software Program, OpenAnatomy, and Brigham and Women’s Hospital through NIH grant R01MH112748</p>

---

## Post #2 by @Fernando (2019-11-21 12:18 UTC)

<p>Great! I’ve coded stuff to get info from clinicians interactions. Thanks you!</p>

---

## Post #3 by @mikebind (2020-01-31 21:56 UTC)

<p>I’m excited by the possibilities for this, but I had no idea what was going on with it at first.  I installed the sandbox for other reasons, and since then there has been a permanent UserStatisticsTableNode which appears in all my scenes and when I save and reload a scene, now there are two UserStatisticsTableNodes.  If I don’t pay attention and delete them, they multiply. I have several saved scenes which have at least 4 of these nodes. Looking the UserStatistics module code, it seems like I should be asked something at startup (showUserConfirmationDialog() in initializeModule() ), but I see no confirmation dialog when starting Slicer.<br>
I would prefer if the UserStatistics module did not automatically create a UserStatisticsTableNode if it is not enabled, and I definitely don’t need empty, non-enabled table nodes to be saved and multiply.</p>
<p>For my own use, I certainly plan to try to implement something like this for my own modules, as well as tracking across multiple modules, including built-in ones.  It looks like the current version is focused only on segmentation, is that correct? A more general purpose one would probably also be useful for the Slicer community.  I realize that different modules have different structures, so would be harder to track across modules in a standardized table, but even just tracking time and module name in a table would be useful.</p>
<p>In any case, the current module seems very useful for tracking segmentation processes, and lays out a clear blueprint for applying tracking to other situations.  Thanks!</p>

---

## Post #4 by @lassoan (2020-02-01 16:13 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="9220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>For my own use, I certainly plan to try to implement something like this for my own modules, as well as tracking across multiple modules, including built-in ones. It looks like the current version is focused only on segmentation, is that correct? A more general purpose one would probably also be useful for the Slicer community. I realize that different modules have different structures, so would be harder to track across modules in a standardized table, but even just tracking time and module name in a table would be useful.</p>
</blockquote>
</aside>
<p>User statistics module records time spent in each module and we also implemented more detailed time logging for Segment Editor module. You can add detailed logging for other modules and operations, too. It would be easy to implement a plugin interface in User statistics module so any module could register additional custom logging functions without modifying User statistics module.</p>
<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="9220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>there are two UserStatisticsTableNodes. If I don’t pay attention and delete them, they multiply</p>
</blockquote>
</aside>
<p>We have a merge function (mergeStatisticsTableNodes), which can be also used from the GUI, but maybe we should merge them automatically. Maybe we should generate a random ID for each log event to ensure that when loading a scene multiple times we don’t duplicate any entries. We could also decide to save logs in a specific folder on the computer instead of saving it with the scene. If you start using the module and see what approach makes the most sense then we can update the module accordingly. If you have any specific idea about what to change and how the best is if you send a pull request with the proposed change.</p>

---

## Post #5 by @mikebind (2020-02-14 23:04 UTC)

<p>Thanks.  I will eventually be trying to put this module to use and I’m sure I will have feedback at that point.  Currently, I’ve decided to just turn off the module.  In case someone else wants to do that and isn’t sure how, you can turn off any module via Edit menu &gt; Application Settings &gt; Modules &gt; uncheck any modules you don’t want to have available, then restart Slicer.</p>
<p>In the meantime, the multiplication of UserStatisticsTableNodes was too big of an annoyance to leave there when I wasn’t even collecting any data (the “Enable” checkbox within the UserStatistics module widget was not checked).</p>
<p>One time, I did try enabling collection of user statistics, and a few minutes later, I was struck by how slow and unresponsive Slicer had become.  After unchecking the UserStatistics “Enable” button and restarting Slicer, the application was responsive again, as usual.  I did not do any further testing, but it was suspiciously correlated with my only attempt at enabling collection of user statistics.</p>

---

## Post #6 by @lassoan (2020-02-18 02:28 UTC)

<p>Thanks for the feedback. I’ve added a button to the user information popup to disable User statistics by a single button click (and tables are not created anymore if the feature is disabled). I’ve added a <a href="https://github.com/PerkLab/SlicerSandbox/issues/5">bug report to track the slowdown issue</a>.</p>

---
