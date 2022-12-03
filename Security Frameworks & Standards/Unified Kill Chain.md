# [Unified Kill Chain](https://www.unifiedkillchain.com/)
A model published by Paul Pols "unifies" the MITRE ATT&CK and Cyber Kill Chain frameworks together. This model provides insight into tactics used by attackers to achieve their objectives.
- **Getting In**
	1. **Reconnaissance:** attacker determines what methods to use and gathers information about the target's personnel, computer systems, and supply chain.
	2. **Weaponization**: Techniques used to create scripts that target and exploit a vulnerability to gain access into a system/network.
	3. **Delivery:** Techniques used to transmit weaponized code to the target environment.
	4. Social Engineering
	5. **Exploitation:** Techniques used to execute weaponized code on the target system.
	6. **Persistence:** Teqniuques applied, allowing the attacker to maintain covert access to a target host or network.
	7. **Defense Evasion:** Defense techniques used by the attacker to evade detection from security systems, such as code obfuscation and refactoring.
	8. **Command & Control:** Weaponized code establishes an outbound channel to a remote server that can then be used to control the remote access tool (possibly download additional tools to progress the attack).
	9. **Pivoting:** process where an attacker (on an outside network) bypasses a network boundary and compromises servers on the inside network.
		- Remote access and tunneling protocols, secure shell (SSH), virtual private networking (VPN), or remote desktop.
- **Getting Through**
	1. **Pivoting**
	2. **Discovery:** Scanning for hosts, IP ranges, and routes between networks to map out the structure of the target network.
	3. **Privilege Escalation:** When an attacker exploits a vulnerability to gain higher-level access to the system.
	4. **Execution:** Techniques used to automate tasks without user input. Executing pre-written scripts provides a considerable time improvement, as the script is as fast as the computer and avoids typing delays and human error.
	5. **Credential Access:** Attackers collect credentials by attacking where credentials are often stored.
	6. **Lateral Movement:** The process by which an attacker can move from one part of a network to another.
	7. **Access**
- **Getting Out**
	1. **Access**
	2. **Collection:** Techniques used to collect data from the target and prepare for Exfiltration.
	3. **Exfiltration:** Techniques used to remove collected data from off the target network/system
	4. **Impact:** The damage caused by an attack, including data loss, financial and reputational damage, etc.
	5. **Objectives:** The attacker's goals for attacking a target system/network.
