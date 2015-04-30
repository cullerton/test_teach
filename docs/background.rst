.. _background-reference-label:

Background
==========

In this lesson, we discuss some motivation and introduce the concept of logging levels.

--------------
Event Tracking
--------------

Logging allows your application to track events.

This can help you see how your application is actually used.

Event tracking can be used for reporting and to debug problems.

-------------
Variable Data
-------------

Your log statements can contain variable information from the application,
including error messages and exceptions from third parties.

--------------
Logging Levels
--------------

Some of the messages you log will be informational only, while others could tell
you about critical problems with your application.

Most logging systems allow you to differentiate between levels of importance,
and tag your log messages with a specific level.

Then, when your application is running, you can choose which levels to view.

Python Logging Levels:
----------------------

======== =========================================================
Level    What
======== =========================================================
Debug    Detailed, for diagnosing problems
Info     Things are working as expected
Warning  Something unexpected happened, application working
Error    Application could not perform function, but still running
Critical Serious error, application may not be working
======== =========================================================

Logging Level Order
-------------------

- Logging levels are **ordered**.
- When you choose to view a particular level, you **also see the more important levels**.
- As an example, if you set the logging level to **Info**:

    - You see levels Info, Warning, Error and Critical.
    - You do not see level Debug.

- Python defaults to viewing level **Warning**.

--------
Question
--------

By default, which logging levels will you see displayed in a Python application?
