
# Project Stardust tooltip stripper

Simple regex script to change hyperlinks from miraheze to the appropriate tooltip infobox.

Example input:
```
| spinals = 1x [[Rebel Quad Heavy Ion Cannon]]
| missiles = 8x [[Concussion Missile]]
| lasers = 6x [[Rebel Small Cannon Hybrid]]
<li> 6x [[Rebel Large Turbolaser]]
<li> 6x [[Rebel Medium Turbolaser]]
<li> 8x [[Rebel Medium Ion Cannon]]
<li> 6x [[Rebel Heavy Ion Cannon]]
```

Example output:
```
| spinals = 1x {{Tooltip|Rebel Quad Heavy Ion Cannon|{{LaserInfobox|Rebel Quad Heavy Ion Cannon}}}}
| missiles = 8x {{Tooltip|Concussion Missile|{{MissileInfobox|Concussion Missile}}}}
| lasers = 6x {{Tooltip|Rebel Small Cannon Hybrid|{{LaserInfobox|Rebel Small Cannon Hybrid}}}}
<li> 6x {{Tooltip|Rebel Large Turbolaser|{{LaserInfobox|Rebel Large Turbolaser}}}}
<li> 6x {{Tooltip|Rebel Medium Turbolaser|{{LaserInfobox|Rebel Medium Turbolaser}}}}
<li> 8x {{Tooltip|Rebel Medium Ion Cannon|{{LaserInfobox|Rebel Medium Ion Cannon}}}}
<li> 6x {{Tooltip|Rebel Heavy Ion Cannon|{{LaserInfobox|Rebel Heavy Ion Cannon}}}}
```

## Getting Started


### Dependencies

* Python
  

### Usage

* Download main.py
* Open your terminal application
* Navigate to the directory
* Start the script with
```
python main.py
```
* Place your input in the top box
* Press 'convert'
* Copy your output in the bottom box
* Press 'clear' to wipe both boxes
  

## Authors

Erb

  


## See Also

* [Game](https://www.roblox.com/games/2394257515/Project-Stardust)

* [Wiki](https://projectstardustwiki.miraheze.org/wiki/Main_Page)
