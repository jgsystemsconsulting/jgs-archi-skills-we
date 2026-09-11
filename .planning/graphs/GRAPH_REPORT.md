# Graph Report - .  (2026-09-11)

## Corpus Check
- 22 files · ~105,433 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 121 nodes · 232 edges · 17 communities detected
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 38 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]

## God Nodes (most connected - your core abstractions)
1. `pick_id()` - 12 edges
2. `main()` - 12 edges
3. `main()` - 8 edges
4. `MCP` - 8 edges
5. `MCP` - 8 edges
6. `MCP` - 7 edges
7. `MCP` - 7 edges
8. `MCP` - 7 edges
9. `MCP` - 7 edges
10. `main()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `pick_id()` --calls--> `main()`  [INFERRED]
  docs\runs\job05_technology_physical.py → docs\runs\moorfield\job01_build.py
- `pick_id()` --calls--> `main()`  [INFERRED]
  docs\runs\job05_technology_physical.py → docs\runs\moorfield\job01_fix_rels.py
- `pick_id()` --calls--> `main()`  [INFERRED]
  docs\runs\job05_technology_physical.py → docs\runs\moorfield\job01_place_layout.py
- `pick_id()` --calls--> `main()`  [INFERRED]
  docs\runs\job05_technology_physical.py → docs\runs\moorfield\job02_build.py
- `pick_id()` --calls--> `ensure_element()`  [INFERRED]
  docs\runs\job05_technology_physical.py → docs\runs\moorfield\job04_build.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.33
Nodes (7): as_list(), find_folder(), main(), MCP, search_exact(), unwrap(), main()

### Community 1 - "Community 1"
Cohesion: 0.32
Nodes (6): as_list(), main(), MCP, pick_id(), Normalize MCP call return that may still wrap result., unwrap()

### Community 2 - "Community 2"
Cohesion: 0.25
Nodes (6): main(), main(), find_folder(), main(), search_exact(), main()

### Community 3 - "Community 3"
Cohesion: 0.4
Nodes (4): as_list(), main(), MCP, pick_id()

### Community 4 - "Community 4"
Cohesion: 0.42
Nodes (2): main(), MCP

### Community 5 - "Community 5"
Cohesion: 0.44
Nodes (3): main(), MCP, pick_id()

### Community 6 - "Community 6"
Cohesion: 0.44
Nodes (3): main(), MCP, pick_id()

### Community 7 - "Community 7"
Cohesion: 0.47
Nodes (2): main(), MCP

### Community 8 - "Community 8"
Cohesion: 0.5
Nodes (2): main(), MCP

### Community 9 - "Community 9"
Cohesion: 0.5
Nodes (2): main(), MCP

### Community 10 - "Community 10"
Cohesion: 0.52
Nodes (6): collect_placed(), ensure_element(), ensure_rel(), find_folder(), main(), search_exact()

### Community 11 - "Community 11"
Cohesion: 0.57
Nodes (6): ensure_element(), ensure_rel(), find_folder(), main(), search_exact(), pick_id()

### Community 12 - "Community 12"
Cohesion: 1.0
Nodes (1): main()

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (1): main()

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (1): main()

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (0): 

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **1 isolated node(s):** `Normalize MCP call return that may still wrap result.`
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 12`** (2 nodes): `job01_place_layout.py`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 13`** (2 nodes): `job01_fix_rels.py`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (2 nodes): `job01_build.py`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (1 nodes): `job05_finalize_reports.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (1 nodes): `check_release.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `main()` connect `Community 0` to `Community 10`, `Community 2`, `Community 11`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Why does `pick_id()` connect `Community 11` to `Community 0`, `Community 2`, `Community 10`, `Community 12`, `Community 13`, `Community 14`?**
  _High betweenness centrality (0.012) - this node is a cross-community bridge._
- **Why does `MCP` connect `Community 0` to `Community 2`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `pick_id()` (e.g. with `main()` and `main()`) actually correct?**
  _`pick_id()` has 10 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Normalize MCP call return that may still wrap result.` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._