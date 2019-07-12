plan webserver (
  TargetSpec $nodes,
) {
  run_command("touch hello", $nodes, '_catch_errors' => true )
}
