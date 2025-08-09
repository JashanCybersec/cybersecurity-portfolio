# Linux Log Analysis Script

This Python script parses an SSH authentication log (`auth.log`) and counts failed login attempts by IP address.

**Usage:**
- Place an `auth.log` file in the same directory.
- Run the script with `python3 linux-log-analysis.py`.
- Output shows failed SSH login counts per IP.




## Labs & Walkthroughs

### TryHackMe Basic Pentesting Walkthrough

**Target IP:** 10.201.93.146

- Full port scan revealed ports: 22 (SSH), 80 (HTTP), 139 & 445 (Samba), 8009 (AJP13), 8080 (Tomcat).
- Enumerated Samba shares; found `staff.txt` with notes.
- Brute forced SSH user `jan` with Hydra; password found: `armando`.
- Logged in as `jan`; found SSH keys for user `kay`.
- Cracked SSH key password with John the Ripper: `beeswax`.
- Logged in as `kay`; found `/home/kay/pass.bak` with a strong password.
- Used password to escalate to root.

*Summary:* Enumeration, brute forcing, key cracking, and privilege escalation practiced.

