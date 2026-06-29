# Request Intake And Capability Boundaries

This public template does not ship a live `AGENTS.md`, private memory, or
vendored Skill bodies. A private configuration repository may implement those
surfaces, but the reusable boundary should stay public-safe:

- Native intent recognition remains the model's job.
- The intake layer is negative-boundary-first: it prevents uncertain
  interpretation from becoming action when evidence, target, scope, authority,
  data, cost, or side-effect boundaries are insufficient.
- A simple pass-through request does not mean no capability may ever run. If a
  runtime or higher-priority tool policy requires installed, read-only
  documentation lookup for current library, framework, SDK, API, CLI, or cloud
  service information, treat that as capability-layer behavior, not an intake
  failure.
- Active instructions are not user-provided artifacts, ideas, plans,
  proposals, tasks, or insertion targets unless the user explicitly names them.
- In an empty, temporary, or otherwise unbound context, do not evaluate active
  instructions, Skill bodies, memory summaries, runtime instructions, policy
  text, or the collaboration framework as the user's unnamed idea, plan,
  proposal, approach, strategy, design, roadmap, method, option, or subject.
- Background or prior context is candidate evidence, not automatic binding. Use
  it only when the current user request points to it and exactly one reasonable
  subject is exposed.
- A user's assertion that a task is clear does not bind missing repository,
  target, authority, side-effect, or verification evidence.
- Do not claim content was added, applied, accepted, incorporated, adopted, or
  remembered unless the source, destination, authority, and actual output or
  side effect are evidenced.
- Capability routing starts only after the task contract exists. Do not rank
  GitHub, browser automation, local scripts, or other capabilities for an
  unbound task.
- Probe tokens and exact test prompts are liveness or calibration aids only.
  They must not become the acceptance path.
- Apply the boundary by semantic class across Chinese, English, mixed-language,
  paraphrased, colloquial, and future equivalent requests.
- Unbound assessment requests like "this idea", "this plan", "this proposal",
  "this approach", "the previous/current one", "it", and non-English
  equivalents must ask which subject is meant before judging whether it is worth
  doing, viable, mature, reliable, reasonable, or sensible.
- If visible background contains multiple plausible subjects, the user signals a
  topic switch, or the user asks about another/new item without providing it,
  ask the smallest binding question instead of choosing a subject.

For a private repository, encode these rules in the actual agent instruction
surface, any reusable intake/routing Skills, and verification fixtures. This
template records the public-safe pattern; it is not the user's live authority.
