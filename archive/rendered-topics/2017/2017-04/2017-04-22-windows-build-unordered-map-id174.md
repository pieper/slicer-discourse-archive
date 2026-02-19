---
topic_id: 174
title: "Windows Build Unordered Map"
date: 2017-04-22
url: https://discourse.slicer.org/t/174
---

# Windows build, unordered_map

**Topic ID**: 174
**Date**: 2017-04-22
**URL**: https://discourse.slicer.org/t/windows-build-unordered-map/174

---

## Post #1 by @tdiprima (2017-04-22 09:42 UTC)

<p>Hi all,</p>
<p>I’m using the <code>&lt;tr1/unordered_map&gt;</code> header and <code>std::tr1</code> namespace in one of my programs.  Works fine for Linux.</p>
<p>During the nightly build for Windows, I’m getting errors.</p>
<p>I believe <code>#include &lt;unordered_map&gt;</code> is available with Visual Studio 2012 (this is the compiler you’re using, right?)</p>
<p>Just looking for a sanity check.  That’s it, right?  No namespace, it’s just <code>unordered_map</code>, correct?</p>
<p>Thanks a lot.</p>
<p>– Tammy</p>

---

## Post #2 by @lassoan (2017-04-22 11:53 UTC)

<p>The officially supported compiler on Windows is VS2013. You can download it for free (the free Community edition is functionally the same as the professional editions).</p>

---

## Post #3 by @tdiprima (2017-04-22 15:26 UTC)

<p>Thank you for the correct version.  Now all I need is to get Windows.  And I’m so <em>not</em> a Windows person, I feel all thumbs with it. <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=5" title=":confused:" class="emoji" alt=":confused:"></p>
<p>If by any chance anybody else has come across this, could you please let me know what worked?  I feel like I’m close to solving this…</p>
<p>Thanks again.</p>

---

## Post #4 by @gcsharp (2017-04-22 15:45 UTC)

<p>If you don’t have Windows, I recommend the virtual machine provided by Microsoft.</p>
<p><a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/" class="onebox" target="_blank" rel="nofollow noopener">https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/</a></p>
<p>Regarding your original question, you probably need to remove the “tr1” part for MSVC.</p>

---

## Post #5 by @lassoan (2017-04-22 20:03 UTC)

<p>Probably the best is to follow the official documentation:<br>
<a href="https://msdn.microsoft.com/en-us/library/bb982522(v=vs.120).aspx" class="onebox" target="_blank">https://msdn.microsoft.com/en-us/library/bb982522(v=vs.120).aspx</a></p>
<p>It is specified there what header to include and what namespace the class is in.</p>
<p>If you update your code according to the documentation but you still have build errors on the factory then let me know and I’ll have a look.</p>

---

## Post #6 by @blowekamp (2017-04-25 17:33 UTC)

<p>Hello,</p>
<p>Using TR1 features can be really tricky across platforms. You have a couple things to look out for:</p>
<ul>
<li>Is C++11 being used? ( using the tr1 spec or the C++11 spec? )</li>
<li>the location of the header ( some require the tr1 subdirectory ).</li>
<li>Is the header even available?</li>
</ul>
<p>Specifically, with OS X and clang the behavior is dependent on if libstdc++ or libc++, this header may not even be available with out C++11.</p>
<p>In SimpleITK I use this same header, I wrote a little wrapper which may be useful:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SimpleITK/SimpleITK/blob/next/Code/Common/include/nsstd/unordered_map.h" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SimpleITK/SimpleITK/blob/next/Code/Common/include/nsstd/unordered_map.h" target="_blank" rel="nofollow noopener">SimpleITK/SimpleITK/blob/next/Code/Common/include/nsstd/unordered_map.h</a></h4>
<pre><code class="lang-h">/*=========================================================================
*
*  Copyright Insight Software Consortium
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*         http://www.apache.org/licenses/LICENSE-2.0.txt
*
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License.
*
*=========================================================================*/
#ifndef sitk_nsstd_unordered_map_h
#define sitk_nsstd_unordered_map_h

</code></pre>

  This file has been truncated. <a href="https://github.com/SimpleITK/SimpleITK/blob/next/Code/Common/include/nsstd/unordered_map.h" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It is based on a couple try compiles.</p>
<p>HTH,<br>
Brad</p>

---

## Post #7 by @tdiprima (2017-04-26 13:36 UTC)

<p>Cool.  Thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I’ll use that in our next release.</p>
<p>What I ended up <a href="https://github.com/SBU-BMI/SlicerPathology/blob/cdba3a3fa218d587e782cad5430b581d554ff613/QuickTCGA/Logic/NucleusSeg_Yi/ConnComponents.h#L13-L19" rel="noopener nofollow ugc">doing</a> in the meantime is - I’m checking existence of header using the <a href="https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B" rel="noopener nofollow ugc">Internal version numbering</a>:</p>
<blockquote>
<pre><code>values of _MSC_VER for various versions of the Visual C++ compiler:
MSVC++ 12.0 _MSC_VER == 1800 (Visual Studio 2013)
</code></pre>
</blockquote>

---
