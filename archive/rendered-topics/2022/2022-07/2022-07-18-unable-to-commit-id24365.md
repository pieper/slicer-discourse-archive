---
topic_id: 24365
title: "Unable To Commit"
date: 2022-07-18
url: https://discourse.slicer.org/t/24365
---

# Unable to commit

**Topic ID**: 24365
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/unable-to-commit/24365

---

## Post #1 by @keri (2022-07-18 12:23 UTC)

<p>Hi,</p>
<p>when executing <code>git commit</code> I get error:</p>
<pre><code class="lang-auto">Your work tree has not been configured for Slicer development.
Paste the following commands into a shell:

  ./Utilities/SetupForDevelopment.sh

See
http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Developers/DevelopmentWithGit
 for more information.
</code></pre>
<p>When I past the command directly to the powershell <code>./Utilities/SetupForDevelopment.sh</code> it simply opens it in text editor.</p>
<p>To execute I change its eextension to <code>ps1</code> and then I get error:</p>
<pre><code class="lang-auto">PS C:\S&gt; ./Utilities/SetupForDevelopment.ps1
At C:\S\Utilities\SetupForDevelopment.ps1:8 char:19
+ printErrorAndExit() {
+                   ~
An expression was expected after '('.
At C:\S\Utilities\SetupForDevelopment.ps1:9 char:47
+   echo 'Failure during git development setup' 1&gt;&amp;2
+                                               ~~~~
The '1&gt;&amp;2' operator is reserved for future use.
At C:\S\Utilities\SetupForDevelopment.ps1:10 char:47
+   echo '------------------------------------' 1&gt;&amp;2
+                                               ~~~~
The '1&gt;&amp;2' operator is reserved for future use.
At C:\S\Utilities\SetupForDevelopment.ps1:11 char:11
+   echo '' 1&gt;&amp;2
+           ~~~~
The '1&gt;&amp;2' operator is reserved for future use.
At C:\S\Utilities\SetupForDevelopment.ps1:12 char:13
+   echo "$@" 1&gt;&amp;2
+             ~~~~
The '1&gt;&amp;2' operator is reserved for future use.
At C:\S\Utilities\SetupForDevelopment.ps1:19 char:3
+ if test -d .git/.git; then
+   ~
Missing '(' after 'if' in if statement.
At C:\S\Utilities\SetupForDevelopment.ps1:36 char:16
+ ./SetupUser.sh || exit 1
+                ~~
The token '||' is not a valid statement separator in this version.
At C:\S\Utilities\SetupForDevelopment.ps1:40 char:17
+ ./SetupHooks.sh || exit 1
+                 ~~
The token '||' is not a valid statement separator in this version.
At C:\S\Utilities\SetupForDevelopment.ps1:44 char:14
+ ./GitTips.sh || exit 1
+              ~~
The token '||' is not a valid statement separator in this version.
    + CategoryInfo          : ParserError: (:) [], ParseException
    + FullyQualifiedErrorId : ExpectedExpression
</code></pre>
<p>Can’t understand what happened.</p>

---

## Post #2 by @keri (2022-07-18 12:45 UTC)

<p>I just figured out that I needed to run it within <code>GIT Bash</code></p>

---
