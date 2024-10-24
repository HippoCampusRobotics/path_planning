^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package path_planning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.3 (2024-10-21)
------------------
* make logging more unambiguous
* fixed indentation
* added generation script for rectangle
* Contributors: Thies Lennart Alff

1.0.2 (2024-09-23)
------------------
* added script to convert pathes from yaml to csv for easy plotting in
  latex
* added README
* Contributors: Thies Lennart Alff

1.0.1 (2024-07-17)
------------------
* added missing ament_index_cpp dependency
* Contributors: Thies Lennart Alff

* added missing ament_index_cpp dependency
* Contributors: Thies Lennart Alff

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
