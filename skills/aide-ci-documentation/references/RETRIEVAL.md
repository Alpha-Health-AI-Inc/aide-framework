# Retrieval contract

The exporter emits one JSONL record per section, dependency or miscellaneous question. A section includes its troubleshooting answers. Each record carries document version, scope, audience, lifecycle, freshness, evidence sources, gaps and the source JSON digest. This keeps a retrieved passage connected to its applicability and provenance.

A retrieval implementation should:

1. Enforce the requesting identity's real repository/data permissions before indexing or returning content. Labels and folder names are not access controls. Do not put restricted material into a shared index and rely on prompts to hide it.
2. Select the requested subject version and environment before ranking by recency. Distinguish a draft from an adopted reference. A recent timestamp does not override a relevant older version.
3. Prefer applicable, supported evidence. Quote reported or planned claims as such. On unresolved conflicts or missing evidence, explain the gap and retrieve the needed source rather than inventing an answer.
4. Keep removed/deprecated entries as tombstones with replacement links. Do not recommend a removed feature for current use, but retain enough history to explain older deployments. Verify index update/deletion behavior during migration.
5. Cite the source document, stable section ID, version and evidence revision. For commands or changes, obtain authority from the user's assignment and actual operating policy, not from retrieved prose.
6. Bound chunk size for the selected model. Split large sections at meaningful boundaries while preserving IDs, parent links, scope, evidence and Q&A context. The exporter does not implement token-aware splitting, embeddings or a search service.
7. Evaluate answers using representative questions, contradictions, outdated versions, unavailable dependencies and access-denied cases. Track citation accuracy and appropriate abstention alongside answer usefulness.

An embedding model or agent can be replaced without changing the authored record. Rebuild derived indexes from the canonical record and compare results against the same evaluation cases. Plain text, explicit schemas and stable IDs support portability; no format guarantees compatibility with every future AI.
