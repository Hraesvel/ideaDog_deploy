plan webserver::arangodb (
  TargetSpec $nodes,
  String $password = 'root',
  String $storage = 'rocksdb'
){
  run_task(webserver::install_arangodb, $nodes, _run_as => root, password => $password, storage => $storage)
  run_task(webserver::add_graph, $nodes)
}
