---
topic_id: 2350
title: "New 3D Slicer Module That Connects To A Mysql Db"
date: 2018-03-18
url: https://discourse.slicer.org/t/2350
---

# New 3D Slicer Module that Connects to a MySQL DB

**Topic ID**: 2350
**Date**: 2018-03-18
**URL**: https://discourse.slicer.org/t/new-3d-slicer-module-that-connects-to-a-mysql-db/2350

---

## Post #1 by @Carlo (2018-03-18 19:31 UTC)

<p>Hi all,<br>
I’m creating a new module for 3D Slicer 4.8.1. It will have to connect to MySql database. So, first of all I installed mysql-connetor in ubuntu</p>
<blockquote>
<p>pip install mysql-connector</p>
</blockquote>
<p>then in my 3D Slicer module I added</p>
<blockquote>
<p>import mysql.connector</p>
</blockquote>
<p>But when I run 3D Slicer, it tells me</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/pippo/Git/Project/src/Module.py”, line 8, in <br>
import mysql.connector<br>
ImportError: No module named mysql.connector</p>
</blockquote>
<p>Can someone help me?</p>
<p>Thanks</p>
<p>Carlo</p>

---

## Post #2 by @lassoan (2018-03-18 20:39 UTC)

<p>See detailed instructions here: <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984">Slicer-Python Packages Use and Install</a></p>

---

## Post #3 by @gleman (2018-03-19 15:54 UTC)

<p>I was able to get pymsql to work with slicer.  It’s pretty straightforward.</p>

---
