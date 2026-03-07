### updates:
`initial    BL` Checked against the beta version V4.0.0.b6

`2026-02-26 BL` Check against version
  ```('ev3', '4.0.0b6', 'ci-build-4741-v4.0.0b6-6-g368c02cc on 2026-02-23')```

`2026-02-26 BL` Check against version
  ```('ev3', '4.0.0b7', 'ci-build-4755-v4.0.0b7 on 2026-02-26')```

`2026-03-03 BL` Update rac3_truck compatibility

`2026-03-07 BL` add urls for Robot Educator Programs (not core sets)


## Mindstorms EV3

[EV3 Example sets from mindstorms-ev3](
https://github.com/pybricks/pybricks-projects/blob/master/sets/mindstorms-ev3/)

1. Some projects have a program rc_tank_util.py that is included they are not **all** the same.
Hard to do that in pybricks-UI.
2. breaking changes:
    - import from  ```pybricks.media.ev3dev``` is now ```pybricks.parameters```


| **Group**           | **Model**         | **Pybricks V4 compatible** | **Missing** |
|:--------------------|:------------------|:-----------------------|:---------|
| education-core      | color sorter      |                         | ~~ImageFile,~~ SoundFile |
|                     | gyro_boy          |                         |  ~~ucollections,  ImageFile,~~ SoundFile      |
|                     | puppy             |                         | ~~media~~ SoundFile        |
|                     | robot arm         | YES                    |          |
|                     | robot educator basic| Yes, but not built   |          |
|                     | robot educator line| Yes, but not built    |          |
|                     | robot educator ultrasonic| Yes, but not built  |          |
 |  |  |  |  |
 | education-expansion | elephant          |                         | SoundFile |
 |                     | stair climber     |                         | ~~Font,~~ SoundFile        |
 |                     | tank bot          | No syntax error, needs build test | ~~ImageFile~~     |
 |                     | znap              |                         |  SoundFile    |
 |  |  |  |  |
 | home-bonus          | bobb3e           |                         | SoundFile  |
 |                     | dinor3x          |                         | SoundFile  |
 |                     | e13ctric-guitar  | No syntax error, needs build test | ~~ImageFile~~  |
 |                     | ev3_d4           |                         | threading, SoundFile |
 |                     | ev3-game         |                         | SoundFile |
 |                     | kraz3            |                         | run_parallel, SoundFile |
 |                     | mr-b3am          |                         | SoundFile  |
 |                     | rac3-truck       | YES, only need to adapt settings of the steering calibration depending on type of floor |          |
 |                     | robodoz3r        |                         |  SoundFile, play_file, time |
 |                     | wack3m           |                         | ~~ImageFile,~~ SoundFile, time     |
 |  |  |  |  |
| home-main | ev3rstorm  |                         | SoundFile ~~,ImageFile~~ |
|           | gripp3r |                         |   SoundFile |
|           | r3ptar    |                         |  SoundFile |
|           | spik3r    |                         | ~~ImageFile,~~ SoundFile    |
|           | track3r_base   |  No syntax error, is imported    |          |
|           | track3r with biblade_spinner | Needs build     |          |
|           | track3r with blasting_bazooka   | Needs build  | ~~ImageFile,~~ SoundFile    |
|           | track3r with gripping_claw   | Needs build | SoundFile   |
|           | track3r with heavy_hammer   | Needs build     |  ~~ImageFile,~~ SoundFile  |


| **model** | **Building instructions** | **Program** |
| :--- | :--- | :--- |
| everstorm | ? | ? |
| | **Robot Educator Programs** |
| Basic Movement | [robot_educator_basic](https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot) | [robot_educator_basic](https://pybricks.com/ev3-micropython/examples/robot_educator_basic.html) |
| Obstacle Avoidance | [robot_educator_obsticle avoidance](https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot) | [robot_educator_obsticle avoidance](https://pybricks.com/ev3-micropython/examples/robot_educator_ultrasonic.html) |
| Line Following | [robot_educator_line following](https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot) | [robot_educator_line following](https://pybricks.com/ev3-micropython/examples/robot_educator_line.html) |
| | **Core Set Programs** |
| Color Sorter | ? | ? |
| Robot Arm H25 | ? | ? |
| Puppy | ? | ? |
| Gyro Boy | ? | ? |
| | **Expansion Set Programs** |
| Elephant | ? | ? |
| Stair Climber | ? | ? |
| Tank Bot | ? | ? |
| Znap | ? | ? |
