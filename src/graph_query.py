def find_nodes_with_pattern(graph_def, pattern):
  node_matches = []
  for n in graph_def.node:
    m = pattern.match(n.name)
    if m:
      node_matches.append((n, m))

  if len(node_matches) == 0:
    raise Exception("No nodes match pattern %s" % pattern)

  return node_matches

def find_results(graph_def, result_pattern):
  node_matches = find_nodes_with_pattern(graph_def, result_pattern)
  ops = [n.name + ":0" for n, m in node_matches]
  result_names = [m.group(1) for n, m in node_matches]

  return (result_names, ops)
