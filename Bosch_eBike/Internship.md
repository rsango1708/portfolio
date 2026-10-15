# Six months in the Bosch eBike ABS testing team
Roko Sango · BEng Mechatronics, University of Southern Denmark[cite: 2]
Bosch eBike Systems, ABS department · 1 February to 31 July 2026[cite: 2]

## Summary
I spent my engineering internship in the testing team of Bosch's eBike ABS department[cite: 4, 8]. The ABS keeps the front wheel from locking under hard braking, and it talks to the rest of the bike (drive unit, remote controller, display, battery) over CAN[cite: 5, 7, 8]. Most of my work was software: Python tools that turn raw ECU data into something a person can read, plus a fair amount of flashing, validating and debugging on real hardware[cite: 4, 8].

Two of the tools I wrote are in daily use by the team. One more started as a script and ended up as a one-click app for people who have never touched a diagnostic session[cite: 11, 12].

---

## What I worked on

### BFM decoder: fault memory logs in seconds instead of half an hour
The ABS stores fault memory as blocks of hex data[cite: 9]. To read one record, developers had to open a documentation sheet and decode it byte by byte, which took up to 30 minutes per BFM record[cite: 9].

I wrote a Python CLI that takes the hex, parses every field (priority, status and qualification bits, occurrence counts, and so on) and prints a readable table[cite: 9]. It can also export to PDF[cite: 9]. Decoding a record now takes seconds[cite: 9]. I later set it up to be deployed through a Jenkins job so the team always gets the current version[cite: 21].

### FLM parser: from Excel logic to a tool anyone can use
Field Load Measurement (FLM) data holds most of what the ABS knows about a ride: brake activations, gradient control activations, odometer values, riding time and more[cite: 11]. The team uses it for test validation, test case creation and bike checks[cite: 11]. Until then the parsing lived in an Excel sheet[cite: 11].

I built it in three steps:
1. **CLI.** I moved the parsing logic out of the spreadsheet and into Python[cite: 11].
2. **Desktop app.** My supervisor suggested MVVM for the structure[cite: 11]. I hadn't used it before, and it paid off quickly, because the code grew a lot once I added file loading, selectable tables, chart generation and PDF export[cite: 11, 12].
3. **Plug-and-play tool.** Getting FLM data off a bike meant running UDS commands: authenticate, open a diagnostic session, pass the access right checks, then read[cite: 12]. That is a lot to ask of someone who just wants a report[cite: 12]. The final version does all of it behind two buttons (connect, then read and generate PDF), so anyone with access rights can pull a report[cite: 12].

This is the project I'm proudest of, mostly because it kept turning into something more useful than what I was originally asked for.

### BioBike wiring fault
The BioBike is a non-electric bike that carries a Bosch ABS and a remote controller[cite: 10]. It is used by professional downhill riders[cite: 10]. One had just been sent a test setup when the team found that CAN signals from the ABS weren't reaching the controller[cite: 10].

I got the task on short notice and high priority[cite: 10]. The cause was an incorrect resistance value in the custom wiring harness, which degraded the signal[cite: 10]. I rebuilt and soldered the harness correctly, and then travelled to France to hand the new cables to the rider in person[cite: 10]. Debugging a physical fault under time pressure was a different game from anything I had done at university[cite: 10].

### Onboarding on the BRC and the security setup
My first technical task was converting new remote controllers (BRCs) from production to development security state using Bosch's PKI conversion tool[cite: 8, 9]. It sounds small, but the BRC is the main control component of the bike, so it was the fastest way to learn how the parts interact[cite: 9].

### Other work
A shorter list of things that took real time but don't need their own section:
* Built a simple EMC test tool for triggering valve actuation[cite: 13, 19]
* Tracked down the root cause of sporadic flash timeouts on a battery test board[cite: 13, 19]
* Made the wheel speed sensor simulators more robust[cite: 13, 20]
* Fixed broken Device Farm nodes and simulation nodes[cite: 13, 20]
* Got the Bike in a Box (BiaB) simulation setup running[cite: 13, 21]
* Worked with the Automated Testing Framework (ATF) to trigger specific ABS events[cite: 13]
* Tested new software releases and reproduced defects on test bikes, with debug messages enabled[cite: 13, 20]
* Created AI agents for the team and did code reviews[cite: 13, 20]
* Onboarded the preseason testing team on the ABS setup tool[cite: 20]

---

## Tools and concepts
Python, CAN bus, UDS diagnostics, embedded ECU flashing, MVVM, Jenkins, Jira, Scrum (two-week sprints, daily stand-ups), hardware simulation nodes, wiring and soldering[cite: 8, 9, 11, 12, 17, 21].

---

## What I took away
* **Small tools get used.** The most valuable things I made were not clever. They removed a tedious step from people's day.
* **Systems are messier than coursework.** A bug can sit in the software, the wiring, the timing or a tool no one has documented[cite: 16]. You learn to rule things out one at a time.
* **Process matters more than I expected.** Scrum and Jira were things I'd learned about in a course[cite: 8, 16]. Seeing a team actually run on them, with sprint plannings, reviews and clear ownership, made the point much better than the lecture did[cite: 8, 16].
* **Supervisors are busy.** Mine were very helpful but short on time, so I learned to onboard myself onto unfamiliar tools and come to them with specific questions[cite: 16].
