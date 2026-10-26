import json, pathlib
p=pathlib.Path(__file__).resolve().parents[1]/"workflow.json"
d=json.loads(p.read_text(encoding="utf-8")); nodes={n["id"]:n for n in d["nodes"]}
assert len(nodes)==len(d["nodes"]), "Duplicate node IDs"
ids=set()
for lid,a,ao,b,bi,kind in d["links"]:
 assert lid not in ids, f"Duplicate link {lid}"
 ids.add(lid)
 assert a in nodes and b in nodes, f"Missing endpoint {lid}"
 assert lid in (nodes[a]["outputs"][ao].get("links") or []), f"Output mismatch {lid}"
 assert nodes[b]["inputs"][bi].get("link")==lid, f"Input mismatch {lid}"
for n in nodes.values():
 for inp in n.get("inputs",[]):
  assert inp.get("link") is None or inp["link"] in ids, "Dangling input"
 for output in n.get("outputs",[]):
  assert all(x in ids for x in (output.get("links") or [])), "Dangling output"
print(f"PASS: {len(nodes)} nodes; {len(ids)} links. Structural validation only; GPU execution not tested.")
