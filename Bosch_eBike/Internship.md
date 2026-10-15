# Six months in the Bosch eBike ABS testing team
Roko Sango  
Bosch eBike Systems, ABS department · 1 February to 31 July 2026

## Summary
I spent my engineering internship in the testing team of Bosch's eBike ABS department. The ABS keeps the front wheel from locking under hard braking, and it talks to the rest of the bike (drive unit, remote controller, display, battery) over CAN. Most of my work was software: Python tools that turn raw ECU data into something a person can read, plus a fair amount of flashing, validating and debugging on real hardware.

Two of the tools I wrote are in daily use by the team. One more started as a script and ended up as a one-click app for people who have never touched a diagnostic session.

---

## What I worked on

### BFM decoder: fault memory logs in seconds instead of half an hour
The ABS stores fault memory as blocks of hex data. To read one record, developers had to open a documentation sheet and decode it byte by byte, which took up to 30 minutes per BFM record.

I wrote a Python CLI that takes the hex, parses every field (priority, status and qualification bits, occurrence counts, and so on) and prints a readable table. It can also export to PDF. Decoding a record now takes seconds. I later set it up to be deployed through a Jenkins job so the team always gets the current version.

### FLM parser: from Excel logic to a tool anyone can use
Field Load Measurement (FLM) data holds most of what the ABS knows about a ride: brake activations, gradient control activations, odometer values, riding time and more. The team uses it for test validation, test case creation and bike checks. Until then the parsing lived in an Excel sheet.

I built it in three steps:
1. **CLI.** I moved the parsing logic out of the spreadsheet and into Python.
2. **Desktop app.** My supervisor suggested MVVM for the structure. I hadn't used it before, and it paid off quickly, because the code grew a lot once I added file loading, selectable tables, chart generation and PDF export.
3. **Plug-and-play tool.** Getting FLM data off a bike meant running UDS commands: authenticate, open a diagnostic session, pass the access right checks, then read. That is a lot to ask of someone who just wants a report. The final version does all of it behind two buttons (connect, then read and generate PDF), so anyone with access rights can pull a report.

This is the project I'm proudest of, mostly because it kept turning into something more useful than what I was originally asked for.

### BioBike wiring fault
The BioBike is a non-electric bike that carries a Bosch ABS and a remote controller. It is used by professional downhill riders. One had just been sent a test setup when the team found that CAN signals from the ABS weren't reaching the controller.

I got the task on short notice and high priority. The cause was an incorrect resistance value in the custom wiring harness, which degraded the signal. I rebuilt and soldered the harness correctly, and then travelled to France to hand the new cables to the rider in person. Debugging a physical fault under time pressure was so much different from projects I had done at university.

### Onboarding on the Bosch Remote Controller and the security setup
My first technical task was converting new remote controllers (BRCs) from production to development security state using Bosch's PKI conversion tool. It sounds small, but the BRC is the main control component of the bike, so it was the fastest way to learn how the parts interact.

### Other work
A shorter list of things that took real time but don't need their own section:
* Built a simple EMC test tool for triggering valve actuation
* Tracked down the root cause of sporadic flash timeouts on a battery test board
* Made the wheel speed sensor simulators more robust
* Fixed broken Device Farm nodes and simulation nodes
* Got the Bike in a Box (BiaB) simulation setup running
* Worked with the Automated Testing Framework (ATF) to trigger specific ABS events
* Tested new software releases and reproduced defects on test bikes, with debug messages enabled
* Created AI agents for the team and did code reviews
* Onboarded the preseason testing team on the ABS setup tool

---

## Tools and concepts
Python, CAN bus, UDS diagnostics, embedded ECU flashing, MVVM, Jenkins, Jira, Scrum (two-week sprints, daily stand-ups), hardware simulation nodes, wiring and soldering.

---

## What I took away
* **Small tools get used.** The most valuable things I made were not too complex. They just removed a tedious step from people's day.
* **Systems are messier than coursework.** A bug can sit in the software, the wiring, the timing or a tool no one has documented. You learn to rule things out one at a time.
* **Process matters more than I expected.** Scrum and Jira were things I'd learned about in a course. Seeing a team actually run on them, with sprint plannings, reviews and clear ownership, made the point much better than the lecture did.
* **Supervisors are busy.** Mine were very helpful but short on time, so I learned to onboard myself onto unfamiliar tools and come to them with specific questions.
