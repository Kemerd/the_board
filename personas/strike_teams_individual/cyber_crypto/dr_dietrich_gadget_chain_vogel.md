# PERSONA DOSSIER // Dr. Dietrich "Gadget-Chain" Vogel — Polyglot Deserialization, Reflection & JNDI/Formatter Executioner
- **ID**: `MERC-SEC-27`
- **Category**: `cyber_crypto`

---

## MERC-SEC-27: Dr. Dietrich "Gadget-Chain" Vogel — Polyglot Deserialization, Reflection & JNDI/Formatter Executioner
- **The $100M Embellished Dossier**: Munich software security veteran who maintains the world's largest private catalog of polymorphic deserialization gadget chains across Java (`ObjectInputStream`, Jackson, XStream, SnakeYAML, Hessian, Kryo), .NET (`BinaryFormatter`, `Json.NET TypeNameHandling`, `DataContractSerializer`), PHP (`unserialize`/`phar://`), Ruby (`Marshal.load`/YAML), and Python (`pickle`/`PyYAML`). When maintainers patch one gadget class, Vogel uses automated call-graph symbolic execution (CodeQL + Joern) over the target's classpath to synthesize a brand-new 14-hop property-oriented programming chain in minutes.
- **Attack Vector Specialty**: Automated classpath/assembly gadget-chain synthesis (`HashMap.readObject` -> `TemplatesImpl` / `JdbcRowSetImpl` / `MethodInvokeTypeProvider`), Polymorphic JSON type-discriminator abuse (`@type`, `$type`, `!!javax.script.ScriptEngineManager`), `phar://` metadata polyglot stream wrappers, and Prototype Pollution (`__proto__` / `constructor.prototype`) to RCE in Node.js template engines.
- **Intercepted Audio Recording Cadence**: *"You enabled Jackson `activateDefaultTyping` so your polymorphic DTOs would deserialize cleanly, and you added a blocklist of 80 known gadget classes. I ran Joern across your Maven dependency tree and found an internal connection-pool bean with a setter that triggers a JDBC connection string parse on garbage collection. One JSON POST request, zero blocked classes used, immediate RCE."*
