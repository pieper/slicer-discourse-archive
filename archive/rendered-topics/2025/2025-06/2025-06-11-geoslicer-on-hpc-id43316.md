---
topic_id: 43316
title: "Geoslicer On Hpc"
date: 2025-06-11
url: https://discourse.slicer.org/t/43316
---

# GeoSlicer on HPC

**Topic ID**: 43316
**Date**: 2025-06-11
**URL**: https://discourse.slicer.org/t/geoslicer-on-hpc/43316

---

## Post #1 by @Lucas_Givord (2025-06-11 15:59 UTC)

<p>Hello everyone,</p>
<p>I saw this post discourse about a slicer based app focused on geological use case : <a href="https://discourse.slicer.org/t/geoslicer-open-source-release/37157" class="inline-onebox">GeoSlicer open source release</a>.</p>
<p>From what I read on <a href="https://github.com/petrobras/GeoSlicer" rel="noopener nofollow ugc">Github</a>, this application seems also to target HPC. AFAIK Slicer doesn’t support distributed IO/Processing/Rendering so I’m curious about how they did it.</p>
<p><a class="mention" href="/u/fbordignon">@fbordignon</a> do you have some inputs for me?</p>
<p>FYI <a class="mention" href="/u/thibault_pelletier">@Thibault_Pelletier</a> <a class="mention" href="/u/finetjul">@finetjul</a></p>

---

## Post #2 by @fbordignon (2025-06-25 17:48 UTC)

<p>Hey Lucas. How are you doing? We are using GeoSlicer inside an HPC environment by using a <a href="https://github.com/selkies-project/docker-nvidia-egl-desktop" rel="noopener nofollow ugc">singularity container</a>, so GeoSlicer is run inside a powerful computer, not really distributed, so it is not getting the most out of the cluster this way.</p>
<p>The second way we are leveraging the cluster is to sort of to function as a cli mechanism but inside the cluster. So GeoSlicer sends the data to the cluster and start and monitor slurm jobs to process the data on the cluster, using algorithms developed with an HPC environment in mind, i.e. using distributed computing.</p>
<p>What exactly are you trying to achieve. Maybe we could help develop the modules you need or point you in some direction. Thanks and sorry for not responding sooner.</p>

---

## Post #3 by @Lucas_Givord (2025-06-26 07:41 UTC)

<p>Hello <a class="mention" href="/u/fbordignon">@fbordignon</a>,</p>
<p>Thanks, that’s clear for me now, your approach seems really interesting.  I don’t intend to develop something currently, I was just exploring Slicer capabilities especially for distributed use case.</p>
<blockquote>
<p>Thanks and sorry for not responding sooner.</p>
</blockquote>
<p>no worries, thanks for your time! <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=14" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @fbordignon (2025-06-26 14:13 UTC)

<p>Alright, for future reference our slurm job monitor is implemented using a view:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/petrobras/GeoSlicer/blob/main/src/modules/JobMonitor/JobMonitor.py">
  <header class="source">

      <a href="https://github.com/petrobras/GeoSlicer/blob/main/src/modules/JobMonitor/JobMonitor.py" target="_blank" rel="noopener nofollow ugc">github.com/petrobras/GeoSlicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/petrobras/GeoSlicer/blob/main/src/modules/JobMonitor/JobMonitor.py" target="_blank" rel="noopener nofollow ugc">src/modules/JobMonitor/JobMonitor.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/petrobras/GeoSlicer/blob/main/src/modules/JobMonitor/JobMonitor.py" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-py">import datetime
import json
import logging
import os

from collections import OrderedDict
from dataclasses import dataclass
from functools import partial
from pathlib import Path

import qt
import slicer

from ltrace.remote.connections import JobExecutor
from ltrace.remote.jobs import JobManager
from ltrace.remote.targets import Host
from ltrace.slicer import ui
from ltrace.slicer.widget.elided_label import ElidedLabel
from ltrace.slicer_utils import LTracePlugin, LTracePluginWidget, LTracePluginLogic

</code></pre>



  This file has been truncated. <a href="https://github.com/petrobras/GeoSlicer/blob/main/src/modules/JobMonitor/JobMonitor.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and a model with the logic:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/petrobras/GeoSlicer/blob/main/src/ltrace/ltrace/remote/jobs.py">
  <header class="source">

      <a href="https://github.com/petrobras/GeoSlicer/blob/main/src/ltrace/ltrace/remote/jobs.py" target="_blank" rel="noopener nofollow ugc">github.com/petrobras/GeoSlicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/petrobras/GeoSlicer/blob/main/src/ltrace/ltrace/remote/jobs.py" target="_blank" rel="noopener nofollow ugc">src/ltrace/ltrace/remote/jobs.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/petrobras/GeoSlicer/blob/main/src/ltrace/ltrace/remote/jobs.py" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-py">import time
import typing
from collections import OrderedDict
import logging
from queue import Queue

import json
from pathlib import Path

from typing import Callable, Dict, List
from threading import Lock, Thread

from ltrace.remote import errors
from ltrace.remote.connections import ConnectionManager, JobExecutor


class JobManager:
    jobs: OrderedDict[str, JobExecutor] = OrderedDict()
    storage: Path = None
    connections: ConnectionManager = None
</code></pre>



  This file has been truncated. <a href="https://github.com/petrobras/GeoSlicer/blob/main/src/ltrace/ltrace/remote/jobs.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There is the need to implement a specific handler for each use case different than ours.</p>

---
