# WorkAdventure Map for Das-Labor

A map for [WorkAdventure](https://workadventu.re) showing 
[Das Labor](https://das-labor.org) in Bochum.


https://virtuallab.das-labor.org/

## EG

![Bild](main.png)

## UG

![Bild](basement.png)


## Tools you will need

In order to build your own map for WorkAdventure, you need:

- the [Tiled editor](https://www.mapeditor.org/) software
- "tiles" (i.e. images) to create your map (this starter kit provides a good default tileset for offices)

## Customizing the map

You find the main map in `main.json`. You can open and edit
it with the [Tiled](https://www.mapeditor.org/) editor.

After push it will be deployed to branch `gh-pages` and made available to
github pages.

The page leading to the workadventure-room is
https://das-labor.github.io/workadv_das-labor/

Feel free to make pull requests.

### About WorkAdventu.re maps

In order to design a map that will be readable by WorkAdventure, you will have to respect some constraints.

In particular, you will need to:

- set a start position for the players
- configure the "floor layer" (so that WorkAdventure can correctly display characters above the floor, but under the ceiling)
- eventually, you can place exits that link to other maps

All this is described in the [WorkAdventure documentation](https://workadventu.re/create-map.html#about-workadventu-re-maps).
Please be sure to check it out. 

## Jitsi-Room

Each conference room area links to a jitsi room that can be accessed via
`https://jitsi.binary-kitchen.de/$ROOM` where `$ROOM` is the room name used
in the `jitsiRoom` layer property. The script 
[jitsiRooms.py](util/jitsiRooms.py) can be used
to retreive rooms and theirs corresponding jitis room URLs.

## Metrics

The pusher provides metrics of an instance under `/metrics` - e.g.
https://pusher.wa.binary-kitchen.de/metrics or 
https://pusher.kraut.world/metrics or 
https://pusher.workadventu.re/metrics

## Related Links

- [rc world link](https://links.rc3.world/)
- [rc3 map urls](https://gist.github.com/MichaelKreil/e967f4b91b3c147fc8b414f88bde9dae)
- [map validator](https://github.com/tiefpunkt/rc3-world-map-validator)
- [chaos-world entrance](https://play.wa.binary-kitchen.de/_/global/c0c0bird.github.io/chaos-world/main.json)
- [chaos-world repo](https://github.com/c0c0bird/chaos-world)
- fediventure: [repo](https://gitlab.com/fediventure/fediventure), [pad](https://pad.inf.re/p/fediventure)
- [rc3 overview](https://miro.com/app/board/o9J_laWLPI8=/)
- [rc3 World dump](https://github.com/rC3XBill/rC3World)
- [rc3 world images](https://archive.org/details/rc3_complete/)
- [tilesets](https://opengameart.org/content/terrain-transitions)

## Credit

- Backgroundsound: [Dave of defeat](https://freesound.org/people/DaveOfDefeat2248/sounds/323090/)
- Dripping sound in basement [antwerpsoundesign](https://freesound.org/people/antwerpsounddesign/sounds/547253/)


