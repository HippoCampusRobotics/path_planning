^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package path_planning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.0 (2024-07-16)
------------------
* moved to separate repo
* ditched yapf
* added circular path
* finer sampling of small bernoulli path
* added paramter for number of waypoints to generate
* added small bernoulli path
* getter for loop flag
* switch back to the normal path follower.
  maybe reimplement the motor failure mode in the future?
* the normal default look ahead distance
* make lemniscate a lemniscate again
* fixed unused variables
* renamed PassLaunchArguments to something more descriptive
* added pre-commit hooks
* fixed formatting errors after latest merge
* snapshot for paper
* generation for motor failure control path added
* added support for different path following modes and a service to start them
* added initial support different path following modes
* hard-coded axis-follower. Probably to be reverted later on
* added licenses and applied formatting to all source files
* added visualization for path follower
* added path_follower
* added path visualizer and thrust subscription
* added params to carrot control and launch files
* path planning package added
* Contributors: Thies Lennart Alff
