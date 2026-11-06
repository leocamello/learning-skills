# learning-skills

**AI Agent Skills for Human Learning — Not Machine Learning**

**Stop using AI as a crutch; use it as a cognitive gym.**

An answer you recognize is not a skill you can use. These six reusable instruction files turn your AI into a tutor that asks you to retrieve, explain, apply, and defend what you know. You do the thinking. The agent supplies the next useful challenge.

[Português](README.pt.md) · [Try a live demo](examples/Before-And-After-PT.md) · [Contribute](CONTRIBUTING.md) · [MIT license](LICENSE)

| With passive AI | With learning-skills |
| --- | --- |
| “Explain it again.” | Explain it yourself; expose the missing link. |
| Copy a complete solution. | Make one reasoning move; earn the next hint. |
| Reread until it feels familiar. | Retrieve without notes; test on a new situation. |
| “Your argument looks great!” | Defend it against its strongest counterexample. |

## Pick your cognitive workout

| Skill | Reach for it when… | What you actually do | Evidence of progress |
| --- | --- | --- | --- |
| 🗺️ [Curriculum Architect](skills/01-curriculum-architect/SKILL.md) | “I want to learn X. Where do I start?” | Diagnose prerequisites and build a focused sequence. | Complete a small, observable project at each node. |
| 🧭 [Socratic Tutor](skills/02-socratic-tutor/SKILL.md) | “I’m stuck on this problem.” | Answer one question at a time, with progressive hints. | Solve a fresh variant without hints. |
| 🗣️ [Feynman Validator](skills/03-feynman-validator/SKILL.md) | “I think I understand this.” | Teach a skeptical novice in plain language. | Explain the mechanism and an unfamiliar case. |
| 🧠 [Retention Engine](skills/04-retention-engine/SKILL.md) | “Test me on these notes.” | Retrieve, apply, and diagnose failures. | Pass a mixed recall test; export atomic flashcards. |
| 🌉 [Mental Model Bridge](skills/05-mental-model-bridge/SKILL.md) | “Make this unfamiliar idea click.” | Map it to something you know; find the analogy’s limits. | Reason about the target without the analogy. |
| ⚔️ [Devil’s Advocate](skills/06-devils-advocate/SKILL.md) | “Challenge my argument or design.” | Defend assumptions and repair weak claims. | Handle a new counterexample with evidence. |

Unsure? Use the [Learner Orchestrator](agents/learner-orchestrator.md). It diagnoses the immediate bottleneck and routes to **one skill at a time**. You can pause, change language, or leave learning mode at any point.

## Start in 30 seconds: any web chatbot

No terminal, API key, paid integration, or coding knowledge required for the paste-in workflow. You need access to a chatbot; saved assistants may depend on your account.

1. Open [Socratic Tutor](skills/02-socratic-tutor/SKILL.md), choose **Raw**, and copy the file’s text.
2. Paste it into a new ChatGPT, Claude, or Gemini conversation.
3. Add: **“Use these instructions for our learning session. I want to understand SQL JOINs. Ask your first question in English.”**

The first response should contain one diagnostic question, not a completed explanation. If the model dumps the answer, say: **“Return to the skill’s diagnostic phase. Ask one question and wait.”** Instructions guide model behavior; they are not a technical enforcement boundary.

### Save your learning assistant

| Platform | Setup |
| --- | --- |
| **ChatGPT Custom Instructions** | In Settings → Personalization, add the short instruction below. Paste the full chosen skill into each study conversation. Custom Instructions are a short entry point, not storage for all six files. [Official guide](https://learn.chatgpt.com/docs/personalize). |
| **ChatGPT custom GPTs** | Where GPT creation is available, paste one skill’s body into **Instructions**. If the editor’s limit prevents this, put the full file in **Knowledge** and use the activation instruction below in Instructions. Start a preview chat to verify it. [Official overview](https://developers.openai.com/api/docs/actions/introduction). |
| **Claude Projects** | Create a study project, add the chosen skill as a project file, and place the activation instruction below in project instructions. Start a new project chat. [Official guide](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects). |
| **Gemini Gems** | In Gemini on the web, open Gems → New Gem. Paste one skill’s body into Instructions and save. If you use an attached file instead, add the activation instruction below. Google announces migration of personal-account Gems to skills starting November 2026; follow the controls shown in your account or use the paste-in workflow. [Official guide](https://support.google.com/gemini/answer/15146780?hl=en). |

Short Custom Instructions:

```text
When I explicitly ask to study or practise, use the learning-skills file I provide. Ask one question at a time, wait for my attempt, and use progressive hints instead of giving away the exercise. Match my language. Check understanding on a fresh task without hints. If no skill is available, ask me to paste it. Respect pause and exit requests.
```

Activation instruction for an attached file:

```text
For this study session, read the attached Socratic Tutor SKILL.md and follow its complete protocol. If you cannot access the file, tell me and ask me to paste it; do not claim it is loaded. Begin with one diagnostic question in my language.
```

To enable routing, put the [orchestrator](agents/learner-orchestrator.md) body in your assistant’s instructions and attach the six skills. Rename uploaded copies to `curriculum-architect.md`, `socratic-tutor.md`, `feynman-validator.md`, `retention-engine.md`, `mental-model-bridge.md`, and `devils-advocate.md` so six identically named files do not collide. The orchestrator recognizes these aliases. File retrieval is not guaranteed: test the first turn, and paste the selected file if retrieval fails.

## Start in 30 seconds: CLI and IDE agents

**Fastest path:** download this repository with **Code → Download ZIP**, extract it, and open it in your editor. In your agent chat, attach `skills/02-socratic-tutor/SKILL.md` and say:

```text
Read this SKILL.md and use socratic-tutor to help me reason about a failing JOIN. Ask one question, then wait for my answer. Do not modify files or run my solution for me.
```

This explicit-file workflow also works when your client does not support native skill discovery.

For native project discovery, copy the six folders into your client’s skill directory. From the extracted repository, run the following in **Bash, macOS Terminal, Linux, WSL, or Git Bash**. This installs into the current project, not globally:

```bash
# Claude Code; choose another destination from the table below if needed.
destination=.claude/skills
mkdir -p "$destination"
for source in skills/[0-9][0-9]-*; do
  name="${source##*/}"
  name="${name#??-}"
  if [ -e "$destination/$name" ]; then
    printf 'Already exists; skipped: %s\n' "$destination/$name"
  else
    cp -R "$source" "$destination/$name"
  fi
done
```

| Client | Set `destination` to | Start the session |
| --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills` | `/socratic-tutor Help me understand SQL JOINs` |
| [Cursor](https://cursor.com/docs/skills) | `.cursor/skills` | Select `socratic-tutor` from the `/` menu, or explicitly ask to use it. |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) | `.github/skills` | Ask Copilot’s agent to use `socratic-tutor`; skill support depends on the client/version. |
| **Windsurf** | `.windsurf/skills` ([maintained installer mapping](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)) | Ask Cascade to use `socratic-tutor`; if discovery is unavailable, attach the file explicitly. |

The numbered source folders keep the catalog ordered. Installed folder names match the frontmatter `name`. These files include the requested project field `cognitive_principle`; a strict host may reject unknown YAML fields. If so, move that field into the Markdown body **in your installed copy**, or use the explicit-file workflow. No client-specific runtime is required. To remove a copied skill, delete its installed folder; the source stays intact.

## Try a useful session

```text
Use curriculum-architect. I have four weeks, three hours a week, and basic HTML. I want to build a small accessible website. Diagnose my starting point before planning.
```

```text
Use feynman-validator. I will explain the difference between authentication and authorization. Challenge any unexplained terms. Speak Portuguese with me.
```

```text
Use retention-engine on the notes I attach. I have 15 minutes. Test my recall before showing answers, then export Front/Back cards for the gaps we find.
```

```text
Use devils-advocate. My thesis is that all university lectures should be replaced by recorded videos. Help me test the assumptions without writing the essay for me.
```

A typical session follows **attempt → targeted feedback → revised attempt → independent transfer**. Planning and flashcards are tools, not proof of learning. “Demonstrated this session” means a fresh task was completed without help; durable retention requires another check on a later day.

The files are written in English for consistent maintenance. **Every skill must interact in the learner’s language**, including Portuguese, English, and Spanish. No translation of the skill file is needed.

## What this project promises

- **Work before answers:** one actionable question or task per turn; no answer hidden inside a leading question.
- **Support before frustration:** smaller steps, three levels of hints, and worked examples of a different problem when needed. Learners can pause or exit.
- **Evidence before praise:** independent explanation or application, not confidence, speed, or agreement.
- **Portable text:** inspectable Markdown, no backend, no telemetry, no required API. Your chatbot provider still handles anything you submit to it.

The protocols draw on retrieval practice, self-explanation, scaffolding, and analogical transfer. Their exact prompts, thresholds, and review intervals are design choices, not a clinically or experimentally validated intervention. The “80/20” lens is a prioritization heuristic, not a measured law of learning. [Research and contribution standards](CONTRIBUTING.md#evidence-and-claims) explain the boundaries.

## Make it yours

Educators: adapt one skill to a learning outcome and run a short anonymous classroom trial. Students: fork a skill for your course, share an anonymized before/after interaction, and report where it gave away the answer or made you feel stuck. Contributors: use the [PR recipe and cognitive science checklist](CONTRIBUTING.md).

**If a skill helped you solve something without AI, star the repository and share that moment.** Bring a reproducible example rather than a promise of better grades.

Inspired by the modular, immediately useful approach of [Addy Osmani’s agent-skills](https://github.com/addyosmani/agent-skills) and [Matt Pocock’s skills](https://github.com/mattpocock/skills). Independent project; no affiliation or endorsement implied.

[MIT licensed](LICENSE). Fork, adapt, translate, and teach with it.
