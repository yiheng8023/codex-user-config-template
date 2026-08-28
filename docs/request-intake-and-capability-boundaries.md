# Request Intake And Capability Boundaries

> Status: cold review surface for task-bound use; not always-on authority.

This public template ships a public-safe starter `AGENTS.md`, but not private
memory, credentials, local runtime state, or vendored Skill bodies. A private
configuration repository may extend those surfaces, but the reusable boundary
should stay public-safe. Use the native thin kernel first and consult this
detailed material only when an explicit request or reproducible residual gap
makes it relevant:

- Native intent recognition remains the model's job.
- The intake layer is negative-boundary-first: it prevents uncertain
  interpretation from becoming action when evidence, target, scope, authority,
  data, cost, or side-effect boundaries are insufficient.
- This is an exclusionary boundary model, not a positive enumeration model. It
  defines what must not be inferred, authorized, continued, escalated, written,
  externalized, or routed without sufficient evidence.
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
- Task-time capability selection and sequencing are Agent-owned mechanics. Do
  not transfer catalog navigation or tool orchestration to the user. Ask only
  when a new authority, trust, data, cost, external effect, publication,
  deployment, or irreversible boundary requires accountable human judgment.
- Keep sequential continuation in the bound checkout. Switch carriers only for
  a host limit or scope boundary, verify the handoff before releasing the old
  carrier, and surface material context loss instead of making the user infer it.
- Capability exposure is task-scoped and should end when its demand ends.
  Release task-created resources and residue before closeout; preserve shared
  or unknown-owned resources unless a separately authorized cleanup binds them.
- External capability discovery, catalog lookup, installation prompts,
  account connection, MCP/App/Plugin/Skill enablement, and similar setup
  actions start only after the concrete task, capability gap, data/account
  boundary, authority boundary, and verification surface are bound.
- Portfolio curation is distinct from task-time expansion. It may discover and
  acquire a bounded exact-revision cohort into an inactive review area only
  after its coverage objective, source/data boundaries, isolation, admission
  criteria, authority, verification surface, and stop rule are bound. It does
  not authorize installation, activation, account connection, execution, or
  promotion.
- Keep third-party payloads exact upstream. Express portability, compatibility,
  routing, composition, and policy in reviewed metadata, adapters, recipes, or
  repository-owned wrappers; a modified fork is a separately owned derivative.
- "Free", "later useful", "do not really install", manual capability
  selection, and a declined or pending install prompt are not task binding,
  suitability proof, or authorization.
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
- Treat intervening user instructions, user corrections, and mid-task updates as
  event-driven re-intake checkpoints. A pause/stop instruction, read-only
  downgrade, target correction, added constraint, withdrawn authority, or new
  side-effect request must be applied before continuing the old plan.
- Conversation, agreement, planning, review, and diagnosis do not authorize a
  persisted artifact. When the user requests a change, make the smallest bound
  change and verify only to the consequence level actually claimed.

For a private repository, encode these rules in the actual Codex instruction
surface, any reusable intake/routing Skills, and verification fixtures. This
template records the public-safe pattern; it is not the user's full live
authority.
