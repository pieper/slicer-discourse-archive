---
topic_id: 27065
title: "Cli Xml Schema Password"
date: 2023-01-05
url: https://discourse.slicer.org/t/27065
---

# CLI XML schema password

**Topic ID**: 27065
**Date**: 2023-01-05
**URL**: https://discourse.slicer.org/t/cli-xml-schema-password/27065

---

## Post #1 by @fbordignon (2023-01-05 22:45 UTC)

<p>Greetings everyone.<br>
Would it be desirable to have a special XML field for passwords in the CLI XML schema?<br>
I have a use case that a CLI calls some functions via paramiko on a ssh connections and the user needs to input a password for slicer to pass as parameter to a python CLI.<br>
I understand the some security issues arise such as logging the user password which may require a hashing scheme of some sorts. I want to hear your thought on this issue, please.<br>
Thank you very much.</p>

---

## Post #2 by @pieper (2023-01-05 23:46 UTC)

<p>There’s a string parameter type, can you just use that?</p>
<p>I don’t know paramiko, but if it’s like ssh you may also have the option of putting keys in .ssh folders, which would be more secure and probably easier than entering the password all the time.</p>

---

## Post #3 by @lassoan (2023-01-06 03:01 UTC)

<p>I agree. Using key or token files should be the way to go, and string or file values should work for these. Since the file path is not sensitive information, it can show up in logs.</p>

---

## Post #4 by @fbordignon (2023-01-06 14:07 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I was thinking on a special field to use *** masking the password and doing some sort of hashing to pass to the command line interface, but I guess you are right. Using keys would be the most elegant way to solve the issue. I may create an auxiliary module designed to help the user generate keys and do a ssh-copy-id to the server before using the CLI. That way the user inputs the password momentarily and inside Slicer only. Another option will be just showing a help text to teach them how to issue ssh-keygen and ssh-copy-id</p>

---

## Post #6 by @fbordignon (2023-02-15 14:40 UTC)

<p>Hi guys, as you stated before, using keys is the solution to this one.<br>
But when I use a <code>&lt;file&gt;</code> parameter type, the user is asked to chose the ssh  pub key. I wanted to make things easier for them and set a <code>&lt;default&gt;</code> key file. Is there a way to set a default in the XML file and use something like <code>&lt;default&gt;%USERPROFILE%\.ssh\id_rsa.pub&lt;/default&gt;</code>?<br>
I guess it would need special treatment for each platform which complicates things.<br>
If there is no way to do that, I can treat the case the user does not change the default inside the CLI, changing the variable to the actual user profile folder.</p>

---

## Post #7 by @pieper (2023-02-15 14:54 UTC)

<p>In principle it would be possible add this to the CLI mechanism if it’s not already supported (I don’t recall but I think not).  But realistically the CLI mechanism is a bit hard to customize so you might be better off using a scripted. module to add some custom widgets to what the CLI generates.</p>

---

## Post #8 by @lassoan (2023-02-17 04:46 UTC)

<p>Probably you can specify a default value, but I think it has to be the same for all platforms. We often use the empty value as an indication that some default/automatic value should be used. For example, specify the key file or leave the path empty for auto-detect.</p>
<p>If you need more fine-tuned user experience then I agree with <a class="mention" href="/u/pieper">@pieper</a> that you can add a thin convenience GUI frontend (or implement the entire logic) as a Python scripted module.</p>

---
