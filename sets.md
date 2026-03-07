
# Mindstorms EV3

Link to [Pybricks EV3 Examples for mindstorms-ev3](
https://github.com/pybricks/pybricks-projects/blob/master/sets/mindstorms-ev3/)

1. Some projects have a program rc_tank_util.py that is included, they are not **all** the same.
    - Hard to do that in pybricks-UI.
2. breaking changes:
    - import from  ```pybricks.media.ev3dev``` is now ```pybricks.parameters```
      - In the stable version this will to be compatible again.

---

## Compatibility

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

---

## Table with links to Building instructions and Pybricks programs
| **model** | **Building instructions** | **Program** |
| :--- | :--- | :--- |
| home-main | [set 31313 all models](https://www.lego.com/en-us/service/building-instructions/31313) | |
| - everstorm | [everstorm](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EV3RSTORM.pdf) | [everstorm](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-main/ev3rstorm) |
| - gripp3r | [gripper](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_GRIPP3R.pdf) | [gripp3r](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-main/gripp3r) |
| - r3ptar | [r3ptar](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_R3PTAR.pdf) | [r3ptar](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-main/r3ptar) |
| - spik3r | [spik3r](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_SPIK3R.pdf) | [spik3r](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-main/spik3r) |
| - track3r_base | [track3r all models](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_TRACK3R.pdf) | [track3r_base](https://github.com/pybricks/pybricks-projects/blob/master/sets/mindstorms-ev3/home-main/track3r/track3r_base.py) |	
| - track3r with biblade_spinner | see track3r_base | [track3r with biblade_spinner](https://github.com/pybricks/pybricks-projects/blob/master/sets/mindstorms-ev3/home-main/track3r/track3r_with_biblade_spinner.py) |	
| - track3r with blasting_bazooka | see track3r_base | [track3r with blasting_bazooka](https://github.com/pybricks/pybricks-projects/blob/master/sets/mindstorms-ev3/home-main/track3r/track3r_with_blasting_bazooka.py) |
| - track3r with gripping_claw | see track3r_base | [track3r with gripping_claw](https://github.com/pybricks/pybricks-projects/blob/master/sets/mindstorms-ev3/home-main/track3r/track3r_with_gripping_claw.py) |
| - track3r with heavy_hammer | see track3r_base | [track3r with heavy_hammer](https://github.com/pybricks/pybricks-projects/blob/master/sets/mindstorms-ev3/home-main/track3r/track3r_with_heavy_hammer.py) |
|   |
| **Home bonus** | [set 31313 all models](https://www.lego.com/en-us/service/building-instructions/31313) |  
| - bobb3e           | [bobb3e](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_BOBB3E.pdf) | [bobbo3e](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/bobb3e) |
| - dinor3x          | [dinor3x](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_DINOREX.pdf) | [dinor3x](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/dinor3x) |
| - e13ctric-guitar  | [e13ctric-guitar](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EL3CTRIC%20GUITAR.pdf) | [e13ctric-guitar](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/el3ctric-guitar) |
| - ev3_d4           | [ev3_d4](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EV3D4.pdf) | [ev3_d4](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/ev3-d4) |
| - ev3-game         | [ev3 game](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_EV3%20GAME.pdf) | [ev3 game](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/ev3-game) |
| - kraz3 | [kraz3](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_KRAZ3.pdf) | [kraz3](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/kraz3) |
| - mr-b3am          | [mr-b3am](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_MR%20B3AM.pdf) | [mr b3am](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/mr-b3am) |
| - rac3-truck       | [rac3-truck](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_RAC3%20TRUCK.pdf) | [rac3-truck](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/rac3-truck) |
| - robodoz3r        | [robodoz3r](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_ROBODOZ3R.pdf) | [robodoz3r](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/robodoz3r) |
| - wack3m           | [wack3m](https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_WACK3M.pdf) | [wack3m](https://github.com/pybricks/pybricks-projects/tree/master/sets/mindstorms-ev3/home-bonus/wack3m) |
|   |
| **Robot Educator Programs** | [robot_educator](https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot) |
| - Basic Movement |  | [robot_educator_basic](https://pybricks.com/ev3-micropython/examples/robot_educator_basic.html) |
| - Obstacle Avoidance | | [robot_educator_obstacle avoidance](https://pybricks.com/ev3-micropython/examples/robot_educator_ultrasonic.html) |
| - Line Following |  | [robot_educator_line following](https://pybricks.com/ev3-micropython/examples/robot_educator_line.html) |
|   |
| **Core Set Programs** | [Core sets](https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-core) |
| - Color Sorter | | [Color sorter](https://pybricks.com/ev3-micropython/examples/color_sorter.html) |
| - Robot Arm H25 | | [Robot arm H25](https://pybricks.com/ev3-micropython/examples/robot_arm.html) |
| - Puppy | | [Pyppy](https://pybricks.com/ev3-micropython/examples/puppy.html) |
| - Gyro Boy | | [Gyro boy](https://pybricks.com/ev3-micropython/examples/gyro_boy.html) |
|   |
|   |
| **Expansion Set Programs** | [Expansion Set](https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-expansion) |
| Elephant | | [Elephant](https://pybricks.com/ev3-micropython/examples/elephant.html) |
| Stair Climber | | [Stair climber](https://pybricks.com/ev3-micropython/examples/stair_climber.html) |
| Tank Bot | | [Tank bot](https://pybricks.com/ev3-micropython/examples/tank_bot.html) |
| Znap | | [Znap](https://pybricks.com/ev3-micropython/examples/znap.html) |

---

### updates:
`initial    BL` 
- Checked against the beta version V4.0.0.b6

`2026-02-26 BL` 
- Check against version ```('ev3', '4.0.0b6', 'ci-build-4741-v4.0.0b6-6-g368c02cc on 2026-02-23')```

`2026-02-26 BL`
- Check against version ```('ev3', '4.0.0b7', 'ci-build-4755-v4.0.0b7 on 2026-02-26')```

`2026-03-03 BL` 
- Update rac3_truck compatibility

`2026-03-07 BL` 
- add table with links to building instructions and pybricks V2 programs

