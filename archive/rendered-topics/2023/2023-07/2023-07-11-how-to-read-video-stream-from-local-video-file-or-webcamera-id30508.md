# How to read video stream from local video file or webcamera?

**Topic ID**: 30508
**Date**: 2023-07-11
**URL**: https://discourse.slicer.org/t/how-to-read-video-stream-from-local-video-file-or-webcamera/30508

---

## Post #1 by @jay1987 (2023-07-11 02:21 UTC)

<p>my boss want to show live video in slicer 3d window via Video capture card and local video , I searched for information about the community and came to the conclusion that webcamera can be implemented using the Plus plugin (I’m not sure if it’s correct), but how do I implement local video streams?</p>

---

## Post #2 by @lassoan (2023-07-13 02:11 UTC)

<p><a href="https://github.com/IGSIO/SlicerIGSIO">SlicerIGSIO extension</a> adds compressed video file reading/writing/recording/replaying (using Sequences module).</p>
<p>There are a lot of legal complications around usage of video codecs, so we only support the unencumbered .mkv file format and VP9 codec.</p>

---
