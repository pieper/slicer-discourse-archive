---
topic_id: 4184
title: "Slicer Logging Architecture And Flexibility"
date: 2018-09-25
url: https://discourse.slicer.org/t/4184
---

# Slicer logging architecture and flexibility

**Topic ID**: 4184
**Date**: 2018-09-25
**URL**: https://discourse.slicer.org/t/slicer-logging-architecture-and-flexibility/4184

---

## Post #1 by @jdx-john (2018-09-25 11:18 UTC)

<p>Hi, in our commercial project we are finding that default Slicer logging is pretty difficult for our users. Our app-specific logs like “Procedure initiated…” get lost amongst all the internal logging. Users struggle to inspect logs which means we have to get them to send us copies, etc, and anyway this sort of logging is normally something users wouldn’t see.</p>
<p>Does Slicer logging architecture strongly couple Slicer to using a single log for everything, or are you using a logger (perhaps a common OSS one) that allows multiple log files to be used in parallel, so we can send different categories of messages to different files?</p>
<p>(I should add our users are doctors, not DICOM experts and definitely not typical Slicer users or software developers at all)</p>

---

## Post #2 by @lassoan (2018-09-25 16:38 UTC)

<blockquote>
<p>single log for everything, or are you using a logger</p>
</blockquote>
<p>A single log file is highly desirable, as it makes most important operations such as rotation (needed for keeping used disk space under control), merging (necessary for analysis), and sharing (for error reporting) much easier.</p>
<p><strong>Intended use:</strong></p>
<p>For developers: Usually viewing with a simple text editor works well, but since log files are structured they can be loaded into a log viewer application, such as <a href="http://logging.apache.org/chainsaw/2.x/">Apache Chainsaw</a>, for searching, tagging, and advanced filtering.</p>
<p>For users: It should not be necessary for users to check the application logs. Maybe there are a few places where we wanted to save some software development time, we did not implement propagation of error messages to the user and just display a message like “… error occurred - see logs for details”. For these cases, uses can open the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog">Log window</a>, which displays a simplified, somewhat user-friendly view of events. Events are grouped by timestamp and can be filtered based on log level. Details, such as source code file names and line numbers are not displayed.</p>
<p><strong>Potential improvements:</strong></p>
<ul>
<li>More consistent logging of all user actions and better use of categories or tags - this would help in identifying what a user did exactly and make the logs more useful in general.</li>
<li>We can also improve the log viewer window to show more or less information, allow searching, or more advanced filtering.</li>
<li>We could also add a “share to web” feature, which could pack up log file and maybe a screenshot and send log to a web service, but there would be a risk of unintentional leaking patient information.</li>
<li>Automatic crash reporting (on next startup) might be useful, too (because people may not realize that they have access to logs of previous application sessions). However, crashes happen so rarely that the benefits would be limited.</li>
</ul>
<p>Overall, I don’t see any serious issues or low-hanging fruits that we should work on, but let us know if you have specific ideas or recommendations.</p>

---
